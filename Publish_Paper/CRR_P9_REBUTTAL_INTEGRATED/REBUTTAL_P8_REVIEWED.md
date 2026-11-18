# Response to the P8 text-revision package

Reviewer: second AI. Reviewed: `CRR_P8_TEXT_AND_FIGURE_HANDOFF.zip` (P8 working draft, claims ledger V4, evidence map, change log, figure handoff).

All M1–M7 and S1–S7 items are addressed, and the four-phase lineage plus the Rule 55584 / 55744 resolution are genuine improvements. The points below are corrections, mostly ones that required data the drafting AI could not access. Supporting primary files are in `supporting_primary/`; see `SUPPORTING_FILES_MANIFEST.md`.

## R1. The figure handoff is out of date

`P8_NEXT_FIGURE_HANDOFF.md` lists F8 and the Y160 trace as blocked and F14 as needing a decision. All three are resolved in the separate figure package `CRR_Figures_For_Paper_v1.zip`:

- **F8 (now Figure 7)** uses the measured Y155 tables (`Y155_SAME_N_PAIRWISE.csv`, `Y155_COMPARATOR_POPULATION.csv`), not the equation reconstruction.
- **F10 (now Figure 5)** uses the primary Y160 per-round traces (`raw/Y160_*.json`); all 28 cases per branch are identical.
- **F14 (now Figure 3)** is the handoff's permitted option, a clearly labeled abstract structural schematic: positions, spacings and cross-core counts are measured; the pentagon glyph is stylized, and the caption says so.

## R2. Nine ledger rows can be upgraded to primary-verified

| Rows | Primary source (in `supporting_primary/`) | Confirmed |
|---|---|---|
| 9a, 9b | `Y149/Y149_MI_ALL.csv`, `Y149/Y149_KEY_RESULTS.csv` | M_curv = N·(5/8)ln 2 for all 8 identities; same-N residual 0 (`Mi_binding = PASS_ZERO`) |
| 9c | `Y149/Y149_KEY_RESULTS.csv` | `alpha_B_projected = FAIL_STRUCTURAL`; same-N B differs by +2 for D2, T3 and T4R666 while M_curv ties |
| 11a, 11b | `Y155/Y155_KEY_RESULTS.csv`, `Y155/Y155_SAME_N_PAIRWISE.csv` | 38/38 pairs for both comparators; totals 0/7 development and 0/11 N5 |
| 11d | `Y151/STAGE_Y151_..._REPORT.md` | Y151 sign relations (see R4) |
| 7b, 7c, 7d | `Y148/STAGE_Y148_..._REPORT.md` | 640/640 periods; 560/560 relabel checks; 28/28 handoffs (also 352/352 successor, 14/14 lineage self-checks) |

With these, §8.5's statement that Y149 and Y155 rest on synthesis "pending primary-stage reports" can be removed. The Y160 summary files are included as provenance for Figure 5a.

## R3. Broken equation in §4.1

The canonical rule reads `(x,z) ` followed by a line break and `ightarrow`: the `\r` in `\rightarrow` was interpreted as a carriage return. Correct text:

```
\[
(x,y),(x,z) \rightarrow (x,z),(x,w),(y,w),(z,w),
\]
```

## R4. §8.3 overstates the Y151 / Y155 relationship

"Retaining the corresponding magnitude structure" implies the same quantity with its sign flipped. They are different quantities with different coefficients:

- **Y151** (forward-only cross response): ΔM_cross = (171/16) ΔB_proj = −(171/16) ΔF_flux
- **Y155** (closed admissible-path action): ΔM_adm = (277/48) ΔF_flux = −(277/48) ΔB_proj

What carries over is the structure, not the magnitude: in both, the two comparators enter with equal and opposite coefficients. Suggested wording: "Y151's forward-only cross response gave ΔM_cross = (171/16)ΔB_proj = −(171/16)ΔF_flux. The closed admissible-path action of Y155 is a different quantity, with ΔM_adm = (277/48)ΔF_flux = −(277/48)ΔB_proj: the comparators again enter with equal and opposite coefficients, but the alignment is reversed."

## R5. Phases 3 and 4 may be the same grammar (please verify)

The draft treats "the Y47 transport grammar" (phase 3) and "FBCL/Y33" (phase 4) as distinct architectures. In the white-paper synthesis, FBCL *is* the Y47 transport construction, renamed at Y48 because it shared zero of eight outputs with Rule 55584, and G6 was first passed on DS001 under it at Y47 (M = (5/8)ln 2). If confirmed against the Y47/Y48 artifacts, phase 3 should end with "the Y47 transport grammar, renamed FBCL at Y48," and the §2.3 sentence listing "the Y47 transport grammar, and FBCL/Y33" as separate dynamics should be corrected. The reviewer does not hold the Y47/Y48 archives, so this rests on synthesis and must be checked.

## R6. §8.4 wording

"Near-doubling" undersells the result: D2R6 is exactly twice DS001 (320 = 2 × 160), and D2R5 is exactly four less (316). Stating it exactly makes the explanation for not promoting the quantity to E0 more important, and the text already gives it.

## R7. Figure callouts and numbering

The draft carries the original fourteen callouts; the figure set is now eleven. Use the mapping table in `CRR_Figures_For_Paper_v1/README_FIGURES.md`. In brief: drop callout 2 (use the §4.5 table), merge callouts 4–5 into one figure, merge callout 7 into Figure 4 panel b, and renumber the rest 1–11.

## Suggested next steps

1. Apply R3, R4, R6 and R7; verify R5 against the Y47/Y48 artifacts.
2. Upgrade the R2 ledger rows using the supporting files.
3. Pair the text with `CRR_Figures_For_Paper_v1`; the draft is then ready for the investigator's full read.
