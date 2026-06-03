# RAG 평가 자료 수집 — academic (Phase 2)

> 담당: academic-collector · 수집일: 2026-06-02
> 검색 쿼리: ["retrieval augmented generation evaluation benchmark survey arxiv 2024", "RAGAS faithfulness answer relevancy metrics"] / 소스: [SRC-01 arXiv] / 도구: [WebSearch]
> Gate: 필수 메타 100% (O-CL-01), 목표 5건 (O-CL-02)

## 1. 수집 요약
- 수집 건수: 5 / 목표: 5 ✅
- 등급 후보 분포: A:0 B:5 C:0 D:0 (전부 프리프린트 → B)

## 2. 항목 카탈로그

### ITM-A01 · Evaluation of Retrieval-Augmented Generation: A Survey
```yaml
type: dc:CollectedItem
id: ITM-A01
status: Draft
anchored_on: [F-1, F-2]
collected_by: academic-collector
from_source: SRC-01
traces_to: [TRK-academic, CSPEC-RAGEVAL]
source_type: preprint
url: https://arxiv.org/abs/2405.07437
publisher: arXiv (2024 CCF Big Data 채택)
pub_date: 2024-05
retrieved_date: 2026-06-02
lang: en
reliability: B
reliability_reason: "프리프린트, 2024 CCF Big Data 채택 — RAG 평가 벤치마크 전수 조사"
dedup_key: "10.48550/arXiv.2405.07437"
related_ids: [ITM-C03]
```
- abstract: RAG의 Retrieval·Generation 구성요소의 정량 메트릭(relevance, accuracy, faithfulness)을 현행 벤치마크 기준으로 비교·분석.
- key_points:
  - RAG 평가를 Retrieval/Generation 축으로 분해해 메트릭 정리
  - 데이터셋·메트릭의 한계와 향후 방향 제시
  - 공식 큐레이션 레포(Awesome-RAG-Evaluation)와 연결 → ITM-C03

### ITM-A02 · Retrieval-Augmented Generation for Large Language Models: A Survey
```yaml
type: dc:CollectedItem
id: ITM-A02
status: Draft
anchored_on: [F-1, F-2]
collected_by: academic-collector
from_source: SRC-01
traces_to: [TRK-academic, CSPEC-RAGEVAL]
source_type: preprint
url: https://arxiv.org/abs/2312.10997
publisher: arXiv (Gao et al.)
pub_date: 2023-12
retrieved_date: 2026-06-02
lang: en
reliability: B
reliability_reason: "널리 인용된 RAG 종합 서베이, 평가 프레임워크·벤치마크 섹션 포함"
dedup_key: "10.48550/arXiv.2312.10997"
related_ids: []
```
- abstract: LLM의 환각·지식 노후화 문제 맥락에서 RAG 패러다임을 종합하고 최신 평가 프레임워크·벤치마크를 정리.
- key_points:
  - Naive/Advanced/Modular RAG 분류로 널리 인용됨
  - 평가 프레임워크·벤치마크 정리 섹션 보유

### ITM-A03 · ARES: An Automated Evaluation Framework for RAG Systems
```yaml
type: dc:CollectedItem
id: ITM-A03
status: Draft
anchored_on: [F-1, F-2]
collected_by: academic-collector
from_source: SRC-01
traces_to: [TRK-academic, CSPEC-RAGEVAL]
source_type: preprint
url: https://arxiv.org/abs/2311.09476
publisher: arXiv (Stanford)
pub_date: 2023-11
retrieved_date: 2026-06-02
lang: en
reliability: B
reliability_reason: "프리프린트, RAG 구성요소별 LLM judge 자동 생성 평가 프레임워크"
dedup_key: "10.48550/arXiv.2311.09476"
related_ids: [ITM-C02]
```
- abstract: RAG 파이프라인 각 구성요소에 맞춤 LLM judge를 자동 생성하는 최초의 자동 평가 시스템.
- key_points:
  - 컴포넌트별 맞춤 judge 자동 생성
  - 오픈소스 구현 존재 → ITM-C02

### ITM-A04 · RAG Evaluation in the Era of LLMs: A Comprehensive Survey
```yaml
type: dc:CollectedItem
id: ITM-A04
status: Draft
anchored_on: [F-1, F-2]
collected_by: academic-collector
from_source: SRC-01
traces_to: [TRK-academic, CSPEC-RAGEVAL]
source_type: preprint
url: https://arxiv.org/abs/2504.14891
publisher: arXiv
pub_date: 2025
retrieved_date: 2026-06-02
lang: en
reliability: B
reliability_reason: "프리프린트, 최신(2025) RAG 평가 방법론 종합 [검증 필요: 채택 여부]"
dedup_key: "10.48550/arXiv.2504.14891"
related_ids: []
```
- abstract: LLM 시대의 RAG 평가 방법론을 포괄 정리한 최신 서베이.
- key_points:
  - 최신 평가 방법론 흐름 정리 `[검증 필요]` (출판 채택 상태 미확인)

### ITM-A05 · Evaluation of RAG Metrics for QA in the Telecom Domain
```yaml
type: dc:CollectedItem
id: ITM-A05
status: Draft
anchored_on: [F-1, F-2]
collected_by: academic-collector
from_source: SRC-01
traces_to: [TRK-academic, CSPEC-RAGEVAL]
source_type: preprint
url: https://arxiv.org/pdf/2407.12873
publisher: arXiv
pub_date: 2024-07
retrieved_date: 2026-06-02
lang: en
reliability: B
reliability_reason: "도메인 특화(통신) RAG 메트릭 실증 평가 프리프린트"
dedup_key: "10.48550/arXiv.2407.12873"
related_ids: []
```
- abstract: 통신 도메인 QA에서 RAGAS 등 RAG 메트릭의 적용성을 실증 평가.
- key_points:
  - RAGAS 메트릭의 도메인 적용 한계·보정 사례

## 3. 공백·주의
- RAGAS 원논문(arXiv:2309.15217 추정)은 이번 검색 결과에 직접 URL이 안 잡힘 → code-data 트랙의 도구 항목(ITM-C01)으로 대체 수집. `[검증 필요]` 원논문 URL 별도 확인 권장.

## 4. 다음 수집 제안
- OpenAlex로 ITM-A01 인용 논문 역추적, RGB·CRUD-RAG 등 벤치마크 데이터셋 논문 보강.
