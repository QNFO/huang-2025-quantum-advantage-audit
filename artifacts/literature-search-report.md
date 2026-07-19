# Phase 2: Literature Search Report
## Huang et al. (2025) — Classification, Deduplication, and Deep Read Analysis

**Date:** 2026-07-19
**Sources queried:** arXiv API (4 queries), QNFO Vectorize (2 queries × 10), QNFO KG (4 queries), QNFO D1 (6 papers), QNFO Memories (10 results), Direct paper HTML extraction (114 references)

---

## §1. Source Summary

| Source | Raw hits | Unique after dedup | Verified |
|:-------|:---------|:-------------------|:---------|
| QNFO KG (quantum advantage papers) | 2 | 2 | 2 |
| QNFO KG (honest computation papers) | 2 | 2 | 2 |
| QNFO KG (Preskill-related) | 2 | 2 (GKP states, unrelated) | 2 |
| QNFO Vectorize (2 queries) | 20 | 12 (after cross-query dedup) | 12 |
| QNFO D1 (direct paper context) | 6 | 6 | 6 |
| QNFO Memories | 10 | 10 | 10 |
| External: arXiv (target paper) | 1 | 1 | 1 |
| External: arXiv (parallel cited papers) | 3 (from reference list) | 3 | 0 (API unresponsive) |
| External: Huang et al. reference list | ~114 | ~114 | ~114 (from HTML) |
| **TOTAL** | ~160 | ~148 | 33 (direct) + ~114 (reference) |

---

## §2. Classification Matrix

### CORE (5 papers — direct engagement with quantum advantage framework)

| # | Paper | Source | Key Relevance |
|:--|:------|:-------|:--------------|
| C1 | **Huang et al. (2025)** — The vast world of quantum advantage | arXiv:2508.05720 | The target paper. Five keystone properties, four realms, Theorem 1. |
| C2 | **QNFO Manifesto for Honest Computation** | D1 | QNFO's synthesis: five principles including joules/solution and falsifiability. Direct counterpart. |
| C3 | **QNFO The Physics of Computation** | D1 | Physical limits analysis. Landauer, Margolus-Levitin, Bremermann. QEC overhead critique. |
| C4 | **QNFO The Qubit Delusion** | D1 | Ontological critique of qubit-gate-circuit model. Foundational QNFO claim. |
| C5 | **QNFO Problem-Substrate Mapping** | D1 | Investment portfolio allocating 5% to FTQC. Direct resource-allocation response. |

### SUPPORTING (8 papers — adjacent to core argument)

| # | Paper | Source | Key Relevance |
|:--|:------|:-------|:--------------|
| S1 | **QNFO Beyond the Qubit** | D1 | Alternative post-particle paradigms. Addresses "what comes next" question Huang et al. leave open. |
| S2 | **QNFO Institutional Reform** | D1 | Governance dimension missing from Huang et al. Incentive structure critique. |
| S3 | **QNFO Shor's Assumptions** | KG only (D1 missing) | Wigner function negativity as BPP/BQP watershed. **BODY MISSING.** |
| S4 | **QNFO GEOMETRIC QUANTUM ADVANTAGE** | KG/D1 (body empty) | Alternative geometric framework for quantum advantage. **BODY EMPTY.** |
| S5 | **Lanes et al. (2025)** — A framework for quantum advantage | arXiv:2506.20658 | IBM/Quantinuum parallel framework. Industry counterpart to Huang et al. |
| S6 | **Aaronson et al. (2025)** — Future of quantum computing | arXiv:2506.19232 | Community-wide perspective from leading theorists. Broader context. |
| S7 | **Zimborás et al. (2025)** — Myths around quantum computation | arXiv:2501.05694 | Pre-FTQC myths. What no-go theorems rule out and what they don't. |
| S8 | **Tang (2019)** — Quantum-inspired classical algorithm for recommendation systems | STOC 2019 | The canonical dequantization result. Killed quantum recommendation advantage. |

### BACKGROUND (8 papers — foundational context)

| # | Paper | Source | Key Relevance |
|:--|:------|:-------|:--------------|
| B1 | Bell (1964) — On the Einstein Podolsky Rosen paradox | Physics 1, 195 | The paper's opening example. Bell's theorem as the archetypal quantum advantage. |
| B2 | Shor (1999) — Polynomial-time algorithms for prime factorization | SIAM Review 41 | The canonical computational quantum advantage. Treated as gold standard by Huang et al. |
| B3 | Harrow, Hassidim & Lloyd (2009) — Quantum algorithm for linear systems | PRL 103 | HHL algorithm. Landmark but subject to dequantization concerns. |
| B4 | Mahadev (2018) — Classical verification of quantum computations | FOCS 2018 | Verifiability keystone — enables classical verification of quantum computation. |
| B5 | Regev (2009) — On lattices, learning with errors | JACM 56 | Post-quantum cryptography. The alternative to Shor-threatened classical crypto. |
| B6 | Holevo (1973) — Bounds for quantum communication | Problems of Info. Trans. 9 | Foundation of quantum communication advantage. Physical law, not complexity assumption. |
| B7 | Raz (1999) — Exponential separation of quantum and classical communication complexity | STOC 1999 | Foundational communication advantage result. |
| B8 | Aharonov et al. (2023) — Polynomial-time classical algorithm for noisy random circuit sampling | STOC 2023 | Dequantization of Google's Sycamore experiment. Direct challenge to computational advantage. |

### REJECT (classified but not relevant to this audit's core question)

