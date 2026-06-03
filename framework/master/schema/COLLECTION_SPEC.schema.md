# Collection Spec (SSOT) 스키마

> `dc:CollectionSpec`의 본문 구조 정의. frontmatter 규칙: `../../ontology/FRONTMATTER.schema.md`.
> Collection Spec은 수집 실행의 **단일 진실(SSOT)** — 범위·트랙·성공기준은 여기서만 변경한다.

## 위치
`projects/{주제}/COLLECTION_SPEC.md`

## frontmatter (필수)
```yaml
type: dc:CollectionSpec
id: CSPEC-{주제약자}
name: {주제} 자료 수집 명세
status: Draft        # Draft → Approved → Locked (Locked 후 P1 착수)
created_at: YYYY-MM-DD
owner: {사용자}
active_tracks: [TRK-academic, ...]   # 이번 수집에서 활성화할 트랙
success_criteria: "{정량 기준}"
seed_queries: ["...", "..."]
# ── Intent·Guidelines (P0a intake-interviewer가 채움) ──
languages: [en, ko]              # 기본 en+ko
region: global                   # 기본 global
must_include: [...]              # coverage 점검(경고)
must_exclude: [...]              # 제목 매칭 시 게이트 FAIL (하드)
preferred_sources: [...]         # 우선 탐색(soft)
banned_sources: [...]            # 도메인 포함 시 게이트 FAIL (하드)
min_ab_ratio: 0.5                # A/B 비율 미달 시 게이트 FAIL (하드)
deadline: 2026-06-30             # 선택
glossary: [...]                  # 핵심 용어
```

> **하드 제약**: `banned_sources`·`must_exclude`·`min_ab_ratio`는 `validate_project.py`가 manifest로 검사해 위반 시 exit 1. 가이드라인은 산문이 아니라 이 필드로 옮겨야 강제된다(P0a 책임).

## 본문 섹션
| # | 섹션 | 내용 |
|---|------|------|
| 1 | 수집 목적 | 왜 모으는가 / 이 자료로 무엇을 할 것인가 (1~3문장) |
| 2 | 범위 (Scope) | 포함/제외 주제, 기간. **언어 기본값 en+ko, 지역 기본값 global**(CLAUDE.md 규칙 6) |
| 3 | 활성 트랙 | `active_tracks`별 사유 + 트랙별 목표 건수(`target_count`) |
| 4 | 성공 기준 | 정량(총 건수, A/B 비율, 트랙 커버리지) — Gate 판정 근거 |
| 5 | 시드 쿼리 | 트랙별 초기 검색어(한/영) — 재현성의 출발점 |
| 6 | 제약·주의 | 유료 접근 한계, 민감정보, 라이선스 등 |
| 7 | Open Questions | 사용자 확인 필요 항목(스코핑 중 발생) |

## 상태 전이 (경량 Confirm Gate)
| 전이 | 조건 |
|------|------|
| Draft → Approved | 1~5 섹션 작성 완료 + Open Questions에 Critical 0건 |
| Approved → Locked | 사용자 변경 요약 컨펌 + Scope Readiness Score ≥ 80 → P1 착수 |
| → Deprecated | 주제 폐기 또는 새 Spec으로 대체(`superseded_by`) |

## 변경 규칙
- Locked 후 범위·트랙·성공기준 변경 시: `version` 증가 + 변경 요약 기록 + 영향받는 Phase 산출물(`traces_to: [CSPEC-…]` 역참조) 재검토.
- 파생 산출물(Source Manifest, Collection, Vetting, Catalog)은 직접 Spec을 수정하지 않는다 — 변경 필요 시 Open Question으로 등록.
