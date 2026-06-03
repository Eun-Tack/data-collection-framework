# 에이전트 로스터 (Agent Roster)

Data Collection Framework에는 **9개의 전문화된 에이전트**가 있습니다(v1.0). Phase 파이프라인(P0~P4)을 따라 동작하며 버전 관리로 개선됩니다.

## 로스터

| Phase | 에이전트 | 버전 | 지시문 | _ESSENCE | 핵심 KPI |
|-------|---------|------|--------|---------|---------|
| P0a | intake-interviewer | v1.0 | `intake-interviewer/v1.0.md` | ✅ | O-IN-01 |
| P0b | collection-scoper | v1.0 | `collection-scoper/v1.0.md` | — | O-SC-01 ≥ 80 |
| P1 | source-scout | v1.0 | `source-scout/v1.0.md` | ✅ | O-SS-01 ≥ 3/트랙 |
| P2 | academic-collector | v1.1 | `academic-collector/v1.1.md` | — | O-CL-01 100% |
| P2 | report-collector | v1.0 | `report-collector/v1.0.md` | — | O-CL-01 100% |
| P2 | web-news-collector | v1.0 | `web-news-collector/v1.0.md` | — | O-CL-01 100% |
| P2 | code-data-collector | v1.1 | `code-data-collector/v1.1.md` | — | O-CL-01 100% |
| P2 | korea-collector | v1.0 | `korea-collector/v1.0.md` | — | O-CL-01 100% |
| P3 | vetting-analyst | v1.2 | `vetting-analyst/v1.2.md` | ✅ | O-VT-01 100% |
| P4 | catalog-synthesizer | v1.1 | `catalog-synthesizer/v1.1.md` | ✅ | O-CT-01 100% |

> `_ESSENCE.md`는 본질(왜 존재·무엇이 좋은 산출물)을 정의하는 핵심 에이전트에만 둔다. 나머지는 `current.md`(버전 포인터) + `v{버전}.md`(행동 규칙).

## 에이전트 로드 방법
```
1. <에이전트>/current.md 열기
2. 현재 버전 확인
3. <에이전트>/v{버전}.md 로드 (_ESSENCE 있으면 먼저 읽기)
4. 지시문에 따라 Phase 진행
```

## 버전 관리 규칙
```
<에이전트>/
├── _ESSENCE.md   <- (선택) 본질 정의 L1~L6
├── current.md    <- 현재 활성 버전 포인터
├── v1.0.md       <- 초기 지시문
└── v1.1.md       <- 마이너 개선
```
- v{Major}.{Minor} — Minor: 지시문 보완. Major: 역할 재정의·구조 재설계.
- 버전업 트리거: Agent Performance Score < 70 (2회 연속) 또는 사용자 수정 요청 반복.
- 절차: 새 버전 파일 작성 → 하단 "버전 이력"에 변경+사유 → `current.md` 갱신 → `../../CHANGELOG.md` 기록.

## Agent Performance Score
```
정량(60%) = (달성 O-KPI 수 / 전체 O-KPI 수) × 100
정성(40%) = Q1-03 체감 완성도(1~5) × 20  (수정요청 0회 +10 / 2회 -10 / 3회+ -20)
종합 = 정량 × 0.6 + 정성 × 0.4
```
| 점수 | 판정 | 조치 |
|------|------|------|
| ≥ 85 | Excellent | 유지, 패턴 문서화 |
| 70-84 | Good | 유지, 약점 개선 |
| 55-69 | Needs Improvement | 다음 실행 전 새 버전 |
| < 55 | Underperforming | 지시문 전면 재작성 |

KPI 정의: `../kpi/KPI_DEFINITIONS.md`.
