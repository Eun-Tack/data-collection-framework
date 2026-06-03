# KPI Definitions — Data Collection Framework

> Phase별 KPI(`dc:KPI`)와 게이트 임계값. 각 KPI는 `measures`로 QualityFactor(`../ontology/VOCABULARY.md` §5)를 측정.
> 기록 절차: `../../CLAUDE.md` "KPI 기록".

## Phase Gate 요약
| Phase | 게이트 KPI | 임계값 |
|-------|-----------|--------|
| P0a Intake | O-IN-01 Intake Readiness | 핵심 의도 항목 충족 |
| P0b Scope | O-SC-01 Scope Readiness Score | ≥ 80 |
| (전 Phase) | 가이드라인 하드 제약(banned/must_exclude/min_ab_ratio) | validate_project FAIL=0 |
| P1 Discovery | O-SS-01 트랙당 후보 소스 수 | ≥ 3 (활성 트랙별) |
| P2 Collect | O-CL-01 필수 메타 완전율 / O-CL-02 트랙 목표 달성 | 100% / 목표 충족 |
| P3 Vet & Dedup | O-VT-01 등급 완전율 / O-VT-02 중복 잔존율 / O-VT-03 깨진 필수 URL | 100% / ≤ 5% / 0건 |
| P4 Catalog | O-CT-01 provenance 완전율 / O-CT-02 카탈로그↔매니페스트 일치 | 100% / 100% |

---

## P0a — intake-interviewer
**O-IN-01 Intake Readiness** (measures: F-4 Coverage·의도 정합) — Collection Spec의 의도 항목(목적·기간/지역·언어·포함/제외·선호/금지 소스·품질바)이 채워지고, 가이드라인이 기계판독 frontmatter(must_include/exclude, banned/preferred_sources, min_ab_ratio)로 옮겨졌는가. inputs/GUIDELINES.md ↔ frontmatter 일치.

## P0b — collection-scoper
**O-SC-01 Scope Readiness Score** (measures: F-4 Coverage) — Collection Spec 완성도, ≥ 80에서 Lock.

| 항목 | 배점 |
|------|------|
| 수집 목적·범위(포함/제외/기간/언어) 명시 | 20 |
| 활성 트랙 선정 + 사유 + 목표 건수 | 20 |
| 정량 성공 기준 정의 | 20 |
| 트랙별 시드 쿼리 2개 이상 | 20 |
| Open Questions에 Critical 0건 | 20 |
| **합계** | **100** |

---

## P1 — source-scout
**O-SS-01 소스 커버리지** (measures: F-4) — 활성 트랙마다 후보 소스 ≥ 3개를 Source Manifest에 등재.
**O-SS-02 접근요건 명시율** (measures: F-1) — 각 소스의 접근 방식(무료/키/유료)·도구 기록률 = 100%.

---

## P2 — 5 트랙 수집가
**O-CL-01 필수 메타 완전율** (measures: F-1 Provenance) — 수집 항목 중 필수 필드(`url, source_type, pub_date, retrieved_date, lang, reliability, dedup_key`) 100% 채움.
**O-CL-02 트랙 목표 달성** (measures: F-4 Coverage) — 트랙별 `target_count` 충족(미달 시 `[자료 공백]` + 보강 쿼리).
**O-CL-03 A/B 우선 비율** (measures: F-2 Reliability) — 수집 단계에서 A/B 후보 비중 ≥ 50% 지향.

---

## P3 — vetting-analyst
**O-VT-01 신뢰도 등급 완전율** (measures: F-2) — 모든 항목에 A/B/C/D + 근거 = 100%.
**O-VT-02 중복 잔존율** (measures: F-5 Dedup) — dedup_key 충돌이 병합되지 않고 남은 비율 ≤ 5%.
**O-VT-03 깨진 필수 URL** (measures: F-1) — 접근 불가 url(접근제한 제외) = 0건.
**O-VT-04 교차검증율** (measures: F-2) — 핵심 사실 항목 중 독립 출처 2건 이상 확인 비율(보고용).
**O-VT-05 IG 정량 점수 / Trust 정합성** (measures: F-2) — vendored REM(`framework/tools/score_manifest.py`)로 IG 점수·도메인 Trust를 산출. 목표: ① 전 항목 IG 점수 부여(선택 단계 수행 시), ② `trust_grade_check` 불일치("review:...") 항목을 모두 검토·해소. IG는 정성 등급(A/B/C/D)의 정량 교차검증.

---

## P4 — catalog-synthesizer
**O-CT-01 provenance 완전율** (measures: F-1) — 카탈로그 전 항목이 출처를 가짐 = 100%.
**O-CT-02 일치율** (measures: F-3 Reproducibility) — 본문 카탈로그 항목 수 = 매니페스트 CSV 행 수, 컬럼 순서 일치 = 100%.
**O-CT-03 합성 완결성** — Top-N + 공백 + 다음 수집 제안 포함(정성).

---

## 정성 평가 (사용자, 선택)
- Q1-01 수정 요청 횟수 ≤ 1
- Q1-03 체감 완성도(1~5) ≥ 4

## Agent Performance Score (AI_SDLC 차용)
`정량(O-KPI 달성률)×0.6 + 정성(Q1-03×20, 수정요청 보정)×0.4`. < 55점 2회 → 지시문 재작성, 70~84 → 개선 이슈. 상세: `../agents/README.md`.
