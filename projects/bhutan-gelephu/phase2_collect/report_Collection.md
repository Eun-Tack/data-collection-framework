# 부탄 겔레푸·미래산업 자료 수집 — report (Phase 2)

> 담당: report-collector · 수집일: 2026-06-03
> 검색 쿼리: ["Gelephu Mindfulness City Royal Charter 2024 masterplan SAR", "Bhutan Carbon Markets Framework 2025 National Carbon Registry", "World Bank Bhutan CCDR carbon market", "Bhutan third NDC 2025 UNFCCC", "ADB Bhutan country partnership strategy 2024-2028 energy", "Bhutan Singapore Article 6 implementation agreement Feb 2025", "GMC fintech digital assets financial center 2025"] / 소스: [SRC-01 gmc.bt, SRC-02 worldbank.org, SRC-03 unfccc.int, SRC-04 moenr.gov.bt, SRC-05 adb.org, SRC-06 mti.gov.sg] / 도구: [WebSearch, WebFetch]
> Gate: 필수 메타 100% (O-CL-01), 목표 8건 (O-CL-02)

## 1. 수집 요약
- 수집 건수: 8 / 목표: 8
- 등급 후보 분포: A:6 B:1 C:1 D:0 · 접근 제한 0건 (메타 확정, 일부 PDF 본문 미열람)

## 2. 항목 카탈로그

### ITM-R01 · Gelephu Mindfulness City — 공식 비전·SAR·8대 우선산업
```yaml
type: dc:CollectedItem
id: ITM-R01
status: Draft
anchored_on: [F-1, F-2]
collected_by: report-collector
from_source: SRC-01
traces_to: [TRK-report, CSPEC-BHUTANGMC]
source_type: report
url: https://gmc.bt/
publisher: Gelephu Mindfulness City (Royal Government of Bhutan / SAR)
pub_date: 2024-12
retrieved_date: 2026-06-03
lang: en
reliability: A
reliability_reason: "GMC 공식 사이트 1차 자료. SAR 거버넌스·8대 산업 정책 출처."
dedup_key: "gmc-bt-official-vision-sar-2024"
related_ids: [ITM-R08]
```
- abstract: GMC는 2024년 12월 Royal Charter로 설립된 고도 자치 특별행정구(SAR)로, 부탄 남부 인도 아삼주 접경 2,600km²(국토 5%)에 걸쳐 행정·입법·사법 권한을 본국 정부와 분리해 보유한다.
- key_points:
  - SAR 거버넌스: 완전한 행정·입법권 + 독립 사법부, 국왕 직접 지도 [출처: gmc.bt]
  - 8대 우선산업: 영성·헬스/웰니스·교육/지식·애그리테크/임업·그린에너지/기술·금융/디지털자산·항공/물류·관광 [출처: gmc.bt]
  - "Mindful Prosperity" 프레임워크 — 전통가치(GNH)와 경제번영 융합 [출처: gmc.bt]
  - 비즈니스 기회: 그린에너지·디지털자산이 명시적 우선산업으로 외자 유치 대상 [추론]

### ITM-R02 · Bhutan Country Climate and Development Report (World Bank CCDR)
```yaml
type: dc:CollectedItem
id: ITM-R02
status: Draft
anchored_on: [F-1, F-3]
collected_by: report-collector
from_source: SRC-02
traces_to: [TRK-report, CSPEC-BHUTANGMC]
source_type: report
url: https://openknowledge.worldbank.org/entities/publication/c3988d59-a6e8-4ea5-8297-d4deace008c1
publisher: World Bank Group
pub_date: 2025-06-18
retrieved_date: 2026-06-03
lang: en
reliability: A
reliability_reason: "World Bank 공식 국가기후개발보고서. 정책 모델링·재원전략 1차 분석."
dedup_key: "worldbank-bhutan-ccdr-2025"
related_ids: [ITM-R03, ITM-R06]
```
- abstract: 부탄 CCDR은 수력·농업 의존 경제의 기후 취약성을 진단하고, 경제 다각화·기후회복력·일자리와 탄소시장·녹색금융을 통한 재원 동원 전략을 제시한다.
- key_points:
  - 적응 투자만으로 건조·고온 시나리오 기후유발 GDP 손실의 약 40% 상쇄 가능(모델링) [출처: worldbank.org]
  - 글로벌 기후기금·탄소크레딧·민간투자·국내 녹색금융 수단 결합 권고 [출처: worldbank.org]
  - 부탄, Carbon Markets Policy Framework 확정 [출처: worldbank.org] [검증 필요: openknowledge PDF 403, 보도자료 기반]
  - 2025-02-28 싱가포르-부탄 Article 6 협정을 국제 탄소시장 진입 이정표로 언급 [출처: worldbank.org]

