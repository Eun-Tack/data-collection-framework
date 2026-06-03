---
type: dc:Source
id: SRCMAN-{주제약자}
status: Draft
created_at: {YYYY-MM-DD}
traces_to: [CSPEC-{주제약자}]
owner: source-scout
---

# {주제} Source Manifest (Phase 1)

> 담당: source-scout · Gate: 활성 트랙마다 후보 소스 ≥ 3 (O-SS-01), 접근요건 명시율 100% (O-SS-02)
> 참조: `../../resources/RESOURCE_MANIFEST.md`

## 트랙별 후보 소스

### TRK-academic
| SRC | 소스 | 접근 | 도구 | 우선순위 | 진입 쿼리 |
|-----|------|------|------|---------|----------|
| SRC-01 | OpenAlex | 무료 API key 필요(2026-02~) | WebSearch/WebFetch | 1 | {q} |
| SRC-02 | arXiv | 무료 | WebSearch(allowed_domains) | 2 | {q} |
| SRC-03 | Semantic Scholar | 무료(키권장) | WebFetch | 3 | {q} |

### TRK-report
| SRC | 소스 | 접근 | 도구 | 우선순위 | 진입 쿼리 |
|-----|------|------|------|---------|----------|
| SRC-04 | {기관} | {무료/유료} | | | {q} |

### TRK-web-news
| SRC | 소스 | 접근 | 도구 | 우선순위 | 진입 쿼리 |
|-----|------|------|------|---------|----------|

### TRK-code-data
| SRC | 소스 | 접근 | 도구 | 우선순위 | 진입 쿼리 |
|-----|------|------|------|---------|----------|
| | GitHub | 무료 | gh CLI | | {q} |

### TRK-korea
| SRC | 소스 | 접근 | 도구 | 우선순위 | 진입 쿼리 |
|-----|------|------|------|---------|----------|
| | RISS/KCI/ScienceON | 무료/일부유료 | WebSearch(allowed_domains) | | {q} |

## 커버리지 점검
| 트랙 | 활성 | 후보 소스 수 | ≥3 충족 |
|------|------|------------|--------|
| academic | ✅ | | |
| report | | | |
| web-news | | | |
| code-data | | | |
| korea | | | |

> 미달 트랙은 추가 발굴 또는 `[자료 공백]` 사유 명시.
