# CRR paper figures, version 2 (P9 integrated)

Eleven main-text figures in one shared visual grammar, numbered to match the paper. This package is the P9-integrated revision of the second-AI figure set. It supersedes all earlier drafts. The original reviewer set was accepted except for two evidence/lineage safeguards: Figure 1 now explicitly identifies the Rule-55584 bridge without treating Y47 and FBCL as separate laws, and Figure 2 removes the primary-pending 2-in-6 contact fraction and synthesis-only repair-rate panel.

## Contents

- `figures/` — PNG (300 dpi) and SVG for each figure. File names give the paper number first, then the working label (for example `Figure_07_F8_...`).
- `CAPTIONS.md` — caption, data sources and placement for each figure.
- `scripts/` — the generating scripts and every data file they read. To regenerate: `cd scripts && python3 f8.py` (and so on); output goes to `scripts/out/`. Requires matplotlib and numpy.

## Visual grammar

- R5 bond: orange. R6 bond: teal. No other figure element uses these two colors.
- DS001 constituent: slate pentagon glyph (five core vertices, central direction marker h).
- Vacuum / environment: light gray. External intervention: crimson. Untouched control: mid gray.
- Titles live in captions, not inside the figures.

## Mapping from the P8 draft's figure callouts

The P8 draft still carries the original fourteen callouts. Replace them as follows:

| Draft callout | Becomes |
|---|---|
| Figure 1 (roadmap) | Figure 1 |
| Figure 2 (rule lineage) | **No figure**; use the §4.5 rule-lineage table |
| Figure 3 (canonical fragility) | Figure 2 |
| Figures 4 and 5 (structures, R5/R6 grammar) | Figure 3 (one combined figure) |
| Figure 6 (carrier engine) | Figure 4 |
| Figure 7 (Y148 scorecard) | **Merged** into Figure 4, panel b |
| Figure 8 (speed control) | Figure 5 |
| Figure 9 (decision map) | Figure 6 |
| Figure 10 (Y155 contrast) | Figure 7 |
| Figure 11 (Y158 reinterpretation) | Figure 8 |
| Figure 12 (rest coupling, C3) | Figure 9 |
| Figure 13 (D37 worldline) | Figure 10 |
| Figure 14 (D37 ladder) | Figure 11 |

## Known data limitations (also stated in captions)

1. Figure 3: literal relation tuples are not preserved in the archives; the pentagon glyph is stylized. Positions, spacings and cross-core counts are measured.
2. Figure 2 intentionally omits the separate 2-in-6 destructive fraction because ledger 1a remains primary-pending. The displayed 0/142 census is primary-verified.
3. Figure 10d: summary values from the D37Q final checkpoint, not raw per-case files.