### ITM-R03 · Kingdom of Bhutan Third NDC (NDC 3.0, Provisional)
```yaml
type: dc:CollectedItem
id: ITM-R03
status: Draft
anchored_on: [F-1, F-3]
collected_by: report-collector
from_source: SRC-03
traces_to: [TRK-report, CSPEC-BHUTANGMC]
source_type: report
url: https://unfccc.int/sites/default/files/2025-11/Third%20NDC%20(Provisional)_10%20November%202025.pdf
publisher: Royal Government of Bhutan / UNFCCC
pub_date: 2025-11-10
retrieved_date: 2026-06-03
lang: en
reliability: A
reliability_reason: "UNFCCC 등재 부탄 공식 NDC 1차 정책문서(PDF)."
dedup_key: "unfccc-bhutan-third-ndc-2025"
related_ids: [ITM-R02, ITM-R04]
```
- abstract: 부탄 3차 NDC(잠정, 2025-11-10 UNFCCC 제출)는 2035년까지 탄소중립 유지를 재확인하고, 에너지·산업·농림·폐기물 감축과 재생에너지 대폭 확대를 제시한다. PM이 2025-10-24 공개.
- key_points:
  - BAU 2035년까지 탄소중립 — 배출 4,454 Gg CO₂e(LULUCF 제외)/8,673(포함) < 흡수능 10,965 Gg CO₂e [출처: unfccc.int]
  - 2040년까지 재생에너지 25,000 MW 확대 목표 [출처: unfccc.int]
  - EV·에너지효율·순환경제, 7대 적응 부문 강조 [출처: unfccc.int]
  - 비즈니스 기회: 25 GW 재생에너지 확장 = 그린에너지·인프라 투자 파이프라인 [추론]

### ITM-R04 · Bhutan Carbon Markets Framework 2025
```yaml
type: dc:CollectedItem
id: ITM-R04
status: Draft
anchored_on: [F-1, F-4]
collected_by: report-collector
from_source: SRC-04
traces_to: [TRK-report, CSPEC-BHUTANGMC]
source_type: report
url: https://www.moenr.gov.bt/?p=15417
publisher: Royal Government of Bhutan (NEC / DECC)
pub_date: 2025
retrieved_date: 2026-06-03
lang: en
reliability: A
reliability_reason: "부탄 정부 탄소시장 정책 프레임워크. 정부 발표·ESG 매체로 본문 확인."
dedup_key: "bhutan-carbon-markets-framework-2025"
related_ids: [ITM-R06, ITM-R07]
```
- abstract: Carbon Markets Framework 2025는 ITMO 생성·인증 절차, Corresponding Adjustment, 기관 거버넌스를 규정하며 2023년 Carbon Market Rules·2024년 National Carbon Registry를 토대로 한다.
- key_points:
  - 프로젝트 사이클: Mitigation Activity Design Document + 제3자 검증 의무화 [출처: esgbroadcast.com 2025-12-27]
  - 거버넌스: NEC(정책)·CCCC(기술)·DECC(이행)·Bhutan Climate Fund(크레딧 집계) [출처: esgbroadcast.com]
  - 국내 감축성과를 ITMO로 전환·승인, Article 6 정합 [검증 필요: 정부 1차 PDF 미열람]
  - 비즈니스 기회: 검증·MRV·크레딧 집계 밸류체인 진입점 [추론]

### ITM-R05 · ADB Bhutan Country Partnership Strategy 2024–2028
```yaml
type: dc:CollectedItem
id: ITM-R05
status: Draft
anchored_on: [F-3]
collected_by: report-collector
from_source: SRC-05
traces_to: [TRK-report, CSPEC-BHUTANGMC]
source_type: report
url: https://www.adb.org/sites/default/files/institutional-document/996396/cps-bhu-2024-2028.pdf
publisher: Asian Development Bank (ADB)
pub_date: 2024-09-13
retrieved_date: 2026-06-03
lang: en
reliability: A
reliability_reason: "ADB 공식 국가파트너십전략 기관문서(PDF). 메타 검색결과로 확정."
dedup_key: "adb-bhutan-cps-2024-2028"
related_ids: [ITM-R02]
```
- abstract: ADB 부탄 CPS(2024–2028)는 포용·지속가능·회복력·일자리 성장을 목표로 공공관리·민간개발, 기후적응 인프라, 인적자본 3대 축을 제시한다. 2024-09-13 출범.
- key_points:
  - 3대 축: PSM/PSD · 기후적응 회복력 인프라 · 인적자본/청년고용 [출처: adb.org]
  - 에너지·교통·도시 인프라, 수력·재생에너지·에너지효율 확대 지원 [출처: adb.org]
  - 비즈니스 기회: ADB 자금연계 인프라/에너지 파이프라인 [추론] [접근 제한: PDF 403, 보도자료 기반]

