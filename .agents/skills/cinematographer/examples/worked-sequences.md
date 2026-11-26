# Worked shot-design exercises

Original, same-author planning walkthroughs written 2026-11-25. These are concrete
text outputs, not independent forward tests or claims that footage was generated.
All stories/assets below are synthetic exercise inputs, not The Stories canon.
Use with [scenarios](../tests/scenarios.md), [rubric](../references/review-rubric.md)
and [current evaluation](../tests/evaluation.md).

## T01 — Silent 30-second visual narrative

**Input:** one paper-styled animated character N enters a workroom, finds a toy
bird on its side, places it on the table, winds its key, releases it and watches
it move. No speech, text, music or sound carries indispensable information.
Locked: N's crescent is on N's own left cheek, scarf knot on own right; bird has
one chipped left wing and never acquires a new wing. Warm desk lamp remains on.
This exercise authorizes those events; Cinematographer is realizing them.

**Strategy:** first establish stillness/relationship, then make contact, winding
and release legible; return wide enough to see consequence and response together.
Alternative continuous master saves cuts but makes the tiny key hard to read.
Selected coverage uses one closer view for the crucial mechanism. All durations
are proposed screen allocations, excluding optional protection and handles.

**Map:** table at (0,0), door at (-2,1), floor bird at (-.6,-.5); north is +y,
meters. Cameras south, looking north; table lamp at (-.8,.4). Keep the door as a
landmark in wider views. Character N approaches from screen-left and stays
left-of-bird. Output 1920×1080, 24 fps; paper look and proposed virtual gate
24×13.5 mm. These are specifications, not measured capture metadata.

| Shot / script beat | Screen time | Frame/action and audience change | Camera/light; cut and state |
| --- | --- | --- | --- |
| S010-SH010 / SB01 | 0–5 s | Wide, door→table relation; N enters, notices bird still on floor. Audience learns location and problem. | Locked south master, moderately deep focus; warm left lamp/bounce reveals silhouette. End: N beside table, hands empty, bird still down. |
| S010-SH020 / SB02 | 5–9 s | Low medium detail retains table leg; left hand lifts bird onto table, keeping chipped wing visible. | Static from same side, match approach; no camera move. End: left hand supports upright bird on table. |
| S010-SH030 / SB03 | 9–14 s | Medium close view includes face, bird/key; N's right hand approaches existing key. Audience understands intended repair. | Static eye-near height, focus includes key and relevant gesture; do not invent internal gears. End: right hand at key, left supports bird. |
| S010-SH040 / SB04 | 14–20 s | Close detail, key and both hands; one readable winding cycle. | Fixed station, f/4-equivalent DOF intention, adequate motivated bounce on key. Cut after winding settles, left hand still supports. |
| S010-SH050 / SB05 | 20–24 s | Detail widens enough for release; hands clear, bird remains upright and briefly still. | Static; hold the interval between release and consequence. End: hands withdrawn, bird stands at initial table mark. |
| S010-SH060 / SB06 | 24–30 s | Medium two-subject frame (N + toy), bird advances about 10 cm, N smiles. Audience sees action worked. | Static, both on readable planes. World-left source unchanged; finish with stable pose, no compulsory fade. |

The [complete JSON packet](silent-30s.json) records stable IDs, states, panel specs
and receiver needs. It is spec-only with missing real reference assets explicitly
marked. At 24 fps, the planned total is 720 frames. This is arithmetic, not a
measured animatic. Critical read: mechanism/key before winding; no “fixed bird”
result before release. Add 0.5 s handles before/after captured actions when useful,
without counting them in the 30 s proposal. Optional full master protects action
continuity but is not an additional mandatory shot.

**Board/previs request to Artist:** render SH040 start/key/end panels with left
hand on body and right hand at key; chipped left wing stays in silhouette. Camera
arrows absent (static); subject arrow marks only key rotation. Keep style from
LOOK-PAPER v1, not a newly invented photorealistic finish. **Editor question:** can
key recognition and release read within proposed 5/6/4 s slots? **Sound note:**
optional winding/click cues may enhance it, but the silent visual test must work
without them. No packet was actually sent to another agent.

**Bad plan / repair:** orbit during winding + extreme shallow focus hides hand
contact and demands unseen design. Hold camera, stop down/restage focal planes;
retest release and own-left/own-right marks in adjacent panels. Text review
cannot certify that the tiny key will read in rendered output.

## T02 — Two-person dialogue and a prop

