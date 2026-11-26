# Story production contract

These are local interfaces, compatible with Artist's IDs/version/status and
handoff approach. No external schema, launcher or installed collaborator is
implied. Keep this folder self-contained; the consuming project chooses storage
and identifiers. Use only fields needed for the task, not a mandatory questionnaire.

## Input contract

| Input | Meaning / handling |
| --- | --- |
| Task and use | Supplied project/task ID, audience, purpose, medium, language and length/budget. Unknown audience is an assumption, not researched positioning. |
| Requested level | Idea/options, premise/logline, complete synopsis, standalone prose, treatment/outline, beat-level design, bible, review or revision. |
| Intent | Desired experience, genre/tonal promise, thematic inquiry, exclusions and source/inspiration roles. |
| Canon and evidence | Current narrative bible/version, relevant episode/scene/character/world/prop/location IDs, selected material and approval source. Appearance locks come from supplied art records. |
| Change scope | Locked facts vs authorized revisions; supplied feedback and whether diagnosis or actual editing is requested. |
| Constraints | Dialogue/text limits, duration/word target, setting/cast/location limits, required beats/endings, culture/factual dependencies. |
| Acceptance | What must be observable in the delivered story and who selects recurring canon. |

Missing canon needed for exact continuation is consequential: ask for the relevant
record and continue only with unaffected work or clearly provisional alternatives.
A short original-story brief is normally enough to proceed. Do not make up an
“approved previous episode” to avoid asking for missing continuity.

## Deliverable contract

Choose the requested level rather than always supplying all of these:

| Deliverable | Smallest useful contents | Not a substitute for |
| --- | --- | --- |
| Concept / premise / logline | Particular situation/organizing interest; meaningful differences for options; chosen direction and why if requested. | A list of themes described as a finished story. |
| Synopsis | Beginning, consequential development and ending, with the relevant emotional/relational change. Label spoiler-free pitch copy separately. | A tease that conceals the missing resolution. |
| Outline / treatment | Connected events in presentation order, ending, access and pacing intent, meaningful story-time anchors. | A screenplay or shot list. |
| Narrative beat table | Stable beat IDs; before → action/discovery/association → after; link/function; audience evidence and continuity dependencies. | A list of emotions or framework stage names with no events. |
| Story bible | Reusable narrative canon, status/provenance, characters/relations/world limits, chronology/knowledge, open promises and revision history. | Artist's visual bible, a pitch deck, or permanent approval of every proposal. |
| Standalone authored story | Actual prose/story text at requested scope; continuity and research notes only as needed. | Writing advice, when the user asked for a story. |
| Review / revision | Located issue → effect → correction/retest; for revision, changed material and dependency status. | Independent Critic sign-off or owner approval. |

Use [story-bible.md](../templates/story-bible.md) for recurring facts and
[story-outline.md](../templates/story-outline.md) for synopsis, outline and beats.
They are records with optional sections, not two competing story methods.

For production, include a compact packet in prose or this YAML-shaped form:

```yaml
task_id: supplied ID, if any
status: draft | reviewed | approved | blocked
story_id: supplied ID, or stable local ID for recurring work
version: revision ID
supersedes: prior version, if any
canon_used: narrative and relevant visual record IDs/versions
deliverables:
  - id: outline or bible ID
    path_or_text: actual saved path or material included in the response
    scope: synopsis, outline, beats, bible, or prose
assumptions: consequential assumptions and invented facts
checks: performed checks and unresolved checks
pending: decisions, factual dependencies, or stale downstream packets
handoff: receiver and relevant narrative invariants
```

“Reviewed” means scoped self-review with evidence, not approval. “Approved” needs
a supplied owner selection/source, scoped to the selected material. Story text
is an actual artifact; a written plan for a film remains a plan. Do not claim
rendered timing, image production, audience comprehension or collaborator review.

## Ownership and collaboration

| Collaborator | Exchange / decision boundary |
| --- | --- |
| User / Director | Receive experience, constraints and selected canon; return meaningful story options, consequences and unresolved cross-role trade-offs. Director integrates the production interpretation. A direct user brief needs no Director ceremony. |
| Screenwriter | Send event logic, character motive/knowledge, intended inference, story IDs/versions and locks. Receiver develops playable scenes/dialogue, script scene IDs and dramatic realization. Scene splits/reorders may be proposed; changes to story facts must be explicit. Narrative POV planning is shared with realization, not transferred wholesale. |
| Artist | Send narrative role, world/function limits, significant object/location states, relevant IDs/versions and emotional intent. Artist chooses/develops appearance within supplied locks. Return design implications as proposals: an unreadable story clue may need narrative redesign; neither side silently changes canon. |
| Cinematographer | Send what the audience must perceive or not yet know, story order and constraints. Receive feasibility/readability concerns. Do not specify lens, angle, coverage or boards as Storyteller's output. |
| Critic | Supply brief, actual story/version, intended effect and uncertainty; receive independent diagnosis. Self-review is labeled. A critique is neither authorization to rewrite canon nor proof of audience response. |
| Strategist | Receive actual audience/use evidence and positioning constraints; return premise/genre promises and testable experience hypotheses. Do not invent research, retention statistics, popularity or guaranteed engagement. |

Use the smallest receiver packet that preserves intent. Ordinary standalone work
does not need messages to imaginary specialists. Role interfaces do not authorize
contacting people, publishing, installing or launching agents.

## Canon, continuity and conflicts

Distinguish (1) world events/rules, (2) character beliefs/knowledge and (3) audience
disclosures. A draft alternative lives outside selected canon. Preserve project
IDs, and map new beat IDs to supplied scene/episode IDs without renaming them.
Appearance facts remain in the art record; refer by version and record the
narrative reason a design detail is required.

When documents disagree, identify the exact claims and versions rather than
silently declaring one newer-looking document authoritative. If a request clearly
revises a lock, carry it out in a new version and retain the earlier one. If it
does not authorize the conflicting change, ask a focused question and continue
unaffected work. Do not promote an assumption into approved canon.

For revisions record reason/authorization, changed facts and beats, preserved
invariants, superseded version and affected outputs. Follow
[review-revision.md](review-revision.md) for diagnosis and propagation.
