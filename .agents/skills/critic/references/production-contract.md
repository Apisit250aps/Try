# Critic production contract

Local semantic proposal **`critic-review/0.1`**, not a shared API, launcher or
claim that another skill implements these fields. Ownership comes from the user
and repository, not from film theory. [P14](evidence-map.md).

## Receive

Extract from the request; do not turn optional fields into a questionnaire:

| Input | Minimum meaning |
| --- | --- |
| Brief | Intended experience, purpose, audience/language, genre, medium, duration/use context, exclusions, acceptance criteria and creative locks. Unknowns stay assumptions. |
| Scope | Concept, bible, screenplay, art/character, shot plan/boards, animatic, rough cut, final cut, cross-artifact, standalone or fix verification. Requested depth and review budget. |
| Evidence | Actual text/files/attachments/locators, artifact IDs, revision/status, provenance, scene/beat/shot IDs, cut identifier and timebase where supplied. A link listed is not necessarily accessible or inspected. |
| Context | Canon/look/script/shot-plan versions, relevant prior episodes, intentional deviations, references' roles and authority source. Conflicting approvals stay unresolved until clarified. |
| Capability | What the host/model can read, see, play, hear or measure; inspected ranges, frame sampling and audio availability. Do not assume a tool or model capability from the role name. |
| Decision | Who can revise/approve, mandatory delivery constraints, priorities, current notes and previous issue states. |

If no version/IDs exist, assign **local review labels** to the supplied material
(for example `submitted-excerpt-A`, paragraph3); do not present them as upstream
production IDs. A missing bible blocks canon certification, not an otherwise
useful standalone reading. Missing sound blocks a mix judgment; continue script
or visible checks with that limit. A description of an image is text evidence
about the description, not direct visual inspection.

## Return

Use [report template](../templates/review-report.md) selectively. A short review
can be prose with the same information. Record:

- Review ID/version, reviewer relationship (independent, same-author or assisted),
  mode, brief/criteria versions and scope of inspection.
- Inventory with artifact ID/version/locator, status/authority, modality,
  inspected subset, tools, not-assessed areas and reasons.
- Strengths to preserve and a scoped independent recommendation: `revise`,
  `ready-for-owner-decision`, `insufficient-evidence` or `no-change-recommended`.
  This is never production approval or a delivery-compliance certificate.
- Stable issue IDs and evidence fields below; rubric/gates/coverage when used;
  unresolved interpretations/decisions, next owner and concrete verification.

### Issue fields

`issue_id`, `category`, `artifact_id`, `revision`, `location`, `expected`,
`observed`, `evidence_basis`, `interpretation`, `impact`, `severity`, `confidence`,
`uncertainty`, `cause_status`, `cause`, `dependencies`, `owner`, `options`,
`tradeoffs`, `acceptance`, `state`, `verification_evidence`, `owner_decision`.

Category: technical defect / creative-intent mismatch / consistency conflict /
interpretation / preference / factual-rights-access concern. A note may span
categories; distinguish what is objectively established from what is inferred.
Location can be a stable text line/paragraph, scene/beat/shot, frame/region or
cut time interval. Use timecode only with a real source: record cut revision,
start offset and known fps/drop-frame basis, otherwise label elapsed timestamps
or scene/paragraph locators. Do not invent frame-exact precision from sparse frames.

`expected` cites a brief/lock, applicable requirement or declared criterion.
`observed` describes evidence; `impact` explains a plausible consequence, not
guaranteed viewer response. `cause_status`: demonstrated / hypothesis / unknown.
One supported option is enough for a simple fix; meaningful creative trade-offs
usually warrant alternatives, including retaining an intentional choice.

Before returning an issue ID, include both severity and confidence even in a
compact note. `needs-evidence` is a state, not a severity. If no defect is
established, report a scope limit without inventing an issue, or label a concern's
severity conditional on the consequence being confirmed; uncertainty is not
automatically a production blocker.

## Owners and decision rights

