# RAG 평가 수집 합성 요약 (Phase 4)

> 담당: catalog-synthesizer · 2026-06-02 · 대상: CSPEC-RAGEVAL

## 1. 수집 요약
- 총 **18건** · 트랙별: academic 5 / report 3 / web-news 3 / code-data 4 / korea 3
- 등급 분포: **A:0 · B:11 · C:7 · D:0** (A/B 61%)

## 2. 핵심 자료 Top 5
1. **Evaluation of RAG: A Survey** (B, 2024-05) — RAG 평가를 Retrieval/Generation 축으로 분해, 메트릭·벤치마크·한계 전수 조사. RAG 평가의 지도. `[출처: arxiv.org/abs/2405.07437]`
2. **RAGAS** (B) — reference-free로 faithfulness·answer relevancy·context precision/recall 측정하는 사실상 표준 OSS. `[출처: github.com/explodinggradients/ragas]`
3. **ARES (논문+레포)** (B) — RAG 컴포넌트별 맞춤 LLM judge 자동 생성. 논문↔공식 구현 연결. `[출처: arxiv.org/abs/2311.09476, github.com/stanford-futuredata/ARES]`
4. **RAG for LLMs: A Survey** (B, 2023-12) — Naive/Advanced/Modular 분류로 널리 인용, 평가 섹션 포함. `[출처: arxiv.org/abs/2312.10997]`
5. **Enterprise KM SLR** (B, MDPI 2025) — 63개 연구 체계적 검토, "도입은 실험 단계, 평가·튜닝이 핵심 난제". `[출처: mdpi.com/2076-3417/16/1/368]`

## 3. 성공 기준 충족 (Collection Spec 대비)
| 기준 | 목표 | 실제 | 충족 |
|------|------|------|------|
| 총 건수 | ≥ 15 | 18 | ✅ |
| A/B 비율 | ≥ 50% | 61% | ✅ |
| 트랙 커버리지 | 활성 5트랙 | 5/5 목표 달성 | ✅ |

→ **모든 성공 기준 충족. P4 Gate(provenance 100%, 카탈로그↔매니페스트 18=18) 통과.**

## 4. 신뢰도·공백 노트
- **강점**: academic·code-data·korea가 B 중심으로 1차/권위 자료 확보. 논문↔구현 연결(ARES, 서베이↔Awesome)로 추적성 양호.
- **공백 `[자료 공백]`**: 정부·국제기구 공식 RAG 평가 문서(NIST/OECD) 부재. report는 시장조사(유료 `[접근 제한]`)·SLR 위주.
- **약한 고리**: web-news 전부 C(벤더/매체) — 사실 주장은 academic으로 교차검증함. 시장 수치(CAGR/시장규모)는 유료 요약 기반 `[검증 필요]`로 단정 보류.
- **확정 필요 `[검증 필요]`**: DeepEval/TruLens 공식 레포 URL, ITM-A04 출판 채택 상태, ITM-K01 KCI 등재구분.

## 5. 다음 수집 제안
- academic: OpenAlex로 ITM-A01 인용망 역추적 → RGB·CRUD-RAG·RAGTruth 등 벤치마크 데이터셋 논문 보강.
- report: NIST GenAI 평가 가이드, OECD AI 문서로 공식 1차 보고서 공백 메우기.
- code-data: `gh search repos "RAG evaluation"`로 스타·라이선스·최근 커밋 보강 + TruLens/DeepEval 공식 레포 확정.
- korea: RISS/ScienceON OpenAPI로 "RAG 평가 메트릭" 정밀 검색.
