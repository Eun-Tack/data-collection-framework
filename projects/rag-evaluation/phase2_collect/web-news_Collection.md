# RAG 평가 자료 수집 — web-news (Phase 2)

> 담당: web-news-collector · 수집일: 2026-06-02
> 검색 쿼리: ["RAG evaluation open source tools RAGAS TruLens DeepEval ARES 2025"] / 소스: [SRC-07, SRC-08] / 도구: [WebSearch]
> Gate: 필수 메타 100% (O-CL-01), 목표 3건 (O-CL-02)

## 1. 수집 요약
- 수집 건수: 3 / 목표: 3 ✅
- 등급 후보 분포: A:0 B:0 C:3 D:0 (벤더/매체 블로그 → C, 주장은 `[근거 부족]` 가능)

## 2. 항목 카탈로그

### ITM-W01 · RAGAS, TruLens, DeepEval: LLM Evaluation Frameworks Compared
```yaml
type: dc:CollectedItem
id: ITM-W01
status: Draft
anchored_on: [F-1, F-2]
collected_by: web-news-collector
from_source: SRC-07
traces_to: [TRK-web-news, CSPEC-RAGEVAL]
source_type: blog
url: https://atlan.com/know/llm-evaluation-frameworks-compared/
publisher: Atlan
pub_date: 2026
retrieved_date: 2026-06-02
lang: en
reliability: C
reliability_reason: "벤더 지식베이스 비교글, 도구 선택 참고용"
dedup_key: "atlan-llm-eval-frameworks"
related_ids: [ITM-C01, ITM-C04]
```
- key_points:
  - RAGAS/TruLens/DeepEval를 가장 널리 쓰이는 3대 OSS로 정리
  - 각 도구의 평가 접근(메트릭 vs feedback function vs 단위테스트) 비교 `[검증 필요]`

### ITM-W02 · 7 RAG Evaluation Tools You Must Know
```yaml
type: dc:CollectedItem
id: ITM-W02
status: Draft
anchored_on: [F-1, F-2]
collected_by: web-news-collector
from_source: SRC-08
traces_to: [TRK-web-news, CSPEC-RAGEVAL]
source_type: blog
url: https://www.iguazio.com/blog/best-rag-evaluation-tools/
publisher: iguazio
pub_date: 2024
retrieved_date: 2026-06-02
lang: en
reliability: C
reliability_reason: "산업 매체 도구 목록, 개요 파악용"
dedup_key: "iguazio-rag-eval-tools"
related_ids: []
```
- key_points:
  - RAG 평가 도구 7종 개관 `[근거 부족]` (선정 기준 불명)

### ITM-W03 · Evaluating RAG Systems in 2025: RAGAS Deep Dive, Giskard Showdown
```yaml
type: dc:CollectedItem
id: ITM-W03
status: Draft
anchored_on: [F-1, F-2]
collected_by: web-news-collector
from_source: SRC-07
traces_to: [TRK-web-news, CSPEC-RAGEVAL]
source_type: blog
url: https://cohorte.co/blog/evaluating-rag-systems-in-2025-ragas-deep-dive-giskard-showdown-and-the-future-of-context
publisher: Cohorte Engineering
pub_date: 2025
retrieved_date: 2026-06-02
lang: en
reliability: C
reliability_reason: "엔지니어링 블로그, RAGAS·Giskard 실무 비교"
dedup_key: "cohorte-rag-eval-2025"
related_ids: [ITM-C01]
```
- key_points:
  - RAGAS 심층 + Giskard 대비, 2025 컨텍스트 평가 흐름

## 3. 공백·주의
- 전부 C 등급(벤더/매체) → 사실 주장은 academic(A/B)으로 교차검증 권장.

## 4. 다음 수집 제안
- Exa/Tavily로 1차 출처(공식 docs·릴리스) 우선 재검색, 날짜 최신순 보강.
