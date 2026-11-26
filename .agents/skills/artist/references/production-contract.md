# Artist production contract and specialist handoffs

Use these fields as a working contract, not a form the user must fill out.
Extract what is already known; omit irrelevant fields for small requests.

## Creative brief input

| Field | Meaning |
| --- | --- |
| Task / project | Project ID, task ID, intended use and audience when relevant. |
| Deliverable | Character concept, reference sheet, environment, prop, costume, keyframe, raster, edit, prompt, or review; count and destination. |
| Narrative intent | What the frame must communicate, emotional tone, action and world constraints. Keep supplied scene/shot IDs and sequence context. |
| Canon | Existing art bible version, character IDs/versions, costume/prop/location IDs, approved reference paths and their roles. |
| Change scope | What may change and what must remain fixed; whether the task requests a new design, variation, or canon revision. |
| Technical constraints | Format, size/aspect ratio, transparency/background, framing/crop, text, editability, target tool, and any generation budget. For pixel art distinguish logical canvas/per-cell drawing size from export dimensions and grid verification status. |
| Use and provenance | Publishing/display context, reference roles and source-use constraints; any accessibility or credit requirements material to this use. |
| Acceptance | Specific visual and continuity checks; who selects or approves new canon. |

Missing fields do not automatically block production. A short "happy programmer
PNG" request is enough to make a one-off asset with the default preset. A request
to preserve an existing character's identity needs the actual reference or a
sufficient character record. If it is missing, ask for it and offer a draft
concept/spec without pretending the identity has been matched.

## Decision authority

| Area | Collaborator / owner (or user) | Artist |
| --- | --- | --- |
| Narrative | Storyteller develops narrative/world/arc; Screenwriter develops screenplay; Director integrates intent. | Expresses supplied facts through appearance, pose, expression, color and light. |
| Visual identity | Selects the project look and approves changes to established canon. | Explores/develops the look, defines visual rules, records and checks continuity. |
| Camera / scene | Cinematographer develops camera/framing, screen direction and shot-lighting plan with Director; Director resolves narrative trade-offs. | Develops visual keys, material/light rules and composition within supplied shot constraints; proposes changes with their impact. |
| Character | Owns story facts, relationships and development. | Owns appearance, proportion, visual personality, costume and expression design within those facts. |
| Production | Editor owns timeline/assembly; Sound Designer owns sound assets/design; Director integrates performance and sequence intent. | Supplies visual assets, reference sheets, technical metadata and art review. |
| Assessment / positioning | Critic independently assesses the brief and work; Strategist develops audience/distribution goals. | Self-reviews visual craft and supplies evidence; does not invent audience evidence, override canon or claim independent critique of its own work. |

The Director is a collaborator role, not a dependency on another installed skill.
Do not invent a Director API, agent launcher, approval endpoint, or file location.
These are project interfaces; a named role may be unavailable in a particular
host. They are not claims that its skill is installed or a universal account of
studio job boundaries.

## Handoff and return

Send the next maker the smallest usable packet: intent, selected/draft distinction,
IDs/versions, actual artifacts, visual rules, scale/material/scene state and
unresolved decisions. Cinematographer needs layout landmarks, light sources and
occlusion limits; Director needs visual alternatives and their narrative effect.
Ask the receiver to identify missing production information rather than filling
it with unapproved canon. An ordinary still needs no cross-role ceremony.

For returned notes, identify affected asset/view, requested outcome, locked facts
and acceptance test. Separate a defect fix from an authorized design revision.
Check downstream sheets/frames that share the changed design. Keep earlier files;
record which revision supersedes which, and what needs re-review. Follow
[continuity](consistency.md) and the [review rubric](review-rubric.md).

## Handling conflicts and revisions

- Explicit task instructions define the requested change. If they revise a
  locked design, acknowledge the revision and create a new version; keep the old
  version available. Do not repeatedly ask for permission already given.
- When a new request conflicts with existing canon without clearly authorizing
  a revision, flag the exact conflict and ask a focused question; proceed with
  unaffected work. Keep explorations provisional until the owner selects them.
- When canon documents and approved images disagree, identify the conflicting
  versions; do not silently choose a new identity from them.
- Scene state (wet coat, held prop, injury, time of day) can vary without changing
  permanent identity. Record the state and preserve continuity across related
  frames unless the brief calls for a transition.

## Delivery contract

For production work, provide a compact handoff with:

```yaml
task_id: project task ID, if supplied
status: draft | reviewed | approved | blocked | spec-only
assets:
  - id: stable asset ID
    version: revision identifier
    path_or_result: real file path or native tool result reference
    format: actual format, dimensions and alpha status when verified
    scene_shot: supplied scene/shot ID, if applicable
    canon: art bible and character versions used
    references: actual input paths/results and their roles
    source_and_export: editable/native source if produced; output profile/layers if known
    provenance: source-use evidence, real tool/settings when exposed; unknowns explicit
checks: what was inspected or validated, with any failures
changes: new decisions, affected assets, and proposed/authorized canon updates
open_issues: limitations, missing capability, or owner decision needed
next_owner: intended receiver and any concrete request, when coordinating
```

Use prose instead of YAML when clearer; these are information fields, not an API
schema. Omit unknown technical metadata instead of inventing values. For a
spec-only result, return the spec as text or a real saved file and leave image
metadata unset. "Reviewed" means Artist checked the stated items; "approved"
requires an explicit owner decision or an existing recorded approval. A usable
draft can be delivered without adding an approval gate to an ordinary request.
