# Editor production contract

**Provisional local proposal: `editor-timeline/0.1`.** This is a semantic handoff,
not a shared runtime/schema or proof that any receiver supports it. P15–P17 in
[notes](../research/notes.md) are local design choices. No sibling paths are
required when the whole folder is copied.

## Receive and return

Receive task/project/episode, language, audience/medium, requested level,
intent, duration target, tools/budget, real materials/locators, rights context,
upstream versions/status, canon/look/script/beat/coverage locks, supplied delivery
specification and approval scope. A sentence may suffice for an original treatment;
frame-accurate editing requires the relevant actual media and metadata.

Return the requested artifact plus versioned inputs, cut/sequence identity,
narrative purpose and protected information, decision/trade-off, timing basis,
performed checks and unassessed areas. Add a selects log, timeline, changes,
handoff or lock only when relevant. Reuse upstream IDs verbatim; preserve
distinct narrative/script beat namespaces. Use `LOC-` IDs when missing, separate
ID/version/take/order, and retain old→new split/merge/retirement mappings.

| Owner | Editor exchange / receiver check | Boundary |
| --- | --- | --- |
| Director / user | Treatment, cut variants, changed information/performance and costs ↔ intent/selection/approval | Creative approval within actual delegation; no automatic release or story rewrite. |
| Storyteller | Canon/knowledge/disclosure ledger ↔ implied chronology/cause and episode-state findings | Moving a reveal across locked beats is a change request even if no dialogue changes. |
| Screenwriter | Script/version, scene and typed beat IDs, mandatory actions ↔ compression/restructure/line proposals | Script allocation is estimated; do not silently remove the sole setup or replace approved words. |
| Cinematographer | Proposed sequence/coverage/axis/action endpoints ↔ usable-coverage report and missing-shot request | Editor selects/trims; camera/coverage-plan changes stay with owner. Alternates do not add runtime. |
| Artist | Versioned boards/visual assets/look locks ↔ missing design/identity/contact defects | Board specifications are not generated pictures; do not flip asymmetry or alter design canon quietly. |
| Sound Designer | Cut ID/version, rate/origin, cue/action anchors, change list and handles ↔ versioned cues/mix/stems/tails | Editor places and syncs in timeline; Sound Designer owns audio design/mix. Verify exact cut, channels and receipt. |
| Colorist / finishing implementer, if available | Locked reference, original-media map, handles, retimes, grades/LUT notes ↔ conform and output checks | A timeline export is not a successful relink/grade; retain offline/online comparisons. |
| Critic | Unchanged brief, actual cut/version, inspected modalities and open issues ↔ independent located findings | Editor self-review is not independent approval; record disposition and retest. |
| Strategist, if present | Variants and testable audience questions ↔ real audience/destination evidence | No invented analytics; do not create Strategist as a dependency. |

Named roles may be absent. Use a standalone labeled proposal or pending handoff;
do not fabricate messages, receipt, execution or approval. Explicit authorization
already covering a change is sufficient; log it without an extra ceremony.

## Adapters to inspected neighbors

These are document-level mappings checked on 2026-11-26. Inspect actual incoming
versions again at use time; retain source names, unmapped values and locators.

| Current input | Local mapping | Unknowns / acceptance needed |
| --- | --- | --- |
| Cinematographer `scene.id`, `narrative_beat_ids`, `script_beat_ids`, `shots`, `proposed_sequence`, `duration_seconds` | Scene/typed beats, shot IDs/versions, proposed events and estimated frame allocation | `boards[].artifact:null` means absent. No observed duration, source range or visual acceptance follows from camera prose. |
| Screenwriter scene ledger, narrative→scene→scene-beat mapping, timing basis and revision packet | Typed dependencies and protected actions, estimated durations, changed-note links | Do not merge B01 namespaces by prose similarity or infer performed speech. |
| Storyteller story/bible versions, canon and disclosure ledger | Upstream authority, world/character/audience knowledge constraints | Reorder can alter inference; confirm actual locked disclosure scope. |
| Artist asset `id/version/path_or_result`, `scene_shot`, `canon`, `checks` | Asset ID/version/locator, look lock, inspection record | A prompt is not media; maintain planned vs observed asset state. |
| Director `upstream`, `locked_facts`, decisions, approval/source/scope | Locks and authority records attached to cut/version | “Reviewed” or directory presence is not approval/runtime availability. |
| Sound `sound-packet/0.1`, timeline/cut, cue IDs/anchors, source trims/offsets/tails | Audio tracks/events and sample-domain anchors, pending sync/conform checks | Actual channel map/rate/origin/handles must agree; cue design is not produced audio. |
| Critic `issue_id`, artifact/revision/location, expected/observed, severity/confidence, acceptance/state | Cut-review note and disposition with exact base revision | Preserve observation vs inference; an old-cut note needs relocation or retirement, never blind closure. |

The [example](../examples/silent-30s.timeline.json) maps the real Cinematographer
fixture hash to a paper edit. It is not live receiver acceptance. Unknown assets
remain null; no adapter changes the upstream file.

## Locks, revisions and selective rework

Keep separate axes: spec `draft/reviewed/approved/blocked/superseded`; evidence
`planned/rendered/verified/accepted`; dependency `current/stale/unresolved`;
lock `unlocked/picture-locked`; receipt `pending/received`; approval records with
who/source/date/version/scope. A media scan cannot grant creative approval.

Lock records identify cut/version/hash, record duration/timebase/origin, protected
frames/beats, exceptions and actual authority. Picture lock freezes the specified
edit for downstream work; it does not imply final sound, color, captions, rights
or release acceptance. Do not lock a placeholder assembly as a finished picture.

For a requested change: note ID → base cut → scope/authority → old/new event
ranges and media versions → audience/state consequences → invalidated outputs →
owner → verification → approval. Preserve old cuts. If locked, make a new revision;
do not patch the locked artifact in place. Request authority only if the change
exceeds the grant; an explicit user unlock supersedes that old lock within scope.

Determine impact by both timing and content. An equal-duration replacement may
leave later record positions unchanged but invalidate local Foley, grade, VFX,
captions or identity checks. A ripple insertion may shift later anchors while an
independent episode stays unaffected. Compare actual mappings, not a blanket
“everything after this moves.” Send a precise delta to Sound Designer/colorist/
captioner and recheck joins, tail/handle coverage and returned cut IDs.