| Owner | Critic provides / receives | Boundary |
| --- | --- | --- |
| Director or direct user | Independent recommendation, intent/impact tensions, conflicting goals and costs ↔ brief, priorities, final creative selection/approval | Record accepted risk or declined note without pretending the defect vanished. No extra approval ceremony for a standalone critique. |
| Storyteller | World/event/knowledge/arc conflicts ↔ canon and narrative revision | Does not rewrite canon; identify exact fact/version and affected episode/beat. |
| Screenwriter | Scene purpose, action/dialogue/subtext/exposition findings ↔ script revision | Notes specify desired effect, not mandatory replacement lines. |
| Artist | Identity/style/readability and reference-region comparisons ↔ asset/design revision | Distinguish permanent design, scene state and perspective/stylization. |
| Cinematographer | Shot function, framing/blocking/light/continuity/coverage diagnosis ↔ shot-plan revision | Suggest outcomes/alternatives; no silent replacement shot list. |
| Sound Designer | Audible/intended clue, intelligibility and sound/image findings ↔ sound revisions | A future/unavailable role can be named as owner; no fabricated listening, mix settings or receipt. |
| Editor | Rhythm, assembly, coverage and dependency findings ↔ actual edit revision | Actual timing/cut belongs to Editor. Script allocation is not measured playback. |
| Strategist | Testable audience hypotheses ↔ audience/use research and study design | No invented retention, demographic preference or platform performance. |

Performance concerns go to Director and the relevant performance/animation maker
identified by the project; do not create an extra Agent. Rights/factual/cultural
uncertainties go to the user/producer and an appropriate qualified reviewer when
needed. Director's creative approval cannot establish legal clearance.

## Provisional adapters inside Critic

Inspected neighbors use compatible semantics but different serialization. This
table records **document-level mapping**, not an executed inter-agent protocol:

| Incoming artifact | Preserve as Critic input | Do not infer |
| --- | --- | --- |
| Storyteller `story_id`, `version`, `canon_used`, narrative beats and disclosure/knowledge ledger | `artifact_id/revision`, upstream references; distinguish world truth, character belief and audience disclosure | `reviewed` means independent approval, or narrative beats equal shot IDs |
| Screenwriter script/scene/scene-beat IDs, upstream narrative links, estimated timing and revision packet | Retain each ID namespace, timing basis and changed-note links | One script scene equals one shot, or a planned read-through occurred |
| Artist `assets[].id/version/path_or_result`, `scene_shot`, `canon`, `checks` | Asset/version/locator plus look locks and actual inspection state | A prompt/seed proves identity; status `approved` is proof without its authority/source |
| Cinematographer `contract: cinematographer-shot-package/0.1`, `scene`, `shots`, `boards`, `references`, `checks` | Scene/shot/beat links, planned purpose/states, real board/clip locator or null | Null boards are images; proposed duration is measured; plans prove camera/light execution |
| Director `director-packet/0.1` (appeared during this task) | Supplied treatment/brief, selected intent, typed upstream IDs, locks, decisions and approval source/scope/version; preserve creative status, artifact evidence, execution and dependency-validity axes separately | Folder presence means runtime/availability; creative approval means technical, rights or release approval. Contract remains provisional and needs reinspection at actual handoff |
| Sound Designer / Editor / Strategist | Actual supplied sound/cut/research packet with IDs/versions and limits | Their skills exist or have acknowledged notes |

Keep unmapped fields and source labels in the review inventory; explain ambiguous
mappings locally. Inspect the actual incoming contract/revision again before
claiming compatibility after parallel changes. No edits to sibling/shared files
are needed. No runtime adapter code is justified until a concrete consumer needs
serialization. Handoff example: `CR-07 → Screenwriter, script v4 S020/B03: make
the key transfer perceivable before S030; preserve mystery identity; compare v5
script plus downstream SH040 plan; receiver response pending`.

## Conflicts and state

Newest-looking document is not automatically canonical. Identify competing facts,
versions and selection evidence. A user-authorized change supersedes an old lock
within that scope; retain history and mark dependent artifacts stale. Never keep
flagging an explicitly superseded rule as a current error.

Issue state: `open → revision-proposed → implemented-unverified → verified`.
Also allow `needs-evidence`, `disputed`, `declined/accepted-risk` and `reopened`.
Store Director/user decision separately with source/scope/date. A creator saying
“fixed” supports implemented-unverified; actual comparison supports verified.
Approval is an owner decision, never an automatic transition from verification.
