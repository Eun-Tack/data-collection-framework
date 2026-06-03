#!/usr/bin/env python3
"""
score_manifest.py — manifest CSV에 IG(정보이득) 정량 점수를 부여하는 후처리 어댑터.

P3(vetting-analyst)의 정성 신뢰도(A/B/C/D)를 보강하는 결정적 점수.
vendored REM(knowledgentropy.IGScorer, stdlib 의존성 0)을 사용한다.

입력 : manifest CSV (dc:CollectedItem 고정 컬럼; 통상 phase2_collect/manifest_raw.csv)
출력 : <입력>_scored.csv 또는 --out 지정 (통상 phase3_vet/manifest_vetted.csv)
        원본 컬럼 + ig_score, ig_base, aer, stability, trust, trust_tier,
        freshness, ig_passed, trust_grade_check

사용:
    python framework/tools/score_manifest.py <manifest.csv> \
        [--threshold 0.35] [--out PATH] [--as-of YYYY-MM-DD] \
        [--fail-on-review] [--json-summary]

옵션:
    --as-of YYYY-MM-DD : freshness 계산 기준일 고정(재현성). 미지정 시 오늘.
    --fail-on-review   : trust_grade_check 불일치가 1건 이상이면 exit 2 (CI/게이트용).
    --json-summary     : 마지막에 요약을 JSON 한 줄로 출력.

freshness = clamp(1 - 경과연수/4, 0, 1)  (pub_date: YYYY / YYYY-MM / YYYY-MM-DD)
점수 텍스트: title + publisher + reliability_reason
무설치: Python 표준 라이브러리만 사용.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from datetime import date

# vendored REM 패키지 경로 등록
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from knowledgentropy import IGScorer  # noqa: E402

# 어댑터 보정: 원본 scorer는 다단계 TLD(.go.kr/.ac.kr)를 단일 세그먼트(.kr)로만
# 인식해 한국 정부·학술 기관을 MID로 떨어뜨린다. 글로벌+한국어 목적에 맞게 보정.
_KO_HIGH_SUFFIXES = (".go.kr", ".ac.kr", ".re.kr")
_IG_OMEGA = (0.45, 0.35, 0.20)  # 원본 IGConfig 기본 (AER, Stab, Trust)


def _domain_of(url: str) -> str:
    from urllib.parse import urlparse
    try:
        return urlparse(url).netloc.lower().lstrip("www.")
    except Exception:
        return ""


def freshness_from_pub_date(pub_date: str, ref_date: date) -> float:
    """pub_date → freshness [0,1]. 미상이면 0.5. ref_date 기준(재현성)."""
    if not pub_date:
        return 0.5
    parts = pub_date.strip().split("-")
    try:
        year = int(parts[0])
        month = int(parts[1]) if len(parts) > 1 else 6
    except (ValueError, IndexError):
        return 0.5
    age_years = (ref_date.year - year) + (ref_date.month - month) / 12.0
    return round(max(0.0, min(1.0, 1.0 - age_years / 4.0)), 4)


def trust_tier(trust: float) -> str:
    if trust >= 0.85:
        return "HIGH"
    if trust <= 0.30:
        return "LOW"
    return "MID"


def grade_check(reliability: str, tier: str) -> str:
    """수동 등급(A/B/C/D)과 도메인 Trust 등급의 정합성 교차검증."""
    g = (reliability or "").strip().upper()
    if g in ("A", "B") and tier == "LOW":
        return "review: grade>=B but LOW-trust domain"
    if g in ("C", "D") and tier == "HIGH":
        return "review: HIGH-trust domain but grade<=C (승급 검토)"
    return "ok"


def main() -> int:
    ap = argparse.ArgumentParser(description="manifest CSV에 IG 점수 부여")
    ap.add_argument("manifest", help="입력 manifest CSV 경로")
    ap.add_argument("--threshold", type=float, default=0.35, help="IG 합격 임계값 (기본 0.35)")
    ap.add_argument("--out", default=None, help="출력 경로 (기본: <입력>_scored.csv)")
    ap.add_argument("--as-of", default=None, help="freshness 기준일 YYYY-MM-DD (재현성). 미지정 시 오늘")
    ap.add_argument("--fail-on-review", action="store_true",
                    help="trust_grade_check 불일치 ≥1건이면 exit 2")
    ap.add_argument("--json-summary", action="store_true", help="요약을 JSON 한 줄로 출력")
    args = ap.parse_args()

    if not os.path.exists(args.manifest):
        print(f"[오류] 파일 없음: {args.manifest}", file=sys.stderr)
        return 1
    try:
        ref_date = date.fromisoformat(args.as_of) if args.as_of else date.today()
    except ValueError:
        print(f"[오류] --as-of 형식은 YYYY-MM-DD: {args.as_of}", file=sys.stderr)
        return 1

    out_path = args.out or os.path.splitext(args.manifest)[0] + "_scored.csv"
    scorer = IGScorer(threshold=args.threshold)

    with open(args.manifest, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        print("[오류] 빈 manifest", file=sys.stderr)
        return 1

    extra = ["ig_score", "ig_base", "aer", "stability", "trust",
             "trust_tier", "freshness", "ig_passed", "trust_grade_check"]
    fieldnames = list(rows[0].keys()) + [c for c in extra if c not in rows[0]]

    n_pass = 0
    n_flag = 0
    for r in rows:
        text = " ".join(filter(None, [r.get("title", ""), r.get("publisher", ""),
                                       r.get("reliability_reason", "")]))
        fresh = freshness_from_pub_date(r.get("pub_date", ""), ref_date)
        res = scorer.score(text, source_url=r.get("url", ""), freshness=fresh)

        # 한국 정부·학술 기관 TLD 보정 (원본 미인식분)
        trust = res.trust_score
        ig_base = res.ig_base
        ig_final = res.ig_score
        passed = res.passed
        domain = _domain_of(r.get("url", ""))
        if trust < 0.90 and domain.endswith(_KO_HIGH_SUFFIXES):
            trust = 0.90
            wa, ws, wt = _IG_OMEGA
            ig_base = round(wa * res.aer_score + ws * res.stability_score + wt * trust, 4)
            ig_final = round(ig_base * (0.5 + 0.5 * fresh), 4)
            passed = ig_final >= args.threshold

        tier = trust_tier(trust)
        chk = grade_check(r.get("reliability", ""), tier)
        r.update({
            "ig_score": ig_final, "ig_base": ig_base, "aer": res.aer_score,
            "stability": res.stability_score, "trust": trust,
            "trust_tier": tier, "freshness": res.freshness,
            "ig_passed": passed, "trust_grade_check": chk,
        })
        n_pass += int(passed)
        n_flag += int(chk != "ok")

    with open(out_path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

    summary = {
        "items": len(rows), "ig_passed": n_pass, "threshold": args.threshold,
        "review_flags": n_flag, "as_of": ref_date.isoformat(), "out": out_path,
    }
    if args.json_summary:
        print(json.dumps(summary, ensure_ascii=False))
    else:
        print(f"[done] {len(rows)} scored -> {out_path}")
        print(f"  IG passed (threshold={args.threshold}): {n_pass}/{len(rows)}")
        print(f"  trust-grade review flags: {n_flag}  (as-of {ref_date.isoformat()})")

    if args.fail_on_review and n_flag > 0:
        print(f"[FAIL] {n_flag} trust-grade review flag(s) — 검토 필요", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
