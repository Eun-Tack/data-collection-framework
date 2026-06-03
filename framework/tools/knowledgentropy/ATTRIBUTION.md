# Attribution — vendored `knowledgentropy` (REM)

- **출처**: https://github.com/Eun-Tack/knowledgentropy — 브랜치 `perception-rem`
- **라이선스**: MIT
- **이식 범위**: `scorer.py`(IGScorer, 바이트 단위 원본) + slim `__init__.py`. 의존성 0(Python stdlib만).
- **이식일**: 2026-06-02

## 왜 이식했나
원본의 **IG(Information Gain) 수식**은 본 프레임워크 P3(vetting-analyst)의 신뢰도 평가를 **정성(A/B/C/D 주관) → 정량(결정적 점수)**으로 보강한다.

```
IG_base  = ω₁·AER + ω₂·Stab + ω₃·Trust   (기본 0.45 / 0.35 / 0.20)
IG_final = IG_base × (0.5 + 0.5 × freshness)
```
- **AER**: 사실 토큰 밀도(숫자·금액·연도·고유명사)
- **Stab**: 역 TTR(핵심 용어 반복도)
- **Trust**: 도메인 신뢰도 — HIGH 0.90(arxiv/nature/ieee/reuters/.edu/.gov/.ac.kr/.go.kr), MID 0.55, LOW 0.25(twitter/reddit/.xyz)

이 `Trust` 등급은 본 프레임워크의 `dc:QualityFactor F-2 Reliability`(A/B/C/D)와 같은 결이며, IG 점수가 그 **정량 측정치(measured_by)** 역할을 한다.

## 미이식(원본 브랜치에 존재)
- `tagger.py` (AutoTagger — 도메인 계층·엔티티 추출)
- `evaluator.py` (NewsletterMetricsEvaluator — AIR·ROUGE)
필요 시 `git checkout perception-rem -- tagger.py evaluator.py models.py config.py`로 동일하게 이식.
