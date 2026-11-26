# Versioned narrative packet and collaboration

This is a local, model-agnostic semantic adapter, `narrative-packet/0.1`, not a
shared schema or an assertion that a receiver implements it. Preserve existing
project identifiers and source records; map fields without changing shared
contracts. If a field has no counterpart, carry it as an extension and explicitly
ask the receiving owner to accept the mapping. No installation or orchestration is
implied. For small standalone work use only relevant fields; do not invent IDs
for existing records. [Template](../templates/narrative-packet.md).

## Record semantics

Every packet: project/story/packet ID and version, request, owner, provenance,
status (proposed/approved/superseded), authority and approval scope, dependencies
with IDs and versions, assumptions, change history, pending decisions and evidence.
Graph: start node; stable route, node, choice, edge and ending IDs, types, narrative
purpose, scene/clip/asset IDs@versions, source and target. Node records distinguish
canonical facts from route-specific facts and character/audience knowledge.
Choice: framing, actor/input, options and availability, knowledge/uncertainty,
immediate and delayed effects, expected narrative impact and feedback.
State dictionary: type/domain/initial/visibility/owner, scope and invariants.
Edge: precondition/guard evaluated on pre-transition state, effect, order and target.
Ending matrix: eligibility guards, priority, ties, fallback and payoff; indicate
whether guards overlap and whether every reachable terminal state is covered.
Record clip duration, route duration, story time and estimated cost with units and
uncertainty; variants and shared assets need separate references and ownership.

For a given decision point define atomic evaluation: snapshot state; calculate
eligible guards; select according to explicit priority and tie-break; apply effects
in specified order; check types/invariants; move to target and record feedback.
Fallback applies only when no ordinary guard is eligible; it must itself be valid.
If rules are unresolved, report a conflict, not an invented ordering. Mark stochastic
rules, seed and probability if used. Conditional expressions are documented in
plain language unless a project has an actual executable language and interpreter.

## Role handoffs

| Owner | Input and responsibility |
| --- | --- |
| Storyteller | Versioned story bible, theme, character/world facts and event/ending proposals; co-authors branch events/endings and resolves canon. |
| Narrative Designer | Graph, choice/consequence and state records, ending resolution, branch validation and production branch plan. |
| Screenwriter | Route/node/scene IDs, entry state, exit and knowledge constraints → playable scene/dialogue; owns screenplay. |
| Director | Experience, trade-offs, budget, conflicts and delegated authority → creative vision and approval within actual authority. |
| Critic | Independent review with evidence and uncertainty; no automatic approval. |
| Strategist | Audience, distribution, navigation and release evidence; no invented platform capability. |
| Artist / Cinematographer / Sound Designer / Editor | Asset variants, shot, cue and timeline/alternate-cut constraints; retain each specialist's ownership. |

Supply each recipient the smallest relevant slice: IDs@version, entry/exit state,
canon, event and knowledge constraints, impact, media references, budget, open
questions, acceptance owner/status and evidence. Ask for a receipt/acceptance only
when actually needed; record pending if unavailable. If working alone, supply the
same explicit assumptions without pretending others acted.

A change to canon, graph, guard, state, asset or timing maps affected route/node,
ending, script, edit, release and validation dependencies; mark previous validation
stale, notify the actual owner when communication is authorized, and re-run affected
checks. Do not overwrite approved material; propose revisions to the authority
recorded in the project. Resolve unresolved incompatible approvals before delivery.
This mapping is a compatibility proposal, not evidence of interoperability.
