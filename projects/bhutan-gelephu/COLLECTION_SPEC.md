---
type: dc:CollectionSpec
id: CSPEC-BHUTANGMC
name: "부탄 국가 프로젝트(겔레푸 마인드풀니스 시티·미래산업·탄소배출권거래소) 자료 수집 명세"
status: Locked
created_at: 2026-06-03
owner: iet03
active_tracks: [TRK-academic, TRK-report, TRK-web-news, TRK-code-data, TRK-korea]
success_criteria: "총 30건 이상, A/B 등급 ≥ 40%, 활성 5트랙 모두 목표 충족"
seed_queries: ["Gelephu Mindfulness City special administrative region masterplan", "Bhutan carbon credit exchange future industries", "부탄 겔레푸 마인드풀니스 시티 투자 기회"]
languages: [en, ko]
region: global
must_include: [Gelephu Mindfulness City, Bhutan future industries, carbon credit]
must_exclude: []
preferred_sources: [gov.bt, gelephu.gov.bt, adb.org, worldbank.org, weforum.org, big.dk]
banned_sources: [reddit.com, x.com]
min_ab_ratio: 0.4
deadline: 2026-06-30
glossary: ["GMC=Gelephu Mindfulness City", "SAR=Special Administrative Region(겔레푸 특별행정구)", "GNH=Gross National Happiness(국민총행복)", "Article6=파리협정 6조 국제 탄소시장 메커니즘"]
---

# 부탄 국가 프로젝트(겔레푸·미래산업) 자료 수집 명세 (Collection Spec)

> SSOT — 범위·트랙·성공기준은 이 문서에서만 변경. 파생물은 `traces_to: [CSPEC-BHUTANGMC]`.
> 의도 근거: `inputs/00_Intent_Digest.md` (P0a Intake, 2026-06-03).

## 1. 수집 목적
부탄의 국가 주도 미래도시 **겔레푸 마인드풀니스 시티(GMC)**와 부탄이 추진하는 **미래산업(탄소배출권거래소·그린에너지·핀테크 등)**의 1차 자료 풀을 확보한다.
- **용도**: ① 보고서 작성 ② 비즈니스 기회 발굴.
- **전략**: 광범위 1차 수집으로 전체 지형을 잡은 뒤, 핵심 영역(탄소시장·투자·진입제도)을 세부 심화.

## 2. 범위 (Scope)
<!-- 기본값: 언어 en+ko, 지역(소스) global (규칙 6). 주제 대상 지역 = 부탄. -->
- **언어**: en + ko (en/ko 이중 쿼리)
- **소스 지역**: global (국제기구·글로벌 미디어·컨설팅 1차) + 한국 비즈니스 관점(korea 트랙)
- **대상 지역(주제)**: 부탄 / 겔레푸
- **포함**: GMC 비전·마스터플랜·거버넌스(SAR 특구법)·미래산업 포트폴리오·탄소배출권/탄소시장·투자/파트너십/자금조달·정량 데이터(경제·탄소·지리)·한국/글로벌 기업 연계
- **제외**: (사용자 지정 없음) — 단, 비즈니스·정책과 무관한 순수 관광/여행 가이드성 콘텐츠는 저우선(P3 저등급)
- **기간**: 2023-01 ~ 현재(2026-06) 중심, 배경자료는 그 이전 허용

## 3. 활성 트랙 (사유 + target_count)
| 트랙 | 활성 | 사유 | 목표 건수 |
|------|------|------|----------|
| TRK-report | ✅ | 정부·국제기구(ADB/WB)·컨설팅·싱크탱크 보고서 = 마스터플랜·제도·산업의 1차 근거 | 8 |
| TRK-web-news | ✅ | GMC는 2023~ 신규 발표 집중 → 투자·파트너십·진척 동향의 최신성 | 8 |
| TRK-korea | ✅ | 비즈니스 기회·한국 기업 연계 관점 + 국내 보도/분석 | 5 |
| TRK-academic | ✅ | 특구·탄소시장·GNH 도시계획의 이론·실증 근거 | 4 |
| TRK-code-data | ✅ | 탄소·경제·지리 정량 데이터셋, 탄소 레지스트리 | 3 |
| **합계** | | | **28 (성공기준 ≥30 여유)** |

## 4. 성공 기준 (Gate 판정 근거)
- 총 수집 건수: ≥ 30
- 신뢰도 분포: A/B ≥ 40% (신흥 주제 특성 반영, 규칙상 미달분은 `[자료 공백]`/`[검증 필요]` 명시)
- 트랙 커버리지: 활성 5트랙 모두 target_count 충족
- 필수 메타 100% (제목·URL·발행처·일자·트랙·출처태그)

## 5. 시드 쿼리 (트랙별)
- **academic**: "Gelephu Mindfulness City special economic zone urban planning" / "Bhutan carbon market Article 6 mechanism" / "부탄 경제특구 탄소시장"
- **report**: "Gelephu Mindfulness City masterplan ADB World Bank Bhutan report" / "Bhutan economic development future industries strategy" / "부탄 겔레푸 마인드풀니스 시티 마스터플랜"
- **web-news**: "Gelephu Mindfulness City investment partnership 2025 2026" / "Bhutan carbon credit exchange launch" / "부탄 겔레푸 탄소배출권 거래소 투자"
- **code-data**: "Bhutan carbon credit registry data" / "Bhutan economic indicators World Bank dataset" / "Gelephu GDP energy data"
- **korea**: "부탄 겔레푸 마인드풀니스 시티 한국 기업 투자 기회" / "부탄 미래산업 탄소배출권 협력" / "부탄 국가 프로젝트 진출"

## 6. 제약·주의
- **신흥 주제**: GMC 공개가 2023년 말로 학술 A급 문헌이 적을 수 있음 → `min_ab_ratio: 0.4`로 보수 설정, 뉴스 단일출처는 `[검증 필요]`.
- **공식 1차 우선**: 부탄 정부/GMC 공식(`gov.bt`, `gelephu.gov.bt`)·국제기구 자료를 우선, 홍보성·소셜(reddit/x) 금지.
- **유료 보고서**(컨설팅 시장조사): 본문 유료 시 `[접근 제한]` 메타만.
- **탄소시장 데이터**: 레지스트리·정량치는 출처·기준일 명시(`--as-of`), 미확인 추정치는 `[추론]`.

## 7. Open Questions
- [OQ-1, 검증 필요] "미래산업"의 정확한 범위(탄소 외 그린에너지/핀테크/항공/헬스 포함 여부) → P1에서 공식 포트폴리오로 확정. *(Non-critical — 광범위 1차로 흡수)*
- [OQ-2, 검증 필요] 탄소배출권거래소가 GMC 내 사업인지 부탄 국가 차원 사업인지 → P2 보고서/뉴스로 확인. *(Non-critical)*
- Critical OQ: **0건 → Lock 가능**

---

### Scope Readiness Score (O-SC-01) 자가 채점
| 항목 | 배점 | 획득 | 근거 |
|------|------|------|------|
| 목적·범위 | 20 | 20 | 목적 2가지 + 포함/제외/기간/언어 명시 |
| 트랙 선별 | 20 | 20 | 5트랙 활성 + 사유 + target_count |
| 성공 기준 | 20 | 20 | 총건수·A/B비율·커버리지·메타 정량화 |
| 시드 쿼리 | 20 | 20 | 트랙별 en/ko ≥2 |
| Critical OQ 0건 | 20 | 20 | Critical 0 (OQ는 모두 Non-critical) |
| **합계** | **100** | **100** | **≥80 충족 → 사용자 컨펌 후 Lock** |
