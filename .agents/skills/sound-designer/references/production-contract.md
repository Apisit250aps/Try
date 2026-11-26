# Sound production contract

**Local proposal: `sound-packet/0.1`.** Semantic interchange for The Stories,
not a shared runtime schema or an assertion that another agent supports it.
Keep supplied names through an explicit adapter; no sibling installation is
required. Contract choices are local synthesis P10 in [notes](../research/notes.md).

## Receive

Read task/project/episode, requested deliverable/language, audience/medium,
narrative intent and protected reveals; actual script/scene/beat/shot/cut locators,
versions and authority; sound/look/voice bibles; tools/media; budget and production
limits; rights/consent evidence; destination specs and acceptance owner.
For a concept, a sentence can suffice. For exact sync, require the relevant cut
and timeline metadata; for a mix, actual source audio and channel layout.
Missing locks or media block only dependent work. Do not invent canon or approval.

## Owners and receiver checks

| Owner | Sound Designer exchange | Boundary / receiver acceptance |
| --- | --- | --- |
| Director / user | Listening interpretation, performance options, sound priorities and costs ↔ intent and creative selection | Director sets integrated performance intent; Sound Designer translates it into vocal/acoustic directions. Flag any reveal/tone conflict before changing it. |
| Storyteller | Motif/canon/knowledge constraints ↔ sound implications | A cue identifying the killer changes disclosure; request that decision, preserve ambiguity meanwhile. |
| Screenwriter | Versioned dialogue/VO, essential sounds, silence and scene beats ↔ pronounceability/ADR/localization needs | Preserve exact approved line text; return proposed wording separately for writer approval. |
| Cinematographer / animation implementer | Visible sync actions, offscreen geography, shot IDs, mouth/action anchors ↔ perspective and sync requirements | Do not equate camera position with listener position. Send audio/viseme timing; receiver implements mouth/body motion and checks actual picture. |
| Artist | Prop/material/location/design versions ↔ Foley texture and acoustic-space needs | Do not alter prop material or visual canon to suit a library sound. |
| Editor | Cut ID/version, rational fps/timecode, action anchors, source media and change list ↔ cue/stem plan, handles, sync/tail needs | Editor implements picture edits and conform; changes affecting causal inference return to Director/writer. Receiver checks alignment, exact start, tails, channel map and cut version. |
| Composer / music editor | Emotional function, entry/exit/hit anchors, space for speech, resources and rights ↔ demos/score/stems | Direction is not composed/recorded music. Keep temp material distinct from cleared masters. |
| Recordist / performer / mixer | Recording or mix brief, selects, consent scope and delivery spec ↔ actual takes/session/mix/log | Naming an implementer does not dispatch work; verify availability, actual receipt and returned evidence. |
| Critic | Unchanged intent, artifact/version, inspected ranges and open checks ↔ located independent findings | Sound self-review is not Critic approval. Rights/creative/technical/release acceptance are separate. |
| Producer / Strategist, if present | Resource estimates, platform constraints, clearance needs ↔ budget or verified destination evidence | Do not infer authorization to spend, license, upload or publish. |

## Packet and cue identity

Small answers can use prose; production packets use these semantics with the
[templates](../templates/cue-sheet.md):

- Header: `contract`, project/episode/task, packet ID/version, status, upstream
  locators/versions/status, locks, assumptions, tools/media inspected and gaps.
- Timeline: cut ID/version/hash if available, rational playback fps (e.g.
  `24000/1001`), timecode convention DF/NDF where applicable, start timecode and
  origin, duration, sample rate, source vs sequence time domains, channel layout.
  Missing values are unknown, never guessed as verified.
- Cue: stable cue ID/version, scene ID, typed narrative/script beat links and
  zero/one/many shot IDs; function, audience inference, diegesis, listener/world
  perspective; category; entry/exit and sync anchors; timing basis/status,
  source trims/offsets/handles/tails, dependencies, priority, asset/take IDs,
  rights/consent status, caption note, owner, acceptance test and evidence.
- Handoff: actual artifacts/locators, intended receiver, mapping, revision delta,
  stale dependencies, open decisions, requested receipt and acceptance source.

Reuse upstream IDs verbatim. If absent, label local IDs, e.g. `LOC-S010`,
`LOC-S010-SH020`, `SD-C010`, `SD-A010`, `SD-V001`; ID is separate from order,
version and take. Keep IDs on reorder. Retire deletions and map split/merge IDs;
one bridge may cross scenes, one cue may have several takes or locale versions.

### Timing rules

Prefer half-open sequence intervals `[in,out)`; record units. Integer frames
plus the declared rational rate avoid ambiguous decimal timecode. Audio offsets
can use integer samples plus sample rate. A source offset is not sequence time.
Record conversion and rounding when frame boundaries fall between samples.
Do not interpret NDF labels as wall-clock seconds or apply DF to every frame rate.
For VFR material ask Editor for a conformed reference or explicit PTS mapping.

An anchor contains ID, observable action/phoneme, scene/shot, cut version, time
domain, frame/sample/PTS position or null, estimate basis and tolerance agreed
with receiver. Script-only anchors are descriptive estimates. No cut means no
frame-accurate sync claim. Duration estimates do not prove performed speech fits.
Keep pre/post handles and reverb tails outside narrative runtime unless specified.

## State, conform and compatibility

Record spec status (draft/reviewed/approved/blocked/superseded) independently of
audio evidence (absent/produced-uninspected/listened/measured/accepted). Approval
records need who/source/date/version/scope; a self-review is scoped and identified.
Rights are unknown/pending/restricted/cleared-for-specified-use, never inherited
from creative approval. Keep planned checks and observed results separate.

For revisions record authorization, old/new cut and packet versions, changed cue
IDs, source trims, sync shifts, retired/replaced assets, invariants, impacted
captions/visemes/music/stems and tests. An insert does not justify shifting every
later cue blindly: compare anchors, changed durations, overlaps and tails. Keep
old exports; mark stale evidence until reconformed and rechecked.

Current neighbors use Director `upstream`/locks/decisions, Screenwriter scene
ledger/beat mapping/timing basis, and Cinematographer `scene`, `shots`,
`proposed_sequence`, `duration_seconds`, `continuity`, `checks`, `handoff`.
Map those into header/typed cue links/estimated anchors without renaming the
source fields or treating alternate coverage as extra runtime. Preserve unknown
fields as attached source notes. Critic findings map by artifact revision and
located cue/shot/range. Actual incoming packets outrank these development-time
examples. Dangling or ambiguous IDs stay unresolved, even if prose looks similar.

A walkthrough is not a live handoff. Record dispatch, receipt, implementation
and acceptance only when they occur. No launcher, messaging service or receiver
response is supplied by this skill.
