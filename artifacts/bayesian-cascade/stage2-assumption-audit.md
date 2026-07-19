# Stage 2: Assumption Audit

**Date:** 2026-07-19

---

## §1. Enabling Assumptions Table

### For Huang et al. Framework

| # | Assumption | Confidence | Fragility | Rationale |
|:--|:-----------|:-----------|:----------|:----------|
| A1 | BPP ≠ BQP | 0.65 | HIGH | 30+ year conjecture. No proof. If false, most computational claims collapse. But strong circumstantial evidence. |
| A2 | Fault-tolerant QC is physically realizable with manageable overhead | 0.50 | HIGH | Threshold theorem is proven mathematically; physical realization faces engineering challenges of unknown difficulty. |
| A3 | The five-keystone framework is complete | 0.40 | MEDIUM | Framework omits economic cost. May need a sixth keystone (Affordability). May need a seventh (Scalability). |
| A4 | The four-realm taxonomy is exhaustive | 0.55 | MEDIUM | Could be missing hybrid realms or entirely unanticipated ones. The paper itself admits "advantages we cannot yet conceive." |
| A5 | QEC overhead is surmountable | 0.45 | HIGH | Current surface code estimates: ~1,000 physical qubits per logical qubit. LDPC codes may reduce this but are unproven at scale. |
| A6 | Quantum sensing can achieve useful advantage despite HNLS limits | 0.60 | MEDIUM | HNLS kills asymptotic advantage but constant-factor improvements are real (LIGO, NV centers). |
| A7 | Classical algorithm innovation will not outpace quantum hardware | 0.40 | MEDIUM | History favors classical — most "quantum advantages" get dequantized. But some (Shor's) have survived decades. |

### For QNFO Framework

| # | Assumption | Confidence | Fragility | Rationale |
|:--|:-----------|:-----------|:----------|:----------|
| Q1 | The qubit is an epistemic failure, not a useful abstraction | 0.25 | HIGH | Most practitioners use qubit as operational abstraction, not ontological claim. This is QNFO's weakest argument. |
| Q2 | QEC overhead (10²–10³×) makes FTQC thermodynamically prohibitive | 0.35 | HIGH | Estimate is qualitative, not derived from a specific computation. No joules-per-solution threshold computed. |
| Q3 | $35B investment has produced zero commercially viable machines | 0.55 | MEDIUM | Definitional — D-Wave and IonQ have revenue. Claim depends on defining "commercially viable" restrictively. |
| Q4 | ~90% of post-classical investment goes to gate-model QC | 0.30 | HIGH | Impressionistic. No systematic survey. May be directionally correct but magnitude is unverified. |
| Q5 | Classical analysis can reliably map quantum advantage landscape | 0.40 | HIGH | Theorem 1 (if correct) directly challenges this. QNFO has not addressed. |
| Q6 | Joules per solution is the correct universal metric | 0.60 | MEDIUM | Reasonable for computation; less clear for sensing, communication, or foundational research. |
| Q7 | Diversified portfolio will outperform concentrated FTQC investment | 0.35 | MEDIUM | Untestable at present. No alternative substrate has demonstrated commercial advantage either. |

---

## §2. Blocking Assumptions

For Huang et al. to be correct in their optimistic framing:
1. **BPP ≠ BQP must be true** — 30 years unproven
2. **QEC overhead must be manageable** — Currently 10²–10³× for surface codes
3. **Classical algorithm innovation must plateau** — Currently accelerating
4. **Quantum hardware scaling must continue** — Currently facing decoherence, control, connectivity limits

For QNFO to be correct in its skeptical framing:
1. **The qubit-as-epistemic-failure argument must survive scrutiny** — Currently proving too much
2. **QEC overhead must remain above thermodynamic viability** — Quantitative analysis missing
3. **No FTQC computation must achieve commercial viability** — 2030-2035 test window
4. **Theorem 1 must not generalize** — If it does, QNFO's classical analysis approach may be inherently limited

---

## §3. Dependency Chain

```
BPP ≠ BQP (unproven)
    │
    ├──► If TRUE:
    │       ├──► Shor's algorithm = genuine computational advantage (theoretical)
    │       ├──► Theorem 1 = valid (conditional)
    │       └──► Requires QEC to be surmountable for practical impact
    │
    └──► If FALSE:
            ├──► All computational quantum advantage claims collapse
            ├──► Theorem 1 = vacuous
            ├──► Sensing/communication advantages survive (physical law-based)
            └──► QNFO's skeptical position largely vindicated
```

**The crucial path:** BPP ≠ BQP → Theorem 1 → Detection requires quantum hardware → Justification for quantum hardware → Hardware development required → QEC must work → Useful computation emerges. **Every link is uncertain.**

---

## QNFO's Own Dependency Chain (Honest Assessment)

```
Qubit is epistemic failure → Alternatives exist → Physics limits QC → Portfolio > concentration → Institutional reform needed
```

**How this chain breaks:**
- If qubit is a useful abstraction (not an epistemic failure): Chain collapses at first link
- If alternatives are also theoretical/unproven: Portfolio diversification is rearranging deck chairs
- If FTQC succeeds despite QEC overhead: QNFO's critique is falsified
- If Theorem 1 generalizes: QNFO cannot evaluate FTQC using only classical tools
