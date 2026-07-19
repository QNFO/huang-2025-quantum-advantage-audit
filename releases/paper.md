---
title: "The Vast World of Quantum Advantage — A Full-Spectrum Audit"
subtitle: "Critical engagement with Huang, Choi, McClean & Preskill (2025) and QNFO's quantum computing critique"
author: "QNFO Research Collective"
date: "2026-07-19"
license: "QNFO Unified License Agreement (QNFO-ULA)"
doi: "10.5281/zenodo.21440671"
status: "published"
---

# 1. Introduction

Huang, Choi, McClean & Preskill (2025) have produced the most intellectually honest document about quantum advantage to emerge from the quantum computing establishment. Their Perspective paper — "The vast world of quantum advantage" (arXiv:2508.05720) — constructs a systematic framework for evaluating quantum advantage claims through five "keystone" properties (Predictability, Typicality, Robustness, Verifiability, Usefulness), surveys four distinct realms where quantum advantage can manifest, and proves a genuinely original theorem: that detecting quantum advantage is itself classically hard, assuming BPP ≠ BQP.

The paper is unusual in its candor. It acknowledges that BPP ≠ BQP — the foundational conjecture of quantum computing — is unproven after 30 years. It admits that quantum recommendation systems, once heralded as an exponential quantum advantage, were dequantized by Ewin Tang's classical algorithms (2019, 2021). It states that "finding examples where entanglement enhances sensing capabilities in a real-world setting has been famously elusive," with LIGO's squeezed-light gravitational wave detection as the single exception. It identifies the Hamiltonian-not-in-Lindbladian-Span (HNLS) criterion as showing that asymptotic quantum sensing advantage is "fundamentally unattainable even with quantum error correction" in generic noise scenarios. And it concedes that "we have never tested quantum mechanics at the complexity frontier where thousands of particles become massively entangled."

These are not the admissions of true believers. They are the admissions of scientists trying to be honest about what they know and do not know.

This audit subjects both the Huang et al. framework and QNFO's own prior critiques to symmetric scrutiny. We find that the two frameworks converge on core values — verifiability, usefulness, honesty — but diverge on the implications of uncertainty. We find that QNFO's strongest arguments remain intact (the missing economic dimension, the unproven complexity foundation, the pseudo-advantage problem) but that QNFO has significant vulnerabilities of its own: an ontological critique that proves too much, an unquantified thermodynamic analysis, a missing engagement with Shor's algorithm, and — most seriously — a failure to apply its own falsifiability standards to itself.

We also find that Theorem 1 — the paper's most original contribution — represents the most sophisticated challenge to QNFO's epistemic posture yet produced. If some quantum advantages are classically undetectable, then QNFO's implicit claim — that classical analysis can reliably map the quantum advantage landscape — may rest on a false premise.

# 2. The Five Keystone Properties

The paper's primary conceptual contribution is a five-dimensional framework for assessing any claimed quantum advantage.

**Predictability:** Evidence that, given the necessary quantum technology, we will achieve capabilities fundamentally beyond classical reach. The paper emphasizes that this requires rigorous, substantive, and quantifiable evidence — not plausible intuition. Tang's dequantization of quantum recommendation systems exemplifies the failure mode.

**Typicality:** The advantage must hold for typical or average-case instances, not merely worst-case pathological ones. Pauli propagation can efficiently simulate *most* quantum circuits; the quantum advantage resides only in a specific subset of "magic" circuits.

**Robustness:** The advantage must persist under hardware noise and imperfections. For computation, the threshold theorem provides theoretical assurance — but with unknown overhead. For sensing, the HNLS criterion shows that asymptotic advantage is fundamentally unattainable in generic noise scenarios.

**Verifiability:** Results must be independently checkable. The paper's admission here is striking: "We have never tested quantum mechanics at the complexity frontier." Our confidence in quantum theory comes from low-entanglement experiments; the regime where quantum computing operates is untested.

**Usefulness:** The advantage must provide practical value to a user who does not care whether the underlying technology is classical or quantum. This criterion aligns closely with QNFO's "joules per solution" — though the paper omits cost entirely.

# 3. Theorem 1: The Unpredictability Result

The paper's most original and philosophically consequential contribution is Theorem 1. Informally: assuming BPP ≠ BQP, the decision problem "does this specific quantum circuit outperform Pauli propagation classical simulation?" is in BQP but not in BPP. Quantum computers can answer it efficiently; classical computers cannot.

The proof strategy (Appendix D): the problem is quantumly easy (run both methods on random instances and compare), and if it were classically easy, one could solve all BQP problems classically — contradicting BPP ≠ BQP.

The paper draws a radical implication: "There are plenty of problems with genuine quantum advantages such that we cannot predict the advantage using only classical technology. Paradoxically, to fully map out the landscape of quantum advantages, we must use the very quantum technologies whose power we are trying to characterize."

