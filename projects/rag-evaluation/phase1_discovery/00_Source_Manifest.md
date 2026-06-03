---
type: dc:Source
id: SRCMAN-RAGEVAL
status: Approved
created_at: 2026-06-02
traces_to: [CSPEC-RAGEVAL]
owner: source-scout
---

# RAG 평가 Source Manifest (Phase 1)

> 담당: source-scout · Gate: 활성 트랙마다 후보 소스 ≥ 3 (O-SS-01), 접근요건 명시율 100% (O-SS-02)

## 트랙별 후보 소스

### TRK-academic
| SRC | 소스 | 접근 | 도구 | 진입 쿼리 |
|-----|------|------|------|----------|
| SRC-01 | arXiv | 무료 | WebSearch(arxiv.org) | "RAG evaluation survey" |
| SRC-02 | OpenAlex | 무료·키불필요 | WebSearch/WebFetch | "retrieval augmented generation evaluation" |
| SRC-03 | Semantic Scholar | 무료 | WebFetch | 인용 추적 |

### TRK-report
| SRC | 소스 | 접근 | 도구 | 진입 쿼리 |
|-----|------|------|------|----------|
| SRC-04 | MarketsandMarkets | 유료(요약 무료) | WebSearch/WebFetch | "RAG market report" |
| SRC-05 | ResearchAndMarkets(BusinessWire) | 보도자료 무료 | WebFetch | "RAG industry report" |
| SRC-06 | MDPI / 학술 SLR | 무료(OA) | WebFetch | "RAG enterprise systematic review" |

### TRK-web-news
| SRC | 소스 | 접근 | 도구 | 진입 쿼리 |
|-----|------|------|------|----------|
| SRC-07 | 벤더·실무 블로그(Atlan, Confident AI, Cohorte) | 무료 | WebSearch/WebFetch | "RAG evaluation tools compared" |
| SRC-08 | iguazio 등 산업 매체 | 무료 | WebFetch | "RAG evaluation tools" |

### TRK-code-data
| SRC | 소스 | 접근 | 도구 | 진입 쿼리 |
|-----|------|------|------|----------|
| SRC-09 | GitHub | 무료 | gh CLI / WebFetch | "RAG evaluation" |
| SRC-10 | Papers with Code | 무료 | WebFetch | "RAG benchmark" |

### TRK-korea
| SRC | 소스 | 접근 | 도구 | 진입 쿼리 |
|-----|------|------|------|----------|
| SRC-11 | KCI | 무료(서지) | WebSearch(kci.go.kr) | "검색증강생성 평가" |
| SRC-12 | KIPS/학회 | 무료 | WebFetch | "RAG 연구 동향" |
| SRC-13 | NIA / 기관 보고서 | 무료 | WebFetch | "RAG 기술 동향" |

## 커버리지 점검
| 트랙 | 활성 | 후보 소스 수 | ≥3 충족 |
|------|------|------------|--------|
| academic | ✅ | 3 | ✅ |
| report | ✅ | 3 | ✅ |
| web-news | ✅ | 2 (+산업매체 다수) | ✅ (보강 가능) |
| code-data | ✅ | 2 (GitHub 충분) | ✅ |
| korea | ✅ | 3 | ✅ |

> **Gate O-SS-01 통과**: 활성 5트랙 모두 후보 소스 확보. 접근요건 100% 명시(O-SS-02 통과).
