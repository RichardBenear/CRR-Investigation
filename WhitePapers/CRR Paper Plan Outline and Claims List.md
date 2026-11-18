# CRR Paper Plan: Outline and Claims List

Sep 30, 2026 · @Richard

## Purpose and workflow

This plan sets the scope, structure and claims for a first paper on the CRR investigation, aimed at the Wolfram Physics community. The existing white paper and companion are a research log organized by chronology; the paper must be organized around a small set of claims, with stage detail in appendices.

Drafting sequence:

1. Outline and claims list (this document), approved by the investigator.
2. First draft by the drafting AI, using the current white paper and companion as source material, not memory.
3. Review pass by the second AI: consistency with the full program history, claim strength, caveats, readability.
4. Number verification by the drafting AI against a claims ledger (every number traced to a stage and verified artifact).
5. Joint fine-tuning, then the investigator's final read; the investigator owns every claim.
6. Outside review, ideally from a Wolfram Physics community reader, before release.

Two AIs refining the same text tend to soften caveats and raise confidence. The "not claimed" section and the investigator's final read are the safeguards.

## Rule lineage and two questions the community will ask

Most later results do not rest on Wolfram's canonical example rule. The paper must say plainly which results rest on which rule.

| Phase | Rule | What was found |
| --- | --- | --- |
| Early program | Canonical binary rule (x,y),(x,z) → (x,z),(x,w),(y,w),(z,w), Wolfram's illustrative example | Recurrent, translating structures exist but are fragile: 1/3 of ordinary background events damage them, no self-repair observed, and repair is provably impossible for the fixed-support architecture (white paper Sections 4–5) |
| Rule search | Ternary relations; 77,314 rules searched | 80 rules with a closed full-turnover particle class; rule 55744 survives 96.8–96.9% from 2,000 to 80,000 events; emergent local dimension ≈4.6 |
| Carrier program (Y-series) | FBCL carrier grammar ("Y33 grammar"), found by targeted search | DS001, composites, autonomous kinematics, and every mass-energy result |

A brief search found the canonical rule presented as an example, with particles described generally as rule-dependent locally stable structures. No published positive or negative result on stable particles under that rule turned up, so the early negative may be a modest contribution. A proper literature check is still required before submission.

The paper should answer two questions up front:

- **Why this rule?** The working grammar was engineered by search because it supports particles. That is an existence result in rule space, not a proposed rule of nature, and should be framed that way.
- **Causal invariance.** Relativistic behavior in the Wolfram framework rests on causal invariance. The CRR rule is not causally invariant (event order changes outcomes) and uses a global sequential scheduler. This limitation belongs in the main text, not only in the scaffolding audit.

## Proposed outline

Working title: *Persistent particles, autonomous kinematics, and the absence of operational mass-energy in an engineered hypergraph rewriting system.*

1. **Abstract.** Rewritten from scratch; the current abstract predates the Y-series.
2. **Introduction.** The question (can mass and inertia emerge from local rewriting?), the approach, a summary of positive and negative findings, and an up-front note that the work was AI-assisted.
3. **Relation to the Wolfram Physics Project.** Particles as locally stable structures, causal invariance, and what CRR adopts and departs from.
4. **Substrate and rule lineage.** Canonical rule, fragility result, ternary relations, rule 55744 search, FBCL/Y33 grammar, with a table of which results rest on which rule.
5. **Methods.** Frozen protocols, sealed holdouts, the provenance recorder, relabeling tests, surgical deletion, independent replay, and the standing scaffold-removal rule.
6. **Results I: persistent structures.** DS001, R5/R6 composites, the bond automaton, the coordination limit.
7. **Results II: autonomous kinematics.** The covariant engine, environmental speed control and reversal, three speed structures, the settling law, independent-vacuum recurrence.
8. **Results III: the mass-energy question.** Topology-blind M\_i, rest-content candidates, action versus state, the Y155 correspondence and its Y158 reinterpretation, the coupler test, and the current status (E\_0 and independent M\_i undefined).
9. **Results IV: two-particle case study.** From "wake" to preparation-dependent formation memory, as a worked example of the method.
10. **Scaffolding audit.** Condensed from white paper Section 10A.
11. **What this paper does not claim.**
12. **Open problems.** Native particle formation, causal invariance or a local scheduler, coupling architecture (Y165-C4), emergent geometry.
13. **Data, code and AI-use disclosure.**

Appendices: rule definitions; stage index; claims ledger; glossary.

## Claims list

Fourteen claims, each with its strength and supporting stages. Every number listed must enter the claims ledger and be verified against artifacts before drafting is final.