**Input:** A and B remain seated across a table; A slides a closed envelope to B.
Dialogue is supplied and unchanged; the seal is not to be inspected yet. Target
20 s, clean continuity, no moving camera. Map: A (-1,0), B (1,0), cameras y<0.
Envelope starts before A; window north-west, no practical switch.

| ID | Proposal / time | Continuity and editorial job |
| --- | --- | --- |
| S020-SH010 | South two shot, 4 s | A-left/B-right, envelope before A; establish positions and available surface. |
| S020-SH020 | A MCU near B-south, 5 s | A looks screen-right toward B; begin from resting hands, retain slide start. |
| S020-SH030 | B OTS near A-south, 5 s | B looks screen-left; show envelope arrival and hand stopping it, closed flap down. |
| S020-SH040 | Shared two shot, 6 s | Match B's stopping contact into hold, cover listener response; don't reveal seal. |

Window stays world north-west; its screen position can differ in reverse views.
Give Editor a matching slide from both angles plus 0.5 s handles. If time permits,
optional silent B reaction protects a cut away from a mismatched hand. It cannot
repair an impossible envelope position. Bad: A and B singles both look right;
return B camera to south near A. Bad: mirror B frame; that flips costume marks.
Acceptance requires adjacent boards and played dialogue; text only checks the
specified side/target, 20 s arithmetic and absence of a planned early reveal.

## T03 — Suspense without an early reveal

**Input:** script S030: courier sits; only then notices the broken seal. Audience
must see the broken edge just before the courier does, but culprit identity stays
unknown. No new threat, silhouette or sound is authorized. Target 18 s.

Propose SH010 (5 s) door/table wide, edge turned away; SH020 (4 s) seated hand
sets envelope down and rotates its already broken edge toward viewer; SH030
(4 s) insert shows that break; SH040 (5 s) courier's reaction/look to envelope.
Audience now knows a little before character, within the script's allowed order.
Key distinction: the insert is evidence, reaction confirms receipt, offscreen
identity remains unknown. Keep edge orientation and hand match across SH020→030.
No arbitrary low angle/color is needed. Cost: controlled envelope orientation.
Test every prior frame/reflection for premature disclosure. Alternative: hold
hand/face in one view and pull focus only after the sit; costs readable depth
planning and may over-emphasize the clue. If script instead forbids audience
knowledge before the look, shift the disclosure trigger; do not silently retain
this version. “Suspense” is an intended effect, not an audience-test result.

## T04 — Fast action versus calm emotion

**Input A:** 12 s to retrieve a rolling ball before it reaches a door. Locked
events: N approaches, blocks ball with foot, lifts it; no dangerous stunt.
Plan: route master 3 s (door screen-right), lateral approach 3 s (left→right),
contact detail 2 s (foot stops the same ball), wider consequence 4 s (N lifts).
Static/short truck as needed; if blur hides contact, test shorter shutter with
exposure compensation rather than adding more cuts. Keep approach/contact/stop
phases and foot side consistent. Fast does not mean every shot must be handheld.

**Input B:** 12 s as N considers the same ball after a friend leaves; no new action
is added. A stable medium 8 s includes empty chair and hands; a wider 4 s retains
door/absence. No automatic push-in or blue wash. Test whether attention actually
changes during the hold; if inert, work with Director on observable performance
or trim with Editor. Do not invent a tear or rewrite the departure. Both plans
use the same runtime but different information density/performance room.

## T05 — Vertical readability revision

**Input:** convert T02 to 1080×1920. A centered crop removes B and envelope contact.
Propose depth-staggered vertical master, A lower-left foreground and B upper-right
middle distance; maintain south-side relation. Thinner OTS shoulder in SH030,
envelope contact near center; include a matching insert if both faces become too
small. Recheck that neither body hides the envelope. Compare against clean singles
with a short vertical establishing view if staging is locked.

Use provisional action-safe x=.10–.85, y=.10–.78 and caption band y=.80–.92 only
as a declared test setup; actual host overlay is missing. Inspect at 270×480 with
the real UI overlay when supplied. Required checks: both participants identifiable,
slide direction/recipient clear, seal withheld, no essential hand/eyes covered.
No rendered vertical frame was produced; these checks remain pending.

## T06 — Stylized identity and prop continuity

