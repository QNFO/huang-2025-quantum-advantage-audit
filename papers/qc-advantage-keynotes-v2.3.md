---
title: "Beyond the Keystones: What Physics Tells Us About Quantum Advantage That Complexity Theory Cannot"
subtitle: "A Response to Huang, Choi, McClean & Preskill (2025)"
author: "Rowan Brad Quni-Gudzinas"
orcid: "0009-0002-4317-5604"
date: "2026-07-20"
version: "2.3"
abstract: |
  Huang, Choi, McClean & Preskill (2025) have produced the most honest
  document about quantum advantage to emerge from the quantum computing
  establishment. But their five-keystone framework operates at the
  mathematical abstraction layer — qubits as Bloch sphere points, gates
  as unitary matrices, error correction as a code — never descending
  into the physics of actual qubit implementations. This response
  identifies four physical keystones the framework overlooks: the
  self-referential circularity of quantum state calibration, a category
  error at the heart of the transmon qubit (calling a bosonic excitation
  a "photon" while using it as if Pauli exclusion applied), systematic
  vocabulary drift across four incompatible physics domains, and the gap
  between textbook qubits and laboratory qubits. I propose two additional
  keystones — Metrological Independence and Ontological Coherence — apply
  the extended framework to Google's Sycamore and IBM's Eagle experiments
  as worked examples, anticipate four counterarguments, and provide
  a calibration register of five dated, falsifiable predictions to
  prevent post-hoc rationalization. The aim is not to refute Huang et al.
  but to extend their framework toward the physics it acknowledges it
  has not yet reached.
keywords:
  - quantum advantage
  - qubit ontology
  - gate set tomography
  - self-referential metrology
  - transmon qubit
  - quantum error correction
  - Boson-Pauli confusion
  - Bruhat-Tits tree
  - ultrametric quantum computing
  - Ostrowski theorem
falsification: |
  This paper would be disconfirmed if: (a) any quantum computing platform
  demonstrates gate fidelities below fault-tolerance threshold with 
  calibration error budgets independently verified to the same precision
  without relying on gate set tomography circularity; (b) a fault-tolerant
  quantum computer performs a commercially useful computation at lower
  joules-per-solution than any classical alternative before 2035 using
  exclusively Archimedean qubit implementations; (c) a structured 
  terminology audit across 100+ quantum computing papers (2019–2026) finds
  that borrowed vocabulary carries its domain-of-origin semantics 
  faithfully with no systematic category drift.
---

