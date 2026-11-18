# CRR Manuscript Review — P8 Discrepancy Report, Round 1

Oct 1, 2026 · @Richard · Reviewed: P0–P7 combined package (Sections 1–13, P1 ledger V3, P2 evidence map and scaffolding catalog, P6 literature controls, P7 sweep) and figure packages F1–F14.

## Overall assessment

The manuscript text is in good shape. It is organized by claim rather than chronology, the later reinterpretations govern consistently (Y158 over Y154/Y155, D37R over D37Q), and the scope language is careful throughout. Section 9's handling of D37R, Section 10.7's list of remaining scaffolds and the Section 11 non-claims table are publication quality. The items below are mostly consistency and completeness fixes, not structural problems.

The figures are a different matter and need a substantive redesign (see the figure assessment below). One figure, F8, has a scientific problem as well as a design one.

**Correction to my earlier P0–P3 review.** I previously said the `0/142` result was a bounded depth-4 search mislabeled as a complete census. The P7 primary-artifact sweep found `CANONICAL_0A4_K_REPORT.md`, which states that all 142 destructive branches were tested in the complete fixed-size predictive quotient. The manuscript's wording is correct and my comment was wrong. The white-paper synthesis wording ("bounded search, depth 4") is the outdated source and will be corrected on my side.

## Must-fix discrepancies

| # | Location | Issue | Proposed fix |
| --- | --- | --- | --- |
| M1 | Working title in all section files (01, 04, 05) | Still "…and the **absence** of operational mass-energy…". This conflicts with the softened Claim 12 and was agreed in the paper plan to change. | "…and no established operational mass-energy in an engineered hypergraph rewriting system." |
| M2 | Abstract (Section 1) | The agreed causal-invariance sentence is missing. It appears only in §2.2, and P0 §6 requires it in the abstract. | Add, near the end: "The working carrier grammar is an engineered existence construction with sequential event selection and is not shown to be causally invariant." |
| M3 | §8.3 and Claim 11 | The Y151 sign reversal is not mentioned anywhere. Y155's 38/38 law uses the closed admissible-path action, which reversed the sign of the earlier Y151 forward-only cross-response. A reader comparing stages will otherwise see a contradiction. | One sentence in §8.3, a P2 evidence-map entry, and a ledger row (Y151 forward-only result; Y155 corrected sign). |
| M4 | §4 rule lineage and §4.4 table | The table jumps from rule 55744 to FBCL/Y33. The X-series momentum program (X1–X45) and the early Y-series ran on the earlier carrier population before FBCL was separated (the transport grammar shared zero of eight outputs with the original rule). That phase needs a row even though no frozen claim rests on it. The white paper also refers both to rule 55744 and to an "original Rule-55584 population"; resolve against the artifacts whether these are the same rule or a typo. | Add a fourth table row and one paragraph in §4.3; record the 55744/55584 resolution in the ledger. |
| M5 | §4.1 internal note and §4.4 table | Both still say the canonical primary-artifact sweep is pending. P7 verified `0/142` from the primary report. Only `1/3` remains pending. | Update both to match P7. |
| M6 | §5 Methods | The D3-4 recurrence-obligation scheduler rule is a model extension on which multi-particle results depend (240 of 1,536 holdout events redirected), but Methods never states it. It appears only in §2.2, §7.1 and §10.7. | Add a short §5.x "Model extensions" paragraph listing D3-4 and any other added rules, stated as postulates. |
| M7 | P4 header | References `P1_CLAIMS_LEDGER_V2.csv`; V3 is current. | Update the reference. |

## Should-fix items

- **S1. Lifetime activity areas (§8.4).** The text says the Y165-D2 areas "distinguish DS001, D2R5, and D2R6" without giving them. The values (DS001 160, D2R6 320, D2R5 316) show D2R6 exactly twice DS001 and D2R5 four less, which looks like a topology-sensitive binding residual. State the numbers and say explicitly why they are not promoted to E\_0: no exchange channel, no conservation, no path independence. Otherwise a careful reader will think a result was missed.
- **S2. Settling law (§7.4).** The preregistered settling law is mentioned but never stated. Give it: first CQ1 match after return to v1 at (sum of bond spacings) + 4, equivalently 24 + n\_R6 for N5 chains, confirmed T4 24/24 and N5 44/44.
- **S3. Two-round lag (§7.3).** The 1 → 3/2 → 2 staircase has a known mechanism: each compound event reads the pre-event geometry, so a deletion can only affect the next event. One sentence would turn an apparent puzzle into an explained feature.
- **S4. Claim 10 support (§8.2).** The D3-7H failure of four simple conservation candidates is a second, independent basis. Cite it briefly, labeled as a different basis from Y112.
- **S5. Open problems (§12).** Two Gate 3 candidates recorded in the white-paper priorities are absent: settling lag (scales with N and depends on topology) and kinematic universality (the Y160 staircase is identical for every species, which is not inertia-like). Add both to §12.1 as candidate independent-response observables.
- **S6. Abstract density.** At about 330 words, with many stage-level numbers, the abstract is heavy for a community post. Consider moving 44/44 and 38/38 into the introduction and keeping the abstract at the level of findings and the main negative.
- **S7. Figure callouts.** No section cites a figure yet. Add placeholders ("Figure 4") at the planned positions so the assembly order can be checked.

