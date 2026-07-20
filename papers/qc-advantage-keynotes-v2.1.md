---
title: "Beyond the Keystones: What Physics Tells Us About Quantum Advantage That Complexity Theory Cannot"
subtitle: "A Response to Huang, Choi, McClean & Preskill (2025)"
author: "Rowan Brad Quni-Gudzinas"
orcid: "0009-0002-4317-5604"
date: "2026-07-20"
version: "2.1"
abstract: |
  Huang, Choi, McClean & Preskill (2025) have produced the most honest
  document about quantum advantage to emerge from the quantum computing
  establishment. But their five-keystone framework operates at the
  mathematical abstraction layer — it never descends into the physics of
  actual qubit implementations. This response identifies four physical
  keystones the framework overlooks: the self-referential circularity
  of quantum state calibration, a category error at the heart of the
  transmon qubit (calling a bosonic excitation a "photon" while using
  it as if Pauli exclusion applied), systematic domain translation
  errors across four incompatible physics vocabularies, and the gap between
  pedagogical qubit pictures and operational qubit physics. I propose
  two additional keystones — Metrological Independence and Ontological
  Coherence — and provide specific falsification conditions. None of
  this refutes Huang et al. It extends them toward the physics the
  framework itself acknowledges it has not yet reached.
falsification: |
  This paper would be disconfirmed if: (a) any quantum computing platform
  demonstrates gate fidelities below fault-tolerance threshold with 
  calibration error budgets independently verified to the same precision
  without relying on gate set tomography circularity; (b) a fault-tolerant
  quantum computer performs a commercially useful computation at lower
  joules-per-solution than any classical alternative before 2035 using
  exclusively Archimedean qubit implementations; (c) a structured 
  terminology audit across quantum computing papers (2019-2026) finds
  that borrowed vocabulary carries its domain-of-origin semantics 
  faithfully with no systematic category drift.
---

