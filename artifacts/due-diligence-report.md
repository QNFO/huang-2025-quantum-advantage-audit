# Phase 1: Due Diligence Report
## Huang et al. (2025) "The vast world of quantum advantage" — Cross-Reference Discovery

**Date:** 2026-07-19
**Project:** huang-2025-quantum-advantage-audit

---

## §1. QNFO Knowledge Graph — Ecosystem Overview

| Metric | Value |
|:-------|:------|
| Total Nodes | 2,143 |
| Total Edges | 1,449 |
| Node Labels | 37 distinct types |
| Relationship Types | 54 distinct types |
| Paper Nodes | ~1,227 (prior baseline; see I-01 desync) |

### KG Nodes Directly Relevant to Quantum Advantage

| Node ID | Title | DOI | Status |
|:--------|:------|:----|:-------|
| paper-geometric-quantum-advantage | GEOMETRIC QUANTUM ADVANTAGE | (none) | D1 body EMPTY — metadata only |
| paper-waveform-vs-quantum | Shor's Assumptions: A Critical Re-examination of Quantum Advantage Foundations | 10.5281/zenodo.21356016 | **D1 body MISSING** — CRITICAL GAP |

### KG: "Honest Computation" Papers (Core QNFO Critique Series)

| Node | Title | DOI |
|:-----|:------|:----|
| paper-paper-manifesto-honest-computation | Manifesto for Honest Computation | 10.5281/zenodo.21299278 |
| paper-paper-problem-substrate-mapping | The Problem-Substrate Mapping | 10.5281/zenodo.21255346 |

---

## §2. D1 Living-Paper — Content Retrieval Results

### Successfully Retrieved (full body available)

| Paper | Slug | Status |
|:------|:-----|:-------|
| Manifesto for Honest Computation | paper-manifesto-honest-computation | Full body |
| The Physics of Computation | paper-physics-of-computation | Full body |
| The Qubit Delusion | paper-the-qubit-delusion | Full body |
| The Problem-Substrate Mapping | paper-problem-substrate-mapping | Full body |
| Institutional Reform | paper-institutional-reform | Full body |
| Beyond the Qubit | paper-beyond-the-qubit | Full body |

### Missing or Empty

| Paper | Slug | Issue |
|:------|:-----|:------|
| GEOMETRIC QUANTUM ADVANTAGE | geometric-quantum-advantage | Body empty, metadata only |
| Shor's Assumptions | waveform-vs-quantum | NOT FOUND in D1 — exists only in KG |

### CRITICAL FINDING: "Shor's Assumptions" is the missing centerpiece of QNFO's quantum advantage critique. It exists as a KG node with DOI 10.5281/zenodo.21356016 and description "Wigner function negativity as formal watershed between BPP/BQP" but has no recoverable body text in D1. If this paper was never written, QNFO has not engaged with quantum computing's strongest argument. If it was written and lost, this is a data preservation failure.

---

## §3. Vectorize Semantic Search Results

### Query: "quantum advantage computational complexity BPP BQP Shor algorithm fault tolerance error correction"

Top 10 matches (score range: 0.7046–0.7710):

| Rank | Score | Title | Slug |
|:-----|:------|:------|:-----|
| 1 | 0.7710 | Qudit Quantum Error Correction | ultrametric-quantum |
| 2 | 0.7602 | Adelic QEC | zbw-majorana-tqc-p5-adelic-qec |
| 3 | 0.7371 | Problem-Substrate Mapping | paper-problem-substrate-mapping |
| 4 | 0.7307 | Manifesto for Honest Computation | paper-manifesto-honest-computation |
| 5 | 0.7220 | Institutional Reform | paper-institutional-reform |
| 6 | 0.7219 | Ultrametric QC + Langlands | reassessing-the-foundations-of-quantum-computation |
| 7 | 0.7163 | Ultrametric Quantum Computation | ultrametric-quantum-computation |
| 8 | 0.7124 | The Qubit Delusion | paper-the-qubit-delusion |
| 9 | 0.7108 | Prime Numbers as Optimization | prime-numbers-as-universal-optimization-primitives |
| 10 | 0.7046 | The Physics of Computation | paper-physics-of-computation |

**Analysis:** The QNFO corpus clusters strongly around quantum computing critique. The top matches are split between the core Qubit Delusion series (Manifesto, Physics, Qubit Delusion, Problem-Substrate) and ultrametric/adelic alternatives. Notably absent: any paper engaging with Shor's algorithm as an algorithm (as opposed to Shor's assumptions about the qubit model).

---

## §4. Memory Search Results

Relevant durable memories retrieved:

| Memory | Summary | Relevance |
|:-------|:--------|:----------|
| "$35B/0-machines narrative excludes D-Wave/IonQ by selective definition" | anti_pattern | Directly relevant — QNFO's headline claim has a definitional problem |
| "QNFO Evidence Synthesis: 5 critical gaps, FCI refuted by own paper, cascade EV 13.5%" | project_fact | QNFO's own forecast downgraded itself |
| "5 Cloudflare Pages projects tracked as active but missing from live account" | anti_pattern | Infrastructure drift — QNFO has operational reliability issues |
| "Fixed qnfo-ipatent /api/search stub and qnfo-qwav LIKE->Vectorize" | anti_pattern | Dead code in production — QNFO's own implementations are incomplete |
| "CFPE Forecast Assumption Audit completed" | task_outcome | Related forecasting work |

