# RAG 평가 자료 수집 — code-data (Phase 2)

> 담당: code-data-collector · 수집일: 2026-06-02
> 검색 쿼리: ["RAG evaluation open source tools RAGAS TruLens DeepEval ARES github"] / 소스: [SRC-09 GitHub] / 도구: [WebSearch]
> Gate: 필수 메타 100% (O-CL-01), 목표 4건 (O-CL-02)

## 1. 수집 요약
- 수집 건수: 4 / 목표: 4 ✅
- 등급 후보 분포: A:0 B:2 C:2 D:0

## 2. 항목 카탈로그

### ITM-C01 · RAGAS (explodinggradients/ragas)
```yaml
type: dc:CollectedItem
id: ITM-C01
status: Draft
anchored_on: [F-1, F-2]
collected_by: code-data-collector
from_source: SRC-09
traces_to: [TRK-code-data, CSPEC-RAGEVAL]
source_type: repo
url: https://github.com/explodinggradients/ragas
publisher: Exploding Gradients
pub_date: 2023
retrieved_date: 2026-06-02
lang: en
reliability: B
reliability_reason: "널리 채택된 OSS, RAG 전용 reference-free 평가(faithfulness/answer relevancy/context precision·recall)"
dedup_key: "github.com/explodinggradients/ragas"
related_ids: [ITM-W01, ITM-W03]
license: "[검증 필요] (Apache-2.0 추정)"
```
- key_points:
  - ground truth 없이 4개 RAG 메트릭 평가(reference-free)
  - 경량 Python, LLM-as-judge 기반

### ITM-C02 · ARES (stanford-futuredata/ARES)
```yaml
type: dc:CollectedItem
id: ITM-C02
status: Draft
anchored_on: [F-1, F-2]
collected_by: code-data-collector
from_source: SRC-09
traces_to: [TRK-code-data, CSPEC-RAGEVAL]
source_type: repo
url: https://github.com/stanford-futuredata/ARES
publisher: Stanford FutureData
pub_date: 2023
retrieved_date: 2026-06-02
lang: en
reliability: B
reliability_reason: "논문(ITM-A03) 공식 구현, 자동 평가 시스템"
dedup_key: "github.com/stanford-futuredata/ARES"
related_ids: [ITM-A03]
```
- key_points:
  - 컴포넌트별 맞춤 LLM judge 자동 생성
  - 논문 ITM-A03의 공식 코드

### ITM-C03 · Awesome-RAG-Evaluation (YHPeter/Awesome-RAG-Evaluation)
```yaml
type: dc:CollectedItem
id: ITM-C03
status: Draft
anchored_on: [F-1, F-2]
collected_by: code-data-collector
from_source: SRC-09
traces_to: [TRK-code-data, CSPEC-RAGEVAL]
source_type: repo
url: https://github.com/YHPeter/Awesome-RAG-Evaluation
publisher: YHPeter
pub_date: 2024
retrieved_date: 2026-06-02
lang: en
reliability: C
reliability_reason: "큐레이션 목록(2차), 단 ITM-A01 서베이 공식 레포 — 출처 추적용으로 유용"
dedup_key: "github.com/YHPeter/Awesome-RAG-Evaluation"
related_ids: [ITM-A01]
```
- key_points:
  - 서베이 ITM-A01의 공식 자료 모음
  - 벤치마크·메트릭·도구 인덱스

### ITM-C04 · DeepEval (confident-ai)
```yaml
type: dc:CollectedItem
id: ITM-C04
status: Draft
anchored_on: [F-1, F-2]
collected_by: code-data-collector
from_source: SRC-09
traces_to: [TRK-code-data, CSPEC-RAGEVAL]
source_type: repo
url: https://www.confident-ai.com/blog/rag-evaluation-metrics-answer-relevancy-faithfulness-and-more
publisher: Confident AI
pub_date: 2024
retrieved_date: 2026-06-02
lang: en
reliability: C
reliability_reason: "공식 GitHub URL 미확인 → 벤더 문서 기반. github.com/confident-ai/deepeval 추정 [검증 필요]"
dedup_key: "deepeval-confident-ai"
related_ids: [ITM-W04]
```
- key_points:
  - LLM 평가를 단위 테스트처럼(PyTest 통합)
  - `[검증 필요]` 공식 레포 URL 확정 필요

## 3. 공백·주의
- TruLens 공식 레포 URL은 이번 검색에서 직접 미확보 → web-news 트랙 비교글(ITM-W01)로 메타만 확보.

## 4. 다음 수집 제안
- `gh search repos "RAG evaluation"`로 스타·라이선스·최근 커밋 보강, TruLens/DeepEval 공식 레포 URL 확정.
