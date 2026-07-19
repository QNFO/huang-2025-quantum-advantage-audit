# PROJECT-PLAN.md — Huang et al. (2025) Quantum Advantage Audit

**Project Slug:** huang-2025-quantum-advantage-audit
**Repository:** https://github.com/QNFO/huang-2025-quantum-advantage-audit
**Start Date:** 2026-07-19
**Status:** Phase 0 — Initialization

---

## §1. Charter

### §1.1 Mission

Conduct a full-spectrum, reproducible deep research audit of Huang, Choi, McClean & Preskill (2025) "The vast world of quantum advantage" (arXiv:2508.05720), situating the paper within the QNFO research ecosystem and subjecting both the paper's claims and QNFO's prior critiques to symmetric scrutiny.

### §1.2 Core Claim Lock

**Huang et al. Core Claim (as reformulated in logically valid, falsifiable terms):**

1. **Framework claim:** Any claimed quantum advantage can be systematically evaluated along five orthogonal dimensions: Predictability (P), Typicality (T), Robustness (R), Verifiability (V), and Usefulness (U). A genuine quantum advantage satisfies all five.

2. **Taxonomy claim:** Quantum advantages fall into four distinct realms — Computational, Learning/Sensing, Cryptographic/Communication, and Space — each with different foundational guarantees (complexity theory vs. physical law vs. information theory).

3. **Theorem 1 (Unpredictability):** Assuming BPP ≠ BQP, the decision problem "does circuit C outperform Pauli propagation classical simulation?" is in BQP but not in BPP. Hence there exist quantum advantages that classical analysis cannot detect.

4. **Future claim:** The most significant quantum advantages are likely to be those we cannot currently conceive, implying that a full map of quantum advantage requires quantum technology itself.

**QNFO Counter-Claim (to be tested):**

1. QNFO's joules-per-solution criterion captures the economic dimension that Huang et al.'s Usefulness keystone omits.
2. QNFO's QEC overhead analysis (10²–10³×) raises a robustness concern that Huang et al. do not adequately quantify.
3. QNFO's ontological critique (The Qubit Delusion) identifies a category of error — conflating useful abstraction with ontological commitment — that Huang et al. do not address.
4. Theorem 1, if correct, strengthens the case for diversified post-classical investment, not concentrated FTQC investment.
5. QNFO has failed to apply its own falsifiability standards to itself and has a structural tendency to declare victory prematurely.

### §1.3 Success Criteria

1. Complete literature search across 5+ sources with full deduplication
2. Systematic engagement with every QNFO paper relevant to the Huang et al. framework
3. Honest acknowledgment of QNFO's own intellectual failures and falsified claims
4. Calibration register with time-bound, falsifiable predictions for both sides
5. Publication-grade analysis document with full provenance
6. All artifacts committed to GitHub and archived to R2

---

## §2. Phases and Work Breakdown Structure

### Phase 0: Project Initialization
| Task | Deliverable | Gate |
|:-----|:-----------|:-----|
| P0.1 | Repo created, feature branch, GitHub remote | Branch ≠ main |
| P0.2 | Directory scaffold | docs/, artifacts/, notebooks/, releases/ |
| P0.3 | PROJECT-PLAN.md | All sections populated |
| P0.4 | README.md | Name, status, quick start |
| P0.5 | Core claim lock | §1.2 locked |
| P0.6 | .gitignore | Present |
| P0.7 | KG/Memory seed | Project logged |
| P0.8 | Phase 0 closeout | Commit, tag v0.1-phase0, push |

### Phase 1: Due Diligence — Cross-Reference Discovery
| Task | Deliverable | Source |
|:-----|:-----------|:-------|
| P1.1 | KG stats query | Ecosystem overview |
| P1.2 | KG quantum-advantage node search | Existing QNFO papers |
| P1.3 | D1 living-paper cross-reference | Paper bodies, counts |
| P1.4 | Vectorize semantic search | "quantum advantage" 10 results |
| P1.5 | arXiv API search for related papers | External literature |
| P1.6 | Semantic Scholar search (rate-limited) | External literature |
| P1.7 | Gap analysis report | artifacts/due-diligence-report.md |

### Phase 2: Literature Search and Triage
| Task | Deliverable |
|:-----|:-----------|
| P2.1 | Multi-source query execution (5 sources) | Raw hit counts |
| P2.2 | Deduplication | Unique paper count |
| P2.3 | Classification (core/supporting/background/reject) | Classification matrix |
| P2.4 | Core paper deep reads | 3-5 key claims per paper |
| P2.5 | Literature search report | artifacts/literature-search-report.md |

### Phase 3: Citation Management
| Task | Deliverable |
|:-----|:-----------|
| P3.1 | Citation extraction from Huang et al. | Citation list |
| P3.2 | BibTeX verification | Audit report |
| P3.3 | Cross-reference with QNFO citations | Overlap analysis |
| P3.4 | Citation report | artifacts/citation-audit.md |

