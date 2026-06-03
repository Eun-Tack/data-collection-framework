<!-- P2 트랙 공용 템플릿. {track}을 academic/report/web-news/code-data/korea로 치환해 사용. -->

# {주제} 자료 수집 — {track} (Phase 2)

> 담당: {track}-collector · 수집일: {YYYY-MM-DD}
> 검색 쿼리: [{q1}, {q2}, ...] / 사용 소스: [{SRC-..}] / 도구: [WebSearch, WebFetch, ...]
> Gate: 필수 메타 100% (O-CL-01), 목표 건수 충족 (O-CL-02)

## 1. 수집 요약
- 수집 건수: {n} / 목표: {target_count}
- 등급 후보 분포: A:{x} B:{y} C:{z} D:{w}

## 2. 항목 카탈로그

각 항목은 아래 frontmatter 블록 + 본문(abstract·key_points). (스키마: `../../ontology/FRONTMATTER.schema.md` §2.8)

### ITM-{T}01 · {제목}
```yaml
type: dc:CollectedItem
id: ITM-{T}01
name: "{제목}"
status: Draft
anchored_on: [F-1, F-2]
collected_by: {track}-collector
from_source: SRC-{nn}
traces_to: [TRK-{track}, CSPEC-{주제약자}]
source_type: {paper|report|news|repo|dataset|gov}
url: {url 또는 DOI}
publisher: {발행처}
pub_date: {YYYY-MM-DD}
retrieved_date: {YYYY-MM-DD}
lang: {ko|en}
reliability: {A|B|C|D}        # 후보 등급, 확정은 P3
reliability_reason: "{근거}"
dedup_key: {DOI|정규화URL|정규화제목+연도}
related_ids: []
```
- abstract: {1~3문장, 원문 근거}
- key_points:
  - {요점 1}
  - {요점 2} `[검증 필요]`(필요 시)

## 3. 공백·주의
- {[자료 공백] / [접근 제한] 항목과 사유}

## 4. 다음 수집 제안
- {미탐색 소스/쿼리}
