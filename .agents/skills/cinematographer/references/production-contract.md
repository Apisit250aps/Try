# Cinematographer production contract

**Local proposal: `cinematographer-shot-package/0.1`.** A semantic interchange
format for this skill, not a shared runtime API or a claim that other agents
already implement it. Preserve supplied field names through a local mapping;
don't modify sibling skills to force compatibility. [S01/S02 in
research notes](../research/notes.md).

## Receive

| Input | Interpretation |
| --- | --- |
| Task / intent | Project/task, requested level (strategy/list/spec/boards/previs/review/revision), language, audience and intended experience. Standalone users may supply a sentence. |
| Narrative / screenplay | Actual text/locator, version/status; scene ID, narrative beat IDs, script beat IDs, action/dialogue and presentation order. Mark mandatory disclosures vs open visualization choices. |
| Authority | Locked canon/look/action, approved changes, evidence of selection and unresolved decisions. Newest-looking file is not automatically authoritative. |
| References | Character/costume/prop/location/look IDs and versions; actual paths/URLs/attachments; each input's role, inspected state and material reuse limits. |
| Production | Medium, ratio/dimensions, capture/playback fps if relevant, runtime target, cast/set/rig/render/generation limits, available tools, schedule and shot budget. |
| State / acceptance | Entry/exit, time/weather, ownership/contact, knowledge, source directions, required readable details and test/approver. |

Missing details do not force a questionnaire. For a one-off original brief,
propose blocking and IDs and label them local/draft. Do not invent approved canon
or a prior scene's state. Missing exact identity reference blocks identity
certification; missing script reveal order may block final reveal planning while
an unaffected geography/coverage proposal continues.

## Return at the requested level

Small requests may use prose/table. Detailed or recurring sequences use the
[packet template](../templates/shot-package.md). The JSON
[30-second example](../examples/silent-30s.json) is a concrete interchange example,
not an external service schema. Omit irrelevant capture settings for simple
boards; keep identity, purpose, states and provenance meaningful.

| Level | Minimum usable output |
| --- | --- |
| Strategy | Script/intent version, audience information/emotion hypothesis, visual approach, meaningful trade-off and test. |
| Shot list | Stable shot/scene/beat links, order, purpose, scale/function, blocking, camera/light summary, duration estimate and essential/optional distinction. |
| Detailed shot package | Fields below, board/previs specification and validation/handoff notes. |
| Review / revision | Located observation/evidence → consequence → remedy → retest; revision additionally records actual changed specs and downstream impact. |

### Detailed packet fields

`contract`, `project_id`, `task_id`, `version`, `status`, `supersedes`,
`upstream`, `locked_facts`, `assumptions`, `pending`, `format`, `scene`,
`references`, `shots`, `proposed_sequence`, `target_duration_seconds`, `checks`
and `handoff`. Preserve extra incoming fields/locators as needed.

- `upstream`: role, document ID/version/status; retain actual artifact locator.
- `scene`: stable `id`, `narrative_beat_ids`, `script_beat_ids`, geography and
  intent; beat lists declare the identifiers used by shots, not replacement text.
- `format`: output width/height, playback fps, normalized `action_safe` rectangle
  `[left,top,right,bottom]` (origin top-left), safe-area authority/status. Record
  capture gate/rate separately when relevant. Never imply provisional margins
  are platform-certified.
- `references`: stable `id`, `version`, role, locator, status/inspection; keep
  missing locators explicit rather than pretending assets exist.
- `shots`: stable `id`, scene and both beat links, version/status, `purpose`,
  `audience` before/after and emotion hypothesis, `reference_ids`, `blocking`,
  `camera`, `light`, `action`, `duration_seconds`, `continuity`, `transition`,
  `coverage`, `generation`, `boards` and `validation`.
- `camera`: station/height, aim/angle, scale, gate/FOV or qualified lens, motion
  start/path/end, support and focus plan. Technical precision scales to the task.
- `light`: world-source direction, quality, contrast/motivation, practical state,
  color/WB intent and continuity/deviations from look version.
