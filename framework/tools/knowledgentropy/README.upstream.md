# knowledgentropy

**Zero-dependency** information-gain scorer, domain tagger, and ROUGE evaluator for AI newsletter / RAG pipelines.

> Python 표준 라이브러리만 사용합니다. 외부 패키지 의존성 없음.

---

## 핵심 수식

### Information Gain (IG)

```
IG_base  = ω₁ · AER + ω₂ · Stab + ω₃ · Trust

IG_final = IG_base × (0.5 + 0.5 × freshness)
```

| 컴포넌트 | 기호 | 기본 가중치 | 설명 |
|----------|------|-------------|------|
| AER  | ω₁ | 0.45 | Answer Extraction Recall — 사실 토큰 밀도 |
| Stab | ω₂ | 0.35 | Stability — 역 TTR (핵심 용어 반복도) |
| Trust| ω₃ | 0.20 | Source Trust — 도메인 신뢰도 (0.25 ~ 0.90) |

환경 변수로 가중치 오버라이드:
```bash
export IG_OMEGA_AER=0.50
export IG_OMEGA_STAB=0.30
export IG_OMEGA_TRUST=0.20
export IG_THRESHOLD=0.35
```

### 도메인별 Trust 기준

| 등급 | 값 | 도메인 예시 |
|------|----|-------------|
| HIGH | 0.90 | arxiv.org, techcrunch.com, reuters.com, .edu, .gov |
| MID  | 0.55 | 미분류 도메인 |
| LOW  | 0.25 | twitter.com, reddit.com, .xyz |

---

## 설치

```bash
# 로컬 editable 설치
pip install -e /path/to/knowledgentropy/

# 또는 저장소 루트에서
cd knowledgentropy/
pip install -e .
```

## 빠른 시작

```python
from knowledgentropy.scorer import IGScorer, IGConfig

# 기본 사용
scorer = IGScorer(threshold=0.35)
result = scorer.score(
    text="NVIDIA invested $10B in new semiconductor fab construction in H1 2026.",
    source_url="https://techcrunch.com/nvidia-fab",
    freshness=0.95,
)
print(f"IG={result.ig_score:.4f}  passed={result.passed}")
# → IG=0.5335  passed=True

# 커스텀 가중치
cfg = IGConfig(omega_aer=0.50, omega_stab=0.30, omega_trust=0.20)
scorer2 = IGScorer(config=cfg, threshold=0.40)
```

```python
from knowledgentropy.tagger import AutoTagger

tagger = AutoTagger()
result = tagger.tag(
    entity="NVIDIA",
    text="NVIDIA announced a $10B investment in AI semiconductor infrastructure...",
    source_url="https://techcrunch.com/nvidia",
    published_at="2026-03-01",
)
print(result.domain_path)   # → "Technology/Hardware"
print(result.hierarchy)     # → ["IT", "Technology", "Hardware"]
for e in result.extracted_entities:
    print(e.name, e.entity_type)  # → NVIDIA  company
```

```python
from knowledgentropy.evaluator import NewsletterMetricsEvaluator

evaluator = NewsletterMetricsEvaluator()
metrics = evaluator.evaluate_from_texts(
    source_texts=["NVIDIA raised $10B for fab...", "Groq raised $1.2B..."],
    newsletter_body="AI semiconductor investment surged in 2026...",
    token_budget=2500,
)
print(f"AIR={metrics.air:.3f}  ROUGE-L={metrics.rouge_scores.rougeL:.3f}")
```

---

## 입출력 스키마

### `IGResult` (scorer.py)

```python
@dataclass
class IGResult:
    ig_score:         float   # IG_final (freshness 감쇠 적용)
    ig_base:          float   # IG_base (감쇠 전)
    aer_score:        float   # AER 컴포넌트 [0, 1]
    stability_score:  float   # Stability 컴포넌트 [0, 1]
    trust_score:      float   # Trust 컴포넌트 [0.25, 0.90]
    freshness:        float   # 신선도 [0, 1]
    passed:           bool    # ig_score >= threshold
```

### `TagResult` (tagger.py)

```python
@dataclass
class TagResult:
    entity:              str              # 입력 엔티티
    domain_path:         str              # "Technology/Hardware"
    keywords:            List[str]        # 최대 10개 키워드
    entity_type:         str              # "company" | "person" | "product" | "event"
    confidence:          float            # 도메인 분류 신뢰도 [0, 1]
    hierarchy:           List[str]        # ["IT", "Technology", "Hardware"]
    extracted_entities:  List[ExtractedEntity]
    meta:                Optional[TagMeta]  # freshness, trust, has_conflict
```

### `IGConfig` — 환경 변수 오버라이드

```python
from knowledgentropy.config import AppConfig
cfg = AppConfig.from_env()
# reads: IG_OMEGA_AER, IG_OMEGA_STAB, IG_OMEGA_TRUST, IG_THRESHOLD
```

---

## 디렉토리 구조

```
knowledgentropy/
├── __init__.py       # 공개 API 재내보내기
├── __main__.py       # python -m knowledgentropy 데모
├── config.py         # 환경 변수 기반 설정
├── models.py         # 공유 데이터 모델 (로컬 복제본)
├── scorer.py         # IGScorer — IG 수식 표준화
├── tagger.py         # AutoTagger v2 — 도메인 계층 + 엔티티 추출
├── evaluator.py      # NewsletterMetricsEvaluator — AIR/ROUGE
├── pyproject.toml
├── README.md
└── run_test.py       # 독립 실행 성능 검증 스크립트
```

---

## 데모 실행

```bash
python -m knowledgentropy          # 전체 기능 데모
python run_test.py                 # 성능 검증 테스트
```

## 라이선스

MIT