### ITM-R06 · Bhutan–Singapore Article 6 Implementation Agreement
```yaml
type: dc:CollectedItem
id: ITM-R06
status: Draft
anchored_on: [F-4]
collected_by: report-collector
from_source: SRC-06
traces_to: [TRK-report, CSPEC-BHUTANGMC]
source_type: report
url: https://www.mti.gov.sg/Newsroom/Press-Releases/2025/02/Singapore-signs-Implementation-Agreement-with-Bhutan-to-cooperate-on-carbon-credits-under-Article-6
publisher: Ministry of Trade and Industry, Singapore (with RGoB MoENR)
pub_date: 2025-02-28
retrieved_date: 2026-06-03
lang: en
reliability: A
reliability_reason: "싱가포르 정부 공식 보도자료. 양자 협정 1차 출처."
dedup_key: "mti-sg-bhutan-article6-2025"
related_ids: [ITM-R04, ITM-R02]
```
- abstract: 2025-02-28 싱가포르-부탄이 Article 6.2 하 탄소크레딧 협력 이행협정을 체결, 고결성 크레딧 법적 이전 프레임워크를 수립. Article 6 룰북(바쿠) 채택 이후 첫 양자협정이자 싱가포르 최초 탄소네거티브국 협정.
- key_points:
  - 1차 발행 시 조정크레딧 2% 취소(글로벌 순감축 기여) [출처: mti.gov.sg]
  - 조정크레딧 가치의 5%를 부탄 적응조치 재원으로 배분 [출처: mti.gov.sg]
  - Article 6 룰북 채택 이후 최초 양자 6.2 협정 [출처: mti.gov.sg]
  - 비즈니스 기회: 부탄發 ITMO 구매·중개·프로젝트 개발 수요 [추론]

### ITM-R07 · Bhutan's Journey into Carbon Markets, Technology (World Bank Blog)
```yaml
type: dc:CollectedItem
id: ITM-R07
status: Draft
anchored_on: [F-4]
collected_by: report-collector
from_source: SRC-02
traces_to: [TRK-report, CSPEC-BHUTANGMC]
source_type: report
url: https://blogs.worldbank.org/en/climatechange/dragons-data-and-clouds-bhutans-journey-carbon-markets-technology-and-resilient
publisher: World Bank Blogs (Torras Vives, Tashi, Singay)
pub_date: 2023-10-19
retrieved_date: 2026-06-03
lang: en
reliability: B
reliability_reason: "World Bank 공식 블로그(저자 명시)이나 2차 해설성. 기술·등록부 디테일 보강용."
dedup_key: "worldbank-blog-bhutan-carbon-journey-2023"
related_ids: [ITM-R04]
```
- abstract: 세계은행 블로그는 세계 최초 탄소네거티브국 부탄의 탄소시장 인프라 — GHG 인벤토리, 탄소등록부, DLT 토큰화 — 와 위성·드론·AI MRV 기술 도입을 소개한다.
- key_points:
  - 헌법상 산림 72.3% 의무 유지로 대규모 격리능력 확보 [출처: blogs.worldbank.org]
  - 위성원격탐사·드론·지상센서·AI/ML로 감축량 정밀 측정 [출처: blogs.worldbank.org]
  - DLT 기반 디지털 탄소크레딧 토큰화 + CAD Trust 연계 [출처: blogs.worldbank.org]
  - 비즈니스 기회: MRV 테크·블록체인 토큰화·검증서비스 진입점 명시 [출처: blogs.worldbank.org]

