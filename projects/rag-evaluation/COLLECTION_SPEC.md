---
type: dc:CollectionSpec
id: CSPEC-RAGEVAL
name: "RAG(검색증강생성) 평가 방법론·벤치마크 자료 수집 명세"
status: Locked
created_at: 2026-06-02
owner: iet03
active_tracks: [TRK-academic, TRK-report, TRK-web-news, TRK-code-data, TRK-korea]
success_criteria: "총 15건 이상, A/B 등급 ≥ 50%, 활성 5트랙 모두 목표 충족"
seed_queries: ["retrieval augmented generation evaluation benchmark", "RAG evaluation framework metrics", "검색증강생성 RAG 평가"]
languages: [en, ko]
region: global
must_include: [RAG evaluation, faithfulness]
must_exclude: [image generation, crypto]
preferred_sources: [arxiv.org, aclanthology.org]
banned_sources: [reddit.com, x.com]
min_ab_ratio: 0.5
deadline: 2026-06-30
glossary: ["RAG=Retrieval-Augmented Generation", "AER=Answer Extraction Recall"]
---

# RAG 평가 방법론·벤치마크 자료 수집 명세 (Collection Spec)

> SSOT — 범위·트랙·성공기준은 이 문서에서만 변경. 파생물은 `traces_to: [CSPEC-RAGEVAL]`.

## 1. 수집 목적
RAG 시스템의 **평가 방법론·메트릭·벤치마크·오픈소스 도구**의 1차 자료 풀을 확보한다. 후속 리서치/도입 검토 시 근거로 사용.

## 2. 범위 (Scope)
- 포함: RAG 평가 메트릭(faithfulness, answer/context relevancy 등), 평가 프레임워크·벤치마크, 평가 도구
- 제외: RAG 일반 아키텍처 구현(평가와 무관한 부분), 비-RAG LLM 평가
- 기간: 2023-01 ~ 현재(2026-06)
- 언어/지역: en 중심 + ko(국내 동향)

## 3. 활성 트랙
| 트랙 | 활성 | 사유 | 목표 건수 |
|------|------|------|----------|
| TRK-academic | ✅ | 평가 방법론의 학술적 근거 핵심 | 5 |
| TRK-report | ✅ | 산업 채택·시장 맥락 | 3 |
| TRK-web-news | ✅ | 도구 비교·최신 실무 동향 | 3 |
| TRK-code-data | ✅ | 실제 평가 도구(OSS) | 4 |
| TRK-korea | ✅ | 국내 동향·한국어 자료 | 3 |

## 4. 성공 기준 (Gate 판정 근거)
- 총 수집 건수: ≥ 15
- 신뢰도 분포: A/B ≥ 50%
- 트랙 커버리지: 활성 5트랙 모두 목표 충족

## 5. 시드 쿼리 (트랙별)
- academic: "retrieval augmented generation evaluation benchmark survey"
- report: "RAG enterprise adoption report 2025 evaluation"
- web-news: "RAG evaluation open source tools RAGAS TruLens DeepEval"
- code-data: "RAGAS ARES github RAG evaluation"
- korea: "검색증강생성 RAG 평가 방법"

## 6. 제약·주의
- 시장조사 보고서(MarketsandMarkets, ResearchAndMarkets) 본문은 유료 → `[접근 제한]` 메타만.
- 일부 도구(TruLens/DeepEval) 공식 레포 URL 미확인 시 `[검증 필요]`.

## 7. Open Questions
- (없음 — Critical 0건, Lock 가능)
