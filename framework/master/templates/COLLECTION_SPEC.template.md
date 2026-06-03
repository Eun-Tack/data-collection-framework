---
type: dc:CollectionSpec
id: CSPEC-{주제약자}
name: {주제} 자료 수집 명세
status: Draft
created_at: {YYYY-MM-DD}
owner: {사용자}
active_tracks: [TRK-academic, TRK-report, TRK-web-news, TRK-code-data, TRK-korea]
success_criteria: "{예: 총 25건 이상, 트랙별 A/B 등급 ≥ 50%}"
seed_queries: ["{시드 쿼리1}", "{시드 쿼리2}"]
# ── Intent·Guidelines (P0a intake가 채움 — validate_project가 하드 제약으로 강제) ──
languages: [en, ko]
region: global
must_include: ["{핵심 주제}"]
must_exclude: ["{제외 주제}"]
preferred_sources: ["arxiv.org"]
banned_sources: ["reddit.com"]
min_ab_ratio: 0.5
deadline: "{YYYY-MM-DD}"
glossary: ["{용어=정의}"]
---

# {주제} 자료 수집 명세 (Collection Spec)

> SSOT — 수집 범위·트랙·성공기준은 이 문서에서만 변경. 파생물은 `traces_to: [CSPEC-{주제약자}]`.

## 1. 수집 목적
{왜 모으는가 / 이 자료로 무엇을 할 것인가}

## 2. 범위 (Scope)
- 포함: {주제·하위주제}
- 제외: {범위 밖}
- 기간: {예: 2023-01 ~ 현재}
- 언어: **en + ko** (기본값 — 이중 쿼리)
- 지역: **global** (기본값 — 국제 자료 우선, 단일 지역 한정 금지)

## 3. 활성 트랙
| 트랙 | 활성 | 사유 | 목표 건수 |
|------|------|------|----------|
| TRK-academic | ✅/❌ | {사유} | {N} |
| TRK-report | ✅/❌ | | |
| TRK-web-news | ✅/❌ | | |
| TRK-code-data | ✅/❌ | | |
| TRK-korea | ✅/❌ | | |

## 4. 성공 기준 (Gate 판정 근거)
- 총 수집 건수: {≥ N}
- 신뢰도 분포: {A/B ≥ X%}
- 트랙 커버리지: {활성 트랙 전부 목표 충족}

## 5. 시드 쿼리 (트랙별, 재현성 출발점)
- academic: {q}
- report: {q}
- web-news: {q}
- code-data: {q}
- korea: {q}

## 6. 제약·주의
{유료 접근 한계, 민감정보, 라이선스 등}

## 7. Open Questions
- [ ] {사용자 확인 필요 항목} `[검증 필요]`
