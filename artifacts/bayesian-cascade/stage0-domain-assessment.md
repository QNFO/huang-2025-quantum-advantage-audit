# Stage 0: Domain Assessment
## Quantum Advantage Research — Domain Topology Map

**Date:** 2026-07-19

---

## Domain Overview

The field of quantum advantage research has undergone three distinct eras:

### Era 1: Theoretical Foundations (1994–2012)
- Shor (1994), Grover (1996), HHL (2009)
- Characterized by discovery of individual algorithms with claimed exponential/polynomial speedups
- Methodology: complexity theory, oracle separations
- Dominant question: "Can quantum computers solve this problem faster than classical?"

### Era 2: Supremacy Experiments (2012–2023)
- Google Sycamore (2019), USTC Jiuzhang (2020), Xanadu Borealis (2022)
- Characterized by experimental demonstrations of quantum-classical separations
- Methodology: random circuit sampling, boson sampling, Gaussian boson sampling
- Dominant question: "Can we demonstrate a quantum advantage experimentally, even on a contrived problem?"

### Era 3: Framework Consolidation (2023–present)
- IBM "quantum utility" reframing (2023)
- Dequantization results (Aharonov et al. 2023, Begušić et al. 2024, 2025)
- Myth-busting papers (Zimborás et al. 2025)
- Framework papers (Lanes et al. 2025, Huang et al. 2025)
- Dominant question: "What actually counts as a genuine quantum advantage?"

---

## Key Research Questions (Active)

| RQ | Status | Key Reference |
|:---|:-------|:--------------|
| Can quantum computers solve commercially relevant problems faster than classical? | Open | Huang et al. §II.5 |
| Is BPP ≠ BQP? | Open (30+ years) | Complexity theory |
| Can quantum sensing achieve asymptotic advantage under realistic noise? | Resolved: NO (HNLS criterion) | Zhou et al. |
| Does quantum error correction enable practical fault tolerance? | Open (engineering) | Threshold theorem vs. overhead |
| Can classical analysis fully characterize the quantum advantage landscape? | Resolved: NO (Theorem 1, conditional on BPP ≠ BQP) | Huang et al. Theorem 1 |

---

## Active Paradigms

### Paradigm A: Gate-Model Quantum Computing (Dominant)
**Key advocates:** Google, IBM, IonQ, Rigetti, Quantinuum, AWS
**Foundation:** BPP ≠ BQP, Shor's algorithm, fault tolerance
**Status:** Active, well-funded ($35B+ cumulative), zero commercial machines
**Critique:** Pseudo-advantages, QEC overhead, unproven complexity assumptions

### Paradigm B: Quantum Sensing (Growing)
**Key advocates:** Academia, national labs, defense
**Foundation:** Physical laws (Heisenberg limit, standard quantum limit)
**Status:** Real advantages demonstrated (LIGO, NV centers, atomic clocks)
**Critique:** Asymptotic advantage fragile under noise (HNLS); most successes are innate sensitivity, not entanglement-enhanced

### Paradigm C: Post-Classical Alternatives (Emerging)
**Key advocates:** QNFO, neuromorphic/optical/thermodynamic computing communities
**Foundation:** Joules per solution, substrate-problem matching
**Status:** Early-stage, underfunded relative to gate-model
**Critique:** No demonstrated commercial success either; largely theoretical

### Paradigm D: Skeptical/Honest Framework (Huang et al.)
**Key advocates:** Huang, Choi, McClean, Preskill
**Foundation:** Five keystone properties, Theorem 1
**Status:** New (August 2025), likely to be highly cited
**Critique:** Framework absent economic dimension; theorem conditional on BPP ≠ BQP

---

## Methodological Approaches

| Approach | Used By | Strength | Weakness |
|:---------|:--------|:---------|:---------|
| Complexity theory | Computational QC | Rigorous | Unproven base assumptions |
| Physical limits | QNFO, sensing community | Law-bound | May overstate constraints |
| Empirical benchmarking | IBM, Google | Data-driven | Moving target (classical keeps improving) |
| Meta-complexity | Huang et al. Theorem 1 | Formal | Narrow, conditional |
| Historical analogy | QNFO Institutional Reform | Pattern-matching | Different domains may have different dynamics |

---

## Domain Topology

```
                    Quantum Advantage Research
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
  Computational          Sensing/Learning      Communication
  (BPP ≠ BQP)           (Physical Law)        (Physical Law)
        │                     │                     │
   ┌────┴────┐          ┌────┴────┐           ┌────┴────┐
   │         │          │         │           │         │
Shor's   Quantum    Entanglement  Innate    QKD     Quantum
Alg.     Sim.      -Enhanced    Sensitivity         Compression
                    (LIGO,      (NV centers,
                     fragile)    atomic clocks)
```

**Key insight:** The foundation of each subdomain determines its epistemic status. Computational advantages rest on unproven conjectures; sensing advantages rest on verified physical laws but face noise limitations; communication advantages rest on information-theoretic bounds.