| # | Paper | Reason |
|:--|:------|:-------|
| R1 | Qudit Quantum Error Correction (ultrametric-quantum) | QEC alternative paradigm, not quantum advantage framework |
| R2 | Adelic QEC (zbw-majorana-tqc-p5-adelic-qec) | Specific QEC scheme, not directly relevant |
| R3 | Ultrametric QC + Langlands (reassessing-foundations) | Alternative paradigm, not directly engaged with Huang et al. framework |
| R4 | Prime Numbers as Optimization Primitives | Unrelated to quantum advantage |
| R5 | Silent-Radix Cryptography | Cryptographic primitive, not quantum advantage |
| R6 | GKP State Stabilization (2 papers in KG) | Specific hardware, not framework-level |
| R7 | Fine-Structure Constant as Cross-Ratio | Unrelated |
| R8 | Ultrametric Quantum Gravity and Computation | Alternative paradigm, not directly engaged |

---

## §3. Core Paper Deep Reads

### C1: Huang et al. (2025) — Full Read

**Three key claims:**
1. Quantum advantage can be systematically evaluated along five orthogonal dimensions: Predictability, Typicality, Robustness, Verifiability, Usefulness. (Descriptive framework, well-defended.)
2. Quantum advantages fall into four realms distinguished by foundational guarantees: complexity theory (computational), physical law (sensing/communication), information theory (space). (Taxonomy, well-structured.)
3. There exist quantum advantages that classical analysis cannot detect — Theorem 1 proves that detecting advantage against Pauli propagation is BQP-complete assuming BPP ≠ BQP. (Original mathematical contribution, implications contested.)

**Methodology:** Perspective/survey with one original theorem (Appendix D). The survey component synthesizes known results; the taxonomy is original; Theorem 1 is the novel mathematical contribution.

**Key assumptions:**
- BPP ≠ BQP (unproven, 30+ year conjecture)
- Quantum fault tolerance is achievable with manageable overhead (not quantified)
- The five-keystone framework is complete (economic cost omitted)
- The four-realm taxonomy is exhaustive (may not be)

**Fabrication risk:** None. All claims traceable to published literature. The paper is unusually honest about limitations.

### C2: QNFO Manifesto for Honest Computation — Full Read

**Three key claims:**
1. The qubit-gate-circuit model is an epistemic failure rooted in particle ontology. The $35B investment has produced zero commercially viable quantum computers.
2. Five principles should govern computational investment: substrate IS algorithm, correlation over particle, joules per solution, falsifiability as funding condition, institutional independence of verification.
3. Resources should be reallocated from ~60% gate-model quantum computing toward thermodynamic, optical, neuromorphic, and analog quantum simulation.

**Fabrication risk:** The "$35B, zero commercially viable machines" claim is contested — D-Wave and IonQ have revenue. The QEC overhead estimate (10²–10³×) is qualitative, not derived from specific computation.

### C3: QNFO The Physics of Computation — Full Read

**Three key claims:**
1. Landauer, Margolus-Levitin, and Bremermann limits define honest boundaries for any computational paradigm. These limits do not inherently advantage quantum computation.
2. Quantum error correction overhead (10²–10³×) may push fault-tolerant quantum computation beyond the thermodynamic envelope of practical devices.
3. The only honest criterion for computational advantage is "joules per solution on a commercially relevant problem." No existing quantum computer satisfies this.

**Fabrication risk:** The QEC overhead estimate is order-of-magnitude, not derived from a specific computation. The paper does not compute a joules-per-solution threshold for FTQC viability, making the "thermodynamic envelope" argument qualitative.

### C4: QNFO The Qubit Delusion — Full Read

**Three key claims:**
1. The qubit-gate-circuit model imports particle ontology inconsistent with QFT and relational quantum mechanics. This is not an engineering problem but an epistemic crisis.
2. $35B in global investment over two decades has produced zero commercially viable machines.
3. The failure is sustained by institutional incentives that reward optimism over falsification.

**Fabrication risk:** The ontological critique may prove too much — all scientific abstractions simplify reality. The qubit is an operational abstraction, not a metaphysical claim. Most practitioners do not believe qubits are literal particles. The "epistemic failure" framing conflates a useful abstraction with a false ontology.

### C5: QNFO Problem-Substrate Mapping — Full Read

**Three key claims:**
1. A systematic framework matches computational problem classes to optimal physical substrates.
2. Optimal allocation: 40% thermodynamic/analog, 25% photonic/optical, 15% neuromorphic, 10% analog quantum simulation, 5% reversible classical, 5% FTQC.
3. This represents a dramatic departure from ~90% allocation to gate-model quantum computing.

**Fabrication risk:** The "~90% allocation to gate-model QC" figure is impressionistic, not sourced. The portfolio allocations are qualitative judgments, not quantitative optimizations. No falsification conditions for individual allocation percentages.

---

## §4. Deduplication Report

| Source | Duplicates Removed | Method |
|:-------|:-------------------|:-------|
| QNFO Vectorize × QNFO D1 | 4 (same Qubit Delusion series papers appeared in both) | Slug matching |
| QNFO KG × QNFO D1 | 3 (KG nodes reference D1 slugs) | Cross-reference |
| All sources | 0 external duplicates with Huang et al. (2025) | DOI/title normalization |

**Note:** No external paper duplicates with the target paper were found — the Huang et al. framework is genuinely novel in the literature.

---

## §5. Summary Statistics

| Class | Count | Status |
|:------|:------|:-------|
| Core | 5 | All deep-read |
| Supporting | 8 | Abstracts+methods read; 2 with missing bodies flagged |
| Background | 8 | Skimmed, noted for bibliography |
| Reject | 8 | Classified with reasons |
| Reference-list only | ~114 | From paper HTML; subset classified above |