### Phase 4: Deep Research — Bayesian Cascade
| Stage | Deliverable |
|:------|:-----------|
| S0 | Domain topology map | artifacts/bayesian-cascade/domain-assessment.md |
| S1 | Paradigm-shift candidates | artifacts/bayesian-cascade/paradigm-candidates.md |
| S2 | Assumption audit | artifacts/bayesian-cascade/assumption-audit.md |
| S3 | Red-team challenge | artifacts/bayesian-cascade/red-team.md |
| S4 | Sensitivity analysis | artifacts/bayesian-cascade/sensitivity-analysis.md |
| S5 | Calibration register | artifacts/bayesian-cascade/calibration-register.md |
| S6 | Portfolio allocation | artifacts/bayesian-cascade/portfolio-allocation.md |
| S7 | Strategic memo | artifacts/bayesian-cascade/strategic-memo.md |
| S8 | Adversarial review | artifacts/bayesian-cascade/adversarial-review.md |

### Phase 5: Publication
| Task | Deliverable |
|:-----|:-----------|
| P5.1 | Synthesis document (paper.md) | docs/paper.md |
| P5.2 | PDF build (Pandoc+XeLaTeX if available) | releases/huang-2025-audit-v1.0.pdf |
| P5.3 | Publication language gate scan | Pass/Fail report |

### Phase 6: Cloudflare Deployment
| Task | Deliverable |
|:-----|:-----------|
| P6.1 | R2 archive of all artifacts | qnfo bucket |
| P6.2 | D1 living-paper insert | Paper row |
| P6.3 | KG node seed | Paper node + edges |

### Phase 7: Dissemination
| Task | Deliverable |
|:-----|:-----------|
| P7.1 | IPFS pinning (primary) | CID |
| P7.2 | Multi-gateway verification | Gateway report |

### Phase 8: 4-D Distribution
| Task | Deliverable |
|:-----|:-----------|
| P8.1 | DNSLink creation | TXT record |
| P8.2 | Internet Archive submission | IA snapshot |
| P8.3 | 4-D verification | _verify_4d.py output |

---

## §3. Milestones and Gate Criteria

| Milestone | Gate Criteria | Tag |
|:----------|:-------------|:----|
| M0: Init complete | All Phase 0 tasks done, pre-flight P1-P10 passed | v0.1-phase0 |
| M1: DD complete | KG+D1+Vectorize+2 external sources queried | v0.2-phase1-dd |
| M2: Lit search complete | ≥5 core, ≥10 supporting classified | v0.3-phase2-lit |
| M3: Citations complete | Audit report with match/missing/unused counts | v0.4-phase3-cite |
| M4: Deep research complete | All 9 cascade stages with documents | v0.5-phase4-deep |
| M5: Publication ready | Paper.md + PDF, language gate passed | v1.0 |
| M6: Deployed | R2 archive + D1 insert + KG seed | v1.1-deploy |
| M7: Disseminated | IPFS CID + gateway verification | v1.2-disseminate |
| M8: 4-D complete | All 4 dimensions verified | v1.3-distribute |

---

## §4. Deliverable Registry

| ID | Deliverable | Path | Archival Target |
|:---|:-----------|:-----|:----------------|
| D01 | Project Plan | PROJECT-PLAN.md | GitHub, R2 |
| D02 | Due Diligence Report | artifacts/due-diligence-report.md | GitHub, R2 |
| D03 | Literature Search Report | artifacts/literature-search-report.md | GitHub, R2 |
| D04 | Citation Audit | artifacts/citation-audit.md | GitHub, R2 |
| D05 | Bayesian Cascade (9 docs) | artifacts/bayesian-cascade/ | GitHub, R2 |
| D06 | Synthesis Paper | docs/paper.md | GitHub, R2, D1 |
| D07 | PDF | releases/huang-2025-audit-v1.0.pdf | R2, Zenodo |
| D08 | BibTeX | docs/refs.bib | GitHub, R2 |
| D09 | 4-D Verification Report | artifacts/verify-4d-report.md | GitHub, R2 |

---

## §5. Risk Register

| ID | Risk | Probability | Impact | Mitigation |
|:---|:-----|:-----------|:-------|:-----------|
| R1 | Semantic Scholar rate limiting blocks external paper retrieval | High (0.7) | Medium | Fall back to arXiv API + manual DOI lookup |
| R2 | Shor's Assumptions paper unrecoverable from D1/KG | High (0.8) | High | Flag as critical gap; reconstruct from KG metadata if possible |
| R3 | Pandoc/XeLaTeX unavailable on Windows | Medium (0.5) | Low | Accept HTML/Markdown as primary format; PDF is nice-to-have |
| R4 | KG API returns errors on complex queries | Medium (0.4) | Medium | Use simpler endpoint queries; cross-reference with D1 direct |
| R5 | QNFO position overfits to confirmation bias | Medium (0.5) | Critical | Explicit red-team stage; acknowledge all QNFO failures |
| R6 | Project scope expansion beyond session capacity | Medium (0.4) | High | Strict phase gate; defer Phases 5-8 if needed |
| R7 | Git remote misdirected to qnfo-skills | Low (0.1) | Critical | REPO-TARGET GATE verified at every commit/tag |
| R8 | R2 upload failure | Low (0.3) | Medium | Local artifacts are primary; R2 is archival duplicate |

---

## §6. Version History

| Version | Date | Description |
|:--------|:-----|:------------|
| v0.1-phase0 | 2026-07-19 | Project initialization |