## What is working well

These should be preserved through later edits:

- **D37R handled correctly (§9.4).** The text separates the robust per-method occupancy predictor (24/24) from the inherited Q law (19/24 per method, 17/24 jointly) and treats the three fresh d=40,− nulls as holdout failures. This was the most important correction from the previous round and it is fully in place.
- **Claim 6 and Claim 13 reconciled (§6.4).** The distinction between a bond's constitutive future and an external environmental remnant is stated cleanly.
- **Y155 and Y158 kept together (§8.3).** "A result surviving numerically while changing scientifically" is exactly the right framing.
- **C3 interpretation (§8.4).** It does not overclaim: the rival is not an independent work channel, which is different from showing that external work has no effect.
- **Verifier caveat (§5.8).** Independent analysis code paths are not independent dynamics engines.
- **Section 11.** The non-claims table, and the distinction between "not established" and "shown absent," are the strongest protection the paper has against misreading.

## Figure assessment

The figure plan is sound: the messages, placements and design sequence (F14 first, to set a shared visual grammar) are the right ones. The executed drafts do not yet carry those messages, and they need a redesign rather than polishing.

**One scientific problem.** F8's "exact contrast parity" panel plots predicted against "observed" values, but its own footnote says the pair table was *reconstructed from the frozen Y154/Y155 equations*. Both axes are therefore computed from the same law, so the plot is a tautology and would mislead a reader into thinking it shows measured agreement. A parity plot must use the measured Y155 values from the primary archive. Until those are extracted, the panel should be replaced by the 38-pair table itself or removed.

**Recurring design problems across the set.**

- **Overlapping and overflowing text.** F12 (labels collide around the formation support), F8 (axis label runs into the footnote), F14 (the right-hand note overflows its box, and the legend runs off the line).
- **Little data, many boxes.** Several figures are mostly bordered text boxes restating counts already in the text (the three boxes at the bottom of F12, the scorecard style of F6). A figure should show something the text cannot.
- **No axes or scales where they matter.** F8 has no tick values; F12 has no position axis even though its message is about position relative to the formation site.
- **Misleading geometry.** F12 draws the leader next to the formation support, when the point of D37K–Q is that the leader is about 250 units away by the time the receiver arrives.
- **Arbitrary color.** In F14 each bond line gets a different, meaningless color, so color cannot be used to teach R5 versus R6.
- **F14 doesn't show structure.** Its stated purpose is to "teach the reader how to see R5 versus R6," but DS001 is drawn as an oval with dots and bonds as colored lines. It needs the actual relational structure (the five-role core, the cross-core relations) from real snapshots.
- **No shared visual grammar.** Each figure invents its own symbols for carriers, relations and interventions, which the plan specifically intended to avoid.

**Data needed for a proper redesign.**

| Figure | Needs |
| --- | --- |
| F14, F4 | Actual relation snapshots for DS001, D2R5, D2R6 and one T3/T4/N5 composite at stationary rest (vertex and relation lists with role labels) |
| F8 | Measured Y155 contrast values for the 38 pairs, and Y149 M\_curv values |
| F12 | Receiver position sequence, formation-support interval and encounter point for representative D37Q cases, plus the leader's actual position at encounter |
| F10 | Per-round speed sequence for one representative Y160 and one Y163 four-leg case |
| F9 | Y158 per-channel action values (SELF, ENV, BOND) for the dimers |

## Recommended next steps

1. **Text round (drafting AI).** Apply M1–M7, then S1–S7, and return a short change log keyed to these item numbers so each can be checked.
2. **Data extraction for figures (drafting AI).** Pull the items in the data table above from the primary archives into small CSV or JSON files, one per figure. This is the step that requires artifact access.
3. **Figure round (reviewing AI), separately.** Redesign the main-text set starting with F14 to establish one visual grammar, then F12, F10 and F8, using the extracted data rather than reconstructed values. Overview figures (F1, F2, F7, F11) follow once the grammar is set.
4. **Investigator input.** The best moment for your read is after step 1, while the figures are being redone, since the text will then be close to final.
5. **Open item before submission.** The canonical `1/3` destructive fraction remains primary-pending; locate it or keep it out of the main text, as the abstract already does.
