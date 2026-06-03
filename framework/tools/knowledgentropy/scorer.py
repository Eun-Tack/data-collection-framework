"""
knowledgentropy/scorer.py

IGScorer — 지식 엔트로피 수식 표준화

IG (Information Gain) 수식:
    IG = ω₁·AER + ω₂·Stab + ω₃·Trust

기본 가중치:
    ω₁ = 0.45  (AER: 정보 회상률)
    ω₂ = 0.35  (Stability: 텍스트 안정성)
    ω₃ = 0.20  (Trust: 출처 신뢰도)

freshness 감쇠 적용:
    IG_final = IG_base × (0.5 + 0.5 × freshness)

Zero-Dependency: Python 표준 라이브러리만 사용합니다.
"""

from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass
from typing import List, Optional


# ─────────────────────────────────────────────────────────────
# 가중치 설정
# ─────────────────────────────────────────────────────────────

@dataclass
class IGConfig:
    """IG 수식 가중치 설정."""

    omega_aer: float = 0.45    # ω₁: AER 가중치
    omega_stab: float = 0.35   # ω₂: Stability 가중치
    omega_trust: float = 0.20  # ω₃: Trust 가중치

    def __post_init__(self) -> None:
        total = self.omega_aer + self.omega_stab + self.omega_trust
        if abs(total - 1.0) > 1e-6:
            raise ValueError(
                f"IGConfig: ω₁+ω₂+ω₃ = {total:.4f} (합계가 1.0이어야 합니다)"
            )


@dataclass
class IGResult:
    """IGScorer 계산 결과."""

    ig_score: float          # IG_final (freshness 감쇠 적용)
    ig_base: float           # IG_base (감쇠 전)
    aer_score: float         # AER 컴포넌트
    stability_score: float   # Stability 컴포넌트
    trust_score: float       # Trust 컴포넌트
    freshness: float         # 신선도 (0.0~1.0, 미제공 시 0.5)
    passed: bool             # ig_score >= threshold

    def to_dict(self) -> dict:
        return {
            "ig_score": self.ig_score,
            "ig_base": self.ig_base,
            "aer_score": self.aer_score,
            "stability_score": self.stability_score,
            "trust_score": self.trust_score,
            "freshness": self.freshness,
            "passed": self.passed,
        }


# ─────────────────────────────────────────────────────────────
# AER 계산 (Answer Extraction Recall)
# ─────────────────────────────────────────────────────────────

_FACT_PATTERN = re.compile(
    r"\d[\d,\.]*\s*(?:억|만|천|%|달러|원|USD|B|M|K|billion|million)\b"
    r"|\b[A-Z][a-z]{1,20}(?:\s+[A-Z][a-z]{1,20}){0,3}\b"
    r"|(?:20|19)\d{2}(?:년|Q[1-4])?",
    re.IGNORECASE,
)


def _compute_aer(text: str, reference: str = "") -> float:
    """Answer Extraction Recall — 텍스트 내 사실 밀도 추정.

    reference가 있으면 text에서 reference 사실을 얼마나 포함하는지 측정.
    reference 없으면 텍스트 내 사실 토큰 비율로 추정.
    """
    if reference:
        ref_facts = set(m.group(0).lower() for m in _FACT_PATTERN.finditer(reference))
        if not ref_facts:
            return 0.5
        found = sum(1 for f in ref_facts if f in text.lower())
        return round(found / len(ref_facts), 4)
    # 자체 밀도 추정 (reference 없을 때)
    tokens = re.findall(r"[가-힣]+|[a-zA-Z0-9]+", text)
    if not tokens:
        return 0.0
    fact_tokens = len(_FACT_PATTERN.findall(text))
    return round(min(fact_tokens / max(len(tokens) * 0.3, 1), 1.0), 4)


# ─────────────────────────────────────────────────────────────
# Stability 계산 (텍스트 안정성)
# ─────────────────────────────────────────────────────────────

def _compute_stability(text: str) -> float:
    """텍스트 안정성 점수 — 어휘 다양성 기반 역엔트로피.

    안정적인 정보는 핵심 용어가 반복되므로 TTR(Type-Token Ratio)이 낮음.
    TTR = 고유토큰 / 전체토큰   → stab = 1 - TTR (클수록 안정)
    단, 매우 짧은 텍스트는 중립값 반환.
    """
    tokens = re.findall(r"[가-힣]+|[a-z]+", text.lower())
    if len(tokens) < 10:
        return 0.5
    ttr = len(set(tokens)) / len(tokens)
    return round(max(0.0, min(1.0, 1.0 - ttr + 0.2)), 4)  # +0.2 보정 (짧은 텍스트 편향)