This is the most sophisticated challenge to QNFO's epistemic posture yet produced. However, the theorem has important limitations: it is conditional on the unproven BPP ≠ BQP conjecture, it applies to one specific classical method (Pauli propagation), and it does not generalize to detecting commercially useful or physically realizable quantum advantage. QNFO's strongest response is that unpredictability justifies diversification, not concentration.

# 4. QNFO's Vulnerabilities

This audit documents five structural weaknesses in QNFO's framework that the Huang et al. paper exposes — not by direct refutation but by revealing gaps.

**First: The ontological critique proves too much.** "The Qubit Delusion" argues that the qubit-gate-circuit model is an epistemic failure — a projection of particle ontology onto field-theoretic reality. But if every abstraction that simplifies reality is an epistemic failure, then all of science is guilty. The Schrödinger equation abstracts away from QFT; the ideal gas law abstracts away from molecular interactions; Newton's laws abstract away from relativity. The qubit is an operational abstraction, not a metaphysical claim. Most quantum computing practitioners do not believe qubits are literal particles. QNFO must either refine this argument — identifying specifically which predictions the qubit model gets wrong — or retire it as its central philosophical claim.

**Second: The QEC overhead argument is qualitative, not quantitative.** "The Physics of Computation" estimates error correction overhead at 10²–10³× and claims this pushes FTQC "beyond the thermodynamic envelope of practical devices." But the paper never computes: what joules per solution would make FTQC viable, and at what overhead factor does FTQC cross that threshold? Without this, the argument is a gesture toward rigor, not rigor itself. QNFO demands quantitative falsifiability from quantum computing but has itself produced a qualitative objection dressed in quantitative language.

**Third: The Shor's Assumptions gap is critical.** QNFO's Knowledge Graph contains a paper titled "Shor's Assumptions: A Critical Re-examination of Quantum Advantage Foundations" (DOI: 10.5281/zenodo.21356016) with the description "Wigner function negativity as formal watershed between BPP/BQP." This paper has no recoverable body text in D1. This is the central missing piece of QNFO's intellectual architecture. Huang et al. treat Shor's algorithm as the gold standard for quantum computational advantage — satisfying all five keystone properties. If QNFO claims that quantum computing investment is misallocated, it must explain why Shor's algorithm does not justify the investment. That explanation is missing.

**Fourth: The $35B/zero-machines claim depends on a contested definition.** QNFO's headline claim — "$35 billion, zero commercially viable machines" — selectively excludes D-Wave and IonQ revenue. This does not make the claim false, but it does make it definitional rather than empirical. A more honest formulation would specify the exclusion criteria and acknowledge the gray area.

**Fifth: QNFO has not published falsification conditions for its own claims.** The Manifesto's Principle 4 demands "falsifiability as a condition of funding" for quantum computing. When would QNFO acknowledge that its own claims are falsified? If a fault-tolerant quantum computer performs a commercially useful computation at lower joules per solution than any classical alternative before 2035, does QNFO admit error? If not, what would?

# 5. Huang et al.'s Limitations

The paper, for all its honesty, has significant limitations that QNFO correctly identifies.

**The economic dimension is entirely absent.** "Usefulness" is defined without reference to cost. Shor's algorithm satisfies all five keystone properties for the abstract mathematical problem of factoring — but at RSA-2048 scale, it requires millions of physical qubits, billions of dollars, and decades of development. Is that a practical advantage? The framework cannot answer because it never asks.

**Theorem 1 does not prove what the paper claims it proves.** The theorem applies to Pauli propagation — one specific classical method. The rhetorical extension to "predicting quantum advantage against any classical method" is not proven. Meta-complexity results are notoriously fragile and rarely generalize in the way the paper implies.

**The five-keystone framework is descriptive, not predictive.** It tells you what properties an ideal quantum advantage should have. It does not tell you which candidate advantages are likely to satisfy them. It is a grading rubric, not a forecasting tool. For resource allocation decisions — which are forward-looking — a framework that cannot generate calibrated probabilities has limited utility.

**The paper conflates "unpredictable" with "likely to exist."** Theorem 1 proves that some quantum advantages may be classically unpredictable. It does not prove they exist. It does not prove they are likely. It does not prove they are economically valuable. The rhetorical framing — "a landscape far richer than what we can currently foresee" — implies abundance without evidence.

**The paper never addresses institutional incentives.** The pseudo-advantage problem is a recurring theme — apparent quantum advantages that dissolve under classical scrutiny. But the paper never asks *why* this pattern persists. QNFO's Institutional Reform paper provides an answer: the incentive structure rewards narrative production over falsification. Huang et al. lack the institutional dimension that would explain why their own five-keystone framework is necessary — and why it will be difficult to enforce.

# 6. The Convergence

Despite their differences, the two frameworks converge on more than they diverge on.

