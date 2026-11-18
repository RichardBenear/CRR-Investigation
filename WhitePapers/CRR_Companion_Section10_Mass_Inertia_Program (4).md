# CRR Companion Document — Section 10: The Mass and Inertia Measurement Program

**This document is Section 10 of the main white paper
(`CRR_White_Paper_Draft.md`), extracted into its own file because it has
grown to be the fastest-moving and most detailed part of the
investigation. Section numbering (10, 10.1, 10.2a, etc.) is preserved
exactly as it appears in the main document, so every cross-reference in
either document, and in prior conversation history, continues to resolve
correctly.**

**How to use these two documents together:** the main white paper
(Sections 1–9, 11, and Appendices A–B) contains the motivating question,
the substrate, the four structural no-go theorems, the engineering
search through Stage W, and the PRO repair criterion — read that first
for context. This document contains everything from Stage X1 onward:
the attempt to actually measure velocity, momentum, and mass on a
surviving candidate. **Always share both documents together** when
starting a new session or handing this off to another instance — the
main document's Section 10 is now only a short summary and pointer to
this file, and this file assumes the main document's Sections 1–9 as
background.

Figures referenced below live in the same `figures/` folder used by the
main document.

---

## 10. A measurement framework: from recurrent defect to mass and inertia

Everything in Sections 4–9 addresses survival: can a candidate structure
persist at all. This section states, in advance of having such a
structure in hand, exactly what would need to be measured on it before
"mass" or "inertia" could be claimed as anything more than the working
identification of Section 1. Stating the target precisely now is meant to
prevent the investigation from mistaking a future survival success for a
physics result — clearing this section's tests is a separate, additional
requirement.

**This framework is, as of Section 7.3, no longer purely aspirational.**
Rule 55744 is the first candidate robust enough (96.7–96.9% stable
producer-flow survival) that attempting the program below is a reasonable
next stage rather than a hypothetical one. The two definitional gaps
flagged when this framework was first written — an operational definition
of the conserved recurrence content $\mathcal{R}$ (Section 10.1) and of
discrete velocity for a recurrent defect (Section 10.2) — remain open and
should be resolved specifically against rule 55744's own producer grammar,
not defined in the abstract.

### 10.1 Rest recurrence energy

A stable, non-translating recurrent defect satisfies $F^p(\Phi) = \Phi$
for some period $p$, defining an intrinsic angular recurrence rate
$\omega_0 = 2\pi/p$. If a conserved recurrence content $\mathcal{R}$ can
be defined for such a defect — a quantity conserved across the cycle, not
yet given an operational definition anywhere in this investigation — the
natural candidate rest energy is

$$
E_0 = \mathcal{R}\,\omega_0.
$$

This is explicitly a candidate, not a result: $\mathcal{R}$ requires a
precise, checkable definition before this expression does any work, and
none has yet been proposed.

**Status as of Stage X45: this section was unresolved for the entire
momentum program (Stages X1–X45).** A deliberate pivot redirected effort
here, tracked as a new **Y-series**, before any further momentum
refinement. Results follow.

![Rule 55584 Winner 28 and Rule 58846 Candidate 8: verified vertex-level transitions](figures/fig20_rule_55584_58846_transitions.png)

*Figure 8c. One verified contact-mediated event for each of the two
primary carriers the Y-series tests, using real vertex identities from
the simulation logs (X44 boundary data) rather than illustrative
placeholders. Winner 28 shows high constituent turnover (3 of 6
vertices replaced in a single contact); Candidate 8 shows low turnover
(1 of 6). The exact ternary relations connecting these vertices are not
independently verified for either rule the way Rule 55744's are (Figure
4b) — only the vertex identities and the gate/contact pattern are
confirmed here.*

### 10.1a Five candidates, one real signal: regeneration/closure burden (Stage Y1)

Y1 tested five frozen candidate definitions for $\mathcal{R}$ against the
twelve robust Rule 55584 carriers (Stage X34/X44's population) plus Rule
58846 Candidate 8 as an external reference, requiring each to pass two
bars: stable within a carrier across independent natural contexts, and
genuinely different across carriers.

Four candidates failed cleanly: structural relation count times
statistical recurrence frequency ($F=1.37$, $p=0.27$); net phase-action,
deliberately overlapping the already-falsified X43 winding-rate program
($F=0.88$, $p=0.56$); phase-arc activity, an improvement but still
short of the bar ($F=2.25$, $p=0.069$); and the typed access/amount/role
loss components individually, none of which tracked their own carrier's
value better than shuffled pairing across a later recurrent context.

**One candidate passed both bars simultaneously — the first in this
entire investigation's history of proposed $\mathcal{R}$ candidates.**
The regeneration/closure burden,
$R_C = 1 - P(\text{exact return within 2 particle-coupled rewrites})$,
measured on a frozen, equally-weighted two-class perturbation panel
(one-role external contact; four-role internal contact), showed real
repeatability within carrier across independent recurrent contexts
(ICC $=0.584$; base-vs-replication $r=0.652$; carrier-pairing
$p=0.032$) and genuine between-carrier discrimination ($F=3.803$,
$p=0.019$, across 11 directly-replicated 55584 carriers). Rule 58846
Candidate 8 sits consistently at the high-burden end (0.80 and 0.67,
reported descriptively, not pooled into the 55584 statistics).

**This is explicitly not yet rest energy** — it is a dimensionless,
bounded regeneration-burden observable, with imperfect stability for at
least one carrier (carrier 5) — but it is the first candidate to survive
a change of recurrent context while separating carrier identities,
qualitatively different from every failed momentum-program observable.

### 10.1b–c Depth censoring resolved: a stable relative scale, no absolute one yet (Stages Y2–Y3)

*(Stage Y2's own report was not preserved; its content is reconstructed
here from Y3's direct description and continuation, since Y3 explicitly
restates and extends Y2's construction before proceeding.)* Y2 defined
the bounded intrinsic regeneration burden $B_D = E[\min(W_{\text{regen}},
D)]$, replacing Y1's binary two-step success/failure test with the full
minimum-work distribution up to a censoring depth $D$, and found a
strong carrier-specific signal at $D=12$.

**Y3 tested whether this was an artifact of the specific depth chosen,
by re-deriving $B_D$ at $D\in\{6,8,12,16\}$ from the identical restart
trajectories** (a nested-prefix audit confirmed 1,536 of 1,536 early
recoveries reproduce exactly across depths — genuine extensions, not
resampled noise). Carrier separation does not wash out as the horizon
extends — if anything it strengthens slightly (ICC $0.651\to0.682$
from $D=6$ to $16$) — and **relative carrier ordering has essentially
converged**: $D{=}12\to16$ gives Spearman $\rho=0.986$; a PCA across all
four depths puts 99.53% of cross-carrier variance on a single component
with nearly identical loadings at every depth (≈0.50 each). A fresh,
never-before-used fourth natural context remains significantly matched
to carrier identity at every depth (Pearson $r=0.726$–$0.750$).

**But the absolute value of $B_D$ has not converged** — the median
carrier burden still rises by 0.469 units per additional censoring tick
at $D=16$, exactly as expected when a nonzero fraction of standardized
perturbations remains structurally unresolved. Y3 correctly refuses to
call this $\mathcal{R} = B_{16}$: a genuine *relative* regeneration-content
scale exists; no absolute normalization does yet.

**Y3's most important methodological result may be what it declined to
claim.** A naive test of $E_0 = \mathcal{R}\,\omega_0$, using $B_{16}$
times one frozen carrier-level $\omega_{\text{cond}}$, looked strong
($F=14.3$, $p=5.5\times10^{-8}$) — but Y3 recognized this could be
mechanically inflated by multiplying every context of one carrier by the
same carrier-specific constant, and checked block-level stability of
$\omega_{\text{cond}}$ itself directly: it is not stable (block CV
$0.401$, $F=1.34$, $p=0.28$). **The apparent $E_0$ signal was therefore
not promoted** — exactly the discipline that caught Stage T's PRO
criterion and Stage X27's index error, now applied to this program's own
first excited result.

### 10.1d Frequency solved; a two-component asymptotic phenotype established; scalar $\mathcal{R}$ still not derived (Stage Y4)

Y4 addressed both of Y3's open bottlenecks directly.

**The frequency clock is now genuinely stable.** Testing a reliability-
weighted renewal intensity, $\omega_{\text{renew}} = 2\pi\,N_{\text{return}}
/N_{\text{particle-hit}}$, against 40 fresh trials split into two
independent 20-trial blocks per carrier gives block Pearson $r=0.953$,
Spearman $\rho=0.979$, and carrier ICC $=0.934$ — a dramatic improvement
over the conditional-return clock's block ICC of $0.118$ that sank Y3's
$E_0$ test. **This resolves the frequency bottleneck Y3 identified.**

**The censoring-depth problem is resolved by fitting a proper survival/
cure mixture instead of a bounded expectation.** $\mathcal{R}_{\text{asym}} =
(q_\infty, \mu_{W|\text{return}})$ — asymptotic eventual-recovery
probability and mean successful-recovery work — both retain significant
carrier identity ($F=5.06$/$4.70$, $p<0.0002$ both) and fresh-holdout
replication ($r=0.73$/$0.77$), essentially insensitive to the exact
geometric tail order fitted ($\rho=0.986$–$1.000$ across tail orders
1–3). One real caveat: $q_\infty$ is identifiable only because the
simulator's "lost" state is trusted as genuinely nonrecovering, not
mere censoring — reported explicitly as a modeling assumption, not
hidden.

**Deliberately, no scalar $\mathcal{R}$ is promoted.** Several transparent
combinations of $(q_\infty,\mu_W)$ were computed for completeness
(inverse survival, retry-normalized work, a throughput-like product),
each showing real signal (ICC $0.51$–$0.60$) — but Y4 explicitly declines
to select one because it fits the data best, calling this out as
"tuning the definition of mass after seeing the answer." The regeneration
phenotype remains genuinely two-component.

**Net Y1–Y4 result.** A recurrent CRR carrier possesses a reproducible,
context-independent regeneration phenotype and an exceptionally
reproducible renewal clock. What is missing is not more data but a
principled reason to collapse two components into one scalar — a
narrower, better-specified problem than the one this pivot started
with.

**Recommended next stage (Y5 — Renewal Action / Conjugate Content
Test).** Do not search further algebraic combinations of $q_\infty$ and
$\mu_W$. Instead construct locked composites of two or more
independently-characterized carriers and test whether a regeneration
functional is *additive under composition* — the same test that would
distinguish a genuine extensive physical quantity (like real energy or
mass) from a merely convenient statistic — and require any surviving
candidate to predict low-velocity propagation/inertial response without
refitting, before retesting $E_0 = \mathcal{R}\,\omega_{\text{renew}}$.

### 10.1e A mechanically-derived, additive scalar — and the one test still missing (Stage Y5)

Rather than search further ad hoc combinations of $(q_\infty,\mu_W)$, Y5
asked what functional form composition itself forces.

**The composition law is derived, not assumed.** For two independent
recurrent units that must both remain viable, joint recoverability
multiplies ($q_{AB}=q_Aq_B$) while successful recovery work sums
($\mu_{AB}=\mu_A+\mu_B$). Requiring a continuous scalar content
$R(q,\mu)$ satisfying $R(q_Aq_B,\mu_A+\mu_B)=R(q_A,\mu_A)+R(q_B,\mu_B)$
has a unique continuous solution:

$$
R(q,\mu) = a\mu - b\ln q.
$$

This single step rules out every previously-tried rational combination
(retry-normalized work, odds-work, raw failure probability) as
fundamental — none of them satisfy this equation, confirmed by their
large median relative-additivity errors (0.62, 1.50, 0.19 respectively,
against exactly 0 for the derived form across all 220 tested
three-carrier compositions, to floating-point precision). This
exactness is a check that the algebra was implemented correctly, not an
independent empirical finding — the genuine discoveries are what
follows.

**Three things that did not have to be true, and were.** (1) The
conversion scale between the two extensive coordinates, obtained
independently from the mean particle-coupled work preceding a genuine
structural-loss event, is $\ell_0 = 8.703$ hits — and shows **no
carrier dependence at all** ($F=0.80$, $p=0.64$, ICC $=-0.073$), with
leave-one-carrier-out estimates confined to $8.54$–$8.85$ and exact
rank preservation ($\rho=1.0$) in every fold. A freely-varying quantity
turning out to be one shared constant across twelve independently-
discovered carriers is a structural finding, not a guarantee of the
derivation. (2) The resulting scalar
$\mathcal{R}_{\text{act}} = \mu_{W|\text{return}} - \ell_0\ln q_\infty$
retains genuine carrier identity and fresh-context replication
($F=8.65$, $p=3.2\times10^{-7}$, ICC $=0.657$; holdout $r=0.799$,
$\rho=0.636$) and is insensitive to the geometric tail order fitted
($\rho=0.986$–$1.000$ across orders 1–3). (3) Combined with Stage Y4's
renewal clock, $E_0=\mathcal{R}_{\text{act}}\,\omega_{\text{renew}}$
**clears the characteristic-value bar Y3 explicitly failed** —
independent-block ICC $=0.918$, block Pearson $r=0.940$, holdout
$r=0.722$ — the most stable population-level result found anywhere in
this investigation's measurement program.

**Why this is still not called rest energy.** The decisive remaining
test — the same scalar independently predicting a measured low-velocity
inertial response, $m_i = \partial^2E/\partial v^2|_{v=0}$ — cannot yet
be run honestly, because the autonomous Rule 55584 carriers still lack
a demonstrated continuously-variable spatial velocity observable. Using
an earlier reduced model's dispersion relation (rule 55744's forced
branching, or the massless triangle's own kinematics) would make the
test circular. This is the same unresolved gap the momentum program
(Sections 10.2b–10.2x) left open, now sitting directly in front of the
one test that would make $\mathcal{R}_{\text{act}}$ physically
meaningful rather than only statistically excellent.

**Recommended next stage (Y6 — Independent Inertial Curvature Test),
with two refinements.** Freeze $\mathcal{R}_{\text{act}}$ and
$E_{0,\text{act}}$ exactly as derived, and test
$m_i \propto E_0$ against an independently-obtained small-velocity or
translation-bias family, with no carrier-specific fitting. Two
additions to the stage as originally proposed: (a) before attempting
the harder velocity problem, apply $\mathcal{R}_{\text{act}}$ to the
massless triangle as a cheap, already-computable consistency check —
its unconditional self-sustenance gives $q_\infty=1$ trivially
($-\ell_0\ln q_\infty=0$), so a genuine rest-content scalar should
plausibly return a value at or near zero for a known massless case,
independent of solving the velocity problem at all; (b) rather than
requiring literal spatial translation, which has failed in five
independent forms across the momentum program (Sections 10.2b, 10.2h,
10.2t, 10.2y, 10.2bb), consider the capacity-bias magnitude
established in Stages X28–X29 (the real, mechanistically-explained
forward-hemisphere transport bias) as a candidate generalized-velocity
proxy, since the curvature test only requires a controlled, varying
quantity, not necessarily displacement itself.

### 10.1f The kinematic gate fails, precisely and instructively; a tempting shortcut correctly declined (Stage Y6)

Y6 froze Y5's $\mathcal{R}_{\text{act}}$ and $E_0$ definitions exactly
and set out a seven-gate validity protocol (same carrier identity;
independent signed velocity; a near-rest family; independent dynamical
cost; finite quadratic curvature; population replication; only then the
out-of-sample mass comparison) before attempting the decisive test.

**An exhaustive re-audit of the entire prior motion program confirms, one
final time and more strictly than before, that no existing observable
qualifies.** X27/X28's redirect cost gives a controlled intervention and
an independent rewrite-count response, but no velocity (23 realized
rewrites, 23 redirected — no local turning penalty exists to build a
family from). X29's scheduler-weighted bias is real but is a static
population frequency, not a signed, tunable quantity. X30 found 0 of 40
unrestricted histories even producing a second exact return. X33/X34
confirmed strong instantaneous directional dressing with no persistence
across renewals. X43/X44's winding rate is broad, path-dependent, and
non-persistent. None satisfy gates G2 or G3.

**A tempting, structurally-perfect shortcut was correctly refused.** A
reduced theoretical model (referenced here as "E17," not independently
reviewed in this document) has exactly the desired mathematical shape —
a dispersion relation $\Omega(k)=\sqrt{\omega_0^2+4c_h^2\sin^2(k/2)}$
giving finite curvature and $m_i=E_0/c_h^2$ near $k=0$. Y6 declined to
use this as validation, correctly identifying that $\omega_0$ and
$E=\mathcal{R}\Omega$ are constructed into that reduced model by
assumption, not independently discovered — using it to "confirm" Y5
would recover an assumption already built into the construction.

**The precise diagnosis of what is actually missing.** Two further
referenced explorations ("E18," "E19") narrow the gap to a specific
variable: not the absence of a position observable (Section 10.2a has
had one since early in the momentum program), but the absence of
**multiple, concurrently-existing, identity-preserving continuations of
the same recurrent carrier that remain relationally distinguishable from
each other across further recurrence turnovers.** Every translation
attempt so far has produced either zero net displacement (the extrusion
finding, Sections 10.2b–10.2c) or a single successor indistinguishable
from any alternative — never genuine, persistent branching of one
identity into distinguishable spatial alternatives.

**Consequence for Y5, stated without either overclaiming or discarding
it.** Y6 neither falsifies nor validates $\mathcal{R}_{\text{act}}$. It
remains the canonical recurrence-content candidate and
$E_0=\mathcal{R}_{\text{act}}\omega_{\text{renew}}$ the canonical
rest-energy candidate; physical inertial mass remains unestablished, and
the bottleneck is now precisely located as autonomous spatial kinematics,
not the energy scalar itself.

**A fully pre-registered protocol for the eventual test** was frozen now,
before any mobile carrier exists, specifically to prevent future tuning:
rest plus at least two symmetric velocity magnitudes per carrier;
velocity measured independently of $\mathcal{R}_{\text{act}}$/$\omega_
{\text{renew}}$/$E_0$; an independent dynamical cost; the even response
$\Delta A_{\text{even}}(v) = \tfrac12 M_i v^2 + O(v^4)$; population
replication across at least six carriers; only then $M_i=\alpha E_{0,i}$
with one global $\alpha$ and held-out carriers.

**Recommended next stage (Y7 — Mobile Multi-Anchor Worldtube
Kinematics), plus one addition.** Construct a recurrent carrier with
several concurrent frontier anchors and search for at least two future
continuations that are locally isomorphic as the same particle, remain
relationally distinct from each other, and stay distinct across multiple
turnovers — the specific missing variable Section 10.1f's diagnosis
identifies — before running Y6's frozen curvature protocol. In addition,
independent of Y7's harder problem: apply $\mathcal{R}_{\text{act}}$ to
the massless triangle now, as a cheap consistency check requiring no
new kinematic architecture — its trivial $q_\infty=1$ predicts near-zero
rest content, testable immediately against a known massless case.

### 10.1g Persistent spatial alternatives found, then shown to be an oscillation, then a genuine composable operator — still not a velocity (Stages Y7–Y9)

**A documentation gap was corrected first.** Stage Y6 had referred to
"E17–E19" without provenance; Y7 clarified these are formal prior
exploratory stages on an older R14 branch (the original canonical rule
from Section 2.1), not informal notes, and supplied full reports
(extended in this package to E20). Their scope is explicit: E20's
finding of an effective rank-3 local relational mobility space on R14
does not transfer to Rule 55584 and is treated only as a proof that this
*type* of mobility is possible in a CRR-like substrate. E17's theoretical
framework, worked independently on this older branch, derived a
dispersion relation $\Omega(k)=\sqrt{\omega_0^2+4c_h^2\sin^2(k/2)}$ giving
finite curvature $m_i=E_0/c_h^2$ for *homogeneous history translation*,
but also proved that a "pure screw" recurrence (translation without
independent co-moving structure) is exactly massless-like — zero
curvature. E19 tested two concurrent R14 worldlines directly for
gravitational attraction and found none (0 of 30 perturbations reduced
future separation); E20 found genuine *unforced* relative divergence
between independent worldlines, explicitly not interpreted as
cosmological expansion but as a structural artifact of that carrier
construction — a direct echo of the X-series extrusion finding on an
entirely different substrate.

**The massless-triangle consistency check proposed after Y6 was run, and
gave the hoped-for result.** The triangle does not instantiate Y5's
strict recovery experiment (it never leaves exact recurrence in the
tested core-preserving challenge), but the natural zero-recovery boundary
extension — treating an already-exact structure as recovered at zero
work — gives $q_\infty=1$, $\mu_{W|\text{return}}=0$, and therefore
$\mathcal{R}_{\text{act}}^{\text{triangle}}=0$ exactly. This is a
boundary-condition control, not a direct application of the same
ensemble used for dressed carriers, but it is genuine, positive,
structural support for $\mathcal{R}_{\text{act}}$ behaving as a real
rest content should for a known massless case.

**Stage Y7 found the first persistent, distinguishable relational
alternative in the entire Rule-55584 program.** Using Winner 28's three
highest-external-participation roles as a frozen worldtube cross-section
and a 24-landmark external panel (72-component relational signature, no
Y5 quantity involved), two of the fourteen X37 exact-return branches were
found to share the same predictive class (cosine $=1.0$) while differing
in 36 of 72 relational coordinates (RMS $=0.882$) — and this separation
persisted through four further exact recurrence turnovers without
reconverging. This is qualitatively different from every earlier
translation attempt, which either produced zero net displacement or
collapsed to a unique successor.

**Stage Y8 immediately, correctly downgraded this.** Following the same
branch pair through additional turnovers showed the apparent one-turn
"velocity" ($+0.401$) is one leg of an exact two-state oscillation
($\Delta x=0$ over two turnovers); the full controlled continuation
quotient closes on just four fixed coordinate values with zero net
displacement in every recurrent cycle. Replaying the natural 70-trial
unforced ensemble found zero four-interval same-sign persistent
candidates, and large apparent natural displacements correlate strongly
with intervening ambient vacuum activity (Pearson $r=0.795$) — a real
warning that raw fixed-landmark coordinates conflate genuine motion with
background evolution, exactly the concern flagged when this reference-
frame methodology was first introduced (Section 10.2a).

**Stage Y9 built a background-corrected concurrent ruler and found a
genuine composable operator — that still fails to translate.** Subtracting
contemporaneous landmark deformation reduced median apparent displacement
from $0.802$ to $0.047$; 90 same-support intervals with up to 84
intervening vacuum rewrites showed *exactly zero* drift under the
corrected ruler, confirming apparent motion accumulates only during
active recovery, not from ambient time. A single one-event operator was
found to be the *unique* exact-return gate at the base boundary, and
composes exactly for 12 consecutive applications — but its spatial action
is a precise period-2 flip (zero net displacement every two turns), and
the natural corrected displacement across the broader archive is
anti-persistent (adjacent-step correlation $r=-0.390$, only 11 of 54
nonzero pairs retaining sign). A composable recurrence operator is not
automatically a translation operator.

### 10.1h Phase-conditioned relocation achieved once, and the same frontier-regeneration obstruction reappears in a new, stronger carrier (Stages Y10–Y11)

**Stage Y10 allowed the operator to differ by recurrence phase and found
real, repeatable, nonzero one-period relocation** — the first anywhere in
the Rule-55584 program. From a frozen library of 119 recovery templates
(not invented after seeing displacement), 8 of 598 candidate phase-law
pairs produce a nonzero first-period displacement ($\Delta x=+1.391$,
confirmed across 19 independent branch realizations, not one lucky
choice), and an exhaustive automorphism check ($6!$ permutations, only
the identity preserves the exact structure) ruled out a hidden role-
relabeling explanation. **But not one of the 19 nonzero candidates
completes a second period** — $T_+^2$ does not exist anywhere in the
tested space, confirmed further by finding zero repeating two- or
four-segment phase cycles in the natural archive (0/30, 0/12). The
particle survives the translation exactly; what fails is regenerating the
condition needed to repeat it.

**Stage Y11 localized this precisely.** The consumed interface is not
simply "the $O_0$ gate" — a legal gate with the right abstract signature
still exists at the translated endpoint. The actual requirement is a
five-relation scaffold *plus* the external recruit occupying a specific
causal-birth-order slot relative to the carrier ($s_2<E<s_5$), verified
directly (not fit) by exhaustive slot testing and cross-checked against
all 12 of Y9's successful compositions. At the translated Y10 endpoint,
the scaffold survives completely intact, but the recruit lands in the
wrong slot — translation misaligns the frontier rather than destroying
it. The *first* layer of this frontier does legally regenerate under
ordinary particle-coupled dynamics (established positively, not merely
failed to falsify), but the complete multi-step program does not: a
bounded two-regeneration search produced 4,118 exact recurrent outputs
and zero complete translation-ready states, and an independent 80-trial
unforced ensemble found 76 exact returns, 15 restoring the first layer,
4 restoring the first launch contact — and, again, zero complete.

**This is the third independent occurrence of the same structural
obstruction in this investigation, on a completely different carrier and
a completely different search path.** Rule 55744's X8–X12 arc
(Sections 10.2c, 10.2f) found single-shot frontier recruitment
achievable and self-renewal impossible. Winner 28's Y10–Y11 arc, via an
entirely independent kinematic construction, reaches the same shape of
wall: relocation once, yes; self-propagating translation, no. Combined
with E17's independent theoretical prediction that pure translational
recurrence is massless-like and requires "independent co-moving
recurrence" for finite inertia, this is no longer plausibly a
coincidence specific to one carrier or one investigative path — it has
the shape of a structural property of this entire match-and-create-
fresh-vertex rule family, in the same sense the old-handle non-creation
theorem (Section 10.2d) turned out to be general once recognized.

**Recommended redirection before Y12.** Given three independent
confirmations, attempt a general proof (or a concrete counterexample) of
whether *any* rule in this family can admit a self-renewing translation-
frontier program, before further empirical search. A proof would
determine in advance whether Y12's search (below) can succeed at all in
this architecture; a counterexample would be a constructive path to the
missing piece, worth more than continued incremental search.

**Y12, as proposed (Self-Regenerating Translation-Frontier Program
Search), if the theorem attempt does not resolve the question outright.**
Represent the translation frontier as a full sequence
$F^{(0)}\to F^{(1)}\to F^{(2)}\to\cdots$ rather than a single static
motif; search for self-generating step pairs among legal particle-
coupled dynamics rather than keeping the current 8-hit program fixed;
require at least 4, preferably 8, consecutive full translation periods
with bounded residual before interpreting any result as genuine
translation; only then reopen the inverse-translation and second-
magnitude search, and only after that approach Y6's frozen curvature
protocol.

### 10.1i Frontier self-renewal solved naturally, across multiple rules — and the wall relocates to orientation transport (Stage Y13)

Rather than continue refining Winner 28, Y13 ran a broad, disciplined
architecture search across rule space, using staged go/no-go filters
that abandoned failing constructions rather than deepening them — the
resource-efficient practice this kind of search needs. Several dead
ends were closed cleanly: the twelve nine-output recurrence variants
around Rule 55744 showed 0/12 intrinsic self-translating cycles; a
strict mandatory six-role look-ahead grammar kills substrate viability
outright (dead within 1–3 events on every tested rule); passive
disjoint-vacuum regeneration of a look-ahead relation succeeded 0/24
times.

**The genuine breakthrough is a single, elegant causal-ordering fix.**
Creating the fresh frontier vertex $q$ *before* the fresh core vertex
$w$ within the same event — rather than after — places $q$ in exactly
the causal-rank slot the next boundary-recruitment step requires. This
one change is enough: combined with X7's genuine pre-existing-ambient-
vertex recruitment, six tested rules (59436, 55584, 55744, 47332,
54776, 54567) each achieve 12/12 consecutive exact controlled shifts,
and — decisively — **101 natural translating start motifs and 69
sampled worldtubes across six independently-evolved vacua complete a
perfect 69/69 on eight autonomous exact shifts, with no controlled
laboratory construction required.** Separately, a minimal two-fresh-
vertex frontier architecture was found to support autonomous self-
renewal in 21 exact rules distributed across all eight tested branching
recurrent cores (27399, 47891, 52067, 54581, 55584, 55585, 55744,
55746) — confirming self-renewing frontier structure is not a singular,
fine-tuned property of one carrier, but occurs generically once the
grammar is allowed a second fresh vertex.

**This is the first time frontier self-renewal has been achieved
naturally, after three independent failures on this exact question**
(Rule 55744's X8–X12 arc, Sections 10.2c/10.2f; Winner 28's Y10–Y11
arc, Section 10.1h). Both prior arcs found single-shot relocation
achievable and self-renewal impossible; Y13 shows self-renewal *is*
achievable, given the right causal ordering and a second fresh vertex.

**With frontier renewal fully solved, spatial momentum is not merely
absent — it is anti-persistent, and precisely so.** The concurrent
relational embedding diagnostic, applied to all 69 exact natural
worldtubes with promotion requiring repeated same-direction
displacement (not mere nonzero motion), found 0 of 69 spatial
promotions and 0 of 69 four-step same-direction runs. Mean adjacent-
displacement cosine across the sample is $-0.749$ (median exactly
$-1$), consistent across all six rules individually ($-0.65$ to
$-0.79$) — the displacement reliably reverses rather than merely
failing to persist, a sharper and more informative failure mode than a
null result.

**The resulting reframing connects to something the momentum program
already found independently.** Y13 concludes the missing object is not
another scalar frontier property but a **covariantly-transported
orientation frame**,
$\Xi=(C,\mathcal{F},\hat{d})$, requiring $\hat{d}_{n+1}\cdot\hat{d}_n>0$
before spatial coherence should be expected at all. This is
structurally the same lesson Stage X35 learned for Winner 28's
interaction current (Section 10.2x): raw displacement was incoherent
in the fixed frame, but became coherent once evaluated in the frame
co-rotating with the dressing's own phase. Two independent
investigative threads — the momentum program's holonomy work and this
frontier-architecture search — have converged on the same missing
ingredient from different directions.

**Four observables that must not be conflated, stated explicitly by
this stage**: recurrent identity, material/support turnover, causal/
frontier propagation, and spatial momentum. Y13 achieves the first
three simultaneously and autonomously; the fourth still fails.

**Recommended next stage (Y14 — Orientation-Preserving Worldtube
Rule-Space Census), with one cheap addition.** Before a full new
census, reuse the 69 already-computed frontier-first worldtubes
directly: test whether their displacement vectors cohere when
evaluated in a frame co-rotating with an already-available local
structural quantity, the same diagnostic that worked for Winner 28's
current in Stage X35, rather than assuming a fresh rule-space search is
required. For the main census as proposed: compute the local relational
frame map from incoming to outgoing frontier/core frame at each exact
self-renewing step, and reject candidates whose one-period map is
parity-reversing, involutive, exactly period-2, or antipodal *before*
running expensive evolved-vacuum displacement tests — this cheap
pre-filter should sharply reduce the search space given how uniformly
the anti-persistence signature appeared here. A positive candidate must
then satisfy both $\hat{d}_{n+1}\cdot\hat{d}_n>0$ and
$\Delta\mathbf{x}_{n+1}\cdot\Delta\mathbf{x}_n>0$ for at least four,
preferably eight, autonomous periods before Y6's frozen curvature
protocol reopens.

### 10.1j The co-rotating check succeeds locally, then explains its own limit exactly (Stage Y13B)

Before committing to a new rule-space census, Y13B ran the cheap
co-rotating check directly on the 69 already-computed Y13 frontier-first
worldtubes (exact reconstruction confirmed: identical concurrent support
descriptor, identical stored step norms).

**Result: dramatic, well-controlled local coherence.** Using a frozen
frame built from ordered Gram-Schmidt orthonormalization of the causal-
role chain $(c_0,c_1,c_2,c_3,e,c_4)$ — no displacement vector enters this
definition — worldtube-weighted adjacent-step cosine rises from Y13's
raw $-0.749$ to $+0.994$, with all 69 of 69 worldtubes individually
exceeding $0.9$. The effect reduces almost entirely to one simple axis,
$a_t = \widehat{r_{c_1}-r_{c_0}}$: all 450 nonzero steps project
positively onto it (mean cosine $0.993$, 437 of 450 exceeding
$0.999999$). A proper shuffle-null control — reassigning role frames
across each worldtube's own eight boundaries, not comparing to zero —
gives $p<0.001$ over 1,000 realizations (null mean $0.043\pm0.042$
against observed $0.992$), and a second, independently-constructed frame
built from the four directed frontier-relation dipoles corroborates
independently ($0.939$ pair-weighted coherence, also $p<0.001$) — not one
arbitrary construction working by chance.

**The decisive test — whether this is a real mechanism or a near-
tautology of the frame's own construction — is run directly, and the
answer sharpens rather than undermines the finding.** The frame's own
transport (does the outgoing axis point the same way as the just-
completed step) is strongly *negative*: mean $-0.617$, with the outgoing
axis pointing backward relative to the last step in 348 of 352 cases. The
correlation between this frame-transport cosine and the raw displacement
anti-persistence is $r=0.989$ — meaning the "co-rotating coherence" and
the original anti-persistence are the same underlying fact viewed two
ways, not independent evidence for two different things. The mechanism
is exact rather than approximate: because the frontier-first role
succession advances as $c_0'\leftarrow c_1,\ c_1'\leftarrow c_2$, the
next boundary's forward axis is *algebraically* the previous $c_1\to
c_2$ edge — confirmed as an exact identity, $\cos=1$ to numerical
precision in all 310 tested cases, not merely a strong correlation — and
that edge points predominantly opposite the previous $c_0\to c_1$ edge
in this rule family. **A genuine, well-defined, doubly-corroborated
local "forward" exists at every boundary; the transport rule that
defines the next one is exactly what folds it backward.** This does not
reopen Y6 — G2 remains failed strictly.

**A practical, immediately usable byproduct.** The same-boundary causal-
chain bend, $B_t=\cos(c_0{\to}c_1,\,c_1{\to}c_2)$, predicts the *next*
raw displacement alignment with $r=0.989$ and mean absolute error
$0.007$ — exact to $10^{-9}$ in 298 of 310 cases — using only the state
at a single recurrent boundary, no 8-step embedded trajectory required.

**Consequence for Y14.** The orientation search no longer needs to
proceed blind. Screen candidates first on $B_t>0$, persistently and
preferably near $+1$, at a single boundary — rejecting folding
worldtubes immediately, before any expensive vacuum-embedding
trajectory test — while still requiring exact recurrent identity,
boundary recruitment, frontier self-renewal, and natural genesis
exactly as Y13 established them.

### 10.1k Orientation preservation is achievable — and produces a genuine rest sector, not motion (Stage Y14)

Using the Y13B causal-chain bend as an upstream prefilter (confirming
the original Y13 rule family is indeed predominantly negative-bend, and
correctly declining to promote an isolated positive exception — Rule
6843's $B\approx+0.174$ at seed 0 — after it failed replication across
5 additional independent vacua), Y14 broadened the search to the full
population of X7-style boundary-transfer operators.

**Orientation preservation turns out not to be forbidden by the
underlying grammar.** Among 489 successfully evaluated one-step exact
support-transfer events, 68 across 25 different rules showed positive
support motion *and* positive frame transport into *and* out of the
step ($R_F>0$, several exactly $R_F=1$) — direct evidence that Y13's
reversal was a property of the six rules that search happened to
sample, not a structural necessity of the boundary-transfer family
itself.

**But building these operators into full autonomous natural recurrence
produces rest, not translation.** Rule 54655's universal two-fresh-
vertex extension (frontier created at causal rank 5, requiring no
delayed or interleaved machinery) arises naturally in evolved vacua
(4, 8, 2 starts across three independent 300-event seeds) and, sampled
across 11 natural worldtubes for 8 shifts each: **11/11 exact, $R_F=1$
throughout, 0 of 88 spatially nonzero shifts.** Rule 66338 gives a
related but distinct phenotype: 15/15 exact worldtubes, 120 total
shifts, exactly 5 nonzero — every one on the *first* shift, with every
subsequent shift stationary (one finite relocation, then permanent
rest). Two structurally independent rank-4 controls (Rules 68960 and
52239, with the successor frontier created *before* rather than after
the fresh core vertex) confirm this is not an artifact of one causal-
rank construction: 9 combined natural worldtubes, 72/72 exact shifts,
0 nonzero. Rule 58846's individually strong candidate (loop 1925,
$R_F=1$, a two-relation frontier, favorable prior vacuum geometry) was
deliberately kept as a conditional reserve rather than promoted, since
its required frontier sits at causal rank 3 and rescuing it would
require complicating the grammar specifically to fit this one case.

**This defines a clean phase diagram, sharpening the actual target.**
The Y13 frontier-first family has negative frame transport and nonzero
but reversing displacement; the Y14 orientation-preserving family has
positive (often exactly $1$) frame transport and exactly zero
displacement. Neither ingredient — coherent transport, or nonzero
motion — is individually forbidden; what has not yet been found in
either family is their coexistence: $a_{n+1}\cdot a_n>0$ together with
repeated nonzero $\Delta x_n$.

**A genuinely new architectural picture.** Exact recurrence, natural
genesis, constituent turnover, autonomous frontier renewal, and stable
positive orientation transport now coexist in a single, cleanly
characterized construction — the closest this investigation has come
to the intuitive architecture of a rest particle, independent of
whether it eventually connects to $E_0$. Rest, on this evidence, looks
like a genuine dynamical sector actively maintained by ongoing
recurrence and turnover, not merely the absence of a discovered motion
channel.

**Recommended next stage (Y15 — Rest-to-Moving Bifurcation Search),
with one low-cost addition.** Search directly from Rule 54655 for a
minimal deformation or branch that preserves exact identity, natural or
scheduler-robust closure, frontier self-renewal, and positive causal
transport, while changing $\Delta x=0$ into persistent nonzero
$\Delta x$ for at least 4, preferably 8, consecutive periods — required
to be two-sided from the start (a genuine $T_+/T_-$ conjugate pair or
independently justified symmetry), not accepted as a single moving
branch alone. Before a fresh search: Y14's promotion criterion used a
strict cutoff, with the strongest examples landing at exactly $R_F=1$;
it is worth checking the *already-collected* 489-operator dataset for a
continuum of operators with $R_F$ close to but below $1$, which might
reveal a natural bridge between "perfectly preserved orientation, zero
motion" and "imperfectly preserved orientation, nonzero motion" without
a new search. Rule 66338's one-shot-then-rest phenotype should be
retained as an interaction/kick-to-rest control, not interpreted as
velocity. Only after a persistent two-sided moving family exists should
Y6's G4/G5 dynamical-cost and curvature protocol reopen.

### 10.1l The rest sector is audited and confirmed genuine (Stage Y14B)

Before searching for bifurcations, a genuine methodological loophole was
tested directly: could the concurrent-vacuum background subtraction be
silently canceling real motion of the particle against correlated
motion of its own ruler? Four progressively stronger tests addressed
this. A synthetic relocation calibration confirms the ruler detects
known relational displacement (42/42 and 64/64 nonzero, minimum signal
$0.465$) — it does not generically collapse distinct locations to zero.
Raw and background-corrected displacement agree to $\lesssim10^{-16}$,
showing the Rule 54655 zero is present *before* any correction is
applied, not manufactured by it. Independent recurrent spectators agree
completely (232/232 unchanged support-to-spectator distance vectors).
**The strongest test removes the ruler model entirely**: freezing all
599 pre-existing vacuum vertices and comparing the complete, uncentered
distance field directly gives zero change across 67,088 individual
comparisons (14 worldtubes, Rule 54655), extended to 110,216 combined
with two independent rank-4 controls — while the identical apparatus
correctly detects real motion in a Y13 oscillatory control (120/120
nonzero). The rest sector is genuine within the represented relational
geometry. What cannot be excluded, and is stated as an explicit,
honestly-scoped limitation rather than glossed over: a state variable
outside the current ternary relational model, or a universal exact
gauge translation applied to the whole vacuum at once, would be
undetectable by any relational test in principle.

### 10.1m A same-rule rest/moving bifurcation exists — and reveals the real missing object: transportable vacuum dressing (Stage Y15)

**Simple decoration of the clean rest state fails outright**: of 93
nonredundant single-relation additions to Rule 54655's event, 70
preserve recurrence but 0 produce any full-field spatial motion.

**The unmodified rule already contains a genuine same-rule bifurcation.**
At each rest boundary, an alternate legal local gate gives an exact
two-event macrocycle, $\Phi_1\to\Phi_0\to\Phi_1$, repeating for all 8
tested periods across all 14 natural worldtubes — the first clean
demonstration that one CRR rule and recurrent identity can contain both
a rest mode and a repeatedly relocating mode. A second, independently
constructed dual-frontier architecture confirms this is not a fluke of
one specific rule. But every native moving branch found this way folds
(mean frame transport $-0.524$, no four-period same-direction run) or,
in the closest near-miss (loop 1509, mean $R_F\approx0.630$), sustains
only about 2 field changes before settling permanently into rest.

**Inverting the search — screening the full Y14 census for rules
natively containing both a rest-like and a moving one-step operator —
converts this from a one-rule limitation into a decisive, general
negative.** Fourteen rules satisfy the native bifurcation signature.
Across 159 seeded trials spanning 29 evaluable native movers: **159/159
achieve exact four-period self-renewing closure; 0/159 achieve four
coherently-aligned nonzero full-field displacement steps.**

**The mechanism was then precisely localized, using Rule 76073's
cleanest case.** Ambient (naturally pre-existing) moving frontiers carry
measurably richer external vacuum embedding than stationary ones (mean
9.56 vs. 7.32 external-only relations, 177 evaluable instances, $R_F=1$
throughout). But this embedding is not something the particle's own
minimal self-renewal regenerates: of 101 validated forward-moving
events, 0 successor states contain a fully pre-embedded next frontier,
and only 4 contain even one of the four required relations. A
deliberately unrealistic "oracle" control — always selecting the
richest-embedded available candidate, an advantage no real dynamics
would have — achieves a maximum recursive handoff chain length of
exactly **1**, with 0 four-handoff chains and 0 promotions across all
five tested look-ahead signatures. The favorable motion belongs to
ambient context the particle happens to start next to, not to anything
the minimal frontier motif can sustain on its own.

**This converges with the momentum program's own earlier finding.**
The natural extended state is not $\Xi=(C,\mathcal{F})$ but
$\Xi=(C,\mathcal{F},\mathcal{D}_{\text{vac}})$ — core, frontier, and a
transportable surrounding vacuum dressing containing the relational
information spatial motion actually requires. This is the same
conceptual object the momentum program identified independently many
stages earlier: the $D_1/D_2$ predictive dressing for Rules 58846/55584
(Sections 10.2g–10.2s), shown in Stages X19 and X33 to carry real,
cross-rule-validated predictive information beyond the bare recurrent
core. Two unrelated investigative threads have now converged on the
same missing architectural ingredient from different directions.

**Recommended next stage (Y16 — Vacuum-Dressing Transport / Minimal
Extended-State Search), with one reuse suggestion.** Do not enlarge the
grammar or copy arbitrary local neighborhoods. Build matched ambient-
moving-versus-self-generated-rest datasets across several rules; measure
local dressing observables frozen *before* looking at displacement;
require predictive generalization across seeds and rules; identify the
smallest dressing state that predicts motion; only then test whether
the rewrite can covariantly regenerate or transport it; require the
full-field motion test to pass for at least 4, preferably 8, periods
before searching the conjugate $-$ sector. Before building a new
observable from scratch: test directly whether a $D_1/D_2$-style
construction — already validated as cross-rule predictive for a related
question in the momentum program — is, or can inform, the compact
dressing observable this search needs.

### 10.1n No compact transferable dressing exists — the obstruction is a property of the vacuum, not the particle (Stage Y16)

Testing directly whether a compact $\mathcal{D}_{\text{vac}}$ could be
identified for Rule 76073's strongest conditional mover (177 evaluable
ambient events: 101 forward, 68 stationary, 8 backward, all features
measured strictly before particle-frontier injection), every tested
construction failed to transfer, in an escalating and increasingly
decisive sequence.

**Simple and global dressing counts do not generalize.** The best single
local scalar (mean ambient-to-core distance) separates forward from
stationary only weakly (AUC $\approx0.627$); a sparse multi-feature model
under leave-one-vacuum-out validation reaches AUC $\approx0.492$ —
chance. Adding compact global vacuum geometry (eccentricity, shell
populations, age statistics) does not repair this (AUC $\approx0.515$).

**The central structural result is a clean, quantitative tradeoff between
predictive power and transferability.** Rooted structural refinement at
increasing depth shows within-sample accuracy climbing from $0.657$ to
$0.982$ while cross-vacuum signature coverage falls from $0.864$ to
**exactly $0$** — predictive information appears only once the
descriptor has encoded vacuum-specific local identity, at which point it
transfers to nothing. There is no useful middle ground between "too
coarse to predict" and "too specific to recur."

**Direct causal intervention rules out the two most natural fixes.**
Transplanting the moving frontier's *entire* incident external halo onto
the freshly generated successor preserves recurrence (47/47) but
*suppresses* the already-limited motion rather than restoring it (mean
nonzero shifts falls to $1.0$, 0 promotions). Searching the vacuum for
another pre-existing vertex with matching ambient dressing finds at most
one additional handoff, never two, and the richer signature finds zero
matching successors at all (0/47).

**The decisive control is a future-looking oracle, and it shows the
problem is not a search failure but an absence.** Given all 12
representative validated forward starts, an oracle allowed to simulate
every rank-compatible candidate and select whichever one *actually*
produces the best-aligned next step — using outcome information no
admissible physical rule could have — finds that 8 of 12 starts have no
positive-alignment candidate available *at all* on the second step
(mean best available cosine $\approx-0.094$). Maximum coherent chain
length across the full test is **2** (the given first step plus
nothing further); 0 of 12 reach four steps.

**This relocates the obstruction from the particle to the vacuum
itself.** The natural interpretation is not "the particle is missing one
more local variable" but "the evolved vacuum, in the tested rules, does
not possess a repeated relational translation symmetry for a persistent
worldline to ride on" — the CRR analogue of ordinary physical space's
homogeneity, which is not automatic in a purely relational substrate and
must itself be generated by the rewrite rule.

### 10.1o Exact emergent translation symmetry is proven to exist — but is not yet interface-compatible with any known particle (Stage Y17)

Y16's diagnosis motivated removing the particle-closure constraint
entirely and searching vacuum-only rule space directly for genuine
translational homogeneity.

**Vacua selected for supporting a closed particle do not have it.**
Screening all 80 inherited Stage W rules (63 survive 250 events) with a
deliberately coarse local-equivalence audit across 54 spatially extended
snapshots finds a maximum exact geodesically composable corridor length
of **3**, and zero corridors of length 5 — independently confirming
Y16's diagnosis by a completely different method.

**A broader, unconstrained search finds real, exact translational
homogeneity.** Sampling 1,600 eight-output templates without requiring
particle closure (225 survive 150 events) isolates six independent
templates forming a sharply different phase: one active rewrite front,
bounded degree, low and decreasing degree variation, large diameter, and
a dominant exact rooted bulk environment — finite-width one-dimensional
relational crystals. All six remain live through 1,200 events with
diameter scaling linearly in $N$ (fitted exponents $0.997$–$1.014$), and
the dominant depth-3 rooted environment covering 97.8–98.3% of all
vertices at that scale.

**The translation symmetry is exact, not statistical — verified directly
against raw shift-matching data, not summarized.** For every relation
$T(a;\{b,c\})$ in the deep bulk, shifting all three birth-index labels
by a fixed $\delta$ maps to another existing relation with fraction
**exactly $1.0$**, confirmed for all six crystal rules at shifts
$\delta=1,2,3$, and for the representative candidate (template 157)
exhaustively at every shift $\delta=1$ through $12$, at five different
vacuum sizes from 305 to 2,405 vertices — every single one of dozens of
tested combinations gives fraction $1.0$ with zero exceptions. This is a
genuine, proven graph automorphism: **CRR's local rewriting is capable
of generating exact emergent translation symmetry**, the first rigorous
demonstration of this foundational property anywhere in the
investigation, on par with the framework's other exact structural
theorems (Sections 5, 10.2d).

**A sharp, informative tension was found between concurrency and exact
homogeneity.** Every nearby rule variant that retains perfect bulk shift
symmetry collapses to the same single-active-gate crystalline growth
front architecture; variants admitting many simultaneous legal gates
lose exact shift symmetry and become compact and heterogeneous instead.
Two independently sampled multi-front controls confirm this: large
diameter, but essentially unique local environments by 1,200 events, and
only 26–30% best-fixed-shift relation matching. This is a real,
if not yet theorem-level, empirical trade-off worth further
investigation in its own right.

**But exact vacuum symmetry does not automatically translate the
particle.** The crystal rules do support genuine boundary-transfer
recurrence (candidate 157 has 2 exact self-loops; others up to 7), and a
carrier prepared in the mature bulk interior can make one genuine,
large, exact relocation through already-existing homogeneous space. But
searching the pre-existing crystal for the next ambient vertex
satisfying the same frontier interface finds **zero** natural second
handoffs, across every tested compatible rule (0/8 for candidate 157,
0/18 for 1035, 0/6 for 214) — maximum natural carrier chain length is 1,
identical in shape to Y16's finding, now shown to persist even in a
vacuum with *proven* exact translation symmetry. The vacuum's own
translation map does not map the required carrier frontier motif into
the next required carrier frontier; the interface itself is not
covariant under the symmetry that carries everything else.

**This cleanly separates two previously entangled requirements, and both
are now independently confirmed.** Emergent relational space with a
composable translation map: **yes**, proven. A recurrent boundary-
transfer carrier automatically propagating on that translation orbit:
**no**. The target is now precisely: a transport-symmetric vacuum *and*
a translation-covariant recurrent interface, co-designed together rather
than found separately. The tested crystals are explicitly a narrow,
one-dimensional proof of principle, not a candidate for physically
realistic 3D space.

**Recommended next stage (Y18 — Interface-Compatible Homogeneous Vacuum
/ Carrier Co-Design).** Do not select vacuum and carrier separately.
Promote a rule only if it simultaneously supplies a live bounded-degree
vacuum with a transport generator composing over at least 8 locations
under ordinary rewriting, a closed full-turnover recurrent state with a
boundary-transfer self-loop, and — the genuinely new requirement — a
frontier motif that itself recurs at successive translated vacuum
locations, with at least 4, preferably 8, natural carrier handoffs
requiring no repair. A secondary target: a vacuum with two or more
independent transport generators, moving beyond the one-dimensional
proof of principle toward something that could eventually support
genuine multi-dimensional geometry. Only after an independent interior
carrier shows persistent $+$ and $-$ velocity should Y6 reopen.

### 10.1p A persistent, genuinely translating carrier is achieved for the first time in the entire investigation (Stage Y18)

Y17's crystal family left a genuine joint-design problem: none of its 14
boundary-transfer loops has its complete required frontier naturally
repeated on the translation orbit, confirmed in the exact-symmetry
one-relation neighborhood of candidate 157 as well (52 variants preserve
the crystal; 0 of 52 has any native frontier chain).

**The mismatch has an exact algebraic cause, not merely an empirical
one.** For the representative rank-5 loop, one required frontier
relation is a function only of the ordinary output roles $y,z,u,v,w$ and
is directly generatable; the other is sourced at the *retired* role $x$,
and the standard five-role output grammar cannot deposit a relation
sourced at $x$ into a repeating bulk motif. Naive additive repair — just
appending the two missing relations — destroys the crystal outright
(shift fraction collapses to exactly $0$ by 1,200 events). **Fixed-budget
co-design** — replacing two of the eight existing periodic outputs
rather than adding to them — succeeds: 4 of 28 guided variants preserve
exact crystalline shift symmetry through 600 events.

**The strongest variant (designated 0-3) achieves, for the first time in
this investigation, all of the following simultaneously.** An
independent recurrent carrier defect, distinct from the vacuum growth
front, whose interface is supplied *naturally* by the crystal (no
injected frontier relation required, unlike every previous stage in this
arc); 8 of 8 consecutive natural boundary transfers at each of three
separated insertion sites; an exact six-microstep internal recurrence
cycle ($\Phi_{n+6}=\Phi_n$); and, measured correctly between equal
internal-phase boundaries rather than individual microevents, **20
consecutive nonzero macro-translations at four widely separated
insertion sites, 80 of 80 combined, with every adjacent macro-step
cosine positive** (minimum $0.781$, worldtube means $0.797$–$0.948$) —
independently confirmed against the raw trajectory data with zero
zero-norm displacements and zero negative adjacent cosines across all 80
tested steps. This is the first long-run CRR trajectory satisfying the
Y6/Y-series four-consecutive-same-direction promotion criterion.

**Why G2 is still not promoted.** The translating mode is not an
attractor of the actual asynchronous scheduler. One of the six carrier
phases admits three structurally distinct legal boundary gates; the
translating channel consistently selects the one recruiting the ambient
vertex *ahead* along the crystal's own translation direction, while the
two competitors recruit the vertex *behind* — a directionally meaningful
distinction, not arbitrary label order, but one the current universal
rule does not yet enforce. Under genuinely uniform random choice among
legal gates, 0 of 60 trials survive even 36 microtransfers (mean
survival $2.9$ transfers), and a naive consistently-backward policy does
not produce a mirror $-v$ mode — it terminates after one transfer. The
correct statement is precise: **a persistent translating carrier
trajectory exists; the current rule does not yet autonomously select
it.**

**Recommended next stage (Y19 — Intrinsic Direction Selector).** Do not
search a new vacuum. Find the smallest covariant state or local rule
that uniquely stabilizes the translating branch against random
scheduling while preserving the homogeneous crystal and the 20-period
macro-translation, then search for a conjugate encoding producing a
persistent $-v$ sector before any curvature or mass test reopens.

### 10.1q A translation-covariant selector makes $+v$ fully robust — the orientation itself is not yet a carrier property (Stage Y19)

**Three simpler hypotheses for the missing selector were tested and
systematically eliminated before the real one was found.** A bare
forward/backward causal-rank bit is insufficient ($0$ of $120$ random
trials survive long-run translation). No hidden fifth relation already
distinguishes the successful gate from its competitors — only the four
ordinary gate-defining relations are shared by all of them. Ordinary
carrier phase alone is insufficient **by exactly one bit**: the settled
six-microstep cycle contains only five distinct normalized phases, with
one phase visited twice requiring two different continuations — the
sharpest possible quantification of the missing information.

**The successful selector is translation-covariant and geometrically
precise.** Using $T$, the exact crystal automorphism proven in Y17/Y18,
define an orbit coordinate relative to the carrier's own support center;
admit carrier-sourced gates with positive signed displacement along a
chosen orientation $\sigma$, and choose the smallest such displacement —
"move to the nearest available site ahead, in your own direction of
travel," stated without reference to any absolute coordinate. Under
$\sigma=+1$: **40 of 40 random-tie trials survive all 121
microtransfers**, all reaching 20 exact period-6 macroperiods; the full
frozen-vacuum distance-field test confirms 80 of 80 nonzero displacements
with minimum adjacent cosine $0.809$; the result is robust across vacuum
ages 300 through 1,200 events (60/60 further trials).

**What remains genuinely missing, stated as precisely as the report
itself states it.** Nineteen candidate static relational markers were
tested as possible internal encodings of $\sigma$; none survives the
full translating cycle (the best holds on only 34 of 41 checked
boundaries). $\sigma$ is therefore not yet a self-renewing property of
the carrier's own relational state — it is supplied externally by the
construction. And this is not merely an unfinished search for a mirror
state: testing $\sigma=-1$ directly on the same crystal gives **0 of 40
surviving beyond the first transfer** — variant 0-3 is not
parity-symmetric, so a working conjugate sector is not guaranteed to
exist for this specific construction without its own discovery.

**Three statements, cleanly separated.** A persistent translating
trajectory exists (Y18). A compact, covariant selection principle
stabilizes it against real scheduler competition (Y19). The selector's
orientation is itself a self-renewing relational carrier state, with a
working conjugate — not yet established. This is the closest this
investigation has come to a genuine notion of momentum,
$p\sim(\text{translating mode},\sigma)$, with $\sigma$ still an external
rather than intrinsic parameter.

**Recommended next stage (Y20 — Relational Orientation Encoding /
Conjugate Momentum Sector).** Keep variant 0-3 frozen; do not search a
new vacuum or carrier. Encode $\sigma$ as a local, translation-covariant
relational or chiral marker that survives full carrier turnover, leaves
the vacuum unchanged when absent, and uniquely enforces the nearest-
interface rule under random scheduling, then search for its conjugate
$-\sigma$ producing a genuine $-v$ trajectory rather than immediate
termination. One concrete lane worth trying first, since it reuses a
solution already proven in this substrate rather than inventing a new
mechanism: given the deficit is precisely one bit within an otherwise-
exact six-phase cycle, test whether doubling the cycle — splitting the
ambiguous phase by which of two extended orbits the carrier currently
occupies — can encode $\sigma$ the same way Rule 55744's exact
instantaneous tether phase (Section 10.2i) was shown to be directly
readable from current relational structure. Only after both orientation
sectors are autonomous should Y6's G3–G5 curvature and mass-comparison
protocol reopen.

### 10.1r The orientation sign becomes a genuine self-renewing relational state for $+v$ (Stage Y20)

The promoted marker, $M_+ = T(c_0;\{c_4,h\})$, is regenerated rather
than preserved: each marked event consumes the old marker, the ordinary
carrier rewrite proceeds unchanged, and a *fresh* marker vertex $h'$
recreates the identical normalized motif, $M_+' = T(u;\{w,h'\})$, with
$u=c_0'$ and $w=c_4'$ along the translating channel. Marker vertex
identity changes every event; the relational pattern persists exactly —
the same structural signature as a real conserved quantity carried by a
state rather than by any specific constituent, echoing Y15's earlier
constituent-turnover finding for identity itself.

**Verified directly against raw trial data**: 40 of 40 long marked
trajectories survive 121 microtransfers with the marker invariant
confirmed true in every case; 0 of 40 survive for the naive negative
attempt. The full-field test confirms 80 of 80 nonzero macrodisplacements
(minimum adjacent cosine $0.809$), robust across vacuum ages 300–1,200
(60/60) and under interleaved ordinary vacuum activity (30/30), with all
30 audited retired marker vertices confirmed relationless.

**The conjugate marker is mathematically well-defined but the backward
transport interface is not.** $M_- = T(c_4;\{c_0,h\})$ has a properly
conjugate update rule — the sign-storage mechanism itself is not the
obstruction. But 0 of 40 long negative trajectories survive; a
depth-15 branch census finds 135 negative phase-return cycles, of which
11 can repeat their role/rank program once, but none remains negative on
a second return. The failure is narrower than before: not "how to
encode direction" (solved), but specifically that the backward-going
frontier does not yet self-sustain in this particular crystal.

**Recommended next stage (Y21 — Parity-Conjugate Interface Co-Design).**
Freeze the successful $M_+$ sector exactly. Identify the specific
missing frontier relation immediately after the first $M_-$ transfer and
search for the smallest parity-paired addition that supplies it without
altering the unmarked crystal or the frozen $+v$ channel. Require at
least 20 negative recurrence periods, matching the positive sector's
demonstrated length, before any mass test reopens.

### 10.1s Genuine bidirectional signed velocity — the first time in this investigation — with two precisely located remaining asymmetries (Stage Y21)

**The missing backward frontier relation was found by direct, exhaustive
search, not guessed.** At every separated insertion site, the successor
after the first $M_-$ transfer is exactly one relation short of a
backward continuation, always requiring the same next ambient site
$T^{-1}(e)$. Testing all 30 directed ternary relations available among
the successor carrier roles and $T^{-1}(e)$ finds a unique clean winner,

$$
Q_- = T(c_0';\{c_4',\, T^{-1}(e)\}),
$$

written only on an $M_-$-marked event, leaving the unmarked vacuum and
the frozen $M_+$ channel untouched.

**The backward sector is robust, independently verified**: 40 of 40
stochastic-tie trials survive 121 marked transfers (carrier center shift
$\approx-123$ crystal sites); 60 of 60 survive across all four tested
vacuum ages; 20 of 20 survive interleaved ordinary vacuum rewrites; only
the newest $Q_-$ relation remains live at any time, with prior instances
properly consumed. Because single-event displacement alternates at
lattice scale, coherence was measured at the minimal block size that is
directionally consistent at all four sites — 4 events — confirmed
directly against raw trajectory data: **exactly $-4.0$ crystal-orbit
sites per block at every one of the four insertion sites**, mean
adjacent full-field cosine $0.742$, minimum $0.703$.

**Signed velocity now genuinely exists, with two real, precisely
measured asymmetries.** Over a common 12-event external clock, the
positive sector moves $\approx+8$ orbit sites and the negative sector
$\approx-12$ — oppositely directed (mean $\pm$ full-field cosine
$-0.584$) but **not equal in magnitude**, a clean $1.5\times$ ratio,
not measurement noise. And the construction is **chiral, not mirror-
symmetric**: the most direct symmetrization attempt — using the same
$c_0$-sourced relation form for both signs — destroys the $+$ cycle
outright; the best candidate for a true parity image ($Q_+ =
T(c_4';\{c_0',\,T(e)\})$) survives a short preliminary screen but
visibly accumulates and perturbs the original $+$ recurrence over long
runs. The working rule is honestly reported as chiral: $M_+$ uses the
original Y20 interface alone, $M_-$ requires the additional transient
$Q_-$ relation with no forward counterpart.

**Y6 gate consequence, stated precisely.** G1 passes within the marked
carrier family. **G2 — independent signed velocity — passes for the
first time in this investigation's history**: both signs produce
persistent, autonomous, oppositely-directed relational translation
through the same homogeneous vacuum. G3 (rest plus a symmetric $\pm v_1$
pair, plus a second speed $\pm v_2$) still fails — no equal-magnitude
pair, no same-architecture rest branch, no second speed. G4/G5 and any
comparison to the frozen Y5 rest-content scalar remain explicitly
closed.

**Recommended next stage (Y22 — Symmetric Velocity Manifold / Rest-
Sector Integration), with one diagnostic addition.** Keep both Y21 sign
sectors frozen as existence proofs; do not yet attempt curvature or mass
comparison. Priority order: (1) a parity-clean, equal-speed $\pm v_1$
pair, ideally from a single conjugate interface law rather than two
different programs; (2) a same-carrier rest branch integrated into the
identical crystal/marker architecture, not merely Y14's separately-
discovered rest sector; (3) a second conjugate speed $\pm v_2$; (4) only
then an independent dynamical cost and Y6 curvature. Before a fresh
search for (1): the $1.5\times$ speed ratio is a precise, measured
number, not a vague asymmetry — worth checking directly whether it
matches a simple combinatorial count (relations written per transfer,
or an analogous quantity) in the $M_+$ program versus the $(M_-,Q_-)$
program, the same way Y18's exact algebraic diagnosis of the retired-
role obstruction pointed directly at its own fix.

### 10.1t A genuine equal-speed $\pm v_1$ pair — rest and a second speed each fail, in three and two distinct informative ways (Stage Y22)

**A single sign-covariant interface law resolves the Y21 speed
asymmetry directly, rather than explaining it.** $Q_\sigma =
T(c_2';\{c_4',\,T^\sigma(e)\})$, with $\sigma=\pm1$ supplied by the
Y20 self-renewing marker, settles after a finite formation transient
into period-1 lanes with exact crystal-orbit motion $\Delta j_T=+1$ and
$\Delta j_T=-1$ per event — a true equal-magnitude pair from one
functional form, not two separately-tuned programs. The settled $+$ and
$-$ five-role core phases are confirmed exactly isomorphic under a
simple $c_0\leftrightarrow c_1$ swap, so this is one structural carrier
family, not two unrelated defects. Verified directly against the raw
full-field data: $\Delta j_T$ is exactly $\pm1$ every event with zero
variance, and — the detail that distinguishes this from the earlier
rejected stride-2 attempts — the live interface relation count stays
fixed (3 for $+$, 1 for $-$) rather than growing with trajectory length.

**The single-event ruler shows crystal-cell microstructure that a naive
reading could mistake for weak coherence; scanning block size rather
than assuming one resolves this cleanly.** Adjacent full-field cosine at
one-event resolution is not meaningful (crystal unit-cell oscillation);
scanning block sizes directly (not chosen by hand) finds the minimal
block passing nonzero same-direction composition for both signs at both
tested locations is exactly 3 events (minimum cosine $0.074$), rising to
$0.61$ at block 4 and $0.99$ at block 5 — the exact translation generator
was correct at one-site resolution throughout; the ruler simply carries
short-scale structure the block scan properly accounts for.

**Rest fails in three genuinely different, informative ways, not one
generic negative.** The existing branch graph contains 41 zero-
displacement phase-return cycles; 7 repeat their gate-role pattern once,
but every one then drifts by $+1$ or $+2$ on the next repetition — no
persistent zero-displacement cycle exists. A direct alternating
$+,-,+,-$ program using the common interface terminates after exactly
one transfer at all four tested sites (confirmed in raw data: 1
microstep survived, 0 in every trial) — plausibly because the settled
$+$ and $-$ lanes carry different live-relation counts (3 vs. 1), making
an abrupt sign flip structurally illegal rather than merely
undiscovered. The original internal producer gate runs but changes the
full frozen-vacuum field strongly on every event and never settles into
one normalized carrier phase — not a rest state by the standard applied
throughout this arc.

**A second speed fails differently: not cleanly rejected, but not yet
found either.** Generalizing $Q_\sigma$ to stride $s=2,3$ and screening
all 30 one-relation signed forms, the negative side can realize clean
$-2$ and $-3$ orbit advances in some cases, but the positive side
consistently either develops non-linear microcycles (e.g., a repeating
$+1,+2,-1$ pattern) or accumulates an unconsumed interface relation per
event — a specific failure mode, not an exhausted search, since every
tested stride reused the same source point ($c_2'$) that happened to
work for $v_1$.

**Y6 gate consequence.** G1 and G2 remain passed. **G3a — equal-speed
$\pm v_1$ pair — now passes**, the first clean parity-symmetric velocity
result in the investigation. G3b (same-identity rest) and G3c (second
symmetric speed) both fail. The full target velocity manifold,
$v=0,\ \pm v_1,\ \pm v_2$, remains incomplete; G4/G5 and any comparison
to the frozen Y5 rest-content scalar remain closed.

**Recommended next stage (Y23 — Rest-State and Second-Speed
Completion), with two concrete suggestions.** Freeze the common
$Q_\sigma$ $\pm v_1$ pair exactly; do not modify it further. For rest:
rather than retrying an immediate sign alternation, which fails
structurally given the two lanes' different bounded-relation counts, try
a longer, symmetric *round trip* — $N$ events of $+$ followed by $N$
events of $-$, returning to the starting position over one full period —
a physically reasonable "zero net velocity" as a bound oscillation
rather than a literally motionless state, and a gentler transition since
each half stays inside an already-proven-stable regime. For the second
speed: screen all five carrier roles as candidate source points at both
strides, not only variations of stride on the single point ($c_2'$) that
happened to work for $v_1$ — the same exhaustive discipline that found
$Q_\sigma$ itself, one level up. Only once $0,\pm v_1,\pm v_2$ coexist
in one common kinematic-state encoding should Y6's action/cost and
inertial-curvature measurement reopen.

### 10.1u The full kinematic manifold is complete: $v=0,\ \pm v_1,\ \pm v_2$, one carrier identity — G3 passes (Stage Y23)

This is the completion of the kinematic target set by Stage Y6, roughly
thirty stages earlier in the momentum program's numbering. Both proposed
strategies (Section 10.1t) were confirmed as correctly diagnostic, but
each needed a further, distinct insight beyond the diagnosis itself to
actually succeed.

**Rest is a genuine bounded shuttle, not pointwise immobility, and the
clean version required more than closing the position.** An immediate
marker flip fails to launch the opposite lane for every tested leg
length $N=1$–$20$, confirming Y22's alternation failure was a genuine
interface mismatch, not an unexplored parameter. A one-relation handoff
search (in the same style as Stage Y21's interface repair) finds a
common law, $Q=T(c_2;\{f,c_4\})$ with $f=T^{-2\sigma}(e)$ at the
reversal, that launches the opposite lane cleanly for every tested leg
length $N=1$–$12$. The first working round trip closes the full-field
position exactly for $N=2$–$12$ — but leaves two stale interface
relations per cycle, invisible to the position ruler but genuine
leftover relational content, and is correctly rejected as not physical
rest on that basis alone. The clean version explicitly consumes the
outgoing lane's live interface state at each turnaround before writing
the incoming one; after this fix, every tested $N=2$–$12$ completes 8
round trips with **exactly one** live interface relation throughout, no
wake.

**The smallest clean shuttle ($N=2$) was made fully autonomous with a
four-state internal marker program** ($+A,+B,-A,-B$), each phase
creating a fresh marker constituent so identity continues to undergo
complete turnover. Verified directly against raw aggregate data: 4
locations $\times$ 50 four-event cycles — **200 of 200** complete with
full-field displacement exactly zero, zero distance-field entries
changed, core phase and marker state identical at every boundary, one
live interface relation, zero marker debris throughout. A further 20
randomized-tie trials (4 locations $\times$ 5 each) all complete 20
autonomous rest periods (mean cycles $20.0$ exactly, one interface
relation, zero debris). Rest is classified precisely as a **zero-drift
recurrent sector**: the carrier executes two forward and two backward
transfers, with exactly zero net relational displacement at its proper
four-event recurrence boundary — an honest, structurally motivated
notion of "at rest," not an approximation.

**The second speed required a change in interface update semantics, not
a different relation.** Expanding the search anchor from the single
ambient point used for $v_1$ to $e$, all five successor carrier roles,
and all five pre-event carrier roles, at strides 2–4 with all 30
relation placements and both signs, finds no direct bounded symmetric
pair in that enlarged space — but cleanly isolates the surviving near-
miss. The negative stride-2 candidate already gives clean $-2$
propagation with the ordinary additive update; the positive side enters
a short transient and can accumulate interface relations because the
old interface relation remains present after it has already served to
enable the event. The fix consumes any surviving old interface relation
immediately after it fires, before writing the next stride-2 relation —
after this, both signs settle to exact $\Delta j_T=+2$ and $-2$ per
event, one normalized carrier phase, one live interface relation.
**$|v_2|=2|v_1|$ exactly**, in the crystal transport coordinate.

**Both directions of $v_2$ were independently confirmed at full-field
resolution and under real scheduling.** Eight settled worldtubes (4 per
sign, 80 post-settling events each) all show exactly $\pm2$ orbit
increments, one carrier phase, one live interface relation; a blind
block scan (not chosen by hand) finds the smallest block passing
same-direction composition at all eight worldtubes is 2 events (worst
adjacent cosine $0.271$), improving sharply to $0.885$ at block 3 —
independently verified against raw block-scan data. Cloning each
settled sign into 20 random-tie continuations across 4 locations (160
trials total) gives **160 of 160** surviving all 61 tested events with
exact $\pm2$ orbit increment, one carrier phase, one live interface
relation throughout — confirmed directly in the raw aggregate.

**The decisive unifying check: all five kinematic states are one
recurrent carrier identity, not five coincidentally similar
constructions.** Pairwise graph-isomorphism testing among the five
settled eight-relation five-role cores ($v=0$, $+v_1$, $-v_1$, $+v_2$,
$-v_2$) gives **25 of 25** passing, verified directly against the raw
isomorphism table, with specific, meaningful role permutations rather
than arbitrary relabelings ($c_0\leftrightarrow c_1$ for the sign
changes at $v_1$ and rest; identity for $+v_2$; a three-role
permutation among $c_0,c_1,c_2$ for $-v_2$). The same table includes the
original, unmarked candidate-157 core as a control, and it is correctly
found non-isomorphic to every one of the five kinematic states — the
positive result is not vacuous.

**Y6 gate consequence.** G1, G2, and now **G3 all pass**: the augmented
marked carrier supports $v=0,\ \pm v_1,\ \pm v_2$, confirmed as one
identity throughout. G4 (independent dynamical cost) and G5 (near-rest
curvature) are explicitly marked *ready, not yet measured* — Y23
deliberately declines to inspect or fit a cost observable at this stage,
stating plainly that choosing a cost definition after seeing the
velocities would risk selecting one that manufactures the desired
curvature. This is the same discipline that caught Stage T's PRO
criterion and Stage Y3's premature $E_0$ signal, now self-applied at the
highest-stakes point this investigation has reached.

**Recommended next stage (Y24 — Independent Inertial Cost / Near-Rest
Curvature).** Freeze the Y23 manifold exactly. In strict order: (1)
define an event/action/cost observable from rewrite dynamics alone, not
from measured spatial displacement; (2) evaluate it, unchanged, on all
five frozen sectors; (3) test sign symmetry, $E(+v_i)\stackrel{?}{=}
E(-v_i)$; (4) test whether the near-rest dependence is even and admits
stable positive curvature; (5) only then define an inertial coefficient
$M_i$; (6) only after that, compare with the frozen Y5 $E_0$ candidate.
The rest sector's cost must be averaged over its complete four-event
proper recurrence, not sampled at an arbitrary one of its four internal
phases, given rest is now known to be a shuttle rather than a single
unchanging state.

### 10.1v The first inertial-curvature test: an exact, clean null for raw edit cost (Stage Y24)

**The predeclared-before-inspection discipline held completely,
including under a real mid-execution complication.** The cost protocol
was written and hashed before any five-sector value was inspected. The
frozen primary observable, the hypergraph edit action
$a_t=|\mathcal{R}_{t+1}\triangle\mathcal{R}_t|$ (relation births plus
deaths across one autonomous update), uses no spatial displacement,
velocity sign or magnitude, and no Y5 quantity. When one initially-
eligible site's $+v_2$ trajectory was found to reach the finite
crystal's boundary partway through the measurement window, it was
excluded on a purely geometric eligibility criterion, explicitly *before*
any cost value from that site was consulted — exactly the scenario the
firewall was built to resist. Two sites (300, 320) survive the full
common-manifold requirement; 16,000 total events were measured (2 sites
$\times$ 20 trials $\times$ 5 sectors $\times$ 80 events).

**The result is an exact structural null, not a weak or noisy one.**
Verified directly against all 16,000 individual event records: every
single measured event, in every one of the five sectors, has cost
exactly $14$ — zero exceptions. $A_{\text{dyn}}(0) = A_{\text{dyn}}(\pm
v_1) = A_{\text{dyn}}(\pm v_2) = 14$ exactly. Sign symmetry is exact
($A_{\text{odd}}(v_1)=A_{\text{odd}}(v_2)=0$), and the predeclared
quadratic-plus-quartic fit gives $M_i=0$, $\beta_4=0$, with a
cluster-bootstrap 95% interval of exactly $[0,0]$ and $P(M_i>0)=0$ — not
a failure of statistical power, a genuine structural fact.

**The mechanism is understood precisely, and it is a predictable
consequence of a design choice made in Stage Y18.** A direct edit-level
audit confirms every event, in every sector, performs exactly 4
relation deaths and 10 births, regardless of which sector or which
direction. Because exact crystalline homogeneity was only achievable by
*replacing* two of the eight existing outputs rather than adding to
them (Section 10.1p), the grammar's edit cardinality is structurally
fixed by construction — different transport speeds attach relations to
different locations, but never a different *number* of them. Raw edit
counting was, in retrospect, close to guaranteed to be blind to speed
in an architecture built this way.

**The interpretation is stated precisely, avoiding overclaim in either
direction.** G4 (independent dynamical cost) passes — a genuine,
noncircular, rewrite-dynamical observable was defined and measured. G5
(positive finite curvature) fails for this specific observable. This is
*not* rephrased as "the carrier is massless" — the justified statement
is narrower: the predeclared edit-action observable has zero inertial
curvature. A physical inertial cost, if one exists here, must depend on
something raw edit cardinality does not capture.

**This connects to a lesson this same investigation already learned,
independently, much earlier.** Stages X28–X29 (Section 10.2s) found
that raw capacity or existence counts did not carry this substrate's
real directional signal — what mattered was scheduler *measure*, how
often a path is actually realized under live dynamics, not merely
whether it exists. Y24's own proposed next direction — a transition-
statistical or accessibility cost, rather than raw edit count — is the
same *kind* of quantity that already carried real signal once before,
in a different part of this program. That is evidence for where to look
next, not a guess.

**Recommended next stage (Y25 — Transition-Statistical / Accessibility
Cost), with the Y24 null kept intact.** Begin with a fresh, independently
predeclared observable — candidates include the local legal-transition
count or branching factor at each event, a scheduler-realized selection
probability, or an accessibility-weighted transition measure, explicitly
modeled on the kind of quantity that carried real signal in Stages
X28–X29 — frozen and hashed before any five-sector value is inspected,
exactly as Y24's own firewall was applied. The Y24 null result for raw
edit cost must not be revised, replaced, or reinterpreted; a new
observable is a new, separately-registered test, not a retry of the old
one.

### 10.1w Two parallel branches: local surprisal is structurally trivial; the triangle shows exact massless history-dispersion (Stage Y25)

**Y25-A tested the scheduler-surprisal cost Y24's own report pointed
toward, and found something more fundamental than another null.** The
local legal carrier-touching gate ensemble is a **singleton** — exactly
1 legal gate, exactly 1 sector-compatible gate — at every one of 16,000
measured events, with zero exceptions, confirmed directly against the
raw per-event record. $P_t=1$ everywhere, so $A_{\text{acc}}=0$
identically; $M_i=0$ again. This is a direct, close-to-inevitable
consequence of the Y19–Y23 marker engineering itself: those stages
achieved scheduler-robust autonomy specifically by *removing* local
ambiguity, so a cost built from local branching entropy was close to
guaranteed to find nothing to measure. A secondary *global* scheduler
measure (competing against the full vacuum-wide gate pool, not just
local carrier-touching options) shows real, nonzero, sector-dependent
variation and would give a descriptive positive $M_i\approx0.87$ under
the same fit — correctly **not promoted**, since it was predeclared as
confounded by finite-system ambient gate volume before any sector value
was inspected.

**Y25-B, run in parallel, is a genuine, carefully-scoped positive
result.** Treating the massless triangle's own period-1 recurrent
handoff as a discrete history-translation operator, $T|n\rangle=
|n+1\rangle$, its measured evolution is exactly $F=T$ on a 257-cell
periodic quotient ($\|F-T\|=0$, $\|[F,T]\|=0$), and the resulting
quasienergy is exactly linear in the translation character:
$E(k)=|k|$, verified directly against all 257 raw dispersion-mode
records with zero residual, $R^2=1.0$. This is a real, exact massless
dispersion relation — but explicitly in **configuration-history space**,
not ordinary spatial momentum; the Stage X19 fixed-anchor null (zero
longitudinal displacement) is deliberately retained rather than
superseded. The result is best read as an empirical confirmation, on
this specific carrier, of the pure-screw massless architecture the
older R14-branch E17 analysis anticipated theoretically (Section
10.1g).

**Consequence.** Local surprisal is now known to be structurally
incapable of carrying inertial signal for this marked architecture; any
further cost search must look at global or background-normalized
scheduler competition, not local branching. The massless program's next
real gate is an independent mapping from history character to a
relational spatial-momentum observable that survives the X19 objection
— not another history-space dispersion fit.

### 10.1x Background-normalized cost still fails, but exposes a real defect the earlier checks never tested (Stage Y26)

Following Y25's own recommendation, Y26 froze a background-normalized
scheduler measure conditioned on directly touching the current
five-node recurrent core (not the auxiliary marker vertex), removing
vacuum-disjoint gates from the denominator so finite-crystal volume
cannot manufacture a signal.

**The four moving sectors are exactly degenerate** ($A_{\text{dir}}=
\ln 7$ for all of $\pm v_1,\pm v_2$ — every moving event has exactly 7
legal gates touching the core and exactly 1 sector-compatible
continuation) **while the rest sector is not stationary at all.** Its
direct-contact gate count begins at 13–16 and then grows by an exact
linear law, $+7$ legal gates per proper four-event rest cycle
(residuals below $2.3\times10^{-13}$ — floating-point roundoff, not
approximate). A relation-level audit localizes this precisely: per
cycle, carrier-touching relations grow by $+11$, distinct external
incident vertices by $+4$, while fully internal three-core relations
stay fixed at 8. **The recurrent core, frozen-vacuum distance field,
marker state, and interface count all return exactly — invariants Y23
checked — while the surrounding contact grammar accumulates without
bound — something none of those checks constrained.** Because the halo
grows, the measured rest cost depends on the arbitrary measurement
horizon (2.62 at 4 events, rising to 5.63 at 400) — there is no
stationary $A_{\text{dir}}(0)$ to compare against a well-defined
moving-sector value at all, so the resulting formally-negative $M_i$ is
explicitly not interpreted as negative physical mass. **Y23's rest
state is recurrent in core, position, and interface — but not in its
full local contact environment.** G3 is downgraded to a new subgate,
G3S (full local stationarity), which fails.

### 10.1y Repair attempts separate two distinct defects, then prove a clean impossibility theorem (Stages Y27–Y28)

**Y27** searched all 28 pre-existing Stage Y18 fixed-budget architecture
variants for a genuinely stationary rest state, with the Y26 cost
explicitly excluded from candidate selection. Result: **0 of 28** pass
full stationarity, but variant 1-3 is a highly informative near-miss —
its direct scheduler-contact grammar closes exactly (a repeating
$2,4,2,2$ gate pattern, horizon-independent, reproduced at 5 separated
sites), while the underlying relational halo still grows at the same
$+11/+4/+1$ rate as the original. This cleanly separates two previously
conflated defects: **scheduler-visible contact proliferation** (fixed by
one specific relation swap) and **relational-history accumulation**
(unaffected by it) — the Y26 signal was not simply the unavoidable
residue of any zero-drift shuttle revisiting its own wake.

**Y28** then determined whether that remaining wake is structurally
forced. Across 100 formally audited site-cycles, the same canonical
**11-relation wake motif** is deposited exactly, with the same two
carrier roles persisting across every proper boundary. A proven
**persistent-anchor wake lemma** explains why: once a deposited relation
contains a retired fresh vertex outside the current five-role support,
it can never again appear in any future selected rest gate, because
deletion is confined to a gate's own matched vertices — so it is
absorbing under the frozen rest law for as long as its attached anchor
remains a carrier constituent. The one native gate that *can* consume a
wake relation does so only by simultaneously destroying three relations
internal to the settled core, landing in a different, non-isomorphic
ten-relation recurrent class — a transmutation channel, not a cleanup
one (0 of 505 further steps ever recover the original carrier). Testing
whether a larger shuttle amplitude helps: **no** — the same two anchors
and the same exact $+11$/cycle wake persist for every tested round-trip
length $N=2$ through $12$. This is stated precisely as a no-go for the
*frozen persistent-anchor rest family specifically*, not a theorem
against every conceivable CRR rest construction.

### 10.1z A proven no-go theorem for full-turnover rest, reached only after catching a real flaw in the measurement tool itself (Stages Y29–Y30)

**Y29** tested the obvious remaining escape — full constituent turnover,
eliminating persistent anchors entirely. Balanced sign-word searches
across the established $v_1$ and $v_2$ laws (up to 21,315 candidate
words) find full turnover reachable only as a **one-time formation
transient**; every one of 132 settled, fully-validated post-formation
recurrent states reconstructs exactly two persistent anchors on every
subsequent period. The anchor pair behaves as an attractor of the
zero-drift dynamics, not a fragile artifact of one specific construction.

**Y30 then caught a genuine methodological flaw in the position tool
used throughout the entire Y-series, before it could distort this
conclusion further.** The frozen-vacuum distance-field ruler seeds
breadth-first search from every current support vertex, so it returns
exactly zero distance for any reference vertex that happens to be part
of the support — meaning "exact position return" secretly entails
"support membership return" whenever a frozen reference vertex belongs
to the baseline carrier. This does not invalidate the ruler's use for
the moving-sector displacement work (Sections 10.1p–10.1u), but it made
it unsuitable, undetected, for independently testing turnover
specifically. A validated, identity-independent replacement,
$X_T=(a+b)/2$ (the midpoint of the carrier's two old-crystal support
sites), reproduces the frozen speeds exactly ($\Delta X_T=\pm1,\pm2$,
40/40 each) and returns exactly over the established rest period.
Rerunning Y29's search under $X_T$ changes nothing numerically — still
0 of 132 settled full-turnover candidates — but now the explanation is
**algebraic, not merely empirical**: every handoff advances a
three-node fresh tail while retaining exactly one of two old-crystal
sites and recruiting one new one; a translation-covariant zero-drift
recurrence forces $\Delta X_T=0$, which forces the old pair to return
exactly, and after any three handoffs the fresh tail has fully turned
over regardless. This proves a clean

$$
\textbf{Two-anchor zero-drift theorem (Stage Y30):}\quad
\Delta X_T = 0 \text{ in a translation-covariant recurrence} \ \Rightarrow\ \{a,b\}_{t+P} = \{a,b\}_t \ \ (P\ge3)
$$

for the frozen two-old-site-register handoff architecture specifically
— an explicit, scoped no-go, not a claim against every possible CRR
rest construction (a carrier with no persistent old-site register, a
different support geometry, or a genuinely different grammar are all
explicitly left open). Native one-step and depth-8 searches for a
topology escape under the unchanged rule find none. **Full-turnover
rest is now algebraically closed for this architecture; the wake
itself, not the anchors, is the remaining unresolved physical defect.**

### 10.1aa A literature-informed reframing, properly tested rather than assumed, produces the sharpest design target yet (Stage Y31)

After five stages converging on a proven wall, Y31 imported one
structural *lesson*, not equations, from the discrete-breather and
dissipative-soliton literature (MacKay & Aubry 1994; Flach & Gorbach
2008; Grelu & Akhmediev 2012): a localized recurrent state need not
renew all of its own material to be physically legitimate, provided a
well-defined **local control volume** closes, even while the larger
system continues to grow around it. This directly supplies the
conceptual permission Y28–Y30 lacked — full turnover, now proven
impossible, was never the necessary target.

**The borrowed idea was tested, not assumed, and the answer clarified
rather than confirmed the analogy.** Of 360 single-relation local vacuum
perturbations, 354 cleanly detach from the advancing producer front
within a few events and 0 remain as a persistent front-locked mode —
the vacuum shows no resonance-trapping behavior at all, ruling out an
oscillatory-leakage explanation for the wake. But a four-point Floquet
decomposition of the rest cycle's attached-relation count,
$(+4,-4,+9,+2)$, has an exact, strictly positive zero-frequency
component, $\tilde{A}_0=2.75$ relations/event — a genuine cycle-averaged
source, not a harmonic that any nonresonance mechanism could suppress.
Global graph growth is $+24$/cycle against only $+11$/cycle retained in
the carrier-attached halo, so CRR already realizes part of the
dissipative-soliton picture (real outward historical export, $+13$/
cycle) — the missing condition is specifically **local flux balance**,
zero net attached-halo change, not global periodicity. A preregistered
search over 21,315 candidate $v_1$/$v_2$ words (1,228 exact recurrences)
finds a strict minimum attached-halo increment of exactly $+11$ with
zero nonpositive cases — confirmed directly against the raw screen
data — and lengthening the recurrence period never removes it. At the
bare carrier-handoff level (before marker/interface bookkeeping), the
source is already $+8$/cycle; the auxiliary machinery adds the
remaining $+3$.

**This is not a solved rest state — G3S still fails — but it converts
an open-ended "wake cleanup" problem into a sharply specified,
quantified design constraint**: a carrier-preserving handoff supplying
at least 8 additional units of shedding per bare cycle, closing the
complete marker/interface program at net zero. That the literature
comparison was tested against its own internal alternative (resonance
vs. flux imbalance) and found to point toward the less flattering,
more specific mechanism — rather than the framing simply being adopted
because it sounded applicable — is what makes this result trustworthy
rather than a loose analogy.

**Recommended next stage (Y32 — Carrier-Preserving Shedding Channel
Search).** Search specifically for a carrier-preserving handoff or
small handoff modification supplying negative attached flux at the
bare level, targeting the $+8$/cycle deficit directly, before any
further marker/interface augmentation; require the completed program to
close the full attached-halo budget at exactly zero over its proper
period while preserving carrier identity, the established $\pm
v_1,\pm v_2$ sectors, and $X_T$-measured zero drift.

### 10.1bb Real, quantified flux reduction, a genuine reversal, and a uniquely forced interface (Stages Y32–Y35)

A four-stage engineering campaign against the Y31 $+11$/cycle deficit,
each stage exhaustively screening a bounded, preregistered grammar
shell before inspecting flux values.

**Y32 (416 one-output substitutions)** finds the wake is genuinely
engineerable, not rigid: the best candidate lowers the complete-cycle
halo growth from $+11$ to $+9$ and the bare handoff budget from $+8$ to
$+6$, reproduced exactly across 6 sites and 300 audited cycles. **0 of
416 close the flux to zero.**

**Y33 (2,548 two-output pairs, seeded from Y32's 7 best first
substitutions)** pushes substantially further: best complete flux
$+6$, best bare flux $+3$, with the same $+3$ gap between them holding
across all 24 moving-compatible survivors — reproduced exactly across
300 further audited cycles (halo growing $54\to348$ over 50 periods,
matching $54+49\times6$ precisely). **0 of 2,548 close the flux.**

**Y34 (1,560 three-output triples, seeded from Y33's 5 best pairs) is
the most informative negative in the batch.** Only 5 of 1,560 candidates
preserve the full kinematic manifold at all, and all five independently
converge on the identical third substitution — a real structural
constraint, not search noise. That unique change **reverses** the
trend: complete flux rises from $+6$ to $+7$. The vacuum-grammar route
is effectively exhausted at this shell; the next available degree of
freedom points the wrong direction.

**Y35 returns to the best Y33 grammar and searches the interface layer
instead, catching a real accounting error in its own immediate
predecessors along the way.** The repeated "$+3$" difference reported in
Y33/Y34 was not a valid physical decomposition — it silently compared
two different observables (anchor-touching count vs. full-support-
touching count) rather than one control volume measured consistently.
A corrected, single-control-volume, operation-by-operation accounting
gives an exact breakdown: rule-firing $+2$, marker removal/addition net
$0$, ordinary event-Q additions $+4$, turnaround cleanup $-2$,
turnaround bridge addition $+2$, summing to $+6$. Screening all 60
legal uniform Q templates finds **exactly 1 survives even the moving-
sector check** — the original interface relation, $Q_1=T(c_2;\{f,c_4\})$
— with all 59 others failing all eight primary moving tests outright,
not merely the halo criterion. The predeclared fallback (3,600 split
event/bridge Q pairs) is pruned to 60 by the same constraint, and the
rest turnaround independently re-selects $Q_1$ again as the only
surviving bridge choice. **The interface relation is not a free tuning
parameter in this architecture — it is uniquely forced by the
established kinematics from two independent directions.** Extended
validation (6 sites, 300 periods) confirms $\Delta H_{\text{local}}=+6$
exactly throughout, with the exact same $(+2,-2,+5,+1)$ event sequence
at every site.

**Consequence.** The flux deficit is real and substantially reducible by
direct engineering ($+11\to+6$), but not by grammar substitution alone,
and not by changing *which* interface relation exists. G3S remains
failed throughout this batch.

**Recommended next stage (Y36 — Phase-Specific Q Lifecycle /
Compensated Interface Search).** Keep the best Y33 vacuum grammar and
$Q_1$ itself fixed for all moving transport. Search instead within the
interface's *lifecycle* — phase-specific retention or removal, distinct
plus-to-minus versus minus-to-plus bridge treatment, or a bounded
compensating relation paired with $Q_1$ and consumed within the same
proper period — rather than its topology. Use the Y35 decomposition as
a bookkeeping constraint on any candidate, not as a post-hoc scoring
function; the pass criterion remains unchanged: exact canonical halo
recurrence with $\Delta H_{\text{local}}=0$.

### 10.1cc The first exact wake-neutral solitons — a symmetric pair, doubly validated — with the remaining obstruction precisely localized to their reversal (Stages Y36–Y38)

**Stage Y36's exhaustive rest-interface search again fails completely**
(0 of 16,384 lifecycle programs; 0 of 600 bounded compensators; 0 of 6
kinematically-eligible phase-Q pairs — G3S remains closed on every
front). **But one phase-specific choice, found within that same search,
produces something qualitatively new**: with only the ordinary
state-0 interface relation changed
($Q_0=T(c_1;\{c_4,f\})$, all else — vacuum grammar, marker program,
turnarounds — unchanged), the carrier settles, after a short formation
transient, into an **exact wake-neutral translator**. Verified directly
against all 300 raw validation records (6 sites $\times$ 50
macroperiods): $\Delta X_T=+1$ crystal site per four-event period,
$\Delta H_{\text{local}}=0$ exactly, halo cardinality exactly 53,
complete local-halo graph isomorphism, and global relation count still
growing by exactly $+22$/period throughout — every single row, zero
exceptions. This is the dissipative-soliton architecture Stage Y31
imported from the literature, now *realized* rather than aspired to:
continued global growth, a bounded co-moving control volume, exact
local closure.

**Stage Y37 independently discovers, and separately validates, the
genuine negative conjugate.** The most direct symmetry search (16 phase
programs, 96 admissible interface pairs) finds 12 candidates with the
right kinematics but none with a settled zero-flux halo within the
original formation horizon — the negative branch simply needs a longer
transient, not a different mechanism. A dedicated long-formation
diagnostic confirms this, and the resulting candidate is independently
validated at six *different* sites (not the discovery sites), 300
further macroperiods: $\Delta X_T=-1$, $\Delta H_{\text{local}}=0$,
halo cardinality exactly 53 — structurally identical to the positive
soliton in every measured respect, confirmed directly against the raw
validation table. **$\pm v_s = \pm0.25$ crystal site/event, exact,
symmetric, doubly independently confirmed.** This substantially
strengthens G2: the program now contains a genuine mirror pair of
exact wake-neutral localized transport modes, not one isolated
construction.

**The obvious next step — splice the two solitons for zero net drift —
fails, but precisely at the reversal, not within either soliton.**
Composing one $+v_s$ period with one $-v_s$ period, respecting the
actual sign-continuity at the join (not the naive hard splice, which
isn't even executable), gives exact $\Delta X_T=0$ with clean core
recurrence throughout — but $\Delta H_{\text{local}}=+12$ per 8-event
composite, a genuine new source appearing only at the reversal.

**Stage Y38 exhaustively confirms this is unavoidable within the
frozen soliton interiors, and proves the source is genuinely fresh
material, not a counting artifact.** A complete 144-candidate reversal-
interface family (4 phase origins each side $\times$ 3 boundary
lifecycles each direction) gives, without exception, $\Delta X_T=0
\Rightarrow \Delta H_{\text{local}}\ge+12$ (18 zero-drift candidates: 8
at $+12$, 10 at $+14$; the 8 minima independently cross-checked at a
second site, reproducing exactly). Neither an 8- nor a 16-event
superperiod closes. A direct relation-provenance audit on two
independent $+12$ minima confirms the source is not old wake material
being re-encountered: of 27 relations present in the final halo but not
the initial one, **all 27 were created during that same reversal
period**. This is a real, structural fact about the act of reversal
itself — the same distinction real soliton-collision physics draws
between individual soliton stability and interaction dynamics,
independently rediscovered here as a genuine property of this
substrate rather than an imported assumption.

**Consequence.** $\text{wake-neutral } +v_s$ and $\text{wake-neutral }
-v_s$ are both established, exactly. Neither wake-neutral reversal nor
wake-neutral rest is. The remaining G3S obstruction is now located with
unusual precision: not the particle, not either direction of travel,
specifically the finite interface at which one is converted into the
other.

**Recommended next stage (Y39 — Reversal-Birth Topology Cancellation /
Interface Co-design), with one reframing worth considering in
parallel.** Freeze both validated soliton interiors exactly; canonicalize
the 27-added/15-lost reversal motif in carrier-role coordinates; search
a finite reversal-only interface (the same 60-template Q family,
independently at the two mode-reversal boundaries, before considering a
bounded compensator) for one that cancels the fresh source while
preserving $\Delta X_T=0$ and exact halo recurrence. Separately, given
the depth of effort (Stages Y26–Y38) invested in forcing literal
$v=0$ without success, while an exact, symmetric, wake-neutral
$\pm v_s$ pair now exists: it may be worth testing whether this
particle species' natural ground state is better identified with
$v_s=\pm0.25$ itself, rather than continuing to require true rest, in
case the reversal-interface problem also proves to be a structural
no-go.

### 10.1dd $\Delta H_{\text{local}}$ ruled out as a state-energy function; a universal reversal-source cardinality found instead (Stages Y39–Y42)

**Every preregistered scalar transform of the carrier halo fails badly
as an $E(v)$-like cost.** Testing $J,A_{\text{abs}},A_2,A_{\text{AC}},
A_{\text{bal}}$ and separate birth/death decompositions ($A_{\text{churn}}$,
$A_{\text{exch}}$) across $v=0,\pm0.25,\pm1,\pm2$: all candidates are
exactly sign-even, but none is convex or monotone in speed — the $v_1$
and $v_2$ sectors have zero scalar halo change event by event while the
slower $\pm0.25$ solitons carry large balanced internal circulation. A
quadratic-plus-quartic fit calibrated on two points and held out against
a third fails by factors of 20 to 425. **$\Delta H_{\text{local}}$ is
not a viable state-energy candidate.**

**A genuine, precise invariant emerges instead.** Mature sign reversals
at three structurally different speed magnitudes ($|v|=0.25,1,2$) all
inject exactly $+6$ attached relations per half-cycle, independent of
gross churn that differs between them by more than an order of
magnitude (Stage Y40: churn 165 at first reversal, rising past 1,687
after 40 prior reversals for the soliton, while the signed source stays
fixed at $+6$ throughout). Stage Y41 sharpens this from a hoped-for
universal six-relation topology (which fails: four distinct signed
motifs exist across the primary cases) to a **universal reversal-
source cardinality**. A causal-necessity audit on the clean $v_1/v_2$
family finds the $+6$ splits exactly in half: suppressing ordinary
output 1 alone removes 3 units with no loss of phase or motion (24/24
validated); suppressing outputs 1 and 3 together removes all 6, but
transmutes the carrier into a new, equally stable recurrent phase
rather than destroying it. Pairing two such phase-transmuting reversals
(Stage Y41) gives exact zero drift and exact core recurrence, with the
source reduced to a rigid $+2$ per 8-event composite — confirmed at
every tested site and magnitude. Stage Y42 exhaustively tests all 16
combinations of independent reversal masks at both boundaries (256
context trajectories, all executable, all exact zero drift) and finds
no combination cancels the $+2$; it is not an artifact of using the
same mask at both reversals.

**Consequence.** $\Delta H_{\text{local}}$ is reclassified as a
transition/order-parameter variable — informative about *changes* of
dynamical sector, strongly coupled to directed motion when perturbed
chirally (Stage Y39: correlation $-0.946$ between induced shedding and
displacement) — not a steady-state energy. The remaining rest
obstruction is narrowed from an open-ended search to a single rigid
$+2$ residue.

### 10.1ee Exact causal-lifetime engineering closes the residual to zero — the first stationary rest state in this investigation (Stages Y44–Y46)

Rather than continuing to search grammar or Q-topology space, this arc
asks a sharper causal question directly: *when, precisely, does each
attached relation stop being dynamically necessary?*

**Stage Y44** counterfactually deletes each of the Y43 boundary
relations at every micro-checkpoint from its birth to the proper
boundary, identifying an exact causal lifetime for 9 of 13 relation
classes. All $2^9=512$ resulting delayed-cleanup programs execute, and
all are rigid: $\Delta H_{\text{local}}=+2$ regardless of which safe
deletions are active, reducing standing turnover from $16$ in/$14$ out
to $7$ in/$5$ out without changing the net source. Four relations
survive as genuine **cross-boundary scaffolds**, needed past the
period boundary to reproduce the correct next-state preparation.

**Stage Y45** tracks those four scaffolds into the following composite
and finds three become safe immediately after the next event-0 rule
firing. Retiring one of them (event-6/output-7) is the only change that
moves the secular source at all: $+2\to+1$, confirmed at 96 of 96
tested periods across all primary contexts. A provenance audit then
isolates the entire remaining source to a single relation class,
event-7/output-7 — one of the three causal-backbone outputs Y41
protected — and measures its exact causal lifetime directly: safe
immediately after the *next* event-1 rule firing, one event later than
the other three scaffolds.

**Stage Y46 closes the gap exactly.** Retiring the previous-cycle
event-7/output-7 relation at its measured safe point, with no other
change to the vacuum grammar, Q topology, marker program, or selector,
gives $\Delta X_T=0$ and $\Delta H_{\text{local}}=0$ with exact full
carrier-halo isomorphism. Verified directly against all 1,200
population validation records (6 sites $\times$ 2 magnitudes $\times$ 2
signs $\times$ 50 periods): zero drift, zero flux, exact phase/
scheduler/Q/marker recurrence, exact halo isomorphism — every single
record, without exception. The exact turnover closure is $7$ in $/7$
out $=0$, the final step in the sequence
$16/14\to7/5\to7/6\to7/7$. **This is the first genuine stationary rest
state — G3S — established anywhere in this investigation**, for the
augmented carrier/interface law built cumulatively across Stages
Y18–Y46. The qualifier "augmented" is retained deliberately: the bare
vacuum grammar has no native consumer for the retired relation; the
lifecycle rule that retires it is an explicit addition, in the same
spirit as the marker and interface machinery the carrier already
depends on.

### 10.1ff The first positive, finite inertial curvature measured in this investigation (Stage Y47)

With a genuinely stationary rest anchor available for the first time,
the original Stage Y26 direct-contact scheduler observable — never
redefined, never refit — becomes interpretable rather than horizon-
dependent.

**Verified directly against all 240 primary trial records, to full
floating-point precision**: every moving sector ($\pm v_1,\pm v_2$)
costs exactly $\ln 2 = 0.6931\ldots$; both independently-realized
stationary rest anchors ($R_1$, halo 47; $R_2$, halo 49 — structurally
different halo sizes, identical measured cost) give exactly
$\tfrac34\ln2=0.5199\ldots$, agreeing to numerical precision despite the
different halo cardinalities. The odd component vanishes exactly
($A_{\text{odd}}(v_1)=A_{\text{odd}}(v_2)=0$). Applying the frozen
Y24/Y26 curvature algebra:

$$
M_i = \frac{16d_1-d_2}{6} = \frac58\ln2 = 0.4332169878499658 > 0,
\qquad
\beta_4 = -\frac1{16}\ln2 < 0.
$$

Reproduced exactly at six further interior sites (57,600 further event
measurements) after a geometry-only site amendment, frozen before any
replacement-site cost was inspected (the original outer sites cannot
support a full $80$-event unidirectional $v_2$ trajectory inside the
finite crystal — an eligibility issue, not a cost result). The negative
quartic term should not be read as "cost decreasing with speed" — $A(v_1)$
and $A(v_2)$ are exactly equal; the positive result is specifically the
near-rest curvature, with the quartic term supplying the flattening
needed to match two equal-cost finite-speed points.

**G5 passes for this carrier architecture** — the first positive,
finite, independently-defined inertial curvature in this program's
history. G6 (population, $\ge6$ distinct carrier identities) and G7
(the frozen Y5 $E_0$ comparison) are explicitly kept closed: six
measurement sites are six environments of one carrier, not six
carriers, and the original anti-selection firewall is preserved rather
than quietly weakened.

### 10.1gg The result does not transfer to the original carrier population — and the reason is now understood precisely (Stage Y48)

Testing whether the complete Y47 architecture transfers, unmodified, to
the twelve frozen Rule-55584 identities from the Y1–Y6 recurrence-energy
program: it does not, decisively. Across $12\times6\times2\times4=576$
carrier/spectator/site/sector trajectories, **zero survive even the
first event** — 460 have no admissible handoff at all, 92 lose the
frozen identity on the first successful handoff, 24 recruit the
designated spectator. A bounded, non-gating exhaustive diagnostic
confirms this is not a selector problem: of 64 admissible first-event
gates across the population, zero preserve any frozen six-node identity.

**The mechanism is precisely identified by a direct grammar audit.**
The transport grammar underlying Y47's result shares **zero of eight**
output relations with the original Stage-W Rule 55584 grammar under
which the Y5 carrier population was discovered (it shares 2 of 8 with
the Y23 base and 4 of 8 with a later intermediate design). Y47's carrier
is not the original rule with an observer attached — it is a distinct,
cumulatively co-designed rewrite architecture, built across roughly
thirty stages targeting kinematics and flux balance rather than
matching the original discovery grammar.

**This does not retract Y47.** The positive curvature stands for its
own architecture. What fails is the assumption that architecture is a
portable wrapper around the original carrier population. G6 fails for
this transfer attempt specifically; G7 remains closed.

### 10.1hh Renaming the construction and searching for genuine diversity within it: a strong attractor, one species so far (Stage Y50)

Rather than continue forcing the new architecture onto the old
population, this stage names it independently — **FBCL, the Flux-
Balanced Carrier Law** — and asks whether FBCL itself naturally
supports multiple distinct recurrent carrier identities, with no
recurrence-energy or curvature value consulted during discovery.

Screening all 4,526 states within three relation edits of the reference
launch core: $1{,}704$ ($37.65\%$) support the complete exact
$\pm v_1,\pm v_2$ manifold under the unchanged law — a strong local
robustness result. But **every one of the 1,704 successful launches
converges to the identical mature five-role isomorphism class**,
confirmed by canonicalizing under all $5!=120$ role permutations before
comparison. Failure modes are equally constrained: every failure is
either an unavailable transport step or an undefined position
coordinate — never an incorrect persistent speed, a non-period-1 core,
or four sectors settling into different classes. The single discovered
species replicates exactly across 32 of 32 site/seed/sector contexts.
**FBCL behaves locally like a strong single-species attractor, not yet
a multi-species spectrum** — the population gate ($\ge6$ distinct
identities) is not met, so no mass-energy comparison is possible for
FBCL either.

**Recommended next stage (Y51 — Global FBCL Recurrent-Core Census).**
Do not extend the local edit radius further; Y50 shows this tests basin
attraction, not species diversity. Instead enumerate the complete
six-relation five-role core space abstractly, prefilter algebraically
for a legal one-step successor, quotient by role isomorphism before
simulating, and test surviving classes in all four signed sectors —
extending to other relation counts or periods only if the six-relation
stratum proves insufficient. This determines whether Y50's single
species is an artifact of local search or a genuine structural property
of FBCL, entirely blind to recurrence energy or curvature throughout.

### 10.1ii The native Rule-55584 branch is decisively closed, retroactively validating the FBCL pivot (Stage Y49)

Returning to the original Stage-W Rule-55584 law and the twelve frozen
Y5 carrier identities directly, rather than transplanting the later
Y33/Y46 architecture: native exact-return mobility turns out to be
common (of 247 first contacts, 227 establish bounded exact-return
macrosteps, and 186 of those have nonzero directional displacement in
the centered relational ruler) — the original population is not simply
pinned. But the population-level requirement fails earlier than
expected: a carrier needs, already at its first exact boundary, at
least one zero-direction return and at least two velocity values of
each sign. **Only 2 of the 12 carriers (identities 5 and 17) meet this
necessary condition**, against the 6 the population gate requires —
making the gate mathematically unreachable regardless of how well those
two carriers might behave under further testing.

Winner 28 — the carrier that motivated much of the earlier momentum
program — is a sharp illustrative control: all 12 of its native exact
returns are directionally zero. Its scheduler-robust recurrence and
spatial motion are cleanly separable, confirming the later Y47 moving
architecture added genuine kinematic structure, not something already
latent in ordinary Rule-55584 recurrence. Carrier 17 sharpens this
further: its rest selector completes 8 of 8 exact-return macrosteps at
$\Delta\mathbf{X}=0$, while every one of its four signed moving
selectors loses its option set within a handful of steps. **The
obstruction is specifically velocity-sector closure and persistence,
not the ability to form an exact recurrent rest state at all** — the
same distinction, independently rediscovered, that has organized the
entire Y18–Y46 kinematic program.

**This closes "Branch A" decisively and retroactively validates Stage
Y50's decision to treat FBCL as its own law rather than force-fitting
the original population**: that choice is now confirmed necessary, not
merely convenient, since the native route is independently proven
unreachable before any FBCL work is invoked.

### 10.1jj Exhaustive confirmation: one species, across every tested notion of "distinct" (Stages Y51–Y53)

Three successive stages close off, in turn, every plausible source of
hidden species diversity within the single-carrier FBCL ontology,
each blind to recurrence energy and curvature throughout.

**Stage Y51** exhausts the *complete* six-relation five-role launch
space: $\binom{30}{6}=593{,}775$ raw age-ordered cores. A methodological
subtlety is caught and corrected before the global result is
finalized — FBCL's explicit causal-order constraint means graph-
isomorphic cores at different age positions are not dynamically
equivalent, so pre-dynamics isomorphism quotienting would have produced
false negatives (confirmed directly: the graph-canonical orientation of
the already-known species fails to launch, while a different age
ordering of the identical graph succeeds). The corrected census finds
37,086 states pass a necessary first-step screen (verified against
direct simulation at 256/256 agreement), 1,783 pass the complete
four-sector test, spanning 454 distinct launch graph orbits — and
**all 1,783 converge to the same mature species**, replicated 32/32
independently.

**Stage Y52** extends the same exhaustive population to internal
periods 1 through 4, using a structural fact that keeps the search
tractable (every successful handoff returns the carrier to exactly six
internal relations, so higher-period species remain a six-relation
problem). Of 17,828 individual sector trajectories that pass, **all
17,828 are period 1** — zero realized at periods 2, 3, or 4. The 2,068
complete four-sector launches span 455 graph orbits and again converge
to the identical species, 32/32 replicated. A projected transition
graph over 37,236 nodes finds only two genuine self-loops (the mature
sign-oriented orientations) and confirms three apparent formal 2-cycles
are context-splicing artifacts, not physically realized recurrences.

**Stage Y53** extends the species definition outward from the bare core
to the complete dressed state (core, live Q and marker relations, full
carrier-touching halo, causal-generation class). Of 2,068 Y52 launch
histories, 1,299 support recurrent dressed states in all four sectors,
and **all 1,299 collapse to one dressed species, DS001** (halo sizes
$42,42,44,44$ for $+v_1,-v_1,+v_2,-v_2$; one live Q and one marker
throughout), replicated 32/32. A genuinely useful distinction is drawn
from the 70 rejected cases: they carry *two* live Q relations rather
than one — an inherited secular history relation whose old-vacuum
offset recedes indefinitely rather than closing — correctly classified
as persistent memory, not a second recurrent species.

**Consequence.** Local static perturbation (Y50), the complete
six-relation core topology (Y51), internal periods 1–4 (Y52), and the
full Q/marker/halo dressing (Y53) are now all exhausted as sources of
single-carrier species diversity, each with a decisive, independently
replicated null. $N_{\text{FBCL,species}}=1<6$ stands on the strongest
possible footing within these bounds.

### 10.1kk A genuine composite particle, precisely characterized as speed-selected rather than history-dependent (Stages Y54–Y55)

**Stage Y54 is the first FBCL population stage to find a structure
that is not merely another basin for the single known carrier.**
Screening 1,600 frozen two-carrier constructions (separations $6$–$30$,
all 16 ordered sector pairs, both update orders, two tie seeds), 8
qualify as a genuine composite — all at exactly separation $d=7$, and
only in the co-moving $(+v_2,+v_2)$ or $(-v_2,-v_2)$ sectors. The pair
carries a single, non-factorizable, regenerating cross-carrier relation,
$T(B_0;\{A_1,O_{+2}\})$ — one role from each constituent plus a shared
old-vacuum scaffold site — with zero cross-carrier gates. Two
implementation errors (confusing the 11-relation launch state with the
6-relation mature core; requiring composite identity during formation
rather than only during measurement) were caught and corrected before
the primary result was interpreted. A post-specified bond-ablation
test confirms the coupling is dynamically real, not decorative: deleting
the cross relation at a mature boundary, the bond regenerates within
one pair round and the full dressed state rejoins the unperturbed
control within 2–3 rounds. Extended stress testing (16/16 contexts,
200 measured pair rounds in an enlarged 1,400-event vacuum) confirms
genuine persistence. This structural dimer family is labeled **CD001**.
Same-speed $\pm v_1$ pairs at the same separation, however, fail the
primary recurrence test — leaving the composite's kinematic manifold
incomplete.

**Stage Y55 corrects Y54's own preliminary diagnosis and finds a
sharper, more decisive characterization.** The direct $d{=}7$ $v_1$
pair is not indefinitely secular, as first classified — extending the
trace shows it settles naturally to an exact period-1 dressed state by
the fourth measured round in all 32 tested contexts (Y54's window was
simply too short). But the settled state has **zero cross-carrier
relations in every one of the 32 contexts** — two independent DS001
carriers at constant separation, not CD001. A rigorously causal
last-use protocol accordingly finds zero relations eligible for
justified retirement, so no forced cleanup is attempted (a real and
important negative: nothing is deleted merely to manufacture a
preferred bond). A separately frozen speed-switch diagnostic then
settles the question decisively: slowing a mature CD001 pair from
$v_2$ to $v_1$, the bond survives exactly one transition round and then
vanishes, relaxing to the same factorized attractor direct $v_1$
formation reaches; accelerating a factorized $v_1$ pair to $v_2$, the
bond nucleates by transition round 2 with no bond inserted by hand, and
the full state rejoins directly-formed CD001 by round 6. Neither
direction shows hysteresis. **CD001 is a genuine $|v|=2$-selected
dynamical bound state, not a hidden residue of formation history.**

**Consequence.** FBCL now supports two structurally distinct objects: a
single-carrier species (DS001) and a composite bound state (CD001) that
exists specifically in the fast sectors. Neither alone completes a
$0,\pm v_1,\pm v_2$ manifold, so G6 remains closed for both, but the
composite result is a genuine expansion of the FBCL ontology — the
first population-relevant structure beyond one isolated attractor.

**Recommended next stage (Y56 — Composite Velocity from Bonded Sign
Words).** Do not modify FBCL further. CD001 already has two strongly
validated microscopic bonded transport states, $+v_2$ and $-v_2$;
search whether periodic sign words built only from these already-
bonded microsteps (starting with periods 2, 4, and 8, both update
modes) yield recurrent composite-level average velocities
$0,\pm1,\pm2$ while preserving the nonfactorizable bond throughout,
rejecting any word whose reversal destroys coupling or full dressed
recurrence — testing whether a stationary or intermediate-velocity
composite can be built entirely from motion already proven to sustain
the bond, rather than reopening the factorized $v_1$ sector.

### 10.1ll Direct bonded reversal is impossible; reversal through the factorized sector works kinematically but leaves an unexpectedly long wake (Stages Y56–Y57)

**Stage Y56 tests the direct approach exhaustively and finds a clean,
total failure at a single, precise point.** All 276 binary sign words
of lengths 2, 4, and 8 (1,104 word/context runs) are tested, restricted
to the already-validated bonded $\pm v_2$ microsteps. The 6 uniform
controls pass in every context, confirming the harness correctly
reproduces established CD001 motion. **Every one of the 270 nonuniform
words fails — 1,080 of 1,080 reversal contexts — and every failure
occurs at exactly the first sign change**, with exact AB/BA symmetry
ruling out a one-constituent defect. A post-specified diagnostic
localizes the mechanism precisely: immediately before reversal each
constituent has exactly one legal old-vacuum handoff, in the current
direction; immediately after the frozen turnaround, both constituents
have zero legal handoffs in *any* direction, while the CD001 bond
itself remains fully intact. The obstruction is a transport-dead
interface, not dimer dissociation — direct bonded reversal is simply
not available under the tested turnaround, at any period.

**Stage Y57 tests the natural alternative — routing the reversal
through the already-established factorized $v_1$ sector — and finds it
kinematically real but far slower than expected.** The path
$+v_2\to+v_1\to-v_1\to-v_2$ (and its conjugate) executes in all 32
tested contexts; both constituents reach exact conjugate $|v|=1$ by
reverse round 3, confirming the reversal is not locally blocked in the
factorized interior. But the complete *dressed* state does not settle
within the preregistered 12-round window in any context — a
post-specified extension shows all 32 eventually converge, but only at
round 48 (positive-start) or 50 (negative-start), with the excess
traced entirely to carrier-touching history relations (15 excess at
round 12, zero at permanent convergence), not to the Q topology, which
stabilizes almost immediately. **Kinematic reversibility is positive;
short dressed recurrence is negative; long-run relaxation is positive**
— three genuinely different questions, cleanly separated for the first
time.

### 10.1mm Two half-reversals do not compose into a cycle — and the reason is a real, linearly-growing, non-local memory effect (Stages Y58–Y59)

**Stage Y58 uses the Y57 relaxation horizon directly and finds the
isolated half-reversal fully validated, but composition fails.** Using
a fixed 60-round reverse-$v_1$ dwell, all 32 contexts complete an exact
half-reversal ($+v_2\to+v_1\to-v_1\to-v_2$ or its conjugate), with
deterministic center-of-pair displacement ($\mp63$ crystal sites).
**But concatenating two half-reversals without re-formation fails in
32 of 32 contexts** — not because the second reversal is blocked, but
because its wake takes far longer to clear: a post-specified 180-round
extension shows all 32 converge, but only at round 99, roughly double
the first reversal's horizon, with the excess relation count growing
*before* shrinking (peaking near round 52–53, well past the original
60-round test window). **The central finding**: the local CD001
fingerprint at the end of a successful half-reversal is *exactly*
equal to a freshly-formed CD001 state — yet the subsequent turnaround
behaves as if it were not fresh. Local recurrence is not a sufficient
renewal state for repeated reversal dynamics.

**Stage Y59 precisely quantifies this memory effect and locates exactly
where it lives.** Running four, then eight, successive half-reversals
(32 contexts primary, 8 further in an extended Tier-C stress; 128 and 64
half-reversals respectively, all executing without failure), the
renewal horizon grows **exactly linearly**: $T_n^{(+)}=54n+9$,
$T_n^{(-)}=54n+11$ reverse-$v_1$ rounds, confirmed through 8 successive
reversals with no saturation and no periodic reset. Peak wake amplitude
grows linearly too ($P_n^{(+)}=24n+1$, $P_n^{(-)}=24n+8$), and
half-reversal displacement grows correspondingly rather than closing
into a bounded cycle. A relation-hop expansion around each locally
exact CD001 boundary finds the surrounding state is indistinguishable
from a genuinely fresh carrier through hops 1–2, first differs from
fresh at hop 3 (exactly 28 records, every tested boundary) — but that
hop-3 difference does not yet encode reversal *count*: same-direction
histories after reversal 1 and reversal 3 remain identical through hop
7, and first differ at **hop 8**, confirmed at 12 of 12 successive
same-direction comparisons through eight reversals, with the hop-8
record count nearly stationary while its structural content changes
uniquely at every occurrence. **FBCL therefore retains a real,
structured, non-resetting history-dependent degree of freedom,
located at a precise and reproducible distance from the carrier
(hop 8), whose growth directly predicts each subsequent turnaround's
cost** — explicitly not yet identified with spin, winding number, or
any other named quantum number, but established as a genuine,
quantified departure from Markovian local-state completeness.

**Consequence.** CD001 does not yet have — and, under repeated reversal
as currently constructed, does not appear to be approaching — a
bounded, stationary proper cycle. The obstruction is not that reversal
is impossible (it plainly isn't) but that FBCL's vacuum retains
structured memory of it that a local particle description cannot see
or discharge. G6/G7 remain closed; no composite cost or curvature was
measured at any stage in this arc.

**Recommended next stage (Y60 — Wake Advection / Forgetting Test).**
Test whether the accumulating turnaround memory can be shed by ordinary
coasting rather than reversal itself: after one locally-completed
half-reversal, allow CD001 to translate uniformly in its bonded $v_2$
sector for a range of frozen coast intervals before the next mediated
reversal, measuring the resulting renewal horizon and hop-8 fingerprint
against the un-coasted baseline. If sufficient coasting returns the
next reversal to the original, un-burdened horizon, the memory behaves
like advected, detachable vacuum wake; if the burden persists
regardless of coast length, it is more tightly bound to the carrier or
interface state itself. This distinction should be resolved before any
further attempt at a stationary CD001 cycle.

### 10.1nn Neither carrier-bound nor decaying: a fixed, location-bound vacuum scar (Stage Y60)

Testing coasts $C\in\{0,4,8,16,32,64,128,256\}$ pair rounds in the
bonded $v_2$ sector between a completed half-reversal and the next,
with an independently-formed matched-fresh control at every coast
length: **neither of the two hypotheses Y59 left open is correct.**

**The carrier genuinely forgets, locally and exactly.** The hop-8
symmetric difference between the historical and matched-fresh
carrier-centered states shrinks with coast length (377/368 at $C=0$,
falling to 12/12 at $C=16$) and reaches **exactly zero at $C=32$,
remaining exact through $C=128$** — verified directly against the raw
per-context data, 8 of 8 primary contexts at every coast length. The
carrier's own neighborhood becomes genuinely indistinguishable from a
freshly-formed composite, not merely similar.

**But the memory is not erased — it is relocated, and precisely so.**
For every coast length with a fully observed reversal ($C\le64$), the
historical reversal pays the identical extra renewal cost relative to
its matched-fresh control: $\Delta H=52$ (initial $+v_2$) or $56$
(initial $-v_2$), **exactly independent of coast length**. The round at
which historical and fresh trajectories first diverge grows exactly
linearly, $r_{\text{div}}=22+2C$, confirmed through $C=128$ — but the
decisive fact is *where* this divergence occurs: at the identical
absolute pair-center coordinate regardless of coast length
($2969.0$ for initial $+v_2$, $3036.0$ for initial $-v_2$, confirmed to
the decimal place across every tested $C$ from 0 to 128, and
independently reproduced at two further insertion centers). The
returning carrier re-encounters the cost only upon physically returning
to the specific location where the original reversal happened — exactly
$8.5$ coordinate units back from the post-reversal boundary, in every
context.

**The appropriate caution around the $C=128$/$256$ results is preserved
deliberately.** At $C=128$, both reversal arms are censored by the
frozen $H=320$ ceiling before certification completes, though the fixed
divergence locus and hop-8 forgetting both still hold. At $C=256$,
historical and fresh traces remain identical throughout the entire
observed window — consistent with the carrier simply not having
traveled far enough back to reach the scar before the cutoff. The
$r_{\text{div}}=22+2C$ law would place a continuation at round 534, but
this is explicitly **not** counted as an observed result and the
horizon was deliberately not extended to chase it.

**Interpretation.** This is neither carrier-bound memory nor ordinary
decaying wake, but a third structure: a persistent, spatially localized
disturbance in the relational vacuum itself, left at the location of
the reversal, undiminished across the entire tested range, invisible to
any local probe of the carrier once it has moved away, and paid in full
only upon direct return. The natural language for this — used
descriptively, not as a claim of identity — is a **relational vacuum
scar**: structurally analogous to memory effects documented in
nonlinear field and gravitational physics, where a rapid event leaves a
permanent, location-bound imprint that a source no longer at that
location does not carry, but that any later trajectory through the
region still detects. The report is explicit that this is not yet
identified with any named physical object (field, topological defect,
charge, spin) — an empirical statement about FBCL's relational vacuum
and the CD001 trajectory, not an interpretation reaching beyond it.

**Recommended next stage (Y61 — Turnaround-Scar Localization and
Persistence).** Freeze a long coast ($C\ge64$, including at least one
$C=128$ arm) so the carrier's own neighborhood is genuinely fresh, then
map the relational state *around the fixed re-contact locus itself*
rather than around the carrier — its spatial support and radius,
signature, and persistence as the carrier continues to move away, using
time-matched fresh-vacuum controls throughout. The decisive follow-up
question, to be addressed only after localization: whether the scar
acts on any compatible carrier passing through it, or specifically on
the carrier/history that created it — the distinction between a
genuine carrier-independent vacuum feature and a spatially-deposited
but still history-tagged memory.

### 10.1oo The scar is a stationary one-sided history trail with a sharp near edge — but its far end is still unresolved (Stage Y61)

Freezing long coasts $C\in\{64,128,256,512\}$ so the carrier's own local
neighborhood is genuinely fresh (32/32 primary checkpoints pass the
hop-8 carrier-local guard), Y61 stopped probing the carrier and instead
scanned the fixed absolute re-contact locus itself, comparing the full
incident relation star and legal gate star of the historical and an
independently-formed matched-fresh state at every old-vacuum vertex
$d=-32\ldots+32$ around it.

**A reproducible, sharply-edged, one-sided trail is present at every
checkpoint.** For an initial $+v_2$ turnaround, every primary context and
every coast length shows nonzero historical/fresh differences
continuously from offset $+4$ to the preregistered $+32$ scan boundary
(226 relation-symdiff records, 8 gate-symdiff records); the initial
$-v_2$ branch mirrors exactly, offsets $-32$ to $-4$ (227 relation, 5
gate records). No difference occurs within three coordinate units of the
frozen locus in either sign. Because the profile is still nonzero at the
scan boundary rather than tapering to zero, Y61 declares the support
**censored**, not finite — the far edge and total trail length remain
unmeasured by design.

**The trail is exactly persistent while the carrier recedes.** For every
one of the 8 primary contexts, the complete $C=64$ support set's raw
relation-star and gate-star content — not merely a summary fingerprint —
is bit-for-bit unchanged at $C=128$, $256$, and $512$, while the carrier
itself moves from 136.5 to 1032.5 coordinate units away from the frozen
locus. No support offset disappears and no new one appears. Tier-B
replication at centers 2400 and 3600 (16/16 checkpoints) reproduces the
identical support intervals, burdens, and exact persistence.

**A post-specified diagnostic ties this directly back to Y60's
divergence point.** At the Y60 first-divergence round, the returning
pair center sits exactly at the frozen locus, and the leading
constituent's own forward old-vacuum support vertex is simultaneously
Y61's first nonzero trail vertex at offset $+4$ (or $-4$). The Y60
trajectory therefore separates from its fresh control at the precise
moment the returning carrier's leading edge first touches the trail's
near boundary — not at some interior or averaged location.

**Interpretation.** The turnaround memory is not a compact,
carrier-bound scar but a stationary, one-sided relational history trail
left behind in absolute vacuum coordinates, with a sharp near edge and
an as-yet-unmeasured far edge. No stationary composite or mass/energy
gate is opened by this result.

**Recommended next stage (Y62 — Full Trail Extent and Return
Coupling).** Freeze a directional scan wide enough to cover the entire
prior half-reversal path (at least 96 coordinates beyond the Y61 near
edge) to locate the far edge and exact total trail length; confirm the
full relation/gate profile remains stationary under long coast across
that whole length; characterize the birth-order deposition sequence
along the trail; and test whether the measured trail length or
integrated burden quantitatively accounts for Y60's sign-dependent extra
renewal costs ($+52$/$+56$ rounds) before sending any independently
prepared third-party carrier across it.

### 10.1pp The trail is finite, and its overlap geometry exactly reproduces the Y60 renewal delay (Stage Y62)

Widening the directional scan to $k=0\ldots192$ from the frozen Y60/Y61
locus closes the censoring left open by Y61.

**The trail is finite, contiguous, and exactly stationary.** For an
initial $+v_2$ turnaround the support is $k=4\ldots75$ — exactly 72
consecutive old-vacuum vertices, zero internal gaps, 117 trailing zero
coordinates before the scan ends (far edge certified). For initial
$-v_2$: $k=4\ldots77$, 74 vertices, zero gaps, 115 trailing zeros. Both
results are identical across all four primary order/tie contexts and
both primary coast checkpoints ($C=64,512$), and replicate exactly at
Tier-B centers 2400 and 3600 ($C=64,256$). The complete raw relation and
gate content at $C=64$ is unchanged at $C=512$ in all 8 primary
contexts — the same exact persistence Y61 found, now shown to hold
across the entire finite trail rather than a truncated window.

**No simple static count tracks the Y60 penalty.** Unique relation-symdiff
records (610 / 622), gate-symdiff records (8 / 8), and integrated
per-offset touch burden $I_{\text{touch}}$ (756 / 768) were all measured,
but none of $\Delta H/L$, $\Delta H/R_{\text{union}}$, or
$\Delta H/I_{\text{touch}}$ is sign-invariant (e.g. $0.7222$ vs.
$0.7568$ for $\Delta H/L$), so Y62 declines to promote any of them as an
energy-like turnaround cost.

**Birth-order provenance is strongly ordered along the trail.** The
per-offset median historical-only relation birth label is monotone with
trail coordinate $k$ (Spearman magnitude $0.98$–$0.99$; OLS slope
$\approx-4.11$ births per coordinate across all contexts) — consistent
with sequential deposition during the original turnaround trajectory,
though this remains bookkeeping provenance, not a physical time claim.

**A fixed 320-round return probe gives an exact geometric match.** Mature
CD001's old-vacuum footprint spans $\pm4$ coordinates about its pair
center, so a contiguous trail of length $L$ should influence the pair
center over exactly $L+8$ positions. This is observed exactly: the
72-vertex $+v_2$ trail produces 80 consecutive historical/fresh
signature-difference rounds ($150$–$229$; pair-center interval
$X_{\text{scar}}\ldots X_{\text{scar}}+79$), and the 74-vertex $-v_2$
trail produces 82 ($150$–$231$; interval $X_{\text{scar}}\ldots
X_{\text{scar}}-81$) — both endpoints matching the predicted convolution
exactly, in all four order/tie contexts each.

**This resolves the Y60 $+52$/$+56$ delay mechanistically.** The
matched-fresh arm renews at round 178 ($+v_2$) or 176 ($-v_2$); the
historical arm, still inside the trail-contact interval, renews only at
230 or 232. The Y60 penalty is exactly the trail-contact time remaining
*after* the fresh control's natural renewal point — $230-178=52$,
$232-176=56$ — not a static count of any kind.

**A post-specified synthesis reconstructs all eight Y59 renewal horizons
exactly**, with no fitted parameter, by accumulating the sign-specific
delays $52$/$56$ on top of the fresh baselines $63$/$65$:
$63,117,171,225,279,333,387,441$ (initial $+$) and
$65,119,173,227,281,335,389,443$ (initial $-$) — reproducing Y59's
observed sequences exactly, and deriving the previously-empirical
universal $+54$ increment algebraically: $(65-63)+52=54$ and
$(63-65)+56=54$. This is strong evidence that Y59's cumulative memory is
an environmental multi-trail history rather than a hidden carrier-internal
counter — but the additivity itself has not yet been tested spatially.

**Recommended next stage (Y63 — Multi-Trail Superposition and
Additivity).** Build two- and three-reversal histories, map every
predicted single-turnaround trail corridor while the carrier is far
away, and test directly whether each earlier trail's raw content survives
a later reversal unchanged, whether the multi-trail historical state
equals the combination of the independently measured single-trail
states, and whether a fixed next reversal accumulates the $52$/$56$
delays one trail at a time from spatially identified objects rather than
from the final timing sequence alone.

### 10.1qq Turnaround-delay additivity is confirmed dynamically, but the environmental record is not an immutable linear superposition (Stage Y63)

Y63 built histories of two and three successive mediated CD001
reversals (8 primary + 8 Tier-B contexts each) and tested the Y62
additivity hypothesis directly, both spatially and dynamically. All 24
primary and 24 Tier-B half-reversals reproduce the frozen Y59
certification horizons exactly ($63,117,171$ / $65,119,173$) before any
new interpretation is drawn.

**Strict raw persistence of older trails fails completely.** Comparing
each older trail's baseline raw relation/gate content immediately after
its deposition against its state after the next reversal: **0/24**
primary and **0/24** Tier-B comparisons remain raw-identical. Every
audited vertex of every older trail corridor changes — including every
one of its original Y62 support vertices. Later reversals do not deposit
an independent trail on top of an untouched earlier one; they rewrite
the existing environmental record.

**The multi-history support is larger than the isolated-template union,
and is itself censored.** At the boundary after two or three prior
trails, historical/fresh support was audited over the frozen union of
the predicted single-trail corridors ($k=0\ldots112$ around each). No
case — 0/16 primary, 0/16 Tier-B — equals the isolated-template union,
and every case reaches the outer edge of the preregistered audit region,
so the complete transformed support is censored rather than finite.
Within the audit region the counts are population-reproducible but
strictly larger than the template union (e.g. two prior trails: 122 vs.
96 nonzero coordinates for initial $+$, 120 vs. 98 for initial $-$;
three prior trails: 167 vs. 150 and 167 vs. 152). No template coordinate
is ever missing — only additional ones are modified.

**The fixed next-reversal probe shows a universal 30-round excess.**
Relative to the contact interval predicted from the untouched isolated
Y62 templates, every two- and three-trail historical trace remains
different from its matched-fresh control for **exactly 30 rounds
longer** (two trails: 134 observed vs. 104 predicted, and 136 vs. 106,
for initial $+$/$-$; three trails: 188 vs. 158, and 190 vs. 160).
Because the static multi-history support itself is censored, Y63 leaves
open whether this is a genuine post-contact dynamical relaxation tail or
simply the signature of the expanded, rewritten static corridor —
that distinction is deferred to Y64.

**Despite the failure of raw spatial superposition, the delay law is
exact.** Using only the independently frozen single-trail delays
$P_+=52$, $P_-=56$, with no fitted parameter: two prior trails (one of
each sign, either starting orientation) predict $52+56=108$, observed
in 16/16 primary+Tier-B contexts exactly; three prior trails predict
$52+56+52=160$ (initial $+$) and $56+52+56=164$ (initial $-$), observed
in 16/16 contexts exactly. Combined: **32/32 exact additive delays**
across every tested history.

**Interpretation.** Turnaround-delay additivity is demonstrated directly
under real multi-history evolution, while a simple immutable linear
superposition of spatial trail states is falsified: successive
turnarounds build a single interacting environmental-history corridor
that later passage actively rewrites, yet each prior turnaround's
contribution to future renewal delay remains exactly additive. No
composite rest sector or mass/energy gate is opened; $52$ and $56$
remain renewal-delay counts, not energies.

**Recommended next stage (Y64 — Multi-History Corridor Extent /
Interaction-Kernel Test).** Rebuild the same two- and three-trail
histories; freeze a substantially wider absolute scan beyond both outer
edges of the Y63 audit union; locate the complete transformed
historical/fresh support after each multi-trail boundary; test whether
convolving that *observed* transformed support with the CD001 footprint
reproduces the full next-reversal difference interval, including the
extra 30 rounds; and localize which later-reversal events rewrite each
older-trail region, and whether that rewriting stays local to the
geometric region of passage or propagates beyond it. The independent
$52$/$56$ delay law should be retained as a separate dynamical invariant
unless a direct structural derivation from the transformed support
emerges. Only after the transformed multi-history state is understood
should an independently prepared third-party CD001 be sent through an
isolated single trail.

### 10.1rr The Y63 excess is explained exactly by an asymmetric active-interaction corridor (Stage Y64)

Freezing a wide scan (`template_min-192` to `template_max+192`, requiring at least 32 consecutive zero coordinates outside both edges) around each two- and three-history boundary, Y64 certifies the transformed multi-history support as **finite** in all 16 primary and 16 Tier-B cases — the shortest observed zero tail is 162 coordinates, far past the certification requirement.

**The rewrite is asymmetric.** Relative to the isolated-template union, the transformed support extends exactly **30 coordinates beyond the exit edge** (the direction the returning carrier eventually travels after entering the region) in every one of the 32 scored cases, and extends **19 coordinates beyond the entry edge** as well — but that entry-side extension turns out to be dynamically silent. Treating the full static support as active over-predicts the next-reversal contact duration by exactly 19 rounds in all 32 cases (e.g. naïve prediction 153 rounds vs. observed 134 for a representative case).

**The correct active corridor recovers Y63 exactly.** Using the *original* isolated-template entry edge together with the *newly measured* transformed exit edge, and convolving that corridor with CD001's $\pm4$-coordinate footprint, reproduces the complete Y63 differing-round counts precisely — 134, 136, 188, and 190 rounds for the four (sign $\times$ 2-or-3-history) cases, 16/16 primary and 16/16 Tier-B exact. Y63's unexplained 30-round excess is therefore not a free relaxation tail; it is the geometric consequence of a **30-coordinate active extension** created when a later reversal rewrites the accumulated history.

**A post-specified rewrite-localization trace** shows this extension is built progressively during physical passage, not deposited nonlocally: the original trail is completely untouched through deceleration and turnaround setup, and every one of its support vertices first changes when the returning pair center is exactly 5 coordinates away, with the rewritten region advancing one coordinate per reverse-v1 round — a local rewrite front tied to carrier passage.

**The 52/56 additive delay law is untouched.** Y64 separates two structures that had previously been conflated: an **environmental interaction geometry** that rewrites nonlinearly and has a directional active kernel, and the **renewal-delay increments**, which stay exactly additive despite that nonlinear spatial rewriting. No structural derivation of 52/56 from a scalar relation count is claimed.

**Recommended next stage (Y65 — Independent Trail Crossing and
Backreaction).** With the environmental interaction geometry now fully resolved, run the deferred third-party test: send an independently prepared CD001 probe, sharing no creator lineage with the trail, through a separately generated isolated trail with matched no-trail controls, in both directions and both signs, to determine whether the trail is externally readable, whether it imposes the same 52/56 delay on an unrelated probe, and whether crossing rewrites it the way creator-history passage does.

### 10.1ss The trail is externally readable, but an unrelated probe does not rewrite it (Stage Y65)

Y65 forms an independent probe dimer, sharing no support lineage with the trail's creator, and sends it through an isolated Y62 trail from the untouched side, comparing it against a matched no-trail control.

**The isolated trail is objectively readable by a stranger.** Every one of 8 primary and 8 Tier-C pristine fresh probes is exactly equal to its no-trail control up to the first round of footprint overlap, differs on every contact round, and rejoins its control on the very first round after contact ends — 80 rounds exactly for a positive-deposition trail, 82 for negative, precisely matching the already-established `trail length + 8` contact prediction. (The opposite, causal-return-side approach could not be made pristine for geometric reasons — the source's own departure history occupies that region — so Y65 also ran a separate, non-scoring matched-history diagnostic there; it reproduced the same 80/82 read-exact result in 16/16 additional cases.)

**Yet the trail itself is left completely unchanged.** In 0 of 8 primary and 0 of 8 Tier-C strict fresh crossings — and 0 of 16 matched-history diagnostic crossings — does any original support vertex change; the post-crossing support count, edges, and entry/exit extents are exactly the original isolated-trail values. This is a sharp contrast with Y64, where every creator-history passage rewrote every original support vertex.

**The 52/56 delays do not transfer to an unrelated probe.** The independent probe's signature separates from its control only during geometric trail contact and rejoins immediately once contact ends — there is no additional universal renewal-delay penalty. The conservative reading is that the trail supplies a universal, externally readable local interaction state, while the 52/56 additive delays require the specific correlated creator-history reversal protocol studied in Y59–Y64; they are not intrinsic scalar properties of a trail in isolation.

**Interpretation.** Environmental memory in FBCL has (at least) two separable operational aspects — **readability**, which is universal and available to any compatible carrier, and **write/rewrite coupling**, which Y65 shows requires something beyond mere geometric passage. No physical-field interpretation is implied.

**Recommended next stage (Y66 — Read/Write State Correlation).** Construct two probes with the identical instantaneous local CD001 state at trail entry — same species, position, direction, and touching signature — but different histories: one creator-derived, one independently prepared. Compare them at the same trail edge to find the smallest enlarged state descriptor that predicts whether a crossing reads or rewrites.

### 10.1tt A minimal read/write discriminator is found: exact local causal age (Stage Y66)

Y66 aligns a creator-derived and an independent trajectory at the identical absolute position, direction, and R=7 CD001 touching signature, with the complete original trail support still bit-for-bit identical between them (16/16 primary + Tier-B alignment guards pass) — the strongest possible control that the later difference cannot be attributed to a different trail, encounter geometry, or damaged composite.

**One identical update later, the two states write different raw records** at the first affected trail vertex (relation symmetric difference 2, gate symmetric difference 2), even though their coarse CD001 signatures and the pre-existing trail remain otherwise aligned.

**The earliest measured distinction is exact local causal age.** Causal-age hop signatures already differ at $h=1$ in 16/16 contexts (24-record symmetric difference), but once every exact age label is replaced by an age-blind token, the $h=1$ neighborhoods become exactly identical in 16/16 cases — the unmatched records are the same 12 relation motifs, uniformly offset in birth age by **+1198** (positive-deposition histories) or **+1210** (negative-deposition), reproducible across the population. After that age erasure, a genuine age-blind structural difference remains, but only starting at $h=2$ (19 records for positive-deposition, 2 for negative-deposition, in every context).

**This refines what "read-only" means.** An independent probe can still make ordinary passage-driven raw changes in both target and matched-control environments; what stays unchanged is specifically the *target-minus-control* trail fingerprint. At the Y66 one-step fork, that target-specific fingerprint changes at 0 of 16 original support vertices for the independent branch, versus the already-established full rewrite (72/72 or 74/74) for the creator branch.

**A secondary repeated-reader diagnostic** confirms the trail is a reusable, non-destructive record: two independent readers sent through the same isolated trail (with the second launched outside the first's own preparation path) both get exact 80/82-round readouts with zero cumulative rewrite.

**Interpretation.** The coarse CD001 touching signature plus local trail geometry is not a complete dynamical state descriptor — two trajectories with identical species, position, direction, touching signature, and raw trail support can still produce different future updates. Exact local causal age is the earliest measured discriminator, but Y66 stops short of showing it is sufficient, since an age-blind difference also exists at $h=2$.

**Recommended next stage (Y67 — Selector-Level Causal Trace).** Instrument the exact Y66 pre-fork update at the level of the signed-v1 selector's legal-candidate enumeration and choice, to determine whether the fork reduces to a concrete ordering/comparison decision, and whether the 1198/1210 age displacement is itself the branch variable or merely correlates with one.

### 10.1uu The one-step fork is an identity-valued relation insertion, not a selector or ordering branch (Stage Y67)

Y67 decomposes the exact Y66 pre-fork update into legal-candidate enumeration, marker removal, grammar fire/support update, marker addition, and Q1 insertion, tracing creator and independent states through each phase.

**The selector never diverges.** In all 16 contexts there is exactly one legal forward candidate per constituent update — no tie to resolve — with identical chosen external old vertex and gate role form between creator and independent states. A longer 100-round, 3,200-update trace finds the same result throughout: **3,200/3,200** identical normalized candidate sets and choices, with candidate count exactly 1 in every case. There is no hidden selector-choice bifurcation anywhere in the traced crossing.

**The first raw difference appears only at Q1 insertion, and it is identity-valued, not structural.** Both histories insert the same role-level relation $T(c_2;\{f,c_4\})$ at the near trail vertex — e.g. creator `(6513, 2973, 6521)` versus independent `(7711, 2973, 7719)` — differing only in which specific post-vacuum vertex identities fill the same structural role. The gate's required ordering, $u{=}f < v{=}c_4$, is forced by the old-vacuum/new-vacuum partition itself ($f$ old, $c_4$ newly born) and **cannot be flipped** by the 1198/1210 causal-age offset Y66 measured.

**Interpretation.** Y67 falsifies a candidate-set explanation, a random-tie explanation, a chosen-gate explanation, a local $u<v$ flip caused by the absolute age displacement, and any later selector divergence within the traced 100-round horizon. Exact causal age remains an excellent lineage/history marker — the earliest measured feature separating the two preparations — but its absolute value is not itself the mechanism. The decisive read/write difference must involve the larger correlated history state in which the otherwise-identical Q1 event is embedded, which makes the still-unexplained age-blind $h=2$ structural difference the nearest remaining candidate.

**Recommended next stage (Y68 — h=2 Recomputation-Closure Trace).** Trace the age-blind $h=2$ difference directly into the simulator's actual `_aff()`/`_gf()` recomputation machinery, to determine whether and when it participates in a successful gate-generation witness, rather than searching a yet larger radius.

### 10.1vv The h=2 lineage difference is dynamically real but not the universal fork cause (Stage Y68)

Y68 traces the age-blind $h=2$ difference through every operation of the frozen 100-round crossing, distinguishing three event levels: a **closure-source hit** (a differing relation enters an operation's recomputed-source set), a **successful `_gf()` hit** (it is actually used in a gate-generation witness), and a **normalized gate consequence** (the recomputed gate sets differ after identities are erased).

**The channel is real but sign-dependent and non-universal.** On the positive-deposition branch, an independent-only $h{=}2$ relation is used in 5 successful gate-generation witnesses at round 1 (constituent A, marker removal), producing a genuine normalized gate difference of 2 — in all 8/8 contexts. On the negative-deposition branch, an $h{=}2$ difference enters a recomputation closure but is used in **zero** successful `_gf()` witnesses across the entire 100-round trace, in all 8/8 contexts.

**At the actual Q-fork operation itself, $h{=}2$ plays no role at all:** 16/16 contexts show zero $h{=}2$ closure hits, zero successful-gate dependencies, and an exactly-equal normalized recomputed gate set. The raw Q-inserted relations still differ, as Y67 established, but only in identity labeling, not through any $h{=}2$-mediated recomputation.

**A temporal-causality check rules out necessity outright.** The first $h{=}2$ recomputation event occurs before the Q fork in 8 of 16 contexts (under AB scheduling) and after it in the other 8 (under BA scheduling), with the fork itself unaffected either way — a mechanism that occurs *after* its supposed effect in half the tested schedules cannot be its universal cause.

**Interpretation.** The most conservative statement after Y66–Y68 is that the first universal creator/independent difference remains the identity-valued Q1 insertion itself; the causal-age and age-blind $h{=}2$ lineage differences are real, correlated surrounding history — with genuine but sign-specific and non-necessary effects on background recomputation — but neither supplies the universal write/read switch. This sharpens the open question to a representational one: how much of the apparent fork is raw post-vacuum identity labeling versus a genuine order/topology-class difference.

**Recommended next stage (Y69 — Order-Isomorphism / Identity-Gauge
Audit).** Construct a canonical representation of creator and independent states that retains old-vacuum geometry, relative causal/birth ordering, relation/gate topology, and carrier roles, while quotienting away arbitrary absolute post-vacuum integer identities; trace both histories phase-by-phase from the Y66 pre-fork state through the full crossing to locate the first point at which they cease to be equivalent under that canonicalization. This will distinguish a pure identity-labeling artifact in the initial Q-insertion fork from a genuine order-sensitive invariant not captured by the present age-blind normalization, before any legal-intervention sufficiency test is attempted.

### 10.1ww The raw Q/trail fork is gauge (identity-only); the real non-gauge difference is pre-existing h=2 structure (Stage Y69)

Y69 applies a strictly stronger quotient than Y66–Y68's age-erasure: an order-preserving canonicalization that keeps old-vacuum geometry, carrier/marker roles, Q ownership, and full relative birth order, while replacing every arbitrary absolute post-vacuum integer ID with its rank.

**The raw Q1 fork disappears under this quotient.** In all 16 contexts, creator and independent states are exactly order-isomorphic at $h{=}1$ both before and after Q1 insertion, and remain order-isomorphic at $h{=}1$ throughout the entire frozen 100-round crossing (101/101 sampled rounds, 16/16 contexts). Even more strikingly, the complete original isolated-trail support — whose raw records the parent stages showed diverging from round 1 onward — remains order-canonically equivalent between creator and independent histories through all 100 rounds, in 16/16 contexts. The Q1 insertion is therefore an identity-valued raw fork, not a local order/topology fork.

**But the histories are not globally gauge-equivalent.** A genuine, cardinality-level non-isomorphism already exists at $h{=}2$, *before* Q1 fires: the creator and independent $h{=}2}$ neighborhoods differ in post-vacuum vertex count by exactly $\pm1$ (61 vs. 62 for positive deposition, 61 vs. 60 for negative), with population-invariant canonical relation/gate symmetric differences (204/7 and 186/5 records respectively). Because the vertex counts themselves differ, no relabeling — order-preserving or otherwise — can equate the two $h{=}2$ sets. This structural difference was already shown in Y68 not to be the universal Q-fork cause; Y69 now additionally shows it is a genuine (non-gauge) state, just not one that explains the fork by itself.

**Interpretation.** Absolute Q/trail integer identities are locally gauge-like and should not be read as a newly generated physical-state distinction. The real open structure is the pre-existing $h{=}2$ asymmetry, and the operational question becomes whether the creator-write / independent-read distinction survives when defined entirely in gauge-invariant variables.

**Recommended next stage (Y70 — Gauge-Invariant Rewrite Audit).** Re-audit the Y64–Y66 environmental-memory results — the isolated trail, the transformed multi-history corridor, and the independent-reader crossing — using the same order-preserving quotient, to determine whether creator passage changes a gauge-invariant target-minus-control state while independent passage does not, and whether Y64's 19/30-coordinate corridor split survives the quotient or was partly raw-identity bookkeeping.

### 10.1xx The 19-coordinate entry extension is pure gauge; the 30-coordinate exit extension is genuine, and alone reproduces the observed timing (Stage Y70)

Re-auditing the Y64 multi-history corridor and the Y65 independent-reader crossing under the Y69 order-preserving quotient produces a substantially cleaner picture, formally classified `gauge_invariant_write_read`.

**The corridor asymmetry simplifies.** Under the gauge quotient, the creator multi-history corridor's 19-coordinate entry-side extension **disappears completely** — 0 gauge coordinates beyond the isolated-template entry edge in every one of 32 scored cases — while the 30-coordinate exit-side extension survives exactly, contiguous, with no missing isolated-template coordinates. The resulting gauge-support lengths (126/128/180/182 for the four sign/history combinations) are exactly what Y64 had to define empirically as its "active corridor," and convolving them with the CD001 footprint reproduces the frozen Y63/Y64 interaction durations (134/136/188/190) exactly — with no separate directional-kernel rule required. The Y64 active-corridor construction and the Y70 gauge-invariant corridor turn out to be the same object.

**The surviving extension is a genuinely different ordered environment, not a labeling residue.** Whole-corridor canonical relation/gate symmetric differences between the creator corridor and a fresh control remain large and sign/history-specific (e.g. 1524/8 records for the shortest case), confirming the 30-coordinate extension reflects real relational structure.

**The independent-reader non-destructiveness result survives the same quotient.** For all 16 strict untouched-side crossings, the gauge-invariant target-minus-control trail fingerprint is unchanged before and after crossing — 0/16 cases show any change once the target-minus-control difference is formed first and *then* canonicalized (an initial, less careful diagnostic that canonicalized each arm separately produced spurious rank-shift artifacts and was corrected before scoring).

**Interpretation.** The operational read/write distinction is not an artifact of arbitrary vertex numbering: an unrelated probe leaves the same gauge-invariant environmental memory before and after passage, while creator-history return genuinely extends a gauge-invariant corridor by 30 coordinates on the exit side. The former 19-coordinate "inactive" extension is retired from the physical-within-model mechanism as pure gauge structure.

**Recommended next stage (Y71 — Gauge-Extension Genesis / Dwell-Sweep
Trace).** Rather than intervening on an arbitrary $h{=}2$ witness, trace the creator-derived second reversal step by step to find the exact operation that first creates a gauge-invariant coordinate beyond the isolated-template exit edge, and follow its causal ancestry and later propagation.

### 10.1yy The environmental-memory mechanism resolves completely: history delays the lifecycle, and dwell alone sweeps the corridor (Stage Y71)

Y71 finds that the Y70 gauge corridor is not generated by any special rewrite behavior at all. It is the ordinary single-turnaround trail, swept through exactly the extra reverse-v1 displacement created by the already-established renewal delay:

$$L_{\text{gauge}} = L_{\text{isolated,current}} + \Delta H,$$

holding exactly, with no fitted spatial parameter, in all 32 scored two- and three-history primary and Tier-B cases (e.g. a 74-coordinate current trail swept through a 52-round delay gives exactly the Y70 gauge-support length of 126; a 72-coordinate trail swept through an accumulated 108-round delay gives exactly 180). The historical endpoint trail is displaced from the trail an equivalent fresh, no-prior-history reversal would deposit by exactly $\Delta H$ coordinates, in the reverse-v1 travel direction, in 32/32 cases; the swept union of every integer translation between those two endpoints reproduces the complete Y70 gauge support exactly, missing or extra coordinates in 0/32 cases.

**A direct forced-dwell intervention confirms the mechanism causally, not just numerically.** A fresh CD001 with *no* prior trail, started at the same reversal boundary but deliberately held in reverse-v1 for exactly the historical dwell duration before being allowed to accelerate, produces exactly the same final gauge-support set as the true historical creator in all 16 tested contexts; historical-creator-minus-forced-control leaves exactly the original single trail (72 or 74 coordinates) in every case. Prior environmental history therefore does not need a special local "write opcode" — its entire operational role is to delay the lifecycle transition out of reverse-v1, after which ordinary continued translation sweeps the same trail pattern across additional coordinates. A representative genesis trace confirms this directly: the extra-support count grows by exactly +1 per round, for exactly $\Delta H$ rounds, with no round contributing more than one coordinate.

**This retires the earlier "30-coordinate" framing.** Y71 shows 30 was never a primitive constant — it was simply what protrudes beyond the specific Y63/Y64 endpoint-template union once most of the dwell-swept corridor is found to overlap that union. The real invariant is the increment law $\Delta L_{\text{corridor}} = \Delta H_{\text{renewal}}$, unifying the Y59 temporal-memory law and the Y70 spatial gauge law into a single mechanism: **environmental history controls how long the creator continues writing (via lifecycle delay), not which local rewrite law it uses.**

**This is a natural stopping point for the environmental-memory branch.** The isolated-trail geometry is known exactly, third-party readability is established, gauge artifacts have been separated from genuine ordered-state support, multi-history spatial growth is now derived (not merely fit) from the renewal delay, and a forced-dwell intervention reproduces the spatial support with no prior history at all. Y71 explicitly recommends pausing this branch here — an open microscopic question (why environmental contact delays the lifecycle certificate in the first place) remains available for later, but is no longer a prerequisite for interpreting the corridor geometry.

**Recommended next priority: return to the deferred recurrence-energy population (Section 11, priority (b)).** With the environmental-memory branch brought to a clean, unified close rather than left open, Y71 recommends resuming the parallel path deferred since roughly Y53 — reconstructing the recurrence-energy population directly under FBCL, obtaining at least six genuinely distinct single-carrier species, measuring $E_{0,i}$ and $M_i$, and testing $M_i=\alpha E_{0,i}$. That path needs neither G6 nor a stationary composite rest state, and is the first route to testing the paper's central proportionality claim against a real population rather than one reference carrier.

### 10.1zz A much deeper energy-blind search still finds exactly one FBCL single-carrier species (Stage Y72)

Y72 restarts the Section 11(b) population program under the unchanged FBCL law, deliberately blind throughout to recurrence energy, inertial curvature, and any other candidate observable — no $\ell_0$, $R_{\text{action}}$, $\omega_{\text{renew}}$, $E_0$, $A_{\text{dir}}$, $M_i$, or $\alpha$ is inspected at any point in this stage.

**The final normalized global launch sweep is far larger than Y50–Y53's original search.** Using the frozen Y51 both-sign algebraic first-gate screen with a fixed seed, 250 distinct screen-passing age-ordered launch masks are sampled at each relation count $k=5$ through $28$ (exhaustive at $k=29$ and $k=30$, where only 30 and 1 masks respectively exist), giving 6,031 sampled masks in total. Of these, 157 support exact four-sector recurrent transport — and **every single one** converges to the same period-1 dressed species already identified at Y50–Y53 (species key `ec93774039a328fa47fe`; DS001 core class inherited from Y51; halo sizes $42,42,44,44$; one live Q and one marker per sector). No period-2-through-16 survivor appears anywhere in the sweep, and the densest sampled strata ($k=26$–$30$) produce **no** recurrent survivor at all.

**The mature dressed state itself was also perturbed directly, exhaustively where feasible.** All $60\times9=540$ possible one-relation carrier/environment decorations were seeded: 517 remain four-sector recurrent, and all 517 converge to DS001. The 23 decorations that fail were then paired exhaustively — all $\binom{23}{2}=253$ unordered pairs — and **none** produces a valid recurrent carrier; the exceptional defects interact destructively rather than stabilizing a hidden excitation. All 30 possible marker/interface excitations were seeded and all 30 remain recurrent, all converging to DS001. A 500-pair deterministic sample from the full two-decoration space gives 454 recurrent carriers, again all DS001.

**Interpretation.** Combining the sweep and the censuses, well over a thousand independently-generated recurrent trajectories were tested across this stage, and not one produced a second species. This substantially strengthens, rather than merely repeats, the Y50–Y53 conclusion — the attractor persists across relation counts spanning more than an order of magnitude, across direct perturbation of the mature dressed state, and across exhaustive pairing of every structural exception found. Y72 is explicit that this is not evidence FBCL admits only one species in *every* enlargeable state space — it is evidence that **five-role launch/dressing diversity specifically is not the missing population mechanism**, which reframes rather than closes the population question.

**Recommended next stage (Y73 — Enlarged Single-Carrier Ontology).** Rather than continuing to resample the five-role launch/dressing space, search for a genuinely larger single-carrier construction under the unchanged FBCL law — a six-role carrier or a carrier-plus-bound-satellite excitation — requiring one connected translation center, no decomposition into two independently propagating DS001 cores, an additional persistent role or halo excitation that renews with the carrier, exact four-sector transport, and bounded dressed recurrence. Discovery should remain blind to $E_0$ and $M_i$ as before; once $\ge6$ distinct species exist, the population branch should proceed immediately to same-law recurrence-energy reconstruction, independent Y47-style curvature measurement, and a frozen development/holdout fit of $\alpha$.

### 10.1aaa A passive bound sixth role is exhaustively ruled out; DS001 is an attractor in six-role dressing space too (Stage Y73)

Y73 tests the most direct enlargement of the single-carrier ontology: attach a sixth persistent post-vacuum role to DS001 as a **passive bound satellite**, while the ordinary five-role kernel continues to drive translation, and see whether it survives as a genuinely new dressed state. Recurrence-energy and inertial observables remain completely sealed throughout.

**The baseline is established first.** A settled DS001 carrier, profiled in all four moving sectors, has exactly **three** post-vacuum vertices incident on its carrier-touching halo, beyond the five core vertices and the marker. Y73 therefore requires any passive-satellite candidate to retain at least a **fourth** such vertex after a 16-event burn-in — a lossless necessary filter for this ontology.

**The search is large and exhaustive within its scope.** Two complementary constructions were tried: a sixth role born fresh at launch and coupled only to the five carrier roles (all 1-, 2-, and 3-relation attachments, both marker birth orders: $60+870+8{,}120=9{,}050$ seeds), and a sixth role inserted into an already-settled DS001 carrier and coupled to carrier roles plus a nearby old-vacuum vertex across offsets $-4$ through $+4$ ($100{,}825$ enumerated specs, $74{,}900$ valid after rejecting $25{,}925$ specs where the old-vacuum role collided with a current core vertex). Combined: **109,875 seed specifications, 83,950 valid distinct-role geometries.**

**Every single one collapses back to the DS001 baseline.** Zero of 83,950 valid seeds retain a fourth post-vacuum halo vertex after the checkpoint; every executable case returns to exactly three. No candidate reaches full four-sector validation, so the single-carrier FBCL population remains exactly one species.

**Interpretation.** This substantially strengthens, and structurally complements, Y72's finding: DS001 is not merely an attractor in five-role launch/dressing space — it is also an attractor in simple six-role *dressing* space. The dynamics either absorb or export any added passive support back down to the ordinary halo count. But Y73 is careful that this null is ontology-specific: it holds the active five-role kernel fixed and asks only whether an extra role can remain passively bound around it. It does not test a six-role carrier whose active five-role *subset itself rotates or exchanges membership* during recurrence — a structurally different possibility that remains untested.

**Recommended next stage (Y74 — Role-Exchange Six-Vertex Carrier).** Search a connected six-vertex support pool in which only five vertices form the active FBCL kernel at any given event, but membership in that active quintet can change from one native grammar fire to the next (no added cleanup rule). A valid species requires one connected support pool and translation center, no decomposition into two independent DS001 cores, deterministic grammar-driven role exchange, exact four-sector transport, recurrent six-role dressed state (period $\le16$ initially), and deduplication under role permutation and cycle rotation — with discovery kept blind to $E_0$ and $M_i$ as before. This is the first remaining route that changes carrier ontology dynamically rather than attaching transient structure to the fixed DS001 kernel.

### 10.1bbb Stages Y74–Y75 extend the dynamical role-exchange null across the full six-role state space

*The complete Y74 and Y75 stage packages were not available when this section was drafted; the summary below is limited to what Stage Y76's own frozen record states about them, and should be read as provisional until the underlying packages are reviewed directly.*

Y76's record indicates that Y74 implemented the role-exchange (rather than passive-satellite) six-role ontology Y73 left open — a connected six-vertex support pool in which the active FBCL quintet's membership can shift via the native grammar's own handoff, with no added cleanup rule — and that Y75 then extended this to a **global** six-role launch-topology census spanning the full density range, analogous in scope to Y72's five-role sweep. Y76 refers to this jointly as "Y75's global six-role null": both stages are stated to have found that every recurrent six-role construction tested still matures into the ordinary DS001 signature, with no second species surviving at any tested density. This is consistent with, and directly continuous with, the pattern established by Y72–Y73 and continued by Y76 below.

### 10.1ccc A native seven-role overlapping-kernel census still returns only DS001, and the branch is formally handed to a discussion gate (Stage Y76)

Y76 enlarges the single-carrier ontology once more, this time to a **native** seven-role object rather than an attached or exchanging one: for any settled carrier, the union of two consecutive active FBCL quintets, $S_t \cup S_{t+1}$, contains exactly seven vertices — the five roles active at $t{+}1$ plus the two roles the native handoff just retired. No manual role swap or added rule is introduced; this transition pool is simply what the unchanged grammar already produces.

**The census is global and large.** 4,951 causal-age seven-role launch masks are sampled across every internal relation-count stratum $k=6$ through the unique fully saturated $k=105$ state (50 masks per stratum, the single available mask at $k=105$), each required to support exact four-sector transport with the seven-vertex transition union holding at every measured event. **291** launches achieve complete four-sector recurrence, and **all 291** exactly match the independently measured DS001 four-sector transition-pool signature (period 1 in every sector; dressed halo sizes 42/42/44/44; 13/13/12/12 seven-pool internal relations). Recurrent survivors appear in 91 of the 100 sampled strata — the search finds *plenty* of recurrent launch basins, they just all lead to the same place. A post-specified translated-site diagnostic (24 contexts at 6 representative densities, replayed at two independent sites) finds the same pattern: sparser launches transport more robustly across sites, denser ones are more context-sensitive and often fail to mature at all, but whenever a translated case *does* mature, it is DS001.

**Interpretation and a deliberate pause.** Y76 explicitly declines to auto-escalate to an eight-role census. With five structurally distinct enlargement axes now tested (five-role launch density, one/two-relation dressed excitations, passive sixth-role satellites, six-role role-exchange, global six-role launch topology, and now native seven-role overlapping kernels) all collapsing to the identical single attractor, Y76 treats the pattern as strong enough to warrant a **theoretical interpretation checkpoint** before further search budget is spent, and explicitly hands off to discussion rather than freezing a Y77 protocol of its own. It notes — carefully, as a computational finding over the tested state spaces rather than a proof — that larger *elementary-carrier* support is not producing a species spectrum, and raises the open question of whether diversity should be sought in launch/support topology at all, or whether the population premise itself needs reframing.

### 10.1ddd DS001 bonding topology produces the first genuine FBCL species spectrum (Stage Y77)

Y77 is the direct response to Y76's discussion gate, and it changes the search ontology rather than escalating it: instead of searching for a second *elementary* carrier, it treats DS001 itself as a candidate elementary FBCL constituent and searches for recurrent **bound states of multiple DS001 copies**. Discovery remains completely blind to $E_0$, $M_i$, $\alpha$, and every other candidate observable throughout.

**A natural census (no seeded bond) rediscovers CD001 and finds it composes further on its own.** Scanning separations $R=5$–$20$ across all 16 sector pairs, both update orders, and both tie seeds (1,024 cases) reproduces exactly the known CD001 family — 8 passes, all at $R{=}7$, same-sign $v_2$ — confirming no other natural dimer bond exists in this population. But scanning adjacent-pair separations for **three**-body chains (4,800 cases) finds 24 passes, every one an $R{=}7/R{=}7$ open chain $A\!-\!B\!-\!C$ with no $A$–$C$ bond — the natural CD001 bond composing spontaneously into a trimer. A further four-body scan (2,592 cases) finds 48 passes, all the natural $7\!-\!7\!-\!7$ open chain — the bond composing a third time, again unforced. Both the trimer and tetramer replicate exactly (48/48 and 96/96) across translated sites, signs, update orders, and ties, and survive 120-round stress tests.

**A deliberate bond-topology atlas then finds two entirely new dimer species.** Seeding one cross-relation between two DS001 cores at every core-role pair, every old-vacuum offset $-4$ to $+4$, both source orientations, separations $R=5$–14, and both $v_2$ signs (9,000 seeds) finds recurrent connected survivors only at $R{=}5$ (39), $R{=}6$ (32), and $R{=}7$ (48, all relaxing to ordinary CD001 — no new $R{=}7$ species). The $R{=}5$ and $R{=}6$ survivors are genuinely new, structurally distinct bond species — not compressed or relabeled CD001 — confirmed by 16/16 replication each across signs, update order, ties, and two translated centers: **D2R5** has four persistent cross-core relations in its mature bond; **D2R6** has three (including a post-vacuum-age component); **CD001** has exactly one.

**The three bond types then compose combinatorially into a same-constituent-number spectrum.** A post-specified extension (documented and hashed before execution, since the R=5/R=6 discovery could not have been anticipated) tests all ordered adjacent bond-pair combinations from $\{5,6,7\}^2$ (216 cases): **six** of the nine possible pairings pass all 24 discovery contexts — `T3R65, T3R66, T3R67, T3R75, T3R76, T3R77` — while the three pairings starting with an R=5 bond (`5-5, 5-6, 5-7`) do not form in this causal construction (Y77 flags this directional asymmetry as real but declines to interpret it as chirality or any other intrinsic property without further work). All six geometries replicate exactly (288/288 across sites/signs/orders/ties, 24/24 in 120-round stress tests), and their mature cross-relation counts are exactly compositional from the underlying bond motifs (e.g. `T3R65` is 3+4, matching the R=6 and R=5 bonds' individual counts) — direct evidence the three-body species are built from reusable bond motifs rather than being unrelated monolithic attractors. A dedicated attempt to close the natural $(7,7)$ trimer into a triangle (seeding an $A$–$C$ relation, 1,800 cases) fails completely: the 16 surviving cases all relax back to the ordinary open-chain signature with zero $A$–$C$ structure.

**The resulting frozen spectrum has ten structural candidates, with genuine same-$N$ diversity:**

| label | DS001 count | geometry | formation | mature bond structure |
|---|---:|---|---|---|
| D2R5 | 2 | R=5 | seeded | 4 cross relations |
| D2R6 | 2 | R=6 | seeded | 3 cross relations |
| CD001 | 2 | R=7 | natural | 1 cross relation |
| T3R65 | 3 | 6-5 | seeded mixed chain | 3 + 4 |
| T3R66 | 3 | 6-6 | seeded mixed chain | 3 + 3 |
| T3R67 | 3 | 6-7 | seeded mixed chain | 3 + 1 |
| T3R75 | 3 | 7-5 | seeded mixed chain | 1 + 4 |
| T3R76 | 3 | 7-6 | seeded mixed chain | 1 + 3 |
| T3R77 | 3 | 7-7 | natural | 1 + 1 |
| T4R777 | 4 | 7-7-7 | natural | three adjacent R7 bonds |

Three distinct dimer (N=2) species and six distinct trimer (N=3) species means a later mass-energy comparison is not forced into the trivial statement that both quantities merely increase with constituent count — there is real structural diversity to test at fixed $N$.

**Interpretation.** Y72–Y76 established, cumulatively and rigorously, that enlarging the *elementary* carrier's own support does not produce a species spectrum. Y77 establishes the complementary result: DS001 plus reusable bonding topology *does*. The suggested working ontology is now: vacuum grammar → DS001 elementary constituent → reusable bond motifs → composite species spectrum. Y77 is explicit that this is a structural conclusion inside the FBCL simulation, not a claim of correspondence with DS001 as a genuine physical fundamental particle or with any Standard Model species.

**The structural multiplicity threshold (≥6 distinct candidates) is now exceeded — but the inertial population gate is not.** These ten candidates have validated $+v_2/-v_2$ transport only; none has yet been shown to possess a stationary rest state or complete $+v_1/-v_1$ manifolds the way DS001 and CD001 required extensive separate work (Y42–Y53, Y54–Y71) to establish. $E_0$, $M_i$, and $\alpha$ remain completely unopened.

**Recommended next stage (Y78 — Composite Kinematic/Lifecycle Closure).** Do not discover further species. Instead: (1) test D2R5, D2R6, and CD001 under $\pm v_1$ and stationary-rest constructions without changing FBCL; (2) test all six N=3 chain species under $\pm v_1$, determining whether their bond motifs survive, factorize, or transform; (3) only once moving-sector behavior is understood, search for stationary recurrent rest lifecycles; (4) require at least six species with complete $0,\pm v_1,\pm v_2$ manifolds before opening the Y5/Y47 measurement machinery; (5) once mass-ready, reconstruct FBCL recurrence energy independently and fit one global $M_i=\alpha E_{0,i}$ relation with held-out species; (6) report both total values and binding residuals $\Delta E_0$, $\Delta M_i$ relative to $N$ independent DS001 constituents, so constituent-count extensivity alone cannot masquerade as the central result.

### 10.1eee Four composite species close a two-speed moving manifold; stationary rest remains the isolated bottleneck (Stage Y78)

Y78 tests whether the Y77 composite spectrum survives deceleration from $v_2$ into $v_1$, and then whether any species can reach a genuine stationary rest lifecycle. Energy and inertia remain blind throughout.

**The $v_2\to v_1$ closure splits the spectrum sharply, along bond composition.** All nine dimer/trimer Y77 species are tested across every sign, constituent update order, and tie. **D2R5, D2R6, T3R65, and T3R66 pass exactly** — 8/8, 8/8, 24/24, and 24/24 contexts respectively, every passing sector exact-speed, connected, and period-1. **Every species containing an R7 (CD001-type) bond factorizes** — loses composite connectivity — at the settled $v_1$ boundary: CD001 itself (0/8) and all four R7-containing trimers (T3R67, T3R75, T3R76, T3R77; 0/24 each). Only T3R77, built from two R7 bonds, and the three mixed R7 chains fail; every chain built purely from R5/R6 bonds survives.

**The bond itself is speed-dependent, not a fixed graph.** The mature $v_1$ bond differs from the mature $v_2$ bond: D2R5 keeps its four cross-relations at both speeds, but D2R6's bond genuinely transforms — three cross-relations at $v_2$, only one at $v_1$. A direct-$v_1$ control (seeding the frozen R5/R6 motifs straight into already-settled $v_1$ DS001 pairs, bypassing any deceleration history) reproduces both results exactly (8/8 each), while the same direct seeding of an R7 bond fails completely (0/8) — the canonical CD001 relation requires an old-vacuum site that the settled-$v_1$ causal geometry doesn't offer. This confirms R5/R6 have genuine, independent $v_1$ bond sectors, while the R7 bond is specifically tied to $v_2$'s interface geometry.

**No stationary rest state is found for any of the four moving-complete species.** Starting each in settled $+v_1$, Y78 exhausts every $\pm$ sign turnaround word of length 2–6 (62 words per species, using the established Y56 turnaround operation), scoring actual measured macro displacement rather than assuming sign-balance implies rest. Per species, the split is identical: 41 non-executable words, 16 that execute but drift, and **5 that achieve exactly zero net displacement yet still fail to reach a recurrent composite dressing state**. That last category is the important one — it shows the rest failure isn't simply "the bond breaks under reversal," but that even trajectories with genuinely zero net motion can still accumulate or transform environmental dressing that never settles into an exact cycle.

**A methodological firewall, not a shortcut.** The established monomer stationary-rest construction (the augmented Y46 delayed-retirement lifecycle, with its phase-specific legal retirement operations) was not present in the recovered Y54–Y77 composite packages. Rather than reconstruct it from prose description or approximate its cleanup rules — which could produce a false-positive stationarity result — Y78 explicitly declines to test composite rest until the exact Y46 executable is recovered or rebuilt from source.

**Interpretation.** Y78 strengthens rather than weakens the Y77 picture: R5 and R6 are not just additional species labels, they are qualitatively more capable bond motifs that determine which velocity sectors a composite can occupy — R7 is a $v_2$-only bond, R6 transforms across speeds, R5 is speed-invariant. Bond topology, not merely constituent count, controls kinematic accessibility. But the population remains formally at zero mass-ready species: four now have complete moving ($\pm v_1,\pm v_2$) manifolds, five R7-containing composites are confirmed $v_2$-only, and none has a stationary rest sector.

**Recommended next stage (Y79 — Exact Y46 Rest-Lifecycle Transfer).** Recover or rebuild the exact frozen Y46 delayed-retirement rest executable from original source; independently reproduce monomer Y46 G3S with it before any composite modification; instantiate two Y46-rest DS001 constituents at the R5 and R6 geometries and test the frozen Y77 bond motifs without retuning; if the dimers close, propagate to T3R65/T3R66; audit full carrier+bond halo recurrence and scheduler stationarity, not merely zero displacement; require at least six species with complete rest + $\pm v_1,\pm v_2$ manifolds before opening the recurrence-energy/inertial-curvature population program. If R5/R6 bonds cannot coexist with exact Y46 rest, the mass-energy program will need either a different rest construction or a structural reformulation of what constitutes the zero-momentum composite sector — a decision Y79 should make explicitly, before any $E_0$ or $M_i$ value is inspected.

### 10.1fff Exact Y46 stationary rest transfers to four composite species — the first complete 0,±v1,±v2 manifolds outside the elementary carrier (Stage Y79)

Y79 resolves the bottleneck Y78 isolated. Discovery remains blind to $E_0$, $A_{\text{dir}}$, $M_i$, and $\alpha$ throughout.

**The exact historical executable is recovered and re-certified before any transfer is attempted.** The archived Y46 package is pulled from the project library; a single packaging-only import fix (a missing `HERE = Path(__file__).resolve().parent` before an existing `sys.path.insert`, no scientific code touched) is needed to run it. Replayed as-is, it reproduces its historical result exactly: **96/96** primary stationary periods and **1200/1200** population periods, zero drift, zero local halo source, exact phase/gate/Q/marker and full-halo-graph recurrence. This control has to pass before any composite result counts — and it does, unchanged.

**The acceptance bar for a composite is deliberately stronger than "each constituent is individually at rest."** A scored period must show, jointly: zero midpoint displacement for every constituent, fixed relative coordinates, a connected interaction graph, frozen bond-edge counts, exact local phase/gate/Q/marker recurrence, exact isomorphism of the complete *joint* carrier-halo graph, and constant joint-halo cardinality — so a constituent that is locally recurrent but sits inside a slowly drifting joint wake is still rejected.

**R6 transfers natively — no new physics required.** D2R6 closes immediately under the unmodified Y46 lifecycle, with a mature rest geometry of one persistent cross-relation at $R{=}6$ (matching its already-reduced $v_1$-sector bond). Confirmatory population: **16/16** contexts, **800/800** stationary periods, joint halo exactly 99 relations throughout. The same bond composes directly into T3R66 (relative coordinates $(0,6,12)$, one cross-relation per adjacent edge): **48/48** contexts, **1440/1440** periods, joint halo exactly 157.

**R5 exposes one genuine residual effect — and Y79 traces it to an exact, principled fix rather than patching around it.** Raw (unmodified) Y46 transfer leaves D2R5 looking almost stationary — both centers return exactly, separation stays $R{=}5$, all four bond relations persist, local phase/gate/Q state recurs — but the complete joint halo grows by exactly **+1 relation per eight-event rest period**. Provenance work identifies the extra relation precisely: it is the spatially leading constituent's own event-3/output-7 scaffold, which at $R{=}5$ specifically (and only at that separation) happens to land incident on the trailing neighbor, so a fresh copy stays attached every cycle instead of retiring as it normally would in isolation. A causal-lifetime audit — replaying the trajectory while deleting the identified relation at successive checkpoints — finds the first timing that is safe in *every* tested sign/order context: **immediately after the same creator completes event 4**. Freezing that one derived, causally-timed retirement (and nothing else — no bond relation removed, no vacuum-grammar change, no bulk historical scrub) closes D2R5 exactly: **16/16** contexts, **800/800** periods, joint halo exactly 97, four persistent cross-relations preserved. The same retirement composes into T3R65 (relative coordinates $(0,6,11)$, mixed R6/R5 edges): **48/48** contexts, **1440/1440** periods, joint halo exactly 155.

**Combined confirmatory result across all four species: 128/128 contexts, 4480/4480 stationary periods — zero scored period shows drift, geometry change, disconnection, local-invariant failure, halo-isomorphism failure, or joint-halo flux.**

**The full speed-dependent bond picture, now closed across all three kinematic sectors:**

| bond | $\lvert v\rvert=2$ | $\lvert v\rvert=1$ | $0$ (rest) |
|---|---:|---:|---:|
| R5 | 4 | 4 | 4 |
| R6 | 3 | 1 | 1 |

R5's four-relation bond is exactly speed-invariant across the complete manifold; R6's bond is genuinely velocity-dependent at $v_2$ but settles to its reduced one-relation form for both $v_1$ and rest.

**Species/gate accounting after Y79.** **D2R5, D2R6, T3R65, and T3R66** are now mass-ready *at the structural level* — they have validated, recurrent $0,\pm v_1,\pm v_2$ manifolds — though "mass-ready" here means only that the kinematic manifold is complete, not that inertial curvature has been measured. Y79 is careful to state the population accounting precisely: **$N_{\text{mass-ready,composite}}=4$**, but since DS001 itself already has a complete manifold and a valid Y47 curvature under the same law, **$N_{\text{mass-ready,same-law}}=5$** once the elementary carrier is counted. The $\ge6$ premeasurement firewall therefore needs exactly **one** more same-law complete-manifold identity (or two more if the eventual population is restricted to composites only, to avoid the fit depending on counting the elementary constituent). G6 itself is still not tested for these composites, since their $A_{\text{dir}}$ curvature has not yet been measured — that comes only after the population is frozen.

**Interpretation.** Y79 shows the stationary sector does not require inventing a new rest mechanism per composite: every constituent runs the identical Y46 lifecycle; R6 is natively compatible with it; R5 introduces exactly one additional, causally well-defined finite-lifetime scaffold with a single covariant delayed retirement; and both bond laws compose cleanly into three-body chains. This strengthens the working architecture: DS001 constituent + bond/interface topology → composite species lifecycle, entirely within the unchanged FBCL law.

**Recommended next stage (Y80 — R5/R6-Only N=4 Chain Species).** The rest mechanism is now understood; Y80 should not search for another rest mechanism. Instead: discover or reconfirm a $v_2$-recurrent four-body R5/R6-only chain topology; test its $v_1$ bond reduction; apply the exact Y46 rest lifecycle to every constituent; apply the frozen R5 event-3/output-7 retirement independently on every R5 edge present; require full joint-halo recurrence. One additional complete-manifold species is sufficient to clear the $\ge6$ same-law firewall when DS001 is counted, but obtaining at least two is preferable so the eventual development/holdout population fit doesn't depend on counting the elementary constituent. Only once that population is frozen should the recurrence-energy and inertial-curvature measurement program reopen.

### 10.1ggg R5/R6 bonds compose into three complete four-body species — the population firewall is crossed (Stage Y80)

Y80 tests the next compositional prediction of the DS001-bond picture directly: do the already-frozen R5/R6 bond motifs, with no new rule of any kind, extend to four-constituent chains? Discovery stays blind to $E_0$, $A_{\text{dir}}$, $M_i$, and $\alpha$ throughout, and two protocol amendments (a v1-burn window extended from 16 to 24 rounds after the first 666 harness run showed the shorter window undercounted a genuine formation transient, and a stronger order-preserving halo certificate substituted for a slow graph-isomorphism check) are both frozen before the global population runs and both make the acceptance criterion stricter, not weaker.

**All eight ordered R5/R6 triples are tested; exactly three become complete species.** Across the full `{5,6}` geometry space (`555, 556, 565, 566, 655, 656, 665, 666`), each scored on 96 moving contexts (both signs, all 24 constituent update orders, both ties), **T4R656, T4R665, and T4R666** pass all 96/96 moving contexts with exact period-1 $v_2$ and settled period-1 $v_1$ recurrence. The five failures are uniform and total: every geometry beginning with an R5 bond (`555, 556, 565, 566`) fails 0/96 because the first R5 seed is invalid in every context, and `655` fails 0/96 because its third bond seed is invalid — the same causal-orientation asymmetry already seen at $N{=}3$, still not interpreted as chirality.

**All three transfer to stationary rest with no new cleanup rule.** Using the unmodified Y46 lifecycle plus the already-derived Y79 R5 event-3/output-7 retirement (applied independently to every R5 edge present) closes all three species outright: **288/288** discovery contexts and **5,760/5,760** stationary periods at the discovery center, then **144/144** contexts and **2,880/2,880** periods under translated-site promotion. Combined: **432/432 contexts, 8,640/8,640 periods, zero exceptions.**

**Bond compositionality survives the jump to $N{=}4$ without modification.** R5 stays a four-relation bond across $v_2$, $v_1$, and rest; R6 stays three relations at $v_2$, reducing to one at $v_1$/rest — the identical law established at $N{=}2,3$, simply reapplied. The three species' $v_2$ bond counts (`3+4+3`, `3+3+4`, `3+3+3`) reduce exactly to `1+4+1`, `1+1+4`, `1+1+1` at $v_1$/rest, with no nonadjacent bond required for connectivity.

**The population firewall is crossed.** The frozen same-law complete-manifold roster now stands at eight identities — DS001, D2R5, D2R6, T3R65, T3R66, T4R656, T4R665, T4R666 — of which seven are composites. The long-standing $\ge6$ premeasurement threshold passes with margin, and passes even restricted to composites only (7 ≥ 6). The population additionally spans three distinct constituent counts (two species each at $N{=}2,3,4$), which matters directly for the eventual mass-energy test: same-$N$ pairs give a direct control against constituent-count extensivity masquerading as a real proportionality.

**Gate status is precise, not yet complete.** Structural/kinematic multiplicity: PASS. Frozen $A_{\text{dir}}$ transfer to composites: not yet run. Positive finite $M_i$ on $\ge6$ identities: open. Same-law recurrence energy and the global $\alpha$ test: sealed. No Y80 result is a mass measurement.

**Recommended next stage (Y81 — Composite Direct-Contact Inertial Curvature).** Freeze the eight-identity population; define one common composite macrocycle normalization for $A_{\text{dir}}$ with no species-specific tuning (the natural candidate: sum the frozen event-local direct-contact surprisals over the constituent updates in one composite macrostep, reporting a per-constituent normalization only as a diagnostic); measure rest and $\pm v_1,\pm v_2$ costs for all eight identities using the same frozen quadratic-plus-quartic estimator from Y47; require finite positive $M_i$ on at least six identities before opening recurrence-energy values; only then reconstruct $\ell_0$, recurrence action, and renewal energy under the same law, preregister a development/holdout split, and test one global $\alpha$ — reporting binding residuals relative to $N$ independent DS001s and exploiting the same-$N$ pairs as the strongest non-extensivity control.

### 10.1hhh The eight-identity population has positive finite inertial curvature — G6 passes — but the curvature sees only constituent count, not bond topology (Stage Y81)

Y81 reopens the frozen Y26/Y47 direct-contact scheduler surprisal — unchanged since its original derivation — on the complete eight-identity population Y80 established.

**The historical DS001 control reproduces exactly.** The archived Y47 executable, replayed directly, reproduces $A(0)=\tfrac34\ln2$, $A(\pm v_1)=A(\pm v_2)=\ln2$, giving $M_i=\tfrac58\ln2\approx0.4332$ and $\beta_4=-\tfrac1{16}\ln2$, both exactly as originally measured, at two independent replication sites.

**A first attempt exposes a genuine design ambiguity, which Y81 handles by process rather than by picking whichever answer looks better.** An initial "union-support" extension of the observable to composites — pooling all constituents' compatible/direct continuation counts — turns out to be *intensive*: it returns exactly the DS001 value for every composite, because its numerator and denominator both scale with $N$ and cancel. Rather than discard or quietly rewrite this, Y81 keeps it as a permanent, separately reported diagnostic, and points out — correctly, citing the already-frozen Y80 checkpoint's own requirement for an *extensive* composite macrocycle — that this was the wrong definition for the primary gate test, before any composite cost value had been inspected. The corrected, extensive definition is simply the unweighted sum of the unchanged Y47 per-constituent action: $A_{\text{ext}}=\sum_{i=1}^N A_{\text{dir},i}$ — no fitted coefficient, no bond-specific term.

**The resulting law is exact, and strikingly simple.**

$$M_i^{\text{ext}}(N) = N\cdot\tfrac58\ln2,\qquad \beta_4^{\text{ext}}(N) = -N\cdot\tfrac1{16}\ln2,$$

holding to arithmetic precision for all eight identities, with all odd components vanishing exactly. Every same-$N$ pair or triple is *exactly degenerate*: $M_i(\text{D2R5})=M_i(\text{D2R6})$; $M_i(\text{T3R65})=M_i(\text{T3R66})$; $M_i(\text{T4R656})=M_i(\text{T4R665})=M_i(\text{T4R666})$. Equivalently, the binding residual $M_i(\text{composite})-N\,M_i(\text{DS001})$ is exactly zero for every tested topology — the frozen direct-contact observable is completely blind to R5-versus-R6 bond structure; it only counts constituents.

**The measurement rests on independently re-verified genuine rest states, not on convenient bookkeeping.** A separate audit of the same rest anchors used for the cost measurement — 7 composites × 2 contexts, 20 stationary periods each — gives **14/14 contexts, 280/280 periods**, all with zero drift, connected bond graph, exact recurrence, and zero joint-halo flux.

**G6 formally passes: 8/8 frozen identities have finite positive extensive curvature under one common observable.** Y81 is explicit that this is a protocol-gate result, not yet a claim that the number is physical inertial mass — and that the observable's complete insensitivity to bond topology within fixed $N$ is itself the most important finding, because it sets up an unusually sharp test for the next stage: if same-law recurrence energy *does* distinguish R5 from R6 or distinguishes same-$N$ topologies while $M_i$ does not, a single global $M_i=\alpha E_0$ cannot hold across those same-$N$ pairs unless the energy differences are themselves negligible. Before any recurrence-energy value is opened, Y81 freezes the development/holdout split: development = {DS001, D2R5, T3R65, T4R656}; held out = {D2R6, T3R66, T4R665, T4R666} — chosen with no reference to any energy value, since none yet exists.

**Recommended next stage (Y82 — Same-Law Recurrence Energy).** Reconstruct $\ell_0$ under the present FBCL law rather than reusing the old Rule-55584 numerical value; measure each identity's same-law regeneration phenotype and renewal clock with one common composite macrocycle convention; form $\mathcal{R}_{\text{act}}$ and $E_0$ without consulting held-out residuals; fit exactly one global $\alpha$ on the four development identities and evaluate the four held-out identities without refitting; report same-$N$ controls and binding residuals separately from total values; do not redefine the Y81 $M_i$ observable after seeing $E_0$.

### 10.1iii The Y5 recurrence-energy construction is not yet portable to FBCL — a missing off-manifold regeneration law, not a failed test (Stage Y82)

Y82 opens the recurrence-energy branch only after Y81's positive-curvature gate passed on all eight identities, and reaches a sharp negative methodological result rather than an $E_0$ value.

**The historical Y5 quantity presupposes something FBCL has never defined.** Recovering the original Y2/Y3/Y5 methodology from archived reports, Y82 confirms the historical measurement rests on an *autonomous off-recurrence regeneration ensemble*: a legal perturbing rewrite knocks a recurrent carrier off its exact state, ordinary dynamics continue on their own, and some fraction of trajectories return while others are lost or censored — this return/loss/censor mixture is exactly what $(q_\infty,\mu_{W|\text{return}})$ measures. FBCL's successful Y33/Y46/Y79/Y80 architecture is a different kind of object: an *augmented* particle/interface lifecycle with frozen marker, Q, selector, and delayed-retirement operations that govern the carrier only while it stays on-manifold. No autonomous recovery dynamics has ever been frozen for what happens when a state is knocked off it.

**Two protocol amendments, both made before any energy value existed, narrow this honestly rather than paper over it.** An initial ablation-style challenge produced immediate loss but was recognized as not matching the historical perturbation semantics and was demoted to a non-scoring diagnostic. Direct enumeration of FBCL's own eight stationary phases then showed the old Rule-55584 one-role/external-source challenge class doesn't exist anywhere on the exact FBCL rest cycle, so Y82 froze an FBCL-native, equal-weight two-class legal panel instead (bare firing of the otherwise-compatible direct gate, versus bare firing of the competing direct gate, with no marker/Q/interface maintenance during the perturbation itself).

**Every single challenged trajectory fails.** Resuming only the already-defined on-manifold lifecycle after the legal challenge gives **0/1,280** recoveries in the primary population (160 challenges × 8 species, balanced across both challenge classes) and **0/640** in independent translated/reversed-order/alternate-tie replication — **0/1,920 combined**, every loss occurring at the very first synchronized recovery tick, identically for both challenge classes.

**Y82 explicitly declines the tempting shortcut of calling this $q_\infty=0$ and an infinite rest energy.** That would require the on-manifold lifecycle itself to be a valid recovery law, which it manifestly isn't — the very first prescribed next operation is simply invalid once the particle is off-manifold. The correct classification is that the Y5 recurrence-action construction is **operationally nonportable / undefined** under FBCL's current off-manifold dynamics, not that the underlying physical quantity has been measured to be infinite. Consequently $\ell_0$, $\mathcal{R}_{\text{act}}$, $E_0$, and $\alpha$ are not estimated, and $M_i\propto E_0$ is **neither confirmed nor falsified** — it remains untested, distinct from failed.

**Interpretation.** Y72–Y81 built a coherent on-manifold architecture (vacuum law → DS001 → R5/R6 bonds → composite species → $M_i=N\,M_i(\text{DS001})$) that is complete and well-tested for what it covers. Y82 draws the boundary of that success precisely: exact recurrent lifecycle stability is established; autonomous regeneration after a legal off-manifold perturbation is not. These are genuinely different properties that earlier stages had no occasion to distinguish, since nothing had previously required knocking a stationary composite off its own manifold.

**Recommended next stage (Y83 — Autonomous FBCL Off-Manifold Regeneration Dynamics).** Do not attempt another algebraic energy proxy. Freeze an independent recovery law — how a carrier that has undergone a legal particle-touching rewrite updates its marker/interface state and selects subsequent continuations until it either returns to a recognized recurrent identity or reaches an objectively defined structural-loss state — preserving the raw Y33 grammar, the existing on-manifold selectors as fixed controls, and constituent-permutation covariance, with no species-specific repair program and no reference to $E_0$, $M_i$, $\alpha$, or the desired proportionality while choosing the law. Only once that law is frozen and independently shown to produce a nondegenerate return/loss ensemble should the Y82 recurrence-action protocol be rerun.

*Editorial note: an earlier attempt at this stage was lost to a session interruption before its output package could be completed, and was reported (secondhand, from memory) to show positive $M_i$ values and a newly-passing G6 gate. That description does not fit this investigation's own record — G6 already passed at Y81, two stages earlier, and is not Y83's concern at all; and Y83's own scope, as frozen and executed below, explicitly excludes $M_i$, $E_0$, $\alpha$, $q_\infty$, and $\ell_0$ from the recovery-law design entirely (Section 2 of the report below states this directly). The lost run is not reflected anywhere in this document; only the reproducible package summarized below is treated as authoritative.*

### 10.1jjj An autonomous off-manifold continuation law closes the Y82 gap — species-blind, hash-frozen before validation, exhaustively checked (Stage Y83)

Y83 asks a narrower question than "what is $q_\infty$": can the existing FBCL architecture be extended by *one* universal, species-independent continuation rule that completes the already-frozen marker/Q/suppression/delayed-retirement semantics after a legal raw perturbation, returns compatible challenges to the recognized manifold, and certifies genuinely incompatible states as structural losses — without touching the on-manifold dynamics at all? The answer, over the complete observed stationary perturbation domain, is yes.

**Y82 is reproduced exactly before anything new is attempted.** The archived Y82 package had a packaging defect (parent code referenced by absolute path rather than vendored), not a scientific one; Y83 reconstructs the dependency chain from the archived parent packages and reruns all 1,920 Y82 trials, matching every row and field exactly, before touching the recovery-law question.

**The actual missing mechanism is diagnosed precisely, and it is structural rather than mysterious.** A raw Y82 perturbation can fire one constituent's legal rewrite while the composite's other constituents remain one lifecycle subevent behind; the old synchronized controller then has no legal next selector because it assumes every constituent is still in step. The fix is a **lifecycle resynchronization rule** — not a species-specific repair routine, not a new rewrite grammar.

**The frozen law, `Y83-FBCL-OMR-v1`, is genuinely minimal and species-blind.** It fires the raw perturbing gate, retires the same output channels $\{1,3\}$ already suppressed on-manifold, requires exactly one external source that must be an old-vacuum vertex (an old-vacuum source is what the existing Q construction needs to instantiate its next relation) — if the source is new scaffold instead, the trajectory terminates with a predeclared structural certificate, `loss:no_old_external_source` — and otherwise applies the unchanged Y46 marker/Q/retirement bookkeeping and advances any lagging constituents through the same event, without ever firing the perturbed constituent twice. On ordinary on-manifold evolution this module is completely dormant.

**A transparency caveat is disclosed rather than hidden.** During pre-freeze debugging, the candidate law was inadvertently exercised on all eight identities at one context before the freeze — so Y83 cannot claim a pristine species-blind holdout, and says so explicitly. The law, protocol, and code were hashed immediately afterward, before any *translated/reversed* validation context was opened, and that previously-untouched context became the real confirmatory firewall.

**Validation is exhaustive, not sampled, and agrees to the gate.** A development-only perturbation atlas across all eight stationary phases of the four development identities in two contexts finds every carrier-touching gate falls into exactly two classes with no exceptions: 80/80 compatible-old-source gates return exactly, 60/60 new-source competitors are certified losses, zero invalid or unresolved outcomes, zero unhandled classes — identical in canonical and reversed-order contexts. Post-freeze, the previously-unseen translated/reversed all-population context (322 gates, all eight species, all eight phases) reproduces the same dichotomy exactly (184/184 compatible returns, 138/138 competitor losses), as does an independent translated canonical context, as does a constituent-order-covariance stress test across every permutation of all four development identities (1,666 gates: 952/952 returns, 714/714 losses). A larger, Y82-sized population check (1,280 primary + 640 replicated trials) confirms the law produces a genuinely **nondegenerate** return/loss mixture (roughly half return, half are lost) rather than Y82's universal failure. A static source-code audit confirms no species label, no energy quantity, and no energy-module import appears anywhere in the recovery code.

**Y83 = PASS**, with every preregistered condition met and the holdout caveat disclosed rather than concealed. It explicitly does not measure $q_\infty$, $\ell_0$, $E_0$, $\alpha$, or any proportionality, and does not claim the augmented FBCL controller reduces to a purely hypergraph-intrinsic law.

**Recommended next stage (Y84 — Same-Law Recurrence Action and Renewal Energy).** Use `Y83-FBCL-OMR-v1` unchanged. Preregister the recurrence measurement and stopping/censoring rules before opening any energy output; re-run the historical Y5-style regeneration measurement under the frozen Y83 dynamics; reconstruct $\ell_0$ under FBCL; measure the renewal clock with one common macrocycle convention; form recurrence action and $E_0$ for the full eight-identity population — keeping the Y81 $M_i$ values and all $\alpha$/residual analysis sealed until every $E_0$ is itself frozen.

### 10.1kkk The recurrence-energy construction fails structurally once the missing dynamics is supplied — an exact, informative null, and G7 stays untested (Stage Y84)

Y84 imports `Y83-FBCL-OMR-v1` unchanged and reuses the Y82 challenge/work convention exactly, deliberately not redesigning the probe after seeing Y83 — and the entire eight-identity energy reconstruction fails structurally rather than statistically, for a reason Y83's own exhaustive census already implied.

**The failure is a direct consequence of the perturbation dichotomy Y83 established being *too clean*.** Because every compatible-old-source challenge returns immediately and every new-source competitor is lost immediately, with no partial or intermediate outcome anywhere in the domain, three things collapse at once: the equal-weight two-class panel mechanically fixes $q_\infty=\tfrac12$ for *every* identity (this is a property of the challenge weighting, not a measured carrier-specific phenotype); every genuine loss carries exactly zero recovery work (mean $W_{\text{loss}}=0$ across all 320 pooled losses in the development population, not sampling noise), forcing $\ell_0=0$ exactly; and because the challenged constituent's own rewrite occupies its current lifecycle slot rather than being refired, DS001 (which has no other constituents to resynchronize) has **zero** post-challenge particle work on every trial, making its renewal-clock denominator zero and $\omega_{\text{renew}}(\text{DS001})$ genuinely undefined.

**For composites, what remains is an algebraic identity, not a measurement.** Every composite's successful-return work is exactly $(N-1)/N$ (the fixed cost of resynchronizing the $N-1$ non-perturbed constituents) and every composite's renewal clock is exactly $2\pi N/(N-1)$ — so $E_0 = R_{\text{act}}\cdot\omega_{\text{renew}} = 2\pi$ **exactly, identically, for every composite regardless of bond topology or constituent count.** Y84 is explicit that this is not seven independently measured rest energies; it's the same deterministic work quantity appearing once in the numerator and once, inverted, in the denominator, cancelling by construction.

**Independent translated/reversed replication (center 500, reversed order, tie 1) reproduces every element of the failure exactly** — same $q_\infty=0.5$, same $\ell_0=0$, same undefined DS001 clock, same $E_0=2\pi$ for every composite — confirming this is structural, not a site or seed artifact. Y84 explains directly why more trials cannot fix it: with the dichotomy already exhaustively characterized by Y83 as unconditionally two-valued (immediate return or immediate loss, nothing else, anywhere in the domain), no amount of additional sampling introduces the missing intermediate cases the original Y5 measurement needed.

**Y84 = FAIL for the present Y5/Y82 recurrence-energy construction. G7 remains CLOSED and explicitly UNTESTED** — not falsified: this is a probe-design failure (the specific perturbation-and-work convention inherited from Y82 stops being informative once a correct, exhaustive continuation law is in place), not evidence against $M_i\propto E_0$ itself. No Y81 $M_i$ value, no $\alpha$, and no binding residual is opened anywhere in Y84.

**Interpretation.** Y82 and Y84 together tell a coherent story: Y82 showed the on-manifold FBCL architecture had no off-manifold continuation at all; Y83 supplied one, correctly and exhaustively; and Y84 shows that the *specific* old Y5/Y82 regeneration probe, built for a system with graded partial-recovery outcomes, degenerates into a pure two-valued dichotomy once FBCL's real off-manifold behavior is exposed — because FBCL's on-manifold recognition is apparently sharp enough that there is no partial-recovery regime for this probe to sample. That sharpness is itself a nontrivial property of the architecture, distinct from either of the two hypotheses it might naively be read as confirming.

**Recommended next stage (Y85 — Nondegenerate FBCL Regeneration-Probe / Renewal-Exposure Audit).** Do not fit $\alpha$ and do not simply gather more Y84 trials — the failure is exact, not statistical. First, recover the original Y4/Y5 raw implementation and settle unambiguously whether its historical work coordinate included or excluded the standardized perturbing hit itself (Y84 honored Y82's frozen exclusion convention without re-deriving it from source). Second, if exclusion is confirmed, search — blind to $M_i$, $\alpha$, and any desired proportionality — for a minimal FBCL-native perturbation ensemble that is nondegenerate under the already-frozen Y83 law: a viable probe must give positive successful-return work for DS001, positive genuine loss work somewhere in the development population, and outcomes not predetermined solely by the challenge-class label. The acceptance criterion should be fixed before any $E_0$ value is inspected.

### 10.1lll The single-event perturbation domain is exhaustively degenerate; whether a longer vacuum path could ever reach the carrier is left explicitly open (Stage Y85)

Y85 first resolves two historical-semantics questions before touching any new probe. Auditing the preserved raw Y2 rollouts directly (3,620 trajectories, 1,580 successful returns) shows every successful return satisfies work $=$ particle-hits exactly, including 612 genuine zero-work immediate returns — confirming the historical convention excludes the standardized perturbing rewrite from recovery work, exactly as Y82/Y84 assumed. But a second audit finds Y84 made an independent, previously unnoticed error: the archived Y4 frequency table shows $\omega_{\text{renew}}=2\pi N_{\text{return}}/N_{\text{particle-hit}}$ was always computed on **fresh natural-history blocks**, not on standardized challenge/recovery trials (36/36 archived rows reproduce to under $10^{-16}$) — so Y84's challenge-exposure-based clock was never a faithful transfer of Y5, independent of the $\ell_0=0$ problem. Neither correction rescues Y84's probe: DS001's compatible challenge is still zero-work and genuine losses still occur before any work accrues.

**A complete, exhaustive single-event census confirms there is no missed third outcome class.** Every legal gate at every one of the eight stationary phases, for all eight species, in two independent contexts (570 gate-phase instances each) sorts into exactly three categories with zero exceptions: carrier-touching exact returns (184), carrier-touching immediate structural losses (138), and carrier-disjoint "spectator" gates (248) — no off-manifold survivor, no invalid or unclassified event, no cross-core event, anywhere. A predeclared no-go theorem had assumed no disjoint legal gates would exist at all; the census falsified that premise directly (248 exist), so rather than force the planned conclusion, Y85 froze an amendment and tested the disjoint gates' actual effect: firing all 496 of them (both contexts) as ordinary raw vacuum rewrites changes the carrier-centered recurrent signature in **zero** cases. Single-event regeneration is therefore exhaustively degenerate under every legal move available.

**Multi-event vacuum behavior is checked but explicitly not resolved.** Two bounded diagnostics — repeatedly firing the nearest legal disjoint gate for 40 events from every DS001 phase (640 traced events, 0 carrier-signature changes, with the active front observed *receding* from distance 8 to distance 15 in the representative trace), and a breadth-first enumeration of disjoint-only vacuum states through depth 4 (79 distinct states, 0 signature changes) — both suggest the ordinary vacuum producer front moves away from the carrier rather than toward it. Y85 is explicit that these are diagnostics, not proof: the disjoint gates aren't a separate graph component, so a longer finite path in principle could still reach the carrier, and a deeper all-branch computation was too expensive to complete in this stage's execution window.

**Verdict: OPEN, not FAIL.** The single-event domain is an exact, exhaustive no-go; whether any finite multi-event vacuum-only path could ever perturb DS001 is unresolved. $E_0$ for the FBCL population remains undefined under a historically faithful, nondegenerate ensemble; Y81's $M_i$ values stay sealed; $M_i\propto E_0$ remains untested; G7 remains closed.

**Recommended next stage (Y86 — DS001 Vacuum-Mediated Perturbation Reachability).** Remain blind to energy and mass. Freeze a state-compressed multiway search over disjoint legal vacuum rewrites starting from DS001, using causal-cone/graph-distance invariants to prune commuting remote branches; search all eight stationary phases and the translated/reversed context; stop positively only on the first carrier-signature-changing state reached with no prior carrier-core touch; if reached, measure whether it returns after positive particle-coupled work; if a monotonic or causal-separation invariant proves reachability impossible, freeze that no-go theorem before reconsidering recurrence energy at all.

### 10.1mmm A very large bounded search finds no vacuum path into the carrier through depth 14 — but the corresponding all-depth theorem is not yet proved (Stage Y86)

Y86 pursues the one loophole Y85 left open: could a finite *sequence* of ordinary legal carrier-disjoint vacuum rewrites eventually propagate inward and perturb DS001, supplying a physically native delayed-recovery probe? Energy and inertia stay completely sealed throughout.

**A subtle methodological error is caught and corrected mid-stage — itself a useful result.** An initially attractive simplification treated freshly-born vacuum vertex labels as interchangeable (a permutation quotient), which would have made the search space far smaller. Y86 found this invalid for the actual frozen implementation: gate legality depends on the numeric condition $u<v$ with $u,v$ playing distinct roles, so relabeling fresh vertices can silently make a legal gate illegal or vice versa — demonstrated concretely by a depth-3 counterexample where swapping two fresh vertex labels removes an otherwise-legal gate. Every result obtained under that quotient was quarantined as diagnostic-only and excluded from the binding verdict; the reported search preserves exact fresh-birth chronology throughout.

**The corrected, chronology-exact search is very large and finds nothing.** Cumulative distinct states through depth 13: **528,091** (frontier growing from 1 state at depth 0 to 297,285 at depth 13); every legal one-step transition from all 297,285 depth-13 frontier states was then exhaustively audited (662,627 transitions, cross-checked by summing three independently generated shards to the same total) — **zero** "bad" (fully old-vertex, carrier-inward) gates appear anywhere through the complete depth-14 successor layer. A separate relation-provenance analysis narrowed the theoretically possible bad-gate families down to two specific patterns, found their required token co-occurrences exactly zero across the entire depth-13 population, checked the 517 closest "near-miss" states (missing only one prerequisite) through every legal successor, and found zero completions — reinforced by a symbolic newborn audit finding zero single-firing paths to a first bad gate anywhere in the chronology-aware relation types actually observed.

**Y86 is explicit about why this still isn't a theorem.** A natural general exclusion principle (that fresh vertices can't simultaneously carry certain old-vertex tokens) turns out to be false in general — it only holds for the specific correlated relation history the exact vacuum skeleton actually produces, not as a syntactic rule-level fact — and attempts to prove a clean invariant using coarser relation abstractions admitted synthetic combinations that don't occur in the real vacuum, making them too permissive to close the induction.

**Verdict: OPEN.** No legal carrier-disjoint vacuum path reaches the DS001 inward condition anywhere in a search covering 528,091+ states and 662,627 audited successor transitions — a very strong bounded negative result — but an all-depth impossibility theorem was not established. Vacuum-mediated delayed perturbation is therefore neither observed nor proved impossible; G7 remains closed and untested.

**Recommended next stage (Y87 — Chronology-Aware Formal Reachability Verification).** Stop increasing raw search depth. Formalize the first-bad-event problem with chronology preserved: use the fixed pre-first-bad old-vertex skeleton as an inductive assumption, encode the remaining correlated mixed-relation motifs as a finite SAT/SMT/IC3-style safety problem, and ask the solver for either an inductive invariant excluding all first bad gates, or a concrete counterexample trace — which, if found, should be replayed in the full frozen simulator as a candidate native delayed perturbation. Keep $E_0$, $M_i$, $\alpha$, and G7 sealed until the reachability question is formally resolved either way.

*Editorial note: Y87's formal verification track has not been executed or reported as of this writing. Its parallel counterpart — a proposed on-manifold recurrence-content protocol drafted collaboratively and independently of the off-manifold reachability question — was run instead, beginning at Y88 below. The two tracks remain independent per the original proposal: a future Y87 result would still be worth pursuing, and should be compared against, not discarded in favor of, the on-manifold route that follows.*

### 10.1nnn Two on-manifold rest-content candidates qualify under strict compositionality; a third is caught and disqualified for exactly the reason the test existed (Stage Y88)

Y88 asks whether FBCL's exact native stationary cycle — with no perturbation, no regeneration ensemble, none of the off-manifold machinery Y82–Y86 wrestled with — supports an additive rest-content observable on its own terms. Three candidates were frozen and hashed before any population value was computed: **A**, a full-period extension of the existing $A_{\rm dir}$ surprisal, summed over the complete eight-subevent cycle rather than sampled at two checkpoints; **B**, raw joint-halo cardinality with no transform; **C**, a cycle-union carrier/halo count sampled at several checkpoints per period.

**A methodological correction, caught before any candidate was promoted, is itself a notable result.** The first independence-compositionality script computed $E(AB) - E(A\mid AB) - E(B\mid AB)$ — subtracting sub-values measured *inside* the same interacting pair, rather than against independently prepared isolated references. Inspecting Candidate C's behavior exposed why this was wrong; the corrected test, $E(AB) - E(A_{\rm isolated}) - E(B_{\rm isolated})$, was frozen and rerun before any already-computed population value was allowed to count.

**Under the corrected test, Candidate C fails cleanly and instructively.** Two independently prepared, zero-cross-relation DS001+composite pairs show a reproducible **+30** excess in four of six controls (e.g. $C(\text{D2R5}{+}\text{DS001})=736$ against isolated values summing to $482+224=506$) — a scheduler/history-dependent artifact appearing *despite* zero shared relations or gates. Reproducibility and strong topology sensitivity, which C also has, are explicitly shown to be insufficient without independent additivity; C is disqualified and its population values retained only as a diagnostic.

**Candidate A passes exactly, and turns out to be algebraically trivial.** Every constituent has the identical eight-subevent grammar (six subevents at $A_{\rm dir}=\ln2$, two at $A_{\rm dir}=0$), so $E_{0,A}(N)=6N\ln2$ is a closed-form consequence of the existing on-manifold structure, not an empirical discovery — parameter-free, exactly additive (6/6 independence controls, max residual $8.9\times10^{-16}$), exactly replicated, and by construction exactly topology-blind: $\Delta E_{A,\rm bind}=0$ for every composite.

**Candidate B passes exactly and is genuinely topology-sensitive.** It reproduces every archived Y47/Y79/Y80 halo value used for the existing composite rest architecture, passes independence exactly (6/6 controls, zero residual), and shows a nonzero, reproducible binding structure relative to the DS001 baseline (47):

| identity | $H_{\rm joint}$ | $\Delta E_{B,\rm bind}$ |
|---|---:|---:|
| DS001 | 47 | 0 |
| D2R5 | 97 | +3 |
| D2R6 | 99 | +5 |
| T3R65 | 155 | +14 |
| T3R66 | 157 | +16 |
| T4R656 | 219 | +31 |
| T4R665 | 219 | +31 |
| T4R666 | 221 | +33 |

The same-$N$ contrasts are exact and consistent: $\text{D2R6}-\text{D2R5}=+2$, $\text{T3R66}-\text{T3R65}=+2$, $\text{T4R666}-\text{T4R656}=+2$ (with T4R665 exactly tied to T4R656). A touch-count decomposition shows this isn't simply "more cross-core bond relations" — R5 has more direct cross-core relations than R6, yet R6 composites can have the larger total halo, meaning bond topology reshapes the surrounding single-core dressing as well as the explicit bond count. Candidate B is frozen specifically on the R1/$v_1$-derived stationary dressing (47, not the alternative R2/$v_2$-derived 49), a caveat Y88 states explicitly rather than treating B as a dressing-independent universal.

**Both A and B are reported side by side, as the predeclared rule requires — neither is picked as "the" answer.** Y88 explicitly declines to combine them or choose using any inertial value; $M_i$ and $\alpha$ remained sealed throughout.

**Recommended next stage (Y89 — Blinded Inertia/On-Manifold-Content Relation Test).** Unseal the frozen Y81 $M_i$ population only now, and test Candidates A and B separately against it under the original Y81 development/holdout split, fitting one coefficient per candidate on development only and evaluating holdout without refitting; do not combine A and B, and keep Candidate B's R1 anchor frozen rather than adjusted after $M_i$ is seen.

### 10.1ooo Candidate A "passes" proportionality only because it is algebraically identical in shape to Mi; the topology-sensitive Candidate B fails outright — a genuinely informative split (Stage Y89)

Y89 unseals Y81's $M_i=N\cdot\tfrac58\ln2$ and fits $M_i=\alpha E_0$ (zero intercept, closed-form least squares) separately for each Y88 candidate on the frozen development set, evaluating holdout without refitting.

**Candidate A passes exactly — for a reason that empties the result of independent content.** $\alpha_A=5/48$ exactly, with development and holdout maximum relative residuals both at floating-point roundoff ($1.71\times10^{-16}$) and Spearman correlation exactly 1.0. But Y89 is explicit about why this doesn't demonstrate mass-energy equivalence: $M_i$ and Candidate A are both built from the identical constituent-local $A_{\rm dir}$ surprisal, both reduce to $N\times$constant, and both have identically zero binding residual on both sides ($\Delta E_{0,A}=\Delta M_i=0$). The fitted 5/48 follows algebraically from the two already-known $N$-laws; the holdout identities, being alternative topologies at $N$ values already in development, cannot probe binding physics when neither observable can see binding at all.

**Candidate B fails the exact-proportionality gate outright, and fails for the most informative possible reason.** Development relative residual reaches 11.06%, holdout 6.33%; the raw Spearman correlation is high (0.9694) but driven almost entirely by both quantities increasing with $N$. Exact single-$\alpha$ proportionality is mathematically impossible here because $M_i(\text{D2R5})=M_i(\text{D2R6})$ while $E_{0,B}(\text{D2R5})=97\ne99=E_{0,B}(\text{D2R6})$ — the same failure recurs for every same-$N$ pair.

**The sharper Y89 result is the binding-residual contrast itself.** Candidate B's nonzero composite residuals $(3,5,14,16,31,31,33)$ sit directly against $\Delta M_i=0$ for every composite. Y89 states the two live readings explicitly without choosing between them: either Candidate B's extra halo content is not inertial rest content, or the Y81 direct-contact curvature is *incomplete* as an inertial observable because it structurally cannot see binding.

**Verdict: A passes but is degenerate; B fails but is the informative failure.** An independent FBCL mass-energy equivalence relation is **not yet established**. Y89 declines to recommend another fit and instead calls for an independently defined observable — not algebraically inherited from Candidate A — that could test whether Candidate B's nonzero binding content has any inertial counterpart at all.

**Recommended next stage (Y90 — FBCL Kinematic Binding Response).** Search for a binding-sensitive inertial response using an independently defined kinematic transition (the existing $v_2\to v_1$ speed change already used for composite closure), constructed with no reference to $A_{\rm dir}$, halo cardinality, $M_i$, or $E_0$; only after that response is frozen should it be compared against Candidate B's sealed binding residuals.

### 10.1ppp A kinematic response to the v2→v1 transition is exact, topology-sensitive, and reproducible — but decomposes into effects that are either horizon-contaminated or don't survive pairwise decomposition (Stage Y90)

Y90 clones each composite's settled $v_2$ state into a matched intervention (switch to $v_1$) and control (continue at $v_2$) pair, and measures cross-constituent relation/gate turnover over the historical Y78 16-round window — with no $A_{\rm dir}$, halo weighting, $M_i$, or fitted parameter in the definitions.

**The transition duration itself is exactly topology-blind:** every identity settles in $L=3$ rounds, across all 60/60 tested contexts (both signs, canonical/reversed scheduler order, primary/translated replication, all exact).

**K1 (identity-turnover excess) resolves topology exactly, but turns out not to be a finite cost.** Its bond decomposition is exact and simple ($+2$ per R5 bond, $-58$ per R6 bond over the fixed window), but a horizon audit shows K1 keeps accumulating for R6 bonds well past the three-round settling point — mature $v_2$ turnover (6 edits/round) simply differs from mature $v_1$ turnover (2 edits/round) for R6, so integrating over an arbitrary window mixes genuine transition work with ordinary ongoing steady-state activity. K1 is real and exact, but not promotable as a finite inertial transition cost.

**K2 (count-turnover excess) is horizon-independent but loses its topology sensitivity under closer inspection.** It reaches a final value by round 3 and stays fixed thereafter, and its global values do distinguish some same-$N$ topologies (T3R65 vs. T3R66: 2 vs. 4) — but a pairwise, per-bond decomposition shows every individual adjacent bond contributes exactly the same 2 count-turnover units regardless of R5 or R6. The apparent global topology sensitivity was an artifact of simultaneous per-bond changes partially cancelling in the total cardinality — the local transition work is actually topology-blind at bond resolution.

**Neither survivor is proportional to Candidate B's binding residuals**, tested only after the response population was frozen: fitting $K_1=\beta_1\Delta E_B$ or $K_2=\beta_2\Delta E_B$ on the three composite development identities gives fits that fail holdout badly (K1: development RMSE 7.95, holdout RMSE 43.28, max holdout relative error 68.1%; K2: development RMSE 0.93, holdout RMSE 1.37, max holdout relative error 66.1%). A same-$N$ contrast is nonetheless striking: every tested R5→R6 substitution gives exactly $\Delta E_B=+2$ against exactly $\Delta K_1=-60$, an exact ratio of $-30$ — a precise correlation that doesn't extend to a working global law.

**Verdict: binding-sensitive kinematics — yes; independent binding inertia — not yet.** FBCL composites do have an exact, reproducible, topology-sensitive kinematic response to a speed change; it just isn't yet isolable as a clean, horizon-independent, additive inertial cost.

**Recommended next stage (Y91 — Rate-Subtracted Bond-Additive Transition Impulse).** Define a transition-localized, asymptotic-rate-subtracted impulse at the individual-bond level (summed rather than measured on the global cardinality, to avoid K2's cancellation problem); measure both $v_2\to v_1$ and the reverse $v_1\to v_2$, plus a signed velocity reversal as an independent control; require direction/reversal reciprocity and horizon independence before calling anything an inertial binding response; only then compare against Candidate B.

### 10.1qqq Rate-subtracted bond-local impulses are exact and topology-sensitive, but fail reciprocity — revealing genuine transition hysteresis instead of a binding cost (Stage Y91)

Y91 defines a per-bond, rate-subtracted impulse ($J_{\rm id}$, $J_{\rm count}$) that removes each bond's independently measured 8-round mature asymptotic turnover rate before integrating, and sums bond-local responses rather than a global cardinality.

**Mature bond rates are exact and simple, and expose the origin of Y90's horizon contamination directly:** R5 has an identical identity-turnover rate (6/round) at both $v_1$ and $v_2$; R6's rate drops from 6/round at $v_2$ to 2/round at $v_1$ — precisely the asymmetry Y90's uncorrected K1 was accumulating.

**The forward $v_2\to v_1$ transition is clean and exact:** every context settles by round 3, horizon-independent from H=3 onward, giving $J_{\rm id}^{2\to1}(\text{R5})=+2$, $J_{\rm id}^{2\to1}(\text{R6})=0$ (composite law $J_{\rm id}^{2\to1}=2n_{R5}$), and $J_{\rm count}^{2\to1}=+2$ for both bond types.

**The reverse $v_1\to v_2$ transition exposes a genuine, reproducible time asymmetry.** Every composite context executes, but none reaches the target mature state under the preregistered round-3 maturity criterion — every one of 56 composite contexts instead needs exactly **4** rounds. Because this maturity gate was frozen at 3 *before* the reverse path was examined, Y91 explicitly does not repair this post hoc: the branch fails the preregistered horizon-independence gate as scored, even though the diagnostic mature value at H≥4 is itself exact and reproducible ($J_{\rm id}^{1\to2}(\text{R5})=+2$, matching the forward value exactly; $J_{\rm id}^{1\to2}(\text{R6})=-4$, *not* matching R6's forward value of 0).

**Direct mature-$v_2$ reversal using the established Y56 turnaround operation fails completely** — 0/60 contexts execute past the first reversed event — flagged as a nonportable operation for this composite state family rather than an infinite cost. Because Y91 had preregistered successful signed reversal as part of the inertial-impulse acceptance gate, this alone blocks promotion. (A signed **$v_1$** reversal, by contrast, does execute cleanly and settles by round 3 in every context, giving an exact, reproducible, topology-sensitive signature of its own: $J_{\rm id}^{{\rm rev},v_1}(\text{R5})=-2$, $J_{\rm id}^{{\rm rev},v_1}(\text{R6})=+2$.)

**Verdict.** Finite bond-local kinematic impulses: established, exactly. R5/R6 topology sensitivity: established, exactly. Time-reciprocal binding inertia: **not established** — R6 specifically breaks forward/reverse reciprocity ($0$ vs. $-4$), and mature-$v_2$ reversal is outright nonportable for the tested composites. Because the full gate fails, Y91 does not unseal Candidate B's binding residuals at all — a deliberate firewall result, not a missed step. The most consequential finding is reframed rather than buried: what looked like a possible binding-inertia signal is a genuine **transition hysteresis** — an exact, reproducible, direction-dependent lifecycle asymmetry, concentrated specifically in the R6 bond sector.

**Recommended next stage (Y92 — Transition Hysteresis / Native v2 Reversal).** Independently establish a native mature-$v_2$ reversal operation for the current composite architecture rather than importing the nonportable Y56 turnaround; map complete state-to-state paths between mature $v_1$/$v_2$ attractors in both directions, preserving lifecycle phase and scheduler state; determine why $v_2\to v_1$ needs 3 rounds while $v_1\to v_2$ needs 4; test whether the R6 asymmetry is a phase-offset artifact, genuine directed lifecycle memory, or a bond-specific hysteresis loop; keep Candidate B, $M_i$, and $\alpha$ sealed throughout.

### 10.1rrr Four independent relaxation clocks are isolated; the hysteresis lives in a slow, exact, population-wide composite-dressing law, and a natural v2 reversal reveals a sign-dependent orientation effect (Stage Y92)

*Editorial note: Y92's primary summary report file is missing from the archived package (a packaging omission of the same kind seen in several earlier stages); this section is assembled from the stage's frozen checkpoint note, key-results table, and white-paper update text, all of which agree, rather than from a narrative report. Detail should be treated as slightly less complete than other companion sections until the full report is available.*

Y92 separates the Y91 hysteresis into four distinct relaxation clocks, none of which were previously distinguished. Sweeping all eight mature source-phase offsets and inserting long exact mature-$v_1$ dwell intervals before transitioning leaves every clock below unchanged — ruling out scheduler phase or short-lived path memory as the explanation.

- **Local lifecycle clock:** $L_{\rm life}=2$, universal across every identity and context.
- **Speed clock:** $L_{\rm speed}=3$ for both $v_2\to v_1$ and $v_1\to v_2$, universal — translation speed itself reaches its target magnitude symmetrically.
- **Composite bond clock:** direction- and topology-dependent — $L_{\rm bond}=4$ universally for $v_1\to v_2$; for $v_2\to v_1$, $L_{\rm bond}=3$ if any R5 bond is present, $L_{\rm bond}=2$ for all-R6 chains.
- **Full dressing clock:** the complete translation-normalized moving dressing relaxes far more slowly than any of the above and obeys exact, population-wide laws in $N$: $L_{\rm full}=3N-1$ for $v_1\to v_2$; $L_{\rm full}=6N-5$ for $v_2\to v_1$ with any R5 bond present; $L_{\rm full}=6N-4$ for all-R6 chains; $L_{\rm full}=4$ for DS001 in both directions.

**The Y91 "3 vs. 4" asymmetry is therefore the coarse edge of a much larger, exact, direction/topology/constituent-count-dependent dressing hysteresis** — not a two-number anomaly but a systematic law spanning the whole population.

**A native reversal route is found, and it is partially, not fully, reciprocal.** Direct mature-$v_2$ Y56 turnaround remains completely nonportable (0/60, confirming Y91). A native speed-mediated route ($v_2\to v_1\to$ reverse-$v_1\to$ reverse-$v_2$) does execute kinematically in all 60 contexts and reaches the reversed speed/bond sector — but exact *conjugate dressing* (bit-for-bit the same dressing as an independently prepared reversed-native state) is not population-wide. DS001 and D2R6 achieve exact persistent reversal in every context (4/4 and 8/8); R5-containing species do not (D2R5 0/8, T3R65 0/8, T4R656/T4R665 0/8), and T3R66 is split (4/8). Larger all-R6 chains develop a genuine sign-direction asymmetry at the exact-dressing level.

**Interpretation, stated carefully.** Y91's asymmetry is now understood as composite bond/dressing hysteresis, not a scheduler or short-path artifact. The emergent sign-dependent effect in larger all-R6 species is flagged explicitly as an orientation/handedness-*like* diagnostic only — not physical spin or chirality — pending further characterization. Y92 promotes no new inertia observable and does not unseal Candidate B, $M_i$, or $\alpha$.

**Recommended next stage (Y93 — Closed Kinematic-Loop Dressing Holonomy / Orientation Sector).** Freeze closed sign/speed loops with identical initial and final kinematics and geometry, and measure the exact dressing holonomy around them; test loop reversal/conjugacy, topology dependence, and bond additivity/persistence of any nonzero holonomy found. Keep Candidate B, $M_i$, and $\alpha$ sealed throughout.

### 10.1sss The Y92 orientation clue does not survive a closed loop — it is finite transition-path memory, not persistent holonomy, with an exact universal transient law (Stage Y93)

Y93 tests the stronger hypothesis directly: does a kinematically closed sign/speed loop — same speed, sign, geometry, bond sector, and lifecycle sector at the end as at the start — leave any persistent internal dressing label behind? The tested loop cycles $v_2(s)\to v_1(s)\to v_1(-s)\to v_2(-s)\to v_1(-s)\to v_1(s)\to v_2(s)$ using the only frozen legal sign reversal (the $v_1$ turnaround), run both with Y92's original 12-round intermediate legs (`EARLY`) and with 32-round legs longer than every Y92 settlement time (`FULL`).

**Direct mature-$v_2$ reversal remains unavailable, and even mature-$v_1$ reversal leaves a real tail.** A direct reversal of the settled $v_1$ state fails to reach the independently prepared opposite-sign full dressing in 0/60 contexts within 48 rounds, even though the lifecycle signature is exact in all 60 and the bond signature in 48/60 — confirming the legal sign-reversal operation itself creates substantial relational tail even once core kinematics and lifecycle have settled.

**Every closed loop returns to the correct macroscopic state but not to the correct microscopic dressing — and the residual obeys an exact, simple law.** All 120 `FULL` loops (both signs, primary/translated contexts, canonical/reversed order) exactly recover speed, sign, geometry, bond signature, and lifecycle signature, but 0/60 recover the exact full dressing at loop closure. The relation-symmetric-difference residual at closure is exactly $\Delta_{\rm rel}(0)=9N^2$ (9, 36, 81, 144 for $N=1..4$) — independent of R5/R6 topology, sign, context, and scheduler order — and evolves to a second exact population law, $\Delta_{\rm rel}(16)=3N(2N+1)$, sixteen rounds later. A changing residual is itself evidence against a stable orientation label.

**Extended diagnostics confirm full relaxation, not persistence.** Every tested species (all-R6 ladder and R5-containing controls alike) reaches the independently prepared exact target dressing by post-loop round 32 and remains there through round 128 — 16/16 and 28/28 exact across every tested context, sign, and scheduler order, including reversed order. The `EARLY`-loop variant closes faster for smaller species but reaches the identical eventual identity, confirming the transient's *path* depends on turn timing while its *destination* does not.

**Verdict: persistent dressing holonomy/orientation sector NOT PROMOTED.** What Y92 flagged as a possible orientation-like effect is real at its finite diagnostic checkpoint but is not a stable asymptotic sector — it is finite transition-path dressing memory that ordinary mature dynamics fully erases. The positive result carried forward is the exact $9N^2$ transient law and its evolving relaxation profile, not a new conserved or persistent label. Candidate B, $M_i$, $E_0$, and $\alpha$ remained sealed throughout.

**Recommended next stage (Y94 — Closed-Loop Dressing Relaxation Spectrum and Pair Additivity).** Measure the first exact closure round for every species/context rather than only fixed checkpoints; decompose the $9N^2$ residual by constituent, constituent pair, relation age, and reversal leg; test whether the quadratic term is an exactly pair-additive wake burden plus a one-body contribution. Remain mechanistic and keep Candidate B, $M_i$, $E_0$, and $\alpha$ sealed; if the transient decomposes cleanly with no persistent internal label, close this kinematic-hysteresis branch and resume the main mass/inertia program.

### 10.1ttt The N²-scaling wake is an exact, directed, collective one-body relaxation front — not microscopic pair dressing — and closes on a universal clock (Stage Y94)

Y94 tests whether the Y93 $9N^2$ transient is literally made of pairwise dressing between constituents, and measures the full relaxation spectrum to closure.

**The quadratic residual is not microscopic pair-touch content.** All 5,364 weighted endpoint residual relations, across the complete 60-context population, touch exactly *one* constituent core — zero touch two, zero touch three or more. The algebraic identity $9N^2 = 9N + 18\binom{N}{2}$ is real arithmetic but does **not** correspond to actual two-body bond relations; Y94 explicitly rejects the tempting "pair-additive" reading this identity invites.

**The true structure is an exact, directed, collective one-body wake.** Ranking constituents by position $j$ from the trailing edge, the endpoint burden on constituent $j$ is $B_0(j)=6N+3+6j$ — passing all 180/180 constituent rows exactly — and summing this directed gradient over the whole composite reproduces $9N^2$ exactly. The quadratic scaling is therefore *collective*: each constituent's individual wake grows with how many other constituents are present, even though the excess relations physically touch only that one constituent's own core. A second exact law governs the post-16-round state ($B_{16}(j)=12(N-j)-3$, again 180/180 exact), with the burden direction having reversed.

**Closure is universal and clean.** Every context reaches the independently prepared exact target dressing at exactly $R_{\rm close}=15+3N$ (rounds 18, 21, 24, 27 for $N=1..4$), independent of bond topology, sign, context, or scheduler order, and remains exact through the full 40-round observation horizon thereafter. One round before closure, exactly three residual relations remain, always on the trailing constituent — a directed cleanup front that explains why each additional constituent extends closure by exactly three rounds.

**Provenance tracing closes the loop on where the wake comes from, and finds a real but transient topology effect.** Every endpoint-residual relation traces unambiguously to the pre-loop or early legs of the loop (never to the second half); exact population laws govern how much wake originates from each leg ($L_1=N(3N-2)$, $L_2=N(3N-1)$, $\text{PRE}+L_3=3N(N+1)$). Where R5 bonds sit in the composite changes which leg the surviving wake traces to (an exact redistribution law, $L_3=N+6W_5$, involving a pairwise cut-counting factor $W_5$) without changing the total $9N^2$ — topology reroutes the wake's provenance, not its size. Rounds 3–15 retain a temporary R5/R6-dependent cleanup-rate difference that vanishes by round 16; Y94 flags this middle-transient dependence as not fully explained and therefore does not yet declare the branch closed.

**Verdict.** Classification: quadratic, collective, directed one-body wake with transient topology-dependent cleanup — explicitly **not** microscopic pair additivity. No physical spin, chirality, mass, energy, or gravitational coupling is promoted. Candidate B, $M_i$, $E_0$, and $\alpha$ remained sealed throughout.

**Recommended next stage (Y95 — R5 Cut-Topology Cleanup Front), status: superseded by explicit redirection.** Y94's own recommendation was to measure exact deletion times by spatial rank and birth leg to explain the remaining rounds 3–15 topology dependence, and only then close this branch. Before that stage was run, the investigation was explicitly redirected back to the main inertial-curvature question, informed by the causal-graph energy/momentum construction from the Wolfram Physics Project (causal edges crossing spacelike vs. timelike hypersurfaces): see Section 11's updated priorities for the resulting Y95 proposal.

### 10.1uuu The causal-edge-flux protocol is frozen and correctly stops itself at its own preflight gate: the simulator does not retain the lineage the observable requires (Stage Y95)

Y95 executes the collaboratively-reviewed Revision 3 causal-edge-flux protocol (Section 2's preflight, required before any implementation) and reaches an instrumentation blocker rather than a measurement.

**The blocker is exactly the one the protocol was designed to catch, and the firewall holds.** Revision 3's Section 2 requires a unique, recoverable producing event for every consumed relation instance before Candidate E1 is implemented, and explicitly forbids substituting a proxy if that lineage is unavailable. Inspecting the archived simulator directly: `Sim` retains the current relation set, structural indexes (`by_src`, `target_sources`), the current gate set, the fresh-vertex counter, and scheduler state — but no persistent relation-instance-to-producer-event map. `Sim.fire()` creates a fresh vertex and adds/removes relations through `_add`/`_remove`, but neither creates nor retains a causal-event identifier. A mature relation can therefore be present in state with no retained record of which update event originally produced that specific instance.

**Two plausible rescues are checked directly and both fail for a precise, structural reason.** The Y68 `_aff()`/`_gf()` recomputation-witness machinery is exact for the question it was built to answer — which currently-present relations participate in a given gate's recomputation closure — but that is membership in a *current* witness set, not a historical producer map; it was never designed to answer "which event created this specific relation instance." Y94's own provenance logger, which might look like a ready-made lineage tool, turns out to be a prospective, experiment-local monkey-patch of `_add` that labels every relation already present at attachment simply `PRE` — it instruments only what happens *after* it is attached, and cannot retroactively reconstruct the origin of already-mature relations.

**Y95 declines to retrofit either tool as a substitute, exactly as the frozen kill condition requires.** Doing so would have been the single easiest way to produce a number quickly, and the protocol was written specifically to prevent exactly that shortcut. No E1/E1_mult implementation, stabilization measurement, compositionality control, frontier-collapse or seed audit, foliation test, population measurement, or E2 residual was attempted. `Mi`, Candidate A, Candidate B, and $\alpha$ all remain sealed.

**Interpretation.** This is explicitly an instrumentation/data-model result, not evidence against causal-edge flux as a candidate. The existing histories are not rich enough to support exact-lineage measurement retroactively — they would need to have been generated with a lineage recorder attached from the start. This does not indict any conclusion drawn by Y46–Y94, none of which depended on exact producer lineage.

**Recommended next stage (Y96 — Prospective Causal-Lineage Instrumentation).** Freeze and validate a lineage-recording extension to the simulator, independent of and prior to any Y95 measurement: assign a unique event id to every update event plus a distinguished seed pseudo-event; record each relation instance's producer id at creation and consumer id at consumption; ensure this record survives `clone()`/state-copy operations exactly; treat relation deletion followed by re-creation as distinct instances; explicitly define how controller-added marker/Q/lifecycle relations map to event identity; and regression-test the instrumented simulator against the existing frozen FBCL trajectories to confirm the recorder is dynamically passive (changes no physics, only adds provenance). Only after that instrumentation is independently validated should fresh mature rest histories be regenerated under it and frozen Y95 Revision 3 rerun from Section 2 forward on the newly-generated histories — the existing archived mature states cannot be retroactively upgraded to exact causal histories.

### 10.1vvv A passive exact-lineage recorder is qualified against the complete regression corpus, checkpoint-for-checkpoint rather than endpoint-only (Stage Y96)

Y96 has exactly one job: add exact producer/consumer relation-instance lineage to the simulator and prove, to the standard of intermediate-trajectory equality rather than final-state equality, that doing so changes nothing about which history the FBCL dynamics actually follows.

**One execution correction is caught and fixed before any qualification counts.** An early pilot ran its regression against a generically-named `V03` vacuum rather than the actual archived `Y33_BEST` (Y33 candidate-178) grammar underlying every Y46–Y94 history. The pilot's 1,927 checkpoint matches were discarded outright rather than salvaged, since they were validated against the wrong background; the corrected target was hashed before any qualification run counted.

**The recorder is instance-local metadata only.** A successful relation insertion gets a monotonically numbered instance ID; removal closes that instance; re-adding the identical tuple creates a new instance ID rather than reusing the old one; the four construction relations are attributed to a distinguished seed pseudo-event; and none of the archived relation set, gate set, indexes, RNG state, rewrite rule, or candidate-selection code is reordered or rewritten — lineage lives entirely in separate recorder-side bookkeeping.

**Passivity is checked far more strongly than endpoint agreement, across three regimes.** An exact 1,800-event vacuum history (matching baseline and instrumented arms) shows zero mismatches in selected gates, fresh IDs, relation/index/gate state, or full RNG state at all 1,801 intermediate checkpoints. The complete 60-context moving population (all eight species, both signs, canonical/reversed order, primary/translated replication) shows zero mismatches across 9,600 checkpoints and 18,720 fresh-ID checks, with identical legal-candidate lists, tie lists, and selector choices predicted from a cloned RNG state at every step. Most importantly, the full stationary-rest lifecycle for all eight identities — the exact machinery (cleanup, bridge, delayed-retirement, Q, marker, and the Y79 R5-specific retirement) most vulnerable to subtle instrumentation side effects — shows zero mismatches across 7,917 checkpoints and 12,472 fresh-ID checks.

**The recorder is also checked for sufficiency, not only passivity.** Across 20,636 audited stationary-rest core events, every one has exactly three identified live input relation instances before firing, none ambiguous, all three correctly marked consumed by that same event afterward — confirming the recorder actually supplies the specific producer-instance-to-consuming-event links Y95 needs, not merely inert bookkeeping. A dedicated remove/re-add unit test also confirms distinct instance IDs are issued correctly with the underlying simulator states remaining exactly equal. As an external anchor, both baseline and instrumented arms exactly reproduce archived Y90 response outputs in all 8 tested contexts.

**Verdict: Y96 = PASS**, stated narrowly and correctly: the recorder is dynamically passive over the tested corpus and is now qualified to regenerate lineage-bearing histories for the already-frozen Y95 protocol. Y96 explicitly does not itself validate causal-edge flux as a rest-content observable — it only clears the instrumentation blocker Y95 stopped at.

**Recommended next stage: resume frozen Y95 Revision 3 exactly as written**, on freshly regenerated histories carrying the now-qualified lineage, in its original frozen order (lineage availability → E1/E1_mult implementation → phase-matched compositionality → frontier-collapse/seed audits → literal foliation sweep → blind population measurement, with `Mi`, Candidates A/B, and $\alpha$ sealed throughout).

### 10.1www E1 passes compositionality and is exactly bond-blind at the period boundary — but the literal foliation sweep reveals a genuine, reproducible R5-localized temporal signature the scalar erases (Stage Y95, resumed)

With Y96's blocker cleared, Y95 Revision 3 resumes from its own frozen order, unchanged, on freshly regenerated lineage-bearing histories.

**Compositionality passes exactly, with a clean numeric signature.** All 6/6 non-interacting controls (DS001+DS001, D2R5+DS001, T3R65+DS001, two separated contexts each) show joint E1 exactly equal to the sum of isolated values (8=4+4; 12=8+4; 16=12+4), zero cross-relations, zero cross-gates, zero seed-sourced flux, and stabilization by the 2-period window in all 30 population contexts.

**At the period-repeat boundary, E1 is exact and completely bond-blind.** The full population gives $E1_{\rm recurrent}=4N$ and $E1_{\rm mult}=5N$ exactly, in every sign/context/scheduler-order combination tested (30/30). The binding residual $E2=E1(\text{composite})-N\,E1(\text{DS001})$ is therefore identically zero for every composite — the same topology-blindness pattern that sank $M_i$ and Y88 Candidate A, now found in a third, structurally independent construction.

**The frontier-collapse diagnostic resolves the $E1$-vs-$E1_{\rm mult}$ distinction exactly, as designed.** Every crossing relation instance has exactly one producer and one consumer, so $E1_{\rm mult}$ collapses to a static carried-relation count. But the producer→consumer map is not injective: in every context, exactly $N$ relation-dependency pairs share a producer/consumer event with another dependency, reducing $5N$ relation dependencies to $4N$ unique event pairs. This is precisely the distinction the bijection-strengthened Section 6.1 check was built to catch, and it works as intended — $E1_{\rm mult}$ collapses, $E1$ itself does not, and both facts are reported rather than merged into one verdict.

**The literal foliation sweep is where the real information is, and E1 fails phase-invariance outright.** Sweeping the spacelike cut through all eleven synchronized whole-composite phases (`start, h0_bridge, e0, e1, e2, e3, h1_bridge, e4, e5, e6, e7`), every cut is a valid antichain and every measurement stabilizes — but the isolated-DS001 profile itself varies sharply with phase, $f(\phi)=(4,4,2,1,1,2,2,1,1,2,4)$, so all 30/30 population contexts receive the frozen PHASE-DEPENDENT verdict. Under Revision 3's promotion rule, this alone blocks scalar promotion regardless of the period-boundary result.

**A genuine, exact, reproducible topology signature lives in that phase structure.** Every all-R6 composite's complete phase profile is exactly $N\cdot f(\phi)$ — pure extensivity, no surprise. But every frozen composite containing one R5 bond shows exactly two additional unique causal edges, localized specifically at phase $e3$ and the immediately following $h1\_bridge$ boundary, independent of sign, scheduler order, or translated context (30/30 exact, e.g. D2R5's profile `(8,8,4,2,2,5,5,2,2,4,8)` against D2R6's `(8,8,4,2,2,4,4,2,2,4,8)`). This excess appears and then exactly disappears again before the period-repeat boundary, which is precisely why the period-boundary scalar $E2$ measures zero even though the underlying causal structure genuinely distinguishes the bonds. Within the tested population, the two distinct one-R5 tetramer placements (T4R656, T4R665) have identical phase profiles, so R5-position sensitivity and multi-R5 scaling are both explicitly left unestablished.

**Verdict: E1 NOT PROMOTED**, for two independent predeclared reasons — phase-dependence under the literal foliation sweep, and exact bond-blindness at the one boundary that was tested as a scalar. `Mi`, Candidate A, Candidate B, and $\alpha$ remain sealed; no proportionality test is run. Y95 is explicit this is not a failure of causal-graph analysis generally — it is a precise negative for the single period-boundary slice this specific protocol proposed.

**Interpretation.** The recurrent FBCL rest cycle carries a well-defined amount of causal activity only once a lifecycle phase is specified — the flux is not a single number, it is a function of where in the cycle you cut. R5's binding signature is real and exact, but it is temporally localized rather than a standing quantity: it appears at one specific phase pair and is exactly cancelled by the time the cycle repeats. This reframes the entire search: the missing rest-content quantity, if it exists in this family of observables at all, is more likely something integrated or aggregated over the full phase structure than any single-slice count — of exactly the kind $M_i$, Candidate A, Candidate B, and now period-boundary $E1$ have all independently turned out to be.

**Recommended next stage (Y97 — Phase-Integrated Causal-Flux Holdout Test).** Do not rescue a phase-integrated candidate by validating it only on the population that revealed the phase pattern. Construct the most defensible version first — a uniform sum/integral over the complete set of synchronized lifecycle phases, with no fitted phase weights, and an explicit, frozen convention for the duplicate `e7`/`start` boundary — then validate it on a genuinely new topology holdout (zero-R5 composites, one-R5 composites at multiple placements/mirrors, and two-or-more-R5 composites if the frozen grammar admits stable examples) rather than only the original eight identities. Keep $M_i$, Candidates A/B, and $\alpha$ sealed throughout candidate construction and holdout validation.

### 10.1xxx A cycle-integrated causal-flux residual is confirmed out of sample on a genuinely new N=5 holdout — the first candidate in this branch to survive true prediction, though per-bond additivity remains unresolved (Stage Y97)

Y97 freezes a fixed full-cycle sum before inspecting any new topology, and tests it against holdout species discovered blind to the candidate itself.

**The candidate is fixed first, correctly deduplicating the cyclic boundary.** Because Y95's 11th cut (`e7`) is the same physical boundary as the next period's `start`, Y97 sums over the ten genuinely distinct cuts, $\mathcal{F}=\sum_{\phi\in P_{10}} E1_{\rm recurrent}(\phi)$, giving $\mathcal{F}_{\rm DS001}=20$ exactly in both tested contexts. The prediction carried forward from Y95 — $\Delta\mathcal{F}=2n_{R5}$, with the stricter phase-localized form of $+1$ at `e3` and $+1$ at `h1_bridge` per R5 bond — is stated explicitly as inherited, not refit.

**A blind structural census supplies new-topology holdout species before any flux value is computed.** Testing all sixteen ordered N=5 four-bond words in $\{5,6\}^4$ under the unchanged FBCL law, a control run first reveals N=5 needs a longer $v_1$ dressing transient than N=4 (exact period-1 only from round 26, versus N=4's earlier settling); a uniform 32-round burn window is frozen for every geometry and the census rerun before any species is accepted. Exactly four geometries reach complete manifold status in both primary and translated/reversed contexts: one all-R6 control (`P5R6666`) and three one-R5 chains at three different R5 positions (`P5R6566`, `P5R6656`, `P5R6665`). No N=5 geometry with two or more R5 bonds survives the frozen left-to-right bond-seeding construction — itself a structural finding, not a measurement gap.

**The holdout prediction passes exactly, in all 8 holdout contexts.** The all-R6 control gives $\mathcal{F}=100=20N$, $\Delta\mathcal{F}=0$. All three one-R5 holdout species give $\mathcal{F}=102$ exactly, hence $\Delta\mathcal{F}=+2$, reproduced identically under translation, sign reversal, and scheduler-order reversal. The complete ten-phase residual, after subtracting five independently-measured DS001 profiles, is exactly $(0,0,0,0,0,{+1},{+1},0,0,0)$ for every one-R5 placement — the same `e3`/`h1_bridge` localization Y95 found on the original population, now confirmed at three entirely new bond positions the candidate had no part in discovering.

**What this does and does not establish is stated with precision.** R5-presence sensitivity, phase localization, and position-independence across the three tested placements are all established out of sample — a materially stronger claim than Y95's original same-population observation. But because no multi-R5 N=5 identity exists to test against, Y97 cannot distinguish genuine per-bond additivity ($\Delta\mathcal{F}=2n_{R5}$) from a weaker "any R5 present" indicator ($\Delta\mathcal{F}=2\cdot\mathbf{1}[n_{R5}>0]$) — both predict identically on every holdout species available. Per its own preregistered gate, Y97 therefore defers promotion rather than promoting on data that cannot discriminate between the two hypotheses.

**Only after the holdout verdict was hashed was the original eight-identity population checked for consistency**, confirming the same law throughout (DS001 20; D2R6/D2R5 40/42; T3R66/T3R65 60/62; T4R666/T4R656=T4R665 80/82) — a genuine consistency check performed in the correct order, not a contributor to the acceptance decision. A secondary multiplicity-weighted cycle sum ($\mathcal{F}_{\rm mult}$) behaves in exact parallel but is retained only as a diagnostic, since Y95 already showed `E1_mult` collapses to a static count.

**Verdict: new-topology causal-flux holdout PASS; R5-presence sensitivity PASS; position-independence (positions 1–3) PASS; exact phase localization PASS; multi-R5/per-bond additivity UNRESOLVED; promotion DEFERRED.** No coefficient was refit and no mass-energy comparison was opened.

**Interpretation.** Y97 is the first candidate in the entire causal-flux/binding-content search to survive a genuine out-of-sample test rather than only reproduce a pattern on the population that suggested it. Inside the model, the clean statement is that an R5 bond inserts exactly two additional units of causal event-pair flux over one complete mature rest cycle, localized to the event-3/half-cycle-bridge transition, for every one-R5 topology tested through N=5. This remains a model-internal causal-cycle result, not yet a claim about physical mass or energy.

**Recommended next stage (Y98 — Multi-R5 Reachability and Formation-Order Holdout).** Keep $\mathcal{F}_{\rm flux}$, $M_i$, Candidates A/B, and $\alpha$ sealed during topology discovery. Revisit N=5 multi-R5 geometries using every legal permutation of the frozen R5/R6 bond-seeding order, not only the historical left-to-right construction; promote a multi-R5 identity only if it converges to an exact complete $v_2$/$v_1$/rest species in independent contexts with no change to FBCL or the bond motifs; if N=5 still supplies none, preregister a limited N=6 `{5,6}` chain census before opening any flux value; only once a genuine multi-R5 identity is frozen should the untouched $\Delta\mathcal{F}=2n_{R5}$ prediction finally be evaluated against it, distinguishing true per-bond additivity from a one-time presence effect.

### 10.1yyy An exact parity theorem, not a search failure, explains why no simultaneous-seed multi-R5 composite exists (Stage Y98)

Y98 keeps all causal-flux values sealed and asks a purely structural question first, exhausting formation order before conceding anything is unreachable.

**Every formation-order permutation at N=5 fails, and N=6 fails identically.** All 11 N=5 multi-R5 geometries under all 24 bond-seeding orders (264 trials) give zero legal complete-manifold qualifiers. A preregistered N=6 fallback, after freezing a corrected 40-round $v_1$ burn window from an all-R6 control, finds all 26 two-or-more-R5 words seed-illegal, leaving only four one-R5 and one zero-R5 word legal — again zero multi-R5 qualifiers.

**The exact cause is found and proven, not just observed.** Auditing all 112 individual R5 placements across N=5 and N=6, a single parity rule predicts legality in 112/112 cases: R6 bonds preserve constituent-position parity, R5 bonds flip it (odd spacing vs. even), so after one legal R5 bond, every downstream constituent reached through any number of R6 bonds has the wrong parity for a second R5 at the same synchronized preseed slice — the failure mode is always the identical `duplicate_endpoint + core_collision`, 56/56. This yields a proven, not merely empirical, structural statement: under the frozen simultaneous +v2 seed construction, an arbitrary-length R5/R6 chain can contain at most one legal R5 bond.

**Verdict.** Per-R5 additivity remains formally UNRESOLVED (not failed) — mechanically extending the same census to N=7, N=8, etc. would not help, since the obstruction is a proven construction-level exclusion, not a sampling gap. $\mathcal{F}_{\rm flux}$, $M_i$, Candidates A/B, and $\alpha$ remain sealed; no new flux value is computed.

**Recommended next stage (Y99 — Sequential-Phase Multi-R5 Formation Test).** Test whether the parity exclusion is a preparation-slice artifact rather than a deeper incompatibility: seed one legal R5, advance through v1 rounds (where global translation toggles constituent parity), then attempt a second R5 seed at a phase fixed before testing, before completing remaining R6 bonds and requiring a full two-speed-plus-rest manifold. Only once a genuine multi-R5 identity is frozen should the untouched Y97 flux prediction be opened.

### 10.1zzz Sequential-phase formation defeats the parity exclusion completely, and the additive causal-flux law is confirmed exactly across n_R5 = 2, 3, 4 (Stage Y99)

Y99 tests whether introducing the second R5 bond at a different lifecycle phase, rather than in the same synchronized preseed slice, escapes the Y98 exclusion — and it does, completely.

**Every one of the eleven N=5 multi-R5 geometries now qualifies.** Sequential parity-phase formation succeeds for all 11/11 identities (spanning $n_{R5}=2,3,4$, up to the fully-R5 `5555` chain) in both primary and replication contexts (22/22), using the unchanged R5/R6 motifs, Y46 rest, and Y79 per-R5 scar retirement with no modification. The Y98 obstruction is therefore conclusively a formation-slice constraint, not a dynamical incompatibility between multiple R5 bonds.

**The additive law is confirmed exactly, resolving the question left open since Y97.** Across all 22 contexts, $\mathcal{F}_{\rm flux}=20N+2n_{R5}$ holds exactly — the additive hypothesis $H_{\rm add}$ passes 22/22, the saturating alternative $H_{\rm sat}$ passes 0/22. The exact phase residual is $+n_{R5}$ at `e3` and $+n_{R5}$ at `h1_bridge`, zero elsewhere, across all 242 phase measurements, every one antichain-valid, stabilized by 2 periods, with zero seed-sourced flux. For N=5: $n_{R5}=2\to\mathcal{F}=104$; $n_{R5}=3\to106$; $n_{R5}=4\to108$.

**Verdict: the phase-integrated causal flux is promoted as a working topology-sensitive causal rest-content candidate within the FBCL model** — the first quantity in the entire mass-energy program to combine exact compositionality, genuine out-of-sample survival, and now confirmed per-bond additivity. $M_i$, Candidates A/B, and $\alpha$ remained sealed throughout Y99; no physical energy/mass identification is made.

**Recommended next stage (Y100 — Causal Rest Content vs. Frozen Inertial Curvature).** Freeze a comparison protocol, then unseal the frozen Y81 $M_i$ and Y88 Candidate A/B populations and test whether one global $M_i=\alpha\mathcal{F}$ relation survives development/holdout and same-$N$ topology controls. Report binding residuals directly; do not redefine observables in response to disagreement.

### 10.1aaaa The first fully-validated topology-sensitive rest-content candidate structurally contradicts the frozen G6 curvature — decisively, not statistically (Stage Y100)

Y100 performs the comparison deliberately deferred since Y95, unsealing $M_i$ and Y88's candidates only after the comparison protocol was frozen.

**The contradiction is exact and structural, not a near-miss.** $M_i(N)=N\cdot\tfrac58\ln2$ is exactly constituent-extensive with zero binding residual for every composite; $\mathcal{F}=20N+2n_{R5}$ is not. A naive one-$\alpha$ least-squares fit looks deceptively close (max relative residual 2.92% in both development and holdout) purely because the dominant $20N$/$N$ terms swamp the small binding term — but the structural gates that remove the shared extensive part expose the contradiction cleanly. The **same-$N$ topology gate fails outright**: $M_i({\rm D2R5})=M_i({\rm D2R6})$ while $\mathcal{F}({\rm D2R5})-\mathcal{F}({\rm D2R6})=2$, and identically for T3R65/T3R66 and both one-R5 tetramers against T4R666. The **binding-residual gate fails decisively**: $\Delta M_i=0$ exactly for every composite while $\Delta\mathcal{F}=2$ for every one-R5 identity — no nonzero global $\alpha$ can satisfy $\Delta M_i=\alpha\Delta\mathcal{F}$ for these species simultaneously.

**Y88's candidates are re-examined with sharper eyes.** Candidate A ($E_A=6N\ln2$) remains exactly proportional to $M_i$ ($M_i=\tfrac5{48}E_A$, arithmetic-zero residual) — but Y100 now identifies this precisely as two observables sharing the *same* constituent-extensive degeneracy, not independent confirmation of anything. Candidate B (joint-halo cardinality) is genuinely topology-sensitive, but resolves R5-vs-R6 in the **opposite direction** from causal flux on every same-$N$ contrast ($\Delta\mathcal{F}=+2$ against $\Delta(\text{Candidate B})=-2$, in all four tested pairs) — meaning Candidate B is not a noisy echo of $\mathcal{F}$, and neither topology-sensitive candidate is represented by the current $M_i$ scalar at all. A post-verdict optional extension attempting to transfer $A_{\rm dir}$ to the Y99 N=5 multi-R5 population is honestly reported as inconclusive, stopped by an overstrict audit rule caught on its very first test case rather than loosened after the fact.

**Verdict: $M_i=\alpha\mathcal{F}$ FAILS STRUCTURALLY.** Y100 is explicit about what this does and doesn't mean: it does not falsify causal-graph rest content, physical mass-energy equivalence, or the FBCL program generally — it falsifies specifically the identification of the current topology-blind Y81 scheduler-response curvature with a quantity proportional to the now-established topology-sensitive causal rest content. The Y89 exact Candidate-A/$M_i$ proportionality is reframed: it related two observables sharing one blind spot, not independent validation of either.

**Interpretation.** Y100 separates two properties the investigation had implicitly conflated since Y81: $M_i$ measures an exactly constituent-extensive scheduler-response cost ($M_i\propto N$); Y99's causal rest content measures constituent content *plus* an additive bond-lifecycle contribution ($\mathcal{F}=20N+2n_{R5}$). They cannot be one global scalar multiple of each other once topology varies. This does not identify which observable, if either, is physical mass — it identifies precisely what the current inertial-curvature construction is missing.

**Recommended next stage (Y101 — Causal Momentum Flux and Inertial Response).** Do not repair $M_i$ with a fitted R5 term — that would force agreement after seeing the answer. Instead return to the momentum-flux construction deliberately deferred at Y95: preregister an exact timelike/kinematic causal cut using the Y96 lineage recorder; measure causal momentum/transport flux on rest, $v_1$, and $v_2$ manifolds without using $\mathcal{F}$ or $M_i$ to tune the definition; test sign reversal, scheduler/context invariance, and compositionality; derive an inertial curvature or dispersion relation from the causal energy-momentum pair only after the moving observable is independently validated; ask whether the resulting causal inertial response contains the same additive R5 contribution as rest content.

### 10.1bbbb The first causal-momentum candidate is exact and sign-sensitive in motion but carries a nonzero, unexplained rest circulation — a clean, informative failure (Stage Y101)

Y101 builds the first kinematic causal-graph observable using only the Y96 lineage, without any R5-aware tuning: the signed spatial displacement of unique causal event pairs entering a mature target window, $P_{\rm edge}(W)=\sum_{(e_p,e_c)\in C_W}[x(e_c)-x(e_p)]$.

**The moving-sector result is remarkably clean.** Across all 32 validation rows (all-R6 population, both signs, both speeds, two contexts), $P_{\rm edge}=Nv$ exactly — sign-odd, context/scheduler-robust, with a simple microscopic accounting: exactly $N$ unique incoming causal pairs and $4N$ consumed relation dependencies per moving macro-round.

**But the preregistered rest-zero gate fails in every case.** Exact stationary Y46 rest carries a nonzero directed causal circulation, $P_{\rm edge}({\rm rest})=\tfrac52 N\sigma$ (where $\sigma=\pm1$ is the inherited rest orientation history), failing 0/8 — and the frozen protocol required Y101 to stop at exactly this point, before any R5 topology, before deriving a causal inertial coefficient, and without introducing post-hoc rest subtraction. A post-specified diagnostic confirms this circulation is not a scheduler artifact (order-independent, 8/8) and a phase decomposition shows it is distributed across the entire rest cycle, not one anomalous event.

**Verdict: NOT_MOMENTUM.** Y101 separates two causal currents the raw all-space construction mixed together: a clean translational current ($Nv$ in motion) and an independently persistent internal orientation circulation (nonzero at rest, reversing with inherited history) — real, reproducible, and explicitly not identified with physical spin or chirality. Because the observable integrates causal-edge displacement over *all* spatial cuts, internal circulation contaminates it even at zero macroscopic motion.

**Recommended next stage (Y102 — Literal Exterior Timelike-Surface Flux).** Freeze one or more fixed lab-frame timelike cuts outside the carrier's support and count only causal edges that physically cross those cuts; require exact zero crossing at rest without subtraction; test cut-position independence, sign reversal, and speed dependence on all-R6 controls before opening any R5/multi-R5 holdout or comparison with $\mathcal{F}$.

### 10.1cccc An exterior-cut filter removes the rest circulation completely — but the resulting crossing count is speed-blind (Stage Y102)

Y102 restricts causal edges to a fixed exterior surface outside the recurrent worldtube, correcting one geometric error along the way.

**Amendment A catches a real implementation bug before any measurement counted.** The initial cut placement (half a lattice unit beyond the instantaneous constituent-center set) could sit *inside* the Y46 rest lifecycle's internal excursions rather than genuinely outside it; the corrected construction determines the recurrent event-coordinate envelope from one unscored mature calibration round/period first, then places the cut half a lattice unit beyond that envelope.

**The corrected construction achieves exact rest-zero, cleanly.** All 128 rest-side measurements (4 identities × 2 contexts × 2 orientations × 4 periods × 2 exterior sides) give $J_{\rm ext}=0$, fully lineage-clean — the Y101 circulation is removed entirely by exterior filtering, with no subtraction required.

**But the speed-resolution gate fails completely.** For every validation identity, $J_{\rm ext}(v)=N\,{\rm sgn}(v)$ at both $|v|=1$ and $|v|=2$ — the observable detects signed passage but is blind to speed magnitude, failing the preregistered $|J_{\rm ext}(v_2)|>|J_{\rm ext}(v_1)|$ gate in 0/8 comparisons, so R5 topology is never opened. A post-verdict decomposition locates exactly why: each constituent contributes one unique crossing pair regardless of speed, but that pair's spatial span is $\pm1$ at $v_1$ and $\pm2$ at $v_2$ — the needed speed information exists geometrically in the accepted edges, it is simply discarded by counting crossings rather than weighting them.

**Verdict: EXTERIOR_CURRENT_NOT_MOMENTUM**, but a genuinely productive failure — it isolates the exact fix needed rather than leaving the problem diffuse.

**Recommended next stage (Y103 — Exterior Span-Weighted Causal Flux).** Retain the exact Y102 exterior-cut filter and event-pair deduplication; weight only accepted crossing pairs by signed spatial span; require exact rest zero with no subtraction; validate sign oddness and speed response on the all-R6 population before opening R5 and the Y99 multi-R5 holdout.

### 10.1dddd The first causal-graph momentum candidate to pass every kinematic gate at once — exact, sign-odd, speed-resolving, and rest-zero — but it too is exactly topology-blind (Stage Y103)

Y103 restores the spatial-span information Y102 discarded, without changing the crossing set: $K_{\rm ext}=\sum_{(e_p,e_c)\in C_{\rm ext}}[x(e_c)-x(e_p)]$ over exactly the Y102 exterior-crossing pairs.

**Every kinematic gate passes simultaneously for the first time in this line of candidates.** All 32 moving validation contexts give $K_{\rm ext}=Nv$ exactly, at both speeds and both signs; all 128 stationary rows give exactly zero with zero accepted crossing pairs — no subtraction needed. The derived two-speed inertial coefficient, using the inherited odd interpolation, is exactly $M_K=N$, $\Gamma_K=0$, with no fitting involved.

**Topology holdout is thorough and uniformly negative.** All 32 moving contexts for the four original R5-containing identities, and all 44 moving rows for the complete Y99 eleven-identity multi-R5 N=5 population (spanning $n_{R5}=2$ through the fully-R5 `5555` chain), remain exactly on $K_{\rm ext}=Nv$ with $M_K=N$ — same-$N$ R5/R6 pairs are numerically identical (e.g. $M_K({\rm D2R5})=M_K({\rm D2R6})=2$), and even four simultaneous R5 bonds produce no deviation. All 176 corresponding stationary rows remain exactly zero.

**The disagreement with causal rest content is therefore exact, not approximate.** $\Delta M_K=0$ for every tested composite, including the four-R5 N=5 object, while $\Delta\mathcal{F}=2n_{R5}$ — for that same object, $\Delta M_K=0$ against $\Delta\mathcal{F}=8$.

**Verdict: PROMOTE_SPAN_MOMENTUM_TOPOLOGY_BLIND.** Y103 promotes $K_{\rm ext}=Nv$ as a working causal-momentum candidate inside the FBCL model — the cleanest kinematic result the causal-graph program has produced — while explicitly classifying its inertial coefficient as constituent-extensive and topology-blind. Two live possibilities are named without being decided between: either $\mathcal{F}$ contains binding content that exterior translational momentum does not represent, or coordinate velocity/macro-round time is not yet the correct normalization for comparing the two.

**Recommended next stage (Y104 — Causal-Depth Proper-Time / Boost Normalization Test).** Do not add an R5 correction to $M_K$. Freeze a causal clock independent of $\mathcal{F}$/$K_{\rm ext}$ — a recurrent causal-depth or event-time interval per complete cycle — and test whether the physical-speed candidate $dx/d\tau_{\rm causal}$ acquires the R5 dependence the independently measured rest content requires. If no topology-sensitive clock normalization emerges naturally, that is itself strong evidence the promoted rest-content and momentum observables belong to different conserved/response sectors rather than one mass-energy four-vector.

### 10.1eeee The simplest exact causal clock is also topology-blind, localizing the mismatch to a specific mechanistic question: where does the R5 binding content go under motion? (Stage Y104)

Y104 constructs a causal-depth clock (longest-path depth between equivalent updates in the causal DAG) entirely independent of $\mathcal{F}$, $K_{\rm ext}$, or any topology label, catching one legitimate implementation subtlety along the way.

**Method Correction A resolves a genuine intra-event edge case before any clock value counted.** The Y46 rest lifecycle legitimately creates and removes some relation instances within one scoped update event; the corrected construction excludes same-event ($p=c$) instances from the causal-parent set while retaining strict $p<c$ dependencies — a real causal-ordering subtlety Y96's lineage recorder correctly permits, not a bug in the recorder itself.

**The clock is exceptionally clean and completely topology-invariant.** $C_{\rm move}=1$ per moving macro-round and $C_{\rm rest}=10$ per complete rest period, exactly, for every one of 256 moving and 64 stationary all-R6 validation rows, and unchanged across the full topology holdout (608 moving + 152 rest rows spanning all original R5 identities and all eleven Y99 multi-R5 species) — even the fully-R5 `5555` object ticks identically to DS001. Boost-normalizing $K_{\rm ext}=Nv$ by this clock gives $M_\tau=N$ at both tested speeds, internally consistent but exactly extensive.

**The mechanistic reason is pinned down exactly, not left as a numerical coincidence.** A post-verdict causal-parent audit finds every audited moving-update event has exactly one inter-event causal parent — the same constituent's own previous update — with zero cross-constituent causal parents at either speed. The R5 bond exists in the hypergraph, but it is structurally absent from the consumed-relation chain that advances this particular clock during uniform transport, so there is no mechanism by which R5 binding could alter this boost normalization, regardless of topology.

**Verdict: CAUSAL_CLOCK_VALID_TOPOLOGY_BLIND.** Using DS001 to fix the one permitted global scale ($\alpha_\tau=20$) reproduces every all-R6 identity exactly while leaving the entire binding term unexplained — $\Delta M_\tau=0$ against $\Delta\mathcal{F}=2n_{R5}$ for every composite, up to a 7.4% discrepancy for the four-R5 object that the exact binding-residual test shows is not a fitting problem at all.

**Interpretation.** Y99 established a topology-sensitive causal rest content. Y103 established a clean topology-blind translational momentum. Y104 shows the simplest exact causal clock is topology-blind too. The evidence now points away from a missing scalar normalization and toward a specific, mechanistic boost-covariance question: the R5 causal content present in the stationary lifecycle simply is not entering either the uniform-motion momentum numerator or the moving event-depth clock. This is a model-internal conclusion about this construction, not a claim about physical relativistic proper time.

**Recommended next stage (Y105 — Rest-to-Motion Causal Binding Transport / Boost Covariance).** Freeze the Y99 R5 causal-content signature and directly trace its relation/event ancestry through a controlled rest→$v_1$ and rest→$v_2$ boost. Ask specifically where the two-per-R5 rest-cycle causal excess goes under motion: transported into a moving causal channel not yet measured, converted into a different invariant, or genuinely extinguished by the transition. Keep $\mathcal{F}$, $K_{\rm ext}$, and the Y104 clock frozen while answering this.

### 10.1ffff No R5 causal content transports into motion at all — the rest-cycle excess is a cleanup-path artifact, not a conserved packet, though R5 does leave a distinct trace in boost-relaxation timing (Stage Y105)

Y105 traces the exact Y99 R5 scar relation instances through a controlled boost, across 320 launch cases (20 identities, including all 11 Y99 multi-R5 species, at four lifecycle launch phases and two target speeds).

**The transport question gets a clean, exact zero.** Across all 240 legal launches (the `e3` phase is non-executable for every identity, including DS001 and all-R6 controls, so this is a property of that launch surface generally, not an R5 effect), every cross-constituent causal measure is exactly zero: cross-constituent event pairs, cross-constituent dependency multiplicity, launch-tagged cross-constituent pairs and multiplicity, and launch-tagged bond-relation multiplicity consumed by moving events are all **0/240**. The Y99 R5 excess simply does not reappear as a transported inter-constituent causal dependency.

**A direct scar-fate audit explains exactly why, mechanistically.** Tracing the specific R5 `e3` scar relation instances (10 audited across D2R5 and the four-R5 `N5R5555`, both contexts): under continued rest, every scar is consumed by the `R5_SCAR_RETIRE` event at `e4` (10/10). Under a boost launched from `h1_bridge`, that retirement event never occurs — the scar instances remain live and carrier-touching throughout the scored boost trajectory instead of being consumed as a moving dependency (0/10 consumed, 10/10 still live at the scored endpoint). The rest-cycle excess is therefore tied to a future-history-dependent cleanup path, not a fixed parcel of content that must be carried anywhere.

**A genuine, exact, topology-sensitive secondary effect is found in its place.** While actual target-speed settlement is exactly topology-blind in every same-$N$ comparison, the *full dressed-settlement* time is not: across all 72 legal N=5 $v_2$ launches, an exact floor/ceiling law in $n_{R5}$ holds without exception — $L_{\rm start}=17-\lfloor n_{R5}/2\rfloor$, $L_{h1}=19-\lfloor n_{R5}/2\rfloor$, $L_{e4}=19-\lceil n_{R5}/2\rceil$ — meaning more R5 bonds let the composite reach its canonical moving dressing *faster*, not slower. N=5 $v_1$ settlement remains unresolved within the tested horizon rather than being extended post hoc. A post-verdict comparison confirms the eventual recurrent moving state, once reached, is exactly identical to an independently-prepared canonical moving carrier (26/26 exact) — so nothing is missing from the final moving state; the difference is purely in how long the transient before it takes.

**Verdict: NO_BINDING_EDGE_TRANSPORT, with R5_DEPENDENT_BOOST_RELAXATION as a genuine secondary result.** Y105 narrows Y99's physical interpretation without invalidating it: the phase-integrated rest-cycle causal action is better described, at this stage, as stationary recurrent causal activity with a topology-dependent cleanup component, not a conserved quantity a boosted particle must carry. No mass-energy coefficient is fit; Y103's momentum and Y104's clock are not corrected.

**Recommended next stage.** Freeze, before measurement, a transition observable comparing a rest-launched path against an independently-prepared canonical moving path at the same target speed, measuring only the finite dressing mismatch/cleanup work needed to join that attractor — blind to $\mathcal{F}$ while being defined, validated on matched same-$N$ all-R6 controls, with speed settlement kept separate from dressing settlement, and the N=5 floor/ceiling law tested out of sample if new topologies become available. The central question: does this finite boost-relaxation action carry a binding-sensitive inertial response, or is it only a preparation-history transient?

### 10.1gggg A substantially broadened search finds no closed three-core triangular composite anywhere in the tested space — an empirical, census-bounded null pointing at a tree-like bonding architecture (Stage Y106)

Y106 is a structural side-question, prompted by direct interest in whether three DS001 constituents can form a closed triangle ($AB$, $BC$, $CA$ all simultaneously bonded) rather than only the open chains found since Y77, and is executed with the same sealed-observable discipline as every mass/energy stage: $\mathcal{F}$, $K_{\rm ext}$, the causal clock, $M_i$, Candidates A/B, and $\alpha$ all remain untouched throughout, since no closed candidate is ever found to open them against.

**The original Y77 closed-trimer null is recertified exactly before the search is broadened.** Reproducing Y77's single-edge $A$-$C$ seeding test (1,800 cases) gives the identical result — 16 recurrent survivors, every one having lost the $A$-$C$ interface entirely and settled back to ordinary open-chain T3R77 — confirming the historical control before extending it.

**Three independent, substantially larger discovery strategies all return zero.** Phase A exhaustively seeds a single $A$-$C$ relation across every source orientation, core-role pair, and old-vacuum offset, for all six replicated open-trimer bond geometries in four discovery contexts (10,800 cases): 0 closed, with every one of the 8,200 legal candidates losing the $A$-$C$ interface by the first mature scored boundary. Phase B transfers the actual mature multi-relation cross-core motifs of R5, R6, and R7 (not just one representative edge) to the $A$-$C$ position, exhausting every nonempty subset (1,104 transfers): 0 closed, same failure mode. Phase C tests whether formation *order* — the mechanism that resolved the Y98/Y99 multi-R5 exclusion — matters here too, trying all six bond-formation-order permutations with both immediate and 12-round-separated timing (1,728 histories): 0 closed. In the 624 cases that survive formation long enough to reach scoring, the pattern is exact and uniform: $AB$ and $BC$ both persist while $A$-$C$ alone is absent — never the reverse, never general chain destruction.

**Combined: 13,632 new discovery cases (15,432 including the reproduced historical control), zero closed triangles anywhere.**

**Verdict: NO_CLOSED_K3_IN_FROZEN_Y106_CENSUS.** Y106 is explicit that this is a strengthened finite-census null, not a proof that no FBCL preparation could ever close a triangle. The consistent empirical pattern — attempted $CA$ closure reliably reduces to $AB+BC$ rather than causing wholesale factorization — suggests either a strong open-chain attractor or a specific dynamical incompatibility for the nonadjacent interface, but Y106 does not attempt to explain which.

**Interpretation and disposition.** This result is a genuine, well-executed answer to a natural structural question the composite-bonding program had not directly tested since Y77's much narrower single-edge check — and it rules out triangular closure far more thoroughly than before, across single-edge, full-motif, and formation-order search strategies at once. It is explicitly a side-branch relative to the active G6/G7 mismatch program: no energy, momentum, clock, or mass observable was touched, and none of Y105's still-open boost-relaxation question was addressed by it. The natural next step for *this* side-question — a mechanistic theorem candidate for why nonadjacent closure fails (causal-age ordering, old-vacuum anchor competition, or a general tree-topology property of FBCL bonding) — is worth returning to at lower priority, but the active priority remains Y105's boost-relaxation observable.

### 10.1hhhh The triangle obstruction is causal non-renewal, not a causal-order violation — and its geometry connects directly back to the bond-distance range already established in Y77 (Stage Y107)

Y107 tests the mechanism behind Y106's robust closure failure directly, replaying the exact 624 Y106 Phase-C histories that form all three bonds before losing $CA$, with the Y96-style passive lineage recorder attached.

**A literal causal-order conflict is cleanly ruled out.** Across all 624 histories: zero producer-after-consumer violations, zero directed event-DAG cycles, and no universal forbidden causal-age orientation (roughly 25.6% of $A$-$C$ seeds have an older source than both targets, 38.9% newer, the rest mixed) — the injected $A$-$C$ relations are chronologically legal objects, not causally paradoxical ones.

**The real mechanism is causal non-renewal, and it is exact and total.** None of the 2,160 relation instances created by successful $A$-$C$ formation is ever consumed by a subsequent carrier-motion event (0/2,160), none has any moving-event descendant (0/624), and the closure never regenerates a successor $A$-$C$ relation the way genuine adjacent bonds do. Every single one of the 2,160 instances remains live but stops touching both current cores — it becomes a stationary wake relation, not a co-moving bond, in 2,160/2,160 cases. Adjacent R6 interfaces, for comparison, actively regenerate through ordinary MOVE-event births (3,600 AB and 2,400 BC births observed in the same population): a true bond has *either* a persistent compatible relation instance or active renewal; the attempted $A$-$C$ closure has neither.

**The R5 weave persists measurably longer before failing, tying this side-branch back to the main bond-topology thread.** R6 and R7 closures lose their $A$-$C$ interface after exactly one macro-round; the denser R5 weave survives one round longer ($L_{AC}=2$), identically across all formation orders and timings — geometric persistence without causal renewal.

**A geometric clue reframes the whole question.** The six open-trimer bases place adjacent constituents at separations 5, 6, or 7 — but the resulting nonadjacent $A$-$C$ separation is their *sum*, $R_{AC}=11$–$14$. Y77's original exhaustive dimer atlas only ever found recurrent bonds at $R=5,6,7$ and none at $R\ge8$. The "triangle" attempted in Y106/Y107 was therefore never a symmetric arrangement with three locally-bonded edges — it was an attempt to impose a long-range interface far outside the range any bond has ever been found to renew at all.

**Verdict: CAUSAL_RENEWAL_FAILURE_WITHOUT_ORDER_CYCLE.** This substantially refines the original motivating intuition (a triangle might violate causal invariance): what's actually observed is that FBCL bonding requires renewable local causal contact, which a long-range closure can be legally written into the substrate but never receive. This naturally produces a tree-like open-chain composite spectrum in the present one-dimensional carrier geometry without requiring any fundamental prohibition on cycles. No sealed energy, momentum, clock, or mass observable was opened.

**Recommended next stage (Y108 — as reprioritized).** Y107 itself suggested testing causal-renewal reach directly across the full $R=5$–$14$ range to find an exact locality boundary. Before that could run, the investigation was redirected back to the active G6/G7 program (see below).

### 10.1iiii A decisive branch test shows the R5 causal-flux excess is not a state function at all — it behaves as recurrent action accumulated over a trajectory, not stored content attached to an instantaneous state (Stage Y108)

Y108 returns to the question Y105 first exposed — is $\mathcal{F}=20N+2n_{R5}$ conserved content the carrier stores, or causal activity tied to which future actually happens? — and settles it with a genuinely decisive experimental design.

**The test clones the identical microscopic state and gives it different legal futures.** At the exact mature-rest `h1_bridge` cut (after the R5 scar exists, before its retirement event), the complete simulator, constituent state, RNG state, and lineage recorder are cloned bit-for-bit (42/42 exact fingerprint matches confirmed before branching), then sent down three separate paths: continue resting, launch to $v_1$, or launch to $v_2$. Because the starting state is provably identical across all three branches, any difference in a "state content" observable measured immediately afterward cannot be explained by the state itself — only by which future was chosen.

**The result is exact and unambiguous: the R5 contribution depends on the future, not the present.** Across 42 branch rows (7 identities × 2 contexts × 3 futures), $C_{\rm REST}=2N+n_{R5}$ while $C_{v_1}=C_{v_2}=2N$ exactly, giving $C_{\rm REST}-C_{\rm MOVE}=n_{R5}$ in all 14 species-context comparisons at both speeds. The instance-level audit is even sharper: the *exact same* cloned R5 scar relation instance is consumed by `R5_SCAR_RETIRE` when the future stays at rest (12/12), and has no consumer at all and remains live through 32 macro-rounds when the identical instance's future is changed to either moving branch (0/24 consumed, 24/24 still live). One object, one starting state, two completely different causal fates depending only on what happens next — this directly rules out treating the R5 excess as content intrinsically attached to the instantaneous carrier.

**An independent dwell-time test reaches the same conclusion from the opposite direction.** Tracking DS001, D2R6, D2R5, and the four-R5 `N5R5555` across 16 exactly-recurrent rest cycles (1,280 phase rows, 100% stabilized by horizon 2, every cycle reproducing an identical exact phase profile), the time-*integrated* causal activity grows exactly linearly with dwell duration — $S(k)=k\mathcal{F}_1$ exactly for $k=1,2,4,8,16$, in all 40 tested cases — even though the carrier itself returns to a bit-identical recurrent boundary state every single cycle. Activity accumulates; the state does not.

**Verdict: RECURRENT_ACTION_SUPPORTED.** Y108 is precise about scope: this establishes that the *R5-dependent term specifically* is trajectory/lifecycle-dependent recurrent causal action, not transported conserved content — it does not prove the topology-blind $20N$ baseline could never contain a genuine state-like component, and $\mathcal{F}=\mathcal{F}_{\rm baseline}+\mathcal{F}_{\rm lifecycle}$ remains a logically open decomposition. No mass/inertia observable was touched.

**Interpretation.** This reframes what kind of quantity the whole causal-flux program has been chasing. A conserved rest energy is supposed to be a *state function* — fixed by the instantaneous configuration, indifferent to what happens next. $\mathcal{F}$'s R5 term is explicitly not that; its exact linear growth with dwell time ($S(k)=k\mathcal{F}_1$) is structurally the signature of an *action* integrated over a trajectory (the discrete analogue of $S=\int L\,dt$ growing with elapsed time for periodic motion), not an energy attached to a point in configuration space. This suggests the target relation this program should be chasing may not be a naive $M_i\propto E_0$ built from a state-local quantity at all, but something built from accumulated recurrent action per cycle — a genuinely different, and arguably more physically appropriate, framing for a substrate whose fundamental objects are rewrite *events* rather than static configurations.

**Recommended next stage.** If the program still seeks a genuinely conserved, branch-invariant mass-energy-like quantity, it must be constructed to be invariant *by design* — tested at the identical Y108 branch cuts, evaluated using only information available at the cut itself (never future consumer information), and covering the complete carrier-plus-wake/substrate state rather than a future-dependent crossing count. Any such candidate should be required to pass the Y108 branch test (same value under REST, $v_1$, and $v_2$ futures from an identical clone) before being taken seriously as a state-like quantity at all.

### 10.1jjjj No simple current-state relation inventory is phase-conserved either — the canonical Y88 halo value is a reproducible snapshot, not a cycle-constant, sharpening rather than undermining the Y108 action framing (Stage Y109)

Y109 tests the complementary hypothesis to Y108's: if $\mathcal{F}$ isn't a state function, does the unchanged stationary manifold contain some *other*, simpler, genuinely state-defined and phase-invariant quantity — one computed purely from the current hypergraph, with no future dependence, no cycle integration, and no fitted coefficient?

**Four natural candidates are frozen and all four fail the conservation gate.** Joint halo cardinality ($H_{\rm joint}$, the Y88 Candidate-B quantity), single-constituent dressing ($H_{\rm single}$), cross-constituent structure ($H_{\rm cross}$), and an incidence-weighted inventory ($H_{\rm inc}$) are each measured at all ten unique phase cuts of the exact stationary rest cycle, for a ten-identity population (the original eight plus two new N=5 controls) across primary and replication histories. None is phase-invariant across the complete population — not even the long-relied-upon $H_{\rm joint}$.

**The most consequential single finding is what happens to the familiar Y88/Y100 halo value.** For DS001, the ten-cut profile is $(47,48,74,116,117,92,92,120,117,67)$ — the quantity swings from 47 to 120 within one exact recurrent cycle, with `e7` returning exactly to 47 (confirming the cycle itself is genuinely recurrent). The value $H_{\rm joint}=47$ used throughout Y88–Y100 was always measured consistently at the same canonical `start` phase, so every comparison built on it remains valid *as a phase-anchored snapshot* — but it is now established precisely that this was never a conserved quantity, only a reproducible point-sample of an oscillating one.

**$H_{\rm cross}$ comes closest, and fails for an interesting, informative reason.** For DS001, D2R5, and the four-R5 `N5R5555` (species with no R6 bond), $H_{\rm cross}$ is exactly phase-invariant. It fails only where an R6 bond is present, breathing from its ordinary value up to one extra cross-relation at exactly two phases (`e0` and `e4`) before returning. This yields a clean, exact, population-wide bond-phase law, confirmed in 110/110 first-cycle measurements: $H_{\rm cross}=4n_5+n_6$ at ordinary phases, $H_{\rm cross}=4n_5+2n_6$ at `e0`/`e4` — genuinely useful as a state-defined structural fingerprint of bond composition, even though it is not a conserved inventory.

**A second-cycle check reveals the surrounding substrate keeps evolving even when the carrier itself recurs exactly.** $H_{\rm joint}$, $H_{\rm single}$, and $H_{\rm inc}$ do not reproduce identical mid-cycle values on the immediately following cycle (e.g. DS001's `e0` value shifts from 74 to 75) even though the canonical `start` value recurs exactly every time — meaning the recurrent carrier-plus-dressing state and the complete surrounding history/wake substrate are genuinely different things and should not be conflated. $H_{\rm cross}$, notably, does not have this problem — it repeats its complete phase profile exactly cycle after cycle.

**Verdict: NO_STATE_DEFINED_CONSERVED_INVENTORY_IN_Y109_FAMILY.** This is a candidate-family null, not a theorem that no state-defined recurrence energy can exist. Per the frozen protocol, since all four candidates failed the first gate, no noninteracting-additivity test was run and Y81's $M_i$ was never unsealed against any of them.

**Interpretation — this result sharpens the Y108 action framing rather than competing with it.** Two distinct facts are now established side by side: state-defined does not imply conserved, and canonical-phase reproducibility does not imply phase-independent energy. Put together with Y108, the picture is exactly what a genuine action-angle structure would predict: individual instantaneous quantities (the "coordinates" of the cycle) oscillate substantially through the period rather than staying fixed — precisely as position or momentum oscillate through a classical periodic orbit — while $\mathcal{F}$'s cycle-integrated sum behaves like the associated action variable. Y109 does not close off the separate possibility that a genuine conserved energy-like quantity exists as some *combination* of instantaneous components whose parts trade off against each other (the discrete analogue of kinetic-plus-potential energy staying constant while each term individually oscillates) — it only shows that none of the four simplest linear relation-counts is that combination.

**Recommended next stage.** Do not rescue Y109 by cycle-averaging — that would just turn a state-defined candidate back into a trajectory-defined one, re-deriving $\mathcal{F}$ under a new name. Instead search for a larger instantaneous closed inventory whose internal components exchange while the total stays constant — motivated by the rewrite ontology itself (e.g. relation inventory plus an independently defined gate/interface inventory, or a bounded substrate-storage term) rather than fitted coefficients chosen post hoc to cancel the observed Y109 oscillations. Any such candidate must retain strict future-independence as a definitional requirement, exactly as Y109's own candidates did.

### 10.1kkkk Widening the state-defined neighborhood shrinks the oscillation but never removes it — and the wider shells reveal a clean, separate wake-production law instead (Stage Y110)

Y110 tests the natural rescue of Y109: is the internal phase-breathing just exchange with a bounded surrounding reservoir, such that a wide-enough neighborhood would be exactly conserved?

**Widening helps quantitatively but never qualitatively.** Four nested, strictly future-independent relation-neighborhood definitions ($J_0$: relations touching current cores/markers; $J_G$: $J_0$ plus every relation consumed by a currently-legal touching gate; $J_1$, $J_2$: one- and two-hop relation-adjacency closures of $J_G$) all fail exact phase conservation in every one of 20 identity-context tests. The relative size of the oscillation does shrink substantially as the shell widens — from roughly 82% of the mean value at $J_0$ to 61% at $J_1$ to 5.2% at $J_2$ — but even the widest tested shell never reaches zero.

**One clean, exact null closes off a specific hidden-reservoir hypothesis.** $J_G=J_0$ in all 440 measured states: every relation consumed by a legal gate touching the object is already counted in the anchor set, so there is no separate gate-side relation reservoir capable of absorbing the Y109 oscillation.

**The most informative result is a clean separation of two different behaviors.** The innermost shells ($J_0$, $J_G$) return to their exact canonical value every cycle — the object-local recurrent dressing genuinely closes. The wider shells ($J_1$, $J_2$) do not: their canonical-start value drifts upward every single cycle (20/20 contexts each), even though the carrier itself is provably back in an identical recurrent state. This drift obeys an exact population law: $\Delta J_1=5N-n_{R5}$, $\Delta J_2=22N-n_{R5}$, so $\Delta(J_2-J_1)=17N$ exactly, independent of bond topology, in 20/20 contexts.

**Verdict: NO_CONSERVED_BOUNDED_REWRITE_NEIGHBORHOOD_IN_Y110_FAMILY.** Y81's $M_i$ remains sealed, since no candidate passed the phase-conservation gate. The system looks less like a closed packet of conserved relation count and more like a genuinely recurrent open subsystem embedded in a substrate that keeps accumulating history around it, regardless of how the boundary is drawn.

**Recommended next stage (Y111 — State-Defined Vacuum-Subtracted Excess).** Do not simply widen the shell radius further — larger raw shells increasingly measure accumulated substrate history rather than anything specific to the particle. Instead pair the live carrier state with a causally age- and site-matched evolved-vacuum control at every measurement, subtract the background relation inventory shell-by-shell with no fitted offset, and ask whether the *excess over vacuum* is phase-invariant and non-accumulating. Freeze the subtraction and matching rule before opening any carrier value.

### 10.1llll A vacuum-matched control isolates a genuinely particle-induced wake-growth law and a striking new quadratic canonical-phase excess — but still finds no conserved quantity (Stage Y111)

Y111 asks whether Y109–Y110's phase dependence and wake growth are largely ordinary evolved-vacuum background rather than anything specific to the composite.

**The vacuum control is genuinely matched, not a convenient stand-in.** For every particle-state measurement, an untouched copy of the same frozen 1,800-event vacuum is advanced to the identical simulator event index and anchored at the particle's own current vertex IDs — guaranteeing identical causal age at every shared site. All 20 identity-context cases pass this qualification exactly (base-vacuum equality, exact index matching, exact particle recurrence in both scored cycles).

**Every vacuum-subtracted candidate still fails phase conservation — 0/20 across all four.** Vacuum subtraction shrinks the relative oscillation at the widest tested shell but does not eliminate it, exactly as raw widening did in Y110. The gate-closure redundancy also survives subtraction exactly: $X_G=X_0$ in all 440 measured states.

**But two genuine, clean structural laws emerge.** The inner vacuum-subtracted excess is exactly recurrent at the canonical `start` phase (20/20) and obeys a striking new exact law, $X_0({\rm start})=3N^2-1+n_{R5}$, holding in 20/20 identity-context cases — a quadratic scaling in constituent count that has not appeared in any prior candidate in this program, and one Y111 is explicit is *not* extensive, making it a poor raw mass-energy candidate on its face even before the phase-conservation failure. Separately, the wider-shell wake-growth laws survive vacuum subtraction completely unchanged ($\Delta X_1=5N-n_{R5}$, $\Delta X_2=22N-n_{R5}$, 20/20 each) — and because the matched vacuum control *itself* returns to identical shell counts every cycle with zero growth, this proves the wake production is genuinely induced by the recurrent object's own history, not an artifact of the ambient vacuum simply continuing to age.

**Verdict: NO_CONSERVED_VACUUM_SUBTRACTED_EXCESS_IN_Y111_FAMILY.** Y81's $M_i$ remains sealed. Y111 now separates three distinct, independently-established quantities: a recurrent but phase-dependent, non-extensive canonical inner excess ($3N^2-1+n_{R5}$); the Y108 recurrent causal action (explicitly trajectory-, not state-, dependent); and a genuinely particle-induced outer wake-production law that survives vacuum subtraction. None of the three is the sought conserved recurrence energy.

**Recommended next stage (Y112 — State-Defined Rewrite-Balance / Conservation-Law Search).** Stop enlarging raw spatial or relation neighborhoods — five stages (Y95, Y109, Y110, Y111, and the underlying halo work since Y88) have now shown that guessing plausible relation-counting schemes and testing them for conservation does not find one. Instead ask whether the rewrite law itself admits an exact local conservation law directly: construct a preregistered basis of every elementary motif-count change the frozen grammar can produce, and solve for integer/rational left-null vectors annihilating all of them simultaneously — the discrete analogue of finding stoichiometric conservation laws (mass, charge) in a reaction network from its stoichiometry matrix. The weights must be derived from the grammar itself, before any species value is inspected, not fitted to cancel the Y109–Y111 phase curves. Any nontrivial law found should then be evaluated as a genuinely state-defined quantity on the full population, passing phase conservation, recurrence, replication, and additivity before Y81 inertia is reopened.

### 10.1mmmm The grammar's own exact conservation laws are found and completely characterized within an 80-dimensional motif basis — and they conserve only constituent number, proving rather than merely observing that this basis contains no topology-sensitive recurrence energy (Stage Y112)

Y112 derives candidate conserved quantities directly from the frozen FBCL transition structure rather than proposing observables from measured species profiles, and validates them against composite dynamics never seen during derivation.

**The state basis is exhaustively enumerated, not sampled.** Every vertex is classified into one of five categories by its relationship to the current object and the old-vacuum cutoff (current-core-from-old-vacuum, current-core-created-after-cutoff, marker, external-old, external-fresh); every live ternary relation is classified by source category and unordered target-category pair, giving $5\times\binom{6}{2}=75$ relation motifs plus 5 vertex counts — 80 dimensions total, combinatorially complete for this categorization scheme.

**The constraint set (elementary transitions) is empirical, so the protocol is built to catch exactly the risk that poses.** A 464-transition development corpus (evolved vacuum, mature DS001 rest/$v_1$/$v_2$) yields a 64-dimensional candidate nullspace — but rather than trusting this directly, Y112 requires every canonical development-derived direction to survive an independent 360-transition composite holdout (all R5/R6 dimers through N=5 chains) with **no recombination or refitting permitted**. This safeguard is immediately vindicated: of the 64 canonical directions, 5 touch genuinely dynamic motif coordinates, and **all 5 fail the holdout outright (0/5)** — laws that looked conserved on single-carrier dynamics alone break the instant real composite bonds are introduced. This is a direct, empirical confirmation that deriving constraints only from a narrow corpus risks exactly the kind of history-specific false invariant this investigation has been burned by before (the Y98 formation-order exclusion, later shown by Y99 to be an artifact of one construction path rather than a real law) — caught here by design rather than by accident.

**A formal symbolic check rules out the most obvious candidate law directly.** The Y33 rule's raw multiset arithmetic suggests $5V-R$ should be conserved, but the simulator is set-valued (a duplicate output tuple creates no second instance), so the actual measured balance across 256 mature-vacuum fires is $4V-R$, exactly constant there (256/256) — but this holds on only 300 of 824 total transitions once particle/lifecycle operations are included, and the naive $5V-R$ holds on only 44/824. Neither is a real invariant; both were attractor-specific artifacts of the narrow vacuum-only regime.

**After the negative direct-promotion verdict, a post-verdict diagnostic finds exactly two — and only two — genuine dynamical conservation laws in the complete 80-dimensional space.** Restricting to the 21 motif coordinates that are neither dormant nor static across the full 824-transition population, the rank is 19, leaving exactly 2 surviving null directions: $I_{\rm out}=R_{CO,COCO}+R_{CO,COO}+R_{CO,OO}=8N$ and $I_{\rm in}=2R_{CO,COCO}+R_{CO,COO}+2R_{O,COCO}+R_{O,COO}=16N$, both exact across every one of the 824 measured transitions (vacuum, DS001 in all three kinematic sectors, and the complete composite holdout), and both identical for R5 and R6 topology at fixed $N$. The two are not even independent — $I_{\rm in}=2I_{\rm out}$ on every measured particle state.

**Verdict: NO_NONTRIVIAL_DIRECT_GRAMMAR_INVARIANT_PROMOTED under the preregistered gate; CONSTITUENT_NUMBER_INVARIANTS_FOUND as the post-verdict structural result; NO_STATE_DEFINED_RECURRENCE_ENERGY_IN_Y112_80D_BASIS.** $M_i$ remains sealed. This is a materially stronger negative than Y109–Y111: those stages showed particular guessed candidates weren't conserved; Y112 shows that within this complete, combinatorially exhaustive 80-dimensional motif basis, the *only* linear conservation laws that exist at all reduce exactly to constituent/support count — not one guess among many failing, but a proof, within this basis, that no topology-sensitive linear invariant is available to find. This remains explicitly basis-bounded: it does not rule out a conserved recurrence energy built from information this coarse-vertex-category basis cannot represent.

**Interpretation.** The 80-dimensional basis only distinguishes vertices by old/new-vacuum role, not by which specific grammar mechanism produced or will consume a relation. Y108 already showed the R5 signal is tied to a specific lifecycle production/retirement channel (the `R5_SCAR_RETIRE` event), which is exactly the kind of semantic distinction this basis cannot see — a strong, targeted hypothesis for why the topology-sensitive content keeps escaping every geometry-only construction tried since Y88.

**Recommended next stage (Y113 — Lifecycle-Provenance-Resolved Conservation Search).** Do not add further arbitrary structural counts. Build a new state-defined basis from the *production channel* of each currently-live relation instance, using the already-qualified Y96 lineage recorder — candidate coordinates drawn directly from the grammar's own explicitly frozen creation channels (Y33 output slot, Q/interface production, marker production, turnaround/bridge production, and other explicit lifecycle channels, plus a small preregistered causal-age class only if the grammar itself requires it). This remains state-defined, since a live relation's producer identity is already part of its own past, not a future consumer. Repeat the exact left-nullspace derivation and holdout procedure. Only if a provenance-resolved invariant survives out-of-sample and is not reducible to $N$ should $M_i$ be reopened.

### 10.1nnnn Producer provenance still collapses to constituent number at the coarse level — but combined with cross-constituent touch, it exposes the first quantity in the entire program to be both exactly conserved and multiplicity-sensitive to bond topology (Stage Y113)

Y113 extends Y112 by tagging every live relation instance with the immutable identity of the past grammar/lifecycle channel that created it — still strictly state-defined, since a relation's producer is part of its own history, never a future consumer.

**The primary, directly-promotable basis (P20: five vertex categories plus 15 producer-channel counts, derived blind from vacuum+DS001 development data) again collapses to constituent number.** All 12 canonical development-nullspace directions survive the holdout algebraically, but the only genuinely dynamic, replication-invariant law is $P_Q+P_{\rm BRIDGE}=N$ — Q/bridge content exchanges internally, but the total is exactly constituent count, exactly the same class of result Y112 found. A second direction, $P_{O1}-P_{O3}$, is phase-invariant but *not* replication-invariant (it flips between $-2N$ and $0$ under sign-reversed preparation), marking it as encoding preparation history rather than an intrinsic species property. Verdict: **NO_NONTRIVIAL_DIRECT_PROVENANCE_INVARIANT_PROMOTED**.

**A preregistered diagnostic basis, splitting each provenance channel by current cross-constituent touch, finds something qualitatively new.** Restricting to relations created as native Y33 output $O_1$ or $O_3$ that currently touch two or more DS001 cores, the quantity $I_{\rm bond}=P_{O1,T2}+P_{O3,T2}$ is **exactly conserved through every mature-rest phase, in both replication histories, across all 396 held-out state rows** — the first candidate in this entire search to combine exact phase-invariance with genuine topology sensitivity. Its value follows $I_{\rm bond}=n_{R6}+3n_{R5}$ exactly, giving every tested identity a distinct, reproducible integer (D2R6: 1; D2R5: 3; T3R66: 2; T3R65: 4; T4R666: 3; T4R656/T4R665: 5; N5R6666: 4; N5R5555: 12). It is a genuine exchange invariant, not a static seed count: for R6-containing composites the underlying $(P_{O1,T2},P_{O3,T2})$ pair switches between $(0,1)$ and $(1,0)$ at phases `e0`/`e4` while the sum stays exactly fixed; R5's pair stays constant at $(1,2)$. A companion identity, $P_{O1,T2}=P_{O7,T2}$, holds exactly in all 396 rows alongside it.

**Y113 explicitly declines to promote $I_{\rm bond}$ as recurrence energy, for reasons worth taking as seriously as the result itself.** Its coefficients were exposed only by the full-population diagnostic, not derived blind from the sealed DS001-only development basis — DS001 has no cross-constituent $T_2$ sector at all, so this quantity could not have been discovered from single-carrier dynamics even in principle. It has only been tested in the mature-rest sector, not across moving sectors, boosts, bond formation/dissociation, or the unused mixed N=5 identities. And its $T_2$ classification presupposes the already-established decomposition into DS001 constituent cores, making it state-defined within the current composite ontology but not yet a fully label-free hypergraph invariant.

**Verdict.** The defensible claim is precisely: an exact, state-defined, phase-invariant, topology-and-multiplicity-sensitive mature-rest bond-content candidate has been discovered — not yet recurrence energy, and not yet promoted. Its exact definition is frozen, unchanged, for a blind Y114 validation. $M_i$ and $\alpha$ remain sealed throughout.

**Recommended next stage (Y114 — Blind Validation of the Frozen Bond-Content Candidate).** Make no coefficient changes to $I_{\rm bond}=P_{O1,T2}+P_{O3,T2}$. Test it blindly, in priority order: the unused mixed-topology N=5 R5/R6 chains from Y99; the exact mature $v_1$ and $v_2$ sectors; rest-to-motion transfer under the same controlled boost used in Y105; bond formation and dissociation histories; a noninteracting-additivity control; and a search for an equivalent, fully label-free local motif formulation that does not presuppose the constituent-core decomposition. Only after these gates should any comparison with $M_i$, inertial curvature, or gravitational sourcing be reopened.

### 10.1oooo The frozen bond-content candidate replicates exactly at rest on unused topologies but reveals an exact, deterministic kinematic-sector law under motion — reclassified as a native cross-scaffold occupancy rather than a universal invariant (Stage Y114)

Y114 tests the exact frozen Y113 candidate, unchanged, across five preregistered gates, with $M_i$, $\alpha$, and all mass-energy proportionality sealed throughout.

**Gate A (unused mixed N=5 rest holdout) passes completely.** All ten previously-unused mixed R5/R6 five-constituent chains, across 440 held-out state rows, reproduce $I_{\rm bond}=3n_{R5}+n_{R6}$ exactly — bond position is irrelevant; only count matters. This is the strongest possible confirmation the Y113 rest-sector law was real, not an artifact of the specific composites used to discover it.

**Gate B (moving sectors) fails the frozen sector-independent prediction, but with an exact deterministic replacement.** Across 608 moving state rows spanning 19 identities, the frozen prediction matches only 336/608 — but the post-verdict law $I(v_1)=3n_{R5}+n_{R6}$, $I(v_2)=3n_{R5}+2n_{R6}$ matches all 608/608 exactly. Every R6 bond contributes exactly one additional unit specifically at $v_2$; R5's contribution is completely speed-invariant, consistent with everything already known about R5's speed-independent bond structure since Y79/Y103.

**Gate C (identical-state branch test, echoing Y108's method) pins down exactly when the change happens.** From the same mature-rest cut, $v_1$ launches preserve the rest value through all 16 scored rounds; every R6-containing $v_2$ launch holds the rest value through rounds 1–2 and switches to the mature-$v_2$ value on round 3, synchronously across every R6 bond in the composite — a transition timing that matches the independently-derived $L_{\rm speed}=3$ universal speed-settlement clock from Y92 exactly, despite the two quantities being constructed by entirely unrelated methods.

**Gate D (formation lifecycle) produces the most consequential structural finding of the stage.** In the specific Y101 preparation histories used throughout this investigation since Y77, the native $O_1$/$O_3$ cross-scaffold count is already present at its mature value *before* the explicit bond seed is ever applied — the seed adds one separate, short-lived $BOND$-provenance relation that never affects the scaffold count and stops touching both cores once the system settles. A post-verdict ablation goes further: branching from the exact 8-round preseed state with the explicit seed omitted entirely still converges, in all 4/4 tested R5/R6 primary/replication cases, to the identical mature bonded signature. **This does not contradict Y77's broad natural-pair census** (which searched far more widely and found bonds mostly do not form spontaneously) — it shows specifically that the narrow, hand-selected preparation trajectories this program has relied on since Y77/Y101 were already committed to the bonded attractor before the seed fired, raising an open question about how much of "bond formation" this investigation has actually observed versus "approach to an already-selected bonded basin."

**Gate E (noninteracting additivity) passes cleanly.** All 176 tested pairings of widely-separated composites give exactly additive $I_{\rm bond}$ values with zero inter-object cross-relations or gates. The planned dissociation subtest is recorded as unavailable rather than faked — no existing frozen lifecycle provides a lawful breakup trajectory to test against.

**Verdict: BOND_CONTENT_INVARIANT_NOT_FULLY_VALIDATED; post-verdict structural result EXACT_KINEMATIC_CROSS_SCAFFOLD_LAW.** Y113's "bond-content invariant" is too strong a description; the defensible quantity is a state-defined, provenance-resolved, additive, kinematic-sector-dependent cross-scaffold occupancy, $I_{\rm scaffold}=3n_{R5}+c_6n_{R6}$ with $c_6=1$ at rest/$v_1$ and $c_6=2$ at $v_2$ — not a universal conserved bond content. Y114 is explicit that kinematic dependence does not by itself disqualify eventual relevance to an energy-like construction (a physical energy need not be invariant under an externally forced change of motion), but declines to open that interpretation without a separately frozen energy criterion.

**Recommended next stage (Y115 — Complementary Exchange-Channel Search for the R6 Scaffold Transition).** Do not simply relabel $I_{\rm scaffold}$ as energy. Freeze the exact rest/$v_1\to v_2$ transition corpus and search, from grammar/lineage state alone (never fitted to the observed curve), for a complementary provenance channel whose count changes oppositely to exactly balance the R6 scaffold's $1\to2$ jump. If a genuine complement exists, this would identify a larger, fully conserved state-defined inventory with $I_{\rm scaffold}$ as one internally-exchanging component — the same "kinetic-plus-potential" structure this program has been looking for since Y109. If none exists, $I_{\rm scaffold}$ stands as a useful order parameter rather than a conserved quantity.

### 10.1pppp The R6 scaffold jump is not a missing exchange partner — it is a boundary-crossing (incidence) effect, reclassifying $I_{\rm scaffold}$ from candidate stored content to a moving-boundary current (Stage Y115)

Y115 searches for the complementary channel Y114 called for — and finds, instead, that no such channel is needed, because the "jump" was never a violation of content conservation to begin with.

**The exhaustive complement search is genuinely negative, at every tier tried.** Using only the D2R6-primary derivation corpus (56 states spanning two rest cycles plus matched $v_1$/$v_2$ branches), Tier 1 tests every one of 17 dynamically active complement features against small integer coefficients ($\pm1,\pm2,\pm3$) added to the frozen scaffold quantity: 0 candidates make the sum exactly constant. Tier 2 repeats this for every eligible feature pair: 0 candidates. A preregistered Tier-3 exact nullspace diagnostic on the full 19-coordinate active basis finds an affine family of solutions, but the simplest representative reduces algebraically to the already-known, already-rejected Y113 preparation-dependent quantity $P_{O3}-P_{O1}$ — a repackaged old identity, not a new discovery, and Y115 catches and reports this rather than mistaking recovered algebra for a fresh result.

**A direct lineage audit of the actual boost event reveals the real mechanism.** At the exact round-3 transition, the specific relation instances involved keep their exact lineage IDs and tuples — none is born, none is destroyed (0 births, 0 deaths of $O_1$/$O_3$-$T_2$ instances). What changes is purely *which current constituent cores* those already-live relations intersect: 2 relations cross from touching one core to touching two; 1 relation crosses the other way. The scaffold "jump" is therefore not new content appearing — it is old content crossing a classification boundary that itself moves as the composite's cores advance.

**This resolves into a clean, exact, population-wide incidence-current law.** Across 16 independently audited species/context rows spanning N=2–5, mixed R5/R6 topologies, and both replication contexts: $J_{\rm in}=2(N-1)$, $J_{\rm out}=2(N-1)-n_{R6}$, with zero births and zero deaths throughout, giving $\Delta I_{\rm scaffold}=J_{\rm in}-J_{\rm out}=n_{R6}$ exactly in every case. The R5-only control (D2R5) is the decisive confirmation: it has genuine incidence traffic too (2 relations in, 2 out), but the traffic is exactly balanced, giving zero net change — R5 doesn't suppress migration, it simply doesn't create the *imbalance* R6 does. R6 bonds specifically produce an asymmetric leak in the outgoing current, not extra incoming content.

**Verdict: NO_SIMPLE_PROVENANCE_EXCHANGE_INVARIANT (primary); EXACT_R6_INCIDENCE_MIGRATION_LAW (post-verdict).** $M_i$, $\alpha$, and any mass/energy interpretation remain sealed. Y115 explicitly separates two concepts this search had begun to blur: **state content** (something a persistent excitation genuinely carries) versus **incidence flux** (how already-existing relations cross a state-defined moving boundary as the excitation propagates). The evidence strongly supports the second reading for $I_{\rm scaffold}$ and finds no simple scalar of the first kind.

**Interpretation.** This is a conceptually clarifying result on par with Y108's action-versus-state-function distinction: $I_{\rm scaffold}$ is not a stored quantity waiting for a conservation partner — the $T_2$ classification is a discrete, current, purely geometric incidence label (does a live relation touch $\ge2$ cores right now), and as the composite's cores physically move, previously-created relations cross that label boundary without being created or destroyed, exactly the discrete analogue of a flux/continuity relation ($\Delta I = J_{\rm in}-J_{\rm out}+B-D$) rather than a local conservation law. Searching for a term whose *content* changes oppositely was the wrong kind of search for this phenomenon from the start.

**Recommended next stage (Y116 — Formalizing the Provenance-Incidence Current).** Stop searching for another scalar to repair $I_{\rm scaffold}$; formalize the current itself. Measure $J_{\rm in}$, $J_{\rm out}$, births, and deaths at every transition across mature rest, $v_1$, $v_2$, formation, and the full mixed-N5 population using exact relation-instance lineage. The nontrivial open question is not the automatic bookkeeping identity but whether the *component currents* obey clean, species-independent constitutive laws the way the Y115 round-3 result does: map the complete current waveform over a full moving macro-cycle for $v_1$ versus $v_2$; test the round-3 law against every mixed-N5 geometry; separate R5 and R6 contributions bond-by-bond; and search for a label-free incidence-current formulation independent of the specific $O_1$/$O_3$ output-slot names before any integrated or Noether-style quantity is sought from it.

### 10.1qqqq The incidence current obeys an exact, sector-dependent constitutive law, and the rest-to-v2 transition resolves into a genuine two-round step response — with a companion physics-vocabulary reading now included as standard practice (Stage Y116)

Y116 promotes Y115's migration observation into a full current-waveform measurement across 1,680 scored transitions, with the mass/inertia firewall held throughout.

**The continuity identity is exact everywhere, and the source terms vanish outside formation.** $\Delta I_{\rm scaffold}=J_{\rm in}-J_{\rm out}+B-D$ holds in all 1,680/1,680 rows; across the 1,596 non-formation rows, $B=D=0$ in every case — every mature-sector and rest-to-motion change is carried entirely by already-live relation instances migrating across the touch-class boundary, never by creation or destruction.

**A clean constitutive law governs the balanced current in each sector.** With $M=N-1=n_{R5}+n_{R6}$: $J_{\rm rest/v1}=2M-n_{R6}=2n_{R5}+n_{R6}$, and $J_{v2}=2M=2n_{R5}+2n_{R6}$, both exact across all 304 mature-$v_1$ and 304 mature-$v_2$ rows, with $B=D=0$ throughout. Each R5 bond contributes exactly two incidence crossings per macro-round in *either* moving sector; each R6 bond contributes one at rest/$v_1$ and two at $v_2$ — the entire sector difference localizes to $\Delta J_{R6}=+1$ per R6 bond, with R5 completely unaffected, consistent with everything established about R5's speed-invariance since Y79.

**The round-3 transition is no longer just a timing observation — it is now a resolved two-step transient.** Round 2 remains in the low-current regime. On round 3, the *inward* current switches to its $v_2$ value while the *outward* current has not yet caught up, producing exactly one round of inflow/outflow mismatch and the observed $\Delta I=n_{R6}$ jump — the frozen Y115 prediction, now validated with no coefficient change in all 38/38 species/context cases, including every mixed-N5 chain in both replication contexts. By round 4 the outward current reaches the new value too, and the boosted occupancy becomes stationary again. A broader discovery-then-validation sweep found 80 exact nonzero affine current laws in $(N{-}1,n_{R6})$, of which 72/80 validate blindly; the 8 exceptions are confined to specific first-cut scheduler/order transients (`e0`, `e4`, branch round 1) in R5-containing replication histories, and none of them produces any occupancy discontinuity.

**Formation independently reinforces Y114's key finding.** For D2R5/D2R6 in both contexts, genuine source/sink activity occurs only in the early unbonded preparation transient; the mature $v_2$ current is reached by preseed round 7 at the latest; the explicit bond seed itself changes none of the $O_1$/$O_3$ scaffold current variables in 4/4 cases; and all 48 post-seed settle rounds sit exactly at the mature current with zero births or deaths — independent confirmation that the native scaffold transport is already established before the explicit seed fires.

**A post-verdict diagnostic, widening from the $O_1$/$O_3$ subset to all eight native Y33 outputs, reveals a richer structure the narrower scaffold current had been hiding.** The complete rest-to-motion branch obeys an exact two-stage current ladder in 608/608 rows. For a $v_1$ future, the native current makes a *round-trip* excursion — rising by $n_{R6}$ at round 1, then falling back by $n_{R6}$ at round 2, settling at $3M-2n_{R6}$. For a $v_2$ future, it rises by $n_{R6}$ at round 1, reaches an intermediate balanced plateau at round 2, rises by $n_{R6}$ again at round 3, and settles at $3M$ from round 4 onward. The $O_1$/$O_3$ scaffold current is therefore not an independent phenomenon — it is the second step of a broader native-output transport reconfiguration, and $v_1$ versus $v_2$ launches are now distinguished by a genuinely different current *shape*, not just a different final value.

**A standard-physics-vocabulary reading is now included as a matter of course, with its scope stated precisely.** Y116 frames the result as a discrete continuity equation plus a sector-dependent constitutive current: a state can have constant occupancy while carrying nonzero balanced flow (steady current with $\partial_t\rho=0$), exactly the structure found here, with the rest/$v_1$ and $v_2$ sectors behaving as two transport regimes and the transition as a one-round charging-style transient. Y116 is explicit that these are structural analogies, not identifications — it has not demonstrated electric current, probability current, stress-energy, momentum flux, mass, or energy; it has established the kind of discrete continuity-plus-constitutive structure such quantities are often built from in standard physics.

**Verdict: EXACT_SECTOR_DEPENDENT_INCIDENCE_CURRENT_LAW (primary, 38/38 boost prediction, 76/76 constant moving groups); EXACT_TWO_STAGE_NATIVE_CURRENT_LADDER (post-verdict, 608/608).** The energy/inertia firewall remains closed.

**Recommended next stage (Y117 — Bond-Local Current Decomposition).** Stop fitting global constituent counts; derive the current from individual bond neighborhoods. For each R5 and R6 bond, follow the exact native relation instances through the rest/$v_1$/$v_2$ transition and build a local incidence transfer table. Test whether each R5 contributes a fixed local current independent of chain position; whether each R6 contributes exactly the low- and high-sector increments Y116 inferred globally; whether the two-stage native ladder decomposes as a sum of independent per-bond channel activations; whether the result survives arbitrary N5 bond ordering and replication context; and whether the law can be expressed without $O$-index labels at all, using only local relation/core incidence and causal producer structure. Only after a local grammar derivation succeeds should recurrence-energy or inertia comparisons be reconsidered.

### 10.1rrrr Both occupancy and current collapse exactly to a sum of two independent, position- and neighbor-blind local bond laws — the strongest locality result the composite program has produced (Stage Y117)

Y117 asks whether Y116's global current laws are genuinely local and additive at the individual-bond level, or only an affine fit that happens to look linear in $n_{R5},n_{R6}$.

**Every migration event is bond-local, with zero exceptions.** Across the complete population (discovery: 7 original composites, primary context; blind validation: the same 7 in replication context plus all twelve N5 chains in both contexts), every single $O_1$/$O_3$ touch-class migration is attributable to exactly one adjacent bond slot: 1,596/1,596 global transitions reconstruct exactly by summing bond-slot currents, 5,292/5,292 local continuity rows hold exactly, and there are zero nonlocal events, zero nonadjacent or multi-core occupancies, and zero direct slot-to-slot transfers anywhere in the tested population.

**The entire composite program's current behavior reduces to a two-entry lookup table.** Every R5 bond, in every tested position and neighbor environment, carries $(I_5,J_5)=(3,2)$ in *both* moving sectors — completely unchanged by speed. Every R6 bond carries $(I_6,J_6)=(1,1)$ at rest/$v_1$ and $(2,2)$ at $v_2$, with the round-3 transition occurring independently, identically, and simultaneously at every R6 slot: $1\to2$, $J_{\rm in}=2$, $J_{\rm out}=1$, storing exactly one occupancy unit locally before the outward current catches up on round 4. Summing these two fixed local objects over any tested chain exactly reproduces every global law from Y113 through Y116, with no species-level fitting anywhere. Position independence (32/32) and neighbor independence (72/72) both hold exactly across every tested terminal and interior slot and every observed R5/R6 neighbor combination.

**The known scheduler transients are handled with the same care as before, and shown to be genuinely inconsequential.** 4,534 of 4,662 validation rows match the primary-discovery signature exactly; all 128 misses are confined precisely to the four cuts already flagged as scheduler/order-sensitive (rest `e0`/`e4`, branch-$v_1$/$v_2$ round 1, R5-containing replication only). The R5 transient at these cuts simply swaps order between primary and replication context (the pair $(2,1)$ becomes $(1,2)$) while the two-cut integrated total stays exactly 3 either way — a phase reordering with zero effect on occupancy, locality, or the promoted mature-sector law.

**A post-verdict diagnostic makes real, if partial, progress on the long-standing label-free question.** Every $O_1$/$O_3$ migration event is reclassified using only immutable causal-producer gate roles and current core incidence — never the arbitrary numeric output-slot name — via one of two structural patterns (a producer root retaining one target while gaining a fresh one; a fresh vertex becoming source to the producer's original target pair). This reclassification is exact in all 23,776 combined discovery and validation events, zero false positives or negatives. It is explicitly not yet fully grammar-role-free — the classification still names specific Y33 rewrite roles — but it removes the arbitrary $O$-index labeling that had been the most obviously "coordinate-dependent" part of the construction since Y113.

**Verdict: EXACT_ADDITIVE_BOND_LOCAL_TRANSFER_LAW (primary); O_INDEX_FREE_GATE_INCIDENCE_RELAY_EQUIVALENCE (post-verdict).** $M_i$, $\alpha$, and every mass/energy/momentum/charge interpretation remain sealed. Y117's own synthesis of Y113–Y117 is worth stating directly: the R6 contribution is not a mysterious property of the whole composite — it is localized identically at every R6 neighborhood, which means the problem the investigation actually needs to explain has shrunk from an arbitrary N-body chain formula down to exactly two local objects, R5 and R6, recovered by simple addition.

**Recommended next stage (Y118 — Minimal Bond-State Automaton and Grammar Derivation).** Stop fitting local current amplitudes empirically; derive them. For isolated, quotiented R5 and R6 neighborhoods (translation-invariant, absolute-vertex-ID-free, irrelevant-remote-vacuum-free), enumerate the complete local transition graph through rest, $v_1$, $v_2$, and the rest-to-$v_2$ step, and ask whether $(I,J)=(3,2)$ for R5 and $(1,1)\to(2,2)$ for R6 follow as exact consequences of the local grammar rather than remaining empirical measurements. Identify the smallest local state variable that distinguishes the low- and high-sector R6 regimes, and test the resulting automaton blindly inside the N5 chains with no reference to bond position or neighbor type. If successful, this converts an observed regularity into a finite grammar-level derivation for the first time in this branch.

### 10.1ssss The entire local current law reduces to a four-state causal-role automaton, with R6's kinematic sector distinguished by a single state-defined bit (Stage Y118)

Y118 resolves each bond's counted relations into two literal causal producer-role classes fixed by the grammar itself — $X$: a native relay of the form $x\to\{u,w\}$; $W$: a native relay of the form $w\to\{y,z\}$ — and asks whether the local microstate $S=(n_X,n_W)$, with no O-index, translation, chain-position, neighbor-type, or species label, deterministically generates Y117's link law.

**Isolated discovery on D2R5/D2R6 alone gives a fully deterministic automaton.** 84 discovery rows collapse to 56 unique $(bond, state, input)$ keys with zero nondeterminism. Exactly four microstates occur: $R5{=}(1,2)$, $R6_W{=}(0,1)$, $R6_X{=}(1,0)$, $R6_{XW}{=}(1,1)$. R5 never changes state at all — its entire mature sector-independence is already visible at the state level. R6's kinematic sector reduces to one bit, $q_6=\mathbf{1}[n_X{>}0 \wedge n_W{>}0]$, giving $I_6=1+q_6$ exactly on every discovery and validation row, with the high-sector transition an explicit four-step local sequence culminating in the decisive edge $R6_X\to R6_{XW}$ ($J_{\rm in}{=}2$, $J_{\rm out}{=}1$, zero birth/death) that *is* the Y117 boost, not a fitted coefficient describing it.

**Blind N5 validation is essentially total.** Across 4,032 slot transitions: 4,032/4,032 exact state-set membership (before and after), 4,032/4,032 exact state transitions, 1,680/1,680 exact $I_6=1+q_6$, 640/640 exact mature $J_6=1+q_6$, 40/40 exact R6 round-3 channel-opening edges, and 2,880/2,880 exact full outputs in the promoted mature/boost domain. A direct live-simulator cross-check on 14 independently rerun N5 cases confirms the reconstruction in all 1,456 slot transitions. The only 112/4,032 full-output misses are exactly the already-known R5 scheduler/order transients (replication `rest e0`/`e4`, branch-$v_1$/$v_2$ round 1) — the state and its transition remain exact at all 112, only the output amplitude wobbles.

**Verdict: FINITE_LOCAL_RELAY_AUTOMATON_VALIDATED**, with the secondary result **R6_ONE_BIT_CHANNEL_STATE**. An all-phase, scheduler-independent automaton is explicitly not promoted, since the 112 R5 amplitude misses remain unexplained by state alone.

**Recommended next stage (Y119 — Symbolic Relay Closure and Local Scheduler-Order Completion).** Derive $X$/$W$ from the literal Y33 input/output tuples rather than sampled trajectories; introduce only a local relative update-order bit $\kappa$ (no context label); test whether $(state,phase,\kappa)$ closes all 112 remaining R5 transients while leaving the 3,920 already-exact rows unchanged; formally minimize both the four-state role-resolved and the coarser three-state constitutive automata.

### 10.1tttt A single local scheduler bit closes the automaton exactly — the R5 transients are order-boundary bookkeeping, not a fifth material state, and X/W are proved literal grammar objects (Stage Y119)

Y119 shows the two relay classes are not an empirical fit at all: inspecting the literal eight native Y33 outputs, exactly two satisfy the $X$/$W$ predicates, and the frozen Y44/Y46 rest-suppression mask is $\{1,3\}$ — precisely those two outputs — so an ordinary mature rest fire creates neither relay, independently confirming $B=D=0$ for the scaffold sector from the grammar's own text rather than only from measurement.

**One local input variable — no context label — closes every remaining ambiguity.** Defining $\kappa=\pm1$ from which of the two adjacent constituents updates first, the isolated D2R5/D2R6 corpus (both bond types, both local orders) yields 112 unique $(bond, n_X, n_W, phase, \kappa)$ keys with zero nondeterminism. Applied blind to all 4,032 N5 slot transitions: 4,032/4,032 exact, preserving all 3,920 previously-exact Y118 rows and correcting all 112 order transients with no new state and no changed dynamics. Formal partition-refinement minimization confirms both automata are exactly minimal on the tested reachable language: four states if relay orientation is retained, three if only the constitutive occupancy/current is kept.

**Interpretation is precise and appropriately scoped.** R5 never leaves $(1,2)$; the transient is one balanced $X$-relay circulation landing on one side or the other of a measurement boundary depending on local update order — an intermediate-flux/operator-splitting artifact, not a stored degree of freedom. Y119 states explicitly that this is a finite **on-manifold** grammar theorem, conditional on the frozen DS001 phase/action program, not an unconditional statement about every legal off-manifold Y33 history.

**Verdict: SYMBOLIC_LOCAL_TRANSDUCER_CLOSED_WITH_ORDER_BIT**, secondary **R5_TRANSIENTS_ARE_ORDER_BOUNDARY_EFFECTS**. $M_i$, $\alpha$, and all mass/energy/momentum/charge quantities remain sealed.

**Recommended next stage (Y120 — Nonlinear-Topology Transfer).** The linear-chain finite-state problem is closed well enough that further chain extension adds little. Deliberately change topology: test whether the frozen Y119 transducer, applied unchanged, survives an imposed loop or degree-3 junction, on the current lineage-aware (not the older Y106) preparation manifold.

### 10.1uuuu An imposed nonlinear edge never enters the relay automaton at all — existing tree edges are completely unaffected, sharpening "no closed loops" into "no causal-relay realization" (Stage Y120)

Y120 rebuilds the Y106/Y107 loop-closure question on the current provenance-resolved manifold (T3/T4 mature-$v_2$ parents) rather than the older, non-lineage-aware preparation, after a pilot showed an old-style R5 edge need not carry the native relay state the current transducer requires.

**Every legal nonlinear seed fails to become a dynamical bond, while every pre-existing edge is untouched.** Of 88 attempted nonadjacent K3/C4/junction geometries, 30 are legal under the frozen motif-transfer rules (all 44 R6 attempts are mechanically illegal; 30/44 R5 attempts are legal). None of the 30 legal seeds ever enters a Y119 relay state: 180/180 scored transitions sit fixed at $(X,W)=(0,0)$ with zero relay current, and the raw geometric weave (4 cross-relations at seeding) decays to zero within two rounds in all 30 cases — the same causal non-renewal mechanism Y107 found, now re-expressed exactly in the Y119 relay language. Simultaneously, all 26 pre-existing tree edges begin and remain in their exact frozen states across 492/492 scored transitions, with 180/180 global currents reconstructing exactly as the unperturbed sum ($J{=}2(N{-}1)$) and zero multi-core native relays anywhere.

**Interpretation is deliberately narrow.** Y120 explicitly does not claim loops are forbidden — every tested nonlinear edge is also a long-range edge in the current one-dimensional carrier coordinate, so topology and locality are confounded in this experiment. What is established precisely: the obstruction occurs *before* a nonlinear constitutive element can exist at all (no causal-relay realization), not as a correction applied to an otherwise-valid edge.

**Verdict: NONLINEAR_EDGE_FAILS_AT_RELAY_REALIZATION**, companion **EXISTING_TREE_TRANSDUCER_UNAFFECTED**.

**Recommended next stage (Y121 — Maximum Renewable Coordination / Locality-Topology Decoupling).** Ask a more fundamental local question before seeding more long-range edges: how many simultaneous Y119-valid relay neighbors can one DS001 constituent support at all, under the unchanged one-dimensional geometry? Determine whether this yields an effective maximum coordination number, and whether it follows from local packing rather than bond competition.

### 10.1vvvv A sharp geometric coordination bound, $z_{\max}=2$, is found and shown to be dynamically saturated — not a competition effect but a packing fact about the carrier's own five-site support (Stage Y121)

Y121 defines coordination strictly as simultaneous occupancy of a Y119-valid relay state (not raw geometric proximity), and finds the bound is set before any bond dynamics are even tested.

**The packing bound is exact and purely geometric.** A DS001 constituent occupies five consecutive old-vacuum sites; the only qualified local bond radii are 5 and 6, giving candidate offsets $\{-6,-5,+5,+6\}$. The two same-side placements at each distance overlap in four of five vertices, so every same-side pair and all four degree-3 subsets are illegal by direct support-overlap — a 16-subset exact census shows the largest disjoint neighbor set has size 2, with no dynamics consulted yet.

**Degree 2 is not just the geometric ceiling — it is robustly, dynamically achievable.** Testing all four opposite-side layouts ($5$-$5$, $5$-$6$, $6$-$5$, $6$-$6$) across both signs, all six scheduler permutations, and both tie seeds (96 cases): the two layouts with a left R6 interface ($6$-$5$, $6$-$6$) form and sustain two simultaneous independent Y119-valid edges in 48/48 contexts, with 768/768 scored edge transitions exact and zero native relays touching three or more cores. The two layouts with a left R5 interface fail formation in all 48 remaining contexts — but a direct diagnostic shows this is the already-known directional R5 seed-geometry obstruction (a specific auxiliary old-vacuum site collides with an existing core), not competition between bonds: the same R5 motif coexists perfectly with a left R6 in the passing $6$-$5$ case.

**Verdict: GEOMETRIC_COORDINATION_BOUND_Z2** — deliberately not "dynamic," since no legal degree-3 candidate ever reaches the point where dynamical competition could even be tested; all four degree-3 subsets fail the geometric disjoint-support gate before any bond seed is attempted.

**Recommended next stage (Y122 — Local Contact-Direction Atlas / Multidimensional-Junction Search).** Stop assuming the scalar carrier coordinate captures every possible local contact. Enumerate legal second-carrier placements directly from the local graph/gate neighborhood — not scalar displacement — quotiented by translation and causal-role symmetry; build the resulting contact-compatibility graph and compute its maximum clique. A clique of size $\ge3$ would be the first genuine, geometry-independent degree-3 junction candidate; a clique of exactly 2 would move the coordination bound from a one-dimensional packing fact toward a grammar-level locality statement.

### 10.1wwww The graph-local search independently rediscovers exactly the same four contacts and the same coordination bound — the result is no longer an artifact of the scalar carrier coordinate (Stage Y122)

Y122 builds candidate neighbor supports entirely from local graph structure — 5-cliques of old-vacuum vertices within graph distance 2 of the central core, touching the distance-1 shell — with no arithmetic offset condition, and no explicit bond seed: a candidate counts only if ordinary $v_2$ evolution alone carries it into a genuine Y119 relay state.

**Of 50 graph-local candidate supports (30 distinct oriented causal-role classes), only the four historically known contacts survive full bidirectional validation.** A primary screen finds 6 candidates with perfect relay behavior — the four familiar contacts plus two genuinely novel noncontiguous supports. Full validation (48 rows: both signs × both local orders × both ties) reduces this to exactly 4 robust contacts, each 8/8; the two novel candidates form exact relay states under one propagation sign only, collapsing to $(X,W)=(0,0)$ under the reverse sign, and are excluded as direction-conditioned rather than bidirectionally robust local directions — a genuinely new diagnostic (a directed causal-cone signature) flagged for future work rather than folded into the coordination count.

**The resulting compatibility graph is exactly $K_{2,2}$, with the same-side pairs excluded by direct support overlap and every opposite-side pair passing full simultaneous three-carrier dynamics.** All 4 geometrically eligible opposite-side pairs pass all 48 compatibility contexts, 288/288 scored macro-rounds, and 576/576 individual edge transitions, with zero required junction correction — giving an exact maximum clique $\omega=2$.

**Verdict: GRAPH_LOCAL_COORDINATION_BOUND_Z2_SUPPORTED, scope-flagged FINITE_ON_MANIFOLD_GRAPH_SHELL_RESULT.** The crucial logical reversal from Y121: Y122 did not start from the known offsets and confirm their packing — it searched the compact local graph shell blind to those offsets and found the same four directions emerge as the *only* robust ones. The coordination-two result is therefore no longer contingent on how the carrier happens to be parameterized; it is supported directly by the local causal/graph contact structure itself, though still only established within a finite, on-manifold, radius-2 shell.

**Recommended next stage (Y123 — Directed Contact Cone and Symbolic Locality Boundary).** Keep the Y122 contact and Y119 relay definitions frozen; extend the compact-support atlas to graph radii 3–4, classifying every contact as bidirectionally robust, positive-only, negative-only, or nonrenewable; investigate whether the one-direction-only contacts form a genuine finite directed causal cone tied to the old-vacuum gate sequence; attempt a grammar-level (not trajectory-executed) predicate for relay renewal; and test whether the bidirectionally robust set remains exactly the same four directions as the shell is enlarged — which would move the coordination bound from a finite census toward an actual symbolic locality theorem.

### 10.1xxxx The bidirectional contact set is stable through graph radius four, establishing a genuine finite-range renewal boundary — but the static contact signature is proven insufficient to predict it (Stage Y123)

Y123 extends the Y122 atlas from radius 2 to a cumulative radius-4 census of 152 compact five-vertex candidate supports (50 at each of distances 1–3, 2 at distance 4) around the same central DS001 core, with the Y119 relay criterion held fixed.

**No new bidirectional contact ever appears, and no outer-shell candidate renews at all.** The four Y122 contacts remain the *only* bidirectional survivors among all 152 candidates; full eight-way (sign × order × tie) validation of every primary-screen survivor gives exactly 4 bidirectional, 2 positive-only, 6 negative-only, and 140 nonrenewable. Every one of the 102 candidates whose nearest vertex sits at graph distance $\ge2$ fails to renew under either sign (0/204 primary sign screens at the discovery center, and again 0/204 at each of two translated centers) — a result Y123 states precisely: touching graph distance 1 is *necessary* for renewal (radius-1 boundary), though not sufficient (38 of 50 radius-1 candidates still fail).

**A genuine, honestly reported insufficiency closes the stage rather than a forced classifier.** Two candidates — supports `706..710` (bidirectional R6) and `706,707,708,709,711` (negative-only R6) — share an identical frozen static role-signature hash and identical declared aggregate features, yet have different renewal classes. Y123 explicitly declines to invent a post-hoc variable to paper over this; it is reported as a clean insufficiency result.

**Verdict: BIDIRECTIONAL_CONTACT_SET_STABLE_THROUGH_R4** (primary); **RADIUS1_NECESSARY_RENEWAL_BOUNDARY** (secondary); **GRAPH_ROLE_LOCALITY_PREDICTOR_NOT_CLOSED** (negative, load-bearing for the next stage).

**Recommended next stage (Y124 — Causal-Age Completion of the Local Contact State).** Keep the static Y123 signature frozen; add only pre-existing causal-history information (producer-event ancestry, relative causal age/order, old-vacuum gate-role sequence) as a minimal augmentation; search for the smallest translation-free addition that separates the exact witness pair and predicts all 12 renewable/directional classes; freeze before testing the 140 nonrenewable holdouts; ask whether the augmented state is Markov-complete for relay renewal.

### 10.1yyyy One small causal-age variable — not a large hidden environment — closes the entire finite contact classifier exactly, including at three translated centers (Stage Y124)

Y124 tests a preregistered hierarchy of causal-age augmentations against the Y123 no-go, using only the 12 renewable/direction-conditioned contacts as the development population and the historical 140 nonrenewables as a feature-selection holdout.

**A one-bit augmentation is deterministic on discovery but generalizes badly — a useful, honestly reported failure.** A continuity bit ("are the five support vertices consecutive fresh-vertex births?") separates the witness pair and closes 12/12 on development, but falsely promotes 5/140 holdout nonrenewables — too coarse to trust.

**The successful variable retains ordering, not just presence, of a birth-order defect.** Defining the four birth-order gaps of a sorted support and recording $\eta=0$ (fully consecutive), $\eta=k$ (a single one-step slip at gap position $k$), or $\eta=9$ (anything else) gives the frozen key $K=(H_{\rm role},\eta)$. This closes the complete center-700 atlas exactly: 12/12 development, 140/140 holdout, 152/152 total, with the exact witness pair separated (candidate 81: gaps $(1,1,1,1)$, $\eta{=}0$; candidate 82: $(1,1,1,2)$, $\eta{=}4$).

**Translation and dynamic re-validation are total.** The key reproduces at centers 500 and 900 in all 304 translated rows; dynamic replay confirms all 12 development classes, all 102 outer-shell nonrenewables, and — newly executed — all 38 radius-1 nonrenewable holdouts remain nonrenewable at both translated centers (0/76 each), giving 304/304 combined dynamic class agreement.

**Verdict: FINITE_CAUSAL_AGE_CONTACT_STATE_CLOSED**, with frozen key $K=(H_{\rm role},\eta)$, scope-flagged as a finite P157-radius-4 result, not a universal theorem.

**Recommended next stage (Y125 — Producer-Ancestry Derivation of the Causal-Age Slip).** $\eta$ is still a numerical-arithmetic coordinate (a difference of fresh-vertex integer labels). Derive the same phase directly from the literal Y33 rewrite ancestry — which event created each vertex, and how creator events are connected by gate roles — with no vertex-ID arithmetic at all, and test whether the resulting label reproduces $\eta$ exactly across the full atlas and translated centers.

### 10.1zzzz The causal-age coordinate is not an arithmetic accident — it is a literal recurrent producer-event spine embedded in the grammar's own gate-role structure (Stage Y125)

Y125 discovers that the qualified vacuum's creator events form one uninterrupted causal chain under a literal gate-role relation, then rebuilds $\eta$ from that chain alone.

**The vacuum has an exact recurrent producer spine, verified directly from the raw event record.** For every successive pair of `VACUUM_FIRE` events, the fresh vertex $w$ produced by one event equals the $v$-role input of the next gate: 1799/1799 successive pairs. After a five-event startup transient, every gate's five roles trace back fixed numbers of spine steps, $(x,y,z,u,v)=(3,5,2,4,1)$ predecessor-lags, holding in 1795/1795 later events; the three consumed input relations likewise have a fixed one/two-step producer pattern, holding in 1798/1798 events.

**A vertex-ID-free label built from this spine exactly reproduces $\eta$.** Recovering each support vertex's unique creator event from the literal Y33 outputs (1800/1800 events, no ID arithmetic), ordering those creators along the spine, and recording whether all four neighbor-pairs are direct spine successors ($\xi{=}0$), exactly one is separated by one intervening event ($\xi{=}k$), or otherwise ($\xi{=}9$) gives $\xi=\eta$ in all 152/152 center-700 candidates. The rebuilt key $K_A=(H_{\rm role},\xi)$ closes the atlas identically (12/12, 140/140, 152/152) and now also translates to a newly-tested confirmatory center 1100, with 456/456 static key rows exact across all three translated centers and a full new dynamic confirmation at center 1100 (152/152 classes, matching the same 4/2/6/140 census).

**Verdict: PRODUCER_ANCESTRY_CONTACT_STATE_CLOSED**, secondary **V_ROLE_CAUSAL_SPINE_PHASE_EQUIVALENCE** — the causal-age variable is now shown to encode a real finite-memory recurrence of the underlying rewrite grammar, not an artifact of how vertices happen to be numbered.

**Recommended next stage (Y126 — Hash-Free Symbolic Contact-State Minimization).** The remaining opaque piece is the Y123 static role-signature hash itself. Expand it back into its declared translation-free components and search for the smallest explicit, human-readable feature set that, together with $\xi$, still closes the complete classifier — replacing a cryptographic hash with a transparent grammar-role predicate if possible.

### 10.1aaaaa The opaque 21-component role hash collapses to exactly two explicit, oriented crossing-relation counts — the complete local contact state is now fully transparent (Stage Y126)

Y126 exhaustively minimizes the three symbolic blocks (13 vertex-role, 7 relation-role, 1 gate-role categories) originally compressed into the Y123 hash, with $\xi$ held fixed throughout.

**Coarse scalar totals fail; only the fully role-resolved relation block succeeds.** A single best-available scalar total (summed degree into the center) closes development but falsely promotes 2/140 holdouts. Of the three literal symbolic blocks, both the full vertex-role multiset and the full relation-role multiset independently close the atlas exactly, while the gate-role block alone does not — establishing directly that no crossing-gate descriptor is needed once ancestry phase and relation-role structure are known, and that the smaller 7-category relation block is the preferred minimization parent over the 13-category vertex block.

**Exhaustive search over all 21 atomic components finds a unique two-feature minimum.** No zero- or one-feature augmentation to $\xi$ closes the full atlas; exactly one two-feature solution does: $A=N_C^{(2,1)}$ (central-sourced crossing relations touching two central and one candidate vertex) and $B=N_Q^{(1,1)}$ (candidate-sourced crossing relations touching one central and one candidate vertex, with the third vertex exterior). The complete explicit state is $\Sigma=(\xi,A,B)$ — three plain numbers, no hash, no absolute position, no post-evolution observable. This closes the center-700 atlas exactly (152/152: 0 false renewables, 0 missed renewables, 0 relay-identity errors, 0 directionality errors) and is fully translation-portable: all three components reproduce exactly at centers 500, 900, and 1100 (456/456 rows), agreeing with the independently-frozen translated dynamics at every one of those cases.

**Verdict: HASH_FREE_SYMBOLIC_CONTACT_STATE_CLOSED**, with explicit state $\Sigma=(\xi,A,B)$ — a genuine state reduction (21 atomic categories down to 2, once $\xi$ is retained), not merely a re-encoding of the same information.

**Recommended next stage (Y127 — Recurrent-Phase Portability of the Explicit Causal Contact State).** Test whether $\Sigma$ is a genuine phase-independent constitutive state of the DS001 lifecycle, or tied specifically to the P157 preparation boundary on which it was discovered: identify other exact recurrent phase boundaries, rebuild the same atlas there without using the P157 outcomes, and ask whether the unchanged Y126 law still predicts renewability, relay class, and directionality.

### 10.1bbbbb The explicit contact state does not port across the recurrent lifecycle — $(A,B)$ are section coordinates on one phase of the orbit, not a covariant state, closing this sub-thread with a precise, informative negative (Stage Y127)

Y127 tests portability at two levels, both negative, and diagnoses exactly what kind of negative each is.

**Direct transplantation of a mature phase into raw vacuum is not even executable.** The recurrent five-core lifecycle collapses to only two internal templates ($P_+$: $+v_1\equiv+v_2$; $P_-$: $-v_1\equiv-v_2$; the sampled rest cuts use the same two templates). Inserting $P_+$/$P_-$ directly into fresh vacuum and continuing with the matched signed rule gives zero legal carrier gates at the entry cut in every case (0/304 across the full candidate population) — a mature phase is not a self-contained state specification detached from the history that produced it.

**The decisive result removes any transplant ambiguity: even genuine, dynamically-reached mature states fail.** Following the 16 known-good Y123 primary passing trajectories from their P157 origin into the actually-realized mature phase by unchanged dynamics, and recomputing $(A,B)$ there, the unchanged 12-key Y126 table predicts correctly in 0/16 cases. The lifecycle's own maturation genuinely changes the local crossing-relation dressing, so $(A,B)$ at the mature section is not the same coordinate that indexed the contact at P157 — the raw relation counts are section-dependent, not phase-invariant.

**Verdict: UNCHANGED_SIGMA_NOT_PHASE_PORTABLE**, companion **MATURE_PHASE_TRANSPLANT_NOT_INDEPENDENTLY_EXECUTABLE**, interpretive **CONTACT_STATE_REQUIRES_LIFECYCLE_PHASE_TRANSPORT**. Y127 is explicit about what this does and does not mean: it does not show the R5/R6 contact identity ceases to exist at the mature phase (it's already known to persist dynamically) — it shows the *P157 symbolic coordinates* used to classify it are not unchanged invariants across the lifecycle. The natural dynamical-systems reading is a Poincaré-section coordinate: highly predictive on one section, not conserved, and requiring an explicit transport map to compare across sections.

**Recommended next stage (Y128 — Phase-Covariant Transport of the Local Contact State).** Do not fit independent tables at $P_+$ and $P_-$. Follow relation-instance lineage through the exact, unchanged maturation path for each P157 development contact and record the deterministic transformation of the crossing-relation role counts (especially $A,B$); treat the phase label as an input to a transport map, not an extra identity label; search for the smallest phase-conditioned map that pulls mature states back to their original P157 coordinate; freeze it on the 12 development contacts before testing the 140 nonrenewables and translated centers; and, if successful, test whether it also transports the Y119 relay state/current consistently through rest/$v_1$/$v_2$ boundaries.

### 10.1ccccc A causal-ancestry pullback restores exact phase covariance for the contact state — but the transported information lives in the wake, not the mature interface, exposing a sharper sufficiency question (Stage Y128)

Y128 asks whether Y127's failure is repairable by causal lineage rather than by fitting a second table.

**Root-label propagation closes the transport exactly.** Each P157 $A$/$B$ relation instance receives an immutable root label; labels propagate only through recorded producer→consumer ancestry (an event's output inherits the union of its inputs' roots). The pulled-back state $\Sigma_\leftarrow=(\xi,A_\leftarrow,B_\leftarrow)$ — counting *distinct live roots*, not raw relation counts — reproduces the original P157 coordinates exactly: 16/16 development, 154/154 executable primary rows (the remaining 150 rows exit during preparation with zero historical passes, giving 304/304 on the complete historical population), 112/112 across six additional mature rounds, 48/48 at three translated centers, and 16/16 at a post-verdict confirmatory center never used to derive the rule.

**The decisive, counterintuitive finding is where the transported information does *not* live.** Across all 16 passing developments, zero mature cross-core relations carry any original root ancestry — the successful R5/R6 relay is entirely freshly regenerated by ongoing dynamics. The roots instead persist in the causal wake, each touching at most one current core, never both.

**Verdict: ROOT_ANCESTRY_PHASE_PULLBACK_CLOSED**, companion **PHASE_COVARIANCE_REQUIRES_CAUSAL_WAKE_MEMORY**, explicit caveat **NOT_YET_AN_AUTONOMOUS_CURRENT_STATE_LAW** — the pullback relies on externally-carried lineage tags from the Y96 recorder, not on anything the raw current relational state contains by itself. Y128 is explicit this is a provenance/history-transport result (Eulerian vs. Lagrangian, in its own stated analogy), not a new local conserved density: instantaneous $A,B$ counts and even descendant-relation counts are *not* conserved — only causal-root set membership is.

**Recommended next stage (Y129 — Intrinsic Wake-State Closure).** Do not fit a more elaborate historical label. Remove the passive root IDs entirely and search, in increasing information order (bounded current wake topology, then current producer-role channels, then bounded ancestry depth only if needed), for a translation-free description of the current relational state alone that reconstructs $(A_\leftarrow,B_\leftarrow)$. Measure the minimum wake radius or ancestry depth required. If a finite bounded encoding exists, replace the passive ledger with it; if not, promote the negative result explicitly — the contact description is genuinely non-Markovian at this resolution.

### 10.1ddddd The P157 identity is recoverable from the current relational state alone, with no external tags at all — but only by looking arbitrarily far into a receding wake, resolving the whole sub-thread into a clean formation-memory/bound-state analogy (Stage Y129)

Y129 removes Y128's passive root IDs and asks whether the same reconstruction survives using only intrinsic current structure.

**A raw-topology and a small producer-count key are both tried and correctly rejected without refit.** Complete radius-2 wake topology collides (two candidates share an identical signature but require different $(A,B)$); a compact producer-aware key separates the 16 development histories perfectly but reconstructs only 16/154 executable rows and is discarded rather than patched.

**The successful construction finds literal physical fossils.** Each prepared carrier leaves a persistent five-vertex, nine-relation remnant of its original P157 support still present in the current relation set (the positive- and negative-type fossils differing from the full P157 support by exactly two relations each). Feeding the fossil's five old-vacuum vertices into the unchanged Y125 creator-event spine re-derives $\xi$ correctly in 154/154 rows; recomputing $A,B$ directly from currently-live vacuum-produced relations, extended at most one causal generation backward for consumed roots (9/154 rows need this repair for $A$; $B$ never does), reconstructs the target exactly in all 154 executable rows, giving the same 304/304 complete historical result and 400/400 across 24 additional mature rounds, with 64/64 across four translated centers including 40/40 on translated nonrenewable rows never used in derivation.

**The clean success comes with an equally clean locality failure.** The fossils do not comove with the carrier — the graph radius needed to still contain both recedes according to an exact tested envelope, $R_{\max}(r)=3+\lceil r/3\rceil$, growing from 3 to 11 over the 24 rounds observed. No fixed-radius local neighborhood suffices; this is a measured, bounded-horizon empirical law, not an asymptotic proof, but it directly rules out a fixed-radius closure over the tested motion.

**Verdict: PASSIVE_ROOT_ID_ELIMINATION_CLOSED** (primary — external tags are not required; the information is genuinely intrinsic to the substrate), **NO_FIXED_RADIUS_INTRINSIC_WAKE_STATE** (secondary), **FORMATION_MEMORY_RECEDES_IN_CAUSAL_WAKE** (interpretive).

**Interpretation.** Y129 resolves the Y123–Y129 arc into a coherent physical picture, drawn explicitly from bound-state/scattering formation rather than from a conserved-order-parameter framing: initial encounter parameters need not become internal state of the resulting bound object. They can instead persist in an outgoing/receding environmental record while the bound object itself settles into a smaller, genuinely local, autonomous description — which, read this way, is exactly what the already-established Y119 relay automaton already is. The P157 $(\xi,A,B)$ coordinates are best understood as *formation history*, not missing internal bond state; the eleven-stage attempt to fold them into a phase-independent local law was, in retrospect, aimed at the wrong target — the local law was already complete.

**Recommended next stage (Y130 — Mature Local-State Sufficiency / Formation-Memory Shedding).** Do not drag the P157 coordinates forward again. Test directly whether the Y119 relay automaton (plus scheduler/order input) is already a *sufficient* local description: collect multiple distinct P157 formation histories that converge to the same mature R5 or R6 sector, quotient comoving neighborhoods under translation and causal phase, and test exact equality of every bounded local future transition/current law across those histories, while independently confirming the P157 distinctions remain recoverable only outside the growing comoving neighborhood. Success would formally establish that formation history is shed rather than hidden; failure would mean the mature bond still carries preparation memory the Y119 automaton does not capture.

### 10.1eeeee The mature relay automaton is constitutively sufficient — different formation histories become identical in every future transition immediately, while their surrounding graph dressing converges from the inside outward on a measured schedule (Stage Y130)

Y130 tests directly whether the Y119 relay law is already a complete local description, using all 16 historically-passing Y123 formation histories, partitioned by sign and relay family before measurement.

**Constitutive future equality is exact and immediate.** For every matched (sign, relay, section) group, every tested history has identical $(X,W)$ state, next state, $X$/$W$/total current in and out, source/sink terms, core-role phase, and displacement — 192/192 individual mature transitions at center 700, 192/192 at center 500, 384/384 combined. Different formation histories are constitutively indistinguishable from the very first scored mature boundary.

**The surrounding graph dressing tells a complementary, slower story.** Exact discrete graph-canonicalization (translation-free, absolute-ID-free, fully discrete refinement — so equality is a genuine isomorphism, not a hash match) shows radius-0 is already history-independent everywhere, but larger radii still carry formation-dependent dressing that converges only after a finite, measured delay: worst-case first-convergence sections $(R0,R1,R2,R3)=(0,1,3,6)$, reproduced exactly at both tested centers, with the empirical (not claimed general) pattern $R(R+1)/2$. Once converged, every radius stays converged for every later tested section (332/332 matched-continuation checks).

**Verdict: MATURE_RELAY_STATE_CONSTITUTIVELY_SUFFICIENT**, companion **FORMATION_DRESSING_SHEDS_OUTWARD_FROM_COMOVING_CORE**, scope-flagged **FINITE_MATURE_V2_R5_R6_FORMATION_MEMORY_SHEDDING_RESULT** — not yet established for $v_1$, stationary rest, or unbounded radius. Read together with Y129, the decomposition is now precise: formation history → mature local state (immediately sufficient) + outgoing wake memory (recoverable, receding, dynamically inert). No mass/energy/momentum/spin/gauge/gravity claim is made.

**Recommended next stage (Y131 — Causal Wake-Decoupling Intervention).** Convert observational sufficiency into a causal test. Freeze mature states after radius-3 convergence; clone them; in matched clones surgically delete only the detected P157 formation fossils (never touching a current core or marker relation); run identical scheduler inputs for at least 12 mature rounds; require exact equality of Y119 state/current, displacement, and bounded comoving neighborhoods against an untouched control. Separately test progressively nearer wake shells to locate any true causal backreaction boundary. A clean null under fossil deletion would make the shedding interpretation causal rather than merely correlational.

### 10.1fffff Direct surgical deletion proves the formation-memory fossil is causally dispensable, while a complementary control confirms the generic surrounding vacuum is not — cleanly separating memory from dynamical support (Stage Y131)

Y131 escalates Y130's observational sufficiency into an actual intervention, cloning each mature state at the common radius-3 convergence section and comparing deletion branches against an untouched control from identical scheduler and RNG state.

**Deleting the formation fossil outright changes nothing.** S1 removes exactly the 18 relations wholly internal to the two rediscovered P157 fossils (no core- or marker-touching relation is ever eligible) and produces zero measured effect over 12 mature rounds: 416/416 matched local states, 384/384 exact future transitions, combined across both tested centers. A Method Correction caught and discarded a flawed pre-freeze implementation (an over-broad deletion rule that removed 31 relations instead of 18) before any scientific output existed.

**A much stronger deletion — the fossil's entire attached relation-star (89–109 relations per history) — still produces no constitutive effect**, though it does leave one honestly-reported, tightly localized trace: 416/416 Y119-state and 384/384 transition equalities hold exactly, while the strictest possible complete local-state comparison is 412/416, with the two exceptions confined to the very round of the intervention itself in the outermost tested radius, vanishing by the next round. This is promoted precisely as *constitutive* decoupling, not claimed as complete instantaneous invisibility — a distinction Y131 states explicitly rather than rounding up.

**The complementary control is what makes the null results trustworthy rather than merely convenient.** Deleting the generic exterior environment beyond a protected radius — a deliberately non-formation-specific, much larger cut (thousands of relations) — *does* backreact, on a clean, delayed, radius-dependent schedule that reproduces exactly at a second translated center (protected radius 3: first local deviation at round 2, reaching the core Y119 state at round 11). This confirms the surgical methodology is sensitive enough to detect a real effect when one exists, which is exactly what makes the S1/S2 nulls informative rather than an artifact of an insensitive test.

**Verdict: FORMATION_FOSSIL_CAUSALLY_DECOUPLED_ON_TESTED_MATURE_HORIZON**, companion **FOSSIL_STAR_NO_CONSTITUTIVE_BACKREACTION_THROUGH_12_ROUNDS**, contrasting **FINITE_ENVIRONMENTAL_BACKREACTION_REACH_DETECTED**, scope-flagged **FINITE_MATURE_V2_R5_R6_WAKE_SURGERY_RESULT**. The decomposition is now causal, not just observational: formation record in the wake $\ne$ ambient renewal reservoir required by ongoing motion. The mature pair has genuinely shed dependence on its own formation history, but it is not an isolated closed object — it still structurally depends on ordinary surrounding relational structure to keep renewing.

**Recommended next stage (Y132 — Renewable Environment Shell / Causal Backreaction Propagation Law).** The formation-memory question is closed; the newly-exposed question is different and more fundamental: which ordinary ambient relations does continued carrier renewal actually require, and how does a missing exterior propagate inward? Extend protected radii to at least $R=4,5,6$; track the exact first relation/gate/current discrepancy crossing from shell $R+1$ into $R$; identify whether the propagation is carried by native relay ancestry, the broader Y116 all-native incidence ladder, or another vacuum channel; derive a shell-to-shell causal transfer law rather than fitting delay against radius; distinguish permanent removal from a finite, ordinarily-replenished local defect; and only then test the same mechanism in $v_1$ and the stationary Y46/Y79 sectors.

### 10.1ggggg The delayed environmental backreaction is not a propagating signal at all — it is the carrier's own worldline advancing into a pre-existing static supply gap, with translation itself remaining completely intact even as the relay scaffold fails (Stage Y132)

Y132 extends Y131's exterior cuts to $R=4,5,6$ and asks whether the resulting shell-by-shell timing is a genuine inward-propagating disturbance or something more mundane.

**Kinematics and relay health turn out to be decoupled.** Across all 96 permanent-cut branches (16 histories × 3 radii × 2 centers, 2,880 scored mature transitions, all executable and lineage-clean through 30 rounds), the exterior cut eventually corrupts the mature relay/current state on a radius-dependent schedule — but the selected carrier gate and the actual $v_2$ displacement remain exactly CONTROL throughout, 2,880/2,880 both. Translation is robust well past the point where the relay scaffold has already failed.

**Forensic tracing kills the more exciting-sounding interpretation in favor of the correct, more mundane one.** The naive reading of the shell-timing schedule ($R6{:}2, R5{:}4, R4{:}7,\ldots,R1{:}14$, exact across both tested centers) looks like a signal propagating inward. Direct provenance tracing of the 75 first-missing scaffold relation instances shows this is wrong: all 75 were produced by the ordinary `VACUUM_FIRE` process, all 75 are literally among the relations deleted at the original intervention (not descendants of any inward-traveling disturbance), and all 75 sit at minimum initial graph distance exactly $R{+}1$ from the two cores. Nothing new is created and nothing propagates — the carrier's own worldline simply advances into a static region that was already empty from the moment of the cut. Every one of the 48 first constitutive failures shows the identical continuity signature ($J_{\rm in}<2$, $J_{\rm out}=2$, $B{=}D{=}0$): an incoming-supply deficit, never an outgoing collapse, a birth/death event, or a changed gate.

**A direct provenance audit reveals a genuine, clean asymmetry between the two bond types.** Mature R5 recruits *both* its incoming relay channels (O1 and O3) from pre-existing ordinary vacuum (210/210 each); mature R6 recruits O1 from pre-existing vacuum but regenerates O3 internally from carrier-produced relations. This is why R6 shows a slightly different failure signature from R5 and adds a new, mechanistically-grounded entry to the growing list of exact structural distinctions between the two bond types.

**Finite-defect recovery confirms the encounter interpretation independently.** Deleting only a two-shell annulus (leaving farther vacuum intact) produces a temporary, exact relay defect that fully recovers in every one of 32 tested branches — while zero of the deleted relation tuples is ever recreated. Recovery is reaching intact vacuum beyond the hole, not repairing the hole.

**Verdict: AMBIENT_RENEWAL_SUPPLY_STARVATION_CAUSES_RELAY_LOSS** (primary), **BACKREACTION_IS_WORLDLINE_SUPPLY_ENCOUNTER_NOT_AUTONOMOUS_INWARD_SIGNAL** (companion — a specific, evidence-based correction of Y131's more cautious "delayed inward consequence" language), **FINITE_DEFECT_RECOVERY_BY_REENTRY_INTO_INTACT_VACUUM**, scope-flagged **FINITE_MATURE_V2_R5_R6_ENVIRONMENT_SUPPLY_RESULT**. The working model-internal decomposition is now: mature local relay automaton + renewable ambient native-relation supply along the worldline → exact recurrent bond transport. Y119's local transition rule is not violated by any of this — it is the *input conditions* for realizing the next relay state that can fail.

**Recommended next stage (Y133 — Renewable-Supply Transfer to v1 and Stationary Rest).** Freeze the Y132 supply-channel definitions; do not fit a new environment observable. Repeat the provenance audit for mature $v_1$ R5/R6 (pre-existing-vacuum vs. carrier-produced), with matched finite-annulus and permanent-exterior challenges along the $v_1$ worldline. Transfer the same audit to the exact Y46/Y79 stationary-rest sector, where there is no translational worldline through fresh vacuum — determine whether rest circulation uses a fixed local reservoir, cyclically regenerated relations, or a genuinely different supply mechanism. Compare $v_2$, $v_1$, and rest in one common incidence-continuity language before reopening any mass/inertia interpretation.

### 10.1hhhhh A clean sector dichotomy closes the environmental-supply picture: moving sectors recruit fresh worldline vacuum, stationary rest cycles a bounded radius-1 reservoir, under one unchanged grammar (Stage Y133)

Y133 transfers the Y132 mechanism to mature $v_1$ and exact stationary rest across the complete seven-composite manifold (14 histories in two contexts).

**Mature $v_1$ reproduces the Y132 mechanism exactly, at a slower encounter rate.** All 760 CONTROL incoming O1/O3 crossings are `VACUUM_FIRE`-produced; the resolved law $J_{v1}=2n_{R5}+n_{R6}$ is now known to be entirely ordinary-vacuum-supplied. Permanent exterior cuts at $R=4,5,6$ (42 branches, 2,520 scored transitions) reproduce the identical starvation signature, later than $v_2$'s failures as expected for the slower worldline, with gate selection and displacement exact throughout (2,520/2,520); 14/14 finite-annulus defects recover with zero relation regeneration.

**Stationary rest is a genuinely different mechanism, not a slow version of the same one.** All 1,184 CONTROL incoming crossings are also `VACUUM_FIRE`-produced, but the relation-instance identities repeat exactly period to period and phase to phase in all 14 histories — a bounded local pool cycling in and out of the bond, not a stream of new material. Every cut at $R\ge1$ is completely invisible to the exact rest current, phase state, and displacement across 16 full periods (84/84 branches, 13,440/13,440 phase-current rows exact); only the $R{=}0$ cut, which reaches into the reservoir itself, changes the current — while even then the scripted rest trajectory and zero displacement remain exact. A first-failure trace confirms all missing relations sit at exactly graph distance 1, establishing a tested reservoir boundary. Post-verdict exact additive reservoir laws are recorded for both distinct-instance and revisited-use counts (e.g. $U_{\rm rest}=11n_{R5}+7n_{R6}$).

**Verdict: V1_AMBIENT_SUPPLY_STARVATION_SAME_MECHANISM_LOWER_WORLDLINE_RATE**; **STATIONARY_REST_USES_FIXED_RADIUS1_CYCLIC_VACUUM_RESERVOIR**; synthesis **MOVING_SECTORS_RECRUIT_WORLDLINE_VACUUM_REST_RECYCLES_LOCAL_VACUUM_SCAFFOLD**, scope-flagged **FINITE_COMPLETE_MANIFOLD_V1_REST_ENVIRONMENT_SUPPLY_RESULT**.

**Recommended next stage (Y134 — Environmental Reservoir Conversion During Acceleration/Deceleration).** Freeze the exact stationary reservoir; follow its individual O1/O3 relation instances through the already-qualified rest→$v_1$ and rest→$v_2$ transitions; measure exactly when the fixed cyclic pool stops being reused and worldline recruitment begins; perform the reverse $v_2\to v_1$ transition and determine how R6's mixed internal/vacuum high relay converts to the low-sector vacuum-only relay; ask whether the reconfiguration is additive per bond and species-independent. Only after that transition law is frozen should its relevance to the inertia program be considered.

### 10.1iiiii The rest→motion and v2↔v1 environmental reservoir conversions are exact, bond-local, and fully additive — and they mechanistically explain the R6 kinematic boost first observed many stages earlier (Stage Y134)

Y134 classifies every scaffold relation by source (L: stationary local pool; V: worldline-recruited vacuum; C: carrier-produced) and follows individual instances through all three transitions across the full seven-composite manifold.

**The conversion is exactly bond-local and species-independent.** After conditioning only on transition type, bond family, the already-known scheduler-order bit $\kappa$, and completed macro-round, all 1,440 scored bond-slot rows collapse to 192 unique template keys with zero species ambiguity; summing local occupancy and current reconstructs the global values exactly in 672/672 history-rounds.

**Rest→motion shows the local pool as a finite, exhaustible starting supply, not a permanent attachment.** For both bond families transitioning to $v_1$, the frozen pool supports exactly the first four moving rounds, then zero local-pool use from round 5 onward — the bond fully transfers to worldline recruitment.

**The R6 rest→$v_2$ boost is now explained mechanistically, closing a question open since Y114.** The high-sector channel is not a recycled rest relation: at round 2 the O1 side already transfers to worldline vacuum (V-O1); at round 3 a genuinely carrier-produced O3 channel (C-O3) is added on top of it, giving the exact $J_{\rm in}/J_{\rm out}=2/1$ boost signature and $I_6:1\to2$. The reverse $v_2\to v_1$ conversion is the mirror image, removing the vacuum O1 leg and replacing the carrier-produced O3 lineage with a fresh vacuum-supplied low-sector O3 stream. A parallel, previously-unexplained one-round R5 transient (an extra carrier-produced O3 relation appearing and then leaving) is also traced exactly: $(1,2)\to(1,3)\to(1,2)$ over rounds 2–3, present in every R5 slot and absent from the final mature state.

**Verdict: BOND_LOCAL_ENVIRONMENTAL_RESERVOIR_CONVERSION_LAW** (primary), **R6_HIGH_LOW_CHANNEL_CONVERSION_EXACT** (companion), scope-flagged **FINITE_COMPLETE_MANIFOLD_SECTOR_TRANSITION_SUPPLY_RESULT**. Y134 is explicit and correct not to overreach: the speed change is still imposed by the frozen sector selector, and "the reservoir conversion may be a consequence of that selected kinematic change rather than its cause" — precisely the question Y135 was designed to test.

**Recommended next stage (Y135 — Transition-Supply Causality).** At the exact rounds identified here, selectively remove or suppress only the relations supplying the next required L/V/C channel and compare matched clones under the same requested sector switch; test the final local-pool relations before rest→$v_1$/$v_2$, the R6 V-O1 boost supply, the carrier-produced O3 leg, the $v_2\to v_1$ replacement V-O3, and the R5 transient pulse; measure separately whether the requested kinematic displacement, relay state, and incidence current change. If the externally selected speed change remains exact while the scaffold conversion fails, the environmental transition is a consequence/support response, not yet an inertia mechanism.

### 10.1jjjjj Direct intervention shows the environmental scaffold is not causally upstream of the explicit kinematic selector — a decisive, correctly-scoped negative that reframes what would actually be needed to test for an inertia mechanism (Stage Y135)

Y135 tests the causal direction Y134 left open, using oracle-defined deletions of the exact relation instances Y134's classifier identifies, never a fitted predictor, with the sign/magnitude selector itself never touched.

**Every one of five preregistered interventions changes the scaffold while leaving the requested kinematics untouched.** Removing the final local-pool support before rest→$v_1$/$v_2$ (72 targeted deletions), removing the R6 V-O1 boost supply (44 deletions), suppressing the carrier-produced R6 high-state O3 leg, interrupting the $v_2\to v_1$ replacement V-O3, and removing the R5 transient C-O3 pulse each produce a measured, bond-additive scaffold-current effect (72/72 intervention branches) — while the selected carrier gate and displacement remain exactly CONTROL in every case: 576/576 gate tuples, 576/576 displacement tuples, across 1,872 constituent updates.

**A post-verdict stress test makes the separation total.** Deleting the *entire* frozen stationary reservoir before the first moving round — every relation in $U_{\rm rest}=11n_{R5}+7n_{R6}$, 484 deletions across 28 branches — leaves the O1/O3 scaffold current and occupancy at exactly zero for the first eight moving rounds in every history, yet the requested gate and displacement remain exact in all 224/224 comparisons. The carrier's selected motion executes with no measured supporting scaffold at all.

**Verdict: TRANSITION_SCAFFOLD_NOT_CAUSAL_FOR_EXPLICIT_SELECTOR_KINEMATICS** (primary), **RESERVOIR_CONVERSION_IS_DOWNSTREAM_CONSTITUTIVE_RESPONSE_UNDER_CURRENT_SELECTOR** (companion), post-verdict **FULL_REST_POOL_DELETION_STILL_DOES_NOT_BLOCK_SELECTED_MOTION**, scope-flagged **FINITE_EXPLICIT_SELECTOR_TRANSITION_SUPPLY_INTERVENTION_RESULT**. Y135 states the scope precisely: this is not a theorem that environmental relations can never constrain motion, only that they do not constrain the currently *scripted* kinematics on the tested manifold. The correct architecture is explicit sector selector → {carrier displacement, environmental relay/scaffold response}, not scaffold conversion → sector change. The most important implication is methodological: an inertia mechanism cannot be demonstrated while the speed sector is imposed by an update selector that bypasses the candidate environmental state entirely.

**Recommended next stage (Y136 — Selector Autonomy / Endogenous Sector Choice).** Audit exactly where the current magnitude selector enters the carrier update and which legal gates differ between sectors. Construct the closest selector-free, same-grammar competition in which both qualified kinematic continuations are exposed to the same native scheduler rather than an externally-chosen magnitude; freeze an unbiased tie/competition rule before observing outcomes; reapply the Y135 scaffold interventions and ask whether L/V/C availability now changes which continuation is selected, its persistence, or transition probability; include rest as a competing sector if a common legal interface can be defined without inventing a new force law. Only if the environmental state changes endogenous motion selection should the inertia program be reopened — and if no selector-free competition can even be formulated without changing the law, that itself is an important result about what the present FBCL construction does and does not contain.

### 10.1kkkkk The v1/v2 magnitude choice is not made by any native competition at all — it is read directly off the code's own function signature (Stage Y136)

Y136 audits the implementation directly rather than inferring selector behavior statistically.

**Gate A settles the question from source code alone.** `carrier_candidates(sim, S, maxold, sign, rng)` — the function that selects the native carrier gate — has no `mag` parameter; magnitude is only consumed later, by a helper that inserts an auxiliary q relation. Across 132 matched constituent-state comparisons (h1 rest launch, mature $v_1$, mature $v_2$; all seven species; both contexts): identical native gate (132/132), identical selected exterior vertex (132/132), identical post-fire support (132/132), yet neither q1 nor q2 is present after the common native fire (0/132 each) — the two program branches are identical until an external, non-competitive insertion splits them.

**Gate B shows both sectors remain dynamically reachable, and the environment matters only for robustness, not selection.** All 84/84 intact and 84/84 scaffold-zero branches (every currently-live O1/O3 T2 relation deleted) reach the requested sector at the identical settling round. The only measured difference is transient composite binding: 9/14 scaffold-zero rest→$v_1$ histories briefly lose a bond, always R6 (12/12 affected slots), recovering by round 32 in all cases.

**Gate C confirms the system accepts an unbiased external command sequence without measurable bias**, explicitly labeled a diagnostic rather than a selector test: 28/28 fair-coin schedules complete, 896/896 command episodes settle to the requested sector, 448/448 paired intact/scaffold-zero episodes have identical settling time.

**Verdict: NO_NATIVE_V1_V2_SELECTOR_IN_CURRENT_CARRIER_PROGRAM**; companion **BOTH_PROGRAMMED_KINEMATIC_SECTORS_AVAILABLE_UNDER_TESTED_SCAFFOLD_STATES**; qualification **SCAFFOLD_STATE_MODULATES_TRANSIENT_R6_BINDING_ROBUSTNESS**. Scope: a result about the current carrier program's implementation, not a theorem about what Y33 could support under a different construction.

**Recommended next stage (Y137 — Native q-Channel Reachability).** Test whether the q relation that currently distinguishes v1/v2 could arise from the frozen Y33 grammar alone, with no helper insertion: check the common post-fire state, immediate one-event native continuations, deterministic multi-event native continuation, and a bounded representative multiway search, under both intact and scaffold-zero environments.

### 10.1lllll The current q selector is definitively non-native at the transition cut — a strong, population-wide, multi-method negative that is honest about its bounded scope (Stage Y137)

Y137 tests reachability directly rather than searching for a replacement.

**Every tested reachability channel returns zero across 264 roots (132 intact, 132 scaffold-zero).** Neither q1 nor q2 is present or emitted by the common native fire (0/264 each); no legal immediate-next native gate produces either target (0 among 3,552 gates); a 32-event pure-native deterministic continuation with no helper never hits either target (0 among 8,448 events); a representative multiway search to depth 8 across six frozen roots finds zero hits among 1,192 branch transitions.

**A self-caught method correction prevents an overclaim.** An initial shortcut theorem ("every Y33 output contains the event's fresh vertex, so no all-old target is ever reachable") was checked directly against the grammar and found false — two of the eight output templates are all-old — and discarded before it could contaminate the scored result.

**Verdict: CURRENT_Q_SELECTOR_IS_NON_NATIVE_AT_THE_SCRIPTED_TRANSITION_CUT**; architecture consequence **CURRENT_V1_V2_CARRIER_PROGRAM_REQUIRES_EXPLICIT_HELPER_Q_INSERTION**. Y137 states its limits precisely: this is strong, population-wide, bounded-depth negative evidence, not an all-depth theorem about the unconstrained global Y33 multiway graph — and even a delayed native appearance elsewhere would not make the *current* scripted transition native, since the program requires q at the immediate post-fire cut.

**Recommended next stage (Y138 — Endogenous Native Selector Synthesis).** Remove `mag` as an external input entirely and search for a small, recurrent, Y33-generated pre-fire motif whose local state distinguishes two autonomous successor sectors without helper insertion, generated and maintained solely by legal Y33 rewrites, valid across species/contexts/environments, discovered before any mass/energy interpretation is reopened.

### 10.1mmmmm A genuine native sector memory is found — but it does not by itself regenerate the carrier gate, separating "memory" from "actuation" for the first time (Stage Y138)

Y138 reconstructs the Y125 producer-ancestry spine and asks whether it encodes speed sector.

**The native memory is exact and population-wide.** Defining $\sigma$ as the ancestry-rank distance between the support's two old-vacuum vertices: $\sigma=1$ for rest and $v_1$ (44/44 each), $\sigma=2$ for $v_2$ (44/44) — and this stride survives the common carrier fire with no q inserted in 176/176 intact/scaffold-zero moving roots. The native relational state really does remember magnitude.

**But the carrier gate itself needs q, not just the memory of speed.** Every one of 88 mature moving carrier gates has exactly three native prerequisites (outputs O2, O5, O7) and exactly one tracked-q prerequisite occupying gate-input slot I2 — 88/88. When q is withheld and every other tracked q relation is scoped out, the stride memory survives but the next carrier gate never regenerates: 0/176 immediate restorations, 0/176 through a 64-event native continuation; a companion control leaving other constituents' q intact gives the same result (0/176), with the fired constituent's own carrier core lost by event 75 in the two longest-surviving cases. A local one-defect motif census finds 176 structural near-misses, but 0/176 have any currently-legal native producer.

**Verdict: NATIVE_SECTOR_MEMORY_FOUND_BUT_NO_ENDOGENOUS_SELECTOR_ACTUATION**; architecture **Q_FUNCTIONS_AS_MISSING_GATE_INPUT_TRANSDUCER_NOT_MERE_SECTOR_LABEL**. The precise open question becomes: native memory $\sigma\not\Rightarrow$ native carrier gate; the implemented construction is $(\sigma, q_{\rm helper})\Rightarrow$ legal gate. A causal transducer, not another scalar, is missing.

**Recommended next stage (Y139 — Backward Native Stride-to-Gate Transducer Synthesis).** Invert the eight Y33 output templates backward from each Y138 one-defect target to find every legal producer-role assignment; backward-chain one or two further causal layers using ancestry/provenance roles rather than vertex numbers; search for a recurrent producer cycle whose availability differs between stride 1 and stride 2; execute forward closed-loop recurrence with no q insertion if a candidate exists.

### 10.1nnnnn Backward inversion finds the nearest static route, but it is sector-nonselective and sits in a self-destructive, unseeded causal cycle — precisely characterizing why the raw grammar cannot close the gap (Stage Y139)

Y139 performs the exact backward search Y138 called for, through three native causal layers.

**Temporal compatibility alone eliminates six of eight output channels**, since any relation containing the firing event's fresh vertex cannot match an all-old target; only channels O3 and O6 remain viable, giving 396 order-compatible producer branches across the 176 reconstructed one-defect motifs (exact match to Y138's census, 176/176).

**An exact three-layer closure search finds nothing.** Across 11,900 (core-preserving) and 13,852 (unrestricted) depth-0–2 path-states, zero target-producing events occur at any layer, and 0/176 candidate gates close by depth 3 under either search variant.

**The single closest structural route is found — and shown to be the wrong kind of route.** A three-relation static dependency cycle $T\leftarrow B\leftarrow P\leftarrow T$ exists in 22 v1-replication roots, with the support-only target one native producer step away. But seeding it directly (a non-native diagnostic, not a scored success) shows the completed relation enables *both* the +1 and +2 candidate gates simultaneously in 22/22 cases — it is propagation-enabling but sector-*non*selective — and the cycle is also self-destructive under Y33's own consumption pattern: firing either producer consumes the input the next step needs (0/22 either direction).

**Verdict: NO_NATIVE_STRIDE_TO_GATE_TRANSDUCER_THROUGH_THREE_Y33_LAYERS.** The key interpretive sharpening: the nearest candidate fix would not have solved the actual problem even if it had been native, because it cannot distinguish which displacement should occur. The missing mechanism must be sector-*selective*, not merely propagation-supporting — reframing what Y140 needs to search for.

**Recommended next stage (Y140 — Minimal Sector-Selective Native Transducer Augmentation).** Search the smallest local rule-level augmentation (not another q-equivalent helper) that reads only native pre-fire structure including the stride distinction, contains no external label of any kind, generates a genuinely displacement-specific relation so +1 and +2 are never simultaneously enabled, is universal across species/contexts, and is frozen on a discovery subset before blind testing.

### 10.1ooooo NST1F: an augmented, purely current-structure-derived rule reproduces the legacy selector exactly, including on a genuinely new species held fully blind — the first working replacement for the external magnitude command (Stage Y140)

Y140 builds and validates NST1F, a rule reading only current hypergraph structure — never `mag`, ancestry history, or a species/sector label.

**NST1F distinguishes moving-from-rest and v1-from-v2 using only present structure**, via a moving-state guard (presence of a specific two-relation motif), direction read from the existing marker, and a sector bit from a local outside-source motif — then selects the exterior vertex via the existing carrier geometry and emits exactly the historical relay relation.

**Static and dynamic agreement with the legacy selector is total, including on data the rule never touched during construction.** Development (88 moving roots): exactly one selection, correct sector bit, and output matching the legacy relation in 88/88 each; rest controls: NST1F dormant in 44/44. A genuinely fresh blind set — two new contexts and, critically, DS001, a species absent from the entire Y138–Y139 population — gives 92/92 on every measure. Sustained 32-round closed-loop validation across 60 combined development+blind cases (1,920/1,920 round rows, 5,760 constituent updates) shows the complete hypergraph and RNG state remaining exactly equal to the legacy helper-controlled branch throughout.

**Verdict: CURRENT_STATE_SECTOR_SELECTIVE_TRANSDUCER_FOUND_IN_AUGMENTED_GRAMMAR**; companion **EXTERNAL_MAGNITUDE_SELECTOR_ELIMINATED_ON_TESTED_MOVING_MANIFOLD**; qualification **SCHEDULER_AUTONOMY_NOT_YET_ESTABLISHED**. Two caveats are stated precisely rather than glossed: this is an *augmented* grammar result (Y139's unmodified-Y33 negative still stands), and the validation harness still scripted *when* NST1F fired — immediately after each carrier fire — which is exactly what Y141 was designed to remove.

**Recommended next stage (Y141 — NST1F Scheduler Autonomy and Grammar Closure).** Encode NST1F as an explicit native compound event rather than a scripted post-fire callback; test arbitrary legal interleavings against it; require pure-vacuum dormancy, rest dormancy, sustained v1/v2 recurrence, bond preservation, and blind-context generalization before any inertia interpretation is reopened.

### 10.1ppppp Folding the transducer into the same compound event as the carrier fire achieves genuine scheduler-robust closure — a separate event does not, exposing a sharp, fully-characterized local race (Stage Y141)

Y141 tests two implementations of NST1F against real event competition.

**A free-standing NST1F event is not confluent, and the failure is precisely local.** In every one of 180 tested roots, exactly one competing native Y33 event touches the post-fire carrier/transducer footprint, and firing it first disables NST1F and destroys the carrier core in all 180/180 cases — an unavoidable, unweighted 1-in-2 local race, not a design accident. Every *remote* one-step interleaving (2,204 tested) commutes perfectly, preserving the same NST1F target and losing zero carrier cores — the scheduling problem is sharply confined to one specific local competitor.

**Folding the relay into the same compound rewrite as the carrier fire itself removes the vulnerable interval entirely.** ANST1F computes the relay from the pre-fire state and the already-selected native gate, before firing, and emits it as part of one compound event. Pre-fire prediction matches the Y140 post-fire selection exactly (180/180). Sustained 32-round closed-loop recurrence across all 60 development+blind cases (1,920/1,920 rows, 5,760 compound events) again shows exact hypergraph/RNG equality with the legacy branch throughout; rest and pure-vacuum controls confirm the compound event stays completely dormant off the moving manifold (44/44 rest, 512/512 vacuum-only continuation bit-identical).

**Verdict: ANST1F_ATOMIC_RELAY_CLOSES_CURRENT_CARRIER_GRAMMAR_ON_TESTED_MANIFOLD**; companion **SEPARATE_NST1F_EVENT_IS_NOT_SCHEDULER_CONFLUENT**; qualification **GLOBAL_CARRIER_EVENT_SCHEDULER_AUTONOMY_NOT_ESTABLISHED**. The resulting architecture is *current moving carrier state → one compound carrier rewrite → next state + next relay*, replacing *carrier fire → externally-timed transducer → next relay*. Two structural caveats remain explicit: ANST1F still operates inside an augmented carrier grammar with a higher-level event scheduler, not a proven autonomous excitation of unmodified Y33 vacuum dynamics alone; and its arithmetic ($f=e+s\cdot m_{\rm native}$) still uses the frozen scalar old-vertex ordering rather than a demonstrated intrinsic causal/graph construction.

**Recommended next stage (Y142 — ANST1F Covariance and Intrinsic-Geometry Audit).** Before reopening $M_i$/$E_0$/$\alpha$ as a candidate physical inertia interpretation: test ANST1F under random admissible relabeling/isomorphism of the complete moving manifold; attempt to replace the scalar arithmetic with an intrinsic causal-spine or graph-relative successor construction; require identical v1/v2 relay selection after relabeling; retain rest/vacuum dormancy and full 32-round closure. Only a covariant transducer should be taken as a genuine structural prerequisite cleared before the deferred recurrence-energy/inertial-proxy population program is reopened.

### 10.1qqqqq IGR1 replaces every scalar-arithmetic step of the carrier relay with intrinsic causal/graph structure and survives exhaustive relabeling stress-testing — while exposing that the historical Y33 gate parser itself is not label-covariant (Stage Y142)

Y142 rebuilds the ANST1F relay entirely from relational structure — intrinsic five-role carrier core, topological direction marker, structural sector motif, and a causal-spine successor/predecessor operator in place of numeric addition — as the frozen rule **IGR1**.

**IGR1 is exactly equivalent to the validated Y141 mechanism on the canonical manifold (180/180 across every measure) and remains exact under real relabeling stress, with negative controls proving the result isn't incidental.** Across 11,520 static isomorphism tests (180 roots × 64 arbitrary permutations, not merely order-preserving ones): intrinsic roles, direction, sector, gate, and relay target are all covariant 11,520/11,520. The old scalar formula, tested under the identical permutations, reproduces the mapped relay in only 2/11,520 (0.017%); the old numeric gate orientation only 49.1%; naive numeric resorting of the relabeled support only 0.68% — confirming IGR1's invariance is a genuine structural property, not an artifact of gentle test permutations. Rest dormancy (2,816 relabeled tests, 0/2,816 false-eligible) and full 32-round persistent-relabeling closure (120/120 runs, 11,520 compound events, exact induced state equality throughout) both hold.

**A broader, unplanned finding emerges from the same audit: the historical global Y33 gate parser's numeric `u<v` orientation convention is itself not label-covariant**, independent of the carrier-relay question — a representation issue in the base engine, not something specific to motion. Y142 explicitly declines to claim this proves the whole historical simulator is covariant; it establishes carrier-relay covariance and identifies this as the next issue to close, deferring rather than glossing over it.

**Verdict: IGR1_INTRINSIC_RELAY_IS_VERTEX_RELABEL_COVARIANT_ON_TESTED_MANIFOLD**; companion **Y141_SCALAR_RELAY_GEOMETRY_REPLACED_BY_CAUSAL_SPINE_SUCCESSOR_OPERATOR**; diagnostic **HISTORICAL_NUMERIC_GATE_ORIENTATION_IS_NOT_VERTEX_RELABEL_COVARIANT**; qualification **FULL_Y33_GRAMMAR_COVARIANCE_AND_GLOBAL_CARRIER_EVENT_SCHEDULER_AUTONOMY_NOT_ESTABLISHED**.

**Recommended next stage (Y143 — Full Y33 Covariant Gate Enumeration and Vacuum/Carrier Regression).** Replace the global numeric `u<v` gate orientation with the structural guard-defined orientation used in IGR1; prove exact equivalence to historical Y33 on canonical vacuum/carrier trajectories; stress-test under arbitrary relabeling; check whether the covariant enumerator exposes any additional legal branches on canonical states; repeat full vacuum and carrier/composite regression. If clean, freeze the covariant engine and reopen the recurrence-energy/inertial-proxy program.

### 10.1rrrrr The covariant gate enumerator leaves vacuum and moving-carrier dynamics completely unchanged — but reveals 22 real, previously-hidden legal branches specifically in the stationary rest sector, blocking a global engine freeze until they are understood (Stage Y143)

Y143 replaces `u<v` globally with the structural guard-based orientation and regresses it against every established trajectory class.

**Vacuum and moving-carrier dynamics are provably unaffected.** The complete 1,800-event frozen vacuum history reproduces identically under the covariant parser (1,800/1,800 selected gates and post-event states exact, 0 extras/missing). All 60 Y141/Y142 moving cases reproduce identically through the full 32-round trajectory (5,820/5,820 boundaries exact, 0 extras/missing). Direct relabeling stress tests confirm the mechanism: the covariant parser recovers the exact mapped gate set in 1,344/1,344 vacuum+moving tests, versus only 192/1,344 for the historical numeric parser — proof the old convention was a label-dependent filter that happened, on these two sectors, to agree with the correct structural answer.

**Stationary rest does not share this property, and the newly exposed branches are real, not artifacts.** Across the 14 canonical `rest_h1` states, 7/14 (all positive-direction primary contexts) expose one previously-hidden legal gate each — 22 total — none of them a duplicate `(u,v)` relabeling of an existing branch; each is confirmed marker-mediated (the fifth vertex is the rest marker itself) rather than an ordinary ambient-vacuum collision. Direct firing shows a consistent, exact structural outcome in all 22/22 cases: the old rest carrier core is lost, a transient moving-core-shaped state forms, but it lacks the intrinsic direction marker IGR1 requires, so it is not an autonomous new moving carrier — the branch instead continues an ordinary Y33 chain that leaves the established carrier class entirely.

**Verdict: STRUCTURAL_Y33_GATE_ENUMERATOR_IS_VERTEX_RELABEL_COVARIANT_ON_TESTED_MANIFOLD**; companion **CANONICAL_VACUUM_AND_MOVING_CARRIER_DYNAMICS_ARE_UNCHANGED**; blocking result **REST_H1_IS_NOT_COVARIANTLY_CLOSED_UNDER_THE_CURRENT_ARCHITECTURE** (22 true marker-mediated branches were hidden by the numeric convention); consequence **DO_NOT_FREEZE_GLOBAL_COVARIANT_ENGINE_OR_REOPEN_E0_MI_YET**. Y143's own discipline is explicit: a clean result on vacuum and moving sectors was not extrapolated to rest — an explicit audit was run, and it changed the verdict.

**Interpretation, stated carefully.** This does not retroactively invalidate any measurement made on the historical simulator — every prior rest-sector result (Y46 onward) is an exact account of the trajectory that engine actually executed. What it opens is a precise, previously invisible question: whether the mature stationary rest state used throughout this program is the unique recurrent consequence of the *fully covariant* grammar, or whether the numeric convention was silently pruning legal exit/decay channels that a label-independent implementation would expose. That question is now well-posed and tractable rather than merely suspected.

**Recommended next stage (Y144 — Covariant Rest-Sector Closure and Marker-Mediated Branch Resolution).** Determine whether the 22 marker-mediated branches are an intended native phase of the rest lifecycle requiring its own intrinsic continuation law, a structural defect in the current rest-marker encoding, or an admissible decay channel incompatible with treating the present `rest_h1` state as stable. Reconstruct the rest lifecycle using intrinsic role labels, remove any sign/asymmetry inherited from numeric support ordering, and test full positive/negative rest periods and rest↔$v_1$/$v_2$ transitions under the covariant parser. Only after the rest architecture is covariantly closed should $E_0$, $M_i$, and $M_i=\alpha E_0$ be reopened.

### 10.1sssss The 22 hidden rest branches are a marker-encoding artifact, not a genuine instability — a one-relation covariant tag removes them exactly while preserving the entire established rest lifecycle and its moving-sector handoffs (Stage Y144)

Y144 diagnoses the Y143 branches directly: the historical rest marker reused the same topological family as the moving-sector direction marker, so the covariant parser legitimately treats it as an active gate participant it was never meant to be.

**A one-relation fix (RST1) closes the gap exactly, with the marker vertex made the source rather than the target of the tag ($R_+=\mathrm{rel}(h,c_0,c_4)$, $R_-=\mathrm{rel}(h,c_0,c_1)$).** Across all 14 canonical roots: all 22 hidden gates removed, 0 new spurious gates introduced, repaired gate set equals the intended historical set (14/14). A first repair candidate was caught and rejected mid-stage — it failed to break a genuine two-fold automorphism the bare core exhibits during R5 scar retirement, leaving the intrinsic frame ambiguous exactly when it mattered — and the corrected tag was built to break that symmetry relationally rather than via an external label.

**Validation is extensive and clean.** Arbitrary relabeling: 896/896 static and 448/448 dynamic exact. Long-run regression: 448 original + 192 genuinely blind (three species never used in construction, two unseen contexts) mature-rest period checks, all exact apart from the intentionally changed marker representation. Both directions of the moving↔rest handoff are verified compatible with the already-established Y140–Y142 machinery: 14/14 moving→rest transitions exact, and rest→motion launches settle to the correct native sector after a discovered, exact, quantized displacement schedule (v1: 2 rounds, displacements $\tfrac12 s$ then $\tfrac32 s$; v2: 1 round, displacement $\tfrac12 s$), followed by 2,816/2,816 exact atomic continuation checks.

**Verdict: RST1_CLOSES_MARKER_MEDIATED_REST_BRANCH_ON_TESTED_MANIFOLD**; interpretive **THE_Y143_HIDDEN_REST_BRANCH_IS_A_MARKER_ENCODING_ARTIFACT, NOT AN_UNAVOIDABLE_BARE-CORE_DECAY_CHANNEL**; remaining blocker **REST_PHASE_SCHEDULER_AUTONOMY_NOT_YET_ESTABLISHED**. This is the most benign of the three outcomes Y143 left open: the mature rest state's stability is not called into question, only its historical representation. What remains scripted is the phase clock itself — two bridge operations, an eight-event phase order, phase-specific cleanup, and an external scheduler — precisely mirroring what Y136–Y141 found and fixed for the moving selector, one architectural layer up.

**Recommended next stage (Y145 — Endogenous Rest Phase Clock and Scheduler Closure).** Classify each rest subphase from instantaneous relational state plus RST1, with no external event counter; derive bridge/turnaround eligibility from native state; replace the procedural event-0…7 clock with state-dependent legal transitions where possible; test scheduler competition against ordinary covariant Y33 events; preserve the validated 32-period trajectories, bonds, lineage, and RST1 inertness; repeat relabeling and unseen-context validation before any global engine freeze or reopening of $E_0/M_i/\alpha$.

### 10.1ttttt A genuine instantaneous rest-phase clock is found and validated with real held-out species — but, exactly as with the moving selector, a readable clock does not yet enforce the correct transition: a destructive competing gate exists at the very first rest boundary (Stage Y145)

Y145 repeats the Y138→Y141 pattern one layer up, with a more operationally difficult execution (a timed-out run resumed from preserved intermediate CSVs and the archived Y144 runtime) reported candidly rather than smoothed over.

**A discriminating instantaneous phase signature is found and passes a genuine leave-species-out test.** A four-statistic local signature distinguishes all ten mature-rest boundary types; trained on four species (220 rows) and evaluated on three species never touched during construction (220 held-out rows), classification is exact both in-sample and out-of-sample (220/220 each), with no species identifier or event counter used. A reduced three-statistic version fails, collapsing two bridge boundaries together (176/220) — confirming the full signature isn't gratuitously redundant. A separate audit finds a repeating local end-of-period signature across all 44 tested period-start/e7-boundary pairs (11 matching indicators each).

**The decisive scheduler test finds exactly the same failure mode Y141 found for motion — but immediately, at the very first boundary rather than after extended search.** At every one of 44 tested constituents, the intended rest gate has one specific, genuinely legal Y33 competitor; firing that competitor first destroys the existing rest core in 44/44 cloned-state interventions, even with RST1 still live. This is a direct, population-wide counterexample to unconditional rest scheduler autonomy.

**Two further gaps are reported honestly rather than papered over.** The mature rest driver still depends on historical pointer bookkeeping (`prev_e6`, `prev_e7`, a per-period creation table) that has not been replaced by intrinsic causal provenance; an attempted static heuristic to recover the R5 scar identity from topology alone failed in all 8 tested cases, which rules out that specific heuristic without ruling out a native provenance law in general. The bridge operations still use procedural timing and historically numeric old-spine arithmetic.

**Verdict: INSTANTANEOUS_STRUCTURAL_REST_PHASE_CLOCK_DISCOVERED_ON_TESTED_STATES**; **REST_EVENT_SELECTION_NOT_SCHEDULER_CONFLUENT**; **PROVENANCE_POINTER_CLEANUP_UNRESOLVED**. Unlike Y144, DS001 and fully unseen-context validation are explicitly not yet established for the phase clock itself — a narrower scope than the RST1 result, stated as such rather than implied to be equally broad.

**Interpretation.** Y145 is explicit that it repeats Y141's lesson at a deeper layer: a readable clock is necessary but not sufficient, and a viable autonomous rest engine likely needs an atomic phase-guarded compound transition — consuming the state-derived phase and emitting the successor relay in one step, exactly as ANST1F did for motion — with cleanup identified through genuine causal provenance rather than pointer bookkeeping. Unlike the moving-sector case, this stage leaves three distinct open sub-problems rather than one (the destructive competitor race, provenance-pointer replacement, and bridge arithmetic covariance), suggesting rest-scheduler closure may take more than a single Y141-style atomic fold to complete.

**Recommended next stage (Y146 — Atomic Rest-Phase Transition and Native Provenance Closure).** Attempt to fold the state-derived phase read together with its successor transition into one compound event, exactly as Y141 did for the carrier relay; construct and test a genuine native-provenance identification for the R5 scar and cleanup pointers rather than a static-topology heuristic; extend the covariant bridge construction to remove residual numeric old-spine arithmetic; and only after all three close, together with DS001/fully unseen-context validation matching Y144's scope, should the global covariant engine be frozen and $E_0/M_i/\alpha$ reopened.

### 10.1uuuuu Atomic folding removes the Y145 scheduler race exactly as it did for motion, cleanly isolating the one remaining obstacle to native causal identity for delayed cleanup (Stage Y146)

Y146 shows the Y145 race is a one-slot ambiguity, not a whole-stencil competition, and closes it by event-granularity change.

**The destructive rival differs from the intended gate in exactly one position.** Across all 44 Y145 roots, both legal carrier/rest-stencil gates agree in four of five slots and differ only in the old successor/relay vertex; the intended gate always has that slot equal to the locally-derived successor, the rival never does. Freezing the rest transition as one atomic event — guarded by intrinsic phase, RST1-valid frame, and the uniquely derived successor vertex, emitting the next phase support in the same rewrite — removes the rival by construction rather than by an external priority rule, directly mirroring Y141's fix for the moving relay. The historical scalar `q = e ± 1` destination is replaced by the already-validated Y142 ancestry-successor operator, $q_{\rm local}=\mathrm{Succ}_{\rm direction}(c_0)$, with the scalar form retained only as a regression signature, not as dynamics. The local transition signature closes across all 44 start/e7 boundary pairs.

**Verdict: ATOMIC_REST_SUCCESSOR_GUARD_FOUND_ON_Y145_CORPUS**; **REST_RIVAL_BRANCH_REMOVABLE_BY_COMPOUND_SEMANTICS**; **NUMERIC_Q_DESTINATION_REPLACEABLE_BY_INTRINSIC_DIRECTIONAL_SUCCESSOR**; remaining blocker **CLEANUP_PROVENANCE_NOT_YET_INTRINSIC**. Y146 explicitly rejects consulting the passive Y96 lineage recorder directly as a shortcut, since that would reintroduce hidden external history rather than making cleanup identity a genuine relational-state fact; the problem is narrowed precisely to constructing a native token satisfying an explicit, frozen list of requirements (Y33-inert, relabel-covariant, non-accumulating, no external table).

**Recommended next stage (Y147 — Covariant Transient Provenance Token and Cleanup Closure).** Construct the minimal transient causal token needed to replace the historical `prev_e6`/`prev_e7`/`created[...]`/R5-scar lookup tables; require it to be emitted and consumed only by native compound rewrites, Y33-inert, relabel-covariant, and non-accumulating; enumerate ordinary Y33 gates touching its footprint for hidden branches; then combine with the Y146 atomic guard for full population regression before any engine freeze.

### 10.1vvvvv PRV2, a two-anchor transient provenance token, is proven — not merely tested — to be inert to every legal Y33 gate, and closes the cleanup-identity problem symbolically across the complete species population (Stage Y147)

Y147 designs PRV2: two temporary anchor vertices sourced only from the RST1 marker `h`, encoding an exact delayed-relation pointer with no numeric IDs, event counters, or external tables.

**Decoding is exact and covariant under real stress.** A randomized decoder test — 1–7 simultaneous tokens, short and long forms, deliberately overlapping payloads, arbitrary post-construction relabeling — reconstructs every pointed relation and its lifetime class exactly in 10,000/10,000 trials.

**The Y33-inertness result is a proof, not a sampled result — the strongest claim in this batch.** Because RST1 already makes `h` source-only, and PRV2 preserves that invariant (every PRV relation sourced by `h`, none targeting it), a direct case check against every Y33 gate role ($x,y,z,u,v$) shows each would require some input or guard relation to target `h`, contradicting the source-only invariant — so `h`, and therefore no PRV relation, can ever occur in any legal Y33 gate. This is a structural theorem about the frozen gate stencil.

**The token grammar covers every known delayed-cleanup family with zero accumulation.** Short tokens (PRV-S) cover the R5 scar and the `e5/e6→O7` pointers; one long token (PRV-L) covers the sole cross-boundary case, `e7/O7→next e1`. A symbolic 128-period run across the full ten-identity population (including two new N=5 controls), 2,560 period checks total, returns to the identical token state every time — zero secular growth, with the largest tested composite peaking at 90 token relations before returning exactly. Stop/launch compatibility is preserved explicitly: a live PRV token is never interpreted as an unconditional deletion command, so the established R5 scar branch-dependent fate (retired under continued rest, preserved under a boost) is unaffected.

**Verdict: EXACT_RELATIONAL_CLEANUP_POINTER_FOUND**; **PRV2_VERTEX_RELABEL_COVARIANT**; **PRV2_Y33_INERT_BY_GATE_STENCIL_THEOREM**; **HISTORICAL_DELAYED_CLEANUP_TABLES_ELIMINABLE_IN_PRINCIPLE**; **TOKEN_LIFECYCLE_PERIODIC_WITH_ZERO_ACTIVE_RELATIONAL_DRIFT**; qualification **FULL_INTEGRATED_RUNTIME_QUALIFICATION_PENDING** — this closes the representation and cleanup architecture symbolically; the archived executable simulator was not available for a fresh bit-for-bit run in this stage, so the engine is explicitly not yet frozen and $E_0/M_i/\alpha$ remain sealed.

**Recommended next stage (Y148 — Integrated Autonomous Rest Grammar Regression and Engine Freeze).** Restore the exact archived runtime; integrate the Y146 atomic successor event and Y147 PRV2 cleanup exactly as specified; replace remaining numeric bridge arithmetic with the ancestry-successor operator; regenerate phase-classifier features directly from runtime states; run at least 32 mature periods for every species/context plus unseen-context validation, arbitrary dynamic relabeling, and a full global gate-set audit at every boundary; require zero stale tokens or anchor residue; re-verify both handoff directions. Freeze the autonomous covariant engine only if every gate passes, then reopen the deferred $E_0/M_i/\alpha$ program.

### 10.1wwwww Full integration succeeds on every preregistered test: the autonomous, covariant rest engine is frozen — closing a thirteen-stage architectural arc that began at Y136 and finally clearing the way to reopen the central recurrence-energy/inertial-proxy population program (Stage Y148)

Y148 restores the exact archived runtime, integrates every Y142–Y147 component together, and runs the complete regression Y147 specified.

**The ancestry-based successor exactly removes the Y145 rival across a full period, not just the sampled corpus.** Across all 352 constituent rest events in one complete original-population period, exactly one legal carrier gate has its ambiguous slot on the causal-ancestry spine, and it matches the archived intended continuation in 352/352 cases — the destructive rival is absent by construction throughout, not merely in the previously-sampled subset.

**Integration catches and corrects a real over-provisioning in Y147's design, exactly the kind of self-correction this program has repeatedly rewarded.** Running PRV2 against the actual archived lifecycle shows two of Y147's provisional token classes (`e7/O4`, `e7/O6`) were never actually needed; the frozen Y148 token set narrows to exactly two tokens per constituent at the mature-start boundary (one short, one long) — a simplification discovered by integration, not assumed in advance.

**Validation is comprehensive and passes without exception.** The regenerated phase detector: leave-species-out 242/242 + 242/242, unseen-context 154/154, driving 640 mature periods through 6,400 phase-triggered compound steps with zero phase exceptions. PRV2 token integrity: 154/154 live-target and decode checks, zero orphan anchors, zero relations targeting `h`. Full boundary projection: 154/154 exact match to the archived Y144 state and complete global Y33 gate set at every phase. Arbitrary relabeling: 560/560 across phase detection, token identity, and the full gate set. Long-run regression: 448/448 original-population periods, 192/192 blind-context periods, 640/640 combined — 6,400 group phase transitions, 14,848 atomic constituent rest events, 3,712 bridge operations. Both handoff directions: rest→motion 28/28 (with a scoped test-fixture correction caught by the lineage recorder's own unscoped-operation check, exactly the kind of integrity safeguard Y96 was built to provide), motion→rest 14/14 plus 112 further autonomous periods.

**Verdict: AUTONOMOUS_COVARIANT_REST_ENGINE_FROZEN_ON_TESTED_MANIFOLD**, hashed and scoped explicitly as a finite-manifold result, not a universal theorem over every possible Y33 history. The frozen engine no longer requires an external rest event counter, numeric gate orientation, scalar successor/bridge arithmetic, or any of the historical cleanup lookup tables — phase, direction, successor, and cleanup identity are now all supplied by current relational state plus causal ancestry. The physical-observable firewall remains closed throughout; freezing the engine is an architectural result, not a physics claim.

**Recommended next stage (Y149 — Autonomous-Engine $E_0$/$M_i$ Population Rebaseline and Proportionality Test).** Freeze the Y148 engine hash; restore the previously frozen $E_0$ and $M_i$ definitions rather than redesigning them in light of the new engine; declare the development/holdout split before measuring; preregister how PRV2 bookkeeping is treated (report both a PRV-erased projection comparable to the historical state and the full augmented state as a robustness diagnostic); measure independently per species/context; fit one global $\alpha$ on development only; evaluate rank correlation, proportional residuals, and held-out performance without refitting; use same-$N$ R5/R6 contrasts as the sharpest test; and do not assign physical meaning from a good model-internal fit alone.

### 10.1xxxxx The frozen G6/G7 mismatch survives the complete autonomous-engine rebuild exactly — proving the disagreement was never an artifact of the old scheduler, and decisively re-confirming Candidate B's structural incompatibility with $M_i$ on same-$N$ controls (Stage Y149)

Y149 is the first direct return to a recurrence-energy/inertial measurement since the whole Y88 program began, now run on the Y148 engine.

**$M_i=N\cdot\tfrac58\ln2$ reproduces to floating precision, with zero binding residual for every composite — the autonomous rebuild introduces no hidden R5/R6 term.** Candidate A likewise reproduces exactly at $6N\ln2$, PRV2-invariant, with the formal $M_i=\tfrac{5}{48}E_{0,A}$ relation surviving every held-out identity — but Y149 explicitly preserves the Y89 caution rather than promoting this: A and $M_i$ share the same constituent-local direct-contact-surprisal machinery, so the agreement remains formally circular, not independent evidence.

**Candidate B is genuinely rebaselined by the new architecture, in a way that confirms rather than undermines its topology sensitivity.** RST1 adds exactly $+N$ to every $B$ value relative to Y88 (one extra carrier-touching relation per constituent from the new covariant marker); retaining PRV2 in the scored state adds exactly $+8N$ more. Both shifts are exact, extensive, and — critically — leave every binding residual $\Delta B$ identical to the original Y88 values. The topology-sensitive signal survives the complete thirteen-stage architectural rebuild completely unchanged.

**The same-$N$ contradiction is now established beyond any architectural excuse.** $M_i({\rm D2R5})=M_i({\rm D2R6})$ exactly, while $B({\rm D2R6})-B({\rm D2R5})=2$; the identical pattern holds at $N=3$ and $N=4$ (three tetramers, two equal $M_i$ groups but $B(\rm T4R666)-B(\rm T4R656)=2$). No scalar conversion, zero- or nonzero-intercept, can reconcile a topology-blind and a topology-sensitive quantity over this population — a structural fact, not a fitting artifact, and now proven immune to the entire list of architectural objections (external scheduler, numeric gate orientation, non-covariant marker, hidden cleanup tables) that motivated Y136–Y148 in the first place.

**Verdict: Y81_MI_REPRODUCED_EXACTLY_ON_Y148_REST_BASELINE**; **CANDIDATE_A_GLOBAL_ALPHA_PASSES_FORMALLY** (circular, not promoted); **CANDIDATE_B_GLOBAL_ALPHA_FAILS_STRUCTURALLY**; **INDEPENDENT_MODEL_INTERNAL_MASS_ENERGY_EQUIVALENCE_NOT_ESTABLISHED**. Y149's own framing is precise: the mismatch lies in the observables, not in the now-repaired scheduler architecture, and the scientifically interesting target becomes an inertial *response* independent of Candidate B's construction, capable in principle of resolving topology.

**Recommended next stage (Y150 — Autonomous Transition-Response Inertial Binding Test).** Do not modify $M_i$ or fit an R5 correction to it. Construct a response entirely from the actual autonomous rest↔moving compound dynamics and the Y142 intrinsic continuation, never the old explicit magnitude selector; preregister an event-local transition cost for standardized rest→$v_1$, rest→$v_2$, $v_1$→rest, $v_2$→rest handoffs; require sign symmetry and covariance before any curvature is computed; test same-$N$ R5/R6 pairs for a nonzero binding-sensitive residual; keep Candidate B and Y99 sealed until that residual is frozen.

### 10.1yyyyy The primary transition-impulse test fails its own sign-symmetry gate cleanly — but the failure is informative, isolating a genuine R6-specific odd orientation response and, kept strictly as a sealed diagnostic, an exceptionally clean sign-even cross-bond channel (Stage Y150)

Y150 builds the first inertial-response candidate from genuinely new structure — a coordinate-free relation-edit count during the rest↔moving handoff — rather than reusing $M_i$'s construction.

**The preregistered primary observable fails its own kill condition before any curvature is computed, and the protocol is honored exactly.** The all-halo edit impulse is not sign-symmetric (D2R6 at $v_1$: $J_{\rm all}(+)=-3.75$ vs. $J_{\rm all}(-)=-5.75$; T3R65: span 13.25), failing at fixed context on multiple species. Per the frozen kill condition, no primary $M_{\rm TR}$ is promoted, Candidate B and Y99 remain sealed, and no $\alpha$ is fit.

**A post-verdict trace explains the failure mechanistically and isolates a genuine new structural fact.** Longer continuation shows the mature target sector itself is sign-symmetric — the asymmetry is confined to the finite transition transient — and obeys an exact population law, $T_+(v_1)-T_-(v_1)=2n_{R6}$, in 8/8 species, entirely within the one-body/halo channel (the cross-constituent channel has exactly zero sign difference). This is recorded as an orientation/chirality-*like* model diagnostic, explicitly not a physical spin claim.

**The preregistered secondary cross-bond channel is exceptionally clean, and is correctly held back from rescuing the failed primary.** $J_{\rm cross}(v_1)=-8n_{R5}$, $J_{\rm cross}(v_2)=-8n_{R5}-\tfrac{33}{4}n_{R6}$, exact on all eight species, giving a diagnostic two-speed coefficient $M_{\rm cross,diag}=-20n_{R5}+\tfrac{11}{8}n_{R6}$ — a genuine topology-sensitive transition law discovered without reference to Candidate B. The protocol explicitly forbade switching primaries after seeing results, so this remains diagnostic-only despite its cleanliness.

**A reverse-path anomaly is found and correctly not forced into the existing framework.** The reverse cross-bond response is exactly additive by bond count at $v_1$ ($44n_{R5}+20n_{R6}$) and for seven of eight species at $v_2$ ($56n_{R5}+43n_{R6}$) — but T4R656 is low by exactly 2 edits relative to the same-bond-count T4R665, which differs only in R5 bond *placement*. This is flagged honestly as a genuine open anomaly, not dismissed as noise or patched with an ad hoc correction.

**Verdict: PRIMARY_ALL_HALO_TRANSITION_IMPULSE_FAILS_SIGN_SYMMETRY**; **NO_PRIMARY_AUTONOMOUS_TRANSITION_INERTIAL_CURVATURE_PROMOTED**; diagnostics **R6_ODD_TRANSITION_DRESSING_EXCESS_EQUALS_2N_R6**, **FORWARD_CROSS_BOND_TWO_SPEED_LAW_EXACT_ON_8_SPECIES**, **REVERSE_V2_CROSS_RESPONSE_HAS_BOND_PLACEMENT_DEPENDENCE**; firewall **CANDIDATE_B_AND_Y99_COMPARISON_NOT_OPENED**.

**Recommended next stage (Y151 — Bond-Local Even/Odd Transition Decomposition and Blind Topology Validation).** Freeze the cross-constituent channel as the new primary, and the odd one-body channel separately, before any new species are measured; derive forward laws from individual bond neighborhoods rather than population fitting; blind-test on the unused Y99 N=5 multi-R5 chains; target the T4R656/T4R665 discrepancy specifically to determine whether it is a placement, order, or genuine path/holonomy effect; only after blind validation should Candidate B/Y99 be reopened.

### 10.1zzzzz The cross-bond transition response survives blind N=5 validation exactly, generalizes to a real pair-channel-overlap explanation of the earlier anomaly, and — the first result of its kind — shows an exact same-$N$ topology-contrast proportionality with both Candidate B and $\mathcal{F}_{\rm flux}$, though not a total-value mass-energy equivalence (Stage Y151)

Y151 promotes the Y150 cross-bond channel to primary and tests it, and the odd channel, fully blind on the eleven Y99 multi-R5 N=5 chains before reopening any comparator.

**Both forward channels generalize exactly.** All 88 blind forward transitions satisfy the frozen total law, the stronger individual-bond decomposition, and exact union-equals-sum-of-pairs additivity (0 unexplained nonadjacent/multi-core residual); the odd channel's $2n_{R6}$ law and its exact zero on the cross channel both hold in 22/22 comparisons, cleanly confirming the even/odd decomposition first suspected at Y150. Relabel covariance holds in 240/240 trials.

**The reverse-path anomaly is correctly re-diagnosed rather than confirmed as originally guessed.** The preregistered "T4R656-specific" correction fails to generalize across the N=5 population; instead, every individual pair constant remains exact while the *union* symmetric difference is reduced whenever relation identities persist across adjacent-pair boundaries with reassigned ownership — a genuine pair-channel-overlap effect, more general and more structurally grounded than the single-species anomaly that motivated the search.

**Only after both structural verdicts were frozen were Candidate B and $\mathcal{F}_{\rm flux}$ reopened — and the result is the first exact same-$N$ topology-contrast proportionality this entire program has produced.** The autonomous N=5 Candidate B remeasurement gives $B_{\rm proj}=3N^2+44N+1-2n_{R5}$, exact across all 19 tested rows (N=1–5). Relative to the same-$N$ all-R6 baseline: $\Delta M_{\rm cross}=-\tfrac{171}{8}n_{R5}$, $\Delta B_{\rm proj}=-2n_{R5}$, $\Delta\mathcal{F}_{\rm flux}=+2n_{R5}$, giving the exact relations $\Delta M_{\rm cross}=\tfrac{171}{16}\Delta B_{\rm proj}=-\tfrac{171}{16}\Delta\mathcal{F}_{\rm flux}$ across every tested row. Candidate B and the new transition response assign R5-vs-R6 contrast the *same* sign; Y99's causal rest content assigns the *opposite* sign.

**Verdict, stated with the precision the result deserves.** This is a genuine, blind-validated, fixed-$N$ structural fact — stronger than an aggregate correlation, since it survives exact same-$N$ controls and out-of-sample topology. It is explicitly *not* total mass-energy equivalence: $M_{\rm cross}$ is signed and can be negative, DS001 has no cross-bond channel at all, the $N$-dependent baselines differ between quantities, and naive zero-intercept total fits are weak ($R^2\approx0.48$–$0.49$). **FORWARD_BOND_LOCAL_CROSS_RESPONSE_BLIND_VALIDATION_PASS**; **FIXED_N_TOPOLOGY_CONTRAST_PROPORTIONALITY_FOUND_FOR_CANDIDATE_B**; **TOTAL_MODEL_INTERNAL_MASS_ENERGY_EQUIVALENCE_NOT_ESTABLISHED**.

**Recommended next stage (Y152 — Bond-Local Closed-Loop Transition Action and Positive Inertial Coefficient Test).** Freeze a closed rest↔motion pair-local cycle functional built from the now-validated forward and reverse histories, separating the odd orientation channel and the reverse overlap term explicitly; require sign evenness, direction/loop reciprocity, nonnegative finite value, and bond-local compositionality; blind-validate on N=5 before any new comparator contact.

### 10.1aaaaaa A genuine positive, topology-sensitive, bond-local transition action is constructed and transfers exactly to trimers — but its promotion is correctly blocked because the underlying rest↔motion cycle does not actually close autonomously for every bond type and direction, exposing a new, precisely-located architectural gap (Stage Y152)

Y152 builds a matched-null action (deviation from the mature target pattern on each leg, summed over the closed rest→motion→rest cycle) to convert Y151's signed response into a candidate nonnegative inertial coefficient.

**The action functional itself succeeds completely on every tested case.** Isolated bond constants are exact and positive ($R5$: $A_1=8$, $A_2=20$, $M_{\rm loop}=18$; $R6$: $A_1=4$, $A_2=\tfrac{125}{4}$, $M_{\rm loop}=\tfrac{131}{24}$), and transfer exactly to T3R65/T3R66 with no refitting (8/8 total and per-bond predictions), giving a clean topology contrast at fixed $N=3$ ($18-\tfrac{131}{24}=\tfrac{301}{24}$ per R5-for-R6 substitution).

**But the promotion gate — genuine autonomous closure of the full cycle — fails, and Y152 reports this as decisive rather than working around it.** Direct $v_1\to$rest sustains the qualified Y148 autonomous orbit for R5-containing D2R5/T3R65 (4/4 each) but not for all-R6 D2R6/T3R66 (0/4 each — landing instead in an unrecognized phase with no PRV discriminator); direct $v_2\to$rest fails to reach the qualified handoff cut for *any* tested species. Even the R5-containing $v_1$ ingress lands on a projected dressing differing from the canonical start state by 79 normalized relations — an alternate recurrent rest orbit, not simple equality with the historical one.

**Verdict, stated exactly as the evidence supports.** *A positive, topology-sensitive, closed-path action candidate exists* — but *a fully autonomous closed transition loop over rest/$v_1$/$v_2$ does not*, for the current architecture. No mass, energy, force, or equivalence-principle claim follows. Because autonomous closure is a necessary promotion gate, the eleven N=5 action holdouts are deliberately left untouched, and Candidate B/Y99/$M_i$/$\alpha$ remain sealed — preserving a clean population for a genuine blind test once closure is achieved.

**Recommended next stage (Y153 — Autonomous Motion-to-Rest Ingress Closure and Alternate Rest-Orbit Classification).** Keep the Y152 action constants sealed. Characterize the alternate R5-supported $v_1\to$rest orbit and determine whether it is covariantly equivalent to or genuinely distinct from the canonical Y148 orbit; localize the exact residual sending all-R6 $v_1$ ingress to the unrecognized phase; determine whether $v_2$ must pass through $v_1$ before reaching rest rather than landing directly; construct no new action coefficient during this closure work; only once a universal autonomous motion→rest ingress exists should the sealed N=5 Y152 holdout be run with the already-frozen functional.

### 10.1bbbbbb The Y152 closure failure was a premature-readiness artifact, not a bond-type limitation — full dressing settlement closes $v_1\to$rest universally, while direct $v_2\to$rest remains structurally excluded and only the indirect $v_2\to v_1\to$rest route closes, landing on a second genuine autonomous rest dressing (Stage Y153)

Y153 diagnoses Y152's closure failure directly rather than patching the phase detector.

**The failure is history-dependent, not bond-type-dependent.** An independently prepared mature-$v_1$ carrier can enter Y148 rest for both R5 and R6; a rest→$v_1$→rest sequence can fail nearby. Tracing shows intrinsic speed-sector readiness occurs early, but the full relational moving dressing keeps changing for many further rounds — attempting rest formation during that tail can land on an unrecognized transient phase. A preregistered test of two plausible interpretations of that transient found both could be made recurrent on development, failing the required uniqueness test — so Y153 explicitly declines to add an underdetermined new rest phase rule.

**Requiring full covariant dressing settlement before ingress closes $v_1\to$rest completely, with a clean settlement law.** A graph-isomorphism-based readiness quotient (CQ1 — built from current carrier/Q-relation incidence only, no absolute IDs) matches the historical operational readiness signature in 28/28 cases and is relabel-covariant in 448/448 trials. Once used as the ingress gate, all seven original species close 28/28, entering the identical historical phase and sustaining eight further autonomous rest periods. The exact settlement law is $L_{v1}=6N$ (any R5 present) or $6N{+}1$ (all-R6).

**Direct $v_2\to$rest remains excluded even after full settlement — a structural fact, not a premature-dressing artifact.** With settlement law $L_{v2}=3N{+}3$ enforced first, direct stopping still fails 0/28, landing outside the qualified rest manifold with a consistent, distinct structural signature. The only route Y153's protocol permitted next — full $v_2$ settlement, the already-established $v_2\to v_1$ transition, full post-transition $v_1$ settlement ($L_{v1|v2}=6N{-}4$/$6N{-}3$), then the validated $v_1\to$rest ingress — closes 28/28.

**Stopping lands on a second, genuinely autonomous, noncanonical rest dressing.** All 28 ingress cases remain recurrent over eight tested periods, but 27/28 are directly non-isomorphic to the independently-prepared canonical Y148 dressing (the 28th, computationally pathological under direct comparison, is confirmed noncanonical by halo cardinality — 185 vs. 225 — and independently reconfirmed recurrent via a stronger covariant incidence check). Y153 is explicit this does not establish two distinct physical particle states — only two model-internal recurrent local environments of the same identity — and that the earlier orientation-like transients remain best explained as Y93-style finite dressing relaxation, not a persistent internal sector.

**Verdict: AUTONOMOUS_MOTION_TO_REST_INGRESS_CLOSED_AFTER_COVARIANT_FULL_DRESSING_SETTLEMENT_ON_TESTED_ORIGINAL_MANIFOLD**; companions **DIRECT_FULLY_SETTLED_V2_TO_REST_FAILS_28_OF_28**; **V2_TO_V1_TO_REST_PASSES_28_OF_28**; **INGRESS_GENERATES_A_SECOND_AUTONOMOUS_RECURRENT_REST_DRESSING**. Consequence for Y152: its direct-$v_2$ leg is retroactively invalid and must not be promoted; the actually admissible path is $v_2\to v_1\to0$.

**Recommended next stage (Y154 — Autonomous Admissible-Path Loop Action Rebaseline and N5 Blind Holdout).** Freeze the transition action on the now-established admissible paths only, replacing the invalid direct-$v_2$ leg with $v_2\to v_1\to0$, treating CQ1 readiness as an unscored gate rather than an action contribution; validate on the T3/T4 population; only then open the sealed eleven-identity N5 action holdout.

### 10.1cccccc The rebuilt admissible-path action is positive, exact, locally compositional, and passes a completely blind N=5 test on every gate — the first fully validated closed-loop inertial-action candidate this program has produced (Stage Y154)

Y154 rebuilds Y152's action on the Y153-validated admissible paths, with CQ1 settlement excluded from the scored action itself.

**The corrected isolated-bond constants remain positive and exact, and the zero post-settlement reverse-rest contribution is itself informative.** R5: $A_1=8$, $A_2^{\rm adm}=9$, $M_{\rm adm}=\tfrac{119}{6}$; R6: $A_1=4$, $A_2^{\rm adm}=\tfrac{57}{4}$, $M_{\rm adm}=\tfrac{199}{24}$ — both exact across sign/context in all 8 development cases. The zero reverse-rest term after full $v_1$ settlement means the nonzero action is entirely localized to *entering/changing* moving sectors, not to any extra cost of stopping from an already-settled state.

**Composition transfers exactly through higher-body validation and then a genuinely blind N=5 test, with zero exceptions anywhere.** T3/T4 validation (5 species, 20 cases): individual constants, composite additivity, zero nonadjacent residual, and both admissible loop closures all exact 20/20. The previously untouched 11-identity N=5 holdout (44 cases): runtime, per-bond constants, composite total, zero nonadjacent residual, and both loop closures all exact 44/44 — including a clean placement control (all six two-R5 arrangements give the identical total while each bond retains its correct local constant). The resulting law: $M_{\rm adm}=\tfrac{199}{24}(N{-}1)+\tfrac{277}{24}n_{R5}$.

**Verdict: AUTONOMOUS_ADMISSIBLE_PATH_BOND_LOCAL_POSITIVE_ACTION_VALIDATED_ON_BLIND_N5_MANIFOLD**, scope **FINITE_TESTED_LINEAR_CHAIN_MANIFOLD; MODEL_INTERNAL_TRANSITION_ACTION; NOT_PHYSICAL_MASS_OR_ENERGY**. Two execution corrections (a missing scored boundary; a missing archived N5 holdout dependency) were caught and fixed before any development or holdout value counted.

**Recommended next stage (Y155 — Frozen Binding-Sector Comparator Test).** Freeze the Y154 population table immutably as the response side; reopen Candidate B and Y99 $\mathcal{F}_{\rm flux}$ without redefinition; compare fixed-$N$ R5-for-R6 replacement contrasts and multi-R5 scaling; compare separately to Y81 $M_i$ as a negative control; fit no species-specific correction and add no DS001 baseline merely to improve proportionality; distinguish structural binding-contrast proportionality from total-value proportionality explicitly.

### 10.1dddddd A single calibration point fixes an exact same-$N$ topology-contrast law that then transfers, with zero refitting, across all 38 pairwise comparisons in the complete tested population — the strongest, most extensively validated cross-observable agreement this investigation has produced, and an explicit, transparent reversal of Y151's incomplete-loop sign conclusion (Stage Y155)

Y155 reopens the sealed comparators only after Y154 was frozen, and finds an exact structural correspondence together with a clean total-value negative.

**One calibration point (D2R5 vs. D2R6) fixes a single scale that then transfers exactly to every other held-out topology contrast with no refitting.** $\kappa=\Delta M_{\rm adm}/\Delta\mathcal{F}_{\rm flux}=\tfrac{277}{48}=-\Delta M_{\rm adm}/\Delta B_{\rm proj}$. Applied cold to the remaining 14 held-out identities (T3R65, both surviving tetramers, all 11 N=5 chains): both contrast laws hold exactly, 14/14 each (15/15 including the calibration pair). Extended to every same-$N$ pair in the tested population regardless of which member is used as reference — not only the all-R6 baseline — both laws hold in all **38/38** pairwise comparisons, while $\Delta M_i^{Y81}=0$ fails all 38 (by construction, since $M_i$ has no same-$N$ variation at all).

**The result explicitly reverses, and states that it reverses, Y151's earlier forward-only sign conclusion.** Y151's incomplete (non-loop-closed) cross-response was anti-aligned with $\mathcal{F}_{\rm flux}$ and aligned with $B$; the corrected, fully admissible-path action is aligned with $\mathcal{F}_{\rm flux}$ and anti-aligned with $B$, with the identical magnitude ratio in both directions. Y155 states this openly as a consequence of using the genuinely closed loop rather than silently superseding the earlier number.

**The total-value gate fails cleanly and for a stated structural reason, keeping the contrast result from being over-read.** Zero-intercept fits against both $\mathcal{F}_{\rm flux}$ and $B$ fail every development and N5 row (0/7, 0/11 each; residuals up to 86.72%). The reason is structural, not a fitting failure: $M_{\rm adm}$'s all-R6 baseline scales as $N{-}1$ while $\mathcal{F}_{\rm flux}$ and $B$ have different baseline structures ($20N$ and $3N^2{+}44N{+}1$ respectively) — and DS001 ($N{=}1$) has exactly zero bond-local action while every rest-content candidate assigns it a nonzero value, so $M_{\rm adm}$ cannot by itself be a complete one-particle mass observable. An explanatory (not fitted) decomposition makes this precise: $M_{\rm adm}=\tfrac{199}{24}(N{-}1)+\tfrac{277}{48}\Delta\mathcal{F}_{\rm flux}$ — an all-R6 baseline term the rest-content binding residual does not encode, plus an R5-topology excess term that is exactly what the contrast law captures.

**Verdict: EXACT_R5_SUBSTITUTION_CORRESPONDENCE_WITH_CAUSAL_REST_CONTENT; TOTAL_MASS_ENERGY_EQUIVALENCE_NOT_ESTABLISHED.** This is the first exact cross-observable link this program has established between the autonomous transition-action branch and the causal-rest-content branch — frozen before comparison, blind-validated on N=5, fixed by one calibration point, and holding on every one of 38 same-$N$ pairwise contrasts in the complete tested population. It remains explicitly narrower than mass-energy equivalence: no one-body action term, no total-value proportionality, no physical rest-energy normalization.

**Recommended next stage (Y156 — Autonomous One-Body Admissible-Path Action and Full Inertial Decomposition).** Derive a one-body action independently, using isolated DS001 under the same Y153/Y154 admissible paths and matched-null construction, with a one-body relation set defined as carrier-touching relations that do not touch another constituent core; freeze a DS001 coefficient before testing composites; test whether composite one-body action is exactly $N$ times that coefficient once the already-frozen bond-local term is separated out; keep every rest-content comparator sealed during derivation. This determines whether the Y155 correspondence is one sector of a larger additive inertia structure or an isolated topology coincidence.

### 10.1eeeeee A positive, covariant isolated one-body action is found for DS001 — but the proposed self-plus-bond decomposition fails completely on composites, with an exact accounting identity pinpointing current-core incidence itself as the flaw (Stage Y156)

Y156 freezes a one-body observable (relations touching exactly one current core) before opening any composite, using the identical Y154 admissible paths and matched-null construction.

**Isolated DS001 passes cleanly and is frozen first.** $A_1^{(1)}=\tfrac{2359}{4}$, $A_2^{(1)}=555$, $M_1=\tfrac{8881}{6}\approx1480.17$ — exact across all four sign/context replicas, both loops closing to autonomous rest phase `e2`, relabel-covariant 256/256.

**The transfer to composites fails universally and immediately.** Against the frozen prediction $M_{\rm one}({\rm composite})=N\cdot\tfrac{8881}{6}$: 0/28 composite totals match, 0/88 individual constituent rows match the isolated DS001 coefficient — while every Y154 bond coefficient and closure gate remains exactly intact in the same 28 cases, ruling out any dynamical cause.

**The mechanism is pinned down by an exact, independently verified accounting identity.** Because the recurrent core's own vertices change over time, a persistent (never-born-or-destroyed) relation can migrate between "touches only constituent $i$," "touches only $j$," and "touches the bond" without any birth/death event — and each such migration silently injects **two** extra edits into the channel-summed action relative to the true whole-halo edit count: $\sum_c|C_c(t)\triangle C_c(t{+}1)| = |H(t)\triangle H(t{+}1)| + 2m_t$, confirmed exactly on real traces (D2R5: 376 migrations, excess $752=2\times376$; D2R6: 331 migrations, excess $662=2\times331$).

**Verdict: CURRENT_CORE_INCIDENCE_ONE_BODY_DECOMPOSITION_FAILS.** This does not retract Y154 — the bond-local action was frozen and validated as a specific cross-bond quantity, never assumed to be one piece of an additive self-plus-bond split. What fails is the *stronger* claim that current-core incidence can serve as an immutable partition of the whole action at all. The N=5 one-body holdout and every comparator remain sealed.

**Recommended next stage (Y157 — Immutable Causal-Ownership Action Decomposition).** Replace current-core incidence with an immutable owner assigned once at a relation instance's birth (via the qualified Y96 producer identity and Y119 bond-relay role), never reassigned by later core turnover; require zero channel migration by construction; derive DS001 and isolated R5/R6 owner channels; validate on the original population before any N5 holdout is opened.

### 10.1ffffff Immutable birth-ownership removes the channel-migration artifact exactly, but first-contact ownership still misattributes old vacuum supply, breaking DS001's own sign symmetry (Stage Y157)

Y157 assigns each relation instance a permanent owner at first carrier contact, removing Y156's exact migration pathology — and finds a different, more informative failure underneath.

**DS001's action is context-replicated but weakly sign-odd.** $A_1^{\rm self}=271.5$ in all four cases, but $A_2^{\rm self}$ differs by exactly one unit between sign orientations ($248$ vs. $249$), traced to a single extra pre-existing vacuum-produced relay entering carrier contact asymmetrically between the two directions during the $v_2\to v_1$ leg.

**Verdict: FIRST_CONTACT_IMMUTABLE_OWNERSHIP_FAILS_DS001_SIGN_EVEN_GATE.** No composite was opened. A post-verdict diagnostic — restricting SELF strictly to instances whose immutable producer event is itself a carrier/lifecycle event, leaving all `VACUUM_FIRE`/seed instances as environmental regardless of contact — restores exact sign symmetry immediately ($A_1=A_2=24$, $M=60$, 4/4), pointing precisely at the needed fix without yet being promoted.

**Recommended next stage (Y158 — Producer-Owned Self/Environment/Bond Action Decomposition).** Freeze a strict producer-defined split before measuring anything: SELF only for instances genuinely produced by carrier/lifecycle events of that constituent; ENV permanently for vacuum/seed and untagged shared productions regardless of later contact; BOND only for instances born already touching the adjacent pair. Validate DS001 first, then isolated R5/R6 dimers, before any higher-body or N5 holdout.

### 10.1gggggg The producer-owned split passes cleanly for DS001, but strict bond-produced action is exactly zero for both bond types — revealing that the celebrated Y154/Y155 bond action is fundamentally a measure of environmental relay dressing migration, not intrinsically bond-produced structure (Stage Y158)

Y158 freezes the strict producer split before any measurement, and the result reframes what Y154/Y155 actually measured, without retracting either.

**DS001 passes exactly**, with SELF ($M{=}60$) cleanly separated from a small ENV contribution ($M{=}5$, entirely the ordinary rest↔motion marker handoff, not physical vacuum work) — reconstructed exactly across 888/888 boundary checks with zero owner mutations.

**Strictly producer-owned bond action is exactly zero for both dimers, in all 8/8 development cases.** The only historically BOND-owned instance in either species is the original seed relation, which contributes no scored action; no new native relay satisfying the dual-core birth condition ever enters the BOND channel. DS001-transfer for SELF also fails (composite SELF is not $2\times60$, and is itself sign/context-dependent) — a second, independent negative alongside the zero-bond result.

**A post-verdict forensic explains the entire Y154 signal mechanistically.** Every adjacent-core relation present at mature rest — all four for R5, the single one for R6 — is a `VACUUM_FIRE` product, permanently ENV under strict producer ownership. Across all 12 sampled D2 trajectories (rest, $v_1$, $v_2\to v_1$, both bond types), every observed change in cross-core incidence is a persistent ENV instance moving in or out of current-core contact; zero true cross-instance births or deaths occur at any sampled boundary. R5 shows far more environmental traffic than R6 (190 ENV entries/exits per case vs. 86), matching the same-direction asymmetry already known since Y132–Y133.

**Verdict: PRODUCER_SPLIT_DS001_PASS; DIMER_IMMUTABLE_BOND_DECOMPOSITION_FAIL**, mechanistic **CURRENT_CROSS_INCIDENCE_CHANGE_IS_PERSISTENT_RELATION_REASSIGNMENT**. Y154's positive `119/6`/`199/24` bond coefficients are explicitly not refit or withdrawn — Y158 sharply reinterprets, rather than retracts, what kind of quantity they measure: an environmental-relay incidence/dressing response that differs between R5 and R6 because the relay pools themselves differ (in count and lifecycle), not a measure of intrinsic bond-produced relation turnover. This also sharply limits the Y155 correspondence: a structural correlation between rest recurrence and environmental dressing does not by itself establish that the dressing produces or resists acceleration.

**Recommended next stage (Y159 — Environmental Relay Incidence Continuity and Intrinsic-Selector Causality).** Build an exact joint ledger of producer births/deaths, ENV/SELF transfer into current-core sectors, and pair-local relay occupancy; qualify it on isolated D2; then run a genuine causal intervention on the *intrinsic* (Y142/Y148) moving-sector selection process — never the old external one Y135 already tested — by suppressing the specific environmental relations predicted to supply the next step, and ask whether intrinsic sector choice or displacement actually changes. Do not repeat Y135's already-answered question; keep the N5 holdout sealed until a genuine causal link survives development.

### 10.1hhhhhh Two environmental channels are cleanly separated for the first time: the topology-sensitive relay dressing behind Y154/Y155 has no causal power over intrinsic motion, but a distinct environmental relation is found to be genuinely upstream of the autonomous sector classifier — the first real crack in the environment-cannot-influence-motion wall standing since Y135 (Stage Y159)

Y159 re-asks the causal question Y135 closed for the old external selector, now against the genuinely autonomous Y142/Y148 engine, and gets two different answers for two different channels.

**Pair incidence turnover is confirmed almost entirely environmental contact transfer, not instance creation/destruction, with an exact reconstruction identity holding throughout.** Across the complete D2 population (616/616 boundary rows), persistent-in exactly equals persistent-out (1,144 each) with zero births/deaths at scored boundaries; R5 shows 190 ENV transfers per case against R6's 86, again matching the established asymmetry.

**The specific channel that produced Y154/Y155's signal — PAIR_ENV_RELAY — is definitively not causal for intrinsic motion.** Deleting the complete set of ENV relations currently touching both adjacent cores (exactly 3 per R5 bond, 1 per R6 bond, confirmed transferring exactly by bond type across all 104 higher-body validation slots including both tetramer R5 placements) changes the intrinsic sector choice in 0/56 mature-state cases and, reapplied every round for four successive rounds, leaves displacement exact in 224/224 rounds.

**A different, genuinely upstream channel is found: SECTOR_ENV.** Exactly one ENV relation targets each moving constituent's intrinsic sector-classifying pair; deleting it reclassifies the constituent from $v_1$ to $v_2$ in the state-derived classifier in 88/88 tests (across D2 and the full higher-body validation population) — a real, causal, environment-to-classifier link. But the very next compound event still displaces by the *old* $v_1$ amount in 88/88 cases, showing an exact one-round dynamical lag between classifier reclassification and any actual motion response.

**Verdict: PAIR_ENV_RELAY_DOWNSTREAM_CONSTITUTIVE_DRESSING_NOT_CAUSAL_FOR_INTRINSIC_MOTION**; companion **DISTINCT_ENV_SECTOR_RELATION_IS_UPSTREAM_OF_INTRINSIC_SECTOR_CLASSIFIER**. This is explicitly not a repeat of Y135: the intrinsic selector genuinely is environmentally sensitive through one specific channel, while the topology-sensitive channel behind the landmark Y154/Y155 result is not — ruling out the interpretation that Y154's positive action is itself a resisting mechanism, while opening, for the first time since Y135, a real candidate causal pathway from environment to motion.

**Recommended next stage (Y160 — Environmental Sector-Bit Intervention and Autonomous Speed-Response Test).** Freeze the SECTOR_ENV deletion; from mature $v_1$, remove only the single relation that flips the intrinsic sector bit and continue under unchanged intrinsic compound motion with no requested magnitude and no fitted edits; test pulse vs. sustained suppression, exact speed settlement, sign/context symmetry, and R5/R6 dependence; the central question is whether the classifier change eventually produces a genuine delayed autonomous $v_1\to v_2$ acceleration. Only if that chain closes should any new inertia interpretation be considered; keep N5 and every mass/rest-energy comparator sealed during mechanism discovery.

### 10.1iiiiii Pure environmental deletion — never an external velocity request — causes genuine, sustained, self-maintaining autonomous acceleration across the entire tested population, with an exact staircase kinematic response and a clean causal explanation for its two-round lag (Stage Y160)

Y160 closes the causal chain Y159 opened: from mature $v_1$, it deletes only SECTOR_ENV relations (never touching the grammar, never issuing a magnitude) and asks whether real displacement changes.

**The clamp branch produces universal, exact, self-sustaining acceleration from only two rounds of deletion.** Across the complete seven-species population (28 cases, both geometries, both signs — 1,344 scored macro-rounds, 4,224 constituent events), the exact kinematic sequence $|v|:1\to\tfrac32\to2$ holds in every case, with exact $v_2$ persisting for all of rounds 3–16 (392/392) under the unmodified intrinsic grammar and **zero further deletions** — only $2N$ total relation removals per case (176 across the whole population) permanently relocate the carrier into the faster autonomous attractor. Controls confirm the matched baseline stays at exact $v_1$ throughout (448/448).

**The two-round lag has an exact, non-mysterious causal explanation.** Because each Y141/Y142 compound event reads the *pre-event* relational geometry to select its gate, deleting the sector relation cannot retroactively alter a gate already fired — it only changes the material available to the *next* event. The resulting chain (remove sector bit → classifier flips to $m{=}2$ → next event writes $v_2$-relay geometry → mixed transition round → full $v_2$ carrier gates) makes the exact $1\to\tfrac32\to2$ staircase a direct causal consequence, not a puzzle. Dressing settlement is confirmed to lag the kinematic change, not precede it: $L_{CQ}=3N+3$ for all-R6, with a one-round sign-sensitive shift for one-R5 species — speed changes first, complete environmental dressing follows.

**A single pulse does not reach sustained $v_2$, but reveals a second reproducible autonomous phenomenon instead of simply reverting.** All 28 pulse cases (0/28 reaching sustained $v_2$ in the 16-round horizon) settle into an exact, self-perpetuating $|v|=\tfrac32$ state for rounds 2–16 (420/420), with the intrinsic magnitude bit and SECTOR_ENV incidence both cycling $2,1,2,1,\ldots$. This is recorded honestly as a finite-horizon candidate period-2 orbit, explicitly not promoted as an established third asymptotic velocity sector — full recurrent classification was not preregistered for this branch.

**The result is precisely separated from the Y154/Y158/Y159 bond-action thread rather than conflated with it.** The architecture is now experimentally split into two independent chains: $\text{SECTOR\_ENV}\to\text{native magnitude bit}\to\text{future relay/gate geometry}\to\text{autonomous speed}$ (causal, established here) versus $\text{motion/topology}\to\text{PAIR\_ENV\_RELAY constitutive dressing}$ (downstream only, established at Y159). Y160 explicitly does not retroactively promote Y154's bond action to a causal inertial mechanism — that remains a separate, still-open question.

**Verdict: FINITE_ENV_SECTOR_SUPPRESSION_CAUSES_AUTONOMOUS_V1_TO_V2_ACCELERATION_ON_TESTED_ORIGINAL_COMPOSITE_MANIFOLD**; companions **SECTOR_STATE_CHANGE_PRECEDES_KINEMATIC_RESPONSE_BY_TWO_MACRO_ROUNDS**; **V2_STATE_SELF_MAINTAINS_AFTER_SECTOR_SUPPRESSION_CEASES**; **TESTED_ALTERNATING_SECTOR_CYCLE_WITH_EXACT_V3_OVER_2_DISPLACEMENT**. This is the first result in the entire autonomous FBCL branch where a targeted environmental intervention changes subsequent intrinsic carrier speed with no external magnitude ever passed to the moving update rule. Physical interpretation (mass, force, work, momentum/energy transfer, gravitational equivalence) remains explicitly unestablished; N=5, $\mathcal{F}_{\rm flux}$, Candidate B, $M_i$, and every Y155 scale/$\alpha$ remain sealed.

**Recommended next stage (Y161 — Autonomous Velocity-Spectrum and Reversible Environmental Sector Control).** Keep every mass/rest-energy comparator sealed. First, classify the pulse-induced $|v|=\tfrac32$ response with longer, phase-closed histories to determine whether it is a genuine recurrent period-2 orbit, and search for other rational intermediate velocities from minimal environmental pulse sequences without fitting to a desired outcome. Second, derive a lawful *reverse* control: starting from mature $v_2$, identify a future-blind environmental construction (from the frozen vacuum/causal spine, not reverse-engineered from the desired result) that could supply the single outside source $v_1$ requires, freeze it before intervening, and test whether it autonomously produces $v_2\to v_1$ with a correspondingly delayed kinematic response. Only if reversible control closes should the N=5 population be opened as a blind causal-transfer test, and only after that should the program reconsider defining an independent inertial work/action tied specifically to changing the causal sector state.

### 10.1jjjjjj The $|v|=\tfrac32$ intermediate response is confirmed a genuine, long-horizon recurrent period-2 orbit — a real third autonomous speed structure — while the first reverse-control attempt fails sign covariance cleanly, with the exact geometric reason pinned down rather than patched (Stage Y161)

Y161 tests both open questions from Y160: is the pulse response real, and can the acceleration be reversed?

**The $\tfrac32$ orbit is confirmed genuinely recurrent on a much longer horizon and a wider population.** A single `SECTOR_ENV` deletion from mature $v_1$, with no further intervention, sustains an exact period-2 sector/displacement cycle for the full 128-round test: across D2R5, D2R6, T3R65, T3R66 (16/16 cases), all 1,792 frozen scored rounds (17–128) show exactly signed $|v|=\tfrac32$, with CQ1 dressing closing isomorphically to the same-parity reference every time. A supplementary blind delete/allow word atlas (all 20 length-2–4 binary words on one anchor) finds only two recurrent classes — period-2 $\tfrac32$ (6 words) and period-1 $v_2$ (14 words) — no third class appears, and the result is explicitly scoped as anchor-diagnostic rather than population-general.

**The first future-blind reverse control works exactly for one sign and fails cleanly, structurally, for the other.** Adding a single source relation at the intrinsic gate's own selected exterior vertex, from mature $v_2$ with no requested velocity, drives all four positive-direction D2 cases through $2\to\tfrac32\to1$ with exact native $v_1$ sustained from round 3 (all core/bond/lineage checks pass). All four negative-direction cases fail identically: after a legitimate first round, the classifier legitimately reaches $v_1$, but the same source rule then creates a second outside source and the chooser halts with an explicit ambiguity error rather than silently producing a wrong answer.

**The exact geometric cause is pinned down, and the temptation to patch and rerun immediately is explicitly declined.** A post-verdict audit of mature $v_1$ finds the sector source equals the selected exterior vertex $e$ for positive motion, but equals $e$ shifted three steps backward along the causal spine for negative motion, in 8/8 constituent rows each — a clean, representation-independent asymmetry, not a fitting artifact. Y161 states directly that it does not test a corrected rule after seeing this failure, deferring the fix to a fresh, separately-justified hypothesis.

**Verdict: V3_OVER_2_PERIOD2_CARRIER_DRESSING_ORBIT_VALIDATED_ON_COMPLETED_D2_PLUS_T3_MANIFOLD** (positive); **FUTURE_BLIND_V2_TO_V1_ENVIRONMENTAL_CONTROL_FAILS_SIGN_COVARIANCE** (negative). The autonomous grammar is now shown to support at least three distinct positive speed structures on the tested manifold ($v_1$, the period-2 $\tfrac32$ orbit, $v_2$), with the intermediate state sustained entirely by the intrinsic compound grammar rather than any controller-supplied magnitude. N=5 and every mass/energy comparator remain sealed.

**Recommended next stage (Y162 — Sign-Covariant Reverse Sector Source and Three-Speed Control Closure).** Freeze a genuinely direction-covariant reverse source operator — using the Y161 mature-$v_1$ geometry as a hypothesis to justify and test fresh, not as an automatic repair — and retest D2 both signs before validating on T3/T4; only if both signs close should N5 be opened; separately test reversible transitions among $v_1$, the period-2 orbit, and $v_2$. Only after genuine three-speed reversible control closes should inertial-action/rest-content comparisons reopen.

### 10.1kkkkkk A sign-covariant-looking reverse source rule, built directly from the Y161 mature-state geometry, fails on the negative-direction transient for a precise structural reason — a mature-state fact extrapolated onto a still-settling trajectory, caught before any rescue attempt (Stage Y162)

Y162 freezes the Y161-suggested candidate — source $=e$ for positive motion, source $=$ three spine-steps back from $e$ for negative motion — and tests it directly rather than assuming the mature-state pattern transfers.

**The rule works exactly for positive-direction transitions.** All four D2 positive cases sustain the full $2\to\tfrac32\to1\to\cdots\to1$ sequence with exact native $v_1$ from round 3 through round 16 (56/56 scored rounds), core/bond/support/lineage valid throughout, using only two relation insertions per constituent on the first two frontiers.

**The rule fails all four negative-direction cases at an identical, precisely located structural collision — not a numeric or R5-specific error.** Round 1 executes correctly at exact $v_2$ displacement; at the second pre-round frontier, the prescribed source coincides with the current carrier's own role `c1` — the relation the rule would insert duplicates an endpoint of the pair it targets, and the source-validity gate correctly rejects it before any invalid relation is created. The report confirms this is not a labeling artifact: any bijective relabeling preserves the source-equals-endpoint collision.

**The diagnosed mechanism generalizes the exact lesson, not just the specific fix.** Y161's source formula was measured on the *fully mature* $v_1$ state; Y162 shows it cannot be extrapolated unchanged onto the still-settling $v_2\to v_1$ transient, because the exterior gate vertex, carrier roles, and causal spine are all still moving relative to each other during the transition. A formula that is exactly covariant at one endpoint of a trajectory can still be dynamically inadmissible partway along it — the fix needed is a phase- or event-conditioned transport operator, not a fixed sign-dependent offset.

**Verdict: Y162_SIGN_CONJUGATE_ENDPOINT_SOURCE_NOT_TRANSITION_SAFE.** This does not undermine the already-qualified Y160 forward acceleration or the Y161 period-2 orbit, and does not reopen the Y159 finding that the topology-sensitive pair-relay channel remains downstream dressing, not upstream control — the separate constituent-local sector relation remains genuinely causal, only its universal inverse is still unconstructed. T3/T4 reverse validation, three-speed control diagnostics, and the N5 holdout remain unopened; no mass/energy comparator was touched.

**Recommended next stage (Y163 — Transition-Phase-Resolved Reverse Sector Source).** Do not propose another fixed endpoint-offset rule. Study the actual legal $v_2\to v_1$ transient's sequence of causal-spine and role-relative source geometry frontier by frontier, and derive a source operator conditioned on that transitional phase rather than only on final-state direction. Require legality at every finite transitional frontier before freezing; only then retest D2 both signs, validate on higher composites, and reopen N5. Keep the Y160/Y161 forward and period-2 results intact and every energy/inertial comparison firewall closed.

### 10.1llllll The Y162 reverse-control failure was an occupancy-policy error, not a source-geometry problem — once corrected, repeated two-speed control closes across every tested composite, with a blind-predicted settling law confirmed on the full N5 population (Stage Y163)

Y163 was executed as a sequence of separately frozen sub-experiments under substantial infrastructure strain (repeated host timeouts, one session interruption, a packaging CRC fault), each checkpointed independently. Read in order, they tell a single coherent story.

**Two structural searches for a better source vertex fail honestly.** A producer-event ancestry selector ("nearest strict causal ancestor of the gate vertex") is unique in only 22/152 recorded observations and is not promoted; it also establishes that requiring a source to precede the gate's *birth* is stronger than requiring it to exist before the *intervention*, and the two must not be conflated. A preregistered 33-selector producer-role incidence census (5,016 evaluations) finds only three globally core-exterior singleton selectors, and the only one reproducing every known-good positive assignment is the original `source=e` rule itself — no new geometry is found. Both are reported as bounded negatives.

**The real fix is an occupancy policy, not a vertex choice.** Holding a common policy fixed — if a lawful outside source into $\{c_0,c_1\}$ already exists, retain it and add nothing; only if the sector is empty compute and insert a source — three different source recipes (E: $s=e$; B0: $c_0$.birth.$v$; C1: $c_1$.child.$v$) all pass the paired D2 gate 8/8 in both signs, while the no-addition control stays at $v_2$ in 8/8. The verifier confirms the three implementations differ only in the recipe clause. Y162's negative-sign failure therefore traces to the historical *unconditional* insertion creating a second source (and the endpoint collision) where one was already present. E, the simplest passing recipe, is chosen for transfer as a simplicity preference, explicitly not as proof of a unique law. E also passes independent CQ1 dressing qualification 8/8.

**Transfer and repeated control close across the entire tested population.**
- Passive 64-round continuation (T3/T4, two vacuum lengths): 40/40; the earlier 16-round dressing gate remains a failure and is not retroactively reclassified.
- Blind N5 reverse-transfer holdout (unchanged E, previously sealed): **44/44**.
- Repeated round-trip $v_1\to v_2\to v_1\to v_2\to v_1$, 64 native rounds per leg, no resets: D2 8/8 (32/32 legs); T3/T4 20/20 (80/80 legs); N5 completion run **44/44 (176/176 legs, 44/44 256-round untouched controls, 22,528 exact independent graph comparisons)**.

**A preregistered settling law is confirmed blind.** First CQ1 reference match after return to $v_1$ was predicted before the relevant data existed as (sum of bond spacings) + 4, equivalently $24+n_{R6}$ for N5 chains. It matched 24/24 T4 cases and then 44/44 N5 cases. It was never used as a pass criterion.

**Execution integrity under strain.** The independent verifier caught a silently overwritten constituent-count variable (invalid first T3/T4 attempt, retained and excluded) and a 1,800-vs-1,860 vacuum-size configuration mismatch (old compliance claim withdrawn, both configurations tested). An interrupted cohort was replayed only after exact saved-prefix audit. The original 900-second N5 run's four genuine untouched-control timeouts were **not** retried or converted; a new, separately frozen 1,500-second completion run with compact checkpointing and at most two concurrent cases was opened instead. One cohort ran under a newer Python/NetworkX version with exact initial-digest reproduction — disclosed as source-hash reproducibility, not full environment replication.

**Verdict: Y163 CLOSED / PASS** for repeated, externally scheduled two-speed control under frozen native dynamics and the frozen deletion/E-source operators. Scope explicitly excludes: spontaneous or native acceleration laws, a reversible three-speed family including rest and the period-2 $v{=}\tfrac32$ orbit, any $E_0$/$M_i$/$\alpha$ relation, and any physical particle, mass, or gravity claim. N5 is now a seen population and may not serve as blind holdout for subsequent rule development.

**Recommended next stage (Y164 — Three-Speed Evidence Map and Reachability Challenge).** Do not rerun Y163 cases. Reconcile all existing rest ↔ $v_1$ ↔ $v_2$ (and $\tfrac32$ orbit) evidence across D2, T3/T4 and N5, separating native transitions from externally prescribed controls; identify concrete missing conjunctions (leg, sign, phase, geometry); only then freeze a distinct three-speed reachability/reversibility test with its own population, horizon, references, CQ1/health gates, resource cap and disjoint holdouts. Keep species selection blind to $E_0/M_i$; reopen the global $M_i=\alpha E_0$ test only if a topology-resolving independent inertial observable and genuine multi-speed controls both exist.

### 10.1mmmmmm Two native two-R5-bond trimer structures recur exactly for 256 untouched rounds across four genuinely independent vacuum histories — the first population test in this program using independent vacuum seeds rather than translated sites (Stage Y164, D8E)

Y164's final gate, D8E, validates a frozen negative-direction trimer population prepared entirely by the original native rules: `T3R55` and `T3R56`, each in both P/R orientations, on four previously unused 2,600-event native vacuum histories (seeds 83003101/107/113/119). No manual bond construction, patched engine, or survivor-based seed replacement was permitted; every slot stayed in the denominator.

**All 16/16 preparations qualified and passed 256/256 fully untreated native-$v_2$ rounds**, preserving both live bonds, core/support/lineage health, exact negative two-unit displacement, homogeneous chooser sectors $[2,2,2]$, and exact phase-colored CQ1 period-1 graph recurrence. A separately authored verifier independently rebuilt every initial state and replayed all 4,096 observations. Post-verdict, P and R preparations are graph-isomorphic within each family in every vacuum, while T3R55 and T3R56 are mutually non-isomorphic and each matches its original D8C development class.

**Why this matters methodologically.** Every earlier population test used translated sites within one deterministic vacuum history (the P/R "contexts"), which are replications rather than independent samples. D8E is the first to vary the vacuum history itself, which is a materially stronger robustness test.

**Verdict: `AUDIT_PASS_FULL_POPULATION`** for finite-horizon (256-round) recurrence of this negative-direction trimer population. Explicitly not tested: $E_0$, $M_i$, $M_i=\alpha E_0$, positive-direction formation, reversible native bond formation/dissociation, or stability beyond 256 rounds. The two graph classes are not claimed to be physically distinct species.

### 10.1nnnnnn Pilot mass-energy program (Y165): a single recurrent particle offers nothing to respond to; a pair under one new autonomous scheduling rule shows a reproducible, causally necessary, direction-covariant partner-dependent slowdown of the trailing carrier (Stage Y165, D3-4 and D3-5)

Y165 began as a pilot search for mass-energy signatures on a small species subset, run in parallel with Y164. Initial single-particle tests were negative. The investigator's redirection was that an isolated particle has no partner to exchange anything with, so no interaction-mediated response can be measured on it by construction; the program therefore moved to two-particle worlds. (A single particle can still be probed by an external perturbation, as Y160–Y163 did; what an isolated particle lacks is a *native* source of perturbation.)

**D3-4A — a causal distinction behind the two-particle failures.** Earlier D3-3 two-particle runs lost carriers. Event-by-event re-reading found that every mature moving DS001 exposes a valid predictive carrier gate reaching its inherited old source, while a competing legal gate shares four core vertices but uses a recently created fresh vertex. Across 37 development events, 9/9 health failures selected this **fresh-source rival**; all safe events did not. This was derivational evidence on exposed data, not a holdout.

**D3-4B — one new scheduling postulate, stated as such.** A global scheduler lets the unchanged Y33 RNG pick a legal gate; if it picks the fresh-source four-core sibling of a currently qualified predictive gate, that rival is deferred and the outstanding predictive recurrence event runs instead. Everything else runs unchanged; no velocity, turn order, distance threshold or attraction bias is supplied. The rewrite grammar is untouched, but this is an **explicit model extension**: an established recurrence obligation takes precedence over a younger sibling gate consuming the same local structure. It redirects a substantial fraction of events (240 of 1,536 in the holdout) and should be reported prominently in any write-up as an added rule on which multi-particle survival depends.

**D3-4C — prospective holdout.** Four unused vacua × three contexts × four worlds (AB, A-only, B-only, vacuum-only) = 48 arms: **48/48** completed 32 scored events with all cores, lineage and supports healthy, and independent replay reproduced all 1,536 events (496 carrier, 240 redirects, 1,040 vacuum). This is the first demonstration in the program of mature recurrent particles coexisting with ordinary vacuum rewriting under a single future-blind global event rule, with no externally prescribed particle turns or speeds. Separation changes at $d=7$ were fully explained by unequal carrier-event counts and are not attraction. A post-holdout forensic at $d=20$ found particle A changing $v_2\to v_1$ in 4/4 paired worlds and 0/4 matched solos.

**D3-5 — prospective reciprocity and causal test.** Four new vacua; offsets $d=12$–$28$; common $+$ and common $-$ motion; normal and mirrored placement; matched solos; 148 registered arms, 4,713 scored events independently replayed (chunked V3 audit, 16/16 chunks PASS).

- **Direction-covariant receiver.** At $d=20$ the receiver responds $v_2\to v_1$ in 4/4 vacua in every one of the four placement/direction contexts, with matched solos 0/8 each. The receiver is always the carrier *trailing* in the common direction of motion; mirroring the placement or reversing the direction swaps it exactly.
- **Causal necessity.** Across 31 responding paired cases and 59 individual $2\to1$ transitions, every transition's defining native-sector relation set contained at least one relation with partner/shared-history provenance (joint preparation, preparation carrier events, or later vacuum fires through the partner's region). Removing only those relations in a read-only predicate diagnostic returned the receiver to $v_2$ in **59/59**. No solo world shows any scored $2\to1$ transition.
- **No simple range law.** The response is absent at close range ($d=12$, and $d=16$ in $-$), sometimes occurs already during warm-up ($d=16$ in $+$, correctly excluded from scored endpoints), and responds 3/4–4/4 at $d=20$–$28$, with timing varying strongly by vacuum history.
- **Accounting.** All 148 arms stay in the denominator: 144 complete, 3 safety stops (paired supports sharing a vertex, cores still valid), 1 with insufficient carrier events. One preparation assertion was corrected before any scored event, and one interrupted solo arm was recovered by exact prefix replay.

**Interpretation.** Under the D3-4 scheduler, a second recurrent carrier can causally alter another carrier's own graph-defined motion state. The effect is one-sided and directional: the trailing carrier slows when its sector acquires relational structure laid down in the leading carrier's region. This reads as a **wake or history encounter**, not a mutual central force. It also connects closely to earlier results: Y161–Y163 showed that *adding* an outside source relation into a carrier's sector drives $v_2\to v_1$, and that is exactly what the partner's footprint supplies here. The pair experiment appears to produce, natively, the same kind of source relation the reverse-control rule inserted by hand. The trailing carrier also moves into the region the leader has just traversed, consistent with Y132's picture of moving carriers recruiting vacuum along their worldline.

**Verdict:** partner-dependent autonomous response **established** at this horizon, with causal necessity of the partner-derived relation and exact placement/direction covariance. **Not established:** reciprocal acceleration, attraction, any range law, conserved exchange, $E_0$, $M_i$, $M_i=\alpha E_0$, or any identification with gravity, electromagnetism or color. The kinematic sign is a direction of motion, not a charge.

**Recommended next stage (Y165-D3-6 — Source versus wake decomposition).** Freeze before outcomes on new vacua at $d=20/24$: simultaneous AB (positive control), partner-first history, receiver-first history, and matched solos, with mirrored placement and both directions. Determine whether the response tracks the partner's current state, continuously regenerated surrounding structure, or a persistent deposited imprint that remains after the partner has moved away. Only after the source channel is identified should a joint carrier+vacuum exchange scalar be frozen and conservation, inertia, or a gravity-like source be considered. A head-on (opposite-direction) configuration, in which neither carrier trails, would be a natural further test of reciprocity.

### 10.1oooooo Investigator hypotheses recorded before D3-6 outcomes: light-cone structure, head-on prediction, vacuum budget, and a Casimir-like mechanism (proposal, no trials run)

These hypotheses were raised by the investigator after D3-5 and are recorded here **before** any head-on or ledger trial, so that later results can be judged against them rather than fitted to them. They are speculative and carry no evidentiary weight until tested.

**1. Light-cone constraint and a registered head-on prediction.** Because every rewrite is local, the substrate has a hard maximum propagation speed per event, giving an effective light cone (compare the directed contact cone of Y123 and the fixed fossil recession rate of Y129). Y132 showed that apparent delayed influence is usually a carrier moving into pre-existing structure rather than a signal traveling toward it, and the D3-5 response appears to be of that kind: the trailing carrier drives into the leader's footprint. In a head-on configuration each carrier's wake lies behind it, so neither can reach the other's wake before reaching its core. **Registered prediction (investigator):** if the response is a wake encounter, no partner-dependent sector change occurs until the cores are within roughly one or two recurrence cycles; an earlier response at trailing-case distances would indicate influence running ahead of the particles and would favor a field-like channel. A known confound to control: much of D3-5's partner-derived provenance came from joint preparation, which D3-6's partner-first and receiver-first arms are designed to separate.

**2. Effective signal speed.** Measure directly the fastest rate at which a change introduced in one carrier's region can appear in the other carrier's speed-setting (sector) relations, giving an operational light-cone speed for the substrate to compare with carrier speeds $v_1$, $v_2$ and the $\tfrac32$ orbit.

**3. Vacuum budget, not vacuum conservation.** The investigator proposed that if the wake represents a change in vacuum structure, a conservation principle would require compensation elsewhere. The model does not conserve vacuum count: every ordinary vacuum fire creates a fresh vertex, and Y109–Y112 found no conserved quantity beyond constituent number. No conservation law is therefore imposed. The testable version is whether some *density, rate or flux* is balanced: a regional ledger of births, consumptions and speed-relevant relations in the inner gap versus the outer flanks of a pair, tracked over time.

**4. Casimir-like mechanism.** In the Casimir effect, boundaries change which vacuum modes can exist between plates, producing a net pressure from an inside/outside asymmetry. The substrate supplies a natural analogue without any added force: Y132 showed moving carriers draw on local vacuum supply, and Y159–Y160 showed that one environmental relation (SECTOR_ENV) causally sets carrier speed. **Hypothesis:** if the region between two carriers has a systematically different supply of speed-setting relations than the outer sides, each carrier's autonomous speed could be biased toward or away from the other. Test by comparing that relation's availability on each side of each carrier. A related classical analogue is Le Sage shadowing, which predicts both attraction and drag on moving bodies; the first interaction observed here is drag-like (the trailing carrier slows), which is noted as a coincidence to examine, not a correspondence.

**Firewall.** None of these tests requires or permits modifying the rewrite grammar or the D3-4 scheduler. $E_0$, $M_i$, $\alpha$ and any gravitational interpretation remain sealed until a source channel is identified and an exchange observable is independently frozen.

### 10.1pppppp The partner-dependent response is carried by persistent deposited history: a leader introduced before the receiver exists produces the response in 24/24 worlds, through relations laid down before the receiver's introduction and lying 5–9 graph steps behind the leader's current core (Stage Y165, D3-6)

D3-6 asks what carries the D3-5 influence: the partner's current state, continually regenerated joint structure, or persistent history deposited before the receiver exists. Grammar and D3-4 scheduler unchanged; four new vacua (83012101/103/107/109); six contexts per vacuum ($d=20$ normal/mirrored in both common directions, $d=24$ normal in both); eight preparation variants: simultaneous (SIM), partner-first (PF, leader introduced and advanced 8 rounds with matched remote-vacuum shams before the receiver exists), receiver-first (RF), four age-matched single-carrier controls, and vacuum-only. 192 arms; all 5,764 scored events independently replayed with zero mismatches; all 192 final-state digests matched.

| Variant | Cases responding | Status |
|---|---:|---|
| SIM | 23/24 | 24 complete |
| PF (partner first) | **24/24** | 24 complete |
| RF (receiver first) | 0/24 | 5 complete, 19 support-overlap stops |
| Four single-carrier controls | **0/96** | all complete |
| Vacuum only | 0/24 | all complete |

**Provenance.** Across 41 PF transitions: every one has a defining native-sector relation whose immutable ancestry reaches the leader's history before receiver introduction; removing only those relations on a read-only copy restores $v_2$ in **41/41**; none requires a relation produced during the scored autonomous phase; every first response has a witness in the leader's early preparation history. At the transition, the responsible relation lies at graph distance 5 (12 events), 6 (19), 7 (3), 8 (6) or 9 (1) from the leader's current core. SIM reproduces D3-5 (49/49 transitions restored by removal); its one nonresponse is kept as a genuine negative. The receiver remains the trailing carrier in every case, preserving D3-5's direction/mirror covariance.

**Notes.** PF worlds begin with a larger gap (the leader's head start) and still respond in every case, early evidence of persistence along the leader's path. RF's 19 support-overlap stops probably reflect the receiver's own head start closing the gap onto the leader's placement site; this inference has not been independently confirmed. Administrative recoveries (one-seed preparation resume with exact SHA reproduction, nine partial cases replayed with exact prefix agreement, per-seed final-state audits after an aggregate timeout) changed no scientific record.

**Verdict:** the causal chain at this horizon is *leading carrier → deposited relational history → later trailing encounter → receiver's native sector change*. Closer to a wake or field-memory substrate than a direct two-core coupling. **Not established:** wake lifetime or decay, propagation velocity, action at arbitrary source distance, reciprocal attraction, source polarity, conserved exchange, inertia, gravity, charge, $E_0$, $M_i$, $\alpha$.

**Recommended next stage (Y165-D3-7 — Wake persistence, propagation and decay).** On new vacua, vary the leader's head-start age (e.g. 4, 8, 16, 32 rounds) and add delay arms before receiver introduction, with matched controls; record each defining wake relation's age, its graph distance from the source core, and whether it persists or is regenerated. A response that persists as the source moves farther away supports stored-field memory; systematic disappearance yields a lifetime. Graph distance is not to be called physical distance until a metric correspondence is established.

### 10.1qqqqqq Revision of the 10.1oooooo investigator hypotheses in light of D3-6 (proposal, no trials run)

The 10.1oooooo record stands as written before D3-6. D3-6 did not test any of those items directly, but its results change how they should be framed. Revisions:

1. **Head-on test — prediction revised, design tightened.** Each carrier's trailing wake lies behind it, so the original "no early interaction" expectation still holds for that component. But D3-6 shows a carrier's *preparation* footprint also carries influence and surrounds its starting site. **Revised registered prediction:** head-on onset distance should correspond to the forward extent of each carrier's deposited footprint (D3-6's 5–9-step measurements are a first estimate). Design: prepare each carrier partner-first style so its footprint is known before the approach; preregister support overlap as a distinct scored *contact* outcome rather than an unassessed safety stop, since overlap is the expected endpoint.
2. **Effective signal speed — folded into D3-7.** The response is a receiver reaching stored structure, not a signal traveling toward it. The relevant measurements are wake-relation age, position relative to the source, and persistence versus regeneration, which D3-7 already proposes.
3. **Vacuum ledger — kept, tied to the wake.** Track the wake relations themselves: count, survival time, position, and whether their total grows, levels or decays as the leader moves on. This addresses the budget question and supplies D3-7's decay law.
4. **Casimir-like asymmetry — kept, with an explicit caveat.** The only interaction observed so far slows the trailing carrier and therefore *increases* separation in the common-direction arrangement; current evidence points away from attraction. The inner-versus-outer relation-supply test remains worthwhile, especially in head-on or stationary arrangements, but must be read against that fact.
5. **New: receiver-speed dependence.** All responses so far are $v_2\to v_1$. Repeat the PF design with the receiver starting at $v_1$ and on the period-2 $\tfrac32$ orbit to determine whether the wake has a consistent effect on motion or acts only on the fastest sector — a property directly relevant to any future inertia observable.

Firewall unchanged: no grammar or scheduler modification; $E_0$, $M_i$, $\alpha$ and gravitational interpretation remain sealed.

### 10.1rrrrrr The partner-dependent interaction is a change in the availability of one specific causal role in the receiver, acting additively or subtractively, carried by persistent deposited history that shows no decay, no forward reach, and no propagation from ordinary later motion (Stage Y165, D3-7A through D3-7G)

Seven sequential sub-stages, each on previously unused native vacua, each with frozen denominators and independent replay. Grammar and D3-4 scheduler unchanged throughout.

**D3-7A — Persistence and age (320 arms).** Leader head-start $H\in\{4,8,16,32\}$ rounds and added pre-receiver delay $Q\in\{0,8,16,32\}$. Valid pair worlds respond **143/143**; receiver-only 0/144, partner-only 0/16, vacuum 0/16. No loss of response or monotonic latency increase with $H$ or $Q$. In 143/143 first responses the necessary relation traces to the original HEAD deposition block; **0/143** need ancestry from the later $Q$ block. In 142/143 the active defining relation is itself a live instance produced before the receiver existed (all 95/95 at $Q>0$), so the structure persists rather than being regenerated. Youngest qualifying witness age 26–171 causal events (median 81), rising with $Q$. Sentinel audit: effective wake relations lie 3–6 graph steps from the leader core at $(H,Q)=(4,0)$ and **23–27** steps at $(32,32)$. No decay cutoff at the tested horizon.

**D3-7B — Causal front (64 arms).** A naturally scheduled leader event $t_0$ was tagged and its descendants traced. $t_0$ lineage entered the receiver's speed predicate in **0/32** pairs; a post-verdict census of all 413 scored leader carrier events found none reaching the receiver's speed-setting relations within 64 events. The tagged lineage does not die out: descendants survive in 32/32 cases, up to 210 instances and causal depth 20. The older preparation-deposited wake still produced responses in 24/32 pairs (0/32 controls). Result: a finite-horizon **non-arrival bound**, not a signal speed.

**D3-7C — Head-on test (100 arms).** Four scored-start separations (14, 22, 30, 38 in the inherited ancestry coordinate), normal and label-mirrored. **32/32** pairs reach support overlap, the preregistered contact outcome, at exactly $|\Delta X_T|=2$, after exactly 6, 10, 14 and 18 carrier events respectively, independent of vacuum history. Before overlap: partner-wake entry into either speed predicate **0/32**; sector change **0/32**; partner-wake relation touching either core 0/32. Each receiver starts only 2–7 graph steps from 52 live partner-history relations, none of which ever enters its speed-setting role. Controls 68/68 complete. Graph proximity alone does not define interaction range.

*Relation to the 10.1oooooo/10.1qqqqqq hypotheses.* The original investigator prediction (no interaction until the cores are within one or two cycles) matches the outcome: nothing happens until contact. The revised prediction (onset at the forward extent of the deposited footprint, about 5–9 steps) did not: there was no onset at all before contact.

**D3-7D — Regional ledger and Casimir-like asymmetry (64 arms).** Co-moving partner-first pairs respond 8/8; head-on pairs reach overlap 8/8 with no response; 48 controls silent. At every co-moving response exactly two partner-derived relations occupy the receiver's outside-source role, but their graph side is not invariant: common-$+$ responses have zero INNER and one or two OUTER wake relations (asymmetry $-1$ or $-2$); common-$-$ responses have either two INNER ($+2$) or two LATERAL (0). The signed inner-minus-outer count therefore neither precedes nor predicts the response, and no fixed regional birth/consumption balance accompanies it. Head-on corridors show substantial rewrite traffic with no coupling. **The simple Casimir-like hypothesis fails**; the invariant is entry into one specific causal role.

**D3-7E — Receiver starting in $v_1$ (84 arms).** $v_2$ benchmark: 16/16 respond $v_2\to v_1$, removal restores $v_2$ 16/16, controls 0/16. $v_1$ receivers: wake enters the speed classifier in 10/16; at entry the receiver stays $v_1$ in 10/10; the wake is the *sole* $v_1$ source in 4/10; 4/16 later show $v_1\leftrightarrow v_2$ toggling, vacuum- and sign-specific; 6/16 show no entry. Controls 0/16. Label mirrors reproduce exactly. The wake acts on the receiver's existing sector state, not as a fixed velocity change.

**D3-7F — DS001 on the period-2 $\tfrac32$ orbit (8 + 64 arms).** DS001 itself is qualified on the $|v|=\tfrac32$ orbit: 8/8 cases, 512/512 scored carrier events at exactly $\pm\tfrac32$, 512/512 same-parity CQ1 returns, independent replay pass. This closes the species gap left by Y161. Wake test (32 pairs, 32 solos): solos 32/32 stay on the orbit. Negative motion: 16/16 first deviations directly wake-caused (removal restores the expected phase); 12 settle to stable $v_1$, 4 slip and recover. Positive motion: 16/16 collapse to stable $v_2$ with **no** partner-wake relation in the classifier, an unexplained pair effect at this stage.

**D3-7G — Two channels, one invariant (24 arms).** A protected-preparation counterfactual rules out the preparation-sham bookkeeping event as necessary. Positive branch: the relation the receiver will later need for its $v_1$ phase is consumed by an ordinary vacuum fire, and in 4/4 cases one of that fire's three inputs was produced by the partner's earliest preparation event; the partner makes a vacuum gate legal that destroys the receiver's future source. Negative branch: the partner-wake relation occupies the source role directly (4/4, surviving protection). **Common invariant: partner history changes the availability of the receiver's $v_1$ outside-source role, either additively (supplying it) or subtractively (enabling its removal).** This also shows that tracing only the final speed-setting relation's ancestry misses constraint-mediated influence.

**Audit.** Every sub-stage preserved its failed or timed-out verifier versions (indentation errors, missing observer bookkeeping, RNG pickle identity, audit labels written into lineage metadata) and resolved them with separately frozen administrative verifiers that changed no scientific check; all partial runs were recovered with exact prefix agreement.

**Critical caveat — where the interaction-capable history comes from.** In every sub-stage the responsible history traces to the leader's *earliest preparation* (the HEAD block in D3-7A; the early-partner event in D3-6 and D3-7G). Later prescribed rounds ($Q$ block, 0/143) and later autonomous events (D3-7B, 0/413) never supplied it. The effective structure therefore looks less like a trail left by motion and more like a persistent remnant of how the leader was introduced, closely resembling the Y129 formation fossils, which Y131 showed are dispensable to the carrier itself. If so, the interaction may depend on the current particle-insertion procedure. This must be resolved before any exchange quantity is built on it.

**Verdict.** Established: persistent, non-decaying (at tested horizon), receiver-state-dependent partner influence acting through a single causal role by additive or subtractive paths; no forward reach before contact; no propagation from ordinary later motion within 64 events; DS001 $\tfrac32$ orbit qualified. Not established: origin of the interaction-capable structure outside the insertion procedure, any conserved exchange, attraction, force law, charge, $E_0$, $M_i$, $\alpha$.

**Recommended next stages.** *(1) Origin test, before any ledger:* using the Y131 surgical-deletion method, remove the leader's formation fossil before introducing the receiver; separately, let a leader run autonomously long enough that its preparation remnant is far behind, then introduce a receiver in its recent autonomous path. If the interaction vanishes in both, it is a formation-remnant effect of the insertion procedure. *(2) Y165-D3-7H causal-role exchange ledger:* track creation, occupancy, consumption and downstream effect of relations eligible for the receiver's source role, under both mechanisms, and test whether any predeclared role-state quantity balances across partner, receiver and vacuum without fitted coefficients. The ledger's interpretation depends on the outcome of (1).

### 10.1ssssss A signed causal-role ledger is validated but conserves nothing and closes no cycle; origin localization then removes every candidate structural carrier and exposes the global scheduler itself as the leading confound for the two-particle interaction (Stage Y165, D3-7H through D3-7M)

Six sub-stages, each on unused native vacua with frozen denominators and independent replay. Grammar and D3-4 scheduler unchanged.

**D3-7H — Causal-role ledger (16 arms, 1,536 events).** Frozen signed ledger $A=R_{\rm pair}-R_{\rm solo}$ (occupancy of the receiver's $v_1$ outside-source role) and transaction label $T=+1$ (partner relation occupies it) or $T=-1$ (partner-enabled vacuum fire consumes the receiver's future source). Primary gate $A=T=A_{\rm sector}$ at first anomaly: **8/8 PASS** (positive: $A=-1$ at receiver event 6, 4/4; negative: $A=+1$ at event 3 or 5, 4/4). All four predeclared simple conservation candidates fail **0/4** each: at the direct response the partner-live count is unchanged and total live relations rise by 6; the subtractive consuming event adds 6 partner-descended and 4 total live relations. A valid signed bookkeeping variable, not a conserved quantity.

**D3-7I — Closed cycle test (16 arms, 3,072 events).** Positive pairs capture to stable $v_2$ (4/4), negative pairs to stable $v_1$ (4/4); solos stay on the $\tfrac32$ orbit. Local period-2 closures after interaction **0/8**; full exchange closures **0/8**. The interaction behaves as a state conversion or capture, not a reversible exchange. A receiver-local CQ1 correction also reclassifies the earlier D3-7H "phase-slip period-2" cases as resumed sector alternation without full recurrent-state recovery.

**D3-7J — Formation-origin gate (48 arms, 9,216 events).** Untouched pairs reproduce the anomaly 8/8. Deleting the exact Y129 formation fossil (9 relations) leaves it in **8/8**, so the compact fossil is not necessary. A receiver placed on an aged leader's recent autonomous path shows **0/8** anomalies, with 339/339 matched receiver events identical to the aged solo. Deleting the wider fossil star (48–51 relations) reorganizes the response to subtractive in 8/8 rather than removing it. Verdict **MIXED_OR_INCONCLUSIVE**. A gate-cache consistency defect in the Y131 deletion helper was caught and corrected (Method Correction A) before any verdict.

**D3-7K — Origin zone (48 arms, 9,216 events).** After 96 autonomous leader events (leader about 250 units away), a receiver placed back at the original zone reproduces the anomaly **8/8**, with the same onset families. Receiver-local ancestry from any aging, post-aging warm-up or scored leader event before onset: **0/8**. A preregistered external first-insertion lineage cone around the current leader contains zero eligible relations (8/8), so that arm is vacuous. Pair and solo neighborhoods of the future receiver site are identical from radius 0 through 7 in 8/8; the first difference is 9–27 outward-crossing relations at radius 8.

**D3-7L — Radius-8 excess (32 arms; 7/8 qualified).** Deleting every pair-only radius-8 attachment (134 total, 130 with earliest-preparation ancestry) leaves the receiver's full trajectory identical to the untreated pair in **7/7**; the equal-count common-boundary control is likewise null. The formation-descended surface is real memory but not the causal carrier. An aggregate label error (counting an unqualified comparison) was corrected post-verdict without rerunning cases.

**D3-7M — Radius-8 deficit (40 arms, 7,680 events).** Deleting the 2–4 solo-only ordinary-vacuum radius-8 relations from the solo leaves its full trajectory unchanged (8/8) and never makes it acquire the pair response (**0/8**). Two-sided boundary equalization still leaves the anomaly in **8/8**.

**The critical post-verdict audit.** At the scored start, pair and solo worlds have equal simulator RNG state in only 1/8 comparisons, **zero common global legal gates in 8/8**, and different event and vertex counters in 8/8. The scheduler draws each event as `rng.choice(gates_set)` over the entire world. A remote leader therefore changes which ordinary vacuum events fire everywhere, including near the receiver, with no causal lineage reaching it. Combined with D3-7K's exact R0–R7 neighborhood equality and D3-7L/M's removal of every radius-8 difference, a divergent vacuum event history after receiver insertion is now the most economical remaining explanation for at least part of the pair-versus-solo contrast. One comparison with equal scored-start RNG still shows the anomaly, so this is not yet a complete explanation.

**Implication for earlier results.** Every Y165 pair-versus-solo contrast (D3-5 onward) compares worlds whose global scheduling histories differ. The direct-occupancy findings (a partner-descended relation in the receiver's speed predicate, whose read-only removal restores the prior sector) remain genuine local causal facts. What is now in question is whether the *pair-versus-solo difference in outcome* reflects that local mechanism, a global scheduling divergence, or both.

**Verdict.** Established: a valid signed causal-role ledger; no simple conservation; no closed exchange cycle (capture); the response is tied to the original prepared zone, not the leader's recent path; neither the compact fossil, the radius-8 excess, nor the radius-8 deficit is causally necessary. Leading confound: global scheduler and RNG coupling. Not established: any genuine current particle-particle interaction independent of scheduling history, conserved exchange, $E_0$, $M_i$, $\alpha$.

**Recommended next stage (Y165-D3-7N — Scheduler-history counterfactual).** The proposed RNG crossover factorial (pair graph with solo RNG and vice versa, plus a common external RNG) and matched-scheduler replay (fire the same ordinary gate in both worlds whenever both expose it) directly target this confound. Two additions are recommended: (i) a **scheduler null distribution**, running the solo alone under many different scheduler RNG streams from the identical frozen state, to measure how often "anomalies" of the same kind arise from scheduling variation with no partner at all; and (ii) an explicit record of which remaining Y165 conclusions survive the scheduler-matched construction. If the anomaly disappears under matched scheduling, the D37 interaction should be classified as a scheduler artifact and retired from the mass-energy path.

### 10.1tttttt The first receiver anomaly is invariant to the scheduler's random stream when measured in receiver steps, and a retrospective check places it where the receiver reaches the leader's original formation region (Stage Y165, D3-7N)

D3-7N tested whether the D37 onset follows the scheduler's random state or the graph. Four unused native vacua (83018201/203/207/209), both signs, aged-origin construction with exact R0–R7 equality at the pre-receiver cut. Six branches per seed/sign transplanted only the simulator scheduler RNG (pair graph with pair, solo, or external RNG; solo graph likewise). 48/48 qualified and completed 192 scored global events (9,216 events). Read-only audit PASS.

**Family A — RNG crossover.** With identical scheduler RNG given to pair and solo, all **24/24** matched-donor comparisons reproduce the native onset exactly in receiver-event coordinates: positive $A=-1$ at $k=6$ (12/12); negative $A=+1$ at the native $k=3$ or $k=5$ for each vacuum (12/12). Solos never show the anomaly under any of the three streams, so this also serves as a small scheduler null distribution. Full receiver histories are *not* RNG-invariant (0/8 identical across donors): global-event timing of onset ranges from 10 to 43 (positive) and 4 to 29 (negative). Pre-onset current-leader receiver touches: 0 across all 24.

**Family B — exact common-gate replay.** Zero exact common global or ordinary gates at both the pre-receiver cut and qualification entry in **8/8**, so the replay family terminated prospectively as not constructible. Part of this is representational: once the worlds create different numbers of vertices, gate tuples cannot match by vertex ID even when structurally equivalent (compare the Y142 covariance lesson). No mapping was invented.

**Verdict:** `RNG_START_STATE_NOT_SUFFICIENT_BUT_EXACT_SCHEDULER_MATCH_NOT_ESTABLISHED`. The scheduler affects timing and later history but does not determine whether, or at which receiver step, onset occurs. The global-scheduler confound of 10.1ssssss is weakened from leading explanation to open question.

**Post-verdict retrospective (D3-7K raw trajectories, non-gating).** Onset is locked to receiver progress, which suggested the relevant difference lies along the receiver's *forward path* rather than around its insertion point (D3-7K's R0–R7 equality was measured only at the insertion site). A check of the D3-7K trajectories supports this:

| Sign | Receiver insertion center | Leader original formation support | Receiver at scored start | Receiver at first anomaly |
|---|---:|---:|---:|---:|
| $+$ | 1250 | 1294–1298 | 1286.5 | **1295.5** ($k=6$, 4/4) |
| $-$ | 1294 | 1250–1254 | 1259.5 | **1252.0** ($k=5$, 3/4); **1255.0** ($k=3$, 1/4) |

Every positive onset and three of four negative onsets occur with the receiver inside the leader's original five-vertex formation interval; the fourth is immediately adjacent. This is a retrospective observation on exposed data and carries no evidentiary weight until tested prospectively. It is consistent with D3-7J (recent path inert), D3-7K (effect follows original geometry), D3-7L/M (structure around the receiver's start dispensable), D3-7J S2 (disturbing the wider fossil star reorganizes the response) and Y132 (a moving carrier entering pre-existing structure rather than receiving a signal). Correction recorded: the eight receiver warm rounds use the $v_1$ operation; most of the forward approach occurs during qualification.

### 10.1uuuuuu Frozen plan for Y165-D3-7O: prospective worldline-encounter test with scheduler bypass (recorded before execution)

Developed jointly by the investigator and two AI assistants after D3-7N and recorded here **before** D3-7O runs.

**Hypothesis.** The receiver does not respond to the remote leader. Its first pair/solo anomaly occurs when its own recurrence worldline reaches a pre-existing, preparation-conditioned difference in the region where the leader was formed.

**Test 1 — worldline-intercept prediction.** On fresh native vacua, both signs, at the exact scored-start state p000 and before any new outcome is observed:
- Take the receiver's prospective path for at least 12 events **from the solo reference trajectory** (already known and period-2), so the prediction does not require executing the pair receiver and cannot coincide with the clamp by construction.
- At each prospective event, evaluate on the *pair* p000 graph and the *solo* p000 graph the receiver's exact native $v_1$ outside-source predicate: eligible source relations, any gate whose firing would consume a future source, pair/solo availability, and provenance. The causal criterion is this predicate, not a graph radius; a radius may be recorded as a secondary measurement.
- Freeze a predicted triple $(k_{\rm geom}, x_{\rm geom}, T_{\rm geom})$: the first event at which the predicate differs, the receiver position there, and the signed mechanism ($T=+1$ if the pair has an eligible preparation/partner-derived source the solo lacks; $T=-1$ if the solo has a required future source that the pair lacks because of a preparation-descended consuming chain).
- Solo negative prediction: the identical map on the solo gives $T_{\rm geom}=0$ throughout the window.

**Test 2 — receiver clamp (scheduler bypass).** Freeze all ordinary vacuum events and the leader; advance only the receiver by its unchanged native predictive recurrence with its own constituent RNG; no draw from the global gate set, no relation insertion or repair; stop honestly on loss of predictive recurrence, ambiguity or health failure. Two cuts:
- **Primary:** from exact p000, where the historical $k=3/5/6$ values are defined. Pass requires $k_{\rm clamp}=k_{\rm geom}$, $x_{\rm clamp}=x_{\rm geom}$ and $T_{\rm clamp}=T_{\rm geom}$ with zero tolerance.
- **Secondary:** from immediately after insertion, warm rounds and pulse, before autonomous qualification, to learn whether the same encounter develops without the qualification scheduler. Reported separately; not merged with the primary.

**Native reference branch.** Ordinary scheduling continues, so corridor structures may change before arrival. Pass criterion is mechanistic rather than a numerical tolerance: the actual onset witness must descend from, occupy or consume the preregistered corridor-role structure. Specificity control: the same criterion applied to equivalent structures chosen off the corridor must not qualify.

**Interpretation boundaries.** A pass would make the D37 effect local within the CRR dynamics in a specific sense (the receiver advances into a prepared environmental feature; nothing propagates to it), analogous to Y132. It would not establish particle-particle interaction, because the feature originates in the insertion procedure. A failure (onset absent, shifted in $k$ or sign, or clamp recurrence lost before onset) would indicate that ambient scheduling or intervening events are mechanistically required, and the D37 interaction would not be used for any conservation ledger.

**Planned sequence.** D3-7O (worldline encounter and scheduler bypass) → **D3-7P** (dose-response: formation displacement $d\in\{40,44,48\}$, each with its own frozen corridor map and predicted $k(d)$, testing $k_{\rm observed}(d)=k_{\rm predicted}(d)$) → **D3-7Q** (preparation-method invariance: whether the remnant's effect survives materially different legitimate formation procedures). Only if the remnant survives D3-7Q should the energy/conservation program be reconsidered. Firewall unchanged: no grammar or scheduler modification; $E_0$, $M_i$, $\alpha$ sealed.

### 10.1vvvvvv A static map of the receiver's source slot, frozen at the scored start, prospectively predicts the onset step, position and mechanism exactly; the receiver walks into a pre-existing preparation-conditioned difference with nothing propagating to it (Stage Y165, D3-7O)

**Geometry reminder.** From D3-7J onward the design is *not* head-on. Both carriers move in the same direction. The leader is formed, then runs 96 autonomous carrier events (about 250 position units away). The receiver is then introduced behind the leader's original formation site, facing the same way, and moves toward that site under its own recurrence.

**Design (frozen per 10.1uuuuuu).** Four unused native vacua (83018211/213/217/219), both signs; pair and matched solo saved at EARLY (after insertion, warm rounds and pulse) and P000 (scored start after 17-event qualification). The receiver-readable footprint is the exact $v_1$ outside-source predicate: a live relation (outside_source, $c_0$, $c_1$) onto the receiver's two old-spine core vertices. The P000 map projected the next 12 receiver old-spine targets **from the solo period-2 trajectory** and read pair and solo graphs at those targets; the first difference counted only with a prospectively identified mechanism (direct/additive $T=+1$ or constraint/subtractive $T=-1$). The mapper was validated on exposed D37K seeds before the holdout, then SHA-frozen.

**Prospective predictions (8/8 qualified).** Positive: $k=6$, $x=1295.5$, $T=-1$ in 4/4 (inside leader formation support 1294–1298); in each, the solo contains a future source relation that the pair lineage shows consumed by an ordinary vacuum fire with earliest-preparation input. Negative: $T=+1$ in 4/4, at $k=3$, $x=1255.0$ in three vacua (one unit beyond support 1250–1254) and $k=5$, $x=1252.0$ in one (inside it), the seed-specific split predicted in advance. Solo corridors matched the period-2 role sequence in all cases.

**Primary P000 receiver clamp** (no global draw, no vacuum fire, no leader event; receiver native recurrence only): $k$, $x$, $A$ and $A_{\rm sector}$ all equal the frozen prediction **8/8**, with zero scheduler, vacuum or leader events before onset.

**Native reference** (unchanged scheduler, 192 events, 3,072 events total): sign 8/8, and exact $k$ and $x$ **8/8**, stronger than the one-event tolerance allowed.

**Secondary EARLY clamp:** no pair/solo anomaly in 8/8. The report interprets this as evidence that the qualification history helps establish the P000 corridor. **Caveat (post-verdict, from raw trajectories):** over its 12-event horizon the early-clamp receiver travels only 1262.5→1279.0 (positive) or 1283.5→1267.0 (negative), stopping about 15 units short of the encounter region (1294–1298, or 1250–1255). The early null is therefore uninformative about whether the difference exists immediately after insertion; the receiver never reached it. D3-7N's finding that qualification under three different random streams leaves onset unchanged weakly favors the difference being present at insertion. Recommended corrective: freeze a static map at the EARLY cut with the same predicate, then extend the early clamp (about 30+ events) through the formation region.

**Verdict:** `PREEXISTING_RECEIVER_READABLE_WORLDLINE_ENCOUNTER_SUPPORTED`. At the scored start the graph already contains a path-local difference in the receiver's source slot that determines where, when and by which signed mechanism the receiver first distinguishes pair from solo; the receiver reaches it by its own recurrence, and nothing from the remote leader propagates to it (the Y132 logic). Still preparation-conditioned; not a particle-particle interaction; energy/conservation closed.

**Next (D3-7P, in progress):** formation displacement $d\in\{40,44,48\}$ with independently mapped $(k,x,T)_{\rm pred}(d)$ and a law gate requiring distinct predicted encounters in the expected direction. Every clamp must run long enough to pass its predicted encounter point with margin, since larger $d$ moves the encounter farther along the path; otherwise a late onset could appear as a spurious null.

### 10.1wwwwww Every qualified formation-displacement prediction is exact, but the strict two-sign dose-response law does not close; the encounter tracks the leader's formation site, and the governing mechanism can flip with displacement (Stage Y165, D3-7P)

**Design.** Four unused native vacua (83018221/223/227/229), both signs, formation displacement $d\in\{40,44,48\}$ (24 comparisons), otherwise the D3-7O construction. Static P000 map over 16 projected receiver events of the exact $v_1$ outside-source slot; the *first* pair/solo occupancy difference counted only with a prospectively identified mechanism under the D3-7O provenance rule, with no substitution of later differences. Frozen law: within each seed/sign triplet, $k_{\rm pred}(40)\le k_{\rm pred}(44)\le k_{\rm pred}(48)$ with at least one strict inequality.

**Map qualification: 19/24.**
- Positive, 12/12: $d=40$: $k=5$, $x=1294.0$, $T=+1$; $d=44$: $k=6$, $x=1295.5$, $T=-1$; $d=48$: $k=9$, $x=1300.0$, $T=+1$, identical in all four vacua.
- Negative, 7/12: $d=40$: $k=1$, $x=1254.0$, $T=+1$ in 3/4; seed 83018227 has no occupancy difference through 16 events. $d=44$: $T=+1$ at $k=5$ (3/4) or $k=3$ (1/4). $d=48$: 0/4 qualify; the first raw difference is a subtractive deficit at $k=8$, $x=1251.5$, but no pair-world consumer meets the preregistered provenance rule.

**Primary clamp and native reference, 19/19 qualified.** Clamp $k$, $x$, $A$, $A_{\rm sector}$ all exact 19/19; native sign, exact $k$ and exact $x$ 19/19 (7,296 native events; 608 clamp receiver events).

**Frozen verdict:** `FORMATION_DISPLACEMENT_GEOMETRY_LAW_NOT_CLOSED` — 19/24 qualified maps; complete monotonic triplets 4/8 (all positive, no negative). No qualified prediction failed after it was made. Post-verdict, non-gating: the five unqualified cases also behave exactly as their raw occupancy map says ($d=48$ negative onset at $k=8$, $x=1251.5$, $A=-1$ in clamp and native; seed 83018227 $d=40$ negative shows no anomaly), making the raw map descriptively exact in 24/24 exposed comparisons, but not a prospective success.

**Observations and recommendations (recorded before D3-7Q).**

1. *The law is better expressed as position relative to the formation site.* For positive motion (receiver inserted at 1250, formation support at $1250+d$ to $1254+d$), encounters occur at offsets $+4.0$, $+1.5$, $+2.0$ from the start of the support for $d=40$, 44, 48: inside or at the edge of the leader's birthplace in every case. Negative encounters are likewise at or immediately beside the support (e.g. $d=48$: 1251.5 beside 1246–1250). The step increase follows from the site moving farther away. D3-7Q should state its law as encounter position relative to formation support, which does not depend on where the scored window starts.
2. *Small $d$ has a window problem.* At $d=40$ negative the onset is at $k=1$, and one vacuum shows no difference at all, most plausibly because the receiver reaches the formation site during qualification, before scoring, so the difference is encountered and used before the map looks. This mirrors the D3-7O early-clamp horizon problem in the opposite direction. Map and clamp from the EARLY cut as well, with horizons long enough to pass through the site.
3. *Occupancy-map clamp agreement is close to a consistency check.* In a clamp only the receiver moves, and its sector is defined by that slot's occupancy, so exact clamp agreement largely confirms the map reads the slot the classifier reads. The informative evidence is native-run agreement (background evolving) and causal origin (Family B).
4. *The mechanism flip with $d$ needs explanation.* Positive motion is additive at $d=40$ and 48 but subtractive at 44. One candidate is arrival phase: the period-2 orbit advances 3 units per two events, so which alternating state the receiver is in on arrival depends on distance. A finer sweep ($d=40,41,\ldots,48$) would distinguish arrival-phase dependence from internal structure of the formation region.
5. *Follow origin classification with intervention.* Once each difference's origin class is identified (formation descendant, qualification history, scheduler divergence, mixed), delete that origin and confirm the response disappears or shifts, following the Y131 surgical logic. The long EARLY clamp from 10.1vvvvvv remains recommended.

**Proposed next stage (D3-7Q, per the other assistant, with the above).** Family A: prospective provenance-independent occupancy law, including explicit NO_DIFFERENCE predictions. Family B: full-DAG causal-origin decomposition, reported separately from timing. Energy/conservation closed.

### 10.1xxxxxx The formation-site occupancy law closes exactly on a full displacement sweep; the remnant predates qualification, the mechanism follows a three-unit arrival-phase periodicity, and normalizing the source slot removes the response (Stage Y165, D3-7Q)

Four fresh vacua (83018231/233/237/239), every integer $d=40$–48, both signs: 72 comparisons. The receiver's exact $v_1$ outside-source slot was mapped prospectively at EARLY (post warm/pulse, pre-qualification) and P000 (scored start); the frozen band for signed formation penetration was $-1\le\delta_{\rm form}\le4$.

**Family A — formation-site occupancy law: PASS.** All 72/72 qualified, every prediction inside the frozen band. **Native runs matched the P000 map exactly in 72/72** ($k$, $x$, $A$, $A_{\rm sector}$), with background and remote leader active; the receiver-only clamp also matched 72/72 (secondary).

**Three-unit arrival-phase periodicity.** Positive: $d\equiv40,43,46$ → $\delta_{\rm form}=4.0$, additive; $d\equiv41,44,47$ → 1.5, subtractive; $d\equiv42,45,48$ → 2.0, additive. Negative: $d\equiv40,43,46$ → 0.0, additive; $d\equiv41,44,47$ → 2.0, additive; $d\equiv42,45,48$ → 2.5, subtractive. Identical in all four vacua. The period matches the period-2 orbit's 3-unit advance per two events, confirming the arrival-phase hypothesis of 10.1wwwwww.

**EARLY: the remnant predates qualification.** EARLY map 72/72, long EARLY clamp exact 72/72, same absolute target position and sign as P000, with $k_{\rm EARLY}=k_{\rm P000}+17$ in every case. The D3-7O early null was a horizon artifact (its 12-event run ended before the earliest encounter at $k=18$).

**Family B — causal origin.** `LEADER_FORMATION_DESCENDANT` in 72/72 (direct leader-preparation relations or vacuum relations whose ancestry reaches the leader's formation history).

**Family C — source-slot normalization.** At $d=40,44,48$ (24 targets): deleting the pair-only source (additive) or restoring the missing solo source (subtractive) removes the anomaly entirely in 24/24 clamp and 24/24 native runs (192 global events).

**Verdict:** `FORMATION_SITE_OCCUPANCY_LAW_PASS`. Leader formation leaves a localized, phase-structured source-slot pattern, already present before qualification, which the receiver encounters by its own recurrence.

### 10.1yyyyyy Two legitimate preparation methods yield an identical mature leader but a different remnant in close negative geometries; the D37 effect is classified as preparation-procedure-dependent formation memory and retired from the mass-energy path (Stage Y165, D3-7R)

Four fresh vacua (83018241/243/247/249), $d=40,41,42$, both signs: 24 comparisons. Method P = the protected-sham head used in D3-7J–Q; Method O = the original remote-sham head (corrected before outcomes after noting P was already the protected sham).

**Matched mature leader.** P and O produce an identical leader before aging in 24/24: core, marker, recurrence magnitude, position, constituent RNG state and complete incident relation star.

**Family C — preparation-method invariance: FAILS as a universal law.** Each method's own P000 map predicts its own native outcome 24/24, including nulls. The inherited D3-7Q law is reproduced in 19/24 (P), 19/24 (O), 17/24 for both. P and O agree in 20/24 and differ in 4/24, all on close negative geometries ($d=40,-$ and $d=41,-$, including $k=1\leftrightarrow3$ swaps). All positive-motion classes and $d=42,-$ are invariant 4/4. Three further fresh $d=40,-$ cases are null under both methods, a direct holdout failure of the D3-7Q law at the smallest negative displacement.

**Family A — root localization (Method P).** A persistent pre-receiver root is found in 21/24: at insertion (6), first head update (8), or aging events 1–8 (7); 3 have no persistent root and are later null. Pattern is phase-structured (e.g. $d=42,+$: insertion 4/4; $d=40,+$ and $d=42,-$: first head update 4/4).

**Family B — upstream root surgery.** Viable in 15/24 (6 prevent later leader recurrence; 3 have no root). All 15/15 viable surgeries alter the later native response (13 abolish it, 2 shift it). The preregistered strict matched control was structurally available in only 1/24 (response preserved); no looser control was introduced, so the controlled upstream-causality gate is **not** closed.

**Verdict:** `FORMATION_ROOT_AND_PREPARATION_INVARIANCE_NOT_CLOSED`; classification **`PREPARATION_PROCEDURE_DEPENDENT_FORMATION_MEMORY`**. The local occupancy-response law is robust, but the remnant supplying it depends on preparation history even with the mature leader exactly matched, so it is not a property of the particle and not a generic particle-particle exchange field. D37 is retired from the mass-energy/conservation path unless a genuinely independent natural formation route becomes available. Audit PASS; 24,576 native scored events; one pre-outcome wrapper crash corrected source-only.

### 10.1zzzzzz The minimal existing-grammar rest coupler, one extra legal rival gate, destroys the unique next rest update in every eligible phase; $E_0$ and independent $M_i$ remain undefined in CRR as specified (Stage Y165, C3)

**Context.** After D3-7R, the original-law Y165-C path was found already completed through C1/C2/C2b2/D0/D1/D2: exact stationary-rest recurrence for DS001, D2R5 and D2R6 and a reproducible producer-owned lifetime activity proxy, but no independently safe rest-local environmental coupler (`OPERATIONALLY BLOCKED_BY_LOCAL_COUPLER_ELIGIBILITY`). C3 is the one separately frozen model-extension gate permitted by Y165-D3: Y33 grammar and Y148 rest engine byte-identical, plus permission for one externally triggered, already-legal local Y33 rival to the native rest gate to fire once, followed immediately by native dynamics.

**Design.** DS001 only; unused development vacuum 83006201; P-positive at center 1500; all eight event phases (h0, e0, e1, e2, h1, e4, e5, e6) in the denominator; viability required a legal scoped intervention, health, execution of the scheduled native event, closure to `start` with zero displacement, a second untouched full rest cycle, and color-preserving CQ1 isomorphism across cycles. No repair or substitution.

**Result.** 6/8 phases had exactly one rival; 2/8 (e5, e6) none; **0/8 viable**. In all six interventions the rival shares 4 of 5 vertices with the native gate, removes 3 live relations and creates 7 (8 at h0), leaves the selected native gate not live (6/6), and the native rest solver reports `REST_ROLE_COUNT_0` (6/6). The untouched control completes two full ten-phase rest cycles with zero displacement, excluding a bad preparation.

**Interpretation.** The rival is not an independent work channel; it competes for the same local support as the unique next rest update. This is the same fresh-source four-core rival family identified in D3-4A (selected in 9/9 carrier deaths), so the outcome was predictable from prior results. Verdict `NO_HEALTHY_RIVAL_GATE_COUPLER`; $E_0$ = UNDEFINED, independent $M_i$ = UNDEFINED, $\alpha$ not testable; R5/R6 and inertia trials not opened. This does not show rest energy is zero or that no coupling extension can exist.

**Next (Y165-C4, coupling-architecture design gate), with recommended modifications.** The proposed seven structural requirements (locality and future-blindness; an action channel not consuming the unique native gate; an explicit, independently measurable environment-side state; a coefficient-free balanced signed ledger with reversibility or closure; zero- and distant-action controls; no direct speed/phase command; exact recurrence health before and after) are supplemented by:
1. *Score existing channels first.* The sector relation (Y159–Y163) already meets most requirements but acts on moving carriers and lacks a balanced ledger. The stationary rest reservoir (Y133; $U_{\rm rest}=11n_{R5}+7n_{R6}$) is an environment-side state present at rest, outside the next gate's footprint, and already topology-sensitive, making it the most natural rest-compatible candidate.
2. *Stop condition and separate reporting.* Preregister what result establishes that no rest-compatible coupling exists within CRR as specified; report any added coupling as a property of an extended model, never folded into CRR's own results.
3. *Circularity and Section 10A guards.* Freeze any coupling before any $E_0$ measurement and test it against more than one candidate observable; derive the rest constraint from the C3 forensic (coupling must act outside the unique next gate's footprint); add covariance under relabeling, independence from the global scheduler, and independence from preparation method to the requirements.

### 10.2 A dispersion relation, and a definition of inertial mass

The decisive test requires the same defect to exist at different mean
translation speeds, $\Phi_v$ — which itself requires an operational
definition of discrete velocity (candidate: net support displacement per
rewrite event) not yet fixed. Given that, and a rule-derived dynamical
cost $E(v)$, two levels of result would be meaningful, in increasing order
of strength:

$$
E(v) = E_0 + \tfrac{1}{2} m_i v^2 + O(v^4)
\qquad\Longrightarrow\qquad
m_i = \left.\frac{\partial^2 E}{\partial v^2}\right|_{v=0}
$$

$$
E(v)^2 = E_0^2 + c_*^2 p^2
\qquad\Longrightarrow\qquad
m_i = \frac{E_0}{c_*^2}
$$

The second, relativistic-shaped form is the stronger and more interesting
target, not merely for the massive case: its $E_0 = 0$ special case is
$E = c_*|p|$, a genuine massless dispersion relation directly testable on
the triangle (Section 3.2) without waiting for any open problem in
Sections 8–9 to be resolved first.

**Why the target is $v=0,\ \pm v_1,\ \pm v_2$, and not just "find
something that moves."** Mass is a curvature, not a value — the
coefficient of the quadratic term in $E(v)$ near $v=0$ — and a
curvature is structurally different from a position or a speed: a
slope needs two points, but a curvature needs several, spread out, not
all collinear, or the number extracted is an artifact of which two
points happened to be available rather than a real property of the
curve.

![Why rest plus two speeds, not one](figures/fig21_velocity_manifold.png)

*Figure 8d. Left: a single nonzero speed plus rest gives only a slope —
infinitely many different curves pass through two points equally well,
so no curvature, and no mass, is defined. Right: the full target
manifold makes the curvature at rest checkable rather than assumed.*

Each piece of the manifold does a distinct, necessary job. **Rest**
($v=0$) is the anchor where the already-derived rest energy $E_0$
(Section 10.1e) actually lives — without a genuine rest state built
from the *same* carrier architecture as the moving states, a mass
measurement would be comparing two unrelated constructions, not one
construction at two conditions. **One signed pair** ($\pm v_1$) checks
parity: if $+v_1$ and $-v_1$ required different mechanisms or unequal
speeds — exactly what Stage X21/Y21 first found before Y22 corrected
it — that is evidence of built-in directional bias, and a "mass"
computed from only one direction would not be the direction-independent
scalar mass is supposed to be. **A second speed** ($\pm v_2$) is what
converts the curve from an assumption into something checkable: if all
five points genuinely lie on one smooth curve, that is real evidence of
a well-defined $m_i$; if $v_2$ does not fit the parabola implied by
$v_1$, that is equally informative — evidence that whatever happens at
$v_1$ is a fact about that one speed, not a generic inertial response.
This is why Stage Y23 (Section 10.1t) is tasked with finding $v_2$
within the *same* marked carrier family rather than any second,
unrelated construction: an unrelated construction could not test the
same curve at all. G4 (dynamical cost) and G5 (curvature, the actual
mass computation) are withheld until all five points — $0,\pm
v_1,\pm v_2$ — exist together, not because of excess caution, but
because a curvature measurement is structurally meaningless without
them.

**A note on what "position" and "velocity" can even mean here.** This
substrate has no coordinates and no absolute space; a vertex's location
only ever means its graph-distance to some other vertex. Every position
and velocity measurement in Sections 10.2a–10.2h is therefore built the
same way real relational physics has to build it: by selecting other,
independently-verified-stationary vacuum vertices as reference anchors,
and measuring the object of interest's distance to those anchors, never
to any absolute frame. "Stationary" is not assumed — Stage X2B verified
it directly, by cloning an evolving vacuum into two forks and confirming
the anchors' own mutual distances stayed fixed under identical exterior
stress before trusting them as a ruler. Stage X4's directionality test
sharpens this into an explicit two-anchor construction: choose $L,R$ with
$d(L,R)$ verified constant, and decompose the tracked object's position
into a longitudinal coordinate $x$ (its position along the $L$–$R$ line)
and an orthogonal remainder $h$ (whatever part of its distance-change to
the anchors is not explained by motion along that line).

![Measuring motion without absolute space](figures/fig17_reference_frame.png)

*Figure 13. Left: genuine translation along a fixed reference axis would
show $\Delta x \ne 0$, $\Delta h \approx 0$. Right: what was actually
measured, in every one of thousands of independently-chosen reference
configurations across Stages X4, X14, and X15 — $\Delta x = 0$ exactly,
with the growth appearing entirely in $h$.*

The trustworthiness of this result rests on using *many* independent
reference configurations rather than one — 23 in Stage X4, scaling to
2,145 and 4,005 in Stages X14–X15 — all agreeing. A result that depended
on which landmarks happened to be chosen would show disagreement between
configurations; this one does not. $h$ itself remains fully relational,
computed from the same anchor distances as $x$ — it is not a
free-floating or externally-assumed quantity, only the specific component
of motion that no fixed-anchor axis, however chosen, is ever found to
capture.

### 10.2a A coordinate-free position observable, and its correction (Stages X1–X5)

The velocity definition called for above has a first concrete attempt for
rule 55744, and a genuinely important self-correction. A naive graph-center
position (a Fréchet center of the particle's five-vertex support) fails
outright: the support forms a clique in the 2-section vacuum graph, so
every support vertex is equidistant and the "center" degenerates to the
whole support, giving zero displacement even on trajectories that later
separate macroscopically — a diagnosed and avoided false negative, not an
oversight. The adopted alternative treats the support as a set and
measures displacement via the intrinsic distance field
$\chi_S(q) = \min_{s\in S} d_t(q,s)$ and the induced Hausdorff distance
$H_t(S,T)$ between two supports evaluated in the same graph slice —
coordinate-free, relabeling-invariant, defined purely from the vacuum's
own graph metric.

**Stage X1** found that the two branch choices at $B$ in rule 55744's
three-state closed SCC ($A\to B$, $C\to B$, $B\to A$ or $B\to C$) produce
qualitatively different displacement histories from the *same* particle
identity, with minimum support separation obeying
$D_{\min}(S_0,S_n) = \lfloor N_A(n)/3 \rfloor$ exactly across 100
randomized trials, suggesting a coarse-grained family $v(f)=f/6$. This was
explicitly flagged at the time as provisional, pending two controls.

**Stage X2B** applied the first control — a paired-fork design cloning an
entire evolving vacuum into an A-branch and a C-branch history and
subjecting both to *identical* exterior stress events, so any common
background-metric drift cancels by construction rather than requiring
separate estimation. Background drift between the two forks was exactly
zero at every checkpoint across 5 trials; the A/C separation persisted
regardless. This ruled out background-metric drift as the source, but
X2B's own analysis correctly identified a further confound it could not
resolve: the A and C histories also differ in mean constituent age, so the
separation might reflect generational renewal rather than genuine
relational motion.

**Stage X3** resolved this. An attempt to construct an "ordinary,"
non-particle full-turnover producer tracer as a matched causal-age control
failed for an unexpected and independently interesting reason: all 186
observed ordinary legal producer supports across four evolved vacua were
absorbed into the A/B/C particle class within two steps — rule 55744's
particle is not merely *a* recurrent structure but a local **attractor**
for coherent producer flow. X3 pivoted to using independent particle
worldlines as mutual controls instead, and found that two worldlines both
taking the rest-like C branch maintain *exactly constant* mutual distance
despite both continuously advancing in causal depth — ruling out simple
causal-time advancement as the source. A clean, additive, exact law held
across 168 checkpoints: each independently evolving A-branch worldline
contributes $1/6$ graph edge per producer event to relative separation
from any C reference, and induced causal DAGs for A and C histories are
non-isomorphic in every tested case, ruling out the possibility that A and
C are merely different schedulings of the same underlying history.

**Stage X4 overturned the velocity interpretation itself.** The decisive
test placed the particle between two reference worldlines fixed relative
to each other ($d(L,R)$ constant) and asked whether it approached one
while receding from the other, the basic signature of translation.
Across 23 independent geometric configurations, the result was uniform and
exact: the particle receded from **both** references by the identical
amount, $d(L,R)$ never changed, and the particle's longitudinal coordinate
along the $L$–$R$ geodesic was **exactly unchanged** ($\Delta x = 0$ in
every case) while an orthogonal, off-frame coordinate grew
($\Delta h = 6$ per 36 events, exactly, with zero exceptions). This is not
translation through the existing reference frame — it is the particle
extruding into relational material the reference frame does not span.
Mixed random A/C histories confirmed the same scalar law,
$h(t) = \lfloor N_A(t)/3\rfloor$, with no directional information encoded
in branch ordering. **The $v=f/6$ family of Stage X1 should be read as a
branch-extrusion rate, not a spatial velocity**, and this document's
earlier framing overstated it accordingly.

**Stage X5** checked whether direction or momentum might instead live in
the particle's surrounding halo rather than its five-node core. It found
a real, persistent, amplifying scalar distinction — A-history halos
rapidly decouple from the old vacuum (falling to a floor of 1 external
touching gate and 24 external relations after 3 cycles) while C-history
halos remain embedded and continue accumulating incident material — but
confirmed this is not momentum: it does not bias the next free branch
choice (exactly 50/50 A versus C, for a structural reason — an exact B
core always presents one gate of each type under the uniform scheduler),
and across 168 anchor comparisons on real particle-preserving relocation
events, zero showed the toward-some/away-from-others signature genuine
spatial motion would require.

**Net assessment.** Rule 55744's core does not currently supply a
direction-bearing spatial velocity, and the measurement program of
Section 10.2 should not be run on it using the A/C branch fraction as
$v$. The halo's decoupling scalar is a real, controllable, persistent
quantity, but is better read as a candidate operational definition for
Section 10.1's still-undefined recurrence content $\mathcal{R}$ (or a
coupling/tether strength) than as momentum.

### 10.2b The screen confirms it, and locates the actual constraint (Stage X6)

X4's diagnosis was exhaustively generalized before searching for a new
architecture. Of Stage W's 80 closed rules, 72 have no internal branch
alternative at all; of the remaining 8, three fail basic environmental
viability, leaving five genuine alternatives to rule 55744. All five were
screened with X4's own methodology (comoving-particle references, an
accumulation-over-time test at 5 checkpoints), and all five produced the
same qualitative outcome: a bounded, O(1) longitudinal offset alongside a
scalar off-geodesic component that grows linearly. **No member of the
Stage W closed-particle family contains a demonstrated direction-bearing
velocity state.** This is architectural, not a property of the specific
rule chosen. The reason is exact and simple: every particle-internal event
in this family matches only its own current five-node support plus one
fresh vertex — there is no mechanism by which it can reach pre-existing
ambient material lying ahead of it, which is what ordinary translation
through existing space would require. The correct design target is
therefore not another closed five-node orbit, but recurrence that closes
**modulo a shift onto pre-existing ambient material** — the relational
analogue of a cellular-automaton glider.

### 10.2c Boundary-coupled translation: a real breakthrough, and a new exact wall (Stages X7–X9)

**Stage X7** found the first genuine direction-bearing translating
recurrence in the investigation. Rule 54567 admits a four-relation
boundary "rail" operator: given a suitable pre-existing neighboring
vertex, the particle recruits it, achieves full constituent turnover after
four shifts, and — critically — passes X4's own directionality test
exactly: across 30 shifts, a left-moving history and its mirror-image
right-moving history diverge to $(d_L,d_R)=(0,17)$ and $(17,0)$
respectively, with the rail endpoints themselves 18 edges apart. Direction
is stored not in the five-node core but in the relation between the core
and its next recruitable frontier — the first credible momentum-memory
mechanism found in this investigation. The honest limitation: this
translating frontier does not arise naturally. Across 8 independent
vacua and 21 relevant natural supports, 0 exact occurrences were found;
natural vacua typically supply only 2 of the 4 required frontier
relations, and priming the missing two requires its own 4-relation
ambient precursor, pushing the genesis problem outward rather than solving
it.

**Stage X8** explains why, with an exact result rather than another
search. The **no-unseen-frontier lemma**: because a rule event's output
relations are built only from its own matched vertices plus one freshly
created vertex, no event can ever write a relation touching a
pre-existing ambient vertex that did not participate in that event. A
single translation step therefore cannot prepare its own successor's
frontier. An exhaustive census found 635 full-turnover boundary
operators across all 80 closed rules; the cheapest (one relation) family
turned out to require the recruited vertex to be strictly older, in
creation order, than the current support — making repeated use a
**bounded ancestral descent**, not a sustainable translation, since
creation order cannot decrease indefinitely. The strongest naturally
recurring candidate (rule 52300) was directly audited by causal depth and
confirmed to be exactly this: a finite migration toward older, not
spatially fresh, material.

**Stage X9** tested the natural fix — let a single event also touch a
second, "lookahead" ambient vertex, preparing next step's frontier while
using this step's — and falsified it exhaustively: 0 of 80 rules admit
any event that recruits a current frontier vertex, incorporates the
fresh rewrite vertex, and leaves a nontrivial prepared frontier around
the lookahead vertex simultaneously. Relaxing the requirement that the
fresh vertex remain part of the recognized particle produces over three
million one-step transfers, but only 4 rules yield even one working
handoff, none yields a second, and every compatibility graph is
exactly acyclic — the prepared frontier is consumed faster than it is
regenerated, a capacity argument structurally identical in shape to
Section 5.1's relation-floor theorem and Section 8.1's ternary analogue,
now appearing for momentum transport rather than damage repair.

**A pattern worth naming explicitly.** This is the fifth independent
appearance, across two ostensibly different questions (repair capacity
and frontier/momentum capacity), of the same underlying obstruction: a
single local event cannot manufacture more capacity than it consumes —
Sections 5.1, 5.4, and 8.1's ternary law for repair; Sections 10.2c's
no-unseen-frontier lemma and capacity-decay result for translation. Given
how consistently this shape of result has recurred, attempting a fully
general theorem — that no locally-propagating quantity requiring more
input than a single match-and-create-one event supplies can be sustained
indefinitely in this rule family — is a reasonable higher priority than
further empirical search, since a positive proof would determine in
advance whether any extended-state architecture (below) can succeed at
all.

**Recommended next stage (X10).** Stop requiring a recognizable five-node
particle phase after every individual event. Search directly for an
extended state $\Psi = (\text{core} + \text{frontier})$ whose orbit closes
only after a multi-event period, $\Psi_t \to \cdots \to \Psi_{t+p} \cong
\text{Shift}(\Psi_t)$, with at least one never-before-used ambient recruit
per period, persistent directional inequivalence, full constituent
turnover, universal closure, no forced descent toward older material, and
eventual live-vacuum testing. This allows the frontier to be part of the
attractor itself, rather than an external accessory a single event must
regenerate from nothing.

### 10.2d A unifying theorem, arrived at by falsifying the naive version first (Stage X10)

The general capacity conjecture proposed at the end of Section 10.2c was
tested, in the right order: an attempt to falsify it preceded any attempt
to confirm it. **The literal single-scalar version is false.** Rule
55744's own clean transitions are a direct counterexample — relation count
increases on one legal transition, legal gate count increases on another,
and an exact four-inequality argument over its four legal transitions
shows no nontrivial linear combination of the two is non-increasing
throughout the particle SCC; the only such combination is trivially zero.

What survives is narrower, proven, and more useful than the original
conjecture.

**Theorem (old-handle non-creation).** If every newly created relation in
a rewrite event has support contained in the matched vertices $M$ plus the
freshly created vertices $W$, then no relation created by that event can
be incident to any pre-existing vertex $q \notin M$. The proof is
immediate from output-support locality. This single theorem has two
previously separate results as direct corollaries: Section 5.4's
zero-incidence absorption (an old vertex with no incident relation can
never regain one, since it can never be matched again) and Section 10.2c's
no-unseen-frontier lemma (a frontier vertex not participating in the
current event can never receive a prepared relation). The distinction that
rescues the intuition from the Rule 55744 counterexample is between
**syntactic multiplication**, which is unrestricted (a matched vertex's
role can be duplicated into arbitrarily many output relations, which is
exactly what let relation and gate counts both rise), and **independent
old-world access**, which cannot be created without matching it.

**A general no-cycle proof schema, not a single conserved quantity.** If
some process-specific quantity $K$, invariant under the relabeling (and,
where relevant, shift) equivalence defining recurrence, is non-increasing
under every legal event in a proposed recurrent basin, and strictly
decreases at least once per proposed period, no recurrent orbit can close.
This is a reusable proof technique — Section 5.1's relation floor, Section
8.1's ternary analogue, Section 5.4's absorption indicator, and Section
10.2c's acyclic handoff graphs are all instances of it, but each required
its own problem-specific monotone to be identified; the schema does not
supply one automatically.

**Capacity is typed, not scalar — cross-validated across two independent
domains.** Reclassifying Stage U's repair data and Stage X9's frontier
data by the same four-level hierarchy — access, amount, role, closure —
gives closely matching shapes despite the two datasets never having been
designed for comparison: repair's 58 deficit / 28 adequate / 6 surplus
branches (0/0/2 succeeding) and translation's 38 deficit / 31 equal / 11
surplus rules (0/0/4 reaching even one handoff, and 0 of those closing
into a cycle). Passing each lower level is necessary but not sufficient
for the next; failing any one level is fatal regardless of the others.
This gives a concrete, general pruning rule for any future extended-state
search: track all four components at every intermediate state of a
candidate orbit, and reject immediately, without further simulation, any
candidate that strictly loses a genuinely monotone component without an
identified regeneration mechanism before the cycle closes.

**A speculative but promising link back to inertia.** If a translating
extended state must expend typed capacity to maintain and redirect its
frontier, and that capacity must be regenerated from the surrounding
substrate over each period, the rewrite burden of keeping that regeneration
balanced is a genuine candidate mechanism for Section 10.1's still-
undefined recurrence content $\mathcal{R}$ — arising from the structure
of the theory itself rather than being posited from outside. This is
explicitly not yet a result: Section 10.1's operational definition of
$\mathcal{R}$ remains open, and this is a lead toward one, not the
definition itself. A useful independent check, not yet performed: whether
Section 8's PRO criterion (access to context; frontier bridge; downstream
role; next-producer legality) is itself an instance of the same
access/amount/role/closure hierarchy — the four conditions map
suggestively onto the four levels, which would mean this framework
unifies the repair program (Sections 4–8) and the translation program
(Section 10.2) into a single structural account rather than two parallel
ones.

### 10.2e The extended-state search: real recurrence, the same wall relocated (Stage X11)

The multi-event relaxation X9 called for was implemented, with Section
10.2d's capacity hierarchy used as an active pruning rule rather than a
retrospective explanation. The result is genuinely mixed, and both halves
matter.

**Dropping the five-node-per-event requirement is a real fix, not a
reformulation.** A compact search across the ten environmentally viable
Stage W rules found 777 formal six-node extended cycles, 371 of them
non-ancestral with eventual full constituent turnover, with every one of
the ten rules producing at least one. This confirms Stage X9's
zero-result was partly an artifact of insisting on a recognizable
five-node phase at every intermediate step, not a fact about the
substrate itself.

**The capacity theory immediately caught a false positive, mechanically.**
The most promising initial cycles required only one ambient relation —
until inspection showed their sixth vertex was completely isolated, an
artifact violating Section 10.2d's access principle rather than a genuine
six-node dynamical object. Enforcing positive incidence and connectedness
on every state vertex left 127 valid cycles, and **the minimum ambient
interface rose to two relations in every single rule** once the artifact
was removed. This is a concrete demonstration that the capacity framework
functions as an active search-pruning tool, not merely an after-the-fact
narrative.

**Two concrete successes, of different kinds.** Rule 59436 yields an
exceptionally clean conditional translating cycle: exact for 40/40 forced
shifts, full turnover after three shifts, exactly one legal gate when its
two-relation frontier is present and zero when absent. Rule 59436 is also
notable for a reason independent of X11: its Stage W local dimension
estimate (~2.86) sits much closer to 3 than rule 55744's (~4.6, Section
7.3) — the cleanest glider candidate and the best-behaved emergent
geometry found so far now coincide in the same rule, which should weight
it as the lead candidate going forward.

![Rule 59436's exact state and required frontier](figures/fig19_rule_59436.png)

*Figure 8b. The exact six-node recurrent state for rule 59436 (solid
navy relations), and the two-relation frontier around vertex $q$ it must
recruit to advance (dashed orange) — exact values from Stage X11's
report. The rewrite step that consumes this frontier was not given
explicitly in the source material, so only the state and its
requirement are shown; the closure claim itself (the state returns to
this same shape, shifted, after the gate fires) was verified
computationally at 40/40 forced shifts.*

Separately, rule 55744 was shown
to support a genuine four-event extended recurrence (also 40/40 exact) —
proof that recurrence of a whole multi-event orbit, with no recognizable
particle phase at several intermediate steps, is a real mechanism in this
substrate, even though this specific orbit does not yet meet the
universal-closure bar (some first-step alternatives fail to return within
the tested depth).

**The wall relocated, precisely.** An exhaustive single-event priming
test — can one ordinary event regenerate the entire missing two-relation
interface while leaving the six-node recurrent state unchanged — returned
0 of 10 rules, confirmed individually for each. Combined with a 12,000-
event natural-occurrence search finding 0 exact instances of rule 59436's
translating start motif, the hierarchy from Section 10.2d gains a fifth,
more precise level: access $\to$ amount $\to$ role compatibility $\to$
**state recurrence** $\to$ **interface regeneration**. X11 clears state
recurrence, which X9 could not represent at all. It does not clear
interface regeneration: frontier access is consumed by translation but
not regenerated by the recurrent object itself, the same shape of
obstruction as every prior capacity result, now located one level further
out.

**Recommended redirection.** Rather than continuing to test whether a
specific candidate orbit's specific requirement happens to be supplied by
the vacuum — the approach behind every genesis test run so far (Stage X7:
0/21; Stage X8's broad sweep; this stage: 0/12,000), always with the same
null result — invert the search. Census the small local motifs a real
evolved vacuum generates most frequently, independent of any particular
orbit's needs, and ask whether an extended recurrent state can be
constructed to consume one of the genuinely abundant motifs as its
interface, rather than requiring the vacuum to supply a bespoke one on
demand.

### 10.2f The inverted search finds real genesis, and relocates the wall to renewal (Stage X12)

The supply-side inversion proposed in Section 10.2e was implemented, with
a further discipline: motifs were censused independently of any candidate
state's demand, and only intersected with search targets afterward.

**Raw interface abundance was never the bottleneck.** For eight of the ten
environmentally viable rules, the two-relation interface types Stage X11
needed occur naturally and often — up to 1,582 times per 900 vacuum
events for rule 76073. This substantially revises how the prior null
genesis results (Stage X7: 0/21; the broad sweep of Stage X8; Stage X11:
0/12,000) should be read: they were not evidence that the vacuum fails to
supply raw material, since it typically does.

**But raw abundance, correct alignment, and a usable recurrent state
around that alignment are three separate quantities, previously
conflated.** For rule 76073's best candidate, the correctly role- and
causal-order-aligned gate class occurred 21 times against 962 occurrences
of the raw relation-pair motif alone — most instances of "the ingredient
exists" are not instances of "the ingredient is usable."

**Restarting from the vacuum's own most common gates (not X11's
templates) found genuine, reproducible natural triggering of extended
recurrence** — 102 and 111 exact one-period recurrent hits across two
independent seeds for rule 76073, 63 and 18 for rule 58846, each spanning
dozens of distinct natural gates, states, and mechanisms. This is a real
resolution of the genesis problem that has recurred, unresolved, since
Section 7.2's original C4-T3 result.

**A self-caught false positive is worth recording as a methodological
result in its own right.** An apparent 20-period translating chain for
rule 76073 was traced to an incomplete worldtube history — fresh
intermediate vertices created and later dropped from the six-node state
were being recaptured and mistaken for genuinely new ambient recruits, the
same failure mode diagnosed externally in Stage X7, this time caught
internally through the team's own standing audit discipline. Under the
corrected worldtube rule (every vertex ever part of the state, touched, or
created during a period counts as "seen," whether or not it survives to
the period boundary), the chain vanished completely.

**The renewal test relocates the wall precisely.** Replaying each natural
recurrence for one exact period and then testing whether *any* legal
new-vertex boundary contact could supply a second, independent handoff
gave a clean negative: 4 of 102 and 0 of 111 candidates for rule 76073, 6
of 63 and 0 of 18 for rule 58846 admitted any second contact at all, and
**every one of those, without exception, required a recruit of creation-
rank 0** — the same finite ancestral-descent mechanism first diagnosed in
Stage X8. Zero non-ancestral second handoffs were found in 194 tested
cases.

**This is a theoretical consequence of Section 10.2d, not a new empirical
accident.** Once a translating period renews its own constituent material,
that fresh material is, by construction, too young to have any
pre-existing relation to old, untouched ambient vertices — so passive
vacuum supply can trigger a first period but cannot, even in principle,
sustain renewal on its own. Interface regeneration for a genuinely
translating (constituent-renewing) object must be an ongoing
particle–vacuum contact process, not a one-time inheritance. This is
structurally analogous to how a moving particle's physical mass in
ordinary QFT is sustained by continuous coupling to the surrounding field
rather than by any static pre-existing property — a resemblance that
emerged from the theorem, rather than being assumed going in.

**Recommended next stage (X13 — Live Contact-Coupled Frontier
Regeneration).** Search for a combined basin in which an ordinary live
vacuum event may perturb the recurrent state itself while supplying a
genuinely new ambient vertex, with subsequent legal dynamics required only
to return the whole system to the translating basin with a refreshed,
non-ancestral frontier — universal closure over the basin, not exact
invariance of a single state after a single priming event. This
deliberately extends Section 8.2's basin-of-attraction correction (dynamic
role transport, not static occupancy) to the translation program.

### 10.2g The vacuum joins the mechanism: live contact-sustained recurrence (Stage X13)

The basin-test relaxation succeeded on its own terms. A single collision
followed by internal recovery was insufficient (0 of 43 and 0 of 69
qualifying weak contacts for rules 76073 and 58846 returned to the
recurrent class), because many post-contact states admit no legal
internal producer gate at all — recovery, if it happens, must itself
involve further vacuum interaction. Allowing two contacts per period
found 16 distinct return paths on one representative rule 58846 state and
4 more on a second, and a concrete worldline was followed through **six
consecutive exact contact-mediated periods**, retaining only one of six
prior constituents at points, with a genuinely new non-ancestral handle
acquired in every period (avoiding Section 10.2c's rank-0 descent). At
every one of the six period boundaries, the state had **zero legal
internal gates** and 17–41 legal vacuum-touching gates — this recurrence
is intrinsically interaction-sustained, not an isolated core that merely
tolerates occasional contact.

**Applying Section 10.2b's own directionality test to this new mechanism
gives a precise, honest diagnosis.** Across 741 stable opposite-side
geodesic reference pairs, 0 showed persistent same-sign longitudinal
drift and 669 showed at least one reversal; independent anchor-cloud
analysis found a mean later-period displacement correlation of $-0.76$ —
a diffusive, repeated-scattering signature, not translation. Replication
was positive but not yet generic (16 and 4 return paths on one seed;
0 on an independently tested state from a second seed), and universal
closure over the full 17–41-action legal grammar at each boundary remains
untested. The defensible summary: **field/contact-mediated recurrent
identity exists; persistent momentum does not, yet.**

### 10.2h Separating identity, interaction current, and momentum (Stages X14–X15)

Two follow-on stages tested whether the reversals found in Section 10.2g
concealed a real directional signal, using increasingly strict controls
against increasingly specific false-positive mechanisms — each one caught
before it could be over-interpreted.

**A genuine separation between position and interaction current.**
Defining a contact-current vector $J$ (how a newly acquired handle's
distance profile differs from the current support's) distinct from the
period displacement $V$, the X13 chain showed $J$ mildly persistent
($\langle\cos(J_t,J_{t-1})\rangle \approx 0.27$) while $V$ strongly
backtracks ($\approx -0.55$) — confirmed a genuine temporal feature, not
an ordering artifact, by an exact permutation test ($p\approx0.017$,
one-sided, out of 120 orderings).

**A promising signal, correctly downgraded by its own control.** A
"dressing vector" $M$ (the mean direction over all legal contact channels
at a boundary) showed strong apparent persistence ($\approx0.73$) — until
tested against 20 unrelated natural recurrent states from the same
vacuum as a null distribution, which matched or exceeded that coherence
about a third of the time. The raw persistence is not statistically
distinct from ordinary vacuum/anchor anisotropy; a background-subtracted
residual survives but is far weaker ($\approx0.15$ baseline, though still
$\approx0.68$ predictive of the next realized current).

**Cycle-phase complementarity, precisely bounded.** Recurrent-state
fidelity is exact at period boundaries (1.000) and collapses during
contact phases ($\approx0.09$–$0.10$), with a representative case showing
11 viable transient six-node supports ($\log_2 11\approx3.46$ bits)
collapsing to exactly one final state after a fixed first contact. This
is real and quantified. The stronger reading — an uncertainty-type
tradeoff — was explicitly tested and **falsified in its simplest form**:
conditioning on the transient support left the next contact-current class
*fully determined* ($H(C_2\mid S_{\text{transient}})=0$ in every tested
case), the opposite of what an uncertainty relation would require. No
conjugate-observable algebra or variance lower bound has been defined;
"cycle-phase complementarity" is the accurate name, not "uncertainty
principle."

**A 12-period current-preserving channel, still not spatial momentum.**
Explicitly selecting contacts by alignment with the previous period's
current produced 12 consecutive periods with no current sign reversal.
Applying Section 10.2b's spatial test again, decisively: 0 of 2,145
opposite-side geodesic pairs showed persistent-sign drift over the
channel, maximum net drift was 1 graph edge, and — the precise diagnosis
— even the *spatial projection* of the contact current itself reverses
across periods (only 25 of 2,145 rulers showed 6+ consistent-sign
periods), while individual local contacts and their resulting position
steps agree in sign 98.6% of the time. Each contact pushes locally in a
real, consistent direction; the direction from which contacts arrive
itself wanders. $J$ is an interaction current, not momentum — stated as
a self-correction, not asserted from the start.

**The slow-rotation loophole, caught before it produced a false
positive.** A criterion requiring only alignment with the *immediately
preceding* current step is satisfiable by a slowly, consistently rotating
current — locally fine at every step, 90–126° from its own start within a
few periods. An apparent 9-period locally-coherent chain was traced to
exactly this: successive cosines against the *original* current were
$0.165, -0.298, -0.161, -0.466, -0.418, -0.588, -0.546, -0.219$ —
already past 90° by the second regenerated period. Rebuilding the test
against the fixed original axis rather than the previous step gives a
materially stronger negative: at most 2 regenerated periods (primary
branch) or 1 (alternate branch) — **no persistent linear spatial momentum
channel exists within the tested search.**

**A well-caveated anomaly worth carrying forward.** PCA of the rotating
current vectors shows 82.1% of variance in two components, with 7 of 8
successive angular increments sharing the same sense of rotation (net
$\approx290°$) and one reversal. Explicitly flagged as neither
established nor ruled out — a short sequence, a possible artifact of the
selection procedure itself, one exception present — but worth testing for
reproducibility, since an internal rotational degree of freedom that
persists where linear translation fails would be a materially different
and independently interesting kind of result (an early analogue of spin,
not momentum), not merely a consolation finding.

**Current hierarchy (Section 9 of Stage X15, as adopted here):** particle
identity — established; live vacuum-sustained recurrence — established;
persistent interaction current — established; locally coherent spatial
differential current — established, up to 8 regenerated periods;
fixed-axis linear spatial momentum — not established; ballistic
translation — not established; inertial mass — premature.

**Recommended next steps, in order of cost.** (a) Test whether the
angular-current rotation is reproducible across independent seeds,
mirrored initial contacts, and independent recurrent states — cheap,
reusing existing methodology, and diagnostic regardless of outcome; if
reproducible, it is a first-class result about an internal degree of
freedom, not a fallback. (b) Rerun Section 10.2h's "directional stiffness"
observation (forced off-axis contacts relaxing back toward their
pre-perturbation orientation) with the background-subtraction control
developed later in the same stage applied from the start — this is
currently the closest thing to a redirection-cost signal found anywhere
in the investigation, and it has not yet been tested under its own best
available control. (c) Only then, whether linear momentum requires a
larger correlated excitation-plus-dressing far-field mode rather than
local contact current alone.

### 10.2i What is $h$? Resolved: an exact tether-depth law, not spatial motion, raw time, or raw entanglement (Stages X17–X18)

Section 10.2b's original finding — displacement against every tested
fixed-anchor axis is exactly zero ($\Delta x=0$), with growth appearing
entirely in the orthogonal remainder $h$ — was treated through Section
10.2h as a negative result for spatial translation, and left as an open
interpretive question with three candidates. Stage X17 first closed off
one remaining hiding place for ordinary momentum; Stage X18 then
resolved $h$ itself, decisively and more precisely than any of the three
original candidates predicted.

**X17: no fixed far-field momentum axis, but a real short-range
predictive dressing.** Testing whether linear momentum might reside in a
farther, collectively stable vacuum dressing rather than local contacts,
the apparent stability of distant (radius-4) shells was found
indistinguishable from ordinary background vacuum stability — 20
unrelated fixed neighborhoods showed near-perfect persistence
(cosine $\approx0.999997$) regardless of any particle at all, so
"stability" alone there is not evidence of anything particle-specific.
What survives is a bounded, genuine effect: radius-1 and radius-2 ambient
shells predict the *next* realized contact direction well above
background-control levels (excess $+0.535$ and $+0.483$, exact
permutation $p\approx0.0016$ and $0.003$), decaying to indistinguishable
from background by radius 3–4. A dynamical dressing memory is real but
short-ranged; a conserved far-field momentum vector is not.

**X18 directly tested the proposed comparison from Section 10.2i and
found something sharper than proportionality.** $h$ is not proportional
to the Stage X5 halo scalar — the A-history's external relation count
falls to a fixed floor by the third cycle while $h$ continues climbing
($1,1,1,2,2,2,3,\ldots$) — so the two are not the same quantity. What
holds instead, exactly, across 728 of 728 checkpoints spanning repeated-A,
repeated-C, and mixed-order histories, with zero exceptions, is:

$$
h(t) = d_{\text{old}}(t) - 1
$$

where $d_{\text{old}}(t)$ is the minimum graph distance from the current
support to any pre-trajectory vacuum vertex never touched by the
particle's worldtube. A second exact regularity — every three additional
A-decisions push this boundary out by exactly one further graph shell,
with the same shell-population profile repeating one layer farther out —
held in 96 of 96 tested comparisons.

**Both halves of the original candidate ranking were tested directly and
both failed, precisely.** Raw causal time: falsified outright — A and C
histories advance maximum causal depth at the identical rate (2.0 per
cycle) while only $h$ under the A-history changes. Raw entanglement/
shared-ancestry *amount*: also falsified — by cycle 12, A and C have
accumulated nearly identical shared causal ancestry with their halos
(21 versus 22) despite $h=4$ versus $h=0$. The coupling/entanglement
instinct was directionally right but wrong in the specific quantity: it
is not *how much* correlation the recurrence accumulates that
distinguishes the branches, but *where that correlation is anchored* —
to the original untouched vacuum (C) or to freshly-generated worldtube
material the recurrence produces for itself (A).

**The resulting physical picture.** $h$ is best read as **tether depth**
or **decoupling depth**: a quantized measure of how many graph shells
now separate the recurrence from the vacuum material it originally sat
in, growing because the A-branch progressively retires its connection to
one more old shell and grows a shell of its own fresh material in its
place — not because anything moves through, or into, space. A secondary,
related process was also confirmed: only A-events advance the deepest
common causal ancestor among the support's own constituents
(mean $+4.17$ per event, post-decoupling) while C-events leave it
unchanged exactly — a real, A-selective causal-coherence clock, distinct
from both raw causal depth and from $h$ itself, supporting a
state-dependent (not universal) time-like component to the same process.

**A scope clarification worth keeping distinct.** This entire result
concerns rule 55744's *pure internal* branching mechanism (Sections
10.2a, 10.2b, this section) — no external vacuum contact is involved in
generating $h$ at all. This is a different mechanism from the
*contact-mediated* recurrence of Sections 10.2g–10.2h (rules 76073 and
58846), where the vacuum actively participates in every period. The two
threads are conceptually related — both concern a recurrence's evolving
relationship to material outside itself — but are not the same
measurement on the same object, and should not be conflated.

**Consequence for Section 10.1 — proposed, then tested and revised.**
Tether/decoupling depth was proposed here as a candidate operational
definition for the recurrence content $\mathcal{R}$. Section 10.2k
reports the direct test of this proposal and its outcome: falsified in
its simplest form. $h$'s absolute value carries no detectable local
dynamical consequence once the tether-front phase is controlled for.

### 10.2j Predictive state extends beyond the core, and the triangle needs its own momentum test (Stage X19)

Synthesizing the observables from Stages X13–X18 rather than searching
for a new one, Stage X19 established that **the recurrent core alone is
not the complete dynamical state** for either well-tested system.

**Rule 55744: $h$ requires one hidden three-state phase to be
Markovian.** A decision tree trained on $h$ plus the next action reaches
only 83.33% held-out accuracy predicting the next tether depth
(conditional entropy 0.459 bits); adding
$\phi = N_A \bmod 3$ makes the transition exactly deterministic — 288 of
288 mixed-history transitions, zero errors, conditional entropy exactly
0. A single C action leaves both $h$ and $\phi$ unchanged; an A action
advances $\phi$ by one, and only the $\phi=2\to0$ transition increments
$h$. The effective state is therefore at least
$\Psi_{\text{eff}}=(\Phi_B, h, \phi)$, not $\Phi_B$ and $h$ alone.

**Rule 58846: a finite-range dressing improves prediction of the next
contact direction.** A composite of the previous contact current and the
radius-1/radius-2 dressing vectors (Section 10.2g), with weights fitted
by leave-one-out cross-validation, improves mean predictive cosine from
0.620 (previous current alone) to 0.745, under an exact sign-flip test
($p=0.03125$). Transferred without refitting to an independent 12-period
trajectory, the same composite still improves prediction on 9 of 11
transitions ($p=0.0327$), though the absolute weights are not universal
across trajectories. The shared lesson across both rules: **the
recurrent core is an identity label, not the whole physical state** —
predictive information is distributed across the core and a finite
surrounding dressing.

**The massless triangle needs its own momentum test — it is not exempt.**
Evolved for 30 events under its exact period-1 action, the transitive
triangle reproduces its normalized shape in 31 of 31 recorded states,
with full original-vertex turnover by event 3 and a causal front
advancing at exactly one vertex per event. Tested against a fixed old
anchor pair with verified-constant mutual distance, its net longitudinal
displacement over 30 events is **exactly zero**, while an off-axis,
tether-like remainder grows by 10 — the identical qualitative signature
found for rule 55744 in Section 10.2b. Fresh-material turnover is not,
by itself, evidence of spatial momentum, for the massless candidate any
more than the massive one; Section 3.2's framing is corrected
accordingly.

### 10.2k The tether phase is a genuine instantaneous state, but $h$ carries no local dynamical weight (Stages X20A–X20B)

**X20A: the hidden phase is directly readable from relational geometry,
not merely remembered.** For each of the five support vertices, define
$d_i$ as its graph-distance to the nearest untouched pre-trajectory
vacuum vertex, and $n_{\min}$ as the number of vertices achieving the
minimum. Across 738 post-shell checkpoints spanning 42 distinct natural
supports from 8 evolved vacua (a development set and an independently
generated held-out set), exactly

$$
\phi = 3 - n_{\min}
$$

with zero exceptions, and the finer coordinate
$Q_{\text{tether}} = h + (3-n_{\min})/3$ equals $N_A/3$ exactly (to
floating-point precision) at every tested checkpoint. The historical
counter $N_A$ is therefore fully reconstructible from the instantaneous
relational state alone — a real state variable, not a bookkeeping
artifact requiring memory of the trajectory. Rooted local-neighborhood
isomorphism confirms the same finite core+dressing geometry simply
recurs one shell farther out at each higher $h$ (84/84 and 48/48 exact
matches at radius 1 and radius 2 respectively).

**X20B: this directly tests, and falsifies, this document's own proposal
for $\mathcal{R}$.** Holding core phase and tether-front phase fixed
while varying $h\in\{1,2,3\}$, and applying identical perturbation
challenges (single and double relation deletion, relation addition,
native external contact, sampled triple deletion — 1,728 matched
challenge triplets in total), the outcome was **identical at every
tested $h$, with zero exceptions.** Because the local core+dressing
neighborhood is exactly repeated at each shell (X20A), any challenge
whose repair basin lies inside that repeated neighborhood must respond
identically regardless of absolute depth. The corrected effective-state
decomposition is

$$
\Psi_{\text{eff}} = (\Phi_B, \phi;\, h),
$$

where the semicolon is deliberate: $(\Phi_B,\phi)$ governs local
dynamics, while $h$ only locates that local state relative to the old-
vacuum boundary, the way a position coordinate in a homogeneous medium
is real without the local physics depending on its absolute value. $h$
is not a local energy, mass, or inertial-cost variable in the tested
regime.

### 10.2l A one-way causal channel: the tether ratchet (Stages X21–X22)

**X21: the old-vacuum boundary is not an active tether.** The complete
set of native boundary-touching gates is exactly identical across
$h=1,2,3$ (12 of 12 matched cases, mean Jaccard similarity 1.000), and
exact positive causal cones launched from the boundary show no
$h$-dependent propagation delay across 144 matched comparisons at depth
4, extended to depths 6–7 on representative cases — zero particle
contacts throughout. Most strikingly, **deleting every relation
connecting the nearest untouched shell to the recurrence entirely** still
leaves the core exact and both branch continuations legal for six further
recurrence cycles (72 of 72 tests) — the old-vacuum tether used to
*define* $h$ is not required to actively sustain the particle at all.

**X22 reverses the direction and finds a genuine, if narrow, asymmetry.**
Core-originated causal cones fail to reach the old boundary in a broad
depth-4 screen (0 of 54). But launching from the recurrence's immediate
dressing — a native external gate at the core-dressing interface — reveals
a different structure: in a reproducible subclass of natural supports (63
of 423 matched tests; 7 of 47 supports succeeding at *every* tested
$(h,\phi)$, an exact all-or-nothing split with no intermediate cases),
positive causal influence walks backward through a stored sequence of
prior interface gates and reaches untouched old-vacuum material, with an
exact constructive path length

$$
\tau_{\text{path}} = 3h + \phi - 1 = N_A - 1,
$$

verified for $N_A=3$ through $11$. Testing the reverse direction on
these same *outward-positive* supports, with the same and deeper
controls (47 native inward gates, 0 particle contacts), the asymmetry
holds: outward propagation is real and exact in this subclass; inward
propagation was not found in any tested case. The mechanism does not
violate Section 10.2d's old-handle non-creation theorem — every outward
step consumes a handle already present in the next interface layer,
touching the old-vacuum vertex only in the final, legally-matched event.

**Why this is not yet called a horizon, stated as plainly as the report
itself states it.** Only 7 of 47 natural supports possess the complete
channel; it is launched from one specific native gate, not general core
perturbation; the inward null result is exact-but-bounded-depth, not a
proven impossibility; and no mass, inertia, redshift, or metric
deformation has been measured. What is established is narrower and still
genuinely new: a reproducible, exactly-quantified subclass of dressed
states with a one-way positive-causal interface channel — a **causal
ratchet** — worth pursuing as a research direction in its own right,
independent of whether it eventually earns any gravitational language.

### 10.2m The channel is broader than first found, and carries real information (Stage X23)

**The forward phenomenon is not limited to the original 7/47 persistent
ladders.** Relaxing path identity while keeping causality strict, 20 of
the same 47 supports (42.55%) admit *some* two-descendant forward channel
at $(h{=}1,\phi{=}0)$; a fresh cohort of 48 supports from independent
seeds added 15 more (31.25%), giving 35/95 (36.84%) combined. The
original persistent ladders are a especially clean sub-phenotype of this
broader transmitter class, not the whole of it.

**Existential reachability was upgraded to measured information
transmission.** Firing one of three local source actions (the external
dressing launch, or either internal recurrence action) and checking
whether a causally-descended event reaches untouched old vacuum within
three further selections gives $P(\text{contact}\mid\text{launch})=0.183$
against **exactly 0** for both internal controls, across all 20
forward-channel supports. With equal input priors this is
$I(X;Y)\approx0.099$ bits per attempt; the corresponding channel capacity
is $\approx0.104$ bits. These are explicitly scheduler- and
depth-dependent operational numbers, not fundamental constants, but the
qualitative content is real: **the remote old-vacuum boundary can
statistically distinguish a local dressing choice from an internal
recurrence choice.**

**A two-part structural criterion for the persistent-ladder subclass was
pre-registered and validated prospectively — precisely the discipline
Stage T's retrospective failure demanded.** The criterion —
interface purification (exactly one external gate after the second A
recurrence) *and* receiver reachability (a two-descendant forward path
at $h{=}1,\phi{=}0$) — was frozen, then tested blind on 48 fresh
supports: 48/48 correct, 6 new persistent ladders identified before
being checked, one-sided Fisher exact $p=8.15\times10^{-8}$. Combined
with the development corpus: 95/95 correct, 13/95 (13.68%) persistent.
The tether phase also modulates channel latency exactly:
$\tau_{\text{witness}} = N_A - 1$, holding across 117 total successful
witness states with zero deviations.

### 10.2n An exact mechanism, shown to be genuinely live — and a sharp conceptual line (Stage X24)

**The persistent ladder has a proven, not merely observed, grammar-level
mechanism.** Every one of 117 known ladder links uses the identical role
transport $O_4 \to I_4$ (the fourth output relation of one event becomes
the fourth input relation of the next), and because Rule 55744 requires
birth order $u<v$ in that same role, this transport forces
$v_{t+1}=u_t<v_t$ — a strict, exact descent, with zero exceptions,
proven directly from the rule's grammar rather than observed
statistically. This is the same ancestral-descent monotone Stage X8
found as an *obstruction* to indefinite translation, now serving as the
*mechanism* for a finite backward channel — one structural fact playing
opposite roles in two different physical questions.

**The channel was shown to activate under the real, unrestricted global
scheduler, not only under a favorable conditioning.** Across 350 trials
with every legal vacuum event competing, natural receiver contact
occurred in 25/350 (7.14% overall; 20.33% conditional on the launch
firing first, 95% CI 13.6–28.5%). Persistent ladders proved substantially
more robust under this real competition than generic short-channel
supports (37.14% vs. 13.64% launch-conditional success,
$p\approx0.0062$). The X23 classifier was further validated
out-of-distribution across different vacuum ages (200 and 900 events, not
only the original 450): 29/29 correct, combined total 124/124 across
three tested ages.

**The massless triangle was re-examined under the same diagnostics, and
the result sharpens a distinction worth stating plainly.** The triangle
has a *perfect* forward causal chain (30/30 producer links) — cleaner
than Rule 55744's minority phenotype — but it advances *with* fresh
material, the opposite direction from the backward ladder, and its
fixed-anchor displacement remains exactly zero (confirming Stage X19).
**Causal propagation and spatial momentum are not the same observable**:
the triangle has the cleanest possible causal chain in the entire
investigation and still shows no momentum, while Rule 55744's dressing
transmits real information without yet showing momentum either. Four
distinct observables — causal current, information current, material
turnover current, and spatial momentum — should be kept explicitly
separate going forward.

### 10.2o The control that matters most: how much of the ratchet is real? (Stage X25)

Stage X24 itself proposed the necessary next test: does the exact
birth-order mechanism survive if Rule 55744's explicit $u<v$ role
selection is removed? The answer is a genuinely informative mixture of
yes and no, not a clean confirmation or a clean debunking.

**The compact particle is birth-order dependent.** Symmetrizing the
$u/v$ role assignment destroys the three-state A/B/C identity as a
universally closed class (expected survival under 2 local events before
leaving it) and breaks the exact three-state tether clock (a fourth
residual pattern appears in 5.5% of checkpoints, breaking X20A's clean
alphabet). Causal-age sensitivity is not incidental to this particular
compact excitation — it is part of what makes it a small, sharply
identified object at all.

**But recurrence itself is not birth-order dependent.** An exact
breadth-first search from the symmetrized rule finds a single, fully
closed, 107-state strongly connected component with zero dead states —
larger, less sharply defined, but genuinely present and naturally
abundant in the vacuum. Symmetrization traded a compact, exactly-clocked
particle for a broad, structurally looser recurrent flow.

**The specific X24 mechanism is exactly and completely dissolved.**
Sampling 83 natural $O_4\to I_4$ transports under the symmetric grammar:
33 decrease in birth rank, 50 increase — an even split with no
preference, precisely because the $u<v$ premise the strict-descent proof
depended on no longer exists. The ratchet Stage X24 proved is not a deep
emergent fact; it is a direct, removable consequence of one explicit
grammar convention.

**Yet the broader one-way channel did not simply vanish with it.** A
pilot test on the same symmetrized grammar, using an actual persistent-
ladder state converted to the new rule, still found the outward launch
reaching old vacuum in 16/60 trials (26.7%) while 72 sampled reverse
attempts from 12 old-boundary sources found 0 contacts — smaller and
less exhaustive than X21–X24's searches, but not nothing. Something
beyond the birth-order convention is still producing an asymmetry.

**A hypothesis was proposed here — that the residual asymmetry is simply
Section 5.2's causal-directionality theorem showing up in a new guise —
and Stage X26 (Section 10.2p) tested it directly and found it incorrect,
more precisely than a flat no.** The correction is worth stating exactly
rather than just noting the miss: it is not fresh-node creation in
general (Section 5.2's theorem, which concerns outputs) that produces the
residual asymmetry; it is specifically the directed source-role labeling
carried by the *pre-existing* relational substrate. That is a real,
different, and more specific mechanism than the one guessed at here.

### 10.2p The decisive control: source labels on old material, not fresh-node creation itself (Stage X26)

Stage X26 graded its controls deliberately, so that only the decisive
test would be credited with the result. Symmetrizing the fresh-containing
outputs, then symmetrizing *all* outputs of Rule 55744's grammar, changed
nothing: the matched reverse census stayed at exactly 0/47 positive
sources, now checked across 281,863 and then 843,837 candidate
second-descendant events respectively. The forward channel, if anything,
became richer under these controls (2 receiver gates at baseline, rising
to 18 under full output symmetrization) — ruling out the simple
hypothesis that asymmetric output-source assignment alone produces the
one-way channel.

**Only symmetrizing the source labels already carried by the
pre-existing snapshot changed the result, and it changed it precisely.**
With the existing relational substrate itself made source-undirected —
while retaining ordinary forward rewrite semantics, old structure
consumed, a genuinely fresh vertex still created — the same representative
outward launch now reaches old vacuum in a single step (8 immediate
receiver gates, down from a depth-2 latency in every directed control).
And, decisively, the identical 47 matched old-boundary sources that
produced zero reverse contacts in every prior control — baseline,
fresh-output-closed, full-output-closed — now yield **2 exact positive
reverse paths** (sources 11 and 24, each with 16 receiver gates, witness
chains verified explicitly). The same two sources had returned zero
contacts against as many as 12,166 second-descendant candidates in the
strongest directed control tested; source-undirecting the old substrate
alone was what changed the outcome.

**A clean independent cross-check.** The 24-state terminal SCC reached
by fully output-source-symmetrizing the directed rule is *exactly* the
reachable set of a completely separately-implemented source-undirected
representation — 24 states, zero states unique to either
implementation. Two different code paths landing on the identical object
is good evidence this endpoint is a real feature of the rule family, not
an artifact of one specific construction.

**The corrected physical picture.** Reciprocity is restored, but only
partially: $\tau_{\text{out}}=1$ against $\tau_{\text{in}}=2$ for just 2
of 47 matched sources. "Strictly one-way" is no longer an accurate
description once source-directionality on old material is removed; "close
to symmetric" is not accurate either. The channel is better described as
**strongly, asymmetrically biased** — closer to ordinary directional
diffusion down a gradient than to an absolute, horizon-like prohibition.
Fresh-node creation alone (Section 5.2's theorem) is confirmed **not**
sufficient to explain it; directed source semantics on already-existing
relations is the specific mechanism, isolated cleanly for the first time
by this stage.

**Consequence for the program.** The symmetry-control sequence (X25–X26)
has now answered its diagnostic question about causal orientation as
thoroughly as is reasonable to expect: birth order (dissolved by X25),
output-source direction (ruled out by X26), and old-substrate source
direction (identified by X26 as the actual mechanism, and shown to
produce only partial, not absolute, asymmetry) are now cleanly
separated. Continuing to strip structure from Rule 55744 would risk
diminishing returns relative to the program's actual goal. The
recommended next stage returns directly to that goal.

### 10.2q The first direct test of operational inertia — corrected, and a real capacity bias found (Stages X27–X28)

This is the first stage to test this program's founding hypothesis
directly, as originally stated in Section 10.2: does redirecting a
persistent recurrent state cost more, in rewrite effort, than letting it
continue. Using rule 58846's predictive dressed state
$\Psi_{\text{eff}} = (\Phi_6, J, D_1, D_2)$ from Stage X19, with the X19
predictor weights frozen (no refitting) and the massless triangle
retained as an explicit control, two questions were asked.

**Correction, made by Stage X28 and confirmed by direct audit.** X27's
original report concluded that the dressing does not constrain available
transport directions, based on a "successor-boundary" reindexing applied
during its final consolidation. Stage X28 re-audited the underlying X15/
X16 construction directly — matching each boundary's actual outgoing
current against its X16 label — and found this reindexing was itself an
off-by-one error introduced late in X27, not a correction: agreement
between the true same-boundary indexing and the X16 labels is exact
(cosine $1.0$ to floating-point precision, all 8 boundaries). **With the
correct indexing, the result reverses.**

**Does the dressing constrain which directions are legally available at
the same boundary, not merely predict which one is chosen?** Correctly
indexed, 76 legal non-ancestral transport actions were found across the 8
boundaries, 70 forward-aligned and 6 reverse-aligned. Exact permutation
tests over all $8! = 40{,}320$ temporal assignments give
$p=0.0097$ (action-weighted alignment), $p=0.00025$ (boundary-balanced
alignment), and $p=0.0064$ (positive-action count) — all significant.
**The dressed state is genuinely associated with the available legal
directional capacity, not only with the realized choice.**

**Does forcing the most strongly misaligned legal contact cost more
rewrite effort to return to the recurrent class than the realized choice
would have?** This part of X27's conclusion is unchanged by the
correction. Across 7 matched boundaries with large, genuine misalignment,
under the same bounded return-search protocol used throughout Stages
X17–X19: **all 7 realized continuations and all 7 forced redirects
returned successfully**, with identical total cost (23 rewrites each;
per-pair differences $[1,0,1,-1,0,0,-1]$). **A local, one-step rewrite-
cost penalty for redirection is still not found.**

**The corrected picture is therefore a real split, not a flat negative:
directional availability bias — yes; local cost penalty for using the
disfavored option — no.** The triangle control reconfirmed its
established role throughout (31/31 exact states, 30/30 causal links,
$\Delta x=0$): material turnover is still not rest mass, causal
propagation is still not spatial momentum.

### 10.2r Locating the mechanism: an interface architecture, not a self-restoring field (Stage X28)

Given the corrected split above, X28 asked directly whether $D_1/D_2$
behave like autonomous causal variables — something that could plausibly
underlie an inertia-like restoring effect — using three escalating
interventions on the same rule 58846 trajectory.

**Ordinary nearby vacuum activity cannot move $D_1$ at all.** Of 592
clean legal core-disjoint events tested across all 8 boundaries (no core
vertex, no reference anchor, no baseline gate overlap), $D_1$ changed in
**zero** cases; $D_2$ changed in 52/592, by a maximum magnitude of 0.043
(minimum cosine to its own prior value: 0.9999). $D_1$ is tightly bound
to the immediate particle-vacuum interface, not a freely propagating
field coordinate.

**Matched legal forks could not establish causal priority for either
dressing vector.** Two core-preserving contacts with nearly identical
imposed current direction but substantially different $D_1/D_2$ changes
were compared; neither branch's own dressing predicted its own future
channel cloud better than the other's, swapped in (exact sign-flip
$p=0.25$) — inconclusive, not a strong negative, but no support found for
$D_1/D_2$ as independent causal drivers.

**A diagnostic (explicitly non-physical) single-relation deletion
localizes the real causal object, and reveals that apparent recovery is
an illusion.** Deleting one interface relation at each of 7 boundaries
(core, fixed-anchor distances, and baseline outgoing gate all preserved
exactly) attenuates $D_1/D_2$ by roughly half after one recurrence cycle
(median residual fraction 0.539) — but the deleted relation is restored
in **0 of 7** cases. Tracked across further phases, the same permanently-
missing relation's measured effect on $D_1/D_2$ is shown to be
non-monotonic: it can shrink to near-invisibility at one phase (as low as
0.10 of its original effect) and then **rebound** to strong at a later
phase (0.70 or higher) — proving the apparent one-cycle "recovery" is
phase-dependent *screening* of a permanent defect, not repair of it. This
is an important, precise negative for any model of $D_1/D_2$ as a simple
self-restoring "dressing spring."

**The same deletions show the underlying interface graph, not $D_1/D_2$
themselves, does the real causal work.** At 2 of 7 tested boundaries,
deleting the same relation removes one specific legal forward-aligned
transport channel outright — direct, if narrow, evidence that specific
interface relations are literal constituents of specific future
transport opportunities, distinct from and prior to the compressed
$D_1/D_2$ summary computed from them.

**The massless triangle control rules out the tempting shortcut that any
sufficiently robust recurrence would show this kind of self-repair for
free.** Severing the triangle's old wake connections entirely still
leaves its exact recurrence fully intact (11/11 both arms), and the
severed connections never regenerate, with the old anchor permanently
disconnected throughout. Pure recurrent identity does not by itself imply
restoration of severed external structure.

**Updated picture:** recurrent core + phase-dependent interface grammar
$\to$ predictive dressing observables + anisotropic legal transport
capacity. $D_1$ and $D_2$ are compressed readouts of a richer interface
structure, not themselves the fundamental causal variables.

**The most promising reframing of inertia to come out of this arc.**
Two direct tests of a *local* resistance law have now failed (X27
corrected, X28). But a real directional *availability* bias has been
established. This suggests inertia in this substrate, if it exists, may
not be a local force at all, but an **emergent statistical bias in which
continuations survive** — forward-aligned paths being more numerous and
more likely to lead back into the recurrent class, without any single
step costing anything extra. This would be a survivorship-based
mechanism rather than a Newtonian resistance mechanism, and notably
better matched to this framework's own founding premise (Section 1;
recall the branchial/multiway framing from early in this investigation)
than a local force would have been.

**Recommended next stage (X29 — Scheduler-Weighted Directional
Persistence).** Stop perturbing $D_1/D_2$ directly. Enumerate all legal
particle-touching actions at many boundaries, weight each by its actual
scheduler probability rather than a greedy choice, and directly compare
$P(\text{recurrent survival}\mid\text{forward-aligned})$ against
$P(\text{recurrent survival}\mid\text{reverse-aligned})$ under live,
unbiased evolution — tracking directional autocorrelation of the
*surviving* recurrent worldline specifically, not of all attempted
contacts. The triangle remains the control separating causal/material
propagation from fixed-frame spatial momentum. A confirmed survival
asymmetry would give this program its first operational, non-Newtonian
statistical mechanism for inertia; a null result would mean the
predictive dressing should be read as local interaction memory rather
than inertia.

### 10.2s A mechanism reconciling capacity bias with equal cost: measure, not resistance (Stage X29)

Stage X29 tested directly whether X28's directional capacity bias has
operational meaning under the rule's actual scheduler, which chooses
uniformly from the legal gate set at every event — meaning legal channel
*count* at a boundary is itself an exact probability measure, with no
additional weighting model required.

**A real, quantified one-step directional bias in scheduler mass.**
Using X28's source-audited strict transport census, pooling across all 8
boundaries gives 70 forward against 6 reverse (92.1% forward). Because 5
of the 8 boundaries admit no reverse channel at all, the more meaningful
figure restricts to the 3 boundaries where both signs genuinely compete
(P0, P4, P5): 28 forward against 6 reverse, an **82.4%** forward
fraction conditional on a strict transport event actually occurring.

**But every available reverse channel, once selected, survives exactly
as well as a matched forward one.** All 6 reverse channels at the mixed-
sign boundaries were tested exhaustively (not sampled) against an equal
number of forward controls drawn at random from the same boundaries,
under the identical bounded two-contact return protocol used in Stages
X17/X28: **6/6 and 6/6 returns**, with cost difference not significant
(mean 3.33 vs. 3.00, exact one-sided sign-flip $p=0.25$).

**This reconciles X27/X28's two findings into one coherent mechanism
rather than leaving them as an unexplained pair.** The bias is not a
resistance encountered once a direction is chosen — it is a difference
in how *often* each direction is legally offered in the first place. A
rare reverse channel is not dynamically expensive; it is simply
outnumbered. This is closer in character to an entropic effect (fewer
legal microstates lead that way) than to a Newtonian force, and gives
Stage X28's "survivorship" reframing an explicit mechanism: uniform
sampling over an asymmetric channel count, rather than a metaphor.

**Precisely scoped as a snapshot result, not yet a persistence law.**
X29 explicitly does not establish conserved momentum, a velocity
variable, a force law, an inertial mass scalar, or — the honest
limitation driving the next stage — whether this one-step bias
compounds into genuine sustained directional persistence over an
unforced, many-step trajectory, as opposed to washing out. The triangle
control was not artificially forced into a comparable scheduler-mass
test, since it lacks the same legal-gate ensemble; existing controls
(exact recurrence and causal advance without demonstrated momentum, no
wake self-repair) stand unchanged, confirming this bias is specific to
rule 58846's dressed interface grammar rather than a generic consequence
of recurrence.

**Recommended next stage (X30 — Unforced Scheduler Worldline
Persistence).** Run genuinely unforced live evolution from matched
dressed recurrent boundaries under the ordinary uniform scheduler —
selecting no contact preferentially — and track only histories in which
the recurrent excitation remains identifiable. Measure survival time,
the realized sequence of interaction-current directions, period-to-period
directional autocorrelation, and the forward/reverse transition matrix
relative to the instantaneous predictor, against both a predictor-time
permutation control and a dressing-scrambled control. The decisive
outcome is a positive directional autocorrelation in *unforced surviving*
histories that disappears once the dressed-state/time association is
deliberately broken — the first test that would show this one-step
measure bias actually compounding into an operational persistence law,
rather than remaining a snapshot fact about isolated boundaries.

### 10.2t Existence versus measure — a recurring structural gap, and the first spontaneous returns (Stages X30–X31)

**Stage X30 ran the genuinely unforced test X29 called for, with no
favorable contact selection at all, and found a clean negative: 0 of 40
trials recovered exact recurrence even once**, so the planned directional
autocorrelation could not even be formed. This does not contradict X29:
the strict transport subset X29 measured (70 forward / 6 reverse) turns
out to be under 10% of all legal touching contacts at the starting
boundary (15 of 158 legal gates). Ordinary scheduler activity samples a
much broader grammar that the favorable bias simply does not reach.

**Stage X31A re-diagnosed the actual bottleneck with a precise, important
distinction: path existence is common, spontaneous recurrence is not.**
Across all 198 legal touching contacts spanning the 8 recurrent
boundaries, 187 (94.44%) have *some* bounded recovery path under the
fixed search grammar — recovery is abundant, not scarce. X30's failure
is therefore not an absence of recovery paths; it is an absence of
scheduler measure on the sequences that realize them. This is the same
structural gap Stage O identified for repair many stages earlier (real
repair paths existed, Stage M; the natural vacuum's realized repair rate
was far lower than needed, Stages N–O) — existence and measure separating
in the same way, now for translation rather than repair, independently
rediscovered rather than assumed. It is worth treating as a candidate
general property of this substrate and checking for explicitly in any
future question this program takes on.

**A genuinely surprising, carefully-scoped discriminator was found along
the way.** A repeated four-core interface motif differs only in which
recurrent-core vertex plays a directed source role in an otherwise
identical pair of gates — same immediate fidelity, same predictor
alignment — yet one orientation is 8/8 recoverable and the other only
2/8 (exact paired-sign $p=0.0156$; Fisher $p=0.0035$, tightening to
$p=0.0007$ for easy-only recovery). Recoverability depends on directed
interface role semantics beyond both the core state and the $(J,D_1,D_2)$
dressing. Explicitly and appropriately **not** claimed as spin or
chirality — flagged only as worth monitoring — though it is now the
second independent hint of an orientation-sensitive hidden variable in
this program, after Stage X15's still-unconfirmed angular-current
rotation; whether the two are the same underlying structure is an open
question worth checking directly.

**Stage X31B found the first spontaneous exact returns anywhere in the
unforced X-series.** Restarting from P4 and P5 — the only selected-
trajectory boundaries with 100% contact-level recoverability (30/30 and
27/27) — produced 3 spontaneous exact returns across 40 trials (2/20 and
1/20), at organically long event counts (174–383 events), with no
favorable steering. Non-lost tracking is significantly better than at P0
(55% vs. 25%, one-sided Fisher $p=0.023$); the exact-return improvement
itself remains suggestive rather than decisive at this sample size
($p=0.12$). A survivor-enrichment test — restarting from the 3 returned
states — found no evidence of self-reinforcement (2/30 further returns,
$p=0.72$): these successes are real but do not yet define an attracting
basin.

**The measurement hierarchy for a persistent, massive-style excitation is
now four layers deep**, with the last two only weakly and phase-
dependently established for rule 58846: recurrent core (established);
dressed interface state (established); directional transport capacity
(established, Stage X28–X29); scheduler-robust recovery measure
(present only weakly and phase-dependently, Stage X31).

**Recommended next stage (X32 — Interface-Protected Recurrence Search).**
Use the X31A role discriminator actively rather than continuing to
sample rule 58846 states passively: search for or construct states/rules
that suppress the hard role-2-source orientation, protect the late
source-only failure class identified in X31A, and preserve the X19-style
directional dressing, scored jointly on contact-level recoverability
*and* actual scheduler-realized recurrence rate — validating any
candidate immediately with unforced restarts. Given X31B's null
enrichment result, the decisive test is whether actively designing for
the role discriminator (not merely selecting already-favorable
boundaries) produces a state whose spontaneous returns *do* compound
under restart, rather than another locally-better but still-fragile
point. Only once multiple exact unforced returns occur in a substantial
fraction of trials does the directional-persistence/autocorrelation
question become meaningful to revisit.

### 10.2u The discriminator used constructively, and an explicit strategic checkpoint (Stage X32)

**Using the X31A role discriminator to actively search, rather than only
diagnose, produced a real, substantial improvement.** Screening the 16
natural Rule 58846 recurrent classes recovered in Stage X12 for
directed-role compatibility and full contact-level recoverability
identified "Candidate 8": 21/21 particle-touching contacts have a
bounded return path (mean cost 3.286), all 6 of its directed-role swap
pairs return in both orientations (against P0's destructive asymmetry),
and under the ordinary unforced scheduler across 70 trials, **16/70
recovered exact recurrence at least once** (22 total returns, 5 trials
with multiple returns, one with three) — against P0's 0/40, one-sided
Fisher $p=0.00036$. Several repeat returns occur with **zero constituent
overlap** with the immediately preceding exact support (7 of 11 recorded
return events), confirming particle identity here is genuinely
independent of any fixed set of vertices, consistent with Section 3.1's
original framing. Candidate 8 and X31's P4 are not yet statistically
distinguishable from each other ($p=0.17$) — this is a real jump over the
original trajectory, not yet a demonstration that the ceiling has been
raised further.

**This is a genuine validation that the capacity-hierarchy framework
(Section 10.2d onward) works as an active design tool, not only a
post-hoc explanatory one** — the same standard set by X11's pruning
success and now repeated one level up the hierarchy.

**An explicit strategic checkpoint, worth recording rather than only
discussing in conversation.** Twenty stages (X13–X32) is a long
investment in one rule, and the recurring existence-versus-measure gap —
independently found for repair (Stage O), frontier regeneration
(Stages X8–X12), and now scheduler-realized recurrence (Stages X30–X32)
— raises a real question of whether continued refinement within Rule
58846 is addressing a structural property of this entire rule family
rather than a fact specific to this one rule. Two concrete, low-cost
checks are recommended before further investment compounds:

1. **Stage X33 (already planned) doubles as a decision fork, not only an
   incremental step.** Re-fit the predictive dressing on Candidate 8. If
   it shows a genuine directional bias comparable to P0's, that is
   evidence this property is somewhat generic across Rule 58846's state
   family, supporting continued investment. If Candidate 8's robustness
   comes without directional bias, that would suggest scheduler-
   robustness and directional bias are in tension *within this specific
   rule* — a structural reason to look elsewhere, not merely a fragile
   trajectory.
2. **A parallel, independent check, run alongside rather than after
   X33.** Apply the same method that produced Candidate 8 — screen a
   rule's natural recurrent states for directed-role compatibility and
   full contact recoverability, validate the best one against an
   unforced scheduler — to a different Stage W rule entirely (not
   55744, not 58846). A comparably strong result at comparable effort
   would show the *method*, not the specific rule, is what is doing the
   work, making diversification low-risk. A much harder search on a
   fresh rule would be real evidence Rule 58846 has a non-generic
   advantage worth continuing to mine specifically.

### 10.2v The strategic checkpoint answered: the method generalizes, and outperforms (Stage X32R)

Item 2 above was carried out as a pre-registered cross-rule replication,
with the discipline that makes its answer trustworthy stated up front:
**the replication rule was frozen using only Stage W evidence that
existed before Stage X31 ever ran** (highest producer-flow survival among
untested W41 rules, excluding 55744, 58846, and 76073, selecting Rule
55584), with a fixed search budget and an explicit rule against extending
it if early results looked unpromising. The discovery implementation was
calibrated against the *known* Rule 58846 case first, confirming it
correctly detects the established recurrence class before being pointed
at the fresh rule.

**The result is not merely a replication — it is an outright
improvement over 20 stages of accumulated refinement on Rule 58846,
using the identical fixed pipeline.** Natural-state discovery in Rule
55584 was, if anything, easier (81 hits, 36 distinct states, within the
same fixed budget that found 5 distinct states for 58846). The selected
winner (instance 28) has 12/12 contact-level recoverability at a
uniform first-found cost of 2 — shallower than Candidate 8's basin — and
under the same 70-trial unforced validation: **34/70 (48.6%) trials
returned to exact recurrence at least once, 54 total returns, 14/70
multi-return trials, one trial with 5 returns.** Against Candidate 8
(16/70, 22 total, 5/70 multi-return), one-sided Fisher tests give
$p=0.0013$ for exact-return incidence and $p=0.023$ for multi-return
incidence — Rule 55584's winner is statistically *better*, not merely
comparable. Constituent turnover was confirmed independently: 26 of 54
return events share no vertex with the original support, 19 of 54 share
none with the immediately preceding exact support.

**One honest methodological wrinkle, handled correctly.** None of the 36
discovered Rule 55584 states contain a literal $y/z$ mirror pair of the
exact form Stage X31's role-discriminator test requires — a genuine
structural difference in this rule's own interface grammar, not a
failure of the test. Rather than manufacture an artificial analogue, the
pre-registered fallback (the complete role-resolved contact-fate census)
was used instead, exactly as specified in advance.

**This directly answers Section 10.2u's checkpoint: scheduler-robust
recurrent identity is not a Rule 58846 accident.** The method — natural-
state discovery, a small unforced screen, directed-role/contact-fate
protection screening, large-scale unforced validation — finds comparable
or stronger carriers in a rule selected blind. Candidate 8 converts from
a possible one-rule artifact into evidence for a broader, discoverable
class of recurrent particle-like carriers, which is a more valuable
result for the program than continued refinement of one rule would have
been.

**What remains genuinely open, and is now the right next priority.**
This replication settles survival, not directionality. Rule 55584's
winner has not yet been given the X17–X19 predictive-dressing treatment
that produced 58846's directional capacity bias (Sections 10.2g–10.2s).
**The decisive next comparison is a head-to-head fit of the X17–X19/X33
dressing protocol on both Candidate 8 and the Rule 55584 winner.** If
both develop comparable directional memory, particle-like recurrence
plus directionality is likely a generic, selectable architecture — a
substantially stronger claim than anything established so far. If only
58846 shows it, that would precisely localize 58846's remaining special
value to its momentum/dressing structure rather than basic survival.
This comparison should take priority over further refinement of either
rule in isolation.

### 10.2w Directional dressing generalizes; temporal persistence still does not (Stages X33–X34)

**Stage X33 ran exactly the head-to-head comparison Section 10.2v called
for, and the answer is a clean, strong positive for generalization.**
Both carriers were analyzed with an identical portable protocol (trial-
held-out LOO fitting throughout, no favorable contact selection). Rule
55584's Winner 28 shows dressing and capacity-bias effects at least as
strong as Rule 58846's Candidate 8, and in most respects stronger:
LOO composite predictive cosine 0.835 vs. 0.733; forward-hemisphere
strict transport capacity 93.3% vs. 82.3% ($p<0.0002$ both). The
single simple predictor $-D_1$ alone achieves 0.690 (58846) and 0.838
(55584) with no fitting at all, and **weights fit on one rule transfer
to the other with almost no loss** (58846's weights score 0.834 on
55584's own data, against 55584's own fit of 0.843) — strong evidence
this is one shared architectural feature, not two independent
coincidences. What remains negative in both: lag-1 current correlation,
once compared against each carrier's own static directional-anisotropy
baseline rather than zero, is not significant (58846: negative; 55584:
$p=0.356$ after control).

**Stage X34 searched explicitly for temporal persistence across the
full robust-carrier population and found none that replicates.**
Twelve pre-screened Rule 55584 states plus the 58846 reference were
tested with a stricter renewal-current observable and an explicit
same-state random-pair baseline subtracted
($M_1 = C_{\text{adjacent}} - C_{\text{static}}$). The strongest
integrated carrier (55584 Winner 28) shows no excess ($M_1=-0.10$,
$p=0.61$). One candidate (state 22) showed an initially encouraging
excess ($M_1=+0.40$, $p=0.18$) that produced **zero usable adjacent
directional pairs across two independent follow-up blocks** — a clean
non-replication, not a suppressed result. The combined, cross-rule
conclusion: **robust recurrence plus strong instantaneous directional
dressing does not imply temporal momentum memory.**

**Toward a reframing: is linear translational momentum the wrong target
entirely?** X34's own Section 8 independently proposes searching for an
internal orientation-like sector ($\sigma$) that survives recurrence and
couples to $D_1$/current direction — explicitly declining to call it
spin prematurely, but naming exactly this shape of variable as the
missing ingredient. This connects to two things already established
separately, never yet checked against each other. First, the *exact*
tether-phase law $\phi = N_A \bmod 3$ (Sections 10.2i, 10.2k) is a
genuine cyclic, group-valued quantity with an exact instantaneous
readout — but it was established entirely within Rule 55744's pure
internal-branching mechanism; whether an analogous cyclic phase exists
for the *dressed* contact-mediated carriers (58846/55584) and couples to
$D_1$'s direction has not been checked. Second, the Stage X15 angular-
current rotation (82% variance in two PCA components, ~290° net
rotation, mostly one consistent sense) is an independent empirical hint
of exactly this kind of variable.

The physical motivation is precise, not merely suggestive: momentum, in
its actual technical definition, is the rate of phase advance of a
wavefunction with respect to *position*; angular momentum is the same
structure with respect to *rotation angle*. Which one applies here
depends on what continuous quantity a candidate phase is advancing
against. Because $\phi$ and $h$ advance per *event*, not per unit of
demonstrated spatial displacement (shown repeatedly to be exactly zero,
Sections 10.2b–10.2j), a phase of this kind is structurally closer to an
**energy or intrinsic angular-momentum (spin) candidate** than to linear
momentum — which would make it a candidate for Section 10.1's still-
unsolved rest recurrence content $\mathcal{R}$ rather than for Section
10.2's velocity/dispersion program.

**A sharper, not-yet-run test.** Every temporal test to date (X27–X34)
asks whether $J_{t+1}$ points in the *same* direction as $J_t$ — always
negative. This is the wrong test for an angular/rotational conserved
quantity: a steadily precessing vector fails a same-direction test by
construction even when something real and conserved drives it. The
correct test is whether the **rotation angle** between successive
current or $D_1$ vectors clusters around a fixed, non-zero value with a
consistent sense, rather than being uniformly distributed — a
precession-rate test, not a direction-repeat test.

**Recommended refinement to X35 (Direction-Bearing Recurrence Sector
Search).** In addition to X34's own proposed $\sigma$-sector search,
explicitly test for fixed-rate precession: compute the signed rotation
angle between successive directional currents (in an appropriately
chosen reference plane) at every recurrent boundary across the robust-
carrier population, and test whether its distribution clusters around a
consistent nonzero value rather than approximating uniform randomness.
In parallel, check whether the dressed carriers (58846/55584) admit an
exact, instantaneously-readable cyclic phase analogous to Rule 55744's
$\phi$, and whether that phase — rather than $D_1$'s raw direction —
is what actually persists and couples to the current. A positive result
on either test would motivate reopening Section 10.1's definition of
$\mathcal{R}$ around this variable before returning to the linear
dispersion-relation program of Section 10.2.

### 10.2x The precession-frame test confirms real structure — a diagnosis, not yet a predictive law (Stage X35)

Stage X35 ran a version of the reframing proposed in Section 10.2w
directly: rather than asking whether the current repeats direction
($J_{t+1}\approx J_t$, repeatedly negative through Stage X34), it asked
whether a recurrent carrier has an instantaneous phase whose *observed*
rotation restores coherence to the current in a co-rotating frame.

**Rule 55584 Winner 28 shows a real, well-controlled positive.** $D_1$
defines an extraordinarily planar phase ($\text{PC1}{+}\text{PC2}$
variance $0.972$). Across 47 successive recurrent-boundary pairs, this
phase persists through recurrent return at $\cos=0.502$ against a
**depth-matched** permutation null of $0.237$ ($p=0.001$) — matched by
recurrence depth specifically to rule out the confound that early
returns merely share similar starting geometry. The result survives
excluding every first return ($0.553$ vs. null $0.051$, $p=0.0008$).
The observable current, which shows only weak raw adjacent alignment
($0.348$), becomes strongly coherent once each transition is evaluated
in the frame co-rotating with $D_1$'s *observed* phase advance
($0.721$, $p=0.0004$; strengthening to $0.854$ on later returns). A
vector that appears to wander in the fixed reference frame is
substantially more coherent in the frame tracking the dressing's own
rotation — direct structural support for treating the current as a
precessing representation of a more persistent phase-bearing state,
exactly as proposed.

**The essential caveat: this is a retrospective diagnosis, not yet a
predictive law, and the two are not close to the same claim.** A model
assuming one fixed, universal rotation per step scores $0.511$ —
statistically indistinguishable from assuming no rotation at all
($0.513$). Every positive result above uses the phase advance *actually
observed* between two already-known boundaries; none of it predicts the
next phase step from the state at time $t$ alone. This is the entire
gap between "a hidden variable exists and organizes the data in
hindsight" and "that variable transports forward like momentum."

**The cross-rule comparison is honestly mixed, not uniformly positive.**
Rule 58846's apparent near-$180°$ phase step is shown, on proper
depth-matched testing, to be mostly an artifact of a shared early
boundary schedule rather than individualized memory ($p=0.657$) — though
a weaker, still-genuine current/phase coupling survives ($\cos=0.242$,
$p=0.0024$). This is the third stage in a row (after X32R and X33) in
which Rule 55584's carrier is markedly cleaner than 58846's, worth
weighing as a reason to promote it to the primary reference carrier
rather than a secondary comparison.

**Four distinct phase-like findings across this investigation should
not be conflated, and X35 is explicit about this.** Rule 55744's exact
$\mathbb{Z}_3$ tether phase (Section 10.2i), Stage X15's empirical
~$35°$ rotation step, Rule 58846's boundary-scheduled near-inversion,
and Rule 55584's noisy continuous-looking rotation are four structurally
different pieces of evidence. Retaining this distinction matters for
not overclaiming a single unified mechanism prematurely.

**Recommended next stage (X36 — Instantaneous Holonomy Generator
Search).** Search the current recurrent-boundary state (core roles,
directed interface motif, $D_1/D_2$ structure, legal-channel class,
recurrence phase, contact-role data) for an instantaneous readout
$g_t=f(\Psi_t)$ — analogous in spirit to Section 10.2k's exact
$\phi=3-n_{\min}$ — that predicts the phase step *before* the next
recurrent return occurs, then test $J_{t+1}\approx g_t J_t$ on held-out
unforced histories. This is the decisive fork: success would convert
phase precession from a retrospective structural diagnosis into a
genuine predictive momentum-transport law, arguably the most important
possible result remaining in this measurement program; failure after a
real search would leave a real but memoryless precessing dressing
variable — still a genuine discovery, but not evidence of momentum.

### 10.2y From a failed generator to an exact path-dependence proof (Stages X36–X37)

**Stage X36** searched directly for the instantaneous generator X35
called for. Coarse-state determinism fails outright: an identical
measured $(D_1,D_2,\text{legal-channel cloud})$ signature, occurring 14
times, produces phase increments ranging from $-1.744$ to $+3.030$ rad
(circular concentration only $R=0.572$) — no exact generator of this
form exists. A weaker precursor was found instead: the inter-shell twist
$\beta_t=\arg D_2-\arg D_1$, available instantaneously, has real
leave-one-trial-out predictive power (median LOTO slope $0.850$,
depth-matched $p=0.044$), and using the *predicted* (not retrospective)
phase advance still improves current transport (0.348→0.423, $p=0.038$).
Applied to Rule 58846 as a control, the same analysis gives an
apparently strong score (0.706) that depth-matched permutation shows is
entirely explained by a shared boundary schedule ($p=0.61$) — confirming
the 55584 signal is not an automatic artifact of defining $D_1/D_2$.

**Stage X37 delivers an exact, non-statistical result that reframes the
entire search.** The identical pre-contact state, hit by the identical
first contact $(208,27,218,22,132)$ (confirmed via matching radius-3/4
neighborhood hashes), returns through two different legal second events
to terminal phases of exactly $0$ and exactly $\pi$
($\cos(D_{1,A}, D_{1,B}) = -1$ to numerical precision). This is a
structural counterexample, not a hypothesis test: **$(\Psi_t, g_1)$
does not determine the terminal phase; the full ordered recovery path
does.** The correct target is therefore a path-conditioned holonomy,
$\phi_{t+1} = \mathcal{H}(\gamma_t)\,\phi_t$, where $\gamma_t$ is the
entire sequence of particle-coupled events between recurrent boundaries
— structurally the same phenomenon as a gauge connection, where parallel
transport around different paths between the same two points gives
different results.

### 10.2z An exact, compositional discrete holonomy law (Stage X38)

Restricting to the controlled shortest-return subgrammar (two ordinary
rewrites per recovery), the dressing phase collapses to an exact
$\mathbb{Z}_2$ sector: $D_1$'s variance is 100% along one axis across
361 tracked recurrent boundaries and 360 transition edges. The ordered,
ID-normalized two-event path signature predicts the sector with
leave-one-start-context-out accuracy of 99.38% (91.89% flip recall,
100% flip precision), paired against identity transport at
$p\approx1.16\times10^{-10}$. **The decisive test is compositional**:
independently predicting three successive segment updates and composing
them via $\mathbb{Z}_2$ addition gives the correct terminal sector in
**124 of 124** six-rewrite chains spanning four independently-generated
$\pi$-sector starting contexts. A separate order-reversal control
(firing the same two legal gates in the opposite order) returns to
exact recurrence in 0 of 340 tested legal-both-ways cases — event order
is not incidental, it is part of the connection itself. This is the
first stage in the entire measurement program combining recurrent
identity, an internal group-valued phase, a path-conditioned update
rule, *and* verified composition of independent predictions — materially
closer to a genuine transport variable than any fixed-vector candidate
tested in Stages X27–X34, though calling $\sigma$ physical momentum
remains premature: no relation to displacement, energy, or inertial
response has been shown, and the result is explicitly scoped to the
controlled shortest-return subgrammar (100% single-axis variance),
narrower than the natural ensemble's broader ~2D phase disk (97.2%
variance in two components, Section 10.2x).

### 10.2aa Confirmed in natural histories, then refined into a continuous winding law (Stages X39–X41)

**Stage X39 bridges the controlled result to natural scheduler
histories.** The natural phase is shown to be strongly antipodal, not
uniform ($R_2=0.79$ across 97 boundaries), splitting cleanly into
near-zero and near-$\pi$ transition classes; stripping the realized
antipodal factor raises phase coherence from 0.502 to 0.827. This
$\mathbb{Z}_2$ split agrees with an independently-derived residual
branch definition in 44 of 47 cases ($p=3.85\times10^{-7}$) — not a
relabeling of the same data, a genuine cross-check. X39 also issues an
important correction to X36: once the discrete part is properly removed,
the earlier shell-twist predictor $\beta$ no longer improves prediction
of the continuous residual — $\beta$ had been partially detecting the
discrete branch, not the residual, all along.

**Stage X40 independently reproduces this in a fresh 160-trial
ensemble** ($R_2=0.769$) and adds an exact structural result: phase
change is accumulated **entirely** during particle-coupled recovery —
zero measured drift during vacuum-only intervals between recovery and
next contact, to $10^{-16}$ precision, across an average of 10.4
vacuum-only rewrites per interval. X38's controlled flip motifs recur
as sub-path signatures inside longer natural recoveries at
significantly elevated rates ($p=0.0017$), and flip probability is
strongly associated with path length (median 4.5 contacts for no-flip
vs. 20.0 for flip, $p\approx10^{-10}$) — evidence the $\mathbb{Z}_2$
sector is a cumulative path quantity, not a one-shot bit.

**Stage X41 resolves this into the cleanest current model: an
approximately constant winding rate per particle-coupled event, not an
independent discrete-plus-continuous mechanism.** Screened at $3.909°$
per contact and frozen before testing, this simple model beats every
more elaborate local-connection model (directed role, full $D_1/D_2$,
causal-age) on independent validation (phase cosine $0.730$ vs. identity
$0.550$, trial-clustered $p\approx0.0096$). The exact $\mathbb{Z}_2$
grammar of Stage X38 is now understood as a real discrete skeleton
**inside** this richer continuous winding process, not a separate
mechanism running alongside it. **The essential limitation, unchanged by
this refinement**: even this best model does not yet improve prediction
of the external current on independent data (0.484 predicted vs. 0.550
using the realized phase) — everything established in this arc concerns
an internal phase clock, and its connection to the carrier's actual
external behavior remains the open gap.

**Recommended next stage (X42 — Phase-Clock / Winding-Rate
Discriminator).** Test whether the ~3.9°/event winding rate tracks
particle-contact count specifically or a more invariant recurrence
clock, by comparing against causal depth, constituent turnover, and
directed source-role counts, and by directly perturbing scheduler
spacing while preserving the contact sequence. If a robust rate
survives, the natural follow-up is to test whether it is
**carrier-specific**: compare 55584 Winner 28's rate against other
independently-discovered robust carriers (58846 Candidate 8, other
Stage W rules), the same way a real particle's Compton frequency is
established as physical by being reproducible and species-specific,
not merely present once.

### 10.2bb A real internal clock, no conserved momentum sector, and a deliberate program pivot (Stages X42–X45)

**Stage X42 established a genuine, well-controlled result: the internal
phase clock is dissociated from ambient time.** A matched-spacing
intervention found that inserting ordinary vacuum-only rewrites between
structurally identical particle-contact paths — varying by as much as
15x (2 vs. 32 rewrites) — does not measurably advance the phase
($d\phi/dN_{vac}=0.01°$, $p=0.92$; the ambient-clock rate falls outside
the confidence interval). The right time variable is particle-coupled
event count specifically, defining a provisional recurrence proper time
$\tau_R \equiv N_{\text{hit}}$ — not ordinary rewrite time.

**Stage X43 then tested, and rejected, the natural next hypothesis: that
the winding rate $\omega_R = \Delta\phi/N_{\text{hit}}$ is itself a
conserved momentum-like state.** The unwrapped rate is broad (mean
4.65°/hit development, 3.07°/hit validation; SD $\approx10°$), not a
sharp eigenvalue, and adjacent recovery episodes show no positive
persistence (correlation $-0.17$, $p=0.19$; ICC $\approx-0.09$). A
weaker, real, independently-replicated positive survives: the
instantaneous dressing (especially $n_1$ and $\beta$) reproducibly
ranks the *tendency* of the next rate ($\rho=0.46$, $p=0.001$ in
validation) without pinning down its magnitude ($R^2\approx0.02$–$0.05$).

**Stage X44 confirmed this is not specific to Winner 28.** Screening
all twelve robust Rule 55584 carriers plus 58846 Candidate 8, no
carrier combines low within-carrier rate dispersion with positive
episode-to-episode persistence. The single promising short-screen
candidate (carrier 22) reverses sign after proper unwrapped replay
($r=-0.236$). **Scheduler-robust recurrence does not imply persistent
winding rate, anywhere in the tested population.**

**Stage X45 closed off the natural retreat — coarser conserved
quotients of the holonomy — with a comprehensive, pre-registered
negative.** Harmonics $m=1$–$6$, conjugacy classes, nearest-$\mathbb{Z}_m$
sectors, orientation sign, and winding class were all tested against
carrier-matched shuffled controls; none replicated. The one nominal
population-screen candidate (carrier 22, $m=4$) failed independent
validation after being frozen before inspection ($\Delta C_4=+0.042$,
$p=0.264$). **No replicated conserved holonomy sector, of any tested
form, survives from one recurrence episode to the next.**

**This does not undo Stages X37–X41.** The path-dependent, compositional
phase law and the dissociation from ambient time remain real, exact, and
independently confirmed results. What X42–X45 establish is narrower and
important in its own right: whatever holonomy is generated during one
recovery episode is *reselected* by the new dressed state at the next
episode, not *transported unchanged*. A legitimate next test — whether
apparently different holonomies become equivalent after a state-
dependent frame transport, $g_{t+1}$ vs. $U(\Psi_t\to\Psi_{t+1})\,g_t\,U^{-1}$
— remains open and unexhausted (X45's own proposed next step).

**Deliberate program pivot, recorded explicitly here rather than left
implicit.** Six consecutive momentum-program stages (X40–X45) have now
returned a comprehensive negative on conserved holonomy structure, on
top of the already-long momentum thread beginning at Stage X13. Section
10.1's rest recurrence energy $\mathcal{R}$, proposed before Stage X1
and never seriously attempted, has had no comparable investment despite
now having exhaustively-characterized carriers and a mature validation
toolkit available for the first time. Rather than continue directly
into the covariant-transport test, the measurement program is
deliberately paused here on momentum and redirected at $\mathcal{R}$,
tracked as a new **Y-series** of stages. This is not an abandonment of
the momentum thread — the covariant-transport question and a possible
broader rule search both remain queued — but a considered choice to
pursue a structurally different, currently untested axis before adding
further refinement to an already heavily-worked one. A clear result on
$\mathcal{R}$, positive or negative, will also inform whether Rule
55584/58846 are worth continuing to refine at all, independent of
momentum.

### 10.3 Vacuum backreaction and the equivalence-principle test

Only after $m_i$ is established for at least one defect should the
gravitational side be reopened. The defect's presence should be checked
against independent far-field observables of the surrounding vacuum —
propagation delay, shortest-path geometry, local causal growth rate, or a
geodesic-like deflection of nearby trajectories — defining a gravitational
source strength $m_g$ from the defect's recurrence energy or stress,
rather than from any separately-posited charge. The critical target,
unchanged since Section 1 and now stated in terms this framework can
actually measure, is

$$
m_g \propto m_i
$$

**checked across multiple distinct recurrent defects, without tuning.** A
single defect satisfying this proportionality would be suggestive; only
comparison across defects of different size, period, or construction
would constitute the first genuine test of an emergent equivalence
principle in this framework.

---


## Appendix C — Momentum-program-specific formulas

*(Continues Appendix A of the main document, which retains the
foundational rule and capacity-theory statements referenced by Section 8.
The four laws below are specific to the tether/momentum investigation and
are not referenced outside this document.)*

$$
\textbf{Exact tether-depth law (Stage X18; resolves the X4 extrusion coordinate } h\text{):}\quad
h(t) = d_{\text{old}}(t) - 1
$$

$$
\textbf{Tether-front phase transition law (Stage X19; }\phi=N_A\bmod3\text{):}\quad
\phi_{t+1} = (\phi_t + I_A)\bmod 3, \qquad h_{t+1} = h_t + I_A \cdot I_{\phi_t=2}
$$

$$
\textbf{Instantaneous phase localization (Stage X20A):}\quad
\phi = 3 - n_{\min}, \qquad Q_{\text{tether}} = h + \frac{3-n_{\min}}{3} = \frac{N_A}{3}
$$

$$
\textbf{Causal ratchet path length (Stage X22; outward-positive subclass only):}\quad
\tau_{\text{path}} = 3h + \phi - 1 = N_A - 1
$$

$$
\textbf{Persistent-ladder criterion (Stage X23; pre-registered, validated 124/124 across three vacuum ages):}\quad
\text{persistent} \iff [\,N_{\text{ext}}(N_A{=}2)=1\,] \wedge [\,h{=}1 \text{ launch has a 2-descendant receiver path}\,]
$$

$$
\textbf{Bridge-role descent lemma (Stage X24; exact, proven from Rule 55744's grammar, } u<v \text{ required):}\quad
O_4 \to I_4 \ \Rightarrow\ v_{t+1} = u_t < v_t
$$

$$
\textbf{Birth-order symmetrization result (Stage X25; the X24 lemma's premise removed):}\quad
u<v \text{ not enforced} \ \Rightarrow\ O_4\to I_4 \text{ bidirectional (33 decrease / 50 increase, no preference)}
$$

$$
\textbf{Localized residual mechanism (Stage X26):}\quad
\text{output-source symmetrization: no change (0/47)}\ ;\quad
\text{old-substrate source-undirection: reciprocity restored (2/47)}
$$

$$
\textbf{Path-dependence counterexample (Stage X37, exact):}\quad
(\Psi_t, g_1)\ \text{identical}\ \Rightarrow\ \Delta\phi \in \{0,\pi\}\ \text{depending on }g_2
$$

$$
\textbf{Discrete holonomy composition law (Stage X38):}\quad
\sigma_{t+1} = \sigma_t \oplus \delta\sigma_t(\Gamma_t),\qquad \Gamma_t = (g_1,g_2),\ \delta\sigma_t\in\mathbb{Z}_2
$$

$$
\textbf{Natural phase decomposition (Stage X39):}\quad
\Delta\phi_t = \pi\,\delta\sigma_t + \theta_t \pmod{2\pi}
$$

$$
\textbf{Constant winding-rate model (Stage X41, best-validated):}\quad
\Delta\phi_\gamma \approx N_{\text{hit}}\cdot\delta\phi_0,\qquad \delta\phi_0 \approx 3.91°\ \text{per particle-coupled event}
$$

$$
\textbf{Two-anchor zero-drift theorem (Stage Y30):}\quad
\Delta X_T = 0 \text{ (translation-covariant recurrence)} \ \Rightarrow\ \{a,b\}_{t+P} = \{a,b\}_t \ \ (P\ge3)
$$

$$
\textbf{Persistent-anchor wake lemma (Stage Y28):}\quad
\text{retired fresh vertex} \notin \text{current support} \ \Rightarrow\ \text{its anchor-attached relations are absorbing under the selected rest law}
$$

$$
\textbf{Exact wake-neutral soliton pair (Stages Y36--Y37):}\quad
v_s=\pm0.25 \text{ site/event}:\ \Delta H_{\text{local}}=0,\ H_{\text{local}}=53,\ \Delta N_{\text{global}}=+22\text{/period (both signs)}
$$

$$
\textbf{Reversal-interface no-go, within the frozen soliton family (Stage Y38):}\quad
\Delta X_T=0 \ \Rightarrow\ \Delta H_{\text{local}}\ge+12\text{/8-event period}
$$

$$
\textbf{Universal reversal-source cardinality (Stages Y40--Y41):}\quad
\Delta H_{\text{reversal}}=+6,\ \ |v|=0.25,1,2\ \text{(magnitude-independent, decomposes into two }+3\text{ halves)}
$$

$$
\textbf{FBCL stationary rest closure (Stage Y46):}\quad
\Delta X_T=0,\ \ \Delta H_{\text{local}}=0,\ \ 7\text{ relations in}=7\text{ relations out per proper period}
$$

$$
\textbf{First positive finite inertial curvature (Stage Y47, frozen Y26 observable):}\quad
A(0)=\tfrac34\ln2,\ \ A(\pm v_1)=A(\pm v_2)=\ln2,\ \ M_i=\tfrac58\ln2\approx0.4332>0
$$

$$
\textbf{CD001 turnaround-memory growth law (Stage Y59, linear through 8 reversals):}\quad
T_n^{(\pm)}=54n+\{9,11\},\ \ P_n^{(\pm)}=24n+\{1,8\},\ \ \text{first reversal-count-sensitive at relation-hop }8
$$

$$
\textbf{Finite single-trail geometry and return-coupling law (Stage Y62):}\quad
L^{(+)}=72\ (k{=}4..75),\ \ L^{(-)}=74\ (k{=}4..77),\ \ D_{\text{contact}}=L_{\text{trail}}+8,\ \ \Delta H = r_{\text{hist,perm}}-r_{\text{fresh,perm}}
$$

$$
\textbf{Turnaround-delay additivity (Stage Y63, exact, 32/32):}\quad
\Delta H_n = \textstyle\sum_{i=1}^{n} P^{(s_i)},\ \ P_+=52,\ \ P_-=56;\ \ \text{spatial linear superposition falsified}
$$

$$
\textbf{Asymmetric active-interaction corridor (Stage Y64):}\quad
\text{exit edge}+30,\ \ \text{entry edge (inactive extension)}+19,\ \ D_{\text{contact}}=L_{\text{active}}+8\ \text{(exact, 32/32)}
$$

$$
\textbf{Independent-probe read law (Stage Y65):}\quad
\text{third-party diff duration}=L_{\text{trail}}+8\ \text{exactly; zero target-specific rewrite (0/32); no universal }52/56\text{ transfer}
$$

$$
\textbf{Environmental-memory unification (Stage Y71, exact, 32/32):}\quad
L_{\text{gauge}}=L_{\text{isolated,current}}+\Delta H,\ \ \Delta L_{\text{corridor}}=\Delta H_{\text{renewal}};\ \ \text{forced dwell alone reproduces the spatial support (16/16)}
$$

$$
\textbf{Composite bond-motif compositionality (Stage Y77):}\quad
\text{cross-relations}(T3R_{XY}) = \text{cross-relations}(D2R_X)+\text{cross-relations}(D2R_Y);\ \ N{=}2\!:3\text{ species},\ N{=}3\!:6\text{ species}
$$

$$
\textbf{Speed-dependent bond structure (Stages Y77–Y79, exact across }0,\pm v_1,\pm v_2\textbf{):}\quad
\text{R5}: 4\to4\to4\ \text{(speed-invariant)};\quad
\text{R6}: 3\to1\to1\ \text{(reduces at }|v|{\le}1\text{)}
$$

$$
\textbf{Population extensive inertial curvature (Stage Y81, exact, 8/8 identities):}\quad
M_i^{\text{ext}}(N) = N\cdot\tfrac58\ln2,\ \ \beta_4^{\text{ext}}(N) = -N\cdot\tfrac1{16}\ln2;\ \ M_i(\text{composite})-N\,M_i(\text{DS001})=0
$$

$$
\textbf{Recurrence-energy nonportability (Stage Y82):}\quad
0/1920\ \text{off-manifold recoveries};\ \ \mathcal{R}_{\text{act}},E_0,\alpha\ \text{undefined — untested, not falsified}
$$

$$
\textbf{Y84 recurrence-energy degeneracy (exact, not statistical):}\quad
q_\infty=\tfrac12,\ \ell_0=0,\ \ \omega_{\text{renew}}(\text{DS001})\ \text{undefined},\ \ E_0(\text{composite})=2\pi\ \text{(algebraic identity, not a measurement)}
$$

$$
\textbf{Single-event perturbation exhaustion (Stage Y85, exact, 0 exceptions):}\quad
\text{carrier-touching}\to\{\text{exact return},\text{immediate loss}\};\quad
\text{carrier-disjoint}\to\text{zero-work spectator (496/496)}
$$

$$
\textbf{Vacuum-mediated reachability (Stage Y86, bounded):}\quad
0\ \text{inward/"bad" gates through depth 14}\ (528{,}091\text{ states},\ 662{,}627\text{ transitions});\ \ \text{all-depth theorem NOT established}
$$

$$
\textbf{On-manifold rest-content candidates (Stage Y88, exact, 6/6 compositionality):}\quad
E_{0,A}=6N\ln2\ \text{(topology-blind)};\quad
E_{0,B}=H_{\rm joint}^{(R1)}\ \text{(topology-sensitive: }\Delta=3,5,14,16,31,31,33)
$$

$$
\textbf{Y89 proportionality split:}\quad
M_i=\tfrac5{48}E_{0,A}\ \text{(exact, but algebraically degenerate — same }N\text{-law shape)};\quad
M_i=\alpha E_{0,B}\ \text{FAILS (}\Delta M_i{=}0\ \text{vs. nonzero }\Delta E_{0,B})
$$

$$
\textbf{Y92 relaxation clocks (exact, population-wide):}\quad
L_{\rm life}=2,\ L_{\rm speed}=3;\ \
L_{\rm full}^{v_1\to v_2}=3N{-}1,\ \
L_{\rm full}^{v_2\to v_1}=6N{-}5\ (\text{R5 present})\ /\ 6N{-}4\ (\text{all-R6})
$$

$$
\textbf{Closed-loop transient wake (Stages Y93–Y94, exact, population-wide):}\quad
\Delta_{\rm rel}(0)=9N^2\ \text{(collective one-body, not pair-touch)};\ \
R_{\rm close}=15+3N;\ \ B_0(j)=6N+3+6j
$$

$$
\textbf{Period-boundary causal-edge flux (Stage Y95, exact, 30/30 contexts):}\quad
E1_{\rm recurrent}=4N,\ \ E1_{\rm mult}=5N,\ \ E2\equiv0\ \text{(bond-blind at this cut)}
$$

$$
\textbf{R5 phase-localized causal excess (Stage Y95, exact, 30/30):}\quad
E1(\phi,N)=N f(\phi) + \mathbf{1}_{\phi=e3}+\mathbf{1}_{\phi=h1\_bridge}\ \text{(one R5 bond)};\ \
f(\phi)=(4,4,2,1,1,2,2,1,1,2,4)
$$

$$
\textbf{Cycle-integrated causal-flux holdout law (Stage Y97, exact, 8/8 holdout contexts):}\quad
\mathcal{F}=20N,\ \ \Delta\mathcal{F}=+2\ \text{per one-R5 topology (position-independent, N=5)};\ \
\text{per-bond additivity UNRESOLVED}
$$

$$
\textbf{Promoted causal rest-content law (Stage Y99, exact, 22/22, additivity confirmed):}\quad
\mathcal{F}=20N+2n_{R5};\ \ H_{\rm add}\ \text{22/22 PASS},\ \ H_{\rm sat}\ \text{0/22 PASS}
$$

$$
\textbf{G6/G7 structural contradiction (Stage Y100, exact):}\quad
M_i=N\cdot\tfrac58\ln2\ (\Delta M_i\equiv0)\ \ \text{vs.}\ \ \mathcal{F}=20N+2n_{R5}\ (\Delta\mathcal{F}=2n_{R5});\ \
M_i=\alpha\mathcal{F}\ \textbf{FAILS STRUCTURALLY}
$$

$$
\textbf{Causal momentum/clock candidates (Stages Y101–Y104, all exact, all topology-blind):}\quad
P_{\rm edge}({\rm rest})=\tfrac52N\sigma\ (\text{NOT\_MOMENTUM});\ \
K_{\rm ext}=Nv,\ M_K=N\ (\Delta M_K\equiv0);\ \
C_{\rm move}=1,\ C_{\rm rest}=10,\ M_\tau=N\ (\Delta M_\tau\equiv0)
$$

$$
\textbf{Boost transport and relaxation (Stage Y105, exact, 240/240 legal launches):}\quad
\text{cross-constituent causal dependency}\equiv0;\ \
L_{v_2}(n_{R5})=17{-}\lfloor n_{R5}/2\rfloor,\,19{-}\lfloor n_{R5}/2\rfloor,\,19{-}\lceil n_{R5}/2\rceil
$$

$$
\textbf{Closed triangular composite census (Stage Y106, 13{,}632 new cases):}\quad
\text{CLOSED }K_3 = 0;\ \ \text{consistent pattern: } AB+BC+\text{attempted }CA \to AB+BC
$$

$$
\textbf{Triangle non-renewal mechanism (Stage Y107, exact, 624/624):}\quad
\text{causal-order violations}=0;\ \ \text{A-C MOVE renewal}=0;\ \ L_{AC}({\rm R5})=2,\ L_{AC}({\rm R6,R7})=1;\ \ R_{AC}=11\text{–}14 \gg R_{\rm bonded}\le7
$$

$$
\textbf{State-function branch test (Stage Y108, exact, 42/42):}\quad
C_{\rm REST}=2N+n_{R5},\ \ C_{v_1}=C_{v_2}=2N;\ \
S(k)=k\mathcal{F}_1\ \text{(linear action accumulation, not a conserved state quantity)}
$$

$$
\textbf{State-defined candidate-family null (Stage Y109):}\quad
H_{\rm joint}(\text{DS001}):47\to120\ \text{across one cycle (not conserved)};\ \
H_{\rm cross}=4n_5+n_6\ (\text{ordinary}),\ 4n_5+2n_6\ (e0,e4)
$$

$$
\textbf{Substrate wake-production law (Stages Y110–Y111, exact, 20/20, survives vacuum subtraction):}\quad
\Delta J_1=\Delta X_1=5N-n_{R5},\ \ \Delta J_2=\Delta X_2=22N-n_{R5},\ \ \Delta(J_2{-}J_1)=17N
$$

$$
\textbf{Vacuum-subtracted canonical excess (Stage Y111, exact, 20/20, non-extensive):}\quad
X_0({\rm start})=X_G({\rm start})=3N^2-1+n_{R5}
$$

$$
\textbf{Grammar-derived exact conservation laws (Stage Y112, 824/824 transitions, topology-blind):}\quad
I_{\rm out}=R_{CO,COCO}+R_{CO,COO}+R_{CO,OO}=8N;\ \
I_{\rm in}=2R_{CO,COCO}+R_{CO,COO}+2R_{O,COCO}+R_{O,COO}=16N=2I_{\rm out}
$$

$$
\textbf{Provenance-resolved bond-content candidate (Stage Y113, exact, 396/396, frozen for blind Y114 validation):}\quad
I_{\rm bond}=P_{O1,T2}+P_{O3,T2}=n_{R6}+3n_{R5};\ \ P_{O1,T2}=P_{O7,T2}
$$

$$
\textbf{Kinematic cross-scaffold law (Stage Y114, exact, 608/608 moving + 440/440 unused-holdout rest):}\quad
I_{\rm scaffold}=3n_{R5}+c_6 n_{R6},\ \ c_6=1\ (\text{rest},v_1),\ \ c_6=2\ (v_2)
$$

$$
\textbf{Incidence-current law (Stage Y115, exact, 16/16 species/context rows, N=2..5):}\quad
J_{\rm in}=2(N-1),\ \ J_{\rm out}=2(N-1)-n_{R6},\ \ B=D=0,\ \ \Delta I_{\rm scaffold}=J_{\rm in}-J_{\rm out}=n_{R6}
$$

$$
\textbf{Sector-dependent constitutive current law (Stage Y116, exact, 304/304 v1 + 304/304 v2, }M{=}N{-}1\textbf{):}\quad
J_{\rm rest/v1}=2M-n_{R6}=2n_{R5}+n_{R6};\ \ J_{v2}=2M=2n_{R5}+2n_{R6}
$$

$$
\textbf{Bond-local transfer law (Stage Y117, exact, position/neighbor-independent, 1596/1596):}\quad
(I_5,J_5)=(3,2)\ \text{always};\quad (I_6,J_6)=(1,1)\ (\text{rest},v_1)\ \to\ (2,2)\ (v_2)
$$

$$
\textbf{Causal-role relay automaton (Stages Y118–Y119, exact, on-manifold):}\quad
S{=}(n_X,n_W);\ \ R5{=}(1,2);\ \ R6_L{\in}\{(1,0),(0,1)\};\ \ R6_H{=}(1,1);\ \ q_6=\mathbf1[n_X{>}0\wedge n_W{>}0]
$$

$$
\textbf{Geometric coordination bound (Stages Y121–Y122, exact, graph-local):}\quad
z_{\max}=2;\ \ \text{robust contacts}=\{-6,-5,+5,+6\};\ \ \text{compatibility graph}=K_{2,2}
$$

$$
\textbf{Explicit local contact state (Stages Y124–Y126, exact, hash-free, 152/152):}\quad
\Sigma=(\xi,A,B);\ \ A=N_C^{(2,1)},\ \ B=N_Q^{(1,1)};\ \ \xi=\text{producer-spine phase}
$$

$$
\textbf{Recurrent producer spine (Stage Y125, exact, 1799/1799):}\quad
w(E_n)=v(E_{n+1});\ \ \text{gate-ancestry lag stencil}=(3,5,2,4,1)
$$

$$
\textbf{Phase-portability failure (Stage Y127, exact):}\quad
\Sigma_{157}\ne\Sigma_{\rm mature}\ \text{(section-dependent, 0/16 unchanged predictions)}
$$

$$
\textbf{Receding wake-fossil locality law (Stage Y129, exact, 400/400):}\quad
R_{\max}(r)=3+\lceil r/3\rceil\ \text{(}r{=}0..24\text{)};\ \ \text{no fixed-radius intrinsic state exists}
$$

$$
\textbf{Formation-memory shedding and causal decoupling (Stages Y130–Y131, exact):}\quad
\text{constitutive future: history-independent from section 0 (384/384)};\ \
\text{fossil deletion: 0 effect (416/416, 384/384)};\ \
\text{exterior cut: real, delayed backreaction}
$$

$$
\textbf{Worldline supply-encounter law (Stage Y132, exact, 2,880/2,880 kinematics intact):}\quad
\text{first-failure signature: } J_{\rm in}<2,\ J_{\rm out}=2,\ B{=}D{=}0;\ \
\text{missing relations at dist. }R{+}1\text{, already absent at }t{=}0
$$

$$
\textbf{Sector-dependent supply architecture (Stage Y133, exact):}\quad
\text{moving }v_1,v_2:\text{ worldline recruitment};\ \ \text{rest: cyclic radius-1 reservoir},\ \ U_{\rm rest}=11n_{R5}+7n_{R6}
$$

$$
\textbf{Reservoir conversion / R6 boost mechanism (Stage Y134, exact, 1,440/1,440):}\quad
\text{R6 rest}\to v_2: \text{r2 V-O1}\to\text{r3 +C-O3}\ (I_6{:}1{\to}2);\ \ \text{rest pool exhausted by round 5}
$$

$$
\textbf{Selector/scaffold causal independence (Stage Y135, exact, 576/576 + 224/224):}\quad
\text{scaffold fully deleted (}I{=}J_{\rm in}{=}J_{\rm out}{=}0\text{)}\ \Rightarrow\ \text{gate/displacement still exact}
$$

$$
\textbf{Native selector architecture, Y136–Y141 (exact, complete-manifold):}\quad
\text{no native competition (Y136–Y137)} \to
\sigma{=}1(v_1)/2(v_2)\text{ memory, no actuation (Y138–Y139)} \to
\text{NST1F/ANST1F: 180/180, 60/60 closed}
$$

$$
\textbf{Covariance closure, Y142–Y143 (exact):}\quad
\text{IGR1 relay: } 11{,}520/11{,}520\text{ relabel-covariant (old formula: }2/11{,}520\text{)};\ \
\text{vacuum/moving unchanged}; \ \text{rest: 22 hidden branches exposed}
$$

$$
\textbf{Rest-marker repair and phase clock, Y144–Y145 (exact):}\quad
\text{RST1 removes 22/22 branches, 0 new};\ \
\text{launch settling: }v_1{=}2\text{ rounds }(\tfrac12s,\tfrac32s),\ v_2{=}1\text{ round }(\tfrac12s);\ \
\text{phase clock found, 44/44 destructive competitor}
$$

$$
\textbf{Autonomous rest engine closure, Y146–Y148 (exact, 640/640 periods, engine frozen):}\quad
\text{atomic successor removes rival } (352/352);\ \
\text{PRV2 Y33-inert (proof)};\ \
\text{zero token accumulation}; \ \text{560/560 relabel-covariant}
$$

$$
\textbf{Post-freeze G6/G7 reconfirmation (Stage Y149, exact):}\quad
M_i=N\cdot\tfrac58\ln2\ (\Delta M_i\equiv0);\ \ E_{0,A}=6N\ln2\ (\text{circular});\ \
B_{\rm proj}=B_{Y88}+N;\ \ \Delta B\ \text{unchanged} \Rightarrow M_i=\alpha B\ \textbf{FAILS}
$$

$$
\textbf{Bond-local transition response and same-}N\textbf{ contrast law (Stages Y150–Y151, exact, blind-validated):}\quad
M_{\rm cross}=-20n_{R5}+\tfrac{11}{8}n_{R6};\ \
\Delta M_{\rm cross}=\tfrac{171}{16}\Delta B_{\rm proj}=-\tfrac{171}{16}\Delta\mathcal{F}_{\rm flux}
$$

$$
\textbf{Positive transition action, closure incomplete (Stage Y152, exact):}\quad
M_{\rm loop}=18n_{R5}+\tfrac{131}{24}n_{R6};\ \ v_1{\to}{\rm rest}\ \text{R5-only closes (4/4)};\ \ v_2{\to}{\rm rest}\ \text{closes for }\textbf{0}\text{ species}
$$

$$
\textbf{Autonomous admissible-path action, validated blind on N=5 (Stages Y153–Y154, exact, 44/44):}\quad
M_{\rm adm}=\tfrac{199}{24}(N{-}1)+\tfrac{277}{24}n_{R5};\ \
\text{admissible loop: }0\to v_1\to0\ \text{and}\ 0\to v_2\to v_1\to0\ \text{only}
$$

$$
\textbf{Landmark: exact same-}N\textbf{ topology-contrast law (Stage Y155, 38/38 pairwise, one calibration point):}\quad
\Delta M_{\rm adm}=\tfrac{277}{48}\Delta\mathcal{F}_{\rm flux}=-\tfrac{277}{48}\Delta B_{\rm proj};\ \
\Delta M_i^{Y81}\equiv0\ \text{(fails all 38)}
$$

$$
\textbf{Channel-migration accounting identity, disproving current-incidence decomposition (Stage Y156, exact):}\quad
\textstyle\sum_c|C_c(t)\triangle C_c(t{+}1)|=|H(t)\triangle H(t{+}1)|+2m_t
$$

$$
\textbf{Reinterpretation: strict producer-owned bond action is zero (Stage Y158, 8/8):}\quad
A_{\rm BOND}^{\rm producer}\equiv0\ \text{(R5 and R6)};\ \
\text{Y154/Y155 signal} = \text{environmental relay incidence dressing, not bond birth/death}
$$

$$
\textbf{Two-channel causal split (Stage Y159, exact):}\quad
\text{PAIR\_ENV\_RELAY: not causal, }0/56\text{ selection changes};\ \
\text{SECTOR\_ENV: causal, }88/88\text{ reclassify, 1-round displacement lag}
$$

$$
\textbf{Landmark: pure environmental deletion causes autonomous acceleration (Stage Y160, exact, 28/28, 0 external command):}\quad
|v|:\,1\to\tfrac32\to2\ \text{via }2N\text{ deletions};\ \ v_2\text{ self-maintains rounds 3–16 (392/392)}
$$

$$
\textbf{Third autonomous speed structure and asymmetric reverse control (Stages Y161–Y162, exact):}\quad
|v|=\tfrac32\text{ period-2 confirmed 16/16, 128 rounds};\ \
2\to\tfrac32\to1\text{ works }4/4\text{ (+ dir)},\ \text{fails structurally }4/4\text{ (}-\text{ dir)}
$$

$$
\textbf{Reversible two-speed control (Stage Y163, exact):}\quad
\text{occupancy-guarded }E\text{: D2 }8/8,\ \text{T3/T4 }20/20,\ \text{N5 }44/44\ (176/176\text{ legs});\ \
t_{\rm first}=24+n_{R6}\ \text{(predicted, 44/44)}
$$

$$
\textbf{Partner-dependent trailing-carrier response (Stage Y165 D3-5, exact):}\quad
d{=}20:\ 4/4\text{ each of 4 contexts, solos }0/32;\ \ \text{partner-relation necessity }59/59
$$

$$
\textbf{Persistent wake (Stage Y165 D3-6, exact):}\quad
\text{PF }24/24,\ \text{solo controls }0/96;\ \ \text{pre-receiver ancestry necessary }41/41;\ \ \text{wake at }5\text{–}9\text{ graph steps behind source}
$$

$$
\textbf{Causal-role coupling (Stage Y165 D3-7, exact):}\quad
\text{persistence }143/143;\ \text{head-on pre-contact response }0/32;\ \text{new-event arrival }0/413;\ \
\text{invariant: availability of receiver's }v_1\text{ source role (additive or subtractive)}
$$

$$
\textbf{Origin localization outcome (Stage Y165 D3-7H–M):}\quad
A{=}T\ 8/8;\ \text{conservation }0/16;\ \text{closed cycles }0/8;\ \text{fossil, R8 excess, R8 deficit all dispensable};\ \
\text{common global gates pair vs solo }0/8
$$

$$
\textbf{Prospective worldline encounter (Stage Y165 D3-7O, exact):}\quad
(k,x,T)_{\rm clamp}=(k,x,T)_{\rm native}=(k,x,T)_{\rm geom}\ \ 8/8;\ \ +{:}\ (6,1295.5,-1);\ -{:}\ (3,1255.0,+1)\text{ or }(5,1252.0,+1)
$$

## Appendix D — Key numerical results, Stages X1–X45, Y1–Y165 (pilot)

*(Continues Appendix B of the main document, which covers results through
Stage W / rule 55744's discovery. Everything below is specific to the
momentum and mass measurement program.)*

| Result | Value |
|---|---|
| Rule 55744: displacement law (forced internal, 100 trials) | $D_{\min}=\lfloor N_A/3\rfloor$ exact, 0/100 deviations |
| Rule 55744: X2B background-drift control (5 trials) | exactly 0 A/C mismatch; displacement persisted regardless |
| Rule 55744: X3 ordinary-producer attractor census | 186/186 absorbed into particle SCC within 2 steps |
| Rule 55744: X3 matched-worldline pair law (168 checkpoints) | exact, 0 deviations; C+C pairs: constant distance |
| Rule 55744: X4 directionality test (23 configurations) | $\Delta x=0$, $\Delta h=$const, exactly, 0 exceptions — extrusion, not translation |
| Rule 55744: X5 halo decoupling (repeated-cycle floor) | A: 1 external gate / 24 relations; C: grows monotonically |
| Rule 55744: X5 branch-choice bias after halo divergence | exactly 50/50 A vs. C (2,319/2,319 direct contacts stay phase B) |
| Rule 55744: X5 directional relocation signature (168 anchor comparisons) | 0 became closer; no momentum signature found |
| X6: Stage W branching alternatives screened / with directional velocity | 5 / 0 (all bounded O(1) offset + scalar extrusion) |
| X7: Rule 54567 conditional glider, two-rail test (30 shifts) | $(d_L,d_R)=(0,17)$ vs. $(17,0)$ — exact directional signature |
| X7: Rule 54567 natural translating-frontier occurrences | 0/21 exact; best natural match 2/4 required relations |
| X7: closure audit, matched rail (399 touching actions) | 399/399 immediate particle survival, 0 losses |
| X8: full-turnover boundary self-loop operator census | 635 operators across 80 rules |
| X8: no-unseen-frontier lemma | exact, proven from output-grammar locality |
| X8: rule 52300 natural same-phase chain | causal-depth audit: ancestral descent, not translation |
| X9: two-ambient active-lookahead screen (all 80 rules) | 0 particle-preserving edges with $e,w\in C', f\notin C'$ |
| X9: fresh-$w$-excluding one-step transfers / compatible handoffs | 3,014,324 / 14 (in 4 of 80 rules) |
| X9: repeatable handoff cycles found | 0; max successive events = 2, all compatibility graphs acyclic |
| X10: single-scalar capacity conjecture | falsified exactly; Rule 55744's own transitions are the counterexample |
| X10: old-handle non-creation theorem | proven; subsumes zero-incidence absorption and no-unseen-frontier lemma |
| X10: repair vs. frontier capacity-hierarchy match | repair 58/28/6→0/0/2; frontier 38/31/11→0/0/4, 0 cycles among the 4 |
| X11: formal six-node extended cycles (10 rules) / non-ancestral eventual-turnover | 777 / 371, all 10 rules represented |
| X11: false-positive removal via access/connectedness pruning | 127 valid cycles remain; min. interface rises to 2 relations in every rule |
| X11: rule 59436 conditional cycle validation | 40/40 exact; full turnover in 3 shifts; 1 gate w/ frontier, 0 without |
| X11: rule 55744 four-event extended orbit validation | 40/40 exact; not yet universally closed |
| X11: single-event interface priming test (10 rules) | 0/10 |
| X11: natural occurrence of rule 59436 translating motif | 0/12,000 sampled vacuum events |
| X11: rule 59436 vs. 55744 local dimension estimate | ≈2.86 vs. ≈4.6 |
| X12: rule 76073 raw interface motif abundance | up to 1,582 occurrences / 900 vacuum events |
| X12: natural triggering of extended recurrence (76073, 2 seeds) | 102 and 111 exact one-period hits |
| X12: natural triggering of extended recurrence (58846, 2 seeds) | 63 and 18 exact one-period hits |
| X12: renewable (non-ancestral) second handoff | 0/194 tested cases; all available second contacts rank-0 |
| X13: contact-mediated exact recurrence periods (rule 58846) | 6 consecutive, 0 legal internal gates at every boundary |
| X13: directionality test (741 geodesic pairs) | 0 persistent-sign; 669 show reversal; mean correlation ≈ −0.76 |
| X14: contact current $J$ vs. position $V$ persistence | $J\approx+0.27$; $V\approx-0.55$ (temporal order confirmed, $p\approx0.017$) |
| X14: dressing vector $M$, raw vs. background-controlled | raw ≈0.73; vs. 20-state null ≈0.61 (not distinct); residual ≈0.15 |
| X14: cycle-phase support ambiguity (representative case) | 11 transient supports ($\log_2 11\approx3.46$ bits) → 1 final state |
| X14: 12-period current-preserving channel, X4 test | 0/2,145 persistent-sign geodesic pairs; local contact/step agreement 98.6% |
| X15: fixed-axis (vs. rotating) momentum criterion | max 2 regenerated periods (primary), 1 (alternate) |
| X15: apparent 9-period locally-coherent chain, true angular drift | 90–126° from original axis by period 2 |
| X15: uncertainty-relation test | falsified in simplest form: $H(C_2\mid S_{\text{transient}})=0$ |
| X15: angular-current PCA (unconfirmed anomaly) | 82.1% variance in 2 components; ≈290° net rotation, 7/8 same-sense |
| X17: far-field (radius 4) axis vs. background control | particle ≈0.86; unrelated background ≈0.999997 — not distinct |
| X17: short-range predictive dressing excess over background (r=1, r=2) | +0.535 (p≈0.0016) and +0.483 (p≈0.003); gone by r=3–4 |
| X18: exact tether-depth law, $h=d_{\text{old}}-1$ | 728/728 checkpoints, zero exceptions |
| X18: modular shell-repeat law ($N_A\to N_A+3$) | 96/96 exact |
| X18: raw causal time vs. $h$ | both A and C advance depth at 2.0/cycle; only $h$(A) changes — falsified |
| X18: raw shared-ancestry amount vs. $h$ (cycle 12) | A: 21, C: 22 shared ancestors, despite $h=4$ vs. $h=0$ — falsified |
| X18: A-selective causal-coherence clock (post-decoupling) | A: mean +4.17 deepest-common-depth per event; C: exactly 0 |
| X19: rule 55744, $h$+action alone vs. $h+\phi$+action (held-out) | 83.33% vs. 100% (0/288 errors) |
| X19: rule 58846, previous-current vs. LOO composite predictor | mean cosine 0.620 vs. 0.745 ($p=0.03125$); transfer 9/11 ($p=0.0327$) |
| X19: massless triangle, X4-style displacement (30 events) | $\Delta x=0$ exactly; off-axis remainder $+10$ — same signature as rule 55744 |
| X20A: instantaneous phase law $\phi=3-n_{\min}$, $Q_{\text{tether}}=N_A/3$ | 738/738 checkpoints exact, 42 supports, 8 vacua |
| X20A: repeated local neighborhood under $h\to h+1$ (radius 1 / radius 2) | 84/84 and 48/48 exact isomorphisms |
| X20B: matched-$h$ challenge outcomes (5 challenge families) | 1,728/1,728 identical at $h=1,2,3$ — falsifies $h$ as local energy/mass |
| X21: native boundary-gate grammar, exact equality across $h=1,2,3$ | 12/12 matched cases, mean Jaccard 1.000 |
| X21: causal-cone structure invariance across $h$ (depth 4, extended to 6–7) | 144/144 identical; 0 particle contacts throughout |
| X21: full old-boundary disconnection, recurrence continuation | 72/72 six-cycle successes even when fully cut off |
| X22: core-originated outward causal cones reaching old boundary | 0/54 |
| X22: dressing-originated causal ratchet (matched support/h/phi tests) | 63/423 (14.89%); 7/47 supports positive at all 9 tested states |
| X22: reverse (inward) control on outward-positive supports | 0/21 and 0/47 particle contacts |
| X23: broader forward-channel supports (development + prospective) | 20/47 (42.55%) and 15/48 (31.25%); combined 35/95 (36.84%) |
| X23: forward mutual information / channel capacity (launch vs. control) | $I\approx0.099$ bits; $C\approx0.104$ bits; $P(\text{contact}\mid\text{launch})=0.183$ vs. $0$ for controls |
| X23: persistent-ladder criterion, prospective out-of-sample test | 48/48 correct, 6 new positives, $p=8.15\times10^{-8}$; combined 95/95 |
| X23: witness path-length law across all successful states | 117/117 exact, zero deviations |
| X24: bridge-role descent lemma, ladder link audit | 117/117 exact $O_4\to I_4$ transports, zero exceptions |
| X24: live global-scheduler activation (350 trials) | 25/350 (7.14%) overall; 25/123 (20.33%) conditional on launch first |
| X24: persistent vs. nonpersistent robustness under global scheduler | 37.14% vs. 13.64% launch-conditional success, $p\approx0.0062$ |
| X24: out-of-distribution classifier test (vacuum ages 200, 900) | 29/29 correct; combined with X23, 124/124 across 3 ages |
| X24: massless triangle causal-chain control | 30/30 exact producer links; $\Delta x=0$ still holds (confirms X19) |
| X25: compact A/B/C survival under symmetrized birth order | expected < 2 local events before leaving the compact class |
| X25: recurrence under symmetrization (independent of compact identity) | 107-state exact closed SCC, 0 dead states |
| X25: tether-phase alphabet under symmetrized dynamics | 94.5% original 3 patterns; new 4th pattern in 5.5% of 1,400 checkpoints |
| X25: bridge-role transport direction under symmetrization | 33 decreasing / 50 increasing (of 83) — ratchet exactly dissolved |
| X25: residual channel pilot on symmetrized grammar | outward 16/60 (26.7%); reverse 0/72 (smaller, non-exhaustive) |
| X26: output-source symmetrization, matched reverse census (baseline / fresh / full) | 0/47, 0/47, 0/47 (up to 843,837 candidates checked) |
| X26: forward channel under output symmetrization (latency / receivers) | depth 2 throughout; receivers grow 2 → 3 → 18 |
| X26: old-substrate source-undirection, forward channel | depth 1 (down from 2); 8 immediate receiver gates |
| X26: old-substrate source-undirection, matched reverse census | **2/47** exact reciprocal paths (sources 11, 24; 16 receivers each) |
| X26: cross-check, full-output-symmetric terminal SCC vs. independent source-undirected build | both exactly 24 states, 0 mismatch either direction |
| X27: dressing-constrains-capacity permutation test — **superseded, see X28 below** | ~~not significant: $p=0.372$, $0.102$, $0.263$~~ (indexing error) |
| X27: realized-vs-redirect return success (6 matched pairs, large misalignment) | 6/6 and 6/6; mean cost 3.33 vs. 3.00; no pair costs more |
| X27: massless triangle control (reconfirmed) | 31/31 exact states; 30/30 causal links; $\Delta x=0$ over 30 events |
| X28: index audit, actual outgoing current vs. X16 boundary label (8/8) | cosine $1.0$ to floating-point precision at every boundary |
| X28: **corrected** dressing-constrains-capacity permutation test (40,320/40,320 exact) | significant: $p=0.0097$, $0.00025$, $0.0064$ (70/76 actions forward-aligned) |
| X28: **corrected** realized-vs-redirect return success (7 matched pairs) | 7/7 and 7/7; identical total cost, 23 vs. 23 rewrites |
| X28: $D_1$ invariance under clean legal core-disjoint vacuum events | 0/592 changes; $D_2$ changed 52/592, max magnitude 0.043 |
| X28: matched-fork own-predictor causal-priority test | null, exact sign-flip $p=0.25$ |
| X28: strict single-relation ablation, one-cycle return and defect persistence | 7/7 returns; deleted relation restored in 0/7 cases |
| X28: multi-phase defect screening (representative relation) | effect ranges 0.10–1.00 of baseline — shrinks then rebounds, not repaired |
| X28: ablation removing a specific legal transport channel | 2/7 boundaries, both forward-aligned channels |
| X28: massless triangle wake-ablation control | 11/11 exact recurrence both arms; 0/2 severed wake relations regenerated |
| X29: pooled scheduler mass, all 8 boundaries (70 forward / 6 reverse) | 92.1% forward, conditional on a strict transport event |
| X29: mixed-sign boundaries only (P0, P4, P5; 28 forward / 6 reverse) | 82.4% forward — the more meaningful figure, since 5/8 boundaries have zero reverse channels |
| X29: exhaustive matched recovery, every reverse channel vs. equal forward sample | 6/6 and 6/6 returns; cost 3.33 vs. 3.00, not significant ($p=0.25$) |
| X30: unforced-scheduler exact recurrent returns (40 trials, no steering) | 0/40; strict transport subset is under 10% of all touching contacts (15/158 at P0) |
| X31A: contact-level bounded recovery, all touching contacts (8 boundaries) | 187/198 (94.44%) recoverable — recovery paths are abundant, not scarce |
| X31A: directed interface role discriminator (paired orientation) | role-1: 8/8 recoverable; role-2: 2/8; paired sign $p=0.0156$; Fisher $p=0.0035$ |
| X31B: first spontaneous unforced exact returns (P4, P5; 40 trials) | 3/40 (2/20, 1/20), at 174–383 events; non-lost 55% vs. P0's 25% ($p=0.023$) |
| X31B: survivor-state restart enrichment test | 2/30 further returns vs. 3/40 baseline — no enrichment ($p=0.72$) |
| X32: Candidate 8 contact-level recoverability and role-swap pairs | 21/21 contacts recoverable; 6/6 role-swap orientations return (vs. P0's destructive asymmetry) |
| X32: Candidate 8 unforced scheduler returns (70 trials) | 16/70 (22.9%) any return, 22 total returns, 5 multi-return trials; vs. P0 0/40, $p=0.00036$ |
| X32: Candidate 8 vs. X31 P4 return-rate comparison | not yet distinguishable, $p=0.17$ |
| X32: constituent turnover across repeat returns | 7/11 recorded return events have zero overlap with the preceding exact support |
| X32R: rule selection (frozen, pre-existing Stage W metric) | Rule 55584, highest producer-flow survival among untested W41 rules |
| X32R: natural-state discovery (fixed 4-seed budget) | 81 hits, 36 distinct states (vs. 58846 calibration: 13 hits, 5 states) |
| X32R: winner (instance 28) contact recoverability | 12/12, uniform first-found cost of 2 |
| X32R: winner unforced scheduler returns (70 trials) | 34/70 (48.6%) any return, 54 total, 14/70 multi-return, max 5 in one trial |
| X32R: winner vs. Candidate 8 (exact-return / multi-return) | $p=0.0013$ / $p=0.023$ — 55584's winner is statistically better |
| X32R: constituent turnover | 26/54 zero overlap with original support; 19/54 zero overlap with immediately preceding support |
| X32R: literal $y/z$ mirror pairs across all 36 discovered states | 0 — genuine grammar difference; pre-registered fallback census used instead |
| X33: LOO composite predictive cosine (58846 / 55584) | 0.733 / 0.835; simple $-D_1$ alone: 0.690 / 0.838 |
| X33: cross-rule weight transfer (58846 weights on 55584 data) | 0.834, vs. 55584's own full fit of 0.843 — almost no loss |
| X33: strict transport-capacity forward-hemisphere fraction (58846 / 55584) | 82.3% ($p=0.0002$) / 93.3% ($p<0.0002$) |
| X33: lag-1 current correlation vs. static-anisotropy baseline (58846 / 55584) | negative / $p=0.356$ — not significant either rule |
| X34: population screen, states with $\geq$3 usable adjacent pairs (of 13) | 1 (55584 Winner 28); excess $M_1=-0.10$, $p=0.61$ |
| X34: state 22, initial validation vs. independent replication | initial $M_1=+0.40$ ($p=0.18$); 2 replication blocks: 0/0 usable adjacent pairs |
| X35: 55584 $D_1$ planarity and phase persistence across returns (47 pairs) | PC1+PC2 variance 0.972; $\cos=0.502$ vs. depth-matched null 0.237 ($p=0.001$) |
| X35: 55584 phase persistence, first returns excluded (25 pairs) | $\cos=0.553$ vs. null 0.051 ($p=0.0008$) |
| X35: 55584 current coherence, raw vs. co-rotating frame | 0.348 raw → 0.721 co-rotating ($p=0.0004$); later returns 0.854 |
| X35: fixed universal rotation model vs. no-rotation (identity) | 0.511 vs. 0.513 — no advantage; not a predictive law |
| X35: 58846 phase persistence (depth-matched) | $p=0.657$ — apparent near-180° step is a shared-schedule artifact |
| X35: 58846 current/phase coupling (weaker, still real) | $\cos=0.242$, $p=0.0024$ |
| X36: coarse-state determinism (14 repeated signatures, phase spread) | $R=0.572$ — exact generator falsified |
| X36: inter-shell twist $\beta$, LOTO predictive slope | median $0.850$; depth-matched $p=0.044$ |
| X37: exact path-dependence counterexample | identical pre-contact hashes; $\Delta\phi=0$ vs. $\pi$ exactly, $\cos=-1$ |
| X38: controlled network size | 361 boundaries, 360 edges, $D_1$ variance 100% on 1 axis |
| X38: ordered-path LOTO prediction (accuracy / flip recall / flip precision) | 99.38% / 91.89% / 100%, paired $p\approx1.16\times10^{-10}$ |
| X38: six-rewrite composition (independently predicted, composed) | 124/124 correct across 4 independent $\pi$-sector starts |
| X38: event-order reversal control | 0/340 reversed sequences return to exact recurrence |
| X39: natural antipodal order and coherence gain after $\mathbb{Z}_2$ removal | $R_2=0.79$ (97 boundaries); coherence 0.502→0.827 |
| X39: independent cross-check of $\mathbb{Z}_2$ split vs. residual branch | 44/47 agreement, $p=3.85\times10^{-7}$ |
| X40: fresh-ensemble replication and exact vacuum-interval invariance | $R_2=0.769$ (160 trials); max phase drift $8.88\times10^{-16}$ rad |
| X40: flip probability vs. path length | median 4.5 (no-flip) vs. 20.0 (flip) contacts, $p\approx9.8\times10^{-11}$ |
| X41: constant winding-rate model, independent validation | $3.909°$/event; phase cosine 0.730 vs. identity 0.550, $p\approx0.0096$ |
| X41: current-transport test using the best frozen model | 0.484 predicted vs. 0.550 realized — not yet improved |
| X42: matched-spacing vacuum-time control (15x spacing variation) | $d\phi/dN_{vac}=0.01°$, $p=0.92$ — ambient time does not advance phase |
| X42: particle vs. vacuum vs. scheduler clock rates | 3.91°/hit vs. 0.0046°/vacuum-rewrite vs. 0.42°/rewrite |
| X43: unwrapped winding rate (development / validation) | mean 4.65°/hit / 3.07°/hit, SD $\approx10°$ — broad, not sharp |
| X43: adjacent-episode rate persistence | $r=-0.17$, $p=0.19$; ICC $\approx-0.09$ — no conserved rate |
| X43: instantaneous dressing predicts next-rate tendency ($n_1$, $\beta$) | $\rho=0.46$ ($p=0.001$), $\rho=0.33$ ($p=0.026$) — ordinal only, $R^2<0.05$ |
| X44: population screen, 12 carriers + 58846 reference | 0/13 combine low dispersion with positive persistence |
| X44: best short-screen candidate (carrier 22), unwrapped replay | sign reverses: $r=-0.236$ |
| X45: harmonic/conjugacy/$\mathbb{Z}_m$/orientation sector search, Winner 28 | 0 replicated conserved sectors ($m=1$–$6$, all tests) |
| X45: nominal population candidate (carrier 22, $m=4$), frozen validation | $\Delta C_4=+0.042$, $p=0.264$ — fails replication |
| Y1: regeneration/closure burden $R_C$, within-carrier repeatability | ICC $=0.584$; base-vs-replication $r=0.652$; pairing $p=0.032$ |
| Y1: regeneration/closure burden $R_C$, between-carrier discrimination | $F=3.803$, $p=0.019$ (11 carriers); other 4 candidates all fail |
| Y3: relative carrier ordering across censoring depths $D=6,8,12,16$ | Spearman $\rho=0.986$ ($D{=}12\to16$); PCA $\mathrm{PC}_1=99.53\%$ |
| Y3: absolute burden convergence at $D=16$ | not converged; median $+0.469$ burden units per added tick |
| Y3: naive $E_0=\mathcal{R}\omega_0$ test, frozen $\omega$ | looks strong ($F=14.3$, $p=5.5\times10^{-8}$) but not promoted — see below |
| Y3: $\omega_{\text{cond}}$ block-level stability (the reason it wasn't promoted) | CV $=0.401$; $F=1.34$, $p=0.28$ |
| Y4: renewal-intensity clock $\omega_{\text{renew}}$, fresh-block stability | Pearson $r=0.953$; ICC $=0.934$ (vs. $\omega_{\text{cond}}$'s $0.118$) |
| Y4: asymptotic phenotype $(q_\infty,\mu_{W\mid\text{return}})$, carrier identity | $F=5.06$/$4.70$, $p<0.0002$ both; holdout $r=0.73$/$0.77$ |
| Y4: tail-model sensitivity (geometric order 1–3) | rank correlations $\rho=0.986$–$1.000$ — not an artifact of tail choice |
| Y5: derived composition-additive form, vs. failed alternatives (median rel. error) | $R_{\text{act}}$: exact ($0$); $\mu/q$: $0.62$; odds-work: $1.50$; $1{-}q$: $0.19$ |
| Y5: universal loss-work scale $\ell_0$ (particle-coupled hits) | $8.703$; no carrier effect ($F=0.80$, $p=0.64$); LOO range $8.54$–$8.85$, $\rho=1.0$ |
| Y5: $\mathcal{R}_{\text{act}}$ carrier identity and holdout replication | $F=8.65$, $p=3.2\times10^{-7}$, ICC $=0.657$; holdout $r=0.799$ |
| Y5: $E_0=\mathcal{R}_{\text{act}}\omega_{\text{renew}}$, independent A/B block test | $r=0.940$, $\rho=0.965$, ICC $=0.918$ — clears Y3's failed bar |
| Y5: physical inertial cross-check | blocked — no independent velocity observable exists yet for these carriers |
| Y6: X27/X28 redirect-cost check | 23 rewrites (realized) = 23 (redirected) — no local turning penalty exists |
| Y6: X30 unrestricted-history recurrent-velocity availability | 0/40 — no second exact return at all |
| Y6: seven-gate validity protocol for the eventual mass test | frozen; requires $\geq6$ carriers, held-out, single global $\alpha$ |
| Y6: verdict on $\mathcal{R}_{\text{act}}$/$E_0$ | neither falsified nor validated — bottleneck is kinematics, not the energy scalar |
| Y7: massless triangle, natural boundary extension | $q_\infty=1$, $\mu_{W}=0$ $\Rightarrow$ $\mathcal{R}_{\text{act}}=0$ exactly |
| Y7: persistent distinguishable embedding (same predictive class) | RMS $=0.882$, 36/72 coordinates differ; persists through 4 further turnovers |
| Y8: controlled continuation quotient, net displacement per recurrent cycle | $\Delta x=0$ in every cycle; 0/70 four-interval same-sign natural candidates |
| Y8: natural apparent displacement vs. intervening vacuum activity | Pearson $r=0.795$, $p=2.8\times10^{-5}$ |
| Y9: concurrent-ruler correction, median displacement (raw → corrected) | $0.802\to0.047$; 90/90 same-support intervals show exactly zero drift |
| Y9: unique one-event exact-return operator, composition vs. translation | 12/12 exact applications; period-2 spatial oscillation, $\Delta x=0$ every 2 turns |
| Y9: natural adjacent-displacement persistence | anti-persistent, $r=-0.390$ ($p=0.0021$); 11/54 same-sign pairs |
| Y10: frozen phase-law screen (pairs tested / nonzero first-period) | 598 / 8; confirmed across 19 independent branch realizations |
| Y10: core automorphism check (rules out hidden role relabeling) | $|\mathrm{Aut}(C)|=1$ (exhaustive over $6!$) |
| Y10: second-period repetition of any nonzero candidate | 0/19; 0/30 natural ABA cycles; 0/12 natural ABAB cycles |
| Y11: causal-rank closure law for frontier $F_0$ ($s_2<E<s_5$) | verified by exhaustive slot test; 12/12 Y9 compositions consistent |
| Y11: bounded two-regeneration search / complete translation-ready states | 4,118 exact outputs / 0 complete |
| Y11: independent 80-trial unforced readiness ensemble | 76 exact returns; 15 restore $F_0$; 4 restore first launch; 0 complete |
| Y13: nine-output recurrence neighborhood, intrinsic self-translation | 0/12 variants |
| Y13: minimal two-fresh frontier threshold ($k$=1–2 / $k$=3, Rule 55744) | 0/465 / 2/4,060 self-renewing extended-state cycles |
| Y13: $k$=3 self-renewing frontier rules across 8 branching cores | 21 total (27399:1, 47891:3, 52067:1, 54581:2, 55584:2, 55585:5, 55744:2, 55746:5) |
| Y13: mandatory six-role look-ahead, substrate survival | dead within 1–3 events on every tested rule |
| Y13: frontier-first causal-ordering fix, controlled shifts (6 rules) | 12/12 consecutive exact, each rule |
| Y13: natural frontier-first worldtubes (6 seed-0 vacua) | 101 natural start motifs; 69/69 sampled complete all 8 autonomous shifts |
| Y13: spatial promotion test on all 69 exact worldtubes | 0/69 promotions; 0/69 four-step same-direction runs |
| Y13: mean/median adjacent-displacement cosine (69 worldtubes) | $-0.749$ / $-1$ (exact reversal at the median) |
| Y13B: co-rotating causal-role frame, worldtube-weighted coherence | raw $-0.749\to+0.994$; 69/69 worldtubes exceed 0.9 |
| Y13B: single-axis reduction ($c_0\to c_1$), all nonzero steps | 450/450 positive; mean $0.993$; 437/450 exceed $0.999999$ |
| Y13B: shuffle-null control (1,000 realizations) | observed $0.992$ vs. null $0.043\pm0.042$ (max $0.177$); $p<0.001$ |
| Y13B: independent frontier-interface-dipole frame (corroboration) | $0.939$ pair-weighted coherence; shuffle $p<0.001$ |
| Y13B: frame transport vs. vacuum (decisive control) | mean $-0.617$; outgoing axis backward in 348/352 cases |
| Y13B: frame-transport / raw-anti-persistence correlation | $r=0.989$ — same underlying fact, not independent evidence |
| Y13B: exact role-succession identity ($c_1{\to}c_2$ becomes next axis) | $\cos=1$ in 310/310 tested cases (algebraic, not approximate) |
| Y13B: one-boundary bend $B_t$ predicts next displacement alignment | $r=0.989$, MAE $=0.007$; exact to $10^{-9}$ in 298/310 cases |
| Y14: upstream $B_t$ prefilter, isolated positive exception (Rule 6843) | seed-0 $B\approx+0.174$; failed replication in 5/5 additional vacua |
| Y14: exact one-step orientation-preserving census | 68/489 evaluable operators, across 25 distinct rules; several exactly $R_F=1$ |
| Y14: Rule 54655 universal variant, natural worldtubes | 11/11 exact (88 shifts); $R_F=1$ throughout; 0/88 nonzero spatial shifts |
| Y14: Rule 66338 universal variant, natural worldtubes | 15/15 exact (120 shifts); 5/120 nonzero, all on first shift only |
| Y14: independent rank-4 controls (Rules 68960, 52239 combined) | 9 natural worldtubes, 72/72 exact shifts, 0 nonzero |
| Y14: Rule 58846 conditional reserve (not promoted) | $R_F=1$, causal-rank-3 frontier — not simple-append self-generatable |
| Y14B: full frozen-vacuum distance field, Rule 54655 (14 worldtubes) | 67,088/67,088 individual comparisons unchanged; combined with rank-4 controls: 110,216 |
| Y14B: same apparatus on a Y13 oscillatory positive control | 120/120 nonzero full-field changes — correctly detects real motion |
| Y15: single-relation decoration of Rule 54655's rest event | 0/93 produce any full-field motion; 70/93 preserve 4 exact shifts |
| Y15: native same-rule rest/move macrocycle ($\Phi_1\to\Phi_0\to\Phi_1$) | 14/14 worldtubes repeat for 8 periods; mean frame transport $-0.524$ |
| Y15: native bifurcation census across full Y14 population | 14 rules qualify (both rest-like and moving one-step operators) |
| Y15: decisive screen, all native movers under self-renewal | 159/159 exact 4-period closure; 0/159 coherent 4-step motion |
| Y15: Rule 76073 ambient embedding, forward vs. zero outcomes | mean 9.56 vs. 7.32 external-only relations (177 evaluable instances) |
| Y15: natural second ambient handoff (101 forward-moving events) | 0/101 fully pre-embedded successor; only 4/101 have even one relation |
| Y15: oracle-assisted look-ahead upper bound (5 signatures, 47 starts each) | max chain length $=1$; 0 four-handoff chains; 0 promotions |
| Y16: rooted-refinement predictive-vs-transferable tradeoff (depth 1/2/3) | accuracy $0.657\to0.704\to0.982$; cross-vacuum coverage $0.864\to0.817\to0$ |
| Y16: leave-one-vacuum-out AUC (sparse local / +global features) | $0.492$ / $0.515$ — chance level |
| Y16: full-halo transplantation onto fresh successor (47 tests) | 47/47 exact recurrence; mean nonzero shifts falls to $1.0$; 0 promotions |
| Y16: future-looking oracle, second-step alignment (12 starts) | 4/12 have any positive candidate; mean best cosine $-0.094$; max chain $=2$; 0/12 four-step |
| Y17: particle-selected vacua, exact geodesic corridor length (54 snapshots) | max length 3; 0 length-5 corridors |
| Y17: exact bulk translation automorphism, candidate 157 | fraction $=1.0$ exactly, all shifts $\delta=1$–$12$, 5 vacuum sizes (305–2,405 vertices) |
| Y17: exact bulk translation automorphism, full 6-crystal family | fraction $=1.0$ exactly, shifts $\delta=1$–$3$, all six rules |
| Y17: crystal diameter scaling exponent (6 rules, to 1,200 events) | $0.997$–$1.014$ (linear in $N$) |
| Y17: natural second carrier handoff in proven-homogeneous crystals | 0/8 (157), 0/18 (1035), 0/6 (214) — max chain length 1 |
| Y18: fixed-budget co-design search (2-of-8 output replacement) | 4/28 variants preserve exact crystal symmetry through 600 events |
| Y18: variant 0-3, natural multi-handoff carrier (3 sites) | 8/8 consecutive natural boundary transfers, no injected frontier |
| Y18: variant 0-3, long-run macro-translation (4 sites, 20 periods each) | 80/80 nonzero; adjacent cosine range $0.781$–$0.936$ (verified in raw data) |
| Y18: random-scheduler robustness control | 0/60 survive 36 microtransfers; mean survival $2.9$ transfers |
| Y18: naive backward-oriented policy (attempted $-v$) | terminates after 1 transfer — no mirror mode |
| Y19: forward-half causal-rank bit alone | 0/120 long survivors — momentum is not a simple rank bit |
| Y19: carrier-phase sufficiency | fails by exactly 1 bit (5 distinct phases across a 6-step cycle) |
| Y19: nearest-oriented selector, $\sigma=+1$ | 40/40 survive 121 microtransfers; 80/80 nonzero; min. adjacent cosine $0.809$ |
| Y19: nearest-oriented selector, $\sigma=-1$ | 0/40 survive beyond the first transfer — not parity-symmetric |
| Y19: scale robustness (vacuum ages 300–1,200 events) | 60/60 survive 61 microtransfers, all reach 10 macroperiods |
| Y19: static relational marker search for $\sigma$ (19 candidates) | none survives the full cycle; best holds 34/41 boundaries |
| Y20: self-renewing $+$ marker, long-run and full-field survival | 40/40 (121 microtransfers); 80/80 nonzero; min. adjacent cosine $0.809$ |
| Y20: retired marker audit / scale / interleaving robustness | 30/30 relationless; 60/60 (4 vacuum ages); 30/30 interleaved |
| Y20: naive negative marker, long-run and branch census | 0/40 survive; 135 negative cycles found, 11 repeat once, 0 repeat twice |
| Y21: exhaustive one-relation backward-interface search | unique winner among 30 candidates: $Q_-=T(c_0';\{c_4',T^{-1}(e)\})$ |
| Y21: backward sector robustness (long-run / scale / interleaving) | 40/40; 60/60 (4 vacuum ages); 20/20 interleaved |
| Y21: minimal coherent backward block, full-field verification | exactly $-4.0$ orbit sites at all 4 sites; adjacent cosine mean $0.742$, min $0.703$ |
| Y21: common-clock speed comparison ($+$ vs. $-$) | $\approx+8$ vs. $\approx-12$ orbit sites/12 events — oppositely directed, unequal ($1.5\times$) |
| Y21: direct parity-mirror attempt / best candidate long-run behavior | destroys $+$ cycle / survives short screen, degrades over long runs |
| Y21: Y6 gate G2 (independent signed velocity) | **PASS** — first time in this investigation |
| Y22: common sign-covariant interface, settled orbit motion | $\Delta j_T=+1$ and $-1$ per event exactly, zero variance |
| Y22: interface boundedness ($+$ / $-$ lanes) | 3 / 1 live relations, fixed — not growing with trajectory length |
| Y22: block-scan minimum adjacent cosine (blocks 3/4/5) | $0.074$ / $0.610$ / $0.988$ |
| Y22: zero-displacement branch cycles / repeat once / repeat twice | 41 / 7 / 0 — no persistent rest cycle |
| Y22: alternating $+,-,+,-$ rest attempt | 0/4 sites survive beyond 1 microstep |
| Y22: second-speed screen (30 forms, strides 2–3) | negative lanes reach clean $-2$/$-3$; positive lanes fail (microcycles or accumulation) |
| Y22: Y6 gate G3a (equal-speed $\pm v_1$ pair) | **PASS** — first clean parity-symmetric result |
| Y22: Y6 gates G3b (rest) / G3c (second speed) | FAIL / FAIL |
| Y23: clean round-trip handoff (8 cycles, $N=2$–$12$) | exactly 1 live interface relation throughout, 0 wake |
| Y23: autonomous rest, long test (4 locations $\times$ 50 cycles) | 200/200; exact-zero displacement; 0 field entries changed; 0 marker debris |
| Y23: autonomous rest, randomized continuation | 20/20; mean 20.0 cycles; 1 interface relation; 0 debris |
| Y23: $v_2$ interface-semantics fix, settled speed | $\Delta j_T=+2$ and $-2$ exactly per event; $|v_2|=2|v_1|$ |
| Y23: $v_2$ full-field block scan (8 worldtubes) | block 2: min. cosine $0.271$; block 3: $0.885$ |
| Y23: $v_2$ settled-state scheduler robustness | 160/160 (4 locations $\times$ 2 signs $\times$ 20 trials), 61 events each |
| Y23: pairwise carrier-identity isomorphism (5 kinematic states) | **25/25 PASS**; original P157 core correctly non-isomorphic (control) |
| Y23: Y6 gate G3 (full manifold $0,\pm v_1,\pm v_2$) | **PASS** |
| Y23: Y6 gates G4/G5 | READY, deliberately not yet measured |
| Y24: predeclared edit-action cost, all five sectors (16,000 events) | exactly $14$ edits/event — zero exceptions, verified event-by-event |
| Y24: edit decomposition (every audited event, every sector) | 4 relation deaths $+$ 10 births $=14$, invariant |
| Y24: sign symmetry / even response / curvature fit | $A_{\text{odd}}=0$ exactly; $\Delta A_{\text{even}}(v_1)=\Delta A_{\text{even}}(v_2)=0$; $M_i=0$ |
| Y24: bootstrap stability of $M_i$ | 95% CI exactly $[0,0]$; $P(M_i>0)=0$ |
| Y24: Y6 gate G4 (independent cost) / G5 (positive curvature) | **PASS** (operational) / **FAIL** (exact null) |
| Y25A: local legal-gate ensemble, all 16,000 events | singleton (1 legal, 1 compatible) throughout; $A_{\text{acc}}=0$ exactly |
| Y25A: secondary global scheduler diagnostic (not promoted) | sector-dependent (4.55–4.91); descriptive $M_i\approx0.87$, excluded pre-inspection |
| Y25B: triangle history-translation dispersion (257 modes) | $F=T$ exactly; $E(k)=|k|$, $R^2=1.0$, max residual $0$ |
| Y26: moving-sector vs. rest direct-contact cost | $A_{\text{dir}}(\pm v_1,\pm v_2)=\ln7$ exactly; rest grows $+7$ gates/cycle (residual $<2.3\times10^{-13}$) |
| Y26: rest relational halo growth per cycle | $+11$ touching relations, $+4$ external vertices, $+1$ two-core relations; internal fixed at 8 |
| Y27: fixed-budget variant screen (28 tested) | 0/28 full stationarity; variant 1-3 closes scheduler-contact grammar exactly (2,4,2,2) |
| Y28: persistent-anchor wake motif (100 site-cycles) | 11-relation motif exact in 100/100; 2 anchors persist in 100/100 |
| Y28: wake-consuming gate census / carrier-preserving consumers | 100/100 consumer occurrences; 0/100 preserve carrier identity |
| Y28: shuttle-amplitude control ($N=2$–$12$) | 2 anchors and exactly $+11$/cycle wake at every tested $N$ |
| Y29: full-turnover search (up to 21,315 candidate words) | reachable only as formation transient; 0/132 settled candidates retain zero overlap |
| Y30: position-tool identity leak, corrected coordinate $X_T$ | reproduces $\pm1,\pm2$ speeds exactly (40/40 each); rest returns exactly |
| Y30: corrected full-turnover rerun (180 cases, 132 settled) | 0/132 full turnover; two-anchor theorem proven algebraically |
| Y31: vacuum impulse-response census (360 perturbations) | 354 detach, 2 absorbed, 4 disrupt producer, **0 front-locked** |
| Y31: rest-cycle Floquet DC component | $\tilde{A}_0=2.75$ relations/event $>0$; global growth $+24$/cycle vs. $+11$/cycle attached |
| Y31: flux-balance word search (21,315 screened, 1,228 exact) | minimum attached-halo increment exactly $+11$; 0 nonpositive cases |
| Y31: bare carrier-handoff flux vs. completed program | $+8$/cycle (bare) $\to$ $+11$/cycle (with marker/Q bookkeeping) |
| Y32: one-output search (416 candidates) / best complete / bare flux | 0/416 close; best $+9$/cycle complete, $+6$/cycle bare |
| Y33: two-output search (2,548 pairs, seeded from Y32) / best flux | 0/2,548 close; best $+6$/cycle complete, $+3$/cycle bare (24 survivors, all gap $=+3$) |
| Y34: three-output search (1,560 triples) / unique kinematic survivor | only 1 combination kinematically viable (5/5 independent starts converge); flux **reverses** to $+7$/cycle |
| Y35: corrected single-control-volume flux decomposition | rule-fire $+2$; marker $0$; event-Q $+4$; cleanup $-2$; bridge $+2$; total $+6$ |
| Y35: uniform Q-template search (60 candidates) | 1/60 passes moving sectors — the original $Q_1$; all 59 others fail all 8 checks |
| Y35: split event/bridge Q search (3,600 pairs, predeclared fallback) | 0/3,600 close; unique survivor $(Q_1,Q_1)$, same $+6$/cycle |
| Y36: rest-interface search (lifecycle/compensator/phase-Q) | 0/16,384, 0/600, 0/6 — G3S fails on every front |
| Y36: exact wake-neutral $+v_s$ translator, 300/300 validation (6 sites) | $\Delta X_T=+1$, $\Delta H_{\text{local}}=0$, halo $=53$, global growth $+22$/period — all exact |
| Y37: exact wake-neutral $-v_s$ conjugate, 300/300 independent validation (6 new sites) | $\Delta X_T=-1$, $\Delta H_{\text{local}}=0$, halo $=53$, global growth $+22$/period — identical structure |
| Y37: sign-continuous $+v_s/-v_s$ splice, zero-drift composite | $\Delta X_T=0$ exact; $\Delta H_{\text{local}}=+12$/8-event period |
| Y38: exhaustive reversal-interface search (144 candidates) | 0/144 bound-state winners; 18 zero-drift candidates, minimum flux $+12$ |
| Y38: site-320 cross-check of the 8 $+12$ minima | 8/8 reproduce exactly ($\Delta X_T=0$, flux $+12$) |
| Y38: relation-provenance audit (2 independent $+12$ minima) | 27/27 and 29/29 final additions created *during* the reversal period, not re-encountered old material |
| Y39: $\Delta H_{\text{local}}$ transforms as $E(v)$, held-out relative error | 20$\times$–425$\times$ — decisively rejected as a state-energy candidate |
| Y39: universal $+6$ reversal source across 3 speed magnitudes | $|v|=0.25,1,2$, all exact; churn varies by $>10\times$, source fixed |
| Y40: forced spatial/time conjugate compensator search (300 programs) | 271/275 executable give exact zero drift; best source still $+11$ |
| Y40: reversal-source vs. gross churn (soliton, 0–40 prior reversals) | churn $165\to1{,}687$; signed source fixed at $+6$ throughout |
| Y41: causal-necessity audit, transport-family reversal source | output 1 alone: $+6\to+3$ (phase preserved); outputs 1+3: $+6\to0$ (phase transmutes) |
| Y41: paired phase-transmuting reversals ($v_1$, $v_2$, 6 sites) | exact zero drift; source reduced to rigid $+2$/8-event period |
| Y42: exhaustive independent reversal-mask search (256 trajectories) | 256/256 zero drift; 0/256 halo closure; floor confirmed at $+2$ |
| Y44: causal-lifetime map, delayed-cleanup programs (512 tested) | 9/13 relation classes safely removable; turnover $16/14\to7/5$; source rigid at $+2$ |
| Y45: previous-cycle scaffold retirement (e6/O7) | source $+2\to+1$; turnover $7/6$; 96/96 periods confirmed |
| Y45: provenance of the remaining $+1$ | uniquely isolated to one relation class, e7/O7; exact lifetime measured |
| Y46: single residual retirement (e7/O7 at measured safe point) | $\Delta X_T=0$, $\Delta H_{\text{local}}=0$; turnover $7/7$ |
| Y46: population validation (6 sites $\times$ 2 mag. $\times$ 2 signs $\times$ 50 periods) | **1,200/1,200** exact: drift, flux, phase, scheduler, Q/marker, halo isomorphism |
| Y47: primary trial costs (240 records, full precision) | $A(\pm v_1)=A(\pm v_2)=\ln2$; $A(\text{rest}, R_1/R_2)=\tfrac34\ln2$ (identical despite different halo sizes) |
| Y47: curvature result and replication (6 further sites, 57,600 events) | $M_i=\tfrac58\ln2\approx0.4332>0$; identical at every site and both rest anchors |
| Y48: distinct-carrier transfer census (576 trajectories, 12 carriers) | **0/576** survive the first event; 0/64 in exhaustive backup diagnostic |
| Y48: grammar overlap audit (original Rule 55584 vs. Y47 architecture) | **0/8** shared outputs — a distinct, co-designed rewrite law |
| Y50: FBCL local launch-basin screen (4,526 states, Hamming radius $\le3$) | 1,704/4,526 (37.65%) support the full $\pm v_1,\pm v_2$ manifold |
| Y50: mature species among all 1,704 successful launches | **1** (all converge to the same canonical isomorphism class); 32/32 replication |
| Y49: native Rule-55584 macrostep census (247 contacts, 12 carriers) | 227 exact returns; 186/227 nonzero displacement; only 2/12 carriers meet the necessary 5-sector filter |
| Y49: Winner 28 native control | 12/12 exact returns, all $\|\Delta\mathbf{X}\|=0$ — recurrence and motion cleanly separable |
| Y51: exhaustive 6-relation launch census (corrected for age-order) | 593,775 raw cores $\to$ 37,086 (screen) $\to$ 1,783 (4-sector) $\to$ **1 species**, 454 launch orbits |
| Y52: period 1–4 extension (17,828 passing sector trajectories) | **17,828/17,828 period 1**; 0 at periods 2, 3, 4; 2,068 launches, 455 orbits $\to$ 1 species |
| Y53: dressed-state census (2,068 Y52 launches) | 1,299 recurrent in all 4 sectors $\to$ **1 dressed species (DS001)**; 70 rejected as 2-Q secular memory |
| Y54: composite pair census (1,600 constructions) | 8 qualify, all at $d=7$, only $(+v_2,+v_2)$/$(-v_2,-v_2)$; bond regenerates after ablation (1 round), stress-tested 16/16 $\times$ 200 rounds |
| Y55: direct $d{=}7$ $v_1$ pair, corrected diagnosis | 32/32 settle period-1 by round 4, but **0/32 ever show cross-carrier coupling** — factorized, not CD001 |
| Y55: speed-switch diagnostic (32/32 each direction) | $v_2\to v_1$: bond gone after 1 round; $v_1\to v_2$: bond nucleates by round 2 — no hysteresis either way |
| Y56: exhaustive bonded sign-word census (276 words, 1,104 runs) | 6/6 uniform controls pass; **0/270 reversal words pass** — fail exactly at first sign change |
| Y56: post-turnaround handoff census (8 mature contexts) | legal handoffs drop $1\to0$ per constituent; CD001 bond remains intact — transport-dead, not dissociated |
| Y57: speed-mediated reversal, kinematic vs. dressed settlement | exact $|v|{=}1$ by round 3 (32/32); dressed state not settled by round 12 (0/32); settles by round 48–50 |
| Y58: isolated half-reversal (fixed 60-round dwell) | 32/32 exact; center displacement $\mp63$ sites |
| Y58: concatenated full cycle (no re-formation) | **0/32** — second wake not settled by round 60; settles instead at round 99 (32/32, extended test) |
| Y59: renewal-horizon growth across 8 successive reversals | exactly linear, $T_n^{(+)}=54n+9$, $T_n^{(-)}=54n+11$; no saturation, no periodic reset |
| Y59: relation-hop memory localization | identical to fresh through hop 2; first differs (28 records) at hop 3; first reversal-count-sensitive at **hop 8** (12/12) |
| Y60: hop-8 local forgetting vs. coast length $C$ | symdiff $377/368\to0$ by $C=32$; exact zero, 8/8 contexts, through $C=128$ |
| Y60: reversal-cost penalty vs. coast length (fully certified $C\le64$) | $\Delta H=52$ ($+v_2$) / $56$ ($-v_2$) — exactly constant, independent of $C$ |
| Y60: return-divergence round vs. coast length | $r_{\text{div}}=22+2C$ exactly, confirmed through $C=128$ |
| Y60: return-divergence spatial locus vs. coast length | fixed absolute coordinate ($2969.0$ / $3036.0$) at every tested $C$; 2 further centers reproduce |
| Y60: $C=256$ censoring | historical/fresh traces identical throughout the observed window — consistent with not yet reaching the scar |
| Y61: scar-centered spatial profile, $\pm32$ scan (8/8 primary contexts, all $C$) | $+v_2$: offsets $+4..+32$ nonzero, 226 relation/8 gate symdiff records; $-v_2$: $-32..-4$, 227/5; censored at scan boundary |
| Y61: exact raw persistence, $C{=}64\to512$ | 8/8 primary contexts: every support-offset relation/gate star bit-for-bit unchanged while carrier recedes to 1032.5 units |
| Y61: Tier-B replication (centers 2400/3600) | 16/16 checkpoints reproduce identical support intervals, burdens, and exact persistence |
| Y62: full trail extent, $k=0..192$ scan | $+v_2$: $k{=}4..75$, 72 vertices, 0 gaps, far edge certified; $-v_2$: $k{=}4..77$, 74 vertices, 0 gaps, far edge certified |
| Y62: relation/gate burden at full trail | $R_{\text{union}}=610/622$, $G_{\text{union}}=8/8$, $I_{\text{touch}}=756/768$; no ratio to $\Delta H$ is sign-invariant |
| Y62: birth-order provenance along trail | Spearman $\rho\approx-0.98$ to $-0.99$; OLS slope $\approx-4.11$ births/coordinate, all contexts |
| Y62: fixed 320-round return probe | $+v_2$: 80 diff rounds ($150$–$229$) $=L{+}8$; $-v_2$: 82 diff rounds ($150$–$231$) $=L{+}8$; both endpoints match prediction exactly |
| Y62: resolved Y60 delay mechanism | hist. permanent start $230/232$ minus fresh permanent start $178/176$ $=$ $52/56$ exactly |
| Y62: post-specified Y59 horizon reconstruction | additive $63,117,171,225,279,333,387,441$ / $65,119,173,227,281,335,389,443$ — exact, no fitted parameter |
| Y63: parent reproduction, 3 successive half-reversals | 24/24 primary, 24/24 Tier-B reproduce Y59 horizons exactly ($63,117,171$ / $65,119,173$) |
| Y63: strict older-trail raw persistence after next reversal | **0/24** primary, **0/24** Tier-B remain raw-identical — every audited vertex changes |
| Y63: multi-history support vs. isolated-template union | 0/16 primary, 0/16 Tier-B exact-union matches; every case censored at audit boundary; e.g. 2-trail $+$: 122 vs. 96 nonzero coords |
| Y63: fixed next-reversal probe, excess beyond isolated-template contact | universal $+30$ rounds beyond prediction in all four (2-trail $\pm$, 3-trail $\pm$) cases |
| Y63: turnaround-delay additivity | 2 prior trails: $52+56=108$, 16/16 exact; 3 prior trails: $160$/$164$, 16/16 exact — **32/32 combined** |
| Y64: transformed multi-history support, wide scan (16/16 primary, 16/16 Tier-B) | finite; shortest zero tail 162 coords; contains full isolated-template union plus more |
| Y64: asymmetric rewrite geometry | exit-side extension exactly $+30$ coords (contiguous), entry-side $+19$ (dynamically silent), 32/32 cases |
| Y64: naïve full-support convolution vs. active-corridor convolution | naïve over-predicts by exactly 19 rounds, 32/32; active-corridor prediction matches observed exactly: $134,136,188,190$ (16/16 + 16/16) |
| Y64: rewrite-front localization | original support unchanged through deceleration/turnaround; each vertex first changes at pair-center distance exactly 5 during reverse-v1 |
| Y65: independent fresh-probe readout (8/8 primary, 8/8 Tier-C) | third-party diff duration $=80$ ($+$) / $82$ ($-$) exactly $=L_{\text{trail}}+8$; equal before/after contact |
| Y65: backreaction on the trail from an unrelated probe | **0/8** primary, **0/8** Tier-C, **0/16** matched-history diagnostic rewrite any original support vertex |
| Y65: 52/56 transfer to independent probe | none — target/control separate only during geometric contact, rejoin immediately; delays are creator-history-specific |
| Y66: aligned creator/independent pre-fork state (16/16 guards) | identical position, direction, R=7 touching signature, bit-for-bit identical trail support |
| Y66: earliest measured read/write discriminator | exact causal age differs at $h{=}1$ (24-record symdiff, 16/16); age-blind $h{=}1$ exactly equal; uniform age offset $+1198$ ($+$) / $+1210$ ($-$) |
| Y66: next discriminator after age erasure | age-blind structural difference first appears at $h{=}2$: 19 records ($+$), 2 records ($-$), 16/16 |
| Y66: repeated-reader non-destructiveness | 2 independent readers, same trail: both exact 80/82-round readout, zero cumulative rewrite (4/4 contexts) |
| Y67: selector-level trace (100 rounds $\times$ 16 contexts $\times$ 2 constituents) | **3,200/3,200** identical candidate sets and choices; candidate count exactly 1 throughout — no tie, no divergence |
| Y67: nature of the one-step fork | identity-valued Q1 insertion only; $u{=}f<v{=}c_4$ forced by old/new-vacuum partition, unaffected by the 1198/1210 age offset |
| Y68: h=2 recomputation channel, positive branch (8/8) | 5 independent-only $h{=}2$ relations used in successful `_gf()` witnesses, round 1; normalized gate symdiff 2 — real but not universal |
| Y68: h=2 recomputation channel, negative branch (8/8) | closure-visible (1 hit) but **0** successful `_gf()` uses across the full 100-round trace |
| Y68: h=2 role at the actual Q fork (16/16) | zero closure hits, zero successful-gate dependencies, gate symdiff 0 — h=2 does not enter that operation's recomputation cone |
| Y68: temporal-necessity check | first h=2 recomputation event precedes the Q fork in 8/16 contexts (AB), follows it in 8/16 (BA) — rules out universal causation |
| Y69: order-preserving quotient, Q1/trail fork (16/16) | Q1 insertion and complete original-trail records: raw-ID different, but order-canonically equivalent at h=1 and on full trail through 100 rounds |
| Y69: genuine (non-gauge) pre-existing difference | h=2 vertex-count differs by exactly $\pm1$ before Q1 fires (61v62 / 61v60); canonical symdiffs 204/7 (+), 186/5 (-) |
| Y70: gauge-invariant multi-history corridor (32/32) | entry-side extension $\to$ **0** (pure gauge); exit-side extension **30**, exact, contiguous, no missing template coordinates |
| Y70: gauge-support convolution vs. Y63/Y64 timing | $126,128,180,182$ gauge-support lengths $+8$ reproduce $134,136,188,190$ observed durations exactly, no directional-kernel rule needed |
| Y70: independent-reader gauge fingerprint (16/16) | target-minus-control gauge difference unchanged before/after crossing in every case |
| Y71: dwell-sweep law (32/32 exact, no fitted parameter) | $L_{\text{gauge}}=L_{\text{isolated,current}}+\Delta H$; e.g. $74+52=126$, $72+108=180$ |
| Y71: forced-dwell intervention (16/16) | fresh no-prior-trail CD001 held in reverse-v1 for exactly $\Delta H$ reproduces the historical gauge support exactly; creator-minus-control leaves exactly the original trail |
| Y71: genesis diagnostic | extra-support count grows by exactly $+1$ per round for exactly $\Delta H$ rounds, no round contributing more than one coordinate |
| Y72: global launch sweep, $k=5..30$ | 6,031 sampled screen-passing masks; 157 four-sector recurrent; **157/157** converge to DS001; 0 recurrent survivors at $k{=}26..30$ |
| Y72: one-decoration exhaustive census | 517/540 seeds recurrent; **517/517** converge to DS001; 23 fail four-sector recurrence |
| Y72: exceptional-defect pairwise census | all $\binom{23}{2}=253$ unordered pairs of failing decorations tested; **0/253** produce a recurrent carrier |
| Y72: marker/interface excitation census | 30/30 seeded excitations recurrent; **30/30** converge to DS001 |
| Y72: two-decoration sample | 500-pair deterministic sample; 454 recurrent; **454/454** converge to DS001 |
| Y72: cumulative population result | 157+517+30+454 = 1,158 recurrent trajectories tested across the stage; **0** second species found |
| Y73: fresh-launch satellite search | 9,050 valid one/two/three-relation seeds ($60+870+8{,}120$); **0/9,050** retain a fourth halo vertex |
| Y73: mature-carrier satellite search | 100,825 specs enumerated, 25,925 rejected (f/core collision), 74,900 valid; **0/74,900** retain a fourth halo vertex |
| Y73: combined passive-satellite null | 109,875 seeds enumerated, 83,950 valid distinct-role geometries; **0** retain an extra bound role; **0** new species |
| Y74–Y75: role-exchange / global six-role null (per Y76's own record; source packages not independently reviewed) | every tested recurrent six-role construction matures to DS001; no second species at any tested density |
| Y76: seven-role overlapping-kernel census | 4,951 launch masks, $k{=}6..105$; **291** four-sector recurrent; **291/291** exact DS001 signature; 0 novel species; survivors in 91/100 strata |
| Y76: translated-site diagnostic | 24 contexts (6 densities $\times$ 2 sites $\times$ 2 ties); 6/24 complete passes, **6/6** DS001 |
| Y77: natural dimer census | 1,024 cases ($R{=}5..20$, 16 sector pairs, 2 orders, 2 ties); **8** passes, all CD001 ($R{=}7$) |
| Y77: natural trimer/tetramer census | trimer: 4,800 cases, 24 passes, all $R{=}7/7$ open chain; tetramer: 2,592 cases, 48 passes, all $7\text{-}7\text{-}7$ chain |
| Y77: dimer bond-topology atlas | 9,000 seeds; recurrent survivors only at $R{=}5$ (39), $R{=}6$ (32), $R{=}7$ (48, all $\to$ CD001); **D2R5** (4 cross rel.), **D2R6** (3 cross rel.) confirmed new, 16/16 replication each |
| Y77: mixed-bond trimer extension | 216 cases; **144** pass; 6 geometries (T3R65/66/67/75/76/77) pass all 24 discovery contexts; 288/288 translated replication; 24/24 stress |
| Y77: closed-trimer attempt | 1,800 cases seeded with an A–C bond; **16** recurrent survivors, **0** retain any A–C structure — closure fails |
| Y77: frozen composite spectrum | **10** structural candidates: 3 dimers (D2R5, D2R6, CD001) + 6 trimers + 1 tetramer (T4R777); structural $\ge6$ threshold exceeded; inertial population gate still closed (no $\pm v_1$/rest closure yet) |
| Y78: v2→v1 composite closure | D2R5 8/8, D2R6 8/8, T3R65 24/24, T3R66 24/24 **PASS**; CD001 0/8 and all R7-containing trimers 0/24 **factorize** |
| Y78: speed-dependent bond topology | D2R5: 4 cross-rel. at both $v_1,v_2$; D2R6: 3 ($v_2$) $\to$ 1 ($v_1$); R7/CD001 bond not instantiable directly in settled $v_1$ |
| Y78: direct-$v_1$ motif control | R5 8/8, R6 8/8 reproduce exact sector with no deceleration history; R7 0/8 |
| Y78: stationary-rest search (62 words/species, 4 species) | **0/4** species close; per-species split: 41 non-executable, 16 drift, **5** zero-displacement-but-dressing-nonrecurrent |
| Y78: mass-ready species | **0** — moving-sector bottleneck now partly resolved (4/10 species), rest-sector bottleneck isolated as the sole remaining blocker |
| Y79: Y46 monomer control re-certification | **96/96** primary stationary periods, **1200/1200** population periods — exact reproduction of historical result after a path-only import fix |
| Y79: D2R6/T3R66 native rest transfer | D2R6 **16/16** contexts, **800/800** periods, joint halo 99; T3R66 **48/48** contexts, **1440/1440** periods, joint halo 157 — no composite-specific fix needed |
| Y79: R5 residual effect and derived retirement | raw transfer: **+1** joint-halo relation per 8-event period; safe retirement timing found at exactly "immediately after creator's event 4" in every tested context |
| Y79: D2R5/T3R65 closure under derived R5 retirement | D2R5 **16/16** contexts, **800/800** periods, joint halo 97; T3R65 **48/48** contexts, **1440/1440** periods, joint halo 155 |
| Y79: combined confirmatory population | **128/128** contexts, **4480/4480** stationary periods; 0 drift, disconnection, isomorphism failure, or joint-halo flux in any scored period |
| Y79: population accounting | $N_{\text{mass-ready,composite}}=4$ (D2R5, D2R6, T3R65, T3R66); $N_{\text{mass-ready,same-law}}=5$ counting DS001; $\ge6$ firewall needs exactly 1 more same-law identity |
| Y80: moving census, all 8 ordered R5/R6 triples | 656/665/666 **96/96** each; 555/556/565/566/655 all **0/96** (invalid R5 or third-bond seed) |
| Y80: stationary transfer, 3 winners | discovery **288/288** contexts, **5,760/5,760** periods; translated promotion **144/144** contexts, **2,880/2,880** periods; combined **432/432 / 8,640/8,640** |
| Y80: population firewall | 8 same-law complete-manifold identities (DS001 + 7 composites); $\ge6$ threshold **PASS**, including composite-only (7≥6) |
| Y81: Y47 DS001 control replay | exact reproduction: $A(0)=\tfrac34\ln2$, $A(\pm v_1)=A(\pm v_2)=\ln2$, $M_i=\tfrac58\ln2$ |
| Y81: extensive population curvature (8/8 identities) | $M_i^{\text{ext}}(N)=N\tfrac58\ln2$ exact; all odd components vanish; **7,680** synchronized measurements, primary = replication exactly |
| Y81: bond-topology resolution | **0** — every same-$N$ pair/triple exactly degenerate (D2R5=D2R6; T3R65=T3R66; T4R656=T4R665=T4R666); binding residual $=0$ for every composite |
| Y81: independent rest-state audit | **14/14** contexts, **280/280** periods — zero drift, exact recurrence, zero halo flux |
| Y81: G6 verdict | **8/8 PASS** — finite positive extensive $M_i$ on all frozen identities |
| Y82: primary nonportability census | 1,280 challenges (160/species, 2 balanced classes); **0/1,280** recoveries, all losses at first recovery tick |
| Y82: replication nonportability census | 640 challenges (80/species, translated/reversed/alt-tie); **0/640** recoveries |
| Y82: combined result | **0/1,920** recoveries; $\ell_0,\mathcal{R}_{\text{act}},E_0,\alpha$ **not estimated**; $M_i\propto E_0$ untested (not falsified) |
| Y83: Y82 exact reproduction | 1,920/1,920 rows match exactly after vendoring parent dependencies; archived outcome (universal first-tick failure) confirmed |
| Y83: development perturbation atlas (canonical + reversed) | 140 gates each context; **80/80** compatible returns, **60/60** competitor losses, 0 invalid/unresolved/unhandled — identical both contexts |
| Y83: post-freeze translated/reversed validation (blind) | 322 gates, 8 species × 8 phases; **184/184** returns, **138/138** losses, 0 exceptions |
| Y83: constituent-order covariance stress | 1,666 gates across all permutations of 4 dev. identities; **952/952** returns, **714/714** losses |
| Y83: nondegeneracy population check | primary 1,280 trials: 640 return/640 loss; replication 640 trials: 320/320 — genuinely mixed, unlike Y82's universal failure |
| Y84: loss-work scale (development, 160 trials/species) | 320 pooled losses, **all** with $W_{\text{loss}}=0$ exactly $\Rightarrow \ell_0=0$ (not sampling noise) |
| Y84: regeneration phenotype (all 8 identities) | $q_\infty=1/2$ exactly (fixed by challenge weighting, not measured); $\mu_{W\vert\text{return}}=(N-1)/N$ |
| Y84: renewal clock | DS001: exposure $=0\Rightarrow\omega_{\text{renew}}$ **undefined**; composites: $\omega_{\text{renew}}=2\pi N/(N-1)$ |
| Y84: nominal composite $E_0$ | $=2\pi$ exactly for every composite — algebraic cancellation of $R_{\text{act}}$ and $\omega_{\text{renew}}$, not 7 independent measurements |
| Y84: translated/reversed replication | reproduces every element of the failure exactly (same $q_\infty$, $\ell_0$, undefined DS001 clock, $E_0=2\pi$) — structural, not a site/seed artifact |
| Y84: verdict | **FAIL** for the Y5/Y82 construction; G7 **CLOSED, untested** (not falsified); no $M_i$, $\alpha$, or residual opened |
| Y85: historical Y2 work-convention audit | 3,620 trajectories, 1,580 returns; work$=$particle-hits exactly in all cases (612 genuine zero-work returns) — exclusion convention confirmed correct |
| Y85: historical Y4 clock audit | $\omega_{\text{renew}}$ formula reproduces archived value to $<10^{-16}$ on 36/36 rows — **computed on fresh natural history, not challenge trials**; Y84's clock was a second, independent error |
| Y85: exhaustive single-event census (8 species × 8 phases × 2 contexts) | 570 gate-phase instances each; 184 exact returns, 138 immediate losses, 248 disjoint spectators, **0** off-manifold survivors/invalid/unclassified |
| Y85: disjoint-gate spectator test | **496/496** disjoint gates fired as raw rewrites; **0** carrier-signature changes |
| Y85: bounded multi-event vacuum diagnostics | 640 traced events (0 changes, front recedes 8→15); depth-4 BFS (79 states, 0 changes) — diagnostic only, not exhaustive |
| Y85: verdict | **OPEN** — single-event no-go exact; multi-event reachability unresolved; $E_0$ undefined, G7 closed |
| Y86: chronology-quotient bug caught and corrected | fresh-vertex-permutation quotient invalidated by a concrete depth-3 counterexample; all quotiented results quarantined, chronology-exact search used for the binding verdict |
| Y86: chronology-aware search through depth 13 | **528,091** cumulative distinct states; depth-13 frontier **297,285**; **0** bad/inward gates found |
| Y86: complete depth-14 successor audit | **662,627** transitions from all depth-13 frontier states (3-shard cross-check exact); **0** bad gates |
| Y86: relation-provenance / near-miss reduction | 2 candidate bad-gate families; required token co-occurrences **0/15,187** and **0/7,607**; 517 near-miss states, **0** completions on any legal successor |
| Y86: verdict | **OPEN** — very strong bounded negative (0/528,091+ states, 0/662,627 transitions); all-depth theorem **not established**; G7 closed/untested |
| Y88: compositionality gate (6 controls each) | A: 6/6 PASS (max residual $8.9\times10^{-16}$); B: 6/6 PASS (zero residual); C: **2/6 FAIL** (+30 excess, 4 of 6 controls) |
| Y88: Candidate A population law | $E_{0,A}=6N\ln2$ exact; $\Delta E_{A,\rm bind}=0$ for every composite (topology-blind) |
| Y88: Candidate B population values | DS001 47; D2R5 97; D2R6 99; T3R65 155; T3R66 157; T4R656 219; T4R665 219; T4R666 221 |
| Y88: Candidate B binding residuals ($-47N$) | 0, +3, +5, +14, +16, +31, +31, +33; same-$N$ contrasts exactly $+2$ (R6 vs. R5) throughout |
| Y89: Candidate A proportionality fit | $\alpha_A=5/48$ exact; dev./holdout max relative residual both $1.71\times10^{-16}$; Spearman $=1.0$ — algebraically degenerate (shares $A_{\rm dir}$ origin with $M_i$) |
| Y89: Candidate B proportionality fit | $\alpha_B=0.00820$; dev. residual 11.06%, holdout 6.33% — **exact proportionality mathematically impossible** ($M_i$ same-$N$-degenerate, $E_{0,B}$ not) |
| Y90: transition settling ($L$), 60/60 contexts | $L=3$ for every identity — topology-blind |
| Y90: K1 bond law (16-round window) | $+2$/R5 bond, $-58$/R6 bond — but **horizon-contaminated** (R6 mature-rate differs by speed: 6/round at $v_2$ vs. 2/round at $v_1$) |
| Y90: K2 pairwise decomposition | every adjacent bond contributes exactly $2$ count-turnover units regardless of R5/R6 — global topology sensitivity is a cancellation artifact |
| Y90: proportionality to Candidate B | K1: dev. RMSE 7.95, holdout RMSE 43.28 (68.1% max error); K2: dev. RMSE 0.93, holdout RMSE 1.37 (66.1% max error) — **both fail** |
| Y91: mature bond rates (8-round, exact) | R5: 6/round at both $v_1,v_2$; R6: 6/round ($v_2$) $\to$ 2/round ($v_1$) |
| Y91: forward $v_2\to v_1$ impulse (exact, H≥3) | $J_{\rm id}(\text{R5})=+2$, $J_{\rm id}(\text{R6})=0$; $J_{\rm count}=+2$ both bonds |
| Y91: reverse $v_1\to v_2$ | **56/56** composite contexts need $L=4$ (not preregistered 3) — **fails horizon gate**; diagnostic H≥4 values: R5 $+2$ (reciprocal), R6 $-4$ (**non-reciprocal** vs. forward $0$) |
| Y91: mature-$v_2$ direct reversal | **0/60** executable (Y56 turnaround nonportable for composites) |
| Y91: signed $v_1$ reversal (exact, 60/60) | $J_{\rm id}(\text{R5})=-2$, $J_{\rm id}(\text{R6})=+2$ |
| Y91: verdict | binding-inertial impulse **NOT PROMOTED**; Candidate B firewall held (never unsealed) |
| Y92: four relaxation clocks (exact, population-wide, phase/dwell-invariant) | $L_{\rm life}=2$; $L_{\rm speed}=3$ (both directions); $L_{\rm bond}$: $v_1\to v_2$ = 4, $v_2\to v_1$ = 3 (R5 present) / 2 (all-R6) |
| Y92: full-dressing clock law | $L_{\rm full}^{v_1\to v_2}=3N-1$; $L_{\rm full}^{v_2\to v_1}=6N-5$ (R5 present) / $6N-4$ (all-R6); DS001 $=4$ both directions |
| Y92: native reversal exact-dressing reciprocity | DS001 4/4, D2R6 8/8 (exact); D2R5 0/8, T3R65 0/8, T4R656/T4R665 0/8 (non-reciprocal); T3R66 4/8 (split) |
| Y93: closed-loop macroscopic recovery | 120/120 FULL loops exact on speed/sign/geometry/bond/lifecycle; **0/60** exact full dressing at closure |
| Y93: transient residual laws | $\Delta_{\rm rel}(0)=9N^2$ (9,36,81,144); $\Delta_{\rm rel}(16)=3N(2N+1)$ (9,30,63,108) — both exact, topology/sign/order-independent |
| Y93: extended persistence | all-R6 ladder 16/16 exact at round 32 (through 128); R5-containing 16/16 at round 32 (through 64); reversed order 28/28 exact |
| Y94: endpoint touch census (5,364 residual relations) | **100%** touch exactly one constituent core — 0 pair-touch, 0 triple+ — quadratic identity is not microscopic pair dressing |
| Y94: directed one-body burden laws (180/180 each) | $B_0(j)=6N+3+6j$ (endpoint); $B_{16}(j)=12(N-j)-3$ (round 16) — direction reverses between the two |
| Y94: universal closure clock | $R_{\rm close}=15+3N$ exact (18,21,24,27 for N=1..4), topology/sign/order-independent, stable through 40-round horizon |
| Y94: provenance/topology redistribution | $L_3=N+6W_5$ (R5 cut-weighted), $\text{PRE}+L_3=3N(N+1)$ — R5 topology reroutes wake origin, not total size; rounds 3–15 cleanup-rate difference unexplained |
| Y95: preflight lineage audit | `Sim` retains relations/indexes/gates/fresh-vertex counter/scheduler state; **no** persistent relation-instance→producer-event map |
| Y95: rescue attempts checked and rejected | Y68 `_aff()`/`_gf()`: witness-set membership, not a producer map; Y94 provenance logger: prospective-only monkey-patch, labels pre-existing relations `PRE` |
| Y95: verdict (preflight) | **STOPPED at Section-2 preflight** per frozen kill condition; E1/E1_mult/compositionality/population/E2 **not attempted**; `Mi`, Candidate A, Candidate B, $\alpha$ sealed |
| Y96: passivity regression (checkpoint-level, not endpoint-only) | vacuum 1,800 events/1,801 checkpoints; moving 9,600 checkpoints/18,720 fresh IDs (60 contexts); rest 7,917 checkpoints/12,472 fresh IDs (8 identities) — **0 mismatches** in every category |
| Y96: sufficiency audit | 20,636 core events; **100%** have exactly 3 identified live input instances, all correctly marked consumed afterward |
| Y96: archived-output anchor | 8/8 baseline and 8/8 instrumented contexts exactly reproduce archived Y90 response outputs |
| Y96: verdict | **PASS** — recorder dynamically passive on full regression corpus; Y95 instrumentation blocker cleared |
| Y95 (resumed): compositionality gate | 6/6 controls exact (joint = isolated sum, 0 cross-relations/gates, 0 seed flux); stabilizes by 2-period window in 30/30 contexts |
| Y95 (resumed): period-boundary population result | $E1_{\rm recurrent}=4N$, $E1_{\rm mult}=5N$ exact in all 30 sign/context/order measurements; $E2=0$ for every composite |
| Y95 (resumed): frontier-collapse diagnostic | producer/consumer map not injective — exactly $N$ shared event-pairs per context; $5N$ dependencies → $4N$ unique edges; `E1_mult` collapses, $E1$ does not |
| Y95 (resumed): literal foliation sweep | all 11 phase cuts valid antichains, all stabilize; **30/30 contexts PHASE-DEPENDENT** — promotion blocked |
| Y95 (resumed): R5 phase-localized signature | exact +1 unique causal edge at $\phi=e3$ and +1 at $\phi=h1\_bridge$ for every one-R5 composite, 30/30 exact; T4R656/T4R665 (different R5 placements) have identical profiles |
| Y95 (resumed): verdict | **E1 NOT PROMOTED** (phase-dependent + zero binding residual at tested boundary); `Mi`, Candidates A/B, $\alpha$ remain sealed |
| Y97: frozen candidate baseline | $\mathcal{F}_{\rm DS001}=20$ (10 deduplicated phase cuts, `e7`≡`start` excluded) |
| Y97: N=5 v1 transient correction | all-R6 control settles exact period-1 only from round 26 (vs. N=4's earlier settling); 32-round burn frozen for all N=5 geometries before re-census |
| Y97: N=5 blind structural census (16 ordered $\{5,6\}^4$ words) | exactly **4** complete-manifold holdouts: 1 all-R6, 3 one-R5 (positions 1/2/3); **0** multi-R5 survivors under left-to-right seeding |
| Y97: holdout population result (8/8 contexts exact) | all-R6: $\mathcal{F}=100=20N$, $\Delta\mathcal{F}=0$; all 3 one-R5 placements: $\mathcal{F}=102$, $\Delta\mathcal{F}=+2$ |
| Y97: holdout phase-residual localization | exact $(0,0,0,0,0,{+1},{+1},0,0,0)$ for all 3 R5 positions after subtracting 5 independent DS001 profiles — matches Y95's development-population localization exactly |
| Y97: original-population consistency (checked only after holdout freeze) | DS001 20; D2R6/D2R5 40/42; T3R66/T3R65 60/62; T4R666/T4R656/T4R665 80/82/82 — same $20N(+2\ \text{if R5 present})$ law throughout |
| Y97: verdict | holdout **PASS**; presence-sensitivity **PASS**; position-independence **PASS**; phase localization **PASS**; per-bond additivity **UNRESOLVED**; promotion **DEFERRED** |
| Y98: N=5 formation-order search | 11 multi-R5 geometries × 24 seed-order permutations = 264 trials; **0/264** legal qualifiers |
| Y98: N=6 fallback census | 26/26 two-plus-R5 words seed-illegal; 0 multi-R5 qualifiers; only 4 one-R5 + 1 zero-R5 words legal |
| Y98: parity theorem | 112/112 R5 placements (N=5+N=6) predicted exactly by one parity rule; all 56 failures exactly `duplicate_endpoint+core_collision` — proven, not empirical, single-R5-per-chain exclusion under simultaneous seeding |
| Y99: sequential-phase multi-R5 formation | **11/11** N=5 geometries qualify, **22/22** primary+replication contexts exact ($n_{R5}=2,3,4$) — parity exclusion is formation-slice-specific, not dynamical |
| Y99: additive causal-flux law (promoted) | $\mathcal{F}=20N+2n_{R5}$ exact, 22/22; $H_{\rm add}$ **22/22 PASS**, $H_{\rm sat}$ **0/22 PASS**; phase residual $+n_{R5}$ at e3/h1_bridge only |
| Y100: same-$N$ topology gate | **FAIL** — $M_i({\rm D2R5})=M_i({\rm D2R6})$ vs. $\mathcal{F}({\rm D2R5})-\mathcal{F}({\rm D2R6})=2$ (and identically for T3R65/66, T4R656/665/666) |
| Y100: binding-residual gate | **FAIL** — $\Delta M_i\equiv0$ vs. $\Delta\mathcal{F}=2n_{R5}$; no nonzero global $\alpha$ satisfies both |
| Y100: Candidate A/B diagnostics | A: exactly $\propto M_i$ (same extensive degeneracy); B: topology-sensitive but **opposite sign** to $\mathcal{F}$ on every same-$N$ contrast ($\Delta{\rm B}=-2$ vs. $\Delta\mathcal{F}=+2$) |
| Y100: verdict | $M_i=\alpha\mathcal{F}$ **FAIL_STRUCTURAL** — not a falsification of causal flux or mass-energy equivalence, but of identifying current $M_i$ with $\mathcal{F}$ |
| Y101: moving-sector causal edge-displacement | $P_{\rm edge}=Nv$ exact, 32/32, sign-odd |
| Y101: rest-zero gate | **FAILS 0/8** — $P_{\rm edge}({\rm rest})=\tfrac52N\sigma$, order-independent (8/8 diagnostic), distributed across full cycle |
| Y101: verdict | **NOT_MOMENTUM** — real translational current contaminated by independent internal orientation circulation; R5/multi-R5 never opened |
| Y102: Amendment A (exterior-cut geometry fix) | initial cut could sit inside Y46 rest excursions; corrected to sit outside a calibration-measured envelope |
| Y102: corrected rest-zero result | **128/128** exact zero, fully lineage-clean — circulation removed without subtraction |
| Y102: speed-resolution gate | **FAILS 0/8** — $J_{\rm ext}(v)=N\,{\rm sgn}(v)$ identical at $\lvert v\rvert=1,2$; decomposition shows discarded span is exactly the missing speed information |
| Y102: verdict | **EXTERIOR_CURRENT_NOT_MOMENTUM** |
| Y103: span-weighted exterior flux (all gates) | $K_{\rm ext}=Nv$ exact: 32/32 moving, 128/128 rest exactly zero; $M_K=N$, $\Gamma_K=0$, no fitting |
| Y103: topology holdout (R5 + all 11 Y99 multi-R5) | 32+44 moving rows exact on $K_{\rm ext}=Nv$; 64+176 rest rows exactly zero; $M_K=N$ for every topology incl. four-R5 `5555` |
| Y103: verdict | **PROMOTE_SPAN_MOMENTUM_TOPOLOGY_BLIND** — $\Delta M_K\equiv0$ vs. $\Delta\mathcal{F}=2n_{R5}$ (exact, e.g. $0$ vs. $8$ for `5555`) |
| Y104: Method Correction A | same-event ($p=c$) relation turnover correctly excluded from causal-parent set (legitimate Y46 intra-event behavior, not a lineage bug) |
| Y104: causal-depth clock (all gates) | $C_{\rm move}=1$, $C_{\rm rest}=10$ exact across 256+64 validation and 608+152 holdout rows — unchanged even for `5555` |
| Y104: mechanistic cause | 100% audited moving updates have exactly one causal parent (same constituent's prior update); **zero** cross-constituent causal parents — no channel for R5 to enter this clock |
| Y104: verdict | **CAUSAL_CLOCK_VALID_TOPOLOGY_BLIND** — $\alpha_\tau=20$ reproduces all-R6 exactly; $\Delta M_\tau\equiv0$ vs. $\Delta\mathcal{F}=2n_{R5}$ (up to 7.4% at `5555`) |
| Y105: launch executability | 320 cases; 240 legal (`start`, `h1_bridge`, `e4`); **all 80 `e3` launches non-executable**, incl. DS001/all-R6 (surface property, not R5-specific) |
| Y105: cross-constituent causal transport | **0/240** on every measure (event pairs, multiplicity, tagged pairs/multiplicity, tagged bond-relation multiplicity) — no R5 excess transported |
| Y105: scar-fate audit (10 instances, D2R5 + `5555`) | continued rest: **10/10** consumed by `R5_SCAR_RETIRE` at e4; boost from h1_bridge: **0/10** consumed, **10/10** still live at scored endpoint |
| Y105: N=5 $v_2$ dressed-settlement law (72/72 exact) | $L_{\rm start}=17-\lfloor n_{R5}/2\rfloor$, $L_{h1}=19-\lfloor n_{R5}/2\rfloor$, $L_{e4}=19-\lceil n_{R5}/2\rceil$ — more R5 settles **faster** |
| Y105: canonical moving-dressing equality | **26/26** exact (D2R6, D2R5 all phases/speeds/contexts; `5555` targeted h1_bridge→v2) — final moving state independent of launch path |
| Y105: verdict | **NO_BINDING_EDGE_TRANSPORT** + **R5_DEPENDENT_BOOST_RELAXATION**; rest excess reframed as cleanup-path-dependent, not conserved |
| Y106: historical-control reproduction | **1,800/1,800** exact match to Y77; 16 recurrent survivors, all lost A-C, all reduce to ordinary T3R77 |
| Y106: Phase A (single-relation A-C seeds) | 10,800 cases, 6 bases × 4 contexts × 450 seeds; **0 CLOSED**; all 8,200 legal candidates lose A-C by first scored boundary |
| Y106: Phase B (full R5/R6/R7 motif/subset transfer) | 1,104 cases; **0 CLOSED**; same failure mode across all three bond-motif classes |
| Y106: Phase C (formation-order + timing) | 1,728 histories (6 orders × 2 orientations × 2 timings); **0 CLOSED**; 624/624 scored cases show AB+BC persist, A-C alone absent |
| Y106: combined census | **13,632** new discovery cases (15,432 incl. historical control); **0** closed $K_3$ species found anywhere |
| Y106: verdict | **NO_CLOSED_K3_IN_FROZEN_Y106_CENSUS** — census-bounded null, not a theorem; no mass/energy observable opened |
| Y107: causal-order test | producer-after-consumer violations **0/624**; directed DAG cycles **0/624**; A-C causal age mixed (25.6% older, 38.9% newer, rest mixed) — no forbidden orientation |
| Y107: causal-renewal test | A-C MOVE-generated births **0/624**; A-C seed consumed by MOVE **0/2,160**; A-C seed-to-MOVE descendants **0/624** — closure causally sterile |
| Y107: seed-fate audit | **2,160/2,160** instances still live but 0/2,160 still cross-core — all become stationary wake, none deleted |
| Y107: exact closure lifetime | $L_{AC}({\rm R6})=L_{AC}({\rm R7})=1$ macro-round; $L_{AC}({\rm R5})=2$ — denser weave persists one round longer, still zero renewal |
| Y107: adjacent-bond renewal (control) | AB MOVE births **3,600**; BC MOVE births **2,400** — true bonds regenerate; attempted A-C never does |
| Y107: verdict | **CAUSAL_RENEWAL_FAILURE_WITHOUT_ORDER_CYCLE** — nonlocal closure lacks renewable causal contact, not a causal-order violation |
| Y108: branch-conditioned crossing count (42/42 exact) | $C_{\rm REST}=2N+n_{R5}$; $C_{v_1}=C_{v_2}=2N$; identical for all 7 tested identities, both contexts |
| Y108: identical-instance scar fate (36 rows) | continued rest: **12/12** consumed by `R5_SCAR_RETIRE`; moving futures: **0/24** consumed, **24/24** still live at 32 rounds — same cloned instance, different fate |
| Y108: dwell-accumulation test (40/40 exact) | $S(k)=k\mathcal{F}_1$ exactly for $k=1,2,4,8,16$; recurrent boundary state bit-identical every cycle while integrated activity grows linearly |
| Y108: verdict | **RECURRENT_ACTION_SUPPORTED** — R5 term is trajectory-dependent causal action, not a conserved state quantity; $20N$ baseline's status remains open |
| Y109: candidate population | 4 state-defined inventories ($H_{\rm joint}$, $H_{\rm single}$, $H_{\rm cross}$, $H_{\rm inc}$) × 10 identities × 10 phase cuts × 2 cycles; **440** current-state phase rows |
| Y109: DS001 phase profile ($H_{\rm joint}=H_{\rm single}=H_{\rm inc}$) | $(47,48,74,116,117,92,92,120,117,67)$ — swings **47→120** within one cycle; `e7` returns exactly to 47 |
| Y109: $H_{\rm cross}$ bond-phase law (110/110 exact) | ordinary phases: $4n_5+n_6$; at `e0`,`e4`: $4n_5+2n_6$ — exact, reproducible, but not conserved (fails only where R6 present) |
| Y109: second-cycle substrate check | $H_{\rm joint}/H_{\rm single}/H_{\rm inc}$ do **not** repeat mid-cycle values cycle-to-cycle (e.g. DS001 e0: 74→75) despite exact `start` recurrence; $H_{\rm cross}$ repeats exactly |
| Y109: canonical-phase Y88 consistency | exact reproduction of all 8 original Candidate-B values + 2 new N=5 controls (N5R6666: 291; N5R5555: 283) |
| Y109: verdict | **NO_STATE_DEFINED_CONSERVED_INVENTORY_IN_Y109_FAMILY** — candidate-family null, not a theorem; $M_i$ never unsealed (all 4 candidates failed gate 1) |
| Y110: phase-conservation across nested shells | $J_0,J_G,J_1,J_2$ all **0/20**; relative oscillation shrinks $82\%\to61\%\to5.2\%$ but never reaches 0 |
| Y110: gate-closure redundancy | $J_G=J_0$ in **440/440** states — no hidden gate-side relation reservoir |
| Y110: inner vs. outer recurrence split | $J_0,J_G$ return exactly every cycle (**20/20**); $J_1,J_2$ drift upward every cycle (**20/20** each) despite exact carrier recurrence |
| Y110: wake-growth law | $\Delta J_1=5N-n_{R5}$, $\Delta J_2=22N-n_{R5}$, $\Delta(J_2-J_1)=17N$ — exact, 20/20, topology-independent in the difference |
| Y110: verdict | **NO_CONSERVED_BOUNDED_REWRITE_NEIGHBORHOOD_IN_Y110_FAMILY** — $M_i$ sealed |
| Y111: vacuum-control qualification | age/site-matched construction; **20/20** G0 pass (base equality, exact index match, exact particle recurrence) |
| Y111: vacuum-subtracted phase conservation | $X_0,X_G,X_1,X_2$ all **0/20** — subtraction shrinks but does not remove oscillation |
| Y111: gate-closure redundancy (post-subtraction) | $X_G=X_0$ in **440/440** states |
| Y111: inner-excess recurrence vs. outer drift | $X_0,X_G$ exact 20/20 cycle-to-cycle; $X_1,X_2$ **0/20** — matched vacuum itself returns exactly (20/20), isolating drift as particle-induced |
| Y111: canonical quadratic excess law | $X_0({\rm start})=3N^2-1+n_{R5}$ exact, 20/20 — new scaling, explicitly non-extensive |
| Y111: wake-growth law survives subtraction | identical to Y110: $\Delta X_1=5N-n_{R5}$, $\Delta X_2=22N-n_{R5}$, both 20/20 |
| Y111: verdict | **NO_CONSERVED_VACUUM_SUBTRACTED_EXCESS_IN_Y111_FAMILY** — three distinct quantities now separated (canonical excess, Y108 action, particle-induced wake); none conserved |
| Y112: motif basis | 80-dim, combinatorially exhaustive (5 vertex classes + $5\times\binom{6}{2}=75$ relation motifs) |
| Y112: development nullspace | 464 transitions (vacuum+DS001 rest/v1/v2); rank 16; nullity 64 |
| Y112: holdout validation (the key safeguard) | 18 composite trajectories, 360 transitions; of 64 canonical directions, 5 touch dynamic coordinates and **0/5 survive holdout** — narrow-corpus "laws" fail on real composites |
| Y112: naive multiset-count check | $4V-R$ exact on 256/256 vacuum-only fires but only 300/824 full population; $5V-R$ only 44/824 — neither a real invariant |
| Y112: post-verdict active-subspace result | 21 dynamic motif columns, rank 19 $\Rightarrow$ exactly **2** surviving null directions across full 824-transition population |
| Y112: surviving laws | $I_{\rm out}=8N$, $I_{\rm in}=16N=2I_{\rm out}$ — exact on all 824 transitions, but identical for R5/R6 at fixed $N$ |
| Y112: verdict | **NO_NONTRIVIAL_DIRECT_GRAMMAR_INVARIANT_PROMOTED**; **CONSTITUENT_NUMBER_INVARIANTS_FOUND**; **NO_STATE_DEFINED_RECURRENCE_ENERGY_IN_Y112_80D_BASIS** — proof within this basis, not merely another failed guess; $M_i$ sealed |
| Y113: P20 direct-promotion basis | development rank 8, nullity 12; **12/12** canonical directions survive holdout algebraically; only dynamic law is $P_Q+P_{\rm BRIDGE}=N$ (constituent number again) |
| Y113: $P_{O1}-P_{O3}$ direction | phase-invariant but **not** replication-invariant ($-2N$ primary vs. $0$ reversed) — preparation history, not a species scalar |
| Y113: P20 verdict | **NO_NONTRIVIAL_DIRECT_PROVENANCE_INVARIANT_PROMOTED** |
| Y113: PT50 diagnostic (full population, 19 active features) | rank 14, nullity 5; one qualitatively new direction found |
| Y113: bond-content invariant $I_{\rm bond}$ | $=P_{O1,T2}+P_{O3,T2}=n_{R6}+3n_{R5}$; exact in **396/396** held-out states, both cycles, all phases, primary+replication |
| Y113: exchange structure (not a static count) | D2R6: $(P_{O1,T2},P_{O3,T2})$ swaps $(0,1)\leftrightarrow(1,0)$ at e0/e4, sum fixed at 1; D2R5: fixed $(1,2)$, sum 3 |
| Y113: companion identity | $P_{O1,T2}=P_{O7,T2}$ exact, 396/396 |
| Y113: verdict | state-defined, phase-invariant, topology-**and**-multiplicity-sensitive candidate found — **not yet promoted** (coefficients from full-population diagnostic, not blind development derivation; untested outside mature rest; presupposes constituent-core decomposition); frozen unchanged for blind Y114 test; $M_i,\alpha$ sealed |
| Y114 Gate A: unused N=5 rest holdout | **440/440** exact, $I=3n_{R5}+n_{R6}$; position-independent, count-only |
| Y114 Gate B: moving-sector transfer | frozen sector-independent prediction: 336/608; post-verdict sector law $I(v_1)=3n_{R5}+n_{R6}$, $I(v_2)=3n_{R5}+2n_{R6}$: **608/608** exact |
| Y114 Gate C: identical-state branch (Y108-style) | $v_1$: rest value preserved 16/16 rounds; $v_2$ (R6-containing): value switches synchronously on **round 3** — matches Y92's independent $L_{\rm speed}=3$ clock |
| Y114 Gate D: formation lifecycle | scaffold count already at mature value **before** explicit seed in Y101 histories; seed-ablation: **4/4** primary/replication cases converge to identical mature signature with no seed at all — doesn't contradict Y77's broad null, narrows what "formation" has actually been tested |
| Y114 Gate E: noninteracting additivity | **176/176** exact, zero inter-object cross-relations/gates |
| Y114 dissociation subtest | recorded **unavailable** (no lawful frozen breakup trajectory exists) rather than faked |
| Y114 verdict | **BOND_CONTENT_INVARIANT_NOT_FULLY_VALIDATED**; post-verdict **EXACT_KINEMATIC_CROSS_SCAFFOLD_LAW**; reclassified as order parameter, not universal conserved content; $M_i,\alpha$ sealed |
| Y115 Tier 1/2: complement search | 17 active features, coeffs $\pm1,\pm2,\pm3$; 1-channel **0/0** candidates; 2-channel **0** candidates — no exchange partner found |
| Y115 Tier 3: nullspace diagnostic | rank 14, nullity 5; simplest new-looking solution reduces exactly to already-rejected $P_{O3}-P_{O1}$ (preparation-dependent, not new) |
| Y115 boost-event lineage audit (D2R6) | round 2→3: **0** O1/O3-T2 births, **0** deaths; 2 relations cross into $T_2$, 1 crosses out — same instance IDs throughout |
| Y115 population incidence law (16/16 rows, N=2–5) | $J_{\rm in}=2(N-1)$, $J_{\rm out}=2(N-1)-n_{R6}$, $B=D=0$, $\Delta I=n_{R6}$ exact |
| Y115 R5 control (D2R5) | 2 in / 2 out, **zero** net change — confirms R6 creates an outflow imbalance, not extra inflow |
| Y115 verdict | **NO_SIMPLE_PROVENANCE_EXCHANGE_INVARIANT** (primary); **EXACT_R6_INCIDENCE_MIGRATION_LAW** (post-verdict) — $I_{\rm scaffold}$ reclassified from candidate stored content to moving-boundary incidence current; $M_i,\alpha$ sealed |
| Y116 continuity audit | $\Delta I=J_{\rm in}-J_{\rm out}+B-D$ exact **1,680/1,680**; $B=D=0$ in all **1,596/1,596** non-formation rows |
| Y116 sector constitutive law | $J_{\rm rest/v1}=2n_{R5}+n_{R6}$ (304/304), $J_{v2}=2n_{R5}+2n_{R6}$ (304/304); sector gap localizes entirely to $+1/{\rm R6}$ bond |
| Y116 rest-to-v2 step response | round 2 low-current; round 3 $J_{\rm in}$ switches, $J_{\rm out}$ lags one round ($\Delta I=n_{R6}$); round 4 $J_{\rm out}$ catches up — Y115 prediction **38/38** exact incl. all 12 N5 chains |
| Y116 affine-law discovery/validation | 80 exact discovery candidates; **72/80** blind-validate; 8 failures confined to first-cut scheduler transients (e0/e4/branch-round-1), zero occupancy effect |
| Y116 formation reinforcement | mature current reached by preseed round 7; explicit seed changes **0/4** current variables; 48/48 post-seed rounds source-free at mature value |
| Y116 post-verdict all-native ($O_0$–$O_7$) ladder | exact **608/608**: $v_1$ future makes a round-trip excursion ($+n_{R6}\to-n_{R6}\to 3M{-}2n_{R6}$); $v_2$ future rises twice ($+n_{R6}$ at r1, plateau, $+n_{R6}$ at r3 $\to 3M$) |
| Y116 verdict | **EXACT_SECTOR_DEPENDENT_INCIDENCE_CURRENT_LAW** (primary); **EXACT_TWO_STAGE_NATIVE_CURRENT_LADDER** (post-verdict); standard-physics-vocabulary reading included as explicit structural analogy only; $M_i,\alpha$ sealed |
| Y117 locality audit | **1,596/1,596** global transitions reconstructed from slots; **5,292/5,292** local continuity rows exact; **0** nonlocal/nonadjacent/multi-core/slot-to-slot events |
| Y117 mature v1/v2 slot validation | **888/888** each; R5 $(I,J)=(3,2)$ unchanged across sectors; R6 $(1,1)\to(2,2)$ |
| Y117 round-3/round-4+ validation | round 3: **111/111** exact ($1\to2$, $J_{\rm in}{=}2$, $J_{\rm out}{=}1$); round 4+: **555/555** exact |
| Y117 position/neighbor independence | **32/32** slot-position groups exact; **72/72** neighbor-environment groups exact |
| Y117 scheduler transients | **4,534/4,662** exact; 128 misses confined to 4 preregistered cuts (rest e0/e4, branch r1), R5-replication only; 2-cut integrated total still exactly 3 either ordering |
| Y117 O-index-free reclassification | 2 structural gate-incidence patterns (no numeric O-label); exact in **23,776/23,776** combined events, 0 false pos/neg |
| Y117 verdict | **EXACT_ADDITIVE_BOND_LOCAL_TRANSFER_LAW** (primary); **O_INDEX_FREE_GATE_INCIDENCE_RELAY_EQUIVALENCE** (post-verdict) — whole-chain problem reduced to 2 local objects (R5, R6); $M_i,\alpha$ sealed |
| Y118 discovery automaton | 84 rows → **56** unique keys, **0** nondeterministic; 4 microstates: $R5{=}(1,2)$, $R6_W{=}(0,1)$, $R6_X{=}(1,0)$, $R6_{XW}{=}(1,1)$ |
| Y118 blind N5 validation | state membership/transition **4,032/4,032**; $I_6{=}1{+}q_6$ **1,680/1,680**; mature $J_6$ **640/640**; round-3 edge **40/40**; full outputs **2,880/2,880** (promoted domain) |
| Y118 verdict | **FINITE_LOCAL_RELAY_AUTOMATON_VALIDATED**; secondary **R6_ONE_BIT_CHANNEL_STATE**; 112/4,032 misses = known R5 scheduler transients only |
| Y119 literal grammar check | exactly 2/8 native Y33 outputs satisfy X/W; rest-suppression mask $\{1,3\}$ = exactly X,W — $B{=}D{=}0$ confirmed from grammar text |
| Y119 order-bit closure | 112 unique $(bond,S,phase,\kappa)$ keys, 0 nondeterministic; blind N5: **4,032/4,032** exact, all 112 Y118 misses corrected, 0 new state |
| Y119 minimization | role-resolved: **4** states exactly minimal; constitutive: **3** states exactly minimal |
| Y119 verdict | **SYMBOLIC_LOCAL_TRANSDUCER_CLOSED_WITH_ORDER_BIT**; scope **ON_MANIFOLD_PHASE_PROGRAM_THEOREM** (conditional, not universal) |
| Y120 nonlinear-edge legality | 88 attempts; **30/88** legal (all 44 R6 illegal; 30/44 R5 legal) |
| Y120 realization test | **0/30** legal seeds ever enter a Y119 relay state; 180/180 stuck at $(0,0)$; raw weave gone by round 2 in **30/30** |
| Y120 tree-edge control | **26/26** baseline exact; **492/492** scored transitions exact; **180/180** pair-current reconstructions exact; global $J{=}2(N{-}1)$ unchanged |
| Y120 verdict | **NONLINEAR_EDGE_FAILS_AT_RELAY_REALIZATION**; companion **EXISTING_TREE_TRANSDUCER_UNAFFECTED** |
| Y121 geometric packing census | 16 subsets; largest disjoint neighbor set **2**; all 4 degree-3 subsets illegal by 4-vertex support overlap, before any dynamics |
| Y121 dynamical saturation | $6$-$5$/$6$-$6$: **48/48** form, **768/768** edge transitions exact, **0/768** multi-core relays; $5$-$5$/$5$-$6$: **48/48** fail (left-R5 seed geometry, not competition — right R5 coexists fine in $6$-$5$) |
| Y121 verdict | **GEOMETRIC_COORDINATION_BOUND_Z2** ($z_{\max}=2$) — packing fact, explicitly not a dynamical exclusion law |
| Y122 graph-local atlas | 50 candidate supports (30 oriented classes), built with **no** scalar-offset criterion; primary screen **6** perfect passes |
| Y122 full validation | **4** robust bidirectional contacts (8/8 each) — exactly the historical $\{-6,-5,+5,+6\}$; 2 novel contacts direction-conditioned (pass one sign only) |
| Y122 compatibility graph | **4/4** opposite-side pairs pass **48/48** contexts, **288/288** macro-rounds, **576/576** edge transitions; graph $=K_{2,2}$, $\omega=2$ |
| Y122 verdict | **GRAPH_LOCAL_COORDINATION_BOUND_Z2_SUPPORTED**; scope **FINITE_ON_MANIFOLD_GRAPH_SHELL_RESULT** — bound now independent of scalar coordinate choice |
| Y123 radius-4 census | 152 candidates (50/50/50/2 by distance 1–4); full validation **4** bidirectional, **2** positive-only, **6** negative-only, **140** nonrenewable |
| Y123 radius boundary | outer-shell (dist $\ge2$): **0/204** pass at each of 3 centers (700/500/900); translated survivor classes **24/24** exact |
| Y123 static-signature no-go | candidates 81/82: identical role hash, different class — **GRAPH_ROLE_LOCALITY_PREDICTOR_NOT_CLOSED** |
| Y124 causal-age key | Tier-1 continuity bit: 12/12 dev. but 5/140 false holdouts; Tier-2 ordered slip $\eta$: **12/12** dev., **140/140** holdout, **152/152** total |
| Y124 translation/dynamic validation | static key **304/304**; dynamic class agreement (incl. new radius-1 holdout replay) **304/304** |
| Y125 producer spine | $w(E_n){=}v(E_{n+1})$ **1799/1799**; gate-ancestry lag $(3,5,2,4,1)$ **1795/1795**; input-producer pattern **1798/1798** |
| Y125 ancestry-derived $\xi$ | $\xi=\eta$ in **152/152**; closes atlas **152/152**; translated (500/900/1100) **456/456**; new center-1100 dynamic **152/152** |
| Y126 minimization | scalar-total Tier-0 fails (2/140 false); relation-block $R$ (7 cat.) succeeds where gate-block does not; exhaustive 21-feature search → unique 2-feature solution |
| Y126 explicit state | $\Sigma=(\xi,A,B)$; center-700 **152/152** exact; translated (500/900/1100) **456/456** |
| Y127 transplant test | $P_+/P_-$ direct insertion: **0/304** legal entry gates (vs. P157's 1 each) |
| Y127 mature-section test | unchanged 12-key table on 16 known-good genuine mature trajectories: **0/16** correct — $(A,B)$ section-dependent, not phase-invariant |
| Y127 verdict | **UNCHANGED_SIGMA_NOT_PHASE_PORTABLE**; interpretive **CONTACT_STATE_REQUIRES_LIFECYCLE_PHASE_TRANSPORT** |
| Y128 root-ancestry pullback | dev **16/16**; executable primary **154/154**; complete historical **304/304**; 6-round stability **112/112**; translated (500/900/1100) **48/48**; post-verdict center 1300 **16/16** |
| Y128 wake-vs-interface split | **0/16** mature cross-core relations carry original root ancestry — all transported information sits in the wake, never the interface |
| Y128 verdict | **ROOT_ANCESTRY_PHASE_PULLBACK_CLOSED**; **PHASE_COVARIANCE_REQUIRES_CAUSAL_WAKE_MEMORY**; caveat **NOT_YET_AN_AUTONOMOUS_CURRENT_STATE_LAW** |
| Y129 rejected candidates | raw radius-2 topology: candidates 77/78 collide (identical signature, different $(A,B)$); compact producer key: 16/16 dev but **16/154** executable — rejected without refit |
| Y129 fossil reconstruction | 5-vertex/9-relation fossils detected **154/154**; $\xi$ **154/154**; $(A,B)$ **154/154** (9/154 need 1-generation repair for $A$, $B$ never); sign prediction **154/154**; historical **304/304** |
| Y129 mature-horizon audit | 24 additional rounds, 400 section rows: reconstruction **400/400**; both fossils persist **400/400** |
| Y129 locality law | $R_{\max}(r)=3+\lceil r/3\rceil$ exact for all 25 measured sections ($r=0..24$), growing 3→11 — no fixed radius suffices |
| Y129 translation | 4 centers (500/900/1100/1300): **64/64** reconstruction, relay, lineage; translated nonrenewable control **40/40** (incl. 24 historically-nonpassing rows) |
| Y129 verdict | **PASSIVE_ROOT_ID_ELIMINATION_CLOSED** (primary); **NO_FIXED_RADIUS_INTRINSIC_WAKE_STATE** (secondary); **FORMATION_MEMORY_RECEDES_IN_CAUSAL_WAKE** (interpretive) |
| Y130 constitutive future equality | **192/192** center 700, **192/192** center 500, **384/384** combined — history-independent from the first scored mature boundary |
| Y130 graph-dressing convergence | strict Gate A: only $R{=}0$ passes globally; worst-case first convergence $(R0,R1,R2,R3)=(0,1,3,6)$, exact at both centers; matched continuation **332/332** |
| Y130 verdict | **MATURE_RELAY_STATE_CONSTITUTIVELY_SUFFICIENT**; companion **FORMATION_DRESSING_SHEDS_OUTWARD_FROM_COMOVING_CORE**; scope **FINITE_MATURE_V2_R5_R6_FORMATION_MEMORY_SHEDDING_RESULT** |
| Y131 S1 (fossil deletion, 18 relations/history) | **416/416** local states, **384/384** transitions — zero measured effect; pre-freeze bug (31 vs. 18 deleted) caught and discarded before any output |
| Y131 S2 (fossil-star deletion, 89–109 relations/history) | Y119/transitions **416/416**/**384/384** exact; strict full-local **412/416** (2 histories, round-0-only, outermost radius) — promoted as constitutive, not complete invisibility |
| Y131 S3 (exterior-cut control, thousands of relations) | real, delayed, radius-dependent backreaction; $R{=}3$: first deviation round 2, reaches Y119 state round 11 — schedule exact at both centers |
| Y131 verdict | **FORMATION_FOSSIL_CAUSALLY_DECOUPLED_ON_TESTED_MATURE_HORIZON**; **FOSSIL_STAR_NO_CONSTITUTIVE_BACKREACTION_THROUGH_12_ROUNDS**; **FINITE_ENVIRONMENTAL_BACKREACTION_REACH_DETECTED** |
| Y132 permanent-cut population | 96 branches (16 hist. × R4/5/6 × 2 centers), 2,880 transitions; **96/96** executable/lineage-clean through 30 rounds; gate/displacement **2,880/2,880** CONTROL-exact throughout |
| Y132 shell-entry timing (R=6, exact both centers) | R6:2, R5:4, R4:7, R3:9, R2:12, R1:14 — **48/48** history/radius records exact across translation |
| Y132 constitutive onset | first Y119/current mismatch: R4 round 13–14, R5 round 16, R6 round 18–19; scaffold and all-native currents diverge same round as Y119 |
| Y132 first-failure mechanism | **48/48** first failures: $J_{\rm in}<2$, $J_{\rm out}=2$, $B{=}D{=}0$ — incoming-supply deficit only |
| Y132 provenance forensics | **75/75** first-missing relations are `VACUUM_FIRE`-produced, directly among the original deletions, at minimum distance exactly $R{+}1$ — not inward-propagating damage |
| Y132 R5/R6 supply asymmetry | R5: O1 **210/210** & O3 **210/210** pre-existing vacuum; R6: O1 **270/270** pre-existing, O3 carrier-produced (18 warm-start + 252 scored) |
| Y132 finite-annulus recovery | 32/32 branches recover exact Y119/current; **0** deleted relation tuples ever regenerated — recovery via reaching intact vacuum, not repair |
| Y132 verdict | **AMBIENT_RENEWAL_SUPPLY_STARVATION_CAUSES_RELAY_LOSS**; **BACKREACTION_IS_WORLDLINE_SUPPLY_ENCOUNTER_NOT_AUTONOMOUS_INWARD_SIGNAL**; **FINITE_DEFECT_RECOVERY_BY_REENTRY_INTO_INTACT_VACUUM** |
| Y133 v1 provenance/challenge | **760/760** CONTROL crossings vacuum-produced; 42/42 cut branches, 2,520/2,520 gate+displacement exact; 14/14 annulus recoveries, 0 relations regenerated |
| Y133 rest provenance/challenge | **1,184/1,184** crossings vacuum-produced but relation-ID sets repeat exactly period-to-period (14/14); $R{\ge}1$: **84/84** branches, **13,440/13,440** rows exact; $R{=}0$ changes current only, kinematics still exact (2,240/2,240) |
| Y133 verdict | **V1_AMBIENT_SUPPLY_STARVATION_SAME_MECHANISM_LOWER_WORLDLINE_RATE**; **STATIONARY_REST_USES_FIXED_RADIUS1_CYCLIC_VACUUM_RESERVOIR**; synthesis **MOVING_SECTORS_RECRUIT_WORLDLINE_VACUUM_REST_RECYCLES_LOCAL_VACUUM_SCAFFOLD** |
| Y134 bond-local template closure | **1,440/1,440** rows → **192** species-independent keys; global reconstruction **672/672** (current), **672/672** (occupancy) |
| Y134 R6 rest→v2 boost mechanism | r1 L-O1; r2 **V-O1**; r3 **+C-O3** ($J_{\rm in}/J_{\rm out}{=}2/1$, $I_6{:}1{\to}2$); rest pool exhausted round 5 for both bond types |
| Y134 R5 transient pulse | $(1,2){\to}(1,3){\to}(1,2)$ over rounds 2–3 via one extra C-O3, present every R5 slot, absent from final mature state |
| Y134 verdict | **BOND_LOCAL_ENVIRONMENTAL_RESERVOIR_CONVERSION_LAW**; **R6_HIGH_LOW_CHANNEL_CONVERSION_EXACT** |
| Y135 preregistered interventions A–E | **72/72** branches alter scaffold; gate **576/576** exact; displacement **576/576** exact; 1,872 constituent updates; 0 failed runs |
| Y135 post-verdict full-reservoir deletion | 484 deletions, 28 branches; scaffold $I{=}J_{\rm in}{=}J_{\rm out}{=}0$ for 8 rounds; kinematics **224/224** exact |
| Y135 verdict | **TRANSITION_SCAFFOLD_NOT_CAUSAL_FOR_EXPLICIT_SELECTOR_KINEMATICS**; **RESERVOIR_CONVERSION_IS_DOWNSTREAM_CONSTITUTIVE_RESPONSE_UNDER_CURRENT_SELECTOR** |
| Y136 Gate A (source-code audit) | `carrier_candidates` has no `mag` param; 132/132 identical gate/e/support; q1/q2 present after common fire **0/132** each |
| Y136 Gates B/C | 84/84 intact + 84/84 scaffold-zero reach requested sector at identical round; 9/14 scaffold-zero rest→v1 lose a bond (12/12 R6, recover ≤32); 896/896 fair-coin episodes settle |
| Y136 verdict | **NO_NATIVE_V1_V2_SELECTOR_IN_CURRENT_CARRIER_PROGRAM** |
| Y137 reachability census (264 roots) | present/emitted after common fire **0/264** each; immediate producers **0/3,552** gates; 32-event native continuation **0/8,448**; multiway depth-8 **0/1,192** |
| Y137 verdict | **CURRENT_Q_SELECTOR_IS_NON_NATIVE_AT_THE_SCRIPTED_TRANSITION_CUT** |
| Y138 native stride memory | $\sigma{=}1$ (rest,v1) **44/44** each; $\sigma{=}2$ (v2) **44/44**; survives q-free common fire **176/176** |
| Y138 gate-input audit / actuation test | every mature gate: 3 native + 1 q at I2 (**88/88**); q-free regeneration **0/176** (primary), **0/176** (contextual-Q control, core loss by event 75) |
| Y138 verdict | **NATIVE_SECTOR_MEMORY_FOUND_BUT_NO_ENDOGENOUS_SELECTOR_ACTUATION** |
| Y139 backward closure (176 motifs, depth 3) | core-preserving: 11,900 path-states, **0/176** closed; unrestricted: 13,852 path-states, **0/176** closed |
| Y139 nearest cycle diagnostic | $T\leftarrow B\leftarrow P\leftarrow T$ in 22/22 v1-replication roots; seeded T enables **both** +1/+2 (22/22) — sector-nonselective; self-destructive both directions (0/22) |
| Y139 verdict | **NO_NATIVE_STRIDE_TO_GATE_TRANSDUCER_THROUGH_THREE_Y33_LAYERS** |
| Y140 NST1F static/blind validation | development **88/88** exact; rest dormant **44/44**; fresh blind set (incl. new species DS001) **92/92** |
| Y140 sustained closure | **60/60** cases, **1,920/1,920** round rows, 5,760 updates — full hypergraph+RNG equality to legacy branch |
| Y140 verdict | **CURRENT_STATE_SECTOR_SELECTIVE_TRANSDUCER_FOUND_IN_AUGMENTED_GRAMMAR**; qualification **SCHEDULER_AUTONOMY_NOT_YET_ESTABLISHED** |
| Y141 Gate B (separate-event race) | local competitor disables NST1F + destroys core: **180/180**; remote commutation: **2,204/2,204** preserved |
| Y141 Gate A/C (atomic ANST1F) | pre-fire prediction = post-fire selection **180/180**; sustained closure **60/60**, 1,920/1,920 rows, 5,760 compound events, exact state equality |
| Y141 Gate D (dormancy) | rest **44/44** dormant; vacuum-only **512/512** bit-identical |
| Y141 verdict | **ANST1F_ATOMIC_RELAY_CLOSES_CURRENT_CARRIER_GRAMMAR_ON_TESTED_MANIFOLD**; qualification **GLOBAL_CARRIER_EVENT_SCHEDULER_AUTONOMY_NOT_ESTABLISHED** |
| Y142 IGR1 canonical equivalence | 180/180 each: roles, direction, sector, gate, relay = Y141 ANST1F |
| Y142 relabel stress (11,520 tests) | IGR1 all measures **11,520/11,520**; old scalar formula **2/11,520** (0.017%); old gate orientation **49.1%**; naive resort **0.68%** |
| Y142 dormancy/sustained closure | rest relabeled: **0/2,816** false-eligible; 32-round persistent relabel: **120/120** runs, 11,520 compound events exact |
| Y142 verdict | **IGR1_INTRINSIC_RELAY_IS_VERTEX_RELABEL_COVARIANT_ON_TESTED_MANIFOLD**; diagnostic **HISTORICAL_NUMERIC_GATE_ORIENTATION_IS_NOT_VERTEX_RELABEL_COVARIANT** |
| Y143 vacuum/moving regression | vacuum 1,800/1,800 exact, 0 extras/missing; moving 5,820/5,820 exact, 0 extras/missing |
| Y143 relabel stress (1,344 tests) | covariant parser **1,344/1,344**; historical parser **192/1,344** |
| Y143 rest-sector exposure | **7/14** canonical states expose **22** new legal branches (all positive-direction primary); all marker-mediated, not duplicate orientations |
| Y143 branch fate (22/22) | old rest core lost; transient moving-shaped state forms but lacks IGR1 direction marker; leaves established carrier class |
| Y143 verdict | **STRUCTURAL_Y33_GATE_ENUMERATOR_IS_VERTEX_RELABEL_COVARIANT**; **REST_H1_IS_NOT_COVARIANTLY_CLOSED**; **DO_NOT_FREEZE_GLOBAL_COVARIANT_ENGINE_OR_REOPEN_E0_MI_YET** |
| Y144 RST1 static/relabel | 22/22 hidden gates removed, 0 new; relabel 896/896 static + 448/448 dynamic exact |
| Y144 regression/blind/handoff | 448 original + 192 blind period checks exact; moving→rest 14/14; rest→v1 settles 2 rounds ($\tfrac12s,\tfrac32s$); rest→v2 settles 1 round ($\tfrac12s$); atomic continuation 2,816/2,816 |
| Y144 verdict | **RST1_CLOSES_MARKER_MEDIATED_REST_BRANCH_ON_TESTED_MANIFOLD**; interpretive **MARKER_ENCODING_ARTIFACT_NOT_BARE-CORE_DECAY**; blocker **REST_PHASE_SCHEDULER_AUTONOMY_NOT_YET_ESTABLISHED** |
| Y145 phase-clock classifier (leave-species-out) | trained on 4 species (220 rows), held out 3 species (220 rows): **220/220** exact both; reduced 3-stat version: 176/220 each (2 bridges collide) |
| Y145 end-of-period closure | 44/44 period-start/e7 pairs match on all 11 tracked indicators |
| Y145 scheduler audit | **44/44** constituents have a genuinely legal destructive competitor at the first rest boundary; RST1 still live in all 44 |
| Y145 provenance/bridge gaps | static R5-scar recovery heuristic: **0/8** — rules out that heuristic, not provenance in general; `prev_e6/prev_e7` and bridge arithmetic still procedural |
| Y145 verdict | **INSTANTANEOUS_STRUCTURAL_REST_PHASE_CLOCK_DISCOVERED**; **REST_EVENT_SELECTION_NOT_SCHEDULER_CONFLUENT**; **PROVENANCE_POINTER_CLEANUP_UNRESOLVED**; DS001/full unseen-context validation not yet established |
| Y146 atomic guard | 44/44 rivals differ in exactly 1 of 5 gate slots; atomic fold removes rival by construction; 44/44 start/e7 signatures close |
| Y146 verdict | **ATOMIC_REST_SUCCESSOR_GUARD_FOUND**; **NUMERIC_Q_REPLACEABLE_BY_ANCESTRY_SUCCESSOR**; blocker narrowed to **CLEANUP_PROVENANCE_NOT_YET_INTRINSIC** |
| Y147 PRV2 decoder stress | 10,000/10,000 exact reconstruction under arbitrary relabeling, overlapping payloads, 1–7 simultaneous tokens |
| Y147 Y33-inertness | proven by case-check against every gate role (not sampled): $h$ source-only $\Rightarrow$ $h$, and thus no PRV relation, can occur in any legal gate |
| Y147 symbolic population run | 10 identities × 2 contexts × 128 periods = 2,560/2,560 exact return, zero token accumulation, N=5 peak 90 tokens |
| Y147 verdict | **EXACT_RELATIONAL_CLEANUP_POINTER_FOUND**; **PRV2_Y33_INERT_BY_GATE_STENCIL_THEOREM**; qualification **FULL_INTEGRATED_RUNTIME_QUALIFICATION_PENDING** — engine not yet frozen |
| Y148 ancestry successor (full period) | exactly 1 ancestry-spine successor per event; matches archived continuation **352/352** |
| Y148 integration correction | Y147's provisional token set narrowed (e7/O4, e7/O6 unneeded) to exactly 2 tokens/constituent at mature-start |
| Y148 phase detector | leave-species-out 242/242 + 242/242; unseen-context 154/154; drives 640 periods, 6,400 phase-triggered steps, 0 exceptions |
| Y148 integrated validation | boundary projection 154/154; token integrity 154/154, 0 orphans; relabel 560/560; long-run 448/448 + 192/192 = 640/640 periods |
| Y148 handoffs | rest→motion 28/28 (1 scoped fixture correction, caught by Y96 recorder's own unscoped-op check); motion→rest 14/14 + 112 further periods |
| Y148 verdict | **AUTONOMOUS_COVARIANT_REST_ENGINE_FROZEN_ON_TESTED_MANIFOLD** — closes the Y136–Y148 architectural arc; $E_0/M_i/\alpha$ cleared to reopen in Y149 |
| Y149 rebaseline | $M_i$ exact to floating precision, $\Delta M_i\equiv0$; $E_{0,A}=6N\ln2$ exact, PRV2-invariant; $\alpha_A=5/48$ (circular, not promoted) |
| Y149 Candidate B shifts | RST1: $B_{\rm proj}=B_{Y88}+N$ exact; full PRV2-retained: $+8N$ more; **all $\Delta B$ unchanged** from Y88 in both cases |
| Y149 same-$N$ contradiction | D2R5/D2R6, T3R65/T3R66, T4R656/T4R665/T4R666: $M_i$ equal, $\Delta B=2$ in every pair — structural, not fitting |
| Y149 verdict | **CANDIDATE_B_GLOBAL_ALPHA_FAILS_STRUCTURALLY**; **INDEPENDENT_MODEL_INTERNAL_MASS_ENERGY_EQUIVALENCE_NOT_ESTABLISHED** |
| Y150 primary (all-halo impulse) | fails sign symmetry (D2R6 $v_1$: $-3.75$ vs $-5.75$; T3R65: span 13.25) — kill condition honored, no promotion |
| Y150 odd diagnostic | $T_+(v_1)-T_-(v_1)=2n_{R6}$, 8/8; cross channel sign-difference exactly 0 |
| Y150 cross diagnostic (sealed) | $J_{\rm cross}(v_1)=-8n_{R5}$, $J_{\rm cross}(v_2)=-8n_{R5}-\tfrac{33}{4}n_{R6}$, exact 8/8; reverse $v_2$ anomaly: T4R656 low by 2 vs. T4R665 |
| Y151 blind N=5 forward validation | total + per-bond law: **88/88** exact; union=sum-of-pairs: 88/88; relabel 240/240; odd law 22/22, cross-channel sign-diff 22/22 |
| Y151 reverse re-diagnosis | preregistered "T4R656-specific" fix **fails to generalize**; correct mechanism: pair-channel overlap/reassignment (general, not one species) |
| Y151 topology-contrast result | $B_{\rm proj}=3N^2+44N+1-2n_{R5}$ exact 19/19 (N=1–5); $\Delta M_{\rm cross}=\tfrac{171}{16}\Delta B_{\rm proj}=-\tfrac{171}{16}\Delta\mathcal{F}_{\rm flux}$ exact every row; total-value fit weak ($R^2\approx0.48$–0.49) |
| Y151 verdict | **FIXED_N_TOPOLOGY_CONTRAST_PROPORTIONALITY_FOUND_FOR_CANDIDATE_B**; **TOTAL_MODEL_INTERNAL_MASS_ENERGY_EQUIVALENCE_NOT_ESTABLISHED** |
| Y152 action constants | R5: $A_1{=}8,A_2{=}20,M_{\rm loop}{=}18$; R6: $A_1{=}4,A_2{=}125/4,M_{\rm loop}{=}131/24$ — both positive, exact; T3 transfer 8/8 |
| Y152 closure gate | $v_1{\to}$rest: D2R5/T3R65 **4/4** sustain orbit, D2R6/T3R66 **0/4**; $v_2{\to}$rest: **0** species reach qualified handoff |
| Y152 verdict | positive action **YES**; autonomous closed loop **NO** — promotion blocked; N=5 holdout and all comparators left sealed |
| Y153 CQ1 readiness gate | matches historical Y105 signature 28/28; relabel-covariant 448/448; $v_1\to$rest closes **28/28** with $L_{v1}=6N$ (R5-present) / $6N{+}1$ (all-R6) |
| Y153 v2 routing | direct settled $v_2\to$rest: **0/28**; $v_2\to v_1\to$rest: **28/28**; post-transition $L_{v1|v2}=6N{-}4$/$6N{-}3$ |
| Y153 landing orbit | 27/28 non-isomorphic to canonical Y148 dressing (28th confirmed noncanonical by halo cardinality 185 vs 225); all recurrent 8/8 periods — second autonomous rest dressing, not two physical states |
| Y154 corrected constants | R5: $A_1{=}8,A_2^{\rm adm}{=}9,M_{\rm adm}{=}119/6$; R6: $A_1{=}4,A_2^{\rm adm}{=}57/4,M_{\rm adm}{=}199/24$ — both positive, exact |
| Y154 validation chain | T3/T4 (5 species): **20/20** all gates; blind N5 (11 species): **44/44** all gates incl. 6-way 2-R5 placement control |
| Y154 verdict | **AUTONOMOUS_ADMISSIBLE_PATH_BOND_LOCAL_POSITIVE_ACTION_VALIDATED_ON_BLIND_N5_MANIFOLD** |
| Y155 scale calibration | single point (D2R5 vs D2R6) fixes $\kappa=277/48$; transfers with **zero refitting** |
| Y155 held-out transfer | 14/14 (both contrast laws) on T3R65+2 tetramers+11×N5; **38/38** on every same-$N$ pairwise comparison in the full population; $\Delta M_i^{Y81}$ fails 38/38 |
| Y155 sign correction | explicitly reverses Y151's incomplete-loop sign: corrected action aligns with $\mathcal{F}_{\rm flux}$, anti-aligns with $B$ — stated openly, not silently superseded |
| Y155 total-value gate | fails cleanly, 0/7 dev + 0/11 N5 for both comparators (residuals to 86.72%); DS001 has zero $M_{\rm adm}$ but nonzero $\mathcal{F}$/$B$/$M_i$ — structural, not a fit failure |
| Y155 verdict | **EXACT_R5_SUBSTITUTION_CORRESPONDENCE_WITH_CAUSAL_REST_CONTENT**; **TOTAL_MASS_ENERGY_EQUIVALENCE_NOT_ESTABLISHED** |
| Y156 DS001 one-body (frozen first) | $A_1{=}2359/4,A_2{=}555,M_1{=}8881/6$; relabel 256/256 |
| Y156 composite transfer | $N\times M_1$: **0/28**; per-constituent match: **0/88**; all Y154 bond coefficients/closures still exact in same 28 cases |
| Y156 migration identity | $\sum_c|C_c(t)\triangle C_c(t{+}1)|=|H\triangle H'|+2m_t$ confirmed exactly: D2R5 376 migrations/752 excess, D2R6 331/662 |
| Y156 verdict | **CURRENT_CORE_INCIDENCE_ONE_BODY_DECOMPOSITION_FAILS** — Y154 not retracted, only the current-incidence self+bond split |
| Y157 immutable-ownership DS001 | $A_1{=}271.5$ both signs; $A_2$: 248(+) vs 249(−) — weakly sign-odd, traced to 1 asymmetric vacuum relay entry |
| Y157 verdict | **FIRST_CONTACT_IMMUTABLE_OWNERSHIP_FAILS_DS001_SIGN_EVEN_GATE**; post-verdict producer-only diagnostic restores exact symmetry ($M{=}60$, 4/4), not yet promoted |
| Y158 DS001 producer split (frozen first) | SELF $M{=}60$; ENV $M{=}5$ (marker handoff only); 888/888 reconstruction checks exact, 0 owner mutations |
| Y158 dimer bond action | strict producer-owned BOND: **exactly 0**, R5 and R6, **8/8** — only historical seed instance persists, no scored turnover |
| Y158 D2 forensic (12 traces) | every adjacent-core relation at mature rest is `VACUUM_FIRE`-sourced (R5: 4, R6: 1); true cross-instance births/deaths at sampled boundaries: **0/12** |
| Y158 verdict | **PRODUCER_SPLIT_DS001_PASS; DIMER_IMMUTABLE_BOND_DECOMPOSITION_FAIL**; reinterprets Y154/155 as environmental relay dressing, not bond-produced action |
| Y159 D2 incidence identity | persistent-in = persistent-out = 1,144; births/deaths at scored boundaries = 0; **616/616** boundary rows exact |
| Y159 PAIR_ENV_RELAY causal test | R5: 3 ENV relays/bond; R6: 1; deletion changes intrinsic selection **0/56**; 4-round repeated clamp exact **224/224** |
| Y159 SECTOR_ENV causal test | exactly 1 ENV relation per constituent targets sector-classifying pair; deletion reclassifies $v_1\to v_2$ in **88/88**; next displacement still old value in 88/88 (1-round lag) |
| Y159 verdict | **PAIR_ENV_RELAY_DOWNSTREAM_CONSTITUTIVE_DRESSING_NOT_CAUSAL**; **DISTINCT_ENV_SECTOR_RELATION_IS_UPSTREAM_OF_INTRINSIC_SECTOR_CLASSIFIER** |
| Y160 population | 28 cases (7 species × 2 geom × 2 sign); **1,344** scored macro-rounds; **4,224** constituent events; CONTROL 448/448 exact $v_1$ |
| Y160 CLAMP (sustained) | staircase $1\to3/2\to2$ **28/28**; only $2N$ deletions/case (176 total); $v_2$ persists rounds 3–16, **392/392**, zero further deletions |
| Y160 dressing-lag confirmation | $L_{CQ}=3N+3$ (all-R6); $3N{+}2$ (one-R5, negative sign only) — speed changes before dressing settles, all species |
| Y160 PULSE | sustained $v_2$: **0/28**; instead settles to exact $|v|=3/2$ rounds 2–16, **420/420**, classifier cycling $2,1,2,1,\ldots$ — reported as candidate orbit, not promoted as a third velocity sector |
| Y160 verdict | **FINITE_ENV_SECTOR_SUPPRESSION_CAUSES_AUTONOMOUS_V1_TO_V2_ACCELERATION**; **SECTOR_STATE_CHANGE_PRECEDES_KINEMATIC_RESPONSE_BY_TWO_MACRO_ROUNDS**; **V2_STATE_SELF_MAINTAINS** — first result where pure environmental deletion, with zero external magnitude, changes autonomous carrier speed |
| Y161 long-horizon $3/2$ orbit | D2R5/D2R6/T3R65/T3R66, 128 rounds: **16/16** cases pass; scored rounds 17–128: **1,792/1,792** exact $|v|=3/2$ + CQ1 same-parity closure |
| Y161 delete/allow atlas (20 words, 1 anchor) | exactly 2 classes: period-2 $3/2$ (6 words), period-1 $v_2$ (14 words); no third class |
| Y161 reverse control ($v_2\to v_1$) | positive-sign: **4/4 PASS** ($2\to3/2\to1$, native $v_1$ sustained); negative-sign: **4/4 FAIL** (`SECTOR_AMBIG`, second outside source) |
| Y161 geometric diagnosis | mature $v_1$ source: $+$ direction $=e$ (8/8); $-$ direction $=$ spine-step($e$,$-$direction,3) (8/8) — not rescued in-stage |
| Y161 verdict | **V3_OVER_2_PERIOD2_CARRIER_DRESSING_ORBIT_VALIDATED**; **FUTURE_BLIND_V2_TO_V1_CONTROL_FAILS_SIGN_COVARIANCE** — 3rd autonomous speed structure confirmed |
| Y162 frozen candidate (from Y161 geometry) | $+$: source$=e$; $-$: source$=$Succ$_{-{\rm dir}}^3(e)$; insert only if zero outside sources exist |
| Y162 D2 test (8 fresh cases) | positive: **4/4 PASS**, $56/56$ post-transition rounds exact $v_1$; negative: **4/4 FAIL** — source collides with current role $c_1$ (endpoint duplication), rejected before insertion |
| Y162 verdict | **Y162_SIGN_CONJUGATE_ENDPOINT_SOURCE_NOT_TRANSITION_SAFE** — mature-state formula not transferable to the still-settling transient; Y160/Y161 results unaffected |
| Y163 ancestry selector | nearest strict event-ancestor unique in **22/152** observations — not promoted |
| Y163 33-selector role census | 5,016 evaluations; 3 globally eligible selectors; only `source=e` preserves all 136 positive assignments |
| Y163 occupancy-matched D2 gate | E / B0 / C1 each **8/8** both signs; no-addition 0/8 (stays $v_2$); E CQ1 **8/8** |
| Y163 passive 64-round T3/T4 | **40/40**; old 16-round gate still 0/40 (remains failed) |
| Y163 N5 blind reverse holdout | **44/44**; settling prediction 44/44 |
| Y163 repeated round-trip | D2 8/8 (32 legs); T3/T4 20/20 (80 legs); N5 **44/44** (176 legs, 44 controls, 22,528 graph comparisons) |
| Y163 integrity notes | count-variable bug and 1,800/1,860 config mismatch caught by verifier; 900-s timeouts left unresolved; 1,500-s completion run separately frozen |
| Y163 verdict | **CLOSED/PASS** — repeated externally scheduled two-speed control; not three-speed, not native acceleration, not $E_0/M_i$ |
| Y164 D8E trimer recurrence | T3R55/T3R56 × P/R × 4 independent vacua: **16/16**, 256/256 untouched rounds each, 4,096 replayed observations |
| Y164 D8E structural classes | P≅R within family in all vacua; T3R55 ≇ T3R56; each matches D8C class |
| Y165 D3-4A rival-gate audit | fresh-source four-core rival selected in **9/9** health failures; 0 safe events (development data) |
| Y165 D3-4 scheduler holdout | 48/48 arms complete; 1,536 events replayed (496 carrier, 240 redirects, 1,040 vacuum) |
| Y165 D3-5 d20 response | receiver = trailing carrier; 4/4 vacua in each of 4 placement/direction contexts; matched solos **0/32** |
| Y165 D3-5 causal diagnostic | 31 responding cases, 59 transitions; removing partner-derived relation restores $v_2$ in **59/59** |
| Y165 D3-5 range | $d{=}12$ none; $d{=}16$ mixed (warm-up response in $+$); $d{=}20$–$28$ 3/4–4/4; strongly vacuum-dependent |
| Y165 D3-5 accounting | 148 arms: 144 complete, 3 support-overlap safety stops, 1 insufficient carrier events; V3 chunked audit 16/16 |
| Y165 verdict | partner-dependent directional wake-like response **established**; no attraction, range law, exchange, $E_0/M_i$ |
| Y165 D3-6 preparation-order matrix | SIM 23/24; PF **24/24**; RF 0/24 (19 overlap stops); single-carrier controls **0/96**; VAC 0/24 |
| Y165 D3-6 provenance | 41 PF transitions: pre-receiver leader ancestry in all; removal restores $v_2$ **41/41**; none needs scored-phase relation |
| Y165 D3-6 wake distance | responsible relation 5/6/7/8/9 graph steps from leader core in 12/19/3/6/1 events |
| Y165 D3-6 audit | 192 arms, 5,764 events replayed, 0 mismatches; 192/192 final digests |
| Y165 D3-6 verdict | persistent deposited-history (wake) channel; lifetime, range, polarity, exchange, $E_0/M_i$ not established |
| Y165 D3-7A persistence | pairs **143/143**; controls 0/176; HEAD ancestry 143/143; $Q$-block ancestry **0/143**; wake 23–27 steps from source at oldest |
| Y165 D3-7B causal front | $t_0$ arrival **0/32**; all 413 scored leader events 0 arrivals; lineage survives 32/32 (depth ≤20); old wake 24/32 |
| Y165 D3-7C head-on | overlap **32/32** at $|\Delta X_T|=2$; pre-contact wake entry/sector change **0/32**; carrier events to contact 6/10/14/18 |
| Y165 D3-7D regional asymmetry | co-moving 8/8, head-on 0/8; signed inner−outer not invariant ($-2$ to $+2$); Casimir-like hypothesis fails |
| Y165 D3-7E v1 receiver | v2 benchmark 16/16; v1 wake entry 10/16, immediate change 0/10, sole source 4/10, later toggling 4/16 |
| Y165 D3-7F DS001 $\tfrac32$ | qualified 8/8, 512/512; pair: $-$ direct wake 16/16, $+$ collapse to $v_2$ 16/16 without wake relation; solos 32/32 stable |
| Y165 D3-7G mechanism | $+$: partner-produced input enables vacuum fire consuming receiver's future source (4/4); $-$: direct occupancy (4/4) |
| Y165 D3-7 origin caveat | interaction-capable history traces to leader's earliest preparation in every tested case |
| Y165 D3-7H ledger | $A=T=A_{\rm sector}$ **8/8**; four simple conservation candidates **0/4** each |
| Y165 D3-7I cycle | capture to stable sector 8/8; closed cycles **0/8** |
| Y165 D3-7J origin gate | fossil deleted: anomaly **8/8**; aged recent path: **0/8** (339/339 identical); star deletion reorganizes 8/8 |
| Y165 D3-7K origin zone | abandoned zone reproduces **8/8**; leader ancestry before onset **0/8**; pair=solo through R7 8/8; first difference R8 |
| Y165 D3-7L R8 excess | pair-only R8 deletion: full trajectory unchanged **7/7** |
| Y165 D3-7M R8 deficit | solo-only R8 deletion: acquires pair response **0/8**; two-sided equalization: anomaly remains 8/8 |
| Y165 D3-7M scheduler audit | RNG equal 1/8; common global legal gates **0/8**; counters differ 8/8 — leading confound |
| Y165 D3-7N RNG crossover | matched-donor onset equal to native **24/24** (receiver-event index); solos never anomalous; full histories RNG-invariant 0/8 |
| Y165 D3-7N common-gate replay | exact common gates at both cuts **0/8** — not constructible |
| Y165 D3-7N retrospective geometry | onset inside leader's original formation interval: $+$ 4/4, $-$ 3/4 (4th adjacent) — exposed data, non-gating |
| Y165 D3-7O static map | 8/8 mechanism-qualified predictions; seed-specific negative $k=3$/$5$ split predicted |
| Y165 D3-7O P000 clamp | $k,x,A,A_{\rm sector}$ equal prediction **8/8**; 0 scheduler/vacuum/leader events before onset |
| Y165 D3-7O native reference | exact $k$ and $x$ **8/8** (tolerance allowed ±1 event) |
| Y165 D3-7O EARLY clamp | null 8/8, but receiver ends ~15 units short of encounter region — uninformative; longer rerun recommended |
| Y165 D3-7P map qualification | **19/24** (positive 12/12; negative 7/12: $d$=40 3/4, 44 4/4, 48 0/4) |
| Y165 D3-7P qualified predictions | clamp exact **19/19**; native exact $k,x$ **19/19** |
| Y165 D3-7P positive sequence | $d$=40/44/48 → $k$=5/6/9, $x$=1294.0/1295.5/1300.0, $T$=+1/−1/+1 (4/4 vacua) — encounter inside/at edge of formation support each time |
| Y165 D3-7P law gate | monotonic triplets 4/8 — **NOT_CLOSED**; post-verdict raw map descriptively exact 24/24 (non-gating) |
| Y165 D3-7Q occupancy law | 72/72 qualified; native exact **72/72**; clamp 72/72; source-slot normalization removes response 24/24 + 24/24 |
| Y165 D3-7Q phase periodicity | mechanism and $\delta_{\rm form}$ periodic in $d$ with period 3 (both signs, 4/4 vacua) |
| Y165 D3-7Q EARLY | EARLY map/clamp exact 72/72; $k_{\rm EARLY}=k_{\rm P000}+17$ in all; origin LEADER_FORMATION_DESCENDANT 72/72 |
| Y165 D3-7R matched leader | P vs O mature leader identical **24/24** |
| Y165 D3-7R invariance | own-map prediction 24/24 each; inherited law P 19/24, O 19/24, both 17/24; P/O differ 4/24 (close negative only) |
| Y165 D3-7R root surgery | roots 21/24; viable surgeries alter response **15/15**; strict control available 1/24 — gate not closed |
| Y165 D3-7R classification | **PREPARATION_PROCEDURE_DEPENDENT_FORMATION_MEMORY** — D37 retired from mass-energy path |
| Y165 C3 rival-gate coupler | eligible phases 6/8; viable **0/8**; rival/native overlap 4/5 and native gate lost 6/6; untouched control 2 full cycles |
| Y165 C3 verdict | **NO_HEALTHY_RIVAL_GATE_COUPLER** — $E_0$, independent $M_i$ undefined; $\alpha$ not testable |
