# Formats, animatics and AI footage

Local craft/system choices [P04, P16, P17] are traced in [notes](../research/notes.md).

## Vertical short form

For 9:16, define the opening's perceptible question/promise, the development that
earns attention and a payoff that answers it. Reframe around the actual subject
and key action, not an automatic center crop. Test a phone-size preview with UI
overlays and captions. Do not crop out the hand that transfers the crucial prop.
Keep captions and readable details onscreen long enough for the actual language,
type size and viewers; document the test rather than invent a reading-speed law.

A hook can be a clear unresolved action, an image that creates a question, or a
contradiction; it need not be loud, misleading or a premature spoiler. Preserve
the promised payoff. Vary pacing with action, performance and information density,
not a mandatory cut every N seconds. No percentages for retention or guaranteed
watch-through without project analytics. Strategist supplies real audience data;
Editor can propose an A/B test with constant title/audience/distribution, defined
completion/retention measure, sample limits and a comprehension check. These are
test-design choices, not results. No platform-specific delivery numbers are
assumed in this package. Obtain and date the current destination specification.

## Long form and episodic

Maintain scene cards for function, duration basis, open question, change, entry/
exit state and setup/payoff dependencies. Review reels/acts in the whole cut;
do not optimize every scene for a miniature climax. Protect orientation after
major ellipses, meaningful recovery after peaks, and the intended endpoint.

For episodes, carry versioned character/prop/time/knowledge state from the prior
approved endpoint. Check recaps, teasers, title breaks and credits separately
from narrative runtime. A recap or trailer may expose a future reveal; treat it
as its own cut with disclosure scope. Missing previous-episode media permits a
provisional assembly but blocks certification of visual/performance continuity.
Never silently alter a preceding episode to repair the new cut. [P16]

## Animation and animatics

Animation editorial participates before completed footage exists. Board → timed
story reel/animatic → layout/previs → animation → lighting/compositing replacements
are iterations, not identical media with prettier pixels. Published practitioner
accounts describe editorial as a coordination hub; production-specific division
of labor varies. [P04]

Time boards against visible action and scratch dialogue; record whether a hold
is an estimate, acted timing, rendered motion or measured playback. A still held
for five seconds does not demonstrate a five-second performance. Use simple
boards to test information order before expensive animation. Track versions and
substitution: a new performance may need a new trim, retime, sound cue or board.
Maintain a frame allocation/change list to departments; seek coverage changes
from Cinematographer/animation maker, visual changes from Artist and dramatic
changes from Director/Screenwriter. Avoid polishing a late lock into existence.

If animation is already baked and coverage absent, compare retaining the take,
an authorized insert/reframe, an explicit ellipse or a new shot request. Do not
invent alternate views or pretend every scene can be fixed in post.

## AI video: inspect and edit observed material

These are risk-management choices [P17], not a claim that a specific model has
been tested. Check actual tool/version docs and a bounded test before asserting
generation length, start/end-frame control, seed determinism or editing support.

1. Inventory each returned asset/take/version: original file/hash, generation
   tool/version/settings/prompt/reference IDs when available, requested versus
   observed dimensions/rate/duration, rights status and inspection scope.
   Preserve original outputs; a seed is not a reproducible file by itself.
2. Review first/last frames **and motion throughout** at playback and defect
   ranges frame by frame. Log temporal wobble, extra/missing parts, identity,
   costume/prop drift, contact, text, light, background, camera path, speed and
   action completeness. Sparse samples can miss a one-frame defect.
3. Mark clean usable islands with source in/out, safe handles and narrative
   coverage. A 7.2-second generation may provide 3.4 useful seconds. Do not pad
   the cut by blindly freezing its final frame or assume its prompt's duration.
4. Compare adjacency across independent generations: entry/exit action phase,
   screen direction, eye line, body/prop positions, identity asymmetry, lens/scale,
   lighting and time. Good individual clips can still make a bad join.
5. Choose the least disruptive repair supported by the evidence below. Keep the
   failed take and rationale. Request bounded regeneration only within granted
   tool/cost scope; after repeated failure simplify the action or return a
   precise missing-coverage request. Do not silently spend on more generations.

| Defect | Editorial option / trade-off | Regenerate or return when |
| --- | --- | --- |
| Tail warps after action has resolved | Trim before defect, retaining readable result and outgoing handle. | Trimming removes the only reaction/payoff or required transition media. |
| One clean alternate covers the same beat | Substitute; compare entry/exit, performance and sync. | Alternate changes identity, prop state or protected meaning. |
| Deformed hand during sole key transfer | Do not hide by shortening past the only cause; use approved coverage if it exists. | Essential causal action is unusable; request exact contact phase/coverage. |
| Unstable motion near a speed change | Compare native timing, a simpler trim, or a tested retime with optical-flow QC. | Retime invents limbs/interpolated objects or damages dialogue sync. |
| Missing reverse | Keep oriented master or use an actually available meaningful listener shot. | Needed viewpoint/performance cannot be inferred; mark gap, no fictional take. |
| Incompatible independent start/end states | Try compatible takes or an intentional/approved ellipsis. | Continuous action cannot join without false state; request matching endpoints. |

Start/end reference frames are planned constraints until output matches them.
Record the actual reference asset versions and whether the provider honored
them. On regeneration, create a new asset version and recheck only dependent
edits, transitions, cues, captions, grade and exports; do not overwrite all cuts.

## Missing or inaccessible footage

Return a useful treatment, selects *request*, or paper edit with absent media
clearly marked. Distinguish a synthetic placeholder, unavailable shot, uninspected
clip and rejected take. List exactly what the next owner must supply and which
claims depend on it. A missing-file slate can support a review assembly; it must
not enter an unflagged final. If no tool can render, deliver an executable handoff
only when its syntax/capabilities have been checked, otherwise a labeled recipe.