# ─────────────────────────────────────────────────────────────
# Trust 계산 (출처 신뢰도)
# ─────────────────────────────────────────────────────────────

_TRUST_HIGH_DOMAINS = frozenset({
    "arxiv.org", "nature.com", "ieee.org", "acm.org", "reuters.com",
    "bbc.com", "nytimes.com", "techcrunch.com", "wired.com",
    "bloomberg.com", "ft.com", "wsj.com", "openai.com", "anthropic.com",
})
_TRUST_HIGH_TLDS = frozenset({".edu", ".gov", ".ac.kr", ".go.kr"})
_TRUST_LOW_DOMAINS = frozenset({"twitter.com", "x.com", "reddit.com", "quora.com"})
_TRUST_LOW_TLDS = frozenset({".xyz", ".click", ".info", ".biz"})


def _compute_trust(source_url: str) -> float:
    """URL 도메인 기반 출처 신뢰도 추정 (0.25 ~ 0.90)."""
    if not source_url:
        return 0.5
    try:
        from urllib.parse import urlparse
        parsed = urlparse(source_url)
        domain = parsed.netloc.lower().lstrip("www.")
        tld = ("." + domain.rsplit(".", 1)[-1]) if "." in domain else ""
    except Exception:
        return 0.5
    if tld in _TRUST_HIGH_TLDS or domain in _TRUST_HIGH_DOMAINS:
        return 0.90
    if domain in _TRUST_LOW_DOMAINS or tld in _TRUST_LOW_TLDS:
        return 0.25
    return 0.55


# ─────────────────────────────────────────────────────────────
# IGScorer
# ─────────────────────────────────────────────────────────────

class IGScorer:
    """
    지식 엔트로피 수식 표준화 스코어러.

    IG = ω₁·AER + ω₂·Stab + ω₃·Trust
    IG_final = IG_base × (0.5 + 0.5 × freshness)

    사용 예시:
        scorer = IGScorer()
        result = scorer.score(
            text="Groq raised $1.2B in Series D...",
            source_url="https://techcrunch.com/...",
            freshness=0.95,
        )
        print(result.ig_score)   # 최종 IG 점수
    """

    def __init__(
        self,
        config: Optional[IGConfig] = None,
        threshold: float = 0.70,
    ) -> None:
        self.config = config or IGConfig()
        self.threshold = threshold

    def score(
        self,
        text: str,
        *,
        reference: str = "",
        source_url: str = "",
        freshness: float = 0.5,
    ) -> IGResult:
        """텍스트의 IG 점수를 계산합니다.

        Args:
            text:       분석할 텍스트
            reference:  AER 계산용 참조 텍스트 (없으면 자체 밀도 추정)
            source_url: 출처 URL (Trust 추정용)
            freshness:  신선도 점수 (0.0~1.0, 기본 0.5)

        Returns:
            IGResult
        """
        aer = _compute_aer(text, reference)
        stab = _compute_stability(text)
        trust = _compute_trust(source_url)

        cfg = self.config
        ig_base = round(
            cfg.omega_aer * aer
            + cfg.omega_stab * stab
            + cfg.omega_trust * trust,
            4,
        )
        # freshness 감쇠: IG_final = IG_base × (0.5 + 0.5 × freshness)
        ig_final = round(ig_base * (0.5 + 0.5 * freshness), 4)

        return IGResult(
            ig_score=ig_final,
            ig_base=ig_base,
            aer_score=aer,
            stability_score=stab,
            trust_score=trust,
            freshness=freshness,
            passed=ig_final >= self.threshold,
        )

    def score_batch(
        self,
        texts: List[str],
        *,
        source_urls: Optional[List[str]] = None,
        freshness_list: Optional[List[float]] = None,
    ) -> List[IGResult]:
        """텍스트 목록에 대해 일괄 IG 점수를 계산합니다."""
        urls = source_urls or [""] * len(texts)
        freshness_vals = freshness_list or [0.5] * len(texts)
        return [
            self.score(text, source_url=url, freshness=f)
            for text, url, f in zip(texts, urls, freshness_vals)
        ]
