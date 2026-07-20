---
title: "Beyond the Keystones: What Physics Tells Us About Quantum Advantage That Complexity Theory Cannot"
subtitle: "A Response to Huang, Choi, McClean & Preskill (2025)"
author: "Rowan Brad Quni-Gudzinas"
orcid: "0009-0002-4317-5604"
date: "2026-07-20"
abstract: |
  Huang, Choi, McClean & Preskill (2025) have produced the most honest
  document about quantum advantage to emerge from the quantum computing
  establishment. Their five-keystone framework represents a significant
  advance in how the field thinks about its own promises. But the framework,
  like the field it evaluates, operates almost entirely within the 
  mathematical abstraction layer — complexity theory, information theory,
  and the qubit-gate-circuit model. It does not descend into the physics of
  actual qubit implementations. This response argues that the physical 
  implementation layer contains its own keystones that the framework 
  overlooks: the self-referential character of quantum state calibration,
  category errors introduced by cross-domain terminology, and a systematic
  confusion between frequency-domain engineering tricks and ontological 
  facts about qubits. I argue that these physical keystones do not refute
  the Huang et al. framework but extend it — and that the most honest
  document about quantum advantage is also, by its own admission, an
  incomplete one.
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
  The central claim — that physical-layer calibration circularity, domain
  translation errors, and the frequency-domain nature of qubit isolation
  constitute overlooked keystones that materially affect quantum advantage
  assessments — is falsifiable. It would be disconfirmed if: (a) any quantum
  computing platform demonstrates gate fidelities below the fault-tolerance 
  threshold with calibration error budgets that are independently verified 
  to the same precision, without relying on gate set tomography circularity;
  or (b) a fault-tolerant quantum computer performs a commercially useful 
  computation at lower joules per solution than any classical alternative 
  before 2035, using exclusively Archimedean qubit implementations.
---

