# CHANGELOG — Data Collection Framework

형식: [버전] — 날짜 / 변경 요약. 에이전트 버전업은 해당 에이전트와 사유를 함께 기록.

## [v1.4] — 2026-06-02 (의도 파악 인테이크 — P0a)

- **intake-interviewer 에이전트 신설(P0a, _ESSENCE+current+v1.0)** — 수집 전 사용자 의도를 인터뷰 + 기본자료 + 가이드라인으로 종합해 Collection Spec의 Intent·Guidelines를 만든다. 기존 P0는 **P0b Scope**로 분리.
- **`inputs/` 도입** — 프로젝트에 `inputs/GUIDELINES.md`(사용자 작성 규칙) + 기본자료(PDF·노트·링크). 템플릿: `framework/templates/phase0_scope/GUIDELINES.template.md`, `projects/_TEMPLATE/inputs/README.md`.
- **가이드라인 = 하드 제약** — Collection Spec frontmatter에 기계판독 필드(must_include/exclude, preferred/banned_sources, min_ab_ratio, languages, region, deadline, glossary). **`validate_project.py`가 강제**: banned_sources 도메인 포함·must_exclude 제목 매칭·min_ab_ratio 미달 → exit 1(게이트 FAIL).
- **대화형 인터뷰** — inputs/에 이미 있는 건 묻지 않고 부족분만 질문(마찰 최소).
- CLAUDE.md(파이프라인·게이트·흐름도), agents/README, KPI(O-IN-01), 스키마·템플릿 반영.

## [v1.3] — 2026-06-02 (Codex 리뷰 반영 — 검증 자동화·정책 갱신)

- **`framework/tools/validate_project.py` 신설** — 게이트 자동 판정기: frontmatter 필수 필드, CSV 정규 14컬럼, URL 형식, id 중복, dedup_key 충돌, traces_to(CSPEC), Catalog↔manifest 건수 일치를 검사. 오류 시 **exit 1**(게이트 실패). `--check-links`, `--json-summary`. (지시문으로만 강제하던 규칙을 실행 가능한 검증으로 승격)
- **`score_manifest.py` 강화** — `--as-of YYYY-MM-DD`(freshness 재현성), `--fail-on-review`(trust 불일치 시 exit 2), `--json-summary`. CI/게이트 연동 가능.
- **OpenAlex 정책 갱신** — 2026-02-13부터 **무료 API key 필수**(크레딧제), polite pool/email 폐지. RESOURCE_MANIFEST·Source Manifest 템플릿·온톨로지 예시·academic-collector 정정. **Crossref**는 mailto polite pool 권장 명시.
- **매니페스트 단계 분리** — `manifest_raw`(P2) → `manifest_vetted`(P3) → `manifest`(P4 최종). **vetting-analyst v1.1 → v1.2**(P3가 P4 산출물 참조하던 순서 오류 수정 + validate 게이트), **catalog-synthesizer v1.0 → v1.1**(vetted→final).
- **외부 프레임워크 = "어댑터" 원칙** + 스크랩 도구 보안 주의(MarkItDown/Docling 입력 격리, Crawl4AI vs Firecrawl) RESOURCE_MANIFEST에 명시.
- 검증: `validate_project.py`가 정상 PASS(rag-evaluation, 18행/0오류) + 고의 결손(URL 누락·dedup 충돌)에서 FAIL(exit 1) 확인. `score_manifest --as-of` 재현성 확인.

## [v1.2] — 2026-06-02

- **REM(knowledgentropy) IG 스코어러 정식 통합** — `Eun-Tack/knowledgentropy` 브랜치 `perception-rem`의 `scorer.py`(MIT, stdlib 의존성 0)를 `framework/tools/knowledgentropy/`에 바이트 단위 이식(ATTRIBUTION 명시).
- **`framework/tools/score_manifest.py`** 추가: manifest.csv → IG 점수·도메인 Trust·freshness·trust_grade_check 부여. `.go.kr`/`.ac.kr`/`.re.kr` 보정 포함(한국 기관 신뢰도 정확화).
- **vetting-analyst v1.0 → v1.1**: 정성 등급(A/B/C/D)에 **정량 IG 점수 + Trust 교차검증** 추가(Step 3·4, O-VT-05 신설). 신뢰도 평가의 주관성 보강.
- **온톨로지**: `dc:QualityFactor F-2 Reliability`를 IG로 `measured_by`/`computed_by` 매핑, `dc:CollectedItem`에 ig_score·trust·freshness 선택 필드.
- 검증: `projects/rag-evaluation/` 18건에 실제 IG 채점 — IG 합격 16/18, arxiv→Trust 0.90 HIGH, kci.go.kr 보정 확인, trust_grade_check 불일치 0건.

## [v1.1] — 2026-06-02

- **글로벌 규칙 6 신설** (CLAUDE.md): 기본 언어 en+ko 이중 쿼리 + 범위 global. Collection Spec 템플릿·스키마·프로젝트 템플릿에 기본값 반영.
- **academic-collector v1.0 → v1.1**: 기법/도구 언급 시 원논문 arXiv ID 병행 검색 강제 + en/ko·글로벌. (사유: rag-evaluation 스모크 테스트에서 RAGAS 원논문 URL 누락 발견)
- **code-data-collector v1.0 → v1.1**: `gh search`/`gh api`로 공식 레포 URL·stars·license 확정 강제, 추정 URL 금지. (사유: DeepEval/TruLens 공식 레포 미확정으로 C등급 정체)
- 첫 실행 검증: `projects/rag-evaluation/` — P0~P4 전 단계 게이트 통과(18건, A/B 61%).

## [v1.0] — 2026-06-02

- 초기 프레임워크 구축. `agents/AI_SDLC/` v2.0 아키텍처 차용(코어 세트).
- 5단계 Phase 파이프라인(P0 Scope → P1 Discovery → P2 Collect → P3 Vet&Dedup → P4 Catalog) 정의.
- 9개 에이전트 v1.0 배포: collection-scoper, source-scout, academic/report/web-news/code-data/korea collector, vetting-analyst, catalog-synthesizer.
- `dc:` 온톨로지 프론트매터 스키마 v0.1, Collection Spec(SSOT) 스키마, Phase별 KPI 게이트 정의.
- 기존 `agents/data-collector/`의 RESOURCE_MANIFEST·메타스키마·신뢰도 루브릭·5트랙 수집가 본문 이식.