### ITM-R08 · Gelephu Financial Services Office (GFSO) — 금융·디지털자산 규제체계
```yaml
type: dc:CollectedItem
id: ITM-R08
status: Draft
anchored_on: [F-2]
collected_by: report-collector
from_source: SRC-01
traces_to: [TRK-report, CSPEC-BHUTANGMC]
source_type: report
url: https://gmc.bt/GFSO
publisher: Gelephu Financial Services Office (GMC SAR)
pub_date: 2025
retrieved_date: 2026-06-03
lang: en
reliability: A
reliability_reason: "GMC 공식 규제기관 페이지 1차 자료. 금융·핀테크 제도 출처."
dedup_key: "gmc-bt-gfso-financial-services-2025"
related_ids: [ITM-R01]
```
- abstract: GFSO는 GMC의 전통금융·블록체인/디지털자산을 아우르는 독립 금융규제기관으로, 1단계 ADGM 법 채택 후 2단계 자체 Financial Services Act 2025·룰북을 발행하며 금융·블록체인 생태계 육성을 담당한다.
- key_points:
  - 1단계: Application of Laws Act 2024 하 ADGM 법 채택 [출처: gmc.bt/GFSO]
  - 2단계: 자체 Financial Services Act 2025 + 룰북(AML·COBS·FUNDS·GEN·MIR·PRU·PIN 등) [출처: gmc.bt/GFSO]
  - 가상자산 기업은 Virtual Asset Guidance 준수, 7단계 라이선스 절차(IPA→FSL) [출처: gmc.bt/GFSO]
  - 인센티브: 0% 법인세(투자규모별)·자본이득/배당/상속세 없음 [검증 필요: GFSO 페이지엔 미기재, 2차 매체(The Block/Bitget) 보도]

### ITM-R09 · Gelephu Mindfulness City Masterplan (BIG·Arup·Cistri 설계)
```yaml
type: dc:CollectedItem
id: ITM-R09
status: Draft
anchored_on: [F-1, F-2]
collected_by: report-collector
from_source: SRC-06
traces_to: [TRK-report, CSPEC-BHUTANGMC]
source_type: report
url: https://big.dk/projects/gelephu-mindfulness-city-16791
publisher: Bjarke Ingels Group (BIG) — Arup(엔지니어링)·Cistri(코디네이션)
pub_date: 2024
retrieved_date: 2026-06-03
lang: en
reliability: B
reliability_reason: "설계 주관사 공식 프로젝트 페이지(1차) — 마스터플랜 디자인·정성 데이터. 정량 투자치는 미기재."
dedup_key: "big-dk-gelephu-masterplan-16791"
related_ids: [ITM-R01]
```
- abstract: BIG·Arup·Cistri가 설계한 GMC 마스터플랜은 35개 하천이 흐르는 부지에 북→남 밀도 구배의 저밀도 도시를 배치하고, 전통 Dzong 양식의 '거주형 다리(inhabitable bridges)'와 중심 기념물 Sankosh Temple-Dam을 결합한다.
- key_points:
  - 부지를 가로지르는 35개 하천 + 몬순 홍수 대비 논(paddy) 완충 [출처: big.dk]
  - 거주형 다리로 11개 네이버후드 연결, GNH·불교 영성을 도시형태에 반영 [출처: big.dk]
  - 설계팀: BIG(마스터플랜·건축)·Arup(엔지니어링)·Cistri(코디)·MQDC·NACO·CDR·ERM [출처: big.dk]
  - Holcim Foundation Award for Sustainable Construction(2025) 수상 [출처: big.dk]
  - 비즈니스 기회: 인프라·건설·엔지니어링·지속가능 건축 밸류체인 [추론]

### ITM-R10 · Royal Charter of Gelephu Mindfulness City (SAR 설립 법령)
```yaml
type: dc:CollectedItem
id: ITM-R10
status: Draft
anchored_on: [F-1, F-2]
collected_by: report-collector
from_source: SRC-01
traces_to: [TRK-report, CSPEC-BHUTANGMC]
source_type: report
url: https://gmc.bt/
publisher: Royal Government of Bhutan (Royal Charter)
pub_date: 2024-12
retrieved_date: 2026-06-03
lang: en
reliability: A
reliability_reason: "SAR 설립 근거 법령(공식). R01 개요와 구별되는 법적 거버넌스 문서. 원문 PDF는 미열람 → 일부 [검증 필요]."
dedup_key: "gmc-royal-charter-2024-sar-legal"
related_ids: [ITM-R01, ITM-R08]
```
- abstract: 2024년 12월 발효된 Royal Charter는 GMC를 완전한 행정·입법권과 독립 사법부를 갖는 특별행정구(SAR)로 설립하는 법적 근거로, 본국 정부와 분리되어 국왕 직접 지도를 받는다.
- key_points:
  - SAR에 "full executive and legislative powers" + 독립 사법부 부여 [출처: gmc.bt]
  - 면적 2,600km²(국토 약 5%), 인도 아삼주 접경 남부 평원 [출처: gmc.bt]
  - 자체 법체계 토대(Application of Laws Act 2024 → ADGM 법 채택, R08과 연계) [출처: gmc.bt]
  - Royal Charter No.1 of 2024 원문 PDF 직접 미열람 [검증 필요]
  - 비즈니스 함의: 독립 법·규제 관할로 외국인 투자·중재·금융 진입 장벽 차별화 [추론]