**Author:** Rowan Brad Quni-Gudzinas | **ORCID:** [0009-0002-4317-5604](https://orcid.org/0009-0002-4317-5604) | **Date:** 2026-07-20

---

# 1. Introduction

Huang, Choi, McClean & Preskill (2025) [1] have produced what I believe is the most intellectually honest document about quantum advantage to emerge from the quantum computing establishment. Their five-keystone framework — Predictability, Typicality, Robustness, Verifiability, and Usefulness — is the kind of systematic evaluation the field has needed for thirty years. Their Theorem 1, proving that detecting quantum advantage is itself classically hard under the BPP ≠ BQP assumption, is a genuinely original contribution. And their candor is remarkable: they acknowledge that BPP ≠ BQP remains unproven, that quantum recommendation systems were dequantized by Tang (2019, 2021), that asymptotic sensing advantage is "fundamentally unattainable" in generic noise, and that "we have never tested quantum mechanics at the complexity frontier where thousands of particles become massively entangled."

But the framework has a structural blind spot. It operates almost entirely within the mathematical abstraction layer — complexity theory, information theory, and the qubit-gate-circuit model as an axiomatic starting point. It does not descend into what actually happens inside a dilution refrigerator. This is not a failure of the framework; it is a failure of scope. The framework was designed to evaluate quantum advantage _claims_ against first principles. But those first principles themselves rest on physical assumptions that, when examined closely, reveal tensions that complexity theory alone cannot resolve.

This response advances four arguments, each grounded in the physics of actual qubit implementations rather than in the mathematical abstraction of qubits as points on a Bloch sphere:

1. **The self-referential metrology problem.** Quantum state calibration is inherently circular. Gate set tomography provides self-consistent estimates, not independent verification. At current fidelities, this circularity is negligible. At the fault-tolerance threshold, it becomes the limiting factor.

2. **The frequency-domain trick.** The transmon qubit's "two-level system" is not a real two-level system. It is a bosonic mode with anharmonic energy spacing, addressed at a single transition frequency. Calling the excitation a "photon" while using it as if it obeyed fermionic exclusion is a category error that obscures the actual physics.

3. **Domain translation errors.** Quantum computing borrows its vocabulary from at least four distinct physical domains — quantum optics, condensed matter physics, the Standard Model of particle physics, and classical computing — and the terms do not translate cleanly. The "photon" of circuit QED is not the photon of quantum optics; the "electron" in a spin qubit is not the electron of the Standard Model. These category errors compound into a systematic map-territory confusion.

4. **The pedagogical-versus-operational distinction.** Working quantum engineers do not believe qubits are tiny billiard balls. They think in terms of collective excitations of modes, relational observables, and spectral addressability. The confusion is in textbooks, press releases, and funding narratives — not in the design of quantum processors.

None of these arguments refute the Huang et al. framework. They extend it in the direction the framework itself acknowledges it has not gone.

---

# 2. The Self-Referential Metrology Problem

## 2.1 How Calibration Actually Works

Every qubit in a quantum processor must be calibrated before use. Calibration means finding the qubit's resonant frequency ω₀₁, its anharmonicity α, the microwave pulse amplitude for a π-rotation, the readout resonator's phase response for |0⟩ and |1⟩, and the cross-talk coupling to neighboring qubits.

How is this done? Through a sequence of mutually dependent measurements. Multi-level spectroscopy sweeps a probe tone to find ω₀₁, ω₁₂, and compute α — this is the closest we have to an independent anchor, probing the bare Hamiltonian's eigenvalues without restricting to the two-level subspace. Rabi oscillations vary pulse duration to find the π-rotation amplitude, but require knowing the readout calibration. Ramsey interferometry measures dephasing time T₂* but requires calibrated pulses and readout. Gate set tomography [2] jointly estimates all gates and measurement operators simultaneously — it guarantees internal consistency but cannot guarantee external accuracy due to gauge freedom in the estimates.

The calibration is a circle: calibrated gates define "known" states, calibrated readout measures them, and the outcomes update the calibration. Every element is defined in terms of every other element.

## 2.2 The Spectroscopic Anchor

The best candidate for an independent anchor is multi-level spectroscopy of the bare Hamiltonian [5]. For a transmon, the anharmonicity α = ω₁₂ − ω₀₁ can be measured without assuming anything about the qubit subspace: spectroscopy treats the transmon as the multi-level system it is. Spectroscopic anchoring is the operational equivalent of the claim that "the qubit is a real subsystem of a larger physical system." It grounds the calibration circle in a measurement that operates on the full Hamiltonian, not the restricted subspace.

It is not perfectly independent. The same readout chain — Josephson parametric amplifier, high-electron-mobility transistor, digitizer — is used for both spectroscopy and qubit readout. But the residual circularity is bounded by the readout fidelity.

## 2.3 When Circularity Becomes the Bottleneck

At current gate fidelities (99.9% single-qubit, 99% two-qubit), calibration circularity is a second-order concern. The dominant errors are physical: decoherence, leakage to higher transmon levels, cross-talk. But the fault-tolerance threshold requires per-gate error rates of approximately 10⁻⁴ to 10⁻³, and achieving logical error rates of 10⁻¹⁰ or below requires well-characterized physical error rates at comparable precision.

In this regime, a new problem emerges: we cannot independently verify that our error models are correct to the required precision. Gate set tomography provides self-consistent estimates with gauge freedom. Randomized benchmarking [16] provides a partially independent check but uses the same physical hardware. Multi-level spectroscopy anchors the computational subspace but does not validate the gate error model.

## 2.4 A Missing Keystone

Huang et al. list five keystones. I propose a sixth: **Metrological Independence.** A quantum advantage claim should specify how calibration circularity has been bounded, what independent anchors have been used, and what the residual calibration uncertainty is.

How does this apply to existing claims? Google's 2019 Sycamore experiment [3] used cross-entropy benchmarking, which is self-consistent but not independently anchored. IBM's 2023 utility experiment [4] used error mitigation that assumes an accurately characterized noise model. Neither experiment reported an independent calibration uncertainty budget. This does not refute these results — it identifies an uncertainty the field currently does not quantify.

---

# 3. The Frequency-Domain Trick

## 3.1 What a Transmon Qubit Actually Is

A transmon qubit [5] is described as a "two-level quantum system" formed by the two lowest eigenstates of an anharmonic LC oscillator. The Josephson junction provides anharmonicity: ω₀₁ ≠ ω₁₂ by approximately 5%.

But a transmon is not a two-level system. It is a bosonic mode with an infinite ladder of states |0⟩, |1⟩, |2⟩, |3⟩, ... — a harmonic oscillator made anharmonic by the cos φ potential. The "two-level" restriction is maintained by **frequency selectivity**: a microwave pulse tuned to ω₀₁ cannot efficiently drive the |1⟩ → |2⟩ transition because it is off-resonance.

This is a frequency-domain engineering trick, not an ontological fact. The higher levels exist. They are populated during fast gates — DRAG pulses are designed to cancel this leakage. They are populated during readout — measurement-induced mixing with |2⟩ is a known error channel. They are populated by thermal photons from the environment.

## 3.2 The Boson-Pauli Tension

This is where a genuinely deep category error resides. The transmon excitation is called a "photon" — borrowing from quantum optics, where photons are bosons that do not obey Pauli exclusion. You can put arbitrarily many photons into the same cavity mode. That is why lasers exist.

But the transmon's "two-level system" is treated as if it obeys an exclusion principle: the qubit can be |0⟩ (zero photons) or |1⟩ (one photon). The "exclusion" is engineered — maintained by spectral isolation and active leakage suppression — not a consequence of particle statistics.

The irony is sharp: the word "photon" — the quintessentially bosonic concept, defined by the _absence_ of exclusion — describes a system whose entire engineering philosophy is to create _effective_ exclusion through frequency-domain tricks. The Josephson junction's anharmonicity does the work that Pauli exclusion would do for free in a fermionic system. But it is not free. The energy gap is finite. The isolation is imperfect. The leakage is measurable.

## 3.3 A Fundamental Trade-Off

The transmon's robustness against noise relies on the EJ/EC ratio — increasing it exponentially suppresses charge noise. But the residual anharmonicity _decreases_ as EJ/EC increases. The more charge-noise-robust the transmon, the less anharmonic it becomes, the more it resembles a harmonic oscillator, and the harder it is to isolate the two-level subspace.

This trade-off is fundamental. It emerges from the bosonic nature of the underlying mode. No amount of Hamiltonian engineering eliminates it. It is a physical keystone that the mathematical framework of the qubit-gate-circuit model obscures.

Majorana zero modes [6, 7] — fermionic excitations in topological superconductors — genuinely obey Pauli exclusion. A Majorana mode cannot be doubly occupied. The protection is topological, not spectral. The contrast — between a bosonic system engineered to mimic fermionic behavior and an actual fermionic system — reveals the deeper question: is the transmon architecture fundamentally limited in ways that fermionic architectures are not?

---

# 4. Domain Translation Errors

## 4.1 One System, Four Vocabularies

Consider the vocabulary used to describe a superconducting transmon quantum processor. The word "photon" comes from quantum optics, where it means an optical-frequency excitation (~500 THz), but in circuit QED it means a microwave excitation (~5 GHz). "Cavity" means a Fabry-Pérot interferometer in quantum optics but a coplanar waveguide on a chip in circuit QED [14]. "Plasmon" means a collective electron density oscillation in condensed matter but a collective Cooper pair oscillation across a Josephson junction in the transmon. "Gate" means a logic gate implemented in silicon in classical computing but a microwave pulse in quantum information.

Every term carries baggage from its domain of origin that does not always survive translation.

## 4.2 The Electron That Isn't There

The word "electron" creates the deepest confusion. In the Standard Model, an electron is a spin-1/2 fermion, an irreducible representation of the Poincaré group [8]. In quantum field theory, it is an excitation of the electron field — non-local, with renormalized properties.

In a superconducting transmon, _the electron does not appear at all._ The charge carriers are Cooper pairs — bosonic bound states of two electrons, mediated by phonons in the superconducting lattice. They are emergent quasiparticles, not fundamental particles. The "plasmon" excitation is a collective oscillation of these Cooper pairs.

Yet the vocabulary invites the reader to imagine something particle-like. The engineer does not imagine this. The engineer thinks in terms of modal occupation numbers. But the vocabulary has a life of its own.

When researchers claim that "quantum mechanics has been tested to extraordinary precision" and extrapolate that confidence to the fault-tolerance regime, they apply evidence from low-entanglement particle physics experiments to high-entanglement engineered many-body systems using vocabulary that systematically obscures the domain translation. The Huang et al. acknowledgment that "we have never tested quantum mechanics at the complexity frontier" is, in my view, the single most important sentence in their paper — but it does not trace this admission to its root cause in vocabulary.

---

# 5. The Pedagogical-Versus-Operational Distinction

One of the most persistent critiques of quantum computing is that it imports a "particle ontology" — treating qubits as tiny billiard balls poked with gates. This critique has merit at the level of public communication but misses a crucial fact: working quantum engineers do not think this way.

Ask an engineer calibrating a transmon what they are doing. They will tell you about measuring anharmonicity, finding the Rabi frequency for π-rotations, optimizing DRAG parameters to cancel leakage. They think in frequency-domain terms, modal occupation numbers, spectral isolation. They do not picture billiard balls.

The particle-qubit picture lives in popular science journalism, quantum computing textbooks for computer scientists [9], and investor presentations. The confusion is pedagogical and financial, not operational.

This distinction reframes the Huang et al. keystone of _Predictability._ There are two "quantum technologies" at play: the pedagogical one (abstract qubits, unitary gates, error correction as a code) and the operational one (actual transmon chips with frequency-domain tricks, calibration circles, readout chains, cross-talk). The Huang framework evaluates the pedagogical technology. It does not evaluate the operational one. The gap between them is the single largest unquantified uncertainty in quantum computing.

---

# 6. Toward a More Complete Framework

## 6.1 Two Additional Keystones

I propose extending the Huang framework with two additional keystones:

**Metrological Independence.** A quantum advantage claim should specify what independent calibration anchors were used, what the residual calibration uncertainty is, and whether it is smaller than the reported error rates by a sufficient factor.

**Ontological Coherence.** A quantum advantage claim should be expressed in vocabulary that unambiguously identifies the physical entities involved. If the claim involves a "qubit," specify the physical implementation and the mechanism of spectral isolation. If it involves "readout," specify where in the amplifier chain projection is assumed to occur.

These are not abstract philosophical demands. They are operational standards that can be evaluated against the published literature.

## 6.2 Falsification Conditions

This response makes specific, falsifiable claims:

**C1:** If any quantum computing platform demonstrates gate fidelities below the fault-tolerance threshold with calibration error budgets independently verified to the same precision — without relying on gate set tomography circularity — then §2 is refuted.

**C2:** If a fault-tolerant quantum computer performs a commercially useful computation at lower joules per solution than any classical alternative before 2035, using exclusively Archimedean qubit implementations, then the combined argument is refuted.

**C3:** If an independent audit demonstrates that domain translation errors do NOT contribute to systematic overconfidence in quantum advantage claims, then §4 is refuted.

---

# 7. Beyond the Transmon: Alternative Paths

The frequency-domain trick suggests a natural question: if the transmon is a bosonic system engineered to mimic fermionic exclusion, why not use actual fermionic systems? Majorana zero modes [6, 7, 10] are fermionic quasiparticles that genuinely obey Pauli exclusion. The protection is topological, not spectral.

A deeper alternative emerges from considering the mathematical structure of quantum state space. Ostrowski's theorem [11] shows that ℚ has exactly two types of completions: the Archimedean ℝ and the p-adic ℚ_p. There exists a literature on p-adic quantum mechanics [12, 13] extending quantum theory to non-Archimedean fields. Bruhat-Tits trees possess an ultrametric structure where the strong triangle inequality prevents small perturbations from accumulating.

Whether p-adic quantum computing provides a practical alternative to transmon-based quantum computing is an open question. I mention this not to advocate but to illustrate that the Huang framework, operating at mathematical abstraction, cannot distinguish between a bosonic frequency-domain trick (transmon), a fermionic topological qubit (Majorana), and a non-Archimedean qubit (Bruhat-Tits tree). All three satisfy the five keystones equally well. But they are physically different in ways that matter for feasibility.

The most immediately testable alternative does not require new hardware. p-adic discrete gate compilation — encoding quantum logic in non-Archimedean gate sets while running on existing transmon or trapped-ion hardware — is a software layer testable on current cloud quantum computing platforms. If it demonstrates improved gate fidelity, the hypothesis that non-Archimedean encoding provides protection gains experimental support. If it does not, the pragmatic argument is weakened. Either outcome advances understanding.

---

# 8. Conclusion

Huang, Choi, McClean & Preskill have done the quantum computing field a service. Their framework is the first systematic attempt to create objective criteria for evaluating the field's central claims. Their candor sets a standard the rest of the field should emulate.

But the framework is incomplete. It operates at the level of mathematical abstraction and does not descend into the physics of actual qubit implementations. This response has argued that the physical layer contains its own keystones: self-referential metrology, the frequency-domain trick, domain translation errors, and the pedagogical-versus-operational distinction.

None of these refute the Huang framework. They extend it — demanding that advantage claims specify what physical assumptions they depend on, what calibration anchors they use, and what vocabulary they inherit. The paper I most want to read does not yet exist: a document applying this extended framework to the actual hardware that quantum computing companies are building, asking what the independent calibration anchor is, what the residual uncertainty is, and what fundamental trade-offs each physical implementation imposes.

The most honest document about quantum advantage is, by its own admission, incomplete. That incompleteness is not a weakness — it is an invitation.

---

## References

[1] Huang, H.-Y., Choi, S., McClean, J.R., & Preskill, J. (2025). The vast world of quantum advantage. arXiv:2508.05720.

[2] Blume-Kohout, R., et al. (2013). Robust, self-consistent, closed-form tomography of quantum logic gates on a trapped ion qubit. arXiv:1310.4492.

[3] Arute, F., et al. (2019). Quantum supremacy using a programmable superconducting processor. Nature 574, 505–510.

[4] Kim, Y., et al. (2023). Evidence for the utility of quantum computing before fault tolerance. Nature 618, 500–505.

[5] Koch, J., et al. (2007). Charge-insensitive qubit design derived from the Cooper pair box. Physical Review A 76, 042319.

[6] Kitaev, A.Y. (2003). Fault-tolerant quantum computation by anyons. Annals of Physics 303, 2–30.

[7] Nayak, C., Simon, S.H., Stern, A., Freedman, M., & Das Sarma, S. (2008). Non-Abelian anyons and topological quantum computation. Reviews of Modern Physics 80, 1083–1159.

[8] Zurek, W.H. (2003). Decoherence, einselection, and the quantum origins of the classical. Reviews of Modern Physics 75, 715–775.

[9] Nielsen, M.A. & Chuang, I.L. (2000). Quantum Computation and Quantum Information. Cambridge University Press.

[10] Microsoft Quantum. (2023). InAs-Al hybrid devices passing the topological gap protocol. Physical Review B 107, 245423.

[11] Ostrowski, A. (1918). Über einige Lösungen der Funktionalgleichung φ(x)·φ(y) = φ(xy). Acta Mathematica 41, 271–284.

[12] Vladimirov, V.S. & Volovich, I.V. (1989). p-Adic quantum mechanics. Communications in Mathematical Physics 123, 659–676.

[13] Vladimirov, V.S., Volovich, I.V., & Zelenov, E.I. (1994). p-Adic Analysis and Mathematical Physics. World Scientific.

[14] Blais, A., et al. (2004). Cavity quantum electrodynamics for superconducting electrical circuits. Physical Review A 69, 062320.

[15] DiVincenzo, D.P. (2000). The physical implementation of quantum computation. Fortschritte der Physik 48, 771–783.

[16] Magesan, E., Gambetta, J.M., & Emerson, J. (2011). Scalable and robust randomized benchmarking of quantum processes. Physical Review Letters 106, 180504.
