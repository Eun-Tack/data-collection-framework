# inputs/ — 의도·기본자료 (P0a intake)

수집 시작 전, 여기에 의도 자료를 둡니다. intake-interviewer가 읽습니다.

## 무엇을 두나
- **GUIDELINES.md** — 사용자가 작성하는 규칙. 양식: `framework/templates/phase0_scope/GUIDELINES.template.md` 복사.
- **기본 자료** — 관련 PDF·노트·기존 보고서·링크 모음(예: `links.md`). 핵심 용어·이미 아는 것을 추출해 중복 수집을 막고 시드 쿼리로 씁니다.

## 흐름
```
inputs/ (GUIDELINES.md + 기본자료)
   ↓ P0a intake-interviewer (부족분만 인터뷰)
COLLECTION_SPEC.md (Intent·Guidelines + 기계판독 가이드라인 frontmatter)
   ↓ P0b collection-scoper (범위·트랙·성공기준·Lock)
   ↓ P1~P4
validate_project.py 가 가이드라인(금지 소스·제외 주제·A/B 비율)을 게이트로 강제
```

> GUIDELINES.md가 없어도 동작하지만(인터뷰로 대체), 있으면 의도가 더 정확히 강제됩니다.