**Input:** N's own-left crescent, own-right scarf knot; chipped left toy wing.
Request reverse view after T01. Keep asset IDs/versions; do not mirror SH030.
Ask Artist for approved back/three-quarter geometry or label unseen construction
provisional. Use table/door/source landmarks to match scale and orientation;
list exactly which marks should be visible from each view. A mark legitimately
occluded is not missing; a mark appearing on the opposite cheek is a defect.
Compare a start/mid/end panel strip and table-contact positions, then a real
clip if generated. A seed alone certifies none of this. Preserve the paper look;
avoid adding unapproved metallic sheen or blur to “improve” consistency.

## T07 — Zoom, dolly, focus pull

**Input:** draw attention to the key without changing viewpoint. Choose a static
zoom/crop or cut to detail, stating resolution cost for crop. Do not call it a
dolly. If the goal is to move past a foreground table leg and reveal the key,
choose a lateral translation; a zoom cannot see behind the leg at a fixed station.
If both key and face are already visible but only one should be sharp, specify a
focus pull key→face, camera fixed. The ideal-camera numerical comparison in
[camera optics](../references/camera-optics.md) supplies an arithmetic sanity test;
actual lens distortion/breathing and generated motion remain untested.

## T08 — Low-light rationale

**Input:** token readable beside an existing lamp, textured shadows, no added
visible fixtures, no shoot measurements. Use the concrete setup in
[lighting](../references/lighting.md): motivate broad offscreen bounce from lamp
direction, constrain spill, retain a readable background edge. Propose f/4 with
more source output vs f/2 with narrower depth; choose after the hand-path test.
No fixture wattage/lux or ISO is invented as guaranteed exposure. Reject “globally
underexpose two stops” as a universal low-key recipe. Acceptance: token and eyes
read, lamp clipping controlled as intended, world direction matches reverses;
needs frames/scopes/clip, currently unmeasured.

## T09 — Deliberate axis crossing

**Input:** Director explicitly requests crossing at the existing turning point
in T02, with geography still comprehensible. Replace the return wide with one
continuous visible arc from south to north, keep both subjects/table/door in
view, settle A-right/B-left. Use north-side singles thereafter. Specify arc radius
and clearance in previs, not an unsupported “orbit 180°” control in every model.
Protect a south-side alternative if the move steals the performance. An insert
of the envelope alone is insufficient to establish the new side. No seat swap,
prop jump or new dialogue is authorized. This is a designed exception with a
reorientation test, not a continuity error automatically marked pass.

## T10 — AI failure and bounded revision

**Synthetic returned report, not an observed clip:** “SH040 has a second key at
2.1 s, and the chipped wing becomes intact after the hand passes.” Do not claim
to have watched it. Request actual clip/frame interval for inspection; meanwhile
propose v2 with static camera, unobstructed side view, one winding action, approved
PROP-BIRD v1 identity/start reference and compatible end state. Preserve left
support/right winding; do not redesign bird to match the defect. If tool lacks
end-frame conditioning, say so and use it only as a check target. If two corrective
attempts still fail, use a shorter winding unit or Artist-produced key poses and
another animation method within the brief/budget. Preserve old outputs and mark
derived SH050/cut stale until hand/contact state matches. No generation executed.

## T11 — Cross-agent handoff with mixed beat types

**Synthetic inputs:** Storyteller outline O v3 has narrative beat `NB07`; script
v5 scene `E02-S030`, script beats `B01` and `B02` cite `NB07`; look bible L v2 locks
scarf. Preserve `E02-S030`; declare `narrative_beat_ids=[NB07]`,
`script_beat_ids=[B01,B02]`. Shot `E02-S030-SH010` maps to `NB07/B01`, SH020 to
`NB07/B02`. Reordering shots does not rename them. If later script v6 splits B02,
require explicit old→new mapping; similar wording alone is not an ID match.

Artist gets SH020 start/key/end panel specs + L v2, actual/missing reference
locators, frame geometry and light sources. Editor gets proposed order, critical
broken-seal read, 18 s estimate and alternate holds; Sound Designer gets look
trigger and offscreen source requirement, not a dictated mix. Director gets the
performance/coverage trade-off. Ask Artist whether the approved seal geometry
reads from the specified view; absent response remains pending. Conflict: a draft
asset shows intact seal while script requires broken. Retain both versions,
flag the exact mismatch, use an authorized broken-state variant if supplied or
request that variant; don't silently rewrite script or approve an asset.

This proves a worked semantic mapping exists. It does not prove actual receiver
acceptance, runtime orchestration or a finished integration with parallel drafts.
