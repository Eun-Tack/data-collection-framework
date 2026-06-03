# 📦 리소스 매니페스트 (Sources & Tools)

`knowledgentropy`의 RESOURCE_MANIFEST를 차용해, **트랙별 자료원**과 **사용 가능한 외부 오픈소스·도구·프레임워크**를 한 곳에 모은다.

핵심 방침:
- **기본은 무설치.** Claude Code 내장 `WebSearch`(도메인 필터)와 `WebFetch`(URL→마크다운+요약)만으로 모든 트랙이 동작한다. `gh` CLI도 이미 설치되어 있다.
- 아래 **선택 강화 도구**는 규모·정밀도·자동화를 높일 때 설치한다. 설치·API 키 등록은 **사용자 동의 후에만** 수행한다.
- 외부 검색 API 시장은 변동이 잦다(2025-12 Google이 SerpAPI 제소, 2026-02 Nebius가 Tavily 인수 발표). 도입 전 최신 상태 확인 권장.

---

## 번들 도구 (무설치, stdlib) — REM IG 스코어러
`framework/tools/knowledgentropy/`에 **vendored REM**(`Eun-Tack/knowledgentropy`의 `perception-rem` 브랜치, MIT, 의존성 0)이 포함됨. P3(vetting-analyst)에서 **정량 신뢰도 점수**를 부여한다.
- `python framework/tools/score_manifest.py <manifest.csv>` → IG 점수·도메인 Trust·freshness·trust_grade_check 산출. 옵션: `--as-of YYYY-MM-DD`(freshness 재현성), `--fail-on-review`(불일치 시 exit 2), `--json-summary`.
- `python framework/tools/validate_project.py projects/<주제>` → **게이트 자동 판정**: frontmatter 필수 필드·CSV 정규 컬럼·URL 형식·id 중복·dedup_key 충돌·traces_to·Catalog↔manifest 건수 일치. 오류 시 exit 1. `--check-links`(URL HEAD), `--json-summary`.
- Python만 있으면 즉시 실행(설치 불필요). `.go.kr`/`.ac.kr`/`.re.kr` 보정 포함. 상세·출처: `framework/tools/knowledgentropy/ATTRIBUTION.md`.
- 확장: 원본 브랜치의 `tagger.py`(도메인 분류)·`evaluator.py`(AIR·ROUGE)도 동일 방식으로 추가 이식 가능.

### 외부 리서치 프레임워크 = "대체" 아닌 "어댑터" 원칙
GPT Researcher·LangChain open_deep_research·STORM 등은 **최종 산출물로 직접 쓰지 않는다.** 그들이 찾은 결과를 **본 프레임워크의 `dc:CollectedItem` 스키마로 변환**해 P3 게이트(신뢰도 등급·IG·dedup·`validate_project.py`)를 통과시킨다. 즉 외부 도구는 P1/P2의 "수집 엔진"으로만 붙이고, 출처·신뢰도·추적성 보증은 이 프레임워크가 책임진다.

### 보안 주의 (문서·스크랩 도구)
- **MarkItDown / Docling**: 신뢰할 수 없는 PDF/Office를 파싱할 때 입력을 제한·격리(공식 보안 경고 반영). 외부 파일은 sandbox에서 변환.
- **Crawl4AI**(로컬·프라이버시·비용 통제) vs **Firecrawl**(JS-heavy·대규모 안정성): 목적에 따라 선택.

---

## 트랙 1 · academic (논문)

