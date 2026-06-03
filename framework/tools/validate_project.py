#!/usr/bin/env python3
"""
validate_project.py — 수집 프로젝트 게이트 자동 판정기.

dc: 온톨로지·메타스키마 규약을 한 번에 검사해 Phase Gate를 '실제로 실패'시킨다.
지시문(문서)만으로 강제하던 규칙을 실행 가능한 검증으로 승격.

검사 항목:
  [구조]   COLLECTION_SPEC.md 존재 + frontmatter(type/id/status)
  [추적성] phaseN 산출물(frontmatter 보유)에 traces_to=CSPEC 포함
  [매니페스트] CSV 헤더가 정규 14컬럼으로 시작 / 필수 필드 비어있지 않음 /
            url이 http(s) / id 유일 / dedup_key 충돌(미병합) 없음
  [일치]   Catalog frontmatter item_count == manifest 행 수
  [선택]   --check-links : 각 url에 HEAD 요청(네트워크)

사용:
    python framework/tools/validate_project.py projects/<주제> \
        [--check-links] [--json-summary]
종료코드: 0=통과(경고 가능), 1=오류(게이트 실패), 2=프로젝트 없음.
무설치: Python 표준 라이브러리만 사용.
"""
from __future__ import annotations

import argparse
import csv
import glob
import json
import os
import re
import sys

CANONICAL_COLUMNS = [
    "id", "track", "title", "authors", "source_type", "url", "publisher",
    "pub_date", "retrieved_date", "lang", "reliability", "reliability_reason",
    "dedup_key", "related_ids",
]
REQUIRED_NONEMPTY = [
    "id", "track", "title", "source_type", "url", "pub_date",
    "retrieved_date", "lang", "reliability", "dedup_key",
]


def parse_frontmatter(path: str) -> dict | None:
    """파일 상단 --- ... --- 블록을 단순 key:value 로 파싱. 없으면 None."""
    try:
        with open(path, encoding="utf-8-sig") as f:
            text = f.read()
    except OSError:
        return None
    if not text.lstrip().startswith("---"):
        return None
    body = text.lstrip()[3:]
    end = body.find("\n---")
    if end == -1:
        return None
    fm = {}
    for line in body[:end].splitlines():
        m = re.match(r"^([A-Za-z_][\w]*)\s*:\s*(.*)$", line)
        if m:
            fm[m.group(1)] = m.group(2).strip()
    return fm


def parse_list_field(raw: str) -> list[str]:
    """frontmatter 리스트 필드 '[a, b]' 또는 'a, b' → [a, b] (소문자·trim)."""
    if not raw:
        return []
    raw = raw.strip()
    if raw.startswith("[") and raw.endswith("]"):
        raw = raw[1:-1]
    out = []
    for tok in raw.split(","):
        t = tok.strip().strip('"').strip("'").lower()
        if t:
            out.append(t)
    return out


def find_manifest(project: str) -> str | None:
    for rel in ("phase4_catalog/manifest.csv", "phase3_vet/manifest_vetted.csv",
                "phase2_collect/manifest_raw.csv"):
        p = os.path.join(project, rel)
        if os.path.exists(p):
            return p
    hits = glob.glob(os.path.join(project, "**", "manifest*.csv"), recursive=True)
    hits = [h for h in hits if "_scored" not in os.path.basename(h)]
    return hits[0] if hits else None


