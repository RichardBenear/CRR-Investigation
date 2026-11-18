# CRR Investigation — Plain-Language Status Briefing

## Where this all started

The original observation: someone in free fall and someone floating in deep
space both measure zero acceleration on an accelerometer strapped to them.
Someone standing on the ground measures 1g. That's the entire seed of this
whole project — the idea that **gravity and inertia might be two faces of
the same underlying thing**, rather than two separate forces that happen to
use the same word ("mass") by coincidence.

The working theory (call it CRR) says: build a toy universe out of nothing
but a single, simple update rule, applied over and over to a huge, ever-
growing network of relationships — no space, time, or matter assumed in
advance, all of it supposed to emerge from the rule itself. Then look for a
small, self-sustaining pattern in that network that behaves like a
"particle." **Mass**, in this picture, is how much that pattern re-uses its
own material instead of dissolving into fresh material each step.
**Inertia** is how much extra work it costs to redirect that pattern once
it's moving. If a structure like that can be found, the natural next
question is whether its "inertial" behavior and its "gravitational" effect
on the surrounding network come out proportional — which would be the
first from-scratch derivation of the equivalence principle.

That's the target. Nothing in this document below is the target itself —
it's all groundwork toward being *able* to ask that question at all.

---

## The toy universe, in engineering terms

Think of the substrate as an enormous, constantly-growing database of
pairwise links — "node A points to node B" — with exactly one rule:
*wherever you see this specific small pattern of links, replace it with
that pattern.* No global controller, no clock, no coordinates. Just: scan
for the pattern, replace it, repeat, forever, everywhere it matches.

It's the same basic idea as Conway's Game of Life, except instead of pixels
on a fixed grid, the "canvas" itself is an arbitrary, ever-growing network
with no fixed shape at all. Space, distance, and dimension are all things
you'd have to *measure* after the fact by looking at how the network's
size grows with distance — the same way you'd measure the dimension of an
unfamiliar material by checking whether its volume grows like r, r², or r³
as you look further from a point.

Grown from a tiny seed, this rule does produce a large, connected,
sprawling structure with a roughly stable, measurable "dimension" — call
that background structure **the vacuum**. That part has worked reasonably
well throughout this investigation.

## What a "particle" means here

A particle candidate is a small loop in the network: a handful of nodes
whose links cycle through 2 or 3 repeating shapes, over and over, as the
rule keeps firing on them — like a limit cycle in a dynamical system, or a
whirlpool that keeps the same overall shape even though the actual water
passing through it is constantly being replaced.

We found and used one concrete example throughout: a 4-node loop that
alternates between two shapes every step. It behaves cleanly and
predictably — as long as nothing disturbs it.

## The central problem: these loops don't self-heal

Take that clean 4-node loop and let one ordinary outside "bump" — the same
kind of event that's constantly happening throughout the vacuum — touch it
once. About a third of the time, that bump destroys one of the loop's
required connections instead of harmlessly passing through. Once that
happens: **the loop never recovers.** Not "rarely" — in every rigorous
test run across this whole investigation, damage was never repaired by
the network's own ordinary activity.

That's the actual central finding of this entire investigation. It's not
that we haven't found the right particle yet — it's that *the specific
particles we can build fall apart the first time they're touched*, and
understanding exactly *why* turned out to be a long, genuinely
interesting engineering-diagnosis problem in its own right.

## Four "why" answers, in plain terms

**1. There's a hard conservation law working against repair (we called it
the relation-floor theorem).** Think of it as a strict "no free lunch"
budget: every legal move this rule can make either keeps the same amount
of local connective material or spends some of it — it can never manufacture
spare capacity out of nothing. Once damage spends the wrong piece, there's
no way to earn it back through ordinary local activity, the same way you
can't recover a lost bank deposit by making more withdrawals.

**2. Time only runs one direction here (we called it the causal-
directionality no-go).** Every new connection this rule creates points
from older material toward newer material — never the other way. It's
like an append-only log file: you can build on the past, but nothing can
ever reach back and edit it. This turned out to make it structurally
impossible to keep two separate moving parts (say, a "motion" part and an
internal "clock" part) properly synced once they're built as separate
pieces — neither can ever check back in with the other.

**3. Self-repair needs the spare part pre-wired right next door, not just
"somewhere nearby" (we called this frontier adjacency).** Imagine a
self-healing machine where the backup component has to already be bolted
directly onto the exact spot it would need to fill in — not sitting in a
warehouse three rooms away. We found exactly one tiny 3-node shape with
that property built in natively. Every actual "particle" shape we found
(the ones with an internal clock, alternating between states) does *not*
have it. That's basically a design trade-off: the shapes that have an
internal state to track time don't have this pre-wired backup, and the
shape that has the pre-wired backup doesn't have any internal state.

**4. If a damaged node is left with zero remaining connections, it's
permanently gone (Stage S).** This is a clean, provable fact: if damage
severs *every* link a node has, no future move of this type of rule can
ever reconnect it, because every move only ever touches things it's
already directly working with plus one brand-new part — never something
sitting off to the side, disconnected. This is like a robot arm that can
only grab things already in its gripper or freshly manufactured — it can
never reach out and pick up a part that's been dropped on the floor.

