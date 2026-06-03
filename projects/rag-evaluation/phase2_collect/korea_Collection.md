# RAG 평가 자료 수집 — korea (Phase 2)

> 담당: korea-collector · 수집일: 2026-06-02
> 검색 쿼리: ["검색증강생성 RAG 평가 한국어 논문 성능 평가 방법"] / 소스: [SRC-11 KCI, SRC-12 KIPS, SRC-13 NIA] / 도구: [WebSearch]
> Gate: 필수 메타 100% (O-CL-01), 목표 3건 (O-CL-02)

## 1. 수집 요약
- 수집 건수: 3 / 목표: 3 ✅
- 등급 후보 분포: A:0 B:3 C:0 D:0

## 2. 항목 카탈로그

### ITM-K01 · 검색 증강 생성(RAG) 기술의 최신 연구 동향에 대한 조사
```yaml
type: dc:CollectedItem
id: ITM-K01
status: Draft
anchored_on: [F-1, F-2]
collected_by: korea-collector
from_source: SRC-11
traces_to: [TRK-korea, CSPEC-RAGEVAL]
source_type: paper
url: https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003124697
publisher: KCI 등재 학술지
pub_date: 2024
retrieved_date: 2026-06-02
lang: ko
reliability: B
reliability_reason: "KCI 등재 학술지 조사논문 (등재구분 [검증 필요])"
dedup_key: "kci-ART003124697"
related_ids: [ITM-K02]
```
- key_points:
  - RAG 평가 기법 소개 + 산업 활용·성능 최적화 사례 분석

### ITM-K02 · 검색 증강 생성(RAG) 기술에 대한 최신 연구 동향 (KIPS ASK 2024)
```yaml
type: dc:CollectedItem
id: ITM-K02
status: Draft
anchored_on: [F-1, F-2]
collected_by: korea-collector
from_source: SRC-12
traces_to: [TRK-korea, CSPEC-RAGEVAL]
source_type: paper
url: https://www.manuscriptlink.com/society/kips/conference/ask2024/file/downloadSoConfManuscript/abs/KIPS_C2024A0212
publisher: 한국정보처리학회(KIPS) ASK 2024
pub_date: 2024
retrieved_date: 2026-06-02
lang: ko
reliability: B
reliability_reason: "학회 발표 논문(학술대회)"
dedup_key: "kips-ask2024-A0212"
related_ids: [ITM-K01]
```
- key_points:
  - 국내 관점 RAG 연구 동향 정리

### ITM-K03 · 검색증강생성(RAG) 기술의 등장과 발전 동향 (NIA)
```yaml
type: dc:CollectedItem
id: ITM-K03
status: Draft
anchored_on: [F-1, F-2]
collected_by: korea-collector
from_source: SRC-13
traces_to: [TRK-korea, CSPEC-RAGEVAL]
source_type: gov
url: https://www.nia.or.kr/common/board/Download.do?bcIdx=27539&cbIdx=82618&fileNo=1
publisher: 한국지능정보사회진흥원(NIA)
pub_date: 2024
retrieved_date: 2026-06-02
lang: ko
reliability: B
reliability_reason: "공식 기관(NIA) 동향 자료"
dedup_key: "nia-rag-27539"
related_ids: []
```
- key_points:
  - 국내 정책·기관 관점의 RAG 등장·발전 동향

## 3. 공백·주의
- 평가 전용 국내 1차 논문은 제한적 → 대부분 "동향/조사" 성격. 평가 메트릭 실증은 영문(academic)에 의존 `[자료 공백]`.

## 4. 다음 수집 제안
- RISS/ScienceON OpenAPI로 "RAG 평가/검색증강생성 성능" 정밀 검색, KCI 등재구분 확정.