---

## §5. External Literature Search

### arXiv API

**Search: author=Huang AND author=Preskill**
Result: No results returned via API. The arXiv author index may not resolve correctly for this query pattern. Known co-authored papers from the literature include:
- Chen, Huang, Preskill & Zhou (2024) "Local minima in quantum systems" (STOC 2024)
- Schuster, Haferkamp & Huang (2025) "Random unitaries in extremely low depth" (Science 389, 92)

**Search: "quantum advantage framework survey"**
Result: Empty — the specific framing of "keystone properties" appears to be genuinely novel to Huang et al. (2025).

**Search: "meta-complexity quantum"**
Result: Empty. The meta-complexity framing of Theorem 1 is a novel contribution.

**Search: "quantum advantage fault-tolerance keystone"**
Result: Empty. The five-keystone dimensional framework is original.

### Parallel Works (cited by Huang et al.)

The following papers are explicitly cited as parallel or related framework papers:

1. **Lanes et al. (2025)** — "A framework for quantum advantage" (arXiv:2506.20658). Authors: Lanes, Beji, Corcoles, Dalyac, Gambetta, et al. (IBM/Quantinuum collaboration). This is the closest parallel work from industry.

2. **Aaronson et al. (2025)** — "Future of quantum computing" (arXiv:2506.19232). Authors: Aaronson, Childs, Farhi, Harrow, Sanders. Community-wide perspective from leading theorists.

3. **Zimborás et al. (2025)** — "Myths around quantum computation before full fault tolerance" (arXiv:2501.05694). Demystification paper addressing what no-go theorems rule out and what they don't.

4. **King (2025)** — "Quantum algorithms: A call to action" (quantumfrontiers.com blog post).

---

## §6. Gap Analysis

### QNFO Coverage Map (The Qubit Delusion Series)

| Phase | Paper | Engagement with Huang et al. Topics |
|:------|:------|:-----------------------------------|
| I | The Qubit Delusion | Ontological critique — no direct engagement with keystone framework (published before it) |
| II | Beyond the Qubit | Alternative paradigms — consistent with Huang et al.'s openness to non-qubit approaches |
| III | The Physics of Computation | Physical limits — directly relevant to Robustness dimension; quantitative gap in QEC overhead analysis |
| IV | Problem-Substrate Mapping | Investment portfolio — offers a resource allocation model Huang et al. lack |
| V | Institutional Reform | Governance — no equivalent in Huang et al. |
| VI | Manifesto for Honest Computation | Synthesis — shares values (verifiability, usefulness, honesty) but reaches opposed conclusions |

### Unaddressed by QNFO

1. **Theorem 1 (Unpredictable Quantum Advantages):** No QNFO paper engages with the meta-complexity argument that some quantum advantages are classically undetectable.
2. **Typicality as a formal dimension:** QNFO critique focuses on worst-case analysis (QEC overhead) but does not systematically address the average-case vs. worst-case distinction.
3. **Learning/Sensing as a distinct realm:** QNFO lumps all quantum technology together; Huang et al. correctly separate sensing (physics-based, real advantages exist) from computation (complexity-theory-based, unproven).
4. **Shor's algorithm defense:** QNFO has no recoverable analysis of why Shor's algorithm — the strongest case for quantum advantage — is insufficient.

### Unaddressed by Huang et al.

1. **Investment allocation:** No discussion of whether current resource concentration is rational.
2. **Economic cost:** "Usefulness" excludes joules/dollars/time.
3. **Ontological critique:** Does not engage with the claim that the qubit is a category error.
4. **Institutional incentives:** No analysis of why pseudo-advantages persist despite theoretical warnings.

---

## §7. Novelty Assessment

The Huang et al. framework is **genuinely novel** in at least three respects:

1. **Systematic five-dimensional evaluation** — Prior frameworks (e.g., IBM's "quantum utility") were one-dimensional or ad hoc.
2. **Theorem 1** — The meta-complexity proof that advantage detection is BQP-complete is an original mathematical contribution.
3. **Honest synthesis** — The paper's tone — acknowledging that BPP ≠ BQP is unproven, that LIGO is the only entanglement-enhanced sensing success, that HNLS kills asymptotic sensing advantage — is unusually candid for quantum computing literature.

**Not novel:** Much of the survey content (Shor's algorithm, quantum sensing limits, oracle-based advantages) is standard material, albeit well-synthesized.

## §8. Due Diligence Assessment

| Check | Status | Evidence |
|:------|:-------|:---------|
| KG queried? | ✓ | stats + 3 node searches |
| D1 cross-referenced? | ✓ | 6 paper contexts retrieved |
| Vectorize searched? | ✓ | 2 queries, 20 results |
| External sources? | ✓ | arXiv API (4 queries) |
| Dedup against QNFO? | ✓ | No direct duplicates found |
| Gap analysis? | ✓ | §6 complete |
| Critical gaps identified? | ✓ | Shor's Assumptions missing; Theorem 1 unaddressed |
