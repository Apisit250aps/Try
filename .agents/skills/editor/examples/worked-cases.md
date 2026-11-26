# Worked editorial choices and counterexamples

These are authored paper edits, not viewed footage, measured reactions or actual
Director/Critic responses. Synthetic timing output, if tested, is logged separately.

## A. Silent 30-second wind-up animation

The [timeline](silent-30s.timeline.json) maps a real upstream shot-plan snapshot;
the hash and mapping are tested without editing that source. No board/clip was
supplied: native source availability, source ranges and playback quality are
unknown. 24 fps comes from the plan. Source intervals are provisional allocations,
not evidence that frames exist. One primary cut excludes optional coverage.

| Event / shot | Record frames [in,out) at 24 fps | Purpose / trim decision | Check before final |
| --- | --- | --- | --- |
| ED-E001 / S010-SH010 | 0–120 | Enter and notice fallen bird; retain discovery before intervention. | Gaze and bird must read without audio. |
| ED-E002 / S010-SH020 | 120–216 | Lift bird to table; preserve continuous hand support and contact. | No teleport floor→table or new hand/prop state. |
| ED-E003 / S010-SH030 | 216–336 | Notice key and reach; audience recognizes cause-to-come. | Key recognition survives output-size preview. |
| ED-E004 / S010-SH040 | 336–480 | Wind key once; select clean action rather than repeated redundant motion. | One winding, consistent own-left/own-right identity, lamp on. |
| ED-E005 / S010-SH050 | 480–576 | Release and wait; delay separates effort from result. | Release visible; hold tests anticipation rather than empty runtime. |
| ED-E006 / S010-SH060 | 576–720 | Movement and response; preserve payoff in shared space. | Bird's chipped left wing and N's reaction remain readable. |

Local editorial treatment: audience moves from concern to recognition of care,
then anticipation and relief. Hard cuts keep cause/action relations direct;
do not add a dissolve to conceal missing contact. Compare a shorter waiting
variant after actual animatic timing: if ED-E005 loses 12 frames, preserve total
only if a supported, meaningful extra 12-frame reaction is available. Record
source/record delta and affected cues; never stretch nonexistent footage.
Counterexample: move the moving bird before winding for a “hook.” That changes
the causal/reveal order and requires approval; it is not a routine trim.

## B. Dialogue, axis and listening

Assumed supplied coverage: master with A left/B right, CU-A looking right,
CU-B looking left, and a second CU-B on the far side. Script beat: A admits the
key is gone; B conceals relief. Take 2 contains a small release of B's jaw after
the admission. Select that listening turn provisionally; stay on A through the
admission's crucial word, then test B while the trailing phrase continues.

Choose the compatible CU-B or hold the master. The far-side CU-B is not cured by
inserting a random clock: reorientation must actually establish the new relation.
Do not mirror it if costume/text/identity are asymmetric. If incompatible take
is the only emotional performance, compare an intentionally reoriented version
with Director and coverage owner. No footage here means no observed eyeline pass.

## C. Suspense vs comedy vs long-take emotion

Suspense: audience knows a watcher is behind the door; character does not.
Protect that imbalance. Hold the listener at the ambiguous creak; reveal only
at the approved door opening. A prelap of an identifying voice or captions
“[Mara laughs]” could spoil the protected identity before picture does.

Comedy: a character boasts that a repaired bird is silent; it squeaks at the
worst moment. Test action→small registering delay→deadpan reaction against a
version that stays in the two-shot. A reaction before the squeak announces the
joke; an arbitrary pause length ignores performance and actual sound timing.
These variants are a test proposal, not evidence of laughs.

Emotion: the actor's silent acceptance unfolds across 18 seconds of a take.
Retain the turn if it remains active and legible; compare a single motivated
listener cut after the realization. Reject a compulsory rapid montage that
removes the moment of change. 18 seconds is this hypothetical take, not a rule.

## D. J/L cuts and source/record math

Assume 24 fps sequence; source picture/audio are 48 kHz-linked through a known
anchor. Picture B begins at record frame 96. B audio starts at frame 84 (J),
and A audio remains until frame 108 (L), on separate audio tracks. Incoming B
source sample 24,000 at record frame 96 maps to sample 0 at frame 84, since
12 frames × 2,000 samples/frame = 24,000. A's outgoing audio extends under B
for 12 frames; adequate source availability/handles are required separately.

These overlapping ranges do not imply an audio mix is correct. Preserve anchors,
listen to both voices/room tone and compare start/mid/end sync. If B's identifying
audio violates a protected reveal, move/replace the cue with Sound Designer's
approval as required. A synthetic pulse can test numeric alignment, not lip sync.

## E. AI trim vs regeneration

Assume actual inspected take A lasts 7.2 s, becomes malformed after 5.8 s, and
its complete key release ends at 5.2 s. A 5.4 s trim may preserve action while
losing outgoing dissolve room: test hard cut/alternate coverage and actual
adjacent state. Do not promise a 12-frame handle unless it exists cleanly.

Countercase: deformation spans 2.0–3.0 s, the only key transfer. Trimming it away
removes the cause; slowing or optical-flow interpolation can create more defects.
Request a new take matching contact phase, identity/prop version, screen direction
and entry/exit state, within authorized generation budget. These numbers are
scenario inputs; no provider/model was invoked by this example.

## F. Picture-lock revision and selective invalidation

CUT-04 v3 is hypothetically picture-locked at 720 frames. CR-07 requests a
12-frame extension of the release at frame 576. First verify the actual request's
scope/authority; a Critic suggestion alone does not unlock picture. If authorized,
create CUT-04 v4. If there is clean source, a ripple makes 732 frames; if a
720-frame slot is locked, propose an explicit compensating 12-frame trim with
its dramatic cost instead of silently stealing the payoff.

Mark shifted bird-motion cues, music hit, captions, grade/conform/exports and
lock reference stale as applicable; keep an unrelated episode current. A
same-duration alternate can still change Foley contact or facial performance.
Recheck the new release→movement join, returned audio anchors and final file.
Log Critic note, Editor implementation and Director disposition separately.
