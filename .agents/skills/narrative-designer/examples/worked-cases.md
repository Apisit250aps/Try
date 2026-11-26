# Worked cases

## A 30–60 second social animation: “The Last Lantern”

Provisional canon: at dusk Mali can use one remaining lantern to signal a lost
fisher or illuminate a dark pier where her sister is searching. Both matter to her.
No prior approved story, platform integration or audience test is implied.

Clip C0 (estimated 35–45s) establishes both needs and offers two labeled routes:
A signal fisher, B illuminate pier. C1A and C1B (each 30–40s, independently
understandable recap included) show consequences and both converge on C2 (30–40s
with two short alternate inserts). The story spans one evening; a viewer's estimated
path is 95–125 seconds, not 30–60 seconds. Figures are planning estimates, not
measured clips. Four main clips plus two inserts
need actual costing; these are not three unique paths or proof of a player.

| Edge | Precondition → effect | Immediate and delayed payoff |
| --- | --- | --- |
| A | at C0 → `signal=true`, `pier_lit=false` | Fisher sees signal; sister later arrives having stumbled. |
| B | at C0 → `signal=false`, `pier_lit=true` | Sister finds her way; fisher later arrives after a longer search. |

At the C2 join preserve both flags, do not claim both places were lit. Each ending
acknowledges a real cost. C0 routes can be released as separately named clips; route
links and fallback search names require platform verification. A poll could select
which C1 to publish later for everyone; it cannot by itself select a clip per
viewer. Viewer-selected independent links allow navigation, not persisted state.
With only one ending and no interaction objective, a single linear film may better
serve the story and budget.

## Three endings and rule resolution

Second, separate interactive project: a witness chooses how to handle evidence.
State `evidence ∈ {shared, sealed, lost}`, `ally ∈ {present, absent}`. E1 "Public
truth" guard evidence=shared; E2 "Protected confidence" evidence=sealed AND ally
present; E3 "Quiet uncertainty" fallback. E1/E2 are disjoint, E3 handles all other
reachable states. Each changes who bears a cost, with no morality score. E3 must
have credible setup for lost or sealed/absent paths, not become a universal happy
ending. Add `ally=present` as an independent E4 guard and it overlaps E1 and E2;
require explicit priority/tie policy or revise predicates. Removing E3 exposes
uncovered cases. A structurally defined ending is not necessarily reachable: list
an actual action trace before claiming reachability.

## Counterexamples and handoff

A foldback that deletes `signal` and shows “you lit the pier” on both routes is a
continuity error. Keep variants or rewrite the shared event to be true in both.
A hub that permits indefinite browsing is intentional only if its contract says so;
a mandatory-ending route that can loop forever needs an exit/progress rule or an
explicit fairness assumption. Six binary decisions can yield 64 histories; this is
not 64 unique animations. Inventory the actual shared and changed assets and cost.

Screenwriter handoff for C2: packet P1@0.1, node C2@0.1, entry signal xor pier_lit,
shared event reunion, variants above, no invented second lantern, estimate 30–40s,
status proposed; source canon and approvals pending. Director chooses the approved
creative approach; Artist, Cinematographer, Sound and Editor receive the variant
references. Changing the one-lantern fact invalidates guards, C1/C2, asset and timing
estimates and all associated validation. These are prepared handoffs, not receipts.
