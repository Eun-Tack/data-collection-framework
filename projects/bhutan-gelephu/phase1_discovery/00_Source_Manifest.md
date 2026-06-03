---
type: dc:Source
id: SRCMAN-BHUTANGMC
status: Approved
created_at: 2026-06-03
traces_to: [CSPEC-BHUTANGMC]
owner: source-scout
---

# 부탄 겔레푸·미래산업 Source Manifest (Phase 1)

> 담당: source-scout · Gate: 활성 트랙마다 후보 소스 ≥ 3 (O-SS-01), 접근요건 명시율 100% (O-SS-02)
> 발굴 방법: 오리엔테이션 WebSearch 3건(en×2, ko×1, 2026-06-03)으로 1차 자료원 실재 확인 → 트랙 매핑.
> 도구: 내장 WebSearch/WebFetch 즉시 동작. `gh`/Python은 선택.

## 트랙별 후보 소스

### TRK-report (목표 8) — 최우선
| SRC | 소스 | 접근 | 도구 | 진입 쿼리/URL |
|-----|------|------|------|----------|
| SRC-01 | **GMC 공식 (gmc.bt)** — Royal Charter·마스터플랜·SAR 제도 | 무료 | WebFetch(gmc.bt) | "Gelephu Mindfulness City charter masterplan" |
| SRC-02 | **World Bank** — Bhutan CCDR·Climate Fund·Carbon Market 블로그/발간물 | 무료 | WebFetch(worldbank.org, openknowledge.worldbank.org) | "Bhutan Country Climate Development Report" |
| SRC-03 | **UNFCCC** — 부탄 3차 NDC(2025-11)·탄소시장 문서 | 무료(PDF) | WebFetch(unfccc.int) | "Bhutan Third NDC 2025" |
| SRC-04 | **부탄 정부 — Carbon Markets Framework 2025 / Carbon Registry** | 무료 | WebSearch/WebFetch | "Bhutan Carbon Markets Framework 2025" |
| SRC-05 | **ADB** — 부탄 국가전략·인프라·에너지 | 무료 | WebFetch(adb.org) | "ADB Bhutan country partnership energy" |
| SRC-06 | **BIG / Arup / Cistri** — 마스터플랜 설계 보고 | 무료 | WebFetch(big.dk, arup.com) | "Gelephu Mindfulness City masterplan" |

### TRK-web-news (목표 8) — 최우선
| SRC | 소스 | 접근 | 도구 | 진입 쿼리/URL |
|-----|------|------|------|----------|
| SRC-07 | **글로벌 미디어** (CNBC, Reuters, Guardian, BBC) | 무료(일부 페이월) | WebSearch | "Gelephu Mindfulness City Bhutan" |
| SRC-08 | **QC Intelligence / ESG Broadcast** — 탄소시장 전문 뉴스 | 무료(일부 유료) | WebFetch | "Bhutan Article 6 carbon fees" |
| SRC-09 | **건축·도시 매체** (Dezeen, ArchDaily, World-Architects, Archello) | 무료 | WebFetch | "Gelephu Mindfulness City BIG" |
| SRC-10 | **크립토 매체** (CoinDesk, BeInCrypto, ESG) — 비트코인 적립·입주기업 | 무료 | WebFetch | "Bhutan Bitcoin Gelephu reserve" |

### TRK-korea (목표 5) — 비즈니스 기회 관점
| SRC | 소스 | 접근 | 도구 | 진입 쿼리/URL |
|-----|------|------|------|----------|
| SRC-11 | **KOTRA 해외시장뉴스** (dream.kotra.or.kr) — 부탄 국가정보·진출 | 무료 | WebFetch | "KOTRA 부탄 시장 진출" |
| SRC-12 | **KIEP 대외경제정책연구원** — 남아시아·신흥시장 분석 | 무료 | WebSearch(kiep.go.kr) | "KIEP 부탄 남아시아 경제" |
| SRC-13 | **국내 미디어/전문지** (TokenPost, 한경, 연합, neoearly) | 무료 | WebSearch/WebFetch | "부탄 겔레푸 마인드풀니스 시티" |

### TRK-academic (목표 4)
| SRC | 소스 | 접근 | 도구 | 진입 쿼리/URL |
|-----|------|------|------|----------|
| SRC-14 | **OpenAlex / Semantic Scholar** — 특구·탄소시장·GNH 도시 | 무료·키불필요 | WebFetch(openalex.org) | "special administrative region charter city Bhutan" |
| SRC-15 | **Google Scholar / SSRN** — 차터시티·SEZ·Article 6 워킹페이퍼 | 무료(서지) | WebSearch | "charter city special economic zone carbon market" |
| SRC-16 | **MDPI / OA 저널 (Sustainability 등)** — GNH·지속가능도시 | 무료(OA) | WebFetch | "Gross National Happiness sustainable city planning" |

### TRK-code-data (목표 3)
| SRC | 소스 | 접근 | 도구 | 진입 쿼리/URL |
|-----|------|------|------|----------|
| SRC-17 | **World Bank Open Data / WDI** — 부탄 경제·에너지·인구 지표 | 무료·키불필요 | WebFetch(data.worldbank.org) | "Bhutan GDP energy indicators" |
| SRC-18 | **Bhutan National Carbon Registry / UNFCCC 등록부** — 탄소 크레딧 데이터 | 무료(서지·일부) | WebFetch | "Bhutan National Carbon Registry credits" |
| SRC-19 | **Our World in Data / Global Carbon Atlas** — 부탄 탄소수지(carbon negative) | 무료 | WebFetch(ourworldindata.org) | "Bhutan CO2 emissions carbon negative" |

## 커버리지 점검 (Gate O-SS-01)
| 트랙 | 활성 | 후보 소스 수 | ≥3 충족 |
|------|------|------------|--------|
| report | ✅ | 6 | ✅ |
| web-news | ✅ | 4 (+매체 다수) | ✅ |
| korea | ✅ | 3 | ✅ |
| academic | ✅ | 3 | ✅ |
| code-data | ✅ | 3 | ✅ |

> **Gate O-SS-01 통과**: 활성 5트랙 모두 후보 소스 ≥ 3.
> **Gate O-SS-02 통과**: 모든 소스에 접근요건(무료/유료/페이월) 100% 명시.
> 주의: academic은 신흥 주제라 직접 문헌이 적을 수 있음 → 인접 문헌(차터시티·SEZ·GNH)으로 보강, 부족분은 P3에서 `[자료 공백]` 명시.
