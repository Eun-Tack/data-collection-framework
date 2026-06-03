# RAG 평가 자료 수집 — report (Phase 2)

> 담당: report-collector · 수집일: 2026-06-02
> 검색 쿼리: ["RAG enterprise adoption report 2025 evaluation benchmark industry"] / 소스: [SRC-04, SRC-05, SRC-06] / 도구: [WebSearch]
> Gate: 필수 메타 100% (O-CL-01), 목표 3건 (O-CL-02)

## 1. 수집 요약
- 수집 건수: 3 / 목표: 3 ✅
- 등급 후보 분포: A:0 B:1 C:2 D:0 · 접근 제한 2건

## 2. 항목 카탈로그

### ITM-R01 · RAG + LLMs for Enterprise Knowledge Management: A Systematic Literature Review
```yaml
type: dc:CollectedItem
id: ITM-R01
status: Draft
anchored_on: [F-1, F-2]
collected_by: report-collector
from_source: SRC-06
traces_to: [TRK-report, CSPEC-RAGEVAL]
source_type: paper
url: https://www.mdpi.com/2076-3417/16/1/368
publisher: MDPI Applied Sciences
pub_date: 2025
retrieved_date: 2026-06-02
lang: en
reliability: B
reliability_reason: "MDPI 피어리뷰 저널 SLR, 63개 1차 연구 분석 — 1차 근거"
dedup_key: "mdpi-2076-3417-16-1-368"
related_ids: []
```
- abstract: 기업 지식관리·문서 자동화에서 RAG+LLM 활용을 63개 연구로 체계적 검토.
- key_points:
  - 기업 도입은 대체로 실험 단계
  - 평가·튜닝 난이도("easy to use, hard to master")가 핵심 장애

### ITM-R02 · Retrieval-Augmented Generation (RAG) Market Report 2025–2030
```yaml
type: dc:CollectedItem
id: ITM-R02
status: Draft
anchored_on: [F-1, F-2]
collected_by: report-collector
from_source: SRC-04
traces_to: [TRK-report, CSPEC-RAGEVAL]
source_type: report
url: https://www.marketsandmarkets.com/Market-Reports/retrieval-augmented-generation-rag-market-135976317.html
publisher: MarketsandMarkets
pub_date: 2025
retrieved_date: 2026-06-02
lang: en
reliability: C
reliability_reason: "시장조사 요약 페이지(본문 유료) [접근 제한]"
dedup_key: "mnm-rag-market-135976317"
related_ids: [ITM-R03]
```
- key_points:
  - RAG 시장 2025 약 19.4억 USD → 2030 98.6억 USD, CAGR 38.4% `[검증 필요]`(요약 수치)
  - 본문 `[접근 제한]`

### ITM-R03 · RAG Industry Report 2025–2035 (Global RAG Market to Surpass $40B)
```yaml
type: dc:CollectedItem
id: ITM-R03
status: Draft
anchored_on: [F-1, F-2]
collected_by: report-collector
from_source: SRC-05
traces_to: [TRK-report, CSPEC-RAGEVAL]
source_type: report
url: https://www.businesswire.com/news/home/20251010008494/en/
publisher: ResearchAndMarkets (BusinessWire 보도자료)
pub_date: 2025-10-10
retrieved_date: 2026-06-02
lang: en
reliability: C
reliability_reason: "보도자료(2차), 본문 유료 [접근 제한]"
dedup_key: "researchandmarkets-rag-2025-2035"
related_ids: [ITM-R02]
```
- key_points:
  - 2035년까지 글로벌 RAG 시장 400억 USD 초과 전망 `[검증 필요]`
  - ITM-R02와 시장 전망 상호 보강(교차)

## 3. 공백·주의
- 시장조사 2건은 본문 유료 → 수치는 요약·보도자료 기반 `[접근 제한]`/`[검증 필요]`.
- 정부·국제기구(OECD/NIST) 공식 RAG 평가 보고서는 미확보 → `[자료 공백]`.

## 4. 다음 수집 제안
- NIST GenAI 평가 가이드, OECD AI 관련 문서로 공식 1차 보고서 보강.
