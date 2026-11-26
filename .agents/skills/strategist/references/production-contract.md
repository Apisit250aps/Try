# Strategy production contract

Local semantic proposal **`strategist-packet/0.1`** (P12). No shared schema,
runtime dispatch, account permission or receiver acceptance is implied. Use prose
for small requests; include only relevant fields, with explicit unknowns.

## Receive and return

| Record | Required meaning for a production handoff |
| --- | --- |
| Identity | `contract`, `packet_id`, `version`, `supersedes`, `channel_id`, `project_id`, `series_id`, `episode_ids`, `task_id`; retain supplied IDs, null when absent, prefix new local IDs `STR-` |
| Decision context | `as_of`, timezone, goals/priorities, funnel stage, audience needs, platform and surface, format/length, region, languages/locales, resources, exclusions, locks and their authority |
| Evidence | `evidence_id`, kind, author/source, actual locator or supplied file, inspected section/subset, publication/update date or unknown, accessed date, observation start/end/timezone, sampling/filters, population, rights/privacy/access, limitations |
| Assertion | `claim_id`, exact claim, evidence IDs, kind (empirical/official/practitioner/observation/hypothesis/design), scope, confidence (low/medium/high + reason), assumptions, contradictions, freshness/recheck trigger |
| Recommendation | stable ID, decision/options, audience/job, rationale/claim IDs, expected outcome (direction, no guarantee), cost/resource basis, dependencies, risks/guardrails, criteria to proceed/stop/revise, priority and next owner |
| Metric observation | native name, platform/surface/format/definition version, unit, numerator/denominator names and values or null, counting/replay/unique rules, data source/export timestamp, observation window, post age, cohort/traffic source/paid-organic/region/locale, coverage, missingness, uncertainty; derived formula separately |
| Experiment | ID, research question/hypothesis, baseline/source, variants, design type and assignment unit, implementation availability, primary/guardrail/quality metrics, MDE/power/sample plan or unavailable, window/stopping/analysis plan, confounds, consent/approval; execution state and result separately |
| Output | audience/positioning, opportunities, creative brief, release plan, experiment or insight artifact with actual locator/text, version, review scope and limitations; do not fill irrelevant modules |
| Feedback | prior recommendation/experiment and episode/version, expected vs observed, alternative explanations, keep/change/stop decision and authority, next evidence, affected owners/packets and stale dependencies |

Stable IDs survive reordering. On split/merge preserve retired IDs and old → new
mapping. Never merge scene, narrative beat, script beat, shot, cut, asset, post,
metric and experiment namespaces. A platform upload ID maps to a content variant,
which maps to an episode/cut version; it is not the episode itself. An export
update or definition change invalidates dependent calculations until rechecked.
Preserve original source labels/unknown fields in attachments; no lossy renaming.

## State and privacy

Keep artifact status (draft/reviewed/approved/superseded/blocked), evidence state
(absent/supplied-uninspected/inspected/measured), execution state
(planned/not-dispatched/running/returned/failed) and approval separate. Each
approval needs who, source, date, exact version and scope. Strategic selection,
creative approval, rights clearance and release authorization are distinct.
Do not manufacture dispatch, receipt or approval because a role is named.

Use authorized aggregate exports. Record intended use, minimum necessary fields,
storage/access/retention/deletion choices agreed with the user. Redact handles,
emails and sensitive comments in shared reports; small cells can identify people.
Do not infer sensitive attributes from viewing behavior or send private exports
to another tool/provider without appropriate authorization. If unavailable,
offer a minimal aggregate-data request and proceed in hypothesis mode.

## Ownership and safe local adapters

These are document mappings from contracts inspected 2026-11-26, **not** executed
handoffs. Re-read actual packets at use. No sibling path is needed at runtime.

| Owner/input | Preserve / Strategist exchange | Limit |
| --- | --- | --- |
| Director `director-packet/0.1`: upstream, locks, decisions, approval scope | versioned intent → audience evidence, positioning options, audience experience goal, measurable trade-off | Director selects final creative direction; strategy does not unlock a creative constraint |
| Storyteller: `story_id`, `version`, `canon_used`, deliverables, pending; narrative disclosure ledger | premise/genre promise, world vs character vs audience knowledge → opportunity/need brief and continuity implications | Storyteller develops premise/canon; don't present new lore as approved |
| Screenwriter: script/scene/beat ledger and timing basis | scene/beat versions → hook question, intended payoff, comprehension/pacing hypothesis | writer implements script; estimated duration is not measured retention |
| Artist: `assets[].id/version/path_or_result/canon`, checks | visual identity constraints → thumbnail/cover communication brief and truthful asset needs | Artist creates visuals; draft packaging does not authorize design changes |
| Cinematographer `cinematographer-shot-package/0.1`: scene/shots/proposed_sequence/checks | typed shot/scene links → platform readability/framing needs | camera/shot plan stays with Cinematographer |
| Sound Designer `sound-packet/0.1`: cut/cue/asset versions, rights, captions | language/locale/platform needs → dubbing/intelligibility/access brief | Sound Designer implements audio; licensing on one platform does not transfer automatically |
| Editor `editor-timeline/0.1` (appeared during this task): cut/sequence identity, typed beats, timing basis, lock/dependency/receipt/approval axes | preserve cut/version, upstream locks, record vs source time, actual media/export evidence; send audience outcome, variant requirements and test questions | late document-level inspection only; Editor owns timeline/export implementation and selective conform; no receiver acceptance or production verification implied |
| Critic `critic-review/0.1`: issue ID/artifact/revision/location/confidence/cause_status | located quality concern → research question, triangulation or experiment; return actual evidence | Critic independent review is separate from Strategist self-review and audience studies |
| Human channel owner | business priorities/resources/data access and release authority → proposals/results/approval request when needed | publishing requires human authorization for exact post/variant/platform/time; no new approval needed for writing a brief |

## Conflict, continuity and return loop

Record conflict as: locked goal/version → evidence strength → strategic benefit
and creative cost → alternatives (including retain intent) → authorized decision
owner. Do not let a high opportunity score override policy, rights, canon or user
requirements. Continue unaffected work while a consequential conflict is open.

For an episodic handoff include previous/next episode dependencies, spoiler limits,
entry-point context and payoff ledger ID/version. A recut or localized caption
that reveals a later twist goes back to Director/Storyteller and its implementer.
Receiver checks IDs/versions, understood outcome, constraints and feasibility;
receipt/implementation/acceptance remain unverified until observed. Link returned
post/export data to exact variant, evaluate only the measured window, then update
the strategy version with decisions and affected handoffs. This skill supplies
records, not a whole-studio orchestrator.
