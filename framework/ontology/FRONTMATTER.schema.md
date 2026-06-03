# Frontmatter Schema — Data Collection Framework `dc:` v0.1

> 모든 산출물(마크다운) YAML frontmatter 작성 규칙. 어휘: `VOCABULARY.md`.
> AI_SDLC `framework/ontology/FRONTMATTER.schema.md`를 미러링.

## 목적
frontmatter를 기계 판독 가능한 그래프 트리플로 사용 — LLM이 본문 대신 frontmatter 슬라이스만 로드, 추적성·누락 자동 검증, 변경 영향 1-hop 조회. 본문은 사람용, frontmatter는 기계·LLM용 — 항상 동기화.

## 1. 공통 필수 필드
| 필드 | 타입 | 설명 | 예 |
|------|------|------|------|
| `type` | enum | `VOCABULARY.md`의 Class | `dc:CollectedItem` |
| `id` | string | Identifier 규칙 | `ITM-A01` |
| `status` | enum | `Draft`/`Approved`/`Locked`/`Deprecated` | `Approved` |
| `created_at` | date | ISO-8601 | `2026-06-02` |

선택 공통: `name`, `version`, `owner`, `source`(출처 태깅), `traces_to`, `tags`.

## 2. Class별 스키마

### 2.1 `dc:Philosophy`
```yaml
type: dc:Philosophy
id: PHIL-DC
status: Locked
statement: "출처와 신뢰도가 검증된 자료만이 의사결정의 근거가 된다"
```

### 2.2 `dc:CollectionPrinciple` (CP-*)
```yaml
type: dc:CollectionPrinciple
id: CP-2
name: Provenance Discipline
status: Locked
derived_from: [PHIL-DC]
statement: "출처 없는 항목은 만들지 않는다"
```

### 2.3 `dc:QualityFactor` (F-*)
```yaml
type: dc:QualityFactor
id: F-2
name: Reliability
status: Approved
derived_from: [CP-2]
measured_by: [O-VT-01, O-VT-05]   # O-VT-05 = REM IG 정량 점수
computed_by: framework/tools/score_manifest.py   # IG(AER·Stab·Trust) 자동 산출
owner: vetting-analyst
```
> F-2(Reliability)는 정성 등급(A/B/C/D)과 **정량 IG 점수**(vendored REM, `framework/tools/`)로 이중 측정한다. Trust 컴포넌트(도메인 신뢰도)가 등급과 같은 결.

### 2.4 `dc:KPI` (O-*, G-*)
```yaml
type: dc:KPI
id: O-VT-01
name: 신뢰도 등급 완전율
measures: [F-2]          # 필수 — 비면 v0.1 호환성 경고
threshold: "= 100%"
phase: P3
owner: vetting-analyst
```

### 2.5 `dc:CollectionSpec` (CSPEC-*) — SSOT
```yaml
type: dc:CollectionSpec
id: CSPEC-RAGEVAL
name: RAG 평가 자료 수집 명세
status: Locked
created_at: 2026-06-02
active_tracks: [TRK-academic, TRK-report, TRK-web-news]
success_criteria: "트랙별 A/B ≥ 50%, 총 25건 이상"
seed_queries: ["RAG evaluation", "retrieval augmented generation benchmark"]
```

### 2.6 `dc:Track` (TRK-*)
```yaml
type: dc:Track
id: TRK-academic
status: Approved
traces_to: [CSPEC-RAGEVAL]
target_count: 10
```

### 2.7 `dc:Source` (SRC-*)
```yaml
type: dc:Source
id: SRC-01
name: OpenAlex
status: Approved
track: TRK-academic
access: "무료 API key 필요 (2026-02~, 크레딧제)"
```

### 2.8 `dc:CollectedItem` (ITM-*)
```yaml
type: dc:CollectedItem
id: ITM-A01
name: "Self-RAG: Learning to Retrieve, Generate, and Critique"
status: Approved
anchored_on: [F-1, F-2]      # 필수: Provenance·Reliability ≥1
collected_by: academic-collector
from_source: SRC-01
traces_to: [TRK-academic, CSPEC-RAGEVAL]
source_type: paper           # paper/preprint/report/news/blog/repo/dataset/gov
url: https://arxiv.org/abs/2310.11511
publisher: ICLR 2024
pub_date: 2023-10-17
retrieved_date: 2026-06-02
lang: en
reliability: A
reliability_reason: "ICLR 2024 peer-reviewed"
dedup_key: "10.48550/arXiv.2310.11511"
related_ids: []
# ── 선택: P3에서 REM IG 스코어러로 자동 부여 (framework/tools/score_manifest.py) ──
ig_score: 0.5662        # IG_final = (ω₁·AER+ω₂·Stab+ω₃·Trust)×(0.5+0.5·freshness)
trust: 0.90             # 도메인 신뢰도 (HIGH 0.90 / MID 0.55 / LOW 0.25)
trust_tier: HIGH
freshness: 0.48
ig_passed: true         # ig_score >= threshold
```
> 본문에는 `abstract`(1~3문장)와 `key_points`(3~5 bullet)를 둔다.
> `ig_score`·`trust`·`freshness`는 P3에서 정량 부여(선택) — F-2 Reliability의 측정치. `reliability`(A/B/C/D)와 교차검증한다.

### 2.9 `dc:Catalog` (CAT-*)
```yaml
type: dc:Catalog
id: CAT-RAGEVAL
status: Approved
traces_to: [CSPEC-RAGEVAL]
item_count: 27
grade_dist: "A:12 B:9 C:5 D:1"
```

### 2.10 `dc:Agent`
```yaml
type: dc:Agent
id: vetting-analyst
status: Active
version: v1.0
phase: P3
generates: [dc:CollectedItem (graded), Vetting Report]
consumes: [dc:CollectedItem, dc:QualityFactor]
gated_by: [O-VT-01, O-VT-02]
```

## 3. 검증 규칙
1. **anchor 규칙**: `dc:CollectedItem`은 `anchored_on`에 QualityFactor ≥1 + `url` 비어 있으면 status `Approved`/`Locked` 전환 불가. (= 출처/신뢰도 없는 항목 drift 차단)
2. **측정 규칙**: `dc:KPI`는 `measures` 필수.
3. **본질 사슬**: `CollectionPrinciple.derived_from`은 Philosophy 1개, `QualityFactor.derived_from`은 ≥1 Principle.
4. **추적 규칙**: 모든 Phase 파생물은 `traces_to`에 CollectionSpec을 포함.
5. **관계 동기화**: `measures` ↔ `measured_by`, `dedup_of` ↔ `related_ids` 역방향 일치.

## 4. 작성 가이드
새 산출물: 해당 Class 스키마 복사 → `id` 부여 → 필수 필드 채움 → 관계 필드(비면 본문에 사유) → `Draft`로 시작, 검증 통과 시 `Approved`. 변경 시 `version` 증가 + 영향 받는 하위(`traces_to`/`anchored_on` 역참조) 확인.