**Author:** Rowan Brad Quni-Gudzinas | **ORCID:** [0009-0002-4317-5604](https://orcid.org/0009-0002-4317-5604) | **Version:** 2.1 | **Date:** 2026-07-20

---

# 1. Introduction

Huang, Choi, McClean & Preskill (2025) [1] have produced the most intellectually honest document about quantum advantage to emerge from the quantum computing establishment. Their five-keystone framework — Predictability, Typicality, Robustness, Verifiability, Usefulness — is the kind of systematic evaluation the field has needed for thirty years. Theorem 1 (detecting quantum advantage is classically hard, assuming BPP ≠ BQP) is genuinely original. And their candor is remarkable: BPP ≠ BQP remains unproven; quantum recommendation systems were dequantized by Tang (2019); asymptotic sensing advantage is "fundamentally unattainable" in generic noise; and "we have never tested quantum mechanics at the complexity frontier where thousands of particles become massively entangled."

But the framework has a blind spot: it operates entirely at the mathematical abstraction layer. Qubits are points on a Bloch sphere. Gates are unitary matrices. Error correction is a code. None of this descends into what actually happens inside a dilution refrigerator.

This response draws four arguments from the physics of real qubit implementations and proposes two new keystones. The aim is not to refute Huang et al. but to extend their framework toward the physics it acknowledges it has not yet reached.

---

# 2. The Self-Referential Metrology Problem

## 2.1 Calibration Is a Circle

Calibrating a transmon qubit means finding its resonant frequency ω₀₁, anharmonicity α = ω₁₂ − ω₀₁, the pulse amplitude for a π-rotation, the readout phase response for |0⟩ and |1⟩, and cross-talk coupling. Every step depends on every other.

Multi-level spectroscopy probes the bare Hamiltonian without restricting to the two-level subspace — it is the closest we have to an independent anchor. Rabi oscillations require knowing the readout calibration. Ramsey interferometry requires calibrated pulses. Gate set tomography [2] jointly estimates gates and measurements with internal consistency — but gauge freedom prevents external accuracy guarantees.

The calibration is a circle: calibrated gates define "known" states, calibrated readout measures them, outcomes update the calibration. Every element is defined in terms of every other element.

## 2.2 The Spectroscopic Anchor

Spectroscopy of the bare Hamiltonian provides a partial anchor. Koch et al. (2007) [3] showed that the anharmonicity α can be measured by two-tone spectroscopy — a probe tone populates |1⟩, a second tone finds ω₁₂ when the |1⟩ population dips. This measurement does not assume the qubit subspace exists; it treats the transmon as the multi-level system it actually is.

The anchor is not perfect. The same readout chain — Josephson parametric amplifier, HEMT, digitizer — serves both spectroscopy and qubit readout. The residual circularity is bounded by the readout fidelity. But it is bounded — and that bound can be quantified.

## 2.3 When Circularity Becomes the Bottleneck

At today's gate fidelities (99.9% single-qubit, 99% two-qubit), calibration circularity is a second-order concern. The dominant errors are physical: decoherence, leakage, cross-talk. But the fault-tolerance threshold requires per-gate error rates of ~10⁻⁴, and logical error rates of 10⁻¹⁰ require physical error characterization at comparable precision.

In this regime, we cannot independently verify our error models. Gate set tomography provides self-consistent estimates with gauge freedom. Randomized benchmarking [4] provides a partially independent check — it measures average fidelity through sequence-length scaling — but uses the same hardware. Spectroscopy anchors the computational subspace but does not validate the gate error model.

**This is not an argument that fault tolerance is impossible.** It is an argument that the metrology required for fault tolerance has not been demonstrated, and the gap between required precision and independently verifiable precision grows with system size.

Google's Sycamore experiment [5] used cross-entropy benchmarking — self-consistent, not independently anchored. IBM's Eagle utility experiment [6] used error mitigation that assumes an accurately characterized noise model. Neither reported an independent calibration uncertainty budget.

---

# 3. The Boson-Pauli Confusion

## 3.1 The Frequency-Domain Trick

A transmon qubit [3] is described as a "two-level quantum system." It is not. It is a bosonic mode with an infinite ladder |0⟩, |1⟩, |2⟩, |3⟩, ... — a harmonic oscillator made anharmonic by the cos φ Josephson potential. The "two-level" restriction is maintained by **frequency selectivity**: a microwave pulse at ω₀₁ cannot efficiently drive |1⟩ → |2⟩ because ω₁₂ ≠ ω₀₁.

This is engineering, not ontology. The higher levels exist. DRAG pulses are designed specifically to cancel leakage to |2⟩ during fast gates. Measurement-induced mixing with |2⟩ is a known error channel. Thermal photons populate higher levels.

## 3.2 Boson = No Exclusion; "Two-Level" = Effective Exclusion

The transmon excitation is called a "photon" — borrowed from quantum optics, where photons are bosons that do not obey the Pauli exclusion principle. You can put arbitrarily many photons into a cavity mode. That is why lasers work.

But the transmon's "two-level system" is treated as if exclusion applies: the qubit stores 0 or 1 photon. This exclusion is _engineered_ — maintained by spectral isolation and active leakage suppression — not a consequence of particle statistics.

The category error is sharp: the word defined by the _absence_ of exclusion describes a system whose entire engineering philosophy is to create an _effective_ exclusion through frequency-domain tricks. The Josephson junction's anharmonicity is doing the work that Pauli exclusion would do for free in a fermionic system. But the isolation is imperfect, the energy gap is finite, and the leakage is measurable.

## 3.3 The EJ/EC Trade-Off

There is a fundamental trade-off engineered into every transmon. Increasing EJ/EC exponentially suppresses charge noise — this is why the transmon exists. But residual anharmonicity _decreases_ as EJ/EC increases. The more charge-noise-robust the qubit, the less anharmonic, the more harmonic-oscillator-like, and the harder to isolate the two-level subspace. This trade-off is bosonic at root: no amount of Hamiltonian engineering eliminates it.

The contrast with genuine fermionic systems is instructive. Majorana zero modes in topological superconductors [7, 8, 9] are fermionic quasiparticles that genuinely obey Pauli exclusion. The protection is topological, not spectral. The question the Huang framework cannot ask — because it does not descend to the physical layer — is whether the transmon's frequency-domain isolation is fundamentally limited in ways fermionic architectures are not.

---

# 4. Domain Translation Errors

## 4.1 One System, Four Vocabularies

The vocabulary of a superconducting transmon processor is borrowed from incompatible domains. "Photon" (quantum optics) means ~500 THz optical excitation but ~5 GHz microwave excitation in circuit QED. "Cavity" (quantum optics) means a Fabry-Pérot interferometer but a coplanar waveguide on a chip in circuit QED [10]. "Plasmon" (condensed matter) means a collective electron density oscillation but a collective Cooper pair oscillation in the transmon. "Gate" (classical computing) means a silicon logic element but a microwave pulse in quantum information.

Each term carries ontological baggage from its domain of origin. The baggage does not always survive translation.

## 4.2 The Electron That Isn't There

In a superconducting transmon, the Standard Model electron does not appear. The charge carriers are Cooper pairs — bosonic bound states of two electrons, emergent quasiparticles, not fundamental particles. The "plasmon" excitation is a collective oscillation of these Cooper pairs. Yet the vocabulary invites the image of something particle-like, and this image propagates into press releases and funding narratives.

The Huang et al. acknowledgment that "we have never tested quantum mechanics at the complexity frontier" is the single most important sentence in their paper. But it does not trace this admission to its root: vocabulary inherited from low-entanglement particle physics is deployed to describe high-entanglement engineered many-body systems, and the semantic drift at the translation boundary is invisible to the mathematical framework that evaluates it.

---

# 5. The Gap Between the Textbook and the Laboratory

## 5.1 Engineers Think Relationally

Ask a calibration engineer what they are doing. They will say: "I'm measuring anharmonicity to confirm α ≈ 5%, finding the Rabi frequency for a 20 ns π-rotation, optimizing the DRAG parameter to cancel |2⟩ leakage." They think in frequency-domain addressability, modal occupation numbers, and spectral isolation. They do not picture billiard balls.

The particle-qubit picture lives in three places: popular science journalism, quantum computing textbooks for computer scientists [11], and investor presentations. The confusion is pedagogical and financial — not operational.

## 5.2 Two Quantum Technologies

This distinction reframes the Huang keystone of _Predictability_. There are two "quantum technologies" at play:

- **The pedagogical technology:** Abstract qubits as two-level systems, unitary gates as matrices, error correction as a code that restores the logical state. Scale up → threshold theorem guarantees success.

- **The operational technology:** Transmon chips with frequency-domain tricks, calibration circles, readout chains, correlated errors, amplifier saturation, leakage. Scale up → problems invisible at single-qubit level become dominant.

The Huang framework evaluates the pedagogical technology. The operational technology contains its own keystones that the framework cannot see. The gap between them is the single largest unquantified uncertainty in quantum computing.

---

# 6. Extending the Framework

## 6.1 Two Additional Keystones

| # | Keystone | Definition | How to Evaluate |
|---|----------|-----------|-----------------|
| 1 | Predictability | Evidence that quantum technology will achieve classical-beyond capability | Huang et al. (original) |
| 2 | Typicality | Advantage for typical instances, not just worst-case | Huang et al. (original) |
| 3 | Robustness | Persistence under hardware noise | Huang et al. (original) |
| 4 | Verifiability | Independent checkability of results | Huang et al. (original) |
| 5 | Usefulness | Practical value to user indifferent to substrate | Huang et al. (original) |
| **6** | **Metrological Independence** | Calibration uncertainty bounded by independent anchors, quantified | §2; specify spectroscopic anchor, GST gauge freedom, residual uncertainty |
| **7** | **Ontological Coherence** | Vocabulary identifies physical entities without cross-domain category errors | §3-4; specify physical implementation, degree of freedom, isolation mechanism, readout chain demarcation |

Keystone 6 captures the calibration circularity argument. A claim should specify: what independent anchors were used, what calibration methods, what residual uncertainty, and whether that uncertainty is smaller than reported error rates by a sufficient factor.

Keystone 7 captures the domain translation argument. A claim involving a "qubit" should specify the physical implementation and isolation mechanism. A claim involving "readout" should specify where in the amplifier chain projection is assumed to occur.

These are operational standards, not philosophical demands. They can be evaluated against the published literature.

## 6.2 Falsification

This response makes three falsifiable claims, each with a verification protocol:

**C1 — Metrology:** If any platform demonstrates gate fidelities below fault-tolerance threshold with calibration error budgets independently verified to the same precision without relying on gate set tomography circularity, §2 is refuted.  
*Verification:* Monitor published calibration procedures for independently anchored error budgets.

**C2 — Hardware:** If a fault-tolerant quantum computer performs a commercially useful computation at lower joules-per-solution than any classical alternative before 2035 using exclusively Archimedean qubit implementations, the combined argument is refuted.  
*Verification:* Monitor quantum computing benchmarks against classical baselines; track joules-per-solution.

**C3 — Vocabulary:** If a structured audit of terminology across 100+ quantum computing papers (2019–2026) finds that borrowed terms carry their domain-of-origin semantics faithfully — i.e., a "photon" in circuit QED is described with the same precision and ontological commitments as in quantum optics — then §4 is refuted.  
*Verification:* Terminology audit; coders classify usage patterns; inter-rater reliability ≥ 0.8.

If all three conditions are met, this response is wrong. If any succeeds, the Huang framework has an operational gap.

---

# 7. Beyond the Transmon

The arguments above point toward a research frontier the Huang framework cannot distinguish. A bosonic frequency-domain trick (transmon), a fermionic topological qubit (Majorana zero mode [7, 8]), and a non-Archimedean qubit on a Bruhat-Tits tree [12, 13] — rooted in Ostrowski's theorem [14] and p-adic quantum mechanics [15] — all satisfy the five original keystones equally well. No keystone captures the difference between spectral isolation and genuine Pauli exclusion, or between Archimedean and p-adic error protection.

The most pragmatic path does not require new hardware. p-adic discrete gate compilation — encoding quantum logic on non-Archimedean gate sets running on existing transmon or trapped-ion platforms — is a software layer testable on current cloud quantum computers. If it demonstrates improved gate fidelity, the non-Archimedean hypothesis gains experimental support. If not, the argument is weakened. Either outcome advances the field.

---

# 8. Conclusion

Huang, Choi, McClean & Preskill have produced a landmark document. Their framework and candor set a standard. But the framework is incomplete at the physical layer.

I have argued that the physical implementation of qubits introduces keystones invisible to complexity theory: calibration circularity that scales with system size, a category error encoded in the word "photon" itself, vocabulary drift across four incompatible physics domains, and a gap between textbook qubits and laboratory qubits that few advantage claims bridge.

None of this refutes Huang et al. It extends them — toward the physics they acknowledge they have not yet reached. The paper I most want to read applies this extended framework, with all seven keystones, to the actual hardware quantum computing companies are building, asking: what is the independent calibration anchor, what is the residual uncertainty, and what fundamental trade-offs does each physical implementation impose?

The most honest document about quantum advantage is, by its own admission, incomplete. That incompleteness is not a weakness. It is an invitation.

---

## References

[1] Huang, H.-Y., Choi, S., McClean, J.R., & Preskill, J. (2025). The vast world of quantum advantage. arXiv:2508.05720.

[2] Blume-Kohout, R., et al. (2013). Robust, self-consistent, closed-form tomography of quantum logic gates on a trapped ion qubit. arXiv:1310.4492.

[3] Koch, J., et al. (2007). Charge-insensitive qubit design derived from the Cooper pair box. Physical Review A 76, 042319.

[4] Magesan, E., Gambetta, J.M., & Emerson, J. (2011). Scalable and robust randomized benchmarking of quantum processes. Physical Review Letters 106, 180504.

[5] Arute, F., et al. (2019). Quantum supremacy using a programmable superconducting processor. Nature 574, 505–510.

[6] Kim, Y., et al. (2023). Evidence for the utility of quantum computing before fault tolerance. Nature 618, 500–505.

[7] Kitaev, A.Y. (2003). Fault-tolerant quantum computation by anyons. Annals of Physics 303, 2–30.

[8] Nayak, C., Simon, S.H., Stern, A., Freedman, M., & Das Sarma, S. (2008). Non-Abelian anyons and topological quantum computation. Reviews of Modern Physics 80, 1083–1159.

[9] Microsoft Quantum. (2023). InAs-Al hybrid devices passing the topological gap protocol. Physical Review B 107, 245423.

[10] Blais, A., et al. (2004). Cavity quantum electrodynamics for superconducting electrical circuits. Physical Review A 69, 062320.

[11] Nielsen, M.A. & Chuang, I.L. (2000). Quantum Computation and Quantum Information. Cambridge University Press.

[12] Vladimirov, V.S. & Volovich, I.V. (1989). p-Adic quantum mechanics. Communications in Mathematical Physics 123, 659–676.

[13] Vladimirov, V.S., Volovich, I.V., & Zelenov, E.I. (1994). p-Adic Analysis and Mathematical Physics. World Scientific.

[14] Ostrowski, A. (1918). Über einige Lösungen der Funktionalgleichung φ(x)·φ(y) = φ(xy). Acta Mathematica 41, 271–284.

[15] Zurek, W.H. (2003). Decoherence, einselection, and the quantum origins of the classical. Reviews of Modern Physics 75, 715–775.
