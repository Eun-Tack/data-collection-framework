# Vocabulary — Data Collection Framework `dc:` 온톨로지

> 버전: v0.1 | 프론트매터 규칙: `FRONTMATTER.schema.md`
> AI_SDLC `ai-sdlc:` 어휘를 자료 수집 도메인으로 미러링.

## 1. Class (type 값)

| Class | 의미 | Identifier 규칙 |
|-------|------|----------------|
| `dc:Philosophy` | 프레임워크 존재 이유(한 문장) | `PHIL-DC` |
| `dc:CollectionPrinciple` | 수집 원칙 P1~P5 | `CP-{번호}` |
| `dc:QualityFactor` | 좋은 수집을 정의하는 품질 요인 | `F-{번호}` |
| `dc:KPI` | 품질 요인 측정 지표 | `O-{에이전트}-{번호}` / `G-{phase}-{번호}` |
| `dc:Agent` | 수집 에이전트 | 에이전트명(예: `source-scout`) |
| `dc:CollectionSpec` | 수집 명세(SSOT) | `CSPEC-{주제약자}` |
| `dc:Track` | 수집 트랙 | `TRK-{academic\|report\|web-news\|code-data\|korea}` |
| `dc:Source` | 자료원(DB·API·사이트) | `SRC-{번호}` |
| `dc:CollectedItem` | 수집된 개별 자료 | `ITM-{트랙첫글자}{번호}` (예: `ITM-A01`) |
| `dc:Catalog` | 최종 카탈로그 | `CAT-{주제약자}` |

## 2. 관계 술어 (predicate)

| 술어 | 의미 | 역방향 |
|------|------|--------|
| `derived_from` | 본질 사슬 상위 참조(Philosophy←Principle←Factor) | — |
| `anchored_on` | 산출물이 정박한 QualityFactor | — |
| `measures` | KPI가 측정하는 QualityFactor | `measured_by` |
| `traces_to` | 파생물이 추적하는 상위(CollectionSpec/Track) | — |
| `collected_by` | 항목을 수집한 트랙 에이전트 | — |
| `from_source` | 항목의 출처 Source | — |
| `dedup_of` | 중복으로 병합된 대표 항목 | `related_ids` |
| `generates` / `consumes` | 에이전트의 산출/입력 Class | — |

## 3. status 값
`Draft` → `Approved` → `Locked` → `Deprecated`. (AI_SDLC와 동일. 운영/Superseded는 미채용.)

## 4. 본질 사슬 (Semantic chain)
```
dc:Philosophy
  └─ derived_from ← dc:CollectionPrinciple (CP-1..CP-5)
        └─ derived_from ← dc:QualityFactor (F-1..F-5)
              └─ measured_by ← dc:KPI
```
`dc:CollectedItem`은 `anchored_on`으로 F-1(Provenance)·F-2(Reliability)에 정박해야 status Approved 가능 → 출처/신뢰도 없는 항목 차단.

## 5. 품질 요인 (Quality Factors)
| ID | 요인 | 정의 | 측정 KPI(예) |
|----|------|------|------|
| F-1 | Provenance | 모든 항목이 접근 가능한 출처(url/DOI)를 가짐 | provenance 완전율 |
| F-2 | Reliability | A/B/C/D 등급 + 근거가 부여됨 | A/B 비율, 미등급률 |
| F-3 | Reproducibility | 검색 쿼리·소스·일자가 기록됨 | 재현 메타 기록률 |
| F-4 | Coverage | 활성 트랙·소스가 충분히 탐색됨 | 트랙당 소스/건수 |
| F-5 | Dedup | 중복이 dedup_key로 제거됨 | 중복 잔존율 |