### 자료원 (API/DB)
| 소스 | 접근 | 특징 |
|---|---|---|
| **OpenAlex** | **무료 API key 필요** (2026-02-13~), 2.5억+ 논문 | Crossref·MAG·arXiv·PubMed 통합, DOI 기반. 계정 발급 후 크레딧제(무료 일일 한도). polite pool/email은 폐지됨. [Auth](https://developers.openalex.org/api-reference/authentication) |
| **arXiv API** | 무료 | CS/물리/수학 프리프린트, 전문 PDF 직접. |
| **Semantic Scholar (Graph API)** | 무료(키 권장) | 인용 그래프·TLDR 요약·영향력 지표. |
| **Crossref REST API** | 무료 (mailto **polite pool** 권장) | DOI 메타데이터 표준 소스. `mailto=` 파라미터로 polite pool 사용. 2025-12-01 rate limit 개정. |
| **PubMed / Europe PMC** | 무료 | 생의학. |
| **Papers with Code** | 무료 | 논문↔코드↔벤치마크 SOTA 연결. |

### 내장 도구로 수집하는 법
- `WebSearch`에 `allowed_domains: ["arxiv.org","openalex.org","semanticscholar.org","aclanthology.org"]`로 학술 도메인 한정.
- `WebFetch`로 초록 페이지를 받아 제목·저자·발행일·요점 추출.

### 선택 강화 도구
| 도구 | 용도 | 설치/연동 |
|---|---|---|
| **paper-search-mcp** | arXiv·PubMed·bioRxiv 검색·다운로드 MCP 서버 | `pip install paper-search-mcp` 후 `.mcp.json`에 등록 — github.com/openags/paper-search-mcp |
| **arxiv-mcp** | arXiv 전용 MCP (검색·비교) | MCP 서버 등록 |
| **paper-qa (PaperQA2)** | 논문 PDF 고정밀 인용 RAG·문헌 리뷰 | `pip install paper-qa` — github.com/Future-House/paper-qa |
| **GROBID** | PDF → 구조화 TEI/메타데이터 | Docker 서비스 |
| **pyalex / arxiv.py / scholarly** | Python에서 OpenAlex/arXiv 질의 | `pip install pyalex arxiv scholarly` |

---

## 트랙 2 · report (보고서·정책)

### 자료원
- 정부·규제기관(예: 과기정통부, EU·OECD·NIST), 국제기구(UN/WHO/IMF), 싱크탱크(Brookings, RAND), 컨설팅(PwC·McKinsey·Gartner·Deloitte) 공개 PDF.
- 검색 전략: `WebSearch`에 `filetype:pdf` 키워드 + 기관 도메인 `allowed_domains` 한정.

### 내장 도구로 수집하는 법
- `WebSearch`로 기관·키워드 조합 → `WebFetch`로 PDF/HTML 본문 요약(WebFetch는 PDF도 마크다운 변환).

### 선택 강화 도구
| 도구 | 용도 | 설치 |
|---|---|---|
| **Firecrawl** | 웹·PDF·DOCX를 LLM용 마크다운으로 스크랩, MCP 지원 | `pip install firecrawl-py` 또는 MCP, 클라우드 키 — github.com/firecrawl/firecrawl |
| **Crawl4AI** | 로컬 우선 LLM 친화 크롤러, 키 불필요(38k★) | `pip install crawl4ai` — github.com/unclecode/crawl4ai |
| **Docling** | PDF/DOCX/PPTX → 마크다운(표·그림 보존, IBM) | `pip install docling` |
| **MarkItDown** | PDF/Office/이미지/오디오 → 마크다운(Microsoft) | `pip install markitdown` |
| **trafilatura** | 웹 본문 텍스트 추출 | `pip install trafilatura` |

---

## 트랙 3 · web-news (외부자료)

### 자료원
- 일반 웹·뉴스·기술 블로그·릴리스 노트. 내장 `WebSearch` + `WebFetch`로 충분히 시작 가능.

### 선택 강화 도구 (검색 API)
| 도구 | 강점 | 비고 |
|---|---|---|
| **Exa** | 시맨틱(뉴럴) 검색, 딥리서치·RAG에 강함, 빠름, people/company/code 검색 | 유료, `pip install exa-py` / MCP. 복잡 질의에서 우위 평가. |
| **Tavily** | LLM 친화 검색, 무료 티어·LangChain 통합 쉬움, 가장 쉬운 출발점 | `pip install tavily-python` / MCP. (2026-02 Nebius 인수 발표) |
| **Brave / Serper / Kagi** | 저렴·고속 대안 | API 키 |
| **mcp-omnisearch** | Tavily·Brave·Kagi·Exa·Firecrawl을 **단일 MCP**로 통합 | github.com/spences10/mcp-omnisearch |

> 권장: 프로토타이핑은 **Tavily**(무료·쉬움), 정밀 딥리서치는 **Exa**.

---

## 트랙 4 · code-data (코드·데이터셋)

### 자료원
- **GitHub**(레포·코드·이슈), **Hugging Face Hub**(모델·데이터셋), **Kaggle**(데이터셋·노트북), **Papers with Code**(SOTA·벤치마크).

### 내장 도구로 수집하는 법
- **`gh` CLI 이미 설치됨**: `gh search repos`, `gh search code`, `gh api`로 메타데이터 수집.
- `WebFetch`로 HF 데이터셋 카드·README 요약.

### 선택 강화 도구
| 도구 | 용도 | 설치 |
|---|---|---|
| **huggingface_hub / datasets** | HF 모델·데이터셋 프로그램 질의·다운로드 | `pip install huggingface_hub datasets` |
| **kaggle CLI** | Kaggle 데이터셋 검색·다운로드 | `pip install kaggle` (키 필요) |
| **GitHub MCP server** | GitHub를 MCP로 통합 | 공식 MCP 등록 |

> 데이터셋 다운로드 시 **디스크 용량 확인**(knowledgentropy 06/07 차용) 및 라이선스·게이트 모델 접근 요건을 메타에 기록.

---

## 트랙 5 · korea (국내자료)

### 자료원
| 소스 | 내용 | 접근 |
|---|---|---|
| **RISS** (riss.kr, KERIS) | 국내외 학위·학술 논문 | Open API 센터(키 신청), 웹 검색 |
| **DBpia** (dbpia.co.kr) | 학회지·연구기관 보고서·정기간행물 | 상당수 유료 → `[접근 제한]` 메타만 |
| **KCI** (kci.go.kr) | 한국학술지인용색인 | 웹 |
| **ScienceON** (KISTI, scienceon.kisti.re.kr) | 과학기술 논문·보고서, **OpenAPI 제공** | API 키 신청 |
| **공공데이터포털** (data.go.kr) | 공공 통계·데이터 | OpenAPI |
| **정책연구 포털**(PRISM 등) | 정부 정책연구 보고서 | 웹 |

### 내장 도구로 수집하는 법
- `WebSearch`에 `allowed_domains:["riss.kr","kci.go.kr","scienceon.kisti.re.kr","data.go.kr"]` + 한국어 쿼리.
- 유료·로그인 자료는 본문 우회 금지 → 메타데이터만 수집하고 `[접근 제한]` 표기.

### 선택 강화
- **KISTI ScienceON OpenAPI**, **RISS Open API**, **공공데이터포털 OpenAPI** — 각 기관 키 신청 후 Python 연동.

---

## 오케스트레이션 프레임워크 (참고)

본 에이전트는 Claude Code 서브에이전트로 다트랙을 오케스트레이션한다. 더 큰 자동 리서치 파이프라인이 필요하면 아래를 참고(채택 시 별도 환경 구성 필요):

| 프레임워크 | 특징 |
|---|---|
| **GPT Researcher** (assafelovic/gpt-researcher) | 자율 리서치 에이전트. CMU DeepResearchGym 평가에서 인용 품질·보고서 품질·커버리지 1위. |
| **LangChain open_deep_research** | 모델·검색·MCP 교체 가능한 오픈 딥리서치. Deep Research Bench 상위. |
| **STORM** (Stanford) | 다중 에이전트가 위키형 리포트를 협업 생성. |
| **DeerFlow** (ByteDance) | 오픈 딥리서치 프레임워크. |

---

## 도입 체크리스트 (사용자 동의 후)
1. 어떤 트랙에서 병목인지 확인 → 해당 트랙 도구만 선별 도입.
2. 무료·무키 우선(OpenAlex, Crawl4AI, paper-search-mcp, `gh`).
3. API 키 필요 도구는 키 발급 안내 → `.env`/세션 환경변수로만 관리(**코드·산출물에 키 하드코딩 금지**, knowledgentropy 차용).
4. MCP 서버는 `.mcp.json`(또는 설정)에 등록 후 연결 테스트.
5. 도입한 도구는 본 매니페스트 표에 "도입됨"으로 갱신.

## 출처 (조사 근거)
- [OpenAlex API (no key)](https://dev.to/0012303/openalex-api-search-250m-academic-papers-for-free-no-key-required-50pn) · [Research Paper APIs 2026](https://intuitionlabs.ai/articles/research-paper-apis-scientific-literature) · [OpenAlex vs S2 vs PubMed](https://intuitionlabs.ai/articles/openalex-semantic-scholar-pubmed-comparison)
- [paper-search-mcp](https://github.com/openags/paper-search-mcp) · [paper-qa (PaperQA2)](https://github.com/Future-House/paper-qa) · [arxiv-mcp](https://mcpservers.org/servers/kelvingao/arxiv-mcp)
- [Firecrawl](https://github.com/firecrawl/firecrawl) · [Crawl4AI](https://github.com/unclecode/crawl4ai) · [Best OSS scraping libs](https://www.firecrawl.dev/blog/best-open-source-web-scraping-libraries)
- [Exa vs Tavily vs SerpAPI](https://dev.to/ritza/best-serp-api-comparison-2025-serpapi-vs-exa-vs-tavily-vs-scrapingdog-vs-scrapingbee-2jci) · [Best web search MCP](https://www.firecrawl.dev/blog/best-web-search-mcp) · [mcp-omnisearch](https://github.com/spences10/mcp-omnisearch)
- [GPT Researcher](https://github.com/assafelovic/gpt-researcher) · [LangChain open_deep_research](https://github.com/langchain-ai/open_deep_research) · [Awesome Deep Research](https://github.com/DavidZWZ/Awesome-Deep-Research)
- [RISS](https://www.riss.kr/index.do) · [DBpia](https://www.dbpia.co.kr/) · [ScienceON RISS API](https://scienceon.kisti.re.kr/srch/selectPORSrchFnct.do?cn=FNCT000557)