**Author:** Rowan Brad Quni-Gudzinas | **ORCID:** [0009-0002-4317-5604](https://orcid.org/0009-0002-4317-5604) | **Version:** 2.3 | **Date:** 2026-07-20

---

# 1. Introduction

Huang, Choi, McClean & Preskill (2025) [1] have produced the most intellectually honest document about quantum advantage to emerge from the quantum computing establishment. Their five-keystone framework — Predictability, Typicality, Robustness, Verifiability, Usefulness — is the systematic evaluation the field has needed for thirty years. Theorem 1 (detecting quantum advantage is classically hard, assuming BPP ≠ BQP) is genuinely original. And their candor is remarkable: BPP ≠ BQP remains unproven; quantum recommendation systems were dequantized by Tang (2019); asymptotic sensing advantage is "fundamentally unattainable" in generic noise; and "we have never tested quantum mechanics at the complexity frontier where thousands of particles become massively entangled."

But the framework operates entirely at the mathematical abstraction layer. Qubits are Bloch sphere points. Gates are unitary matrices. Error correction is a code. None of this descends into what actually happens inside a dilution refrigerator.

This response draws four arguments from the physics of real qubit implementations and proposes two new keystones. Section 6 applies the extended framework to Sycamore and Eagle as worked examples. Section 7 anticipates four counterarguments. Section 8 provides a calibration register of five dated, falsifiable predictions. The aim is not to refute Huang et al. but to extend their framework toward the physics it acknowledges it has not yet reached.

---

# 2. The Self-Referential Metrology Problem

## 2.1 Calibration Is a Circle

Calibrating a transmon qubit means finding its resonant frequency ω₀₁, anharmonicity α = ω₁₂ − ω₀₁, the pulse amplitude for a π-rotation, the readout phase response for |0⟩ and |1⟩, and cross-talk coupling. Every step depends on every other.

Multi-level spectroscopy probes the bare Hamiltonian's eigenvalues without restricting to the two-level subspace — the closest we have to an independent anchor. But Rabi oscillations require knowing the readout calibration. Ramsey interferometry requires calibrated pulses. Gate set tomography [2] jointly estimates gates and measurements — guaranteeing internal consistency but not external accuracy, due to a gauge freedom: different gauge-equivalent gate sets produce exactly the same measurement statistics.

The calibration is a circle: calibrated gates define "known" states, calibrated readout measures them, outcomes update the calibration. Every element is defined in terms of every other.

## 2.2 The Spectroscopic Anchor

Spectroscopy of the bare Hamiltonian provides a partial anchor. Koch et al. (2007) [3] showed that anharmonicity α can be measured by two-tone spectroscopy — this measurement does not assume the qubit subspace exists. It treats the transmon as the multi-level system it is.

The anchor is not perfect. The same readout chain — Josephson parametric amplifier, HEMT, digitizer — serves both spectroscopy and qubit readout. But the residual circularity is bounded by the readout fidelity, and that bound can be quantified.

## 2.3 When Circularity Becomes the Bottleneck

At today's gate fidelities (99.9% single-qubit, 99% two-qubit), calibration circularity is a second-order concern. But the fault-tolerance threshold requires ~10⁻⁴ per-gate error rates, and logical error rates of 10⁻¹⁰ demand physical error characterization at comparable precision. In this regime, we cannot independently verify our error models. Gate set tomography gives self-consistent estimates with gauge freedom. Randomized benchmarking [4] uses the same hardware. Spectroscopy anchors the computational subspace but does not validate the gate error model.

Google's Sycamore [5] used cross-entropy benchmarking — self-consistent, not independently anchored. IBM's Eagle [6] used error mitigation assuming accurately characterized noise. Neither reported an independent calibration uncertainty budget.

---

# 3. The Boson-Pauli Confusion

## 3.1 The Frequency-Domain Trick

A transmon qubit [3] is described as a "two-level quantum system." It is not. It is a bosonic mode with an infinite ladder |0⟩, |1⟩, |2⟩, |3⟩, ... — a harmonic oscillator made anharmonic by the cos φ Josephson potential. The "two-level" restriction is maintained by **frequency selectivity**: a microwave pulse at ω₀₁ cannot efficiently drive |1⟩ → |2⟩ because ω₁₂ ≠ ω₀₁.

This is engineering, not ontology. DRAG pulses are designed to cancel leakage to |2⟩. Measurement-induced mixing with |2⟩ is a known error channel. Thermal photons populate higher levels.

## 3.2 Boson = No Exclusion; "Two-Level" = Effective Exclusion

The transmon excitation is called a "photon" — borrowed from quantum optics, where photons are bosons that do not obey the Pauli exclusion principle. You can put arbitrarily many photons into a cavity mode.

But the transmon's "two-level system" is treated as if exclusion applies: 0 or 1 photon. This exclusion is _engineered_ — maintained by spectral isolation and active leakage suppression — not a consequence of particle statistics.

The category error is sharp: the word defined by the _absence_ of exclusion describes a system whose entire engineering philosophy creates _effective_ exclusion through frequency-domain tricks. The Josephson junction's anharmonicity does the work Pauli exclusion would do for free in a fermionic system. But the isolation is imperfect, the gap is finite, and leakage is measurable.

## 3.3 The EJ/EC Trade-Off — Quantitative Analysis

The transmon Hamiltonian in the phase basis is:

$$\hat{H} = 4E_C(\hat{n} - n_g)^2 - E_J\cos\hat{\varphi}$$

where $\hat{n}$ is the Cooper pair number operator, $\hat{\varphi}$ is the superconducting phase, $n_g$ is the gate charge offset, $E_C = e^2/2C_\Sigma$ is the charging energy, and $E_J = I_c\Phi_0/2\pi$ is the Josephson energy.

The eigenvalue problem yields eigenstates $|k\rangle$ with energies $E_k$. The qubit frequency and anharmonicity are:

$$\hbar\omega_{01} \approx \sqrt{8E_JE_C} - E_C$$

$$\alpha \equiv \omega_{12} - \omega_{01} \approx -E_C$$

where the approximations hold in the transmon regime $E_J/E_C \gg 1$. The two critical figures of merit for qubit performance depend on the ratio $E_J/E_C$:

- **Charge dispersion** $\varepsilon_1$ (sensitivity to gate charge noise): scales as $\propto \exp(-\sqrt{8E_J/E_C})$
- **Anharmonicity** $|\alpha|$: scales as $\propto (E_J/E_C)^{-1/2}$

This is the fundamental trade-off. For a typical transmon with $E_J/E_C = 50$ (ω₀₁/2π ≈ 5 GHz, E_C/h ≈ 250 MHz):

| Parameter | Value | Scaling with $E_J/E_C$ |
|-----------|-------|----------------------|
| Qubit frequency ω₀₁/2π | ~5 GHz | ∝ $(E_J/E_C)^{1/2}$ |
| Anharmonicity $|\alpha|$/2π | ~250 MHz (5%) | ∝ $(E_J/E_C)^{-1/2}$ |
| Charge dispersion ε₁/2π | ~10 kHz | ∝ $\exp(-\sqrt{8E_J/E_C})$ |
| T₁ (dielectric loss limited) | ~100 μs | ∝ $(E_J/E_C)^{1/2}$ |
| Gate time (fixed Rabi) | ~20 ns | constant (at fixed ω₀₁) |
| Leakage to |2⟩ per gate | ~1% | ∝ $(\omega_{01}/|\alpha|)^2 \propto E_J/E_C$ |

Increasing $E_J/E_C$ suppresses charge noise exponentially (good for T₁) but decreases anharmonicity linearly (bad for spectral isolation). At $E_J/E_C = 100$, anharmonicity drops to ~3.5%; at $E_J/E_C = 200$, to ~2.5%. Below ~3%, DRAG pulses cannot reliably suppress leakage in sub-20 ns gates, and the "two-level system" approximation begins to break down operationally.

This trade-off is bosonic at root: a harmonic oscillator has vanishing anharmonicity and vanishing charge dispersion simultaneously. The Josephson junction introduces both at the cost of coupling them through a single parameter. No amount of Hamiltonian engineering decouples them — they are linked by the device geometry.

The contrast with Majorana zero modes in topological superconductors [7, 8, 9] is instructive. Majorana modes are fermionic: Pauli exclusion is genuine, not engineered. The protection is topological — the ground state degeneracy is robust against local perturbations independent of any energy ratio. The transmon's $E_J/E_C$ engineering is a brilliant workaround, but it is a workaround for a problem that fermionic architectures do not have.

---

# 4. Domain Translation Errors

## 4.1 One System, Four Vocabularies

The vocabulary of a transmon processor is borrowed from incompatible domains. "Photon" (quantum optics: ~500 THz) means ~5 GHz in circuit QED. "Cavity" (Fabry-Pérot) means a coplanar waveguide on a chip [10]. "Plasmon" (electron density oscillation) means Cooper pair oscillation across a JJ. "Gate" (silicon logic) means a microwave pulse. Every term carries ontological baggage that does not always survive translation.

## 4.2 The Electron That Isn't There

In a superconducting transmon, the Standard Model electron does not appear. The charge carriers are Cooper pairs — bosonic bound electron states, emergent quasiparticles. The "plasmon" excitation is their collective oscillation. Yet the vocabulary invites the image of something particle-like, and this image propagates into press releases and funding narratives.

Huang et al.'s acknowledgment that "we have never tested quantum mechanics at the complexity frontier" is the single most important sentence in their paper. But it does not trace this admission to its root: vocabulary inherited from low-entanglement particle physics is deployed to describe high-entanglement engineered many-body systems, and the semantic drift at the translation boundary is invisible to the mathematical framework evaluating it.

---

# 5. The Gap Between the Textbook and the Laboratory

## 5.1 Engineers Think Relationally

Ask a calibration engineer what they are doing. "I'm measuring anharmonicity, finding the Rabi frequency for a 20 ns π-rotation, optimizing the DRAG parameter." Frequency-domain addressability, modal occupation numbers, spectral isolation. No billiard balls.

The particle-qubit picture lives in popular science, quantum computing textbooks for computer scientists [11], and investor presentations. The confusion is pedagogical and financial — not operational.

## 5.2 Two Quantum Technologies

There are two "quantum technologies" at play:

- **Pedagogical:** Abstract qubits as two-level systems, unitary gates as matrices, error correction as a code. Scale up → threshold theorem guarantees success.
- **Operational:** Transmon chips with frequency-domain tricks, calibration circles, correlated errors, amplifier saturation. Scale up → problems invisible at single-qubit level become dominant.

The Huang framework evaluates the pedagogical technology. The operational technology contains its own keystones the framework cannot see. The gap between them is the single largest unquantified uncertainty in quantum computing.

---

# 6. Extending the Framework

## 6.1 Two Additional Keystones

| # | Keystone | Definition | How to Evaluate |
|---|----------|-----------|-----------------|
| 1–5 | Predictability, Typicality, Robustness, Verifiability, Usefulness | Per Huang et al. (2025) | Per Huang et al. (2025) |
| **6** | **Metrological Independence** | Calibration uncertainty bounded by independent anchors, quantified and reported | Specify spectroscopic anchor, GST gauge freedom, residual uncertainty budget |
| **7** | **Ontological Coherence** | Vocabulary identifies physical entities without cross-domain category errors | Specify physical implementation, degree of freedom, isolation mechanism, readout chain demarcation |

Keystone 6 asks: what independent anchors were used, what residual calibration uncertainty remains, and is it smaller than reported error rates by a sufficient factor?

Keystone 7 asks: what physical implementation is the "qubit"? Where in the amplifier chain does projection occur? Is the vocabulary faithful to the physics, or does it borrow from incompatible domains?

## 6.2 Worked Example: Sycamore (2019)

Google's 53-qubit Sycamore experiment [5] claimed quantum supremacy: a random circuit sampling task in 200 seconds that would take a classical supercomputer 10,000 years. Under the extended framework:

| Keystone | Assessment | Evidence |
|----------|-----------|----------|
| Predictability | PARTIAL — conditional on BPP ≠ BQP | Founding conjecture unproven 30 years |
| Typicality | PASS | Random circuits are worst-case for classical simulation |
| Robustness | PARTIAL — demonstrated at 53 qubits | Error rates too high for fault tolerance at this scale; threshold theorem guarantees future scalability but with unknown overhead |
| Verifiability | PARTIAL — gap too large to cross-verify | 10,000-year gap precludes classical verification; subsequent algorithms reduced gap |
| Usefulness | FAIL | Random circuit sampling has no known practical application |
| **Metrological Independence** | **FAIL** | No independent calibration uncertainty budget; cross-entropy benchmarking is self-consistent, not independently anchored |
| **Ontological Coherence** | **FAIL** | "53 superconducting qubits" without identifying physical degree of freedom or isolation mechanism; fidelity characterization and solver map on same platform |

Sycamore passes 1 keystone, partially passes 3, and fails 3.

## 6.3 Worked Example: IBM Eagle (2023)

IBM's 127-qubit Eagle processor [6] performed an Ising model simulation that strained classical methods, claimed as evidence of "quantum utility." Under the extended framework:

| Keystone | Assessment | Evidence |
|----------|-----------|----------|
| Predictability | PARTIAL | Ising model solved at 127 qubits; path to classically intractable 300+ unclear; no proof that scaling preserves advantage |
| Typicality | WEAK | Ising model has polynomial-time approximation algorithms; tensor network methods (PEPS, MPS) perform competitively on 2D grids |
| Robustness | WEAK | Zero-noise extrapolation assumes noise model is accurate at zero noise — an extrapolation, not a measurement; post-selection discards ~60% of shots |
| Verifiability | PARTIAL | ~127-spin Ising is at the boundary of classical tractability; verification by tensor network cross-check, not by direct classical solution |
| Usefulness | FAIL | The Ising model at 127 sites solved no commercially valuable problem; material science applications require larger systems and lower error rates |
| **Metrological Independence** | **FAIL** | Zero-noise extrapolation depends on the gate error model; no independent calibration uncertainty reported; error mitigation amplifies dependence on calibration accuracy |
| **Ontological Coherence** | **PARTIAL** | Platform described as "127-qubit Eagle processor" with 2D heavy-hex connectivity; some physical metadata provided (gate times, T₁, T₂) but no independent calibration anchor specified |

Eagle passes 0 keystones fully, partially passes 4, and fails 3. Its strongest partial pass is Verifiability — the Ising model at 127 spins is at the classical-quantum frontier, making the claim objectively interesting even if commercially useless. Its weakest assessment is Metrological Independence: zero-noise extrapolation replaces one calibration-dependent model (the gate error model) with another (the noise model), compounding rather than resolving the circularity.

## 6.4 Falsification Conditions

**C1 — Metrology.** If any platform demonstrates gate fidelities below fault-tolerance threshold with independent calibration error budgets verified to the same precision without GST circularity, §2 is refuted.  
*Verification:* Monitor published calibration procedures.

**C2 — Hardware.** If a fault-tolerant quantum computer performs commercially useful computation at lower joules-per-solution than any classical alternative before 2035 using exclusively Archimedean implementations, the combined argument is refuted.  
*Verification:* Monitor benchmarks; track joules-per-solution.

**C3 — Vocabulary.** If a structured terminology audit across 100+ quantum computing papers (2019–2026) finds borrowed terms carry domain-of-origin semantics faithfully with no systematic drift — inter-rater reliability ≥ 0.8 — then §4 is refuted.  
*Verification:* Independent coders classify usage patterns.

---

# 7. Objections and Responses

I anticipate four counterarguments and address each.

## 7.1 "Calibration circularity is a solved problem — gate set tomography handles it."

Gate set tomography provides self-consistent estimates, not externally verified ones. The gauge freedom means different gauge-equivalent gate sets produce identical measurement statistics but assign errors to different parts of the circuit. For a decoder, it matters whether errors are attributed to single-qubit gates, two-qubit gates, or measurements. GST alone cannot resolve this ambiguity — which is why randomized benchmarking and multi-level spectroscopy are used as partial cross-checks.

The point is not that calibration is impossible. It is that calibration uncertainty is not currently reported, and at the fault-tolerance threshold, unreported uncertainty becomes the bottleneck. This is a demand for transparency, not a claim of impossibility.

## 7.2 "The Boson-Pauli point is semantic, not substantive — engineers know the transmon is anharmonic."

Precisely the opposite. Engineers know the physics. The category error is in how the field _communicates_ advantage claims to funders, journalists, and textbook readers based on a mathematical model that engineers already recognize as a scaffold.

When a press release claims "53 superconducting qubits performed a computation in 200 seconds that would take 10,000 years classically," the listener imagines 53 quantum particles doing something particle-like. The engineer knows it is 53 frequency-domain isolation zones in a bosonic circuit. The gap between these two descriptions is not cosmetic — it is the mechanism by which overclaiming propagates from the laboratory to the marketplace. This is an operational concern, not a semantic one.

The quantitative EJ/EC analysis in §3.3 demonstrates that the trade-off is not merely semantic: the coupling of charge-noise protection to anharmonicity through a single device parameter is a constraint on physical performance that the pedagogical "two-level system" abstraction hides.

## 7.3 "You haven't proven that calibration circularity limits fault tolerance — you've asserted it."

Correct. That is why §6.4 and §8 provide falsification conditions and a calibration register. If a fault-tolerant device is demonstrated meeting the conditions of C1 and C2, the argument of this response is refuted. The burden of proof should fall on those claiming quantum advantage, not on those questioning it. Huang et al. would agree: they explicitly state that advantage claims require "rigorous, substantive, and quantifiable evidence."

## 7.4 "What do you propose instead of the transmon architecture?"

Three paths, none exclusive:

1. **Fermionic qubits.** Majorana zero modes in topological superconductors [7, 8, 9] offer genuine fermionic exclusion — no frequency-domain trick needed. The engineering challenges are substantial, but the physical principle is different from the transmon, and it bypasses the EJ/EC trade-off entirely.

2. **Non-Archimedean approaches.** Ostrowski's theorem [12] shows that ℚ has exactly two types of completions: Archimedean ℝ and p-adic ℚ_p. p-adic quantum mechanics [13, 14] extends quantum theory to non-Archimedean fields. Whether this translates into physical qubit protection is an open hypothesis — not a proven framework — but it is a hypothesis the current framework cannot evaluate because it does not distinguish topologies.

3. **The software-first path.** p-adic discrete gate compilation — encoding quantum logic on non-Archimedean gate sets while running on existing transmon or trapped-ion hardware — is a software layer testable on current cloud quantum computers.

The broader response is that proposing alternatives is not a prerequisite for identifying a gap. The Huang framework identifies gaps in advantage claims without proposing alternative algorithms. My argument identifies gaps in the framework itself — and where possible, sketches what might fill them.

---

# 8. Calibration Register

To prevent post-hoc rationalization, I lock the following dated, falsifiable predictions as of 2026-07-20. First audit due: 2028-07-20.

| # | Prediction | Check Date | P |
|---|-----------|-----------|-----|
| **P1** | No quantum computing platform will publish an independently anchored calibration uncertainty budget with a Metrological Independence score above the fault-tolerance threshold (i.e., residual calibration uncertainty smaller than reported physical error rates) | 2028-07-20 | 0.65 |
| **P2** | A structured terminology audit of ≥50 quantum computing papers (2019–2026) will find that at least 30% of terms imported from quantum optics, condensed matter, or Standard Model particle physics have semantically drifted from their domain-of-origin definitions | 2027-07-20 | 0.75 |
| **P3** | By 2030, at least one major quantum computing textbook or review article will explicitly address the EJ/EC trade-off and the bosonic nature of transmon qubits as a physical constraint on scalability, not merely as a calibration consideration | 2030-07-20 | 0.40 |
| **P4** | Google's Sycamore or a comparable experiment will publish at least one successor paper that includes an independent calibration uncertainty budget, either confirming or refuting the Metrological Independence concern | 2029-07-20 | 0.50 |
| **P5** | If a fault-tolerant quantum computer performs a commercially useful computation before 2035, the calibration procedures will reveal residual circularity that was bounded but not eliminated — i.e., Metrological Independence will be demonstrated as an asymptotic achievement, not a binary property | 2035-07-20 | 0.70 |

**P1 and P2** are the earliest tests — they can be evaluated against the existing literature without waiting for future experiments. If P1 fails (a platform publishes an independently anchored calibration budget), the central argument of §2 is substantially weakened. If P2 fails (no semantic drift is found), the domain translation argument of §4 is refuted.

**P3** tests whether the Boson-Pauli analysis influences the pedagogical literature. **P4** tests whether the Metrological Independence keystone is taken seriously by experimental groups. **P5** expresses the core thesis: that calibration circularity is a persistent structural feature, not a transient engineering problem — bounded but never eliminated.

If all five predictions fail, this response is wrong. If even one succeeds, the framework proposed here has identified something the Huang et al. keystones do not capture.

---

# 9. Conclusion

Huang, Choi, McClean & Preskill have produced a landmark document. Their framework and candor set a standard the rest of the field should emulate.

But the framework is incomplete at the physical layer. I have argued that the physical implementation of qubits introduces keystones invisible to complexity theory: calibration circularity that scales with system size, a category error encoded in the word "photon" itself, vocabulary drift across four incompatible physics domains, and a gap between textbook qubits and laboratory qubits that few advantage claims bridge.

The Sycamore and Eagle worked examples (§6) demonstrate that applying the extended framework changes how we evaluate specific, widely cited advantage claims. The objections section (§7) shows the arguments withstand anticipated counterarguments. The calibration register (§8) locks in five dated, falsifiable predictions to prevent post-hoc rationalization — the same standard of intellectual honesty Huang et al. exemplified in their original paper.

The paper I most want to read applies this extended framework, with all seven keystones, to every major quantum advantage claim of the past decade — Sycamore, Eagle, Willow, and whatever comes next — asking for each: what is the independent calibration anchor, what is the residual uncertainty, and what fundamental physical trade-offs does the implementation impose?

The most honest document about quantum advantage is, by its own admission, incomplete. That incompleteness is not a weakness. It is an invitation. This response is an attempt to accept it.

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

[12] Ostrowski, A. (1918). Über einige Lösungen der Funktionalgleichung φ(x)·φ(y) = φ(xy). Acta Mathematica 41, 271–284.

[13] Vladimirov, V.S. & Volovich, I.V. (1989). p-Adic quantum mechanics. Communications in Mathematical Physics 123, 659–676.

[14] Vladimirov, V.S., Volovich, I.V., & Zelenov, E.I. (1994). p-Adic Analysis and Mathematical Physics. World Scientific.

[15] Zurek, W.H. (2003). Decoherence, einselection, and the quantum origins of the classical. Reviews of Modern Physics 75, 715–775.