## The engineering fixes we tried, and why each one specifically failed

We treated this like a real troubleshooting log — try a targeted fix,
find out exactly why it doesn't work, use that to inform the next attempt.

| Attempt | Idea | Why it failed |
|---|---|---|
| Backward-edge rule | Let the new part also wire back to the old part | The extra wire attached to the part about to be thrown away, not the part that survives — so it didn't actually help, just moved the same problem |
| Survivor-edge rule (V1/V2) | Wire the extra connection to the part that survives instead | **Partial success** — genuinely fixed some repairs, for the first time anywhere in this investigation, but only covered *some* of the loop's states, not all of them, and even a generous best case still fell far short of what's needed for long-term survival |
| Two-species rule | Keep a separate, "hidden" spare-parts inventory that doesn't count against the main budget | The hidden storage worked exactly as designed — but the mechanism to actually *use* the spare parts fired constantly everywhere, flooding the whole vacuum with unwanted side effects, and even just having that option available destabilized the clean loop, even without any damage occurring |
| Shared-ancestry (entanglement) | Link two separate particle copies back to a shared parent event, hoping one could help repair the other | Tested rigorously with proper statistical controls — genuinely no advantage over an isolated particle, despite searching a much larger space of possibilities |
| Adjacency-as-requirement (C1) | Only allow the rule to fire where the backup is already pre-wired | The rule became too restrictive to sustain any recurring loop at all |
| Gated spare-parts inventory (C2) | Fix the "fires everywhere" problem from the two-species attempt by only allowing repair right where it's needed | Coverage got worse, not better |
| Relation-neutral donor rule (C3) | Borrow capacity from an unrelated part of the network so nothing is created from nothing | Failed the very first sanity check |
| Three-way (ternary) relations (C4) | Use a genuinely richer type of connection that can encode motion, internal state, and repair capacity all in one object, instead of separate wires for each | **The real breakthrough on this specific sub-problem** — a large, honestly-tested population of loops (tens of thousands) all had full backup coverage for the first time in the whole investigation |

The ternary idea (C4) then needed its own follow-up fixes because the
background "vacuum" built from it turned out to be one-dimensional (like
a single wire instead of open space) and, separately, the loop shape
never spontaneously appeared in the vacuum's own natural growth — it had
to be hand-built and placed there. Both are real, still-unresolved
problems.

## The most recent, most encouraging result: a working diagnostic checklist

Going back through every failed and successful repair attempt across the
whole investigation — 604 individual test cases spanning four different
designs — one four-item checklist turned out to predict the outcome with
**perfect accuracy**:

1. Is the damage actually hitting the part of the loop that matters, not
   some irrelevant spot?
2. Does the loop's own shape already have a "backup wire" pre-installed
   in the right place?
3. Did the surviving connection end up on the *correct side* of that
   backup wire (not just present, but oriented the right way)?
4. After the dust settles, can the loop's very next required move still
   actually happen, or did the damage quietly break something else
   needed for that next step?

If all four are "yes," repair happens, every single time tested. If any
one is "no," repair never happens, every single time tested. That's a
genuinely clean, useful diagnostic — but it's honestly still just a
description of the 604 cases it was built from, not yet a proven law, and
it's only ever been tested on the "two-wire" style of connection, never
on the newer three-way connections. The obvious next test — predict the
outcome for a new, different kind of case *before* checking the answer —
is in progress.

---

## So: where does this actually leave us, relative to gravity and inertia?

Here's the honest gap, stated plainly, since that's the point of this
document.

**What's been established:** a rigorous, detailed, and increasingly
precise picture of *why* small self-repeating structures in this
particular toy universe are fragile, and *exactly* what conditions a
structure would need to satisfy to survive being disturbed. That's real,
hard-won engineering knowledge about this system's failure modes.

**What has not yet been touched at all:** mass, inertia, gravity, or
anything resembling the equivalence principle. Every stage so far has
been asking a strictly *prior* question — can a candidate structure
survive long enough to have stable properties in the first place? You
can't meaningfully measure the "mass" or "inertia" of something that
falls apart the instant it's perturbed. All of this work has been
necessary groundwork, not the actual measurement.

**What would actually put us back on the direct path to the original
question:** a structure that (a) survives disturbance reliably — passes
the PRO checklist above, essentially always, not just sometimes — and
(b) is actually moving, so "resistance to redirection" is even a
meaningful thing to measure on it. Only once both of those are true does
it become possible to ask the questions this whole project actually
exists to answer: does inertia scale with size the way we'd expect from
"self-reuse," and does that same structure warp the surrounding vacuum's
geometry in a way that's proportional to it.

**For a future white paper**, the honest framing is: this is a rigorous
negative-and-diagnostic result about one specific candidate rule, with a
precise, well-tested characterization of exactly what property a
self-sustaining structure needs and doesn't yet have — not (yet) a
positive result about gravity or inertia. That's a legitimate and
publishable kind of result on its own, and it also tells you exactly what
a *successful* rule would need to look like, which is valuable either as
a target for continuing this search or as a clearly-stated open problem.
