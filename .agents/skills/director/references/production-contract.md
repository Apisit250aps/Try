# Director production contract

**Provisional local interface: `director-packet/0.1`.** This is a semantic record,
not a shared schema, transport API or runtime. P10/P12–P14 in
[notes](../research/notes.md) distinguish design choices from source evidence.

## Inputs and authority

Receive the task, requested artifact/language, audience/medium/duration, creative
intent, constraints, budget/time/generation allowance, actual available roles and
tools, materials with locators and IDs/versions/status, user requirements,
approved locks, revision authorization and acceptance/approvers. A sentence can
be enough for an original treatment. Missing materials block only dependent claims.

Use supplied identifiers verbatim, preserving narrative beats, script beats,
scene IDs, assets and shots as different types. If absent, assign clearly local
IDs (e.g. DIR-T01, LOC-S010), stable across reorder. Version separately; on split/
merge retire IDs with old → new mapping. A newer timestamp does not prove authority.
An explicit user revision supersedes the relevant old lock within its scope;
do not ask again for permission already supplied. Preserve old versions and log
required upstream updates rather than pretending they already occurred.

## Responsibility, implementation and approval

| Role | Owns | Director exchange / approval boundary |
| --- | --- | --- |
| User | Requirements and granted authority; reserved approvals | Director makes creative decisions within that grant. User resolves a requirement/canon change beyond it, new cost or release approval when reserved. |
| Director | Brief/treatment, creative vision, audience experience, performance direction, specialist assignments, creative decisions/approval and log | Integrate interpretations, choose within locks, request revisions; responsibility does not grant unlimited mutation or release rights. |
| Storyteller | Canon, plot, story bible | Request story alternatives, exact fact/knowledge/reveal resolution; Director cannot quietly declare new canon. |
| Screenwriter | Screenplay and scene beats | Request playable realization, scene intent alignment, dialogue/action revisions; do not replace the script in a camera brief. |
| Artist | Visual assets and design bible | Brief appearance/readability functions; choose proposed look within authority; approved design changes require an explicit update by its owner or an authorized labeled fallback. |
| Cinematographer | Shot, camera and lighting plan | Brief perspective, coverage/performance/reveal needs; choose creative strategy, return feasibility conflicts. |
| Sound Designer | Audio design | Brief narrative listening experience, cue functions and limits; do not imply mixed audio exists. |
| Editor | Timeline and final-cut implementation | Request order, rhythm and protected beats; creative approval is distinct from actual implementation/export and final release authority. |
| Critic | Independent evaluation | Supply unchanged brief/artifact/version; consider findings and record disposition. Director's self-review cannot be labeled independent Critic approval. |
| Strategist | Audience/platform research | Use actual findings, distinguish them from an audience hypothesis. Director retains creative interpretation within user constraints. |
| Producer, if added | Production budget and schedule | Receive feasibility and cost/time estimates, propose creative trade-offs; Director cannot approve spend/schedule commitments outside authority. |

Named roles can be absent. A skill folder's presence proves neither installed
runtime capability nor active availability. Record implementer availability as
unknown/available/unavailable and execution state separately. For standalone work,
Director may draft the requested provisional material using its own capabilities,
with the role hat and limits explicit; it must not fabricate another specialist's
authorship, review or approval. Do not create other skills as a fallback.

## Minimum output and state

Return the actual requested artifact or text plus material versions used,
interpretation, decisions with rationale/trade-offs, consequential assumptions,
checks and unresolved dependencies. For coordination add assignments/next owners,
artifact/version links, approvals and downstream impact. Use the
[packet](../templates/director-packet.md) only as needed.

Keep these axes separate:

| Axis | Local vocabulary / meaning |
| --- | --- |
| Creative record status | draft → reviewed → approved; blocked or superseded as needed. Reviewed means scoped review, approved requires approver/source/scope/version. |
| Artifact evidence | spec-only; produced-uninspected; inspected; accepted. A treatment's text can be produced and reviewed while its proposed video remains spec-only. |
| Execution | not-dispatched, assigned, in-progress, returned, failed, cancelled; use only observed transitions. |
| Dependency validity | current, stale, unresolved, unaffected after recorded impact check. Stale is not deleted or automatically defective. |
| Approval | pending, granted, declined, revoked; who, actual source/date, artifact/version, scope and conditions. Creative approval, technical acceptance, rights clearance and release authorization are separate scopes. |

A specialist saying “done” is not proof of inspection or user approval. A returned
artifact on an old base is not current merely because it arrived last.
Label your own choice **Director selection** (or Director creative approval when
explicitly delegated), with its authority source. A request to create/review an
artifact is not evidence that the user has approved the resulting artifact.

## Adapters to contracts actually inspected

The 2026-11-25 comparison is documented in [audit](../research/audit.md). On a real
handoff, re-read the actual incoming packet; the following is a local mapping,
not evidence that any receiver accepts `director-packet/0.1`:

| Incoming information | Director mapping / outgoing need |
| --- | --- |
| Storyteller `story_id`, `version`, `canon_used`, `deliverables`, `pending` | upstream narrative record with actual text/locator; retain narrative IDs and locks; send interpretation/questions without rewriting source |
| Screenwriter scene ledger, scene/beat mapping, timing basis, note states | upstream script/version; keep script vs narrative IDs typed; scene intent points to both; timing remains estimated until measured |
| Artist `assets[].id/version/path_or_result/canon`, `checks`, `open_issues` | artifact registry, actual reference and evidence state; send task-specific look/readability notes, not an unsupported identity certificate |
| Cinematographer `contract: cinematographer-shot-package/0.1`, `upstream`, `scene`, `shots`, `checks`, `handoff` | retain scene/narrative/script/shot and asset IDs/versions, `proposed_sequence` and primary duration vs alternates; approve only inspected strategy/spec scope |

Preserve unknown fields in a source attachment/note. Ambiguous IDs remain unresolved;
similar prose is insufficient to merge records. Record source field → local field,
lost/unknown semantics, receiver request and actual receipt if obtained. Neighbor
contracts and their test gates may change during parallel work.