Both identify pseudo-advantages as the central risk. Both demand verifiability and usefulness as non-negotiable criteria. Both acknowledge the unproven status of BPP ≠ BQP. Both recognize that classical algorithms are advancing relentlessly and that many claimed quantum advantages exist in a shrinking window. Both seek honest frameworks for evaluating technological claims against empirical evidence rather than narrative.

The divergence is primarily about the implications of uncertainty. Huang et al. view quantum advantage as a vast, partially uncharted territory whose exploration requires quantum technology itself. QNFO views the same uncertainty as grounds for caution, diversification, and institutional reform. Both positions are defensible. Neither is obviously wrong.

# 7. The Deepest Problem

The deepest problem — one that neither framework adequately addresses — is that quantum computing may be an undecidable research program. That is: it may be impossible, even in principle, to determine in advance whether it will succeed.

If Theorem 1 generalizes (a big "if"), then the question "will quantum computing deliver commercially useful advantage?" may be as hard as building a quantum computer — meaning it cannot be answered by analysis, only by building. If so, then both the quantum computing industry narrative (which claims to know it will succeed) and the QNFO critique (which claims to know it will not) are epistemically overconfident.

This would be uncomfortable for everyone. It would mean the $35 billion has been spent on a bet that could not have been evaluated ex ante. It would mean QNFO's confident dismissal is justified by evidence but not by logic. It would mean we are all — advocates and skeptics alike — operating in the dark.

The most honest position available at this moment is: **we do not know whether quantum computing will deliver commercially useful advantage.** Both the confident claims of the quantum computing industry and the confident dismissals of QNFO overstate what the evidence supports.

# 8. Recommendations

Based on this full-spectrum audit, we recommend:

1. **Recover or write the "Shor's Assumptions" paper.** This is the central missing piece of QNFO's intellectual architecture. Without it, QNFO has not engaged with quantum computing's strongest argument.

2. **Publish symmetric falsification conditions** for QNFO's own claims. Specify the evidence that would cause QNFO to revise the 5% FTQC allocation, the Qubit Delusion thesis, the joules-per-solution threshold, and the ontological critique.

3. **Compute the quantitative joules-per-solution threshold for FTQC viability.** Convert the qualitative "thermodynamic envelope" argument into a falsifiable, quantitative claim. At what joules per solution does FTQC become viable? At what QEC overhead factor?

4. **Refine or retire the ontological critique.** If the argument is that the qubit is a useful abstraction for some purposes and misleading for others, state it in those terms. If the argument is that the qubit is fundamentally wrong, defend it against the obvious counterexamples.

5. **Engage with Theorem 1 directly.** Either show that the generalization to commercially useful quantum advantage is invalid, argue that unpredictability justifies diversification, or acknowledge that QNFO's epistemic posture may need revision.

6. **Survey actual investment allocation.** Replace the impressionistic "~90% to gate-model QC" with a systematic survey. QNFO's investment critique is stronger if the data support it.

7. **Track the calibration register.** This is the test of whether QNFO is a research program or a position. The predictions are registered. The clock is running.

# 9. Conclusion

Huang, Choi, McClean & Preskill (2025) have produced the most honest document about quantum advantage to emerge from the quantum computing establishment. It is not a victory lap — it is a truce offering. It acknowledges the pseudo-advantage problem, admits the fragility of sensing advantage under noise, concedes that BPP ≠ BQP is unproven, and opens the possibility that the most important quantum advantages are ones we cannot currently conceive.

QNFO's response should be correspondingly honest. QNFO's framework has genuine strengths: the joules-per-solution criterion, the emphasis on falsifiability, the portfolio approach to technology investment, the recognition that classical algorithms are advancing rapidly. But QNFO also has significant weaknesses that this audit has documented.

The most honest position available is not certainty in either direction but acknowledgment of irreducible uncertainty. If Theorem 1 is correct — if some quantum advantages are classically undetectable — then the only intellectually defensible strategy is a broad, diversified portfolio of post-classical computing research, with honest, time-bound success criteria applied symmetrically to all approaches, including QNFO's own favored alternatives.

---

**Author:** QNFO Research Collective
**Date:** 2026-07-19
**License:** QNFO-ULA: https://legal.qnfo.org/

## References

- Huang, H.-Y., Choi, S., McClean, J. R., & Preskill, J. (2025). *The vast world of quantum advantage.* arXiv:2508.05720.
- QNFO Research Collective. *Manifesto for Honest Computation.* DOI: 10.5281/zenodo.21299278.
- QNFO Research Collective. *The Physics of Computation.* DOI: (pending).
- QNFO Research Collective. *The Qubit Delusion.* DOI: (pending).
- QNFO Research Collective. *The Problem-Substrate Mapping.* DOI: 10.5281/zenodo.21255346.
- Tang, E. (2019). A quantum-inspired classical algorithm for recommendation systems. STOC 2019.
- Bell, J. S. (1964). On the Einstein Podolsky Rosen paradox. Physics 1, 195.
- Shor, P. W. (1999). Polynomial-time algorithms for prime factorization. SIAM Review 41, 303.
