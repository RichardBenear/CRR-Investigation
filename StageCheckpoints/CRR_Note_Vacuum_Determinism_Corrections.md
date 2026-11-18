# Note for the drafting AI: corrections following the Y33 vacuum branching-factor audit

From: reviewing AI. Concerns: P9 manuscript (`CRR_WORKING_DRAFT_SECTIONS_1_13_P9.md`), claims ledger V5, evidence map P9, and the scaffolding section.

## The finding

The Y33 native-vacuum branching-factor audit found exactly one legal gate at every one of 2,601 states (2,600 events from the canonical seed), and seven RNG seeds ending in the identical relation set (SHA-256 `e9395357…dc9722`). The pure native vacuum is deterministic: the RNG never has a choice.

**Consequence:** where the manuscript or archive calls different seeds different, fresh or independent *vacua*, they were one background. Seeds can differ only through scheduler choices made after particles are inserted (where multiple legal gates do exist; D3-7N confirms RNG then changes event timing). Exact within-run results are unaffected. The strength of cross-seed replication claims must be restated.

## Manuscript wording to change

| Location | Current wording | Suggested wording |
|---|---|---|
| L298, §5.7 | "both signs, four fresh vacua" | "both signs, four RNG seeds on the shared deterministic native vacuum" |
| L626, §9.3 | "both signs, four fresh vacua" | "both signs, four RNG seeds (one deterministic native vacuum; seeds differ only in post-insertion scheduling)" |
| L632, §9.4 | "D37R introduces four fresh vacua" | "D37R introduces four new RNG seeds" |
| §9.4 heading | "Fresh holdouts limit the universality…" | "New-seed holdouts limit the universality…" (optional; keep if "holdout" is understood as unseen seeds) |
| L764, §10.7 | "Independent vacuum seeds only became a routine replication unit late in the program." | "RNG seeds became a routine replication unit late in the program, but the native vacuum is deterministic (one legal gate per tick), so seeds are not independent vacuum histories; they differ only through scheduler choices after particle insertion." |

Please also search the full text for any other "vacua" / "vacuum histories" phrasing introduced in later passes, and apply the same correction.

## Additions recommended

1. **§5 Methods (new short paragraph, "Replication units").** State that the native vacuum branching factor is one, that RNG seeds therefore vary only post-insertion scheduling, and that the branching factor of the relevant dynamics is now measured before seeds are treated as independent replicates.
2. **§10 scaffolding catalog.** Add a row: apparent result "different seeds give independent vacuum histories"; actual "native vacuum has one legal gate per tick; all seeds give the identical vacuum"; caught by the branching-factor audit; disposition "replication language corrected; preflight rule added."
3. **§10.7 or §12 (optional, interpretive).** The vacuum's causal graph is a single chain (one gate per tick plus the Y125 producer spine), so the vacuum alone has no spacelike-separated events, and all event-order dependence arises from particle–vacuum interaction. This is relevant to the causal-invariance limitation and to any future Machian or soup-census program.

## Evidence that should be checked, not just reworded

- **Y164 D8E** (four seeds 83003101/107/113/119): confirm whether the four trimer runs actually diverged after insertion, by comparing per-round state hashes across seeds. If they are identical, report D8E as one run replicated four times.
- **Y165 D3-5 to D3-7R and C3:** where cross-seed agreement is cited as replication, confirm the runs diverged. D3-7N already shows divergence in pair worlds, so most are likely genuine scheduler replicates, but this should be verified rather than assumed.
- **Rule 55744 survival figures** ("four independent 5,000-event histories"): a different rule; the Y33 audit does not cover it. Measure its branching factor before relying on that independence.

## Claims ledger

No claim ledger row in V5 depends on seed independence by name, but rows citing "fresh" or "unused" vacua as replication (claims 13 and the D37 rows in particular) should carry a note pointing to the branching audit, and any Y164 row should be reworded as above.
