# Engaging Theorem 1: Unpredictability Justifies Diversification

**QNFO Research Collective | 2026-07-19**
**Triggered by huang-2025-quantum-advantage-audit Recommendation 5**

---

## 1. The Challenge

Huang, Choi, McClean & Preskill (2025) prove Theorem 1: assuming BPP ≠ BQP, the decision problem "does this specific quantum circuit outperform Pauli propagation classical simulation?" is in BQP but not in BPP — quantum computers can answer it efficiently; classical computers cannot.

The paper draws a radical implication: "There are plenty of problems with genuine quantum advantages such that we cannot predict the advantage using only classical technology. Paradoxically, to fully map out the landscape of quantum advantages, we must use the very quantum technologies whose power we are trying to characterize."

This challenges QNFO's implicit claim — that classical analysis (thermodynamic limits, ontological critique, institutional forensics) can reliably map the quantum advantage landscape. If some advantages are classically undetectable, QNFO's map may have blind spots.

## 2. QNFO's Response: Diversification

QNFO's strongest response to Theorem 1 is already present in the Manifesto:

> "The rational investment response to these findings is a diversified portfolio across physical substrates, allocated in proportion to the evidence for each substrate-problem pair. Approximately 45% thermodynamic and analog... 25% optical... 20% neuromorphic... and only 5–10% fault-tolerant quantum."

This is exactly the strategy Theorem 1 implies. If the quantum advantage landscape is partially opaque to classical analysis, the epistemically defensible posture is:

1. **Maintain a small allocation** to the domain that classical analysis can't fully map (5–10% FTQC)
2. **Maximize the expected return** of the domain that IS classically analyzable (90–95% diversified)
3. **Adjust allocation as evidence accumulates** through the calibration register

Theorem 1 does not refute QNFO. It justifies QNFO's core recommendation.

## 3. Limitations of Theorem 1

Theorem 1 has three limitations that prevent it from undermining QNFO's classical analysis:

**Limitation 1: Single classical method.** The theorem applies to Pauli propagation — one specific classical simulation technique. It does NOT prove that no classical method can detect quantum advantage. The rhetorical extension to "any classical method" is not proven. Meta-complexity results are notoriously fragile and rarely generalize.

**Limitation 2: Conditional on BPP ≠ BQP.** The theorem inherits the same unproven premise (BPP ≠ BQP) that underlies quantum computing's foundational claims. If BPP = BQP, Theorem 1 is vacuously true (no quantum advantages exist to detect) — but that would collapse both Huang et al.'s framework AND the quantum computing industry's justification. The theorem is only interesting in the world where quantum computing works, and we don't know whether we live in that world.

**Limitation 3: Detection ≠ commercial viability.** Theorem 1 proves that detecting *some* quantum advantage may be classically hard. It does not prove that *commercially useful* quantum advantage will be classically undetectable. The gap between "mathematical advantage against Pauli propagation" and "commercially useful advantage against the best available classical methods" is the entire question.

## 4. The Diversification Argument, Formally

If Theorem 1 is correct (big if): the quantum advantage landscape is partially opaque to classical analysis. This implies:

P1. Some quantum advantages may be classically undetectable. (Theorem 1, conditional on BPP ≠ BQP)
P2. We cannot distinguish classically detectable from classically undetectable advantages without quantum hardware. (Theorem 1)
P3. We must allocate some resources to quantum hardware development to maintain the option of discovering classically undetectable advantages. (P1 + P2)
P4. The vast majority of claimed quantum advantages that WERE classically analyzable have been dequantized, qualified, or shown to lack commercial viability. (Empirical evidence: 15+ abelian HSP, Tang 2019/2021, D-Wave 2014)
P5. The resource allocation to quantum hardware should be proportional to the probability-weighted expected value of discovering classically undetectable, commercially viable advantages. (Expected utility)
C. The optimal allocation is a small but non-zero allocation to FTQC — exactly QNFO's 5–10% recommendation. (P3 + P4 + P5)

This is a constructive engagement with Theorem 1 that neither dismisses it nor concedes to it.

## 5. What Would Require Revision

QNFO's current analysis would need revision if:

1. **Theorem 1 is disproved or shown not to generalize.** If a classical method for detecting quantum advantage against arbitrary quantum circuits is found, the unpredictability argument collapses and QNFO's classical analysis becomes more complete.

2. **Classically undetectable, commercially useful quantum advantage is demonstrated.** If an FTQC device solves a commercially relevant problem at lower joules-per-solution than any classical alternative, and that advantage was NOT predicted by classical analysis, this would validate Theorem 1's implication AND demonstrate that QNFO's map had a consequential blind spot. Portfolio allocation would shift toward FTQC.

3. **The pattern of classical dequantization reverses.** If new quantum algorithms are discovered that resist classical dequantization for extended periods (≥60 months), QNFO's empirical analysis of the dequantization trend would need updating.

## 6. Conclusion

Theorem 1 does not refute QNFO. It justifies QNFO. The unpredictability of quantum advantage — the fact that classical analysis cannot map the entire landscape — is exactly why a diversified portfolio with a small FTQC allocation is the epistemically defensible strategy. QNFO arrived at this conclusion through thermodynamic analysis; Huang et al. arrived at it through complexity theory. The fact that two independent lines of reasoning converge on the same recommendation — diversify, but don't abandon — strengthens both.

---

*Document prepared by huang-2025-quantum-advantage-audit, QNFO Research Collective, 2026-07-19.*
*References: Huang et al. (2025) arXiv:2508.05720; Manifesto for Honest Computation (DOI: 10.5281/zenodo.21299278)*