def main() -> int:
    ap = argparse.ArgumentParser(description="수집 프로젝트 게이트 검증")
    ap.add_argument("project", help="projects/<주제> 경로")
    ap.add_argument("--check-links", action="store_true", help="각 url HEAD 요청(네트워크)")
    ap.add_argument("--json-summary", action="store_true")
    args = ap.parse_args()

    if not os.path.isdir(args.project):
        print(f"[오류] 프로젝트 디렉터리 없음: {args.project}", file=sys.stderr)
        return 2

    errors: list[str] = []
    warns: list[str] = []

    # 1) Collection Spec
    spec_path = os.path.join(args.project, "COLLECTION_SPEC.md")
    cspec_id = None
    spec_fm: dict = {}
    if not os.path.exists(spec_path):
        errors.append("COLLECTION_SPEC.md 없음")
    else:
        spec_fm = parse_frontmatter(spec_path) or {}
        if spec_fm.get("type") != "dc:CollectionSpec":
            errors.append("COLLECTION_SPEC.md: type != dc:CollectionSpec")
        for k in ("id", "status"):
            if not spec_fm.get(k):
                errors.append(f"COLLECTION_SPEC.md: {k} 누락")
        cspec_id = spec_fm.get("id")

    # 2) phaseN 산출물 traces_to
    for md in glob.glob(os.path.join(args.project, "phase*", "**", "*.md"), recursive=True):
        fm = parse_frontmatter(md)
        if not fm:
            continue  # frontmatter 없는 본문(트랙 collection 등)은 스킵
        rel = os.path.relpath(md, args.project)
        for k in ("type", "id", "status"):
            if not fm.get(k):
                errors.append(f"{rel}: frontmatter {k} 누락")
        if "traces_to" not in fm or "CSPEC" not in fm.get("traces_to", ""):
            errors.append(f"{rel}: traces_to(CSPEC) 누락")

    # 3) manifest
    manifest = find_manifest(args.project)
    n_rows = 0
    if not manifest:
        warns.append("manifest CSV 없음 (P2 이후 산출 예정이면 정상)")
    else:
        rel = os.path.relpath(manifest, args.project)
        with open(manifest, encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            header = reader.fieldnames or []
            rows = list(reader)
        n_rows = len(rows)
        if header[:len(CANONICAL_COLUMNS)] != CANONICAL_COLUMNS:
            errors.append(f"{rel}: 헤더가 정규 14컬럼으로 시작하지 않음")
        seen_id, seen_dedup = set(), {}
        for i, r in enumerate(rows, 1):
            for c in REQUIRED_NONEMPTY:
                if not (r.get(c) or "").strip():
                    errors.append(f"{rel}#{i}({r.get('id','?')}): 필수 '{c}' 비어있음")
            url = (r.get("url") or "").strip()
            if url and not re.match(r"^https?://", url):
                errors.append(f"{rel}#{i}({r.get('id','?')}): url 형식 비정상 '{url[:40]}'")
            rid = (r.get("id") or "").strip()
            if rid in seen_id:
                errors.append(f"{rel}: id 중복 '{rid}'")
            seen_id.add(rid)
            dk = (r.get("dedup_key") or "").strip()
            if dk:
                seen_dedup.setdefault(dk, []).append(rid)
        for dk, ids in seen_dedup.items():
            if len(ids) > 1:
                errors.append(f"{rel}: dedup_key 충돌(미병합) '{dk}' -> {ids}")

        # --- 가이드라인 하드 제약 (Collection Spec frontmatter) ---
        from urllib.parse import urlparse
        banned = parse_list_field(spec_fm.get("banned_sources", ""))
        excludes = parse_list_field(spec_fm.get("must_exclude", ""))
        for i, r in enumerate(rows, 1):
            rid = r.get("id", "?")
            url = (r.get("url") or "").strip()
            dom = urlparse(url).netloc.lower().lstrip("www.") if url else ""
            if dom and any(dom == b or dom.endswith("." + b) for b in banned):
                errors.append(f"{rel}#{i}({rid}): 금지 소스 도메인 '{dom}' (banned_sources)")
            title = (r.get("title") or "").lower()
            for ex in excludes:
                if ex and ex in title and not ex.startswith("{"):
                    errors.append(f"{rel}#{i}({rid}): 제외 주제 '{ex}' 제목 매칭 (must_exclude)")
        try:
            min_ab = float(spec_fm.get("min_ab_ratio", "") or 0)
        except ValueError:
            min_ab = 0.0
        if min_ab > 0 and rows:
            ab = sum(1 for r in rows if (r.get("reliability") or "").strip().upper() in ("A", "B"))
            ratio = ab / len(rows)
            if ratio < min_ab:
                errors.append(f"{rel}: A/B 비율 {ratio:.2f} < min_ab_ratio {min_ab} (품질바 미달)")

        if args.check_links:
            import urllib.request
            for r in rows:
                url = (r.get("url") or "").strip()
                if not re.match(r"^https?://", url):
                    continue
                try:
                    req = urllib.request.Request(url, method="HEAD",
                                                 headers={"User-Agent": "dc-validate/1.0"})
                    urllib.request.urlopen(req, timeout=10)
                except Exception as e:  # noqa: BLE001
                    warns.append(f"링크 점검 실패 {r.get('id','?')}: {url[:50]} ({type(e).__name__})")

    # 4) Catalog item_count == manifest 행 수
    cat = os.path.join(args.project, "phase4_catalog", "00_Catalog.md")
    if os.path.exists(cat):
        fm = parse_frontmatter(cat) or {}
        ic = fm.get("item_count")
        if ic and ic.isdigit() and manifest and int(ic) != n_rows:
            errors.append(f"Catalog item_count({ic}) != manifest 행수({n_rows})")

    summary = {
        "project": args.project, "cspec": cspec_id, "manifest_rows": n_rows,
        "errors": len(errors), "warnings": len(warns),
        "passed": len(errors) == 0,
    }
    if args.json_summary:
        print(json.dumps(summary, ensure_ascii=False))
    else:
        for e in errors:
            print(f"  [ERROR] {e}")
        for w in warns:
            print(f"  [warn ] {w}")
        verdict = "PASS" if not errors else "FAIL"
        print(f"[{verdict}] {args.project}  errors={len(errors)} warnings={len(warns)} rows={n_rows}")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
