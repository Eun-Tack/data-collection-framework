# 부탄 겔레푸·미래산업 자료 수집 — code-data (Phase 2)

> 담당: code-data-collector · 수집일: 2026-06-03
> 검색 쿼리: ["World Bank Open Data Bhutan GDP energy electricity WDI", "Bhutan carbon negative CO2 emissions Our World in Data", "Bhutan National Carbon Registry UNFCCC Article 6", "Bhutan CAD Trust Climate Action Data Trust national registry"] / 소스: [SRC-17..SRC-19] / 도구: [WebSearch, WebFetch]
> Gate: 필수 메타 100% (O-CL-01), 목표 3건 (O-CL-02)

## 1. 수집 요약
- 수집 건수: 3 / 목표: 3
- 등급 후보 분포: A:3 B:0 C:0 D:0

## 2. 항목 카탈로그

### ITM-D01 · World Bank Open Data — Bhutan 국가 지표(GDP·인구·전력·에너지) / WDI
```yaml
type: dc:CollectedItem
id: ITM-D01
status: Draft
anchored_on: [F-1, F-2]
collected_by: code-data-collector
from_source: SRC-17
traces_to: [TRK-code-data, CSPEC-BHUTANGMC]
source_type: dataset
url: https://data.worldbank.org/country/bhutan
publisher: World Bank Group (World Development Indicators)
pub_date: 2025
retrieved_date: 2026-06-03
lang: en
reliability: A
reliability_reason: "국제기구 1차 공식 통계 데이터베이스(WDI). 국가 통계기관·국제기구 출처를 표준화 집계, 메타데이터·갱신이력 투명."
dedup_key: "worldbank-open-data-bhutan-wdi"
related_ids: []
```
- abstract: 부탄 국가 단위 개발지표 시계열(WDI). 경제·인구·에너지·인프라 등 다부문 지표를 1990년대~최신연도까지 제공. 무료·키불필요.
- key_points:
  - GDP: 약 USD 3.01 billion (기준연도 2023). 인구: 791,524명 (기준연도 2024).
  - 전력 접근율: 100% (기준연도 2023) — 전력 보편 보급. [수력 의존 구조는 별도 지표]
  - 데이터 품질: Statistical Performance Indicator 58.0/100 (2024) — 보통 수준의 통계역량.
  - 접근방식: 무료. CSV/XML/Excel 일괄 다운로드 + REST API + DataBank 인터랙티브. 키 불필요.

### ITM-D02 · Our World in Data — Bhutan CO₂·온실가스 배출 데이터셋(탄소 네거티브 근거)
```yaml
type: dc:CollectedItem
id: ITM-D02
status: Draft
anchored_on: [F-1, F-3]
collected_by: code-data-collector
from_source: SRC-19
traces_to: [TRK-code-data, CSPEC-BHUTANGMC]
source_type: dataset
url: https://ourworldindata.org/co2/country/bhutan
publisher: Our World in Data (원자료: Global Carbon Project, Jones et al., Energy Institute, U.S. EIA)
pub_date: 2026
retrieved_date: 2026-06-03
lang: en
reliability: A
reliability_reason: "원자료가 Global Carbon Project 등 1차 과학 데이터. OWID는 투명한 표준화·코드북·오픈리포(owid/co2-data) 제공. CC-BY."
dedup_key: "our-world-in-data-bhutan-co2"
related_ids: [ITM-D01]
```
- abstract: 부탄의 총·1인당·누적·소비기준 CO₂ 및 온실가스(메탄·N₂O·총 GHG) 배출 시계열. 연료원별·부문별 분해 포함. 누적 CO₂는 1751년~최신, 대부분 지표 연 단위 갱신.
- key_points:
  - 부탄=세계 최초 탄소 네거티브 국가. 산림 흡수량 약 900만 tCO₂/yr 대 배출 약 200만 tCO₂ (2020 기준 인용치) — 순흡수.
  - 산림율 72.3%(헌법상 최소 60% 유지 의무), 2021년 수력발전 약 11,000 GWh 생산·80%+ 수출 — 배출 상쇄 구조.
  - 접근방식: 무료·CC-BY. 다운로드 포맷 CSV/XLSX(코드북 포함)/JSON, 정식 데이터 리포 `github.com/owid/co2-data`. 최근 갱신 2026-06, 2025-12, 2025-11.