- `action`: description plus `start_state` and `end_state`, including relevant
  pose, hands, object/identity, location and light facts. Use stable state keys
  across continuous shots so comparisons are possible; keys describe world
  state, not changing camera views.
- `continuity`: `relation` to previous primary shot (`start`, `continuous`,
  `ellipsis`, `overlap`, `parallel`), axis/eyeline/screen direction and `exception`
  explaining a deliberate state/time mismatch. Blank exception is fine when none.
- `coverage`: essential/optional role, protected beat, alternate connection and
  what is lost if omitted. `proposed_sequence` lists only the primary cut proposal;
  alternate coverage is not added to runtime.
- `generation`: subject motion, camera motion, constraints, `start_frame_id`,
  `end_frame_id` referencing panel specs, capability/budget status; actual
  provider invocation stays in a separate adapter record when there is one.
- `boards`: panel `id`, start/key/end role, concrete composition/action and actual
  artifact locator or null. Panels are not automatically one-to-one with shots.
- `validation`: requested checks and actual status/evidence. `checks` at packet
  level records performed tests. Timing includes basis and uncertainty in notes;
  `duration_seconds` is the estimated primary screen allocation, not handles.

### Identity and revision rules

Reuse upstream scene/beat IDs verbatim. A narrative beat can map to several script
beats and shots; a shot can span beats. If no scheme exists, assign local IDs
like `LOC-S010`, `LOC-S010-B01`, `LOC-S010-SH010`; don't renumber on reorder.
Separate ID from version, panel and take IDs. On split/merge, retire IDs and
record old → new mappings; retain earlier packages.

`draft`, `reviewed`, `approved`, `blocked` describe spec status. Reviewed means
scoped self-review, not owner approval; approved requires approval source/scope.
Artifact evidence states (spec-only, generated-uninspected, inspected, accepted)
are separate. Never promote planned validation to performed evidence.

For a revision record note/authorization, from/to version, changed shot IDs,
unchanged invariants, acceptance test and affected boards/clips/cut. An approved
script revision can invalidate camera/asset plans; mark stale links, not just
the changed document. Where versions conflict, report the exact conflict and
offer a canon-preserving plan plus a separate change proposal. Continue unaffected
work. [S02]

## Receiver handoff and local adapters

| Owner | Send / receive | Boundary / actionable receiver check |
| --- | --- | --- |
| Director / user | Visual strategy, coverage alternatives, performance demands and costs ↔ intent and selected interpretation | Ask which conflicting goal takes priority; no invented approval service. |
| Screenwriter | Scene/script-beat IDs, required clue/action dependencies ↔ camera feasibility/readability | Preserve dialogue and action; return “S030-B02 cannot expose seal at current prop angle; can blocking change?” |
| Storyteller | Narrative beat links and audience knowledge ledger ↔ canon/reveal invariants | A shot revealing the culprit earlier is a story-change proposal, not routine coverage. |
| Artist | Panel specs, frame/asset/version references, set landmarks, light plan ↔ rendered frames and design constraints | Artist renders; receiver checks asymmetry, construction, readable pose and named panel state. Look-bible changes remain explicit. |
| Editor | Proposed order, alternates, action phase/handles, duration basis and required holds ↔ measured cut/timing | Editor can test trims/reorder; changing causal inference is flagged to Director/Screenwriter. |
| Sound Designer | Look/reveal triggers, visible sync events, offscreen geography, required silence/audio dependencies ↔ cue timing needs | Sound treatment belongs to receiver; a silent test cannot rely on an unprovided sound. |

**Parallel adapter procedure:** read the actual incoming artifact; keep its
version/locator and field names in a mapping such as `source scene ledger.Scene
ID → scene.id`, `source beat IDs → script_beat_ids`. Preserve narrative and script
beat types even when both are called B01. Carry unknown fields in an attached
source note. Ambiguous/dangling IDs stay unresolved; don't merge by similar prose.
Export the fields the receiver actually consumes and ask for one concrete missing
decision. Record a receipt only when a receiver really responds. A fabricated
role-play handoff is a walkthrough, not live integration. The package requires
no sibling paths and no messaging or agent launching. [S01/S02]
