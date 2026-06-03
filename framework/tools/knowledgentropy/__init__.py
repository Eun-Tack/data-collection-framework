"""
knowledgentropy (vendored, slim) — IG 스코어러만 노출

원본: Eun-Tack/knowledgentropy, 브랜치 `perception-rem` (MIT). 의존성 0(stdlib).
본 프레임워크는 IGScorer만 사용하므로 scorer.py만 이식했다.
(tagger.AutoTagger / evaluator.NewsletterMetricsEvaluator는 원본 브랜치에 있으며,
 필요 시 동일 방식으로 추가 이식 가능 — ATTRIBUTION.md 참조)
"""

from .scorer import IGScorer, IGResult, IGConfig

__all__ = ["IGScorer", "IGResult", "IGConfig"]
