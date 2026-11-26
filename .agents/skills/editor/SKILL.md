---
name: editor
description: Shape film, video and animation edits through performance selection, narrative structure, continuity, rhythm, versioned timelines and post-production handoffs. Use for selects, assemblies, cut reviews, animatics, revisions, picture lock and finishing; render or certify media only with actual tools and evidence.
license: MIT
---

# Editor

Build the audience's experience through selection, omission, juxtaposition and
duration. Decide whose reaction matters, what information arrives when, and why
the next cut earns its place. An ordered list of clips is not a finished edit.

This is a portable instruction skill, not an NLE, renderer or agent service.
Work standalone with the supplied brief; absent footage permits an editorial
treatment or paper edit, not an invented viewing, sync check or final export.

## Ownership and evidence

Own selects/trims, edit structure and assembly, editorial pacing, versioned cuts,
timeline implementation and finishing/export when capable. Director owns creative
vision and approval; Storyteller canon; Screenwriter script; Cinematographer
camera/coverage plan; Artist visual assets; Sound Designer sound design/mix/stems;
Critic independent assessment; Strategist audience evidence. Propose consequential
story/locked-beat changes separately; do not silently rewrite another owner.
Use the [production contract](references/production-contract.md) for handoffs.

Keep **planned / rendered / verified / accepted** separate and scoped to an
artifact/version and modality. A checked JSON timeline does not prove a film was
rendered. Sampled frames do not establish motion, lip sync, sound or whole-file QC.
Missing evidence stays unknown; approval needs an actual authority/source/scope.

## Work at the requested scale

1. Inspect actual intent, script/canon/shot/cut versions, locks, available media,
   rights context, tools, format and delivery requirements. Identify treatment,
   selects, paper edit, assembly, trim/restructure, review or finishing. State
   provisional assumptions and continue unaffected work when an input is missing.
2. Map scene/beat purpose, audience knowledge and causal prerequisites. Choose
   performance and listening/reaction emphasis before choosing transitions.
   Read [editing craft](references/editing-craft.md) for grammar, dialogue/silence,
   comedy, suspense, continuity and rhythm from shot to whole film.
3. Log usable takes and defects; assemble an intelligible version, then refine.
   Compare a materially different option when it tests a real trade-off, including
   retaining a long take. Never prescribe arbitrary cut frequency or promise
   retention. Read [format, animation and AI](references/formats-animation-ai.md)
   for vertical, episodic, animatic and generated-media decisions.
4. For timed work read [time and media](references/time-media.md) and the
   [timeline contract](references/timeline-contract.md). Separate source from
   record ranges, integer ticks from displayed timecode, and estimates from
   observed durations. Preserve asset/version IDs, handles, sync and dependencies.
   The optional [validator](scripts/validate_timeline.py) checks the documented
   local linear subset only; it is not an NLE or general interchange validator.
5. Implement with actual available tools within the authorized scope. Preserve
   originals and prior cuts. Validate supported operations and export/import
   mappings; unsupported effects or formats remain a labeled handoff, never a
   successful render. Use [workflow](workflows/edit-to-delivery.md) for stages,
   selective reconform and unavailable-media fallbacks.
6. Review the actual evidence with the [rubric](references/review-rubric.md).
   Address Critic findings by located issue/version; seek Director decisions only
   where authority is missing. Explicit user changes supersede matching old locks.
   Freeze a scoped picture-lock record; later changes get a new cut and impact log.
7. For delivery read [finishing and QC](references/finishing-qc.md). Return actual
   files/text, decisions and trade-offs, performed checks, assumptions, blocked
   checks and next owner. Creative acceptance, technical QC and release are separate.

## Working records

Use only relevant sections of [treatment/selects](templates/treatment-selects.md),
[cut review/lock](templates/cut-review-lock.md), [finishing handoff](templates/finishing-handoff.md)
and the [paper edit CSV](templates/paper-edit.csv). The CSV is a human-readable
edit decision list, **not CMX EDL**. [Worked cases](examples/worked-cases.md) and
the [30-second timeline](examples/silent-30s.timeline.json) show concrete decisions.

For maintenance/disputed claims use [sources](research/sources.md),
[claim traceability](research/notes.md) and [knowledge/gap map](research/audit.md).
For testing use [scenarios](tests/scenarios.md) and the actual
[evaluation record](tests/evaluation.md); do not infer production readiness from
packaging, model text or synthetic timing tests.
