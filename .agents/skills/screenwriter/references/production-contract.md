# Production contract

These are **The Stories interface proposals**, not universal studio job rules.
Use existing project field names and IDs when supplied. No sibling file path,
API, schema, launcher or approval service is assumed. See
[P10](../research/notes.md#p10-local-contracts) for provenance.

## Receive and resolve

Extract task/project, mode (draft/adapt/revise/analyze), requested deliverable,
medium/house style, language/register, audience, duration/slot, production limits,
outline/bible/version, narrative beat IDs, character/location/prop IDs, rights
context when adapting, and acceptance criteria. Do not demand a complete bible
for a standalone sketch. For an exact continuation, missing prior episode state
may block only continuity certification; offer a provisional scene with that limit.

Preserve semantic links: narrative beat → script scene ID → scene beat ID →
production requirement. A scene beat is a change in tactic, attention, knowledge,
relationship or action, not an automatic synonym for a shot or story-outline beat.
Retain source IDs; map rather than silently rename them. If no ID scheme exists,
propose stable local IDs such as E02-S030 / B02, clearly marked local.

| Owner | Screenwriter receives / returns | Escalate when |
| --- | --- | --- |
| Storyteller | Canon, plot, theme, world rules, arc, outline/narrative beats → playable realization, continuity findings, adaptation alternatives | Compression changes a cause, motive, relationship, world rule, reveal order with plot consequences, or arc outcome |
| Director | Vision, tone, approvals, priorities → draft/options and explained audience effect | Creative intent conflicts with resources or owners disagree |
| Cinematographer | Existing scene geography/camera locks → visible information, action dependencies, reveal order and spatial needs | A required clue cannot read within a locked plan; propose options, do not replace the shot list |
| Artist | Approved look/assets → character/prop/location IDs, visible state, necessary interaction/readability | Script needs a missing asset, appearance or permanent design change |
| Editor | Slot/assembly constraints → script order, approximate beat durations, mandatory setup/payoff and optional trims | Trimming/reordering changes comprehension or continuity; Editor owns actual timeline |
| Sound Designer | Supplied audio constraints → dialogue/VO, story-essential sounds and silence/function | Sound carries an indispensable clue; designer owns treatment, performance/audio direction and mix |

## Standalone and parallel development

When alone, write the requested script using a compact provisional premise and
state assumptions. The user may approve it. Do not fabricate a Storyteller review
or call a draft canon. If sibling skills are under development, use this semantic
contract provisionally, inspect actual incoming artifacts when they arrive, and
report any mismatch before claiming interoperability. Screenwriter can be useful
without the other specialists passing their own evaluation gates.

Canon conflict response: cite the exact locked fact and scene consequence, offer
a canon-preserving realization and, if useful, a separate change proposal with
owner, benefit, cost and affected beats. Continue unaffected scenes. If the user
explicitly changes the fact, create a new script version and flag the upstream
bible update; do not continue treating the superseded fact as binding.

## Return and version

The smallest useful packet contains actual artifact paths/text, project and script
version, upstream versions, draft/approval status, scene/beat mapping, timing basis,
state changes, dependencies, accepted notes and unresolved owner decisions.
Include change records only for revisions: note ID → scene/version → requested
outcome → actual change → acceptance check → downstream impact → open/implemented/
verified/approved status. Implemented and verified are different states.

Keep stable IDs across reorder; retire deleted IDs, assign new ones to additions,
and record split/merge mappings. Internal IDs can live in a ledger outside a clean
submission script. Preserve earlier versions; production page locks/revision colors
follow the receiving production's scheme, not an invented universal standard.

Receiver needs an actionable question: “S030 requires the audience to read the
broken seal before the character turns; confirm readability or return a constraint.”
A text packet is not a test that the receiver actually understood or executed it.
Use the optional [packet template](../templates/script-packet.md).