### ITM-R11 · Bhutan & Singapore: Advancing Carbon Market Innovation through Partnership (World Bank — Bhutan Climate Fund 투자자 라운드테이블)
```yaml
type: dc:CollectedItem
id: ITM-R11
status: Draft
anchored_on: [F-3, F-4]
collected_by: report-collector
from_source: SRC-02
traces_to: [TRK-report, CSPEC-BHUTANGMC]
source_type: report
url: https://blogs.worldbank.org/en/transport/Advancing_Carbon_Market_Innovation_through_Partnership
publisher: World Bank Blogs (Gemma Torras Vives, Jade Shu Yu Wong)
pub_date: 2025-07-28
retrieved_date: 2026-06-03
lang: en
reliability: B
reliability_reason: "World Bank 공식 블로그(저자 명시), Bhutan Climate Fund 투자자 라운드테이블 1차 전언. 2차 해설성이라 B."
dedup_key: "worldbank-blog-bhutan-singapore-carbon-partnership-2025"
related_ids: [ITM-R06, ITM-R02]
```
- abstract: 세계은행이 Bhutan Climate Fund를 주제로 투자자 라운드테이블을 개최, 투자자·탄소트레이더·프로젝트 개발자 약 30개 이해관계자가 부탄 탄소크레딧 포트폴리오 투자 기회를 모색. 부탄(공급)–싱가포르(규제·수요연결) 상호보완 모델을 제시.
- key_points:
  - Bhutan Climate Fund: 크레딧을 집계해 국제 구매자에게 중개하는 국부펀드 구조 [출처: blogs.worldbank.org]
  - 투자자 라운드테이블에 약 30개 이해관계자(투자자·트레이더·개발자) 참여 [출처: blogs.worldbank.org]
  - 부탄=세계 최초 탄소네거티브국, 산림 72% → 고결성 크레딧 공급원 [출처: blogs.worldbank.org]
  - 비즈니스 기회: 탄소크레딧 투자·중개·프로젝트 개발의 직접 진입 채널(라운드테이블) 명시 [출처: blogs.worldbank.org]

## 3. 공백·주의
- [접근 제한] World Bank openknowledge PDF(R02)·ADB CPS PDF(R05) 403 반환 — 메타·공식 보도자료로 확정, 수치 인용 시 PDF 재확인 권장.
- [검증 필요] Carbon Markets Framework 2025 1차 정부 PDF 미확보 — 본문은 ESG 매체(2025-12-27) 해설 기반.
- [검증 필요] GMC 세제 인센티브(0% 법인세 등)는 GFSO 공식 페이지가 아닌 2차 보도 출처 — Financial Services Act 2025 원문 대조 필요.
- [자료 공백] Royal Charter 2024 원문 PDF·BIG/Arup/Cistri 마스터플랜 보고서 원본 직접 미열람(개요만 확보).
- Bitcoin Development Pledge(2025-12, 최대 10,000 BTC)·TER 골드토큰(Solana) 등은 2차·시장 매체 다수 — 별도 검증 항목 분리 권장.

## 4. 다음 수집 제안
- gmc.bt에서 Royal Charter No.1 of 2024 · Application of Laws Act 2024 원문 PDF 확보(A등급 법령).
- NEC/DECC에서 Carbon Markets Framework 2025 + Carbon Market Rules 2023 + National Carbon Registry 운영지침 원문 PDF.
- BIG·Arup·Cistri 마스터플랜 설계보고서(B등급) — 11개 네이버후드·만다라 도시계획·공항(1.3M→5.5M)·대인도 고속철 정량 데이터.
- UNDP/GCF NDC 3.0 준비·역량강화 문서로 R03 보강.
- 부탄 첫 국내채권(2025) 발행자료 — 공항·스마트그리드·고속철 파이낸싱 구조.