### ITM-D03 · Bhutan National Carbon Registry × Climate Action Data Trust(CAD Trust) 공개 대시보드
```yaml
type: dc:CollectedItem
id: ITM-D03
status: Draft
anchored_on: [F-3, F-4]
collected_by: code-data-collector
from_source: SRC-18
traces_to: [TRK-code-data, CSPEC-BHUTANGMC]
source_type: registry
url: https://data.climateactiondata.org/
publisher: Climate Action Data Trust (창립: World Bank, IETA, Government of Singapore) · 부탄 측 운영: Druk Holding & Investments / Ministry of Energy and Natural Resources
pub_date: 2023
retrieved_date: 2026-06-03
lang: en
reliability: A
reliability_reason: "World Bank·IETA 창립 메타레지스트리 공식 공개 대시보드. 부탄 국가 레지스트리 자체가 1차 등록부. 블록체인 기반 메타데이터로 이중계상 방지."
dedup_key: "bhutan-national-carbon-registry-cad-trust"
related_ids: [ITM-D02]
```
- abstract: 부탄 국가 탄소 레지스트리(Article 6 크레딧 발급·이전·준수 추적)가 CAD Trust 메타데이터 레이어에 최초 통합된 국가 레지스트리. CAD Trust 공개 대시보드에서 다수 표준(Verra, GCC, EcoRegistry, BioCarbon, CDM) + 부탄 레지스트리 데이터를 표준 분류체계로 조회 가능.
- key_points:
  - 부탄 국가 탄소 레지스트리 COP28(2023년 12월) 출범 — CAD Trust 통합 최초 국가(통합 발표 2023).
  - 운영·IT 인프라: Druk Holding & Investments(부탄 정부 상업부문), 주관: Ministry of Energy and Natural Resources.
  - 데이터 범위: 크레딧 발급/이전/취소 메타데이터, 이중계상 방지(블록체인). 다수 표준 데이터셋 통합.
  - 접근방식: 무료 공개 대시보드(data.climateactiondata.org). 약관 동의 후 열람·비교·다운로드.

## 3. 공백·주의
- [주의] OWID 부탄 페이지 본문은 인터랙티브 차트로 표시되어 정확한 최신연도 수치(예: 정확한 2024 총배출 tCO₂)는 차트/리포 다운로드로 확인 필요. 본 수집의 수치는 2차 인용(2020 기준)·OWID 코드북 기반으로 [기준연도 명시]함. 정밀 수치는 P3 검증 시 `owid/co2-data` CSV에서 재확인 권장.
- [주의] World Bank "renewable energy share(수력 제외)" 지표가 0.0%(2021)로 표시되는데 이는 수력을 제외한 비수력 재생에너지 기준임 — 부탄 전력은 사실상 수력 100%이므로 지표 선택 시 정의 혼동 주의.
- [자료 공백] 부탄 국가 레지스트리의 누적 발급 크레딧 정량치(tCO₂e, 프로젝트 수)는 공식 단일 수치로 확보 못함 — CAD Trust 대시보드 직접 쿼리 또는 부탄 3차 NDC(2025-11) 교차확인 필요(SRC-03 연계).
- 겔레푸(GMC) 단위의 미시 데이터셋은 부재(신규 도시) — 국가 단위 지표를 프록시로 사용해야 함을 P3에서 명시.

## 4. 다음 수집 제안
- 부탄 3차 NDC(UNFCCC, 2025-11 PDF, SRC-03)에서 배출 기준선·감축목표·수력 상쇄 정량치 추출 → ITM-D02 보강.
- ADB Carbon Market Program 슬라이드(unfccc.int) 및 부탄 Carbon Market Rules 2023(moenr.gov.bt PDF)에서 거래·등록 절차 데이터 확보 → ITM-D03 정량 보강.
- IMF/ADB 데이터포털·부탄 NSB(National Statistics Bureau)에서 수력 발전·전력 수출액 시계열 확보 → 그린에너지 산업 근거.
