# manifest.csv 컬럼 규격 (고정)

P4에서 생성하는 `manifest.csv`는 아래 컬럼 순서를 고정한다. (스키마: `../../ontology/FRONTMATTER.schema.md` §2.8)

```csv
id,track,title,authors,source_type,url,publisher,pub_date,retrieved_date,lang,reliability,reliability_reason,dedup_key,related_ids
```

규칙:
- 본문 카탈로그(`00_Catalog.md`) 항목 수 = CSV 행 수 (O-CT-02).
- `abstract`·`key_points`는 길어서 CSV 제외 — 카탈로그 본문에 둔다.
- 빈 값은 비워두지 말고 `[검증 필요]`·`[자료 공백]` 등으로 명시.

예시 행:
```csv
ITM-A01,academic,"Self-RAG",Asai et al.,paper,https://arxiv.org/abs/2310.11511,ICLR 2024,2023-10-17,2026-06-02,en,A,"ICLR peer-reviewed",10.48550/arXiv.2310.11511,
```

## 정량 점수 확장 (선택, P3) — `manifest_scored.csv`

`framework/tools/score_manifest.py`로 위 manifest에 REM IG 점수를 부여하면 아래 컬럼이 추가된 `manifest_scored.csv`가 생성된다.

```
ig_score, ig_base, aer, stability, trust, trust_tier, freshness, ig_passed, trust_grade_check
```
- `trust`: 도메인 신뢰도(HIGH 0.90 / MID 0.55 / LOW 0.25). `.go.kr`/`.ac.kr`/`.re.kr` 보정 포함.
- `ig_passed`: `ig_score >= threshold`(기본 0.35).
- `trust_grade_check`: 수동 등급(reliability)과 도메인 Trust 등급의 정합성. 불일치 시 "review: ..." → 승급/강등 검토.

실행:
```bash
python framework/tools/score_manifest.py projects/<주제>/phase4_catalog/manifest.csv
```
