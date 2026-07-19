# Manifesto Corrections Applied (v1.1 Revision)

**Recommended to QNFO for next Manifesto version | 2026-07-19**
**Triggered by huang-2025-quantum-advantage-audit Recommendation 4**

---

## Background

The full-spectrum audit of QNFO's vulnerabilities against Huang et al. (2025) identified an inconsistency: QNFO's Knowledge Graph contains a Correction node (`correction-economic-narrative`, status: `applied`, 2026-07-17) acknowledging the $35B/0-machines claim "was misleading" and should be "Corrected to 'selective market exclusion'" — but the canonical Manifesto text in D1 and Zenodo was never updated.

Additionally, the red-team review found that the Manifesto's language ("epistemic failure," "$35 billion, zero machines") implies greater certainty than the underlying analysis supports. QNFO's own portfolio allocates 5–10% to FTQC — a hedged position, not a dismissal.

## Specific Corrections

### Correction 1: Preamble — "Not one commercially viable quantum computer exists"

**Current text (Manifesto, Preamble, ¶3):**
> Those claims have not been realized. Not one commercially viable quantum computer exists. Not one problem of genuine economic value has been solved faster, cheaper, or more accurately by a quantum computer than by a classical alternative.

**Recommended replacement:**
> Those claims have not been realized. Under the selective market exclusion criterion — which excludes annealers and analog devices that have generated commercial revenue without demonstrating classical speedup — no general-purpose fault-tolerant quantum computer has yet demonstrated commercially useful advantage. No problem of genuine economic value has been independently verified as solved faster, cheaper, or more accurately by a gate-model quantum computer than by the best available classical alternative.

### Correction 2: Preamble — "The failure is structural"

**Current text (Manifesto, Preamble, ¶4):**
> This is not a temporary setback. It is not a matter of insufficient funding, insufficient talent, or insufficient time. The failure is structural.

**Recommended replacement:**
> This is not a temporary setback, although it may also not be a permanent one. The protracted timeline — now entering its fourth decade with no commercially viable general-purpose quantum computer — is consistent with structural challenges beyond engineering difficulty. These include: institutional incentive systems that reward narrative production over falsifiable results; the neglect of fundamental thermodynamic limits in quantum computing roadmaps; and the absence of independent verification with enforcement mechanisms.

### Correction 3: §1.1 — "epistemic failure"

**Current text (Manifesto, §1.1, ¶1):**
> The qubit-gate-circuit model is an epistemic failure. It projects particle ontology onto a relational, field-theoretic reality.

**Recommended replacement:**
> The qubit-gate-circuit model imports an ontological assumption — particle ontology — that is inconsistent with the relational, field-theoretic framework of modern quantum field theory. While this does not make the model "wrong" as an operational abstraction (scaffolds serve legitimate representational purposes), it means that the model's conceptual foundations are not aligned with what we have learned about quantum reality since the mid-20th century. The distinction between scaffold and invariant — explained in detail in The Qubit Delusion §2.1 — is the relevant framework, not a blanket charge of "failure."

### Correction 4: §1.1 — Narrative production claim

**Current text (Manifesto, §1.1, ¶2):**
> The $35 billion quantum computing industry has optimized for narrative production, not computational output...

**Recommended addition after this sentence:**
> This claim is qualified: it applies to a pattern of institutional behavior, not to individual researchers. Many quantum computing researchers produce rigorous, falsifiable work. The critique targets the incentive structure, not the people operating within it.

---

## Meta-Correction: D1 Body vs. Zenodo

The D1 living-paper record for the Manifesto (`paper-manifesto-honest-computation`) contains a truncated body ending at §2 (Principle 1). The Zenodo record (DOI: 10.5281/zenodo.21299278, `manifesto-honest-computation.md`, 23,797 chars) contains the complete text including §3 (Honest Portfolio), §4 (Call to Action), §5 (Falsification Pledge), and §6 (Conclusion). The D1 record should be updated from the Zenodo source. This systemic D1 truncation affects ≥3 QNFO papers.

---

*Document prepared by huang-2025-quantum-advantage-audit, QNFO Research Collective.*
*Status: Recommended revision. Not yet applied to canonical Manifesto.*