| # | Claim | Strength | Stages |
| --- | --- | --- | --- |
| 1 | The canonical binary rule is unsuitable for persistent particles: recurrent structures are fragile (1/3 destructive fraction, no observed self-repair), and repair is impossible for the fixed-support architecture | Established, tested architecture | White paper Sections 4–5 |
| 2 | Particle-supporting rules exist but are rare: 80 of 77,314 ternary rules have a closed full-turnover particle class; rule 55744 survives 96.8–96.9% from 2,000 to 80,000 events; its emergent geometry (local dimension ≈4.6) is not physical-like | Established; geometry open | Stages V–W |
| 3 | The FBCL/Y33 grammar supports an exact recurrent carrier (DS001) and a family of bonded composites with complete kinematic manifolds | Established, tested manifold | Y46–Y80 |
| 4 | Bond dynamics reduce to a finite, minimal four-state automaton derived from literal grammar roles | Established, on-manifold | Y118–Y119 |
| 5 | Each constituent supports at most two renewable bonds, found by two independent methods | Established, finite graph shell | Y121–Y123 |
| 6 | Formation history is shed: a mature bond's future does not depend on how it formed, and deleting the formation fossil has no effect on the bond itself | Established | Y129–Y131 |
| 7 | A covariant engine runs the kinematics autonomously, replacing every scripted motion and rest element, validated under thousands of relabelings | Established; rests on stated added rules | Y136–Y148 |
| 8 | The environment controls speed: deleting a specific environmental relation causes autonomous acceleration (28/28); occupancy-guarded reversal works in both directions; repeated round trips succeed (44/44 at N5); a period-2 third speed structure exists; a preregistered settling law was confirmed blind | Established; triggers applied externally | Y159–Y163 |
| 9 | The inertial curvature M\_i = N·(5/8)ln 2 is exactly topology-blind, and every topology-sensitive rest-content candidate contradicts it; the mismatch survives the full architectural rebuild | Negative, robust | Y81, Y100, Y149 |
| 10 | No conserved quantity beyond constituent number appears within the tested bases | Negative, bounded | Y109–Y112; Y165-D3-7H |
| 11 | A same-N topology-contrast correspondence holds exactly (38/38) between independently built quantities; it reflects environmental dressing, not bond-built content, and is not total-value equivalence | Bounded | Y154–Y158 |
| 12 | Within CRR as specified, E\_0 and independent M\_i cannot be defined, because no safe rest-local coupling exists; this is not a claim that rest energy is zero | Negative, structural | Y165-C, C3 |
| 13 | The two-particle effect is preparation-dependent formation memory: an exact local law (72/72) describes the receiver encountering the leader's formation remnant, but the remnant depends on preparation method even for an identical mature leader; not a particle-particle interaction | Established classification | Y165-D3-5 to D3-7R |
| 14 | Many apparent effects were artifacts of experimental scaffolding, each caught by a specific control; the paper documents the catalog and the standing scaffold-removal rule | Methodological | White paper Section 10A |

## Explicitly not claimed

The paper's Section 11 should state, without hedging, that it does not claim:

- any physical identification of particles, mass, energy, force, charge or gravity;
- relativistic behavior, or causal invariance of the working rule;
- a physically realistic emergent geometry;
- natural particle formation (particles are inserted by a prescribed procedure);
- that any rule studied is proposed as a model of nature;
- that rest energy or inertial mass is zero (only that neither is operationally definable in CRR as specified).

## Instructions for the drafting AI

1. Draft from the current `CRR_White_Paper_Draft.md` and `CRR_Companion_Section10_Mass_Inertia_Program.md`, not from memory. Preserve the reinterpretations (for example Y158's rereading of bond action) and every scope statement.
2. Organize by the outline above, not by stage chronology. Keep the main text to roughly 20–30 pages; move stage detail to appendices or cite the companion.
3. Build the claims ledger as you draft: for each number, record claim number, value, stage, artifact path and verification status. Flag any claim you cannot verify rather than rewording it.
4. Do not strengthen any claim beyond the strength column. If the evidence supports more, propose it as a note for the investigator, not in the text.
5. Write the rule-lineage table and the causal-invariance limitation into the main text.
6. Run a literature check on prior work about stable particles under the canonical Wolfram rule, and report what you find before the related-work section is finalized.
7. Include the AI-use disclosure: how stages were generated, executed and verified, and which steps the investigator directed.
8. Mark open questions inline as `[OPEN: …]` rather than resolving them silently.
