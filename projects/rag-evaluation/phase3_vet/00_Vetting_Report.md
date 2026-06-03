---
type: dc:CollectedItem
id: VET-RAGEVAL
status: Approved
created_at: 2026-06-02
traces_to: [CSPEC-RAGEVAL]
owner: vetting-analyst
---

# RAG 평가 Vetting Report (Phase 3)

> 담당: vetting-analyst · 검증일: 2026-06-02
> Gate: 등급 완전율 100% (O-VT-01), 중복 잔존율 ≤5% (O-VT-02), 깨진 필수 URL 0 (O-VT-03)

## 1. 종합 판정
- 검증 항목 수: 18 (중복 병합 후 18 — 진성 중복 없음)
- 등급 분포: **A:0 · B:11 · C:7 · D:0** → A/B = 11/18 = **61%** (성공기준 ≥50% ✅)
- 깨진 필수 URL: 0건 (R02·R03 본문은 유료 → `[접근 제한]`, url 자체는 유효)
- 미등급 항목: 0 (O-VT-01 100% ✅)
- **판정: 통과**

## 2. 등급 확정 표
| id | title | reliability | reason | url 상태 |
|----|-------|-------------|--------|---------|
| ITM-A01 | Eval of RAG: A Survey | B | 프리프린트·CCF Big Data 채택 | OK |
| ITM-A02 | RAG for LLMs: Survey | B | 다수 인용 종합 서베이 | OK |
| ITM-A03 | ARES (논문) | B | 자동평가 프레임워크 프리프린트 | OK |
| ITM-A04 | RAG Eval in Era of LLMs | B | 최신 서베이 `[검증 필요]` 채택여부 | OK |
| ITM-A05 | RAG Metrics in Telecom | B | 도메인 실증 프리프린트 | OK |
| ITM-C01 | RAGAS (repo) | B | 널리 쓰이는 OSS | OK |
| ITM-C02 | ARES (repo) | B | 논문 공식 구현 | OK |
| ITM-C03 | Awesome-RAG-Evaluation | C | 큐레이션 목록(2차) | OK |
| ITM-C04 | DeepEval | C | 공식 레포 URL 미확정 `[검증 필요]` | OK(벤더문서) |
| ITM-W01 | Atlan 비교글 | C | 벤더 지식베이스 | OK |
| ITM-W02 | iguazio 7 tools | C | 산업 매체 목록 `[근거 부족]` | OK |
| ITM-W03 | Cohorte 2025 | C | 엔지니어링 블로그 | OK |
| ITM-R01 | MDPI SLR | B | 피어리뷰 SLR(63개 연구) | OK |
| ITM-R02 | MnM Market Report | C | 시장조사 요약 `[접근 제한]` | OK(본문 유료) |
| ITM-R03 | R&M Industry Report | C | 보도자료 `[접근 제한]` | OK(본문 유료) |
| ITM-K01 | KCI 조사논문 | B | KCI 등재지 `[검증 필요]` 등재구분 | OK |
| ITM-K02 | KIPS ASK2024 | B | 학회 발표 | OK |
| ITM-K03 | NIA 동향자료 | B | 공식 기관 자료 | OK |

## 3. 중복 병합
- 진성 중복(dedup_key 충돌) **없음**. 아래는 관계(related_ids)로 연결한 연관 항목:

| 관계 | 항목 | 내용 |
|------|------|------|
| 논문↔구현 | ITM-A03 ↔ ITM-C02 | ARES 논문과 공식 레포 |
| 서베이↔자료모음 | ITM-A01 ↔ ITM-C03 | 서베이와 Awesome 레포 |
| 도구↔소개글 | ITM-C01 ↔ ITM-W01/W03 | RAGAS와 비교/리뷰 |
| 시장보고 상호보강 | ITM-R02 ↔ ITM-R03 | 시장 전망 교차 |
| 국내 동향 | ITM-K01 ↔ ITM-K02 | RAG 동향 조사/발표 |

## 4. 교차검증 (핵심 사실)
| 사실 | 독립 출처 | 결과 |
|------|----------|------|
| RAGAS 핵심 메트릭 = faithfulness·answer relevancy·context precision/recall | ITM-C01 + ITM-A01 + ITM-W01 | ✅ 일치 |
| RAG 시장 고성장(CAGR 38%대) | ITM-R02 + ITM-R03 | ⚠ 둘 다 유료 요약 `[검증 필요]`(수치 단정 금지) |

## 5. 공백·보강
- report 트랙에 정부·국제기구 공식 평가 문서 부재 → `[자료 공백]`. NIST GenAI 평가 가이드 보강 권장.
- web-news 전부 C → 사실 주장은 academic(B)으로 교차검증함.
- DeepEval/TruLens 공식 레포 URL 확정 필요 `[검증 필요]`.
