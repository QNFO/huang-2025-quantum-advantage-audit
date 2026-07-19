# Stage 4: Bayesian Sensitivity Analysis

**Date:** 2026-07-19

---

## Candidate: "FTQC Delivers Commercially Useful Advantage by 2040"

### Baseline EV Estimate

**QNFO estimate:** 0.05–0.15 (Physics of Computation, Problem-Substrate Mapping)
**Industry estimate:** 0.50–0.80 (Google, IBM roadmaps)
**Huang et al. implicit:** 0.30–0.50 (cautious optimism)
**Analysis midpoint:** 0.25

### ±20% Sensitivity Analysis

| Parameter | Baseline | −20% | +20% | ΔEV | Sensitivity Rank |
|:----------|:---------|:-----|:-----|:----|:-----------------|
| BPP ≠ BQP probability | 0.65 | 0.52 | 0.78 | ±0.08 | **1 (HIGHEST)** |
| QEC overhead factor | 500× | 600× | 400× | ∓0.04 | 2 |
| Classical algorithm innovation rate | 0.50/yr | 0.60/yr | 0.40/yr | ∓0.03 | 3 |
| Government funding continuity | 0.70 | 0.56 | 0.84 | ±0.02 | 4 |
| Private investment continuity | 0.60 | 0.48 | 0.72 | ±0.02 | 5 |
| Alternative paradigm success rate | 0.20 | 0.24 | 0.16 | ∓0.02 | 6 |

### Halve-Priors Analysis

Starting from the QNFO skeptical baseline, halve all optimistic priors:

| Parameter | QNFO Baseline | Halved | Effect |
|:----------|:-------------|:-------|:-------|
| BPP ≠ BQP probability | 0.40 | 0.20 | EV drops ~0.08 |
| QEC overhead manageable | 0.35 | 0.175 | EV drops ~0.04 |
| Industry claims credible | 0.25 | 0.125 | EV drops ~0.03 |
| **Combined effect:** | EV = 0.15 | **EV ≈ 0.06** | Near-zero |

Starting from industry optimistic baseline, halve all optimistic priors:

| Parameter | Industry Baseline | Halved | Effect |
|:----------|:-----------------|:-------|:-------|
| BPP ≠ BQP probability | 0.90 | 0.45 | EV drops ~0.10 |
| QEC overhead manageable | 0.80 | 0.40 | EV drops ~0.08 |
| Timeline achievable | 0.75 | 0.375 | EV drops ~0.06 |
| **Combined effect:** | EV = 0.60 | **EV ≈ 0.25** | Converges toward midpoint |

### Correlation Stress-Test

**Worst-case correlation scenario:** BPP = BQP AND QEC proves infeasible AND classical algorithms keep improving.
**Probability:** 0.10 (low but non-trivial)
**Impact:** EV → 0.00 (complete collapse of computational QC case)

**Best-case correlation scenario:** BPP ≠ BQP proven AND QEC overhead drops (LDPC codes work) AND classical algorithms plateau.
**Probability:** 0.05 (very low — requires multiple breakthroughs)
**Impact:** EV → 0.80 (near-certain commercial QC)

### Tornado Summary

```
Parameter sensitivity to FTQC commercial success by 2040:

BPP ≠ BQP probability          ████████████████████░ ░ ░ ░ ░ ░ ±0.08
QEC overhead factor            ██████████░░░░░░░░░░░ ░ ░ ░ ░ ░ ±0.04
Classical algorithm rate       ████████░░░░░░░░░░░░░ ░ ░ ░ ░ ░ ±0.03
Government funding             ██████░░░░░░░░░░░░░░░ ░ ░ ░ ░ ░ ±0.02
Private investment             ██████░░░░░░░░░░░░░░░ ░ ░ ░ ░ ░ ±0.02
Alternative paradigm success   ██████░░░░░░░░░░░░░░░ ░ ░ ░ ░ ░ ±0.02
```

**Key insight:** BPP ≠ BQP is the dominant uncertainty driver. A 30-year-old unproven conjecture controls the entire EV assessment. This is both Huang et al.'s honesty (they acknowledge this repeatedly) and QNFO's strongest argument (the foundation is unproven).

---

## Candidate: "QNFO Framework Validated by Events"

**Baseline EV:** 0.20 (probability that QNFO's specific predictions are broadly correct)

### Sensitivity

| Parameter | Baseline | ±20% Effect | Rank |
|:----------|:---------|:------------|:-----|
| FTQC fails to deliver | 0.75 → 0.60-0.90 | ±0.06 | 1 |
| Alternative substrates succeed | 0.15 → 0.12-0.18 | ±0.02 | 2 |
| QNFO acknowledged by mainstream | 0.10 → 0.08-0.12 | ±0.01 | 3 |

**Key insight:** QNFO's framework is validated primarily by FTQC's failure, not by its own successes. This is a structural asymmetry — QNFO wins if QC loses. The framework does not generate independent positive predictions that distinguish it from mere pessimism.
