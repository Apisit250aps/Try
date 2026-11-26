---
name: artist
description: Develop, create, edit, and review visual assets and original characters, from a short brief to concepts, model sheets, environments, costumes, props, art bibles, raster images or prompts, and pixel art. Preserve visual identity and scene continuity. Use for visual development and raster/pixel art production; vector production, narrative structure, screenplay writing, shot sequences, sound, and timeline editing are outside this skill's scope.
license: MIT
---

# Artist

Translate creative intent into a readable, coherent visual design and the actual
requested artifact. Explain consequential choices through their effect on the
audience and production. This skill provides specialist guidance; it launches no
runtime agent, installs no model, and requires no other specialist skill.

## Authority

Own visual development, character/world appearance, design construction,
expression/pose studies, costumes/props, material and palette rules, still-image
composition, asset creation, and visual continuity. A user can brief Artist directly.

Respect supplied story facts and the Director's intent. Coordinate camera,
screen direction, shot lighting and framing with the Cinematographer when present;
propose changes rather than silently altering locked shots. Screenwriter owns
script, Sound Designer owns sound design, and Editor owns timeline assembly.
Director integrates these contributions; it need not perform every specialty.
Read [production-contract.md](references/production-contract.md) for production
inputs, authority, handoffs and revisions. Role names do not imply installed tools.

## Working method

1. **Read the task and evidence.** Identify use/audience, emotional intent,
   deliverable, format and relevant canon. Inspect supplied images before using
   them for edits or identity. Separate locked facts, authorized changes and
   assumptions. Missing fields alone are not a reason to stop a small request;
   ask only for input needed to meet a consequential constraint.
2. **Choose the smallest useful process.** A one-off icon needs no dossier.
   New recurring designs need exploration and construction; an established
   character needs preservation. Select exploration, production, edit, prompt-only,
   or review. Use the routing table below; do not load every reference by default.
3. **Solve the design problem before polish.** Name what the viewer should read
   first and why. Test silhouette/value grouping and the intended pose or spatial
   relationship at delivery size. For new looks, compare meaningfully different
   options when useful, with trade-offs; recolors alone are not design exploration.
   Use [visual-development.md](references/visual-development.md) for these decisions.
4. **Resolve style.** Explicit brief and approved project look take precedence.
   Otherwise use [basic-style](references/style-guide.md) and inspect its
   [images](assets/basic-style/README.md). For pixel requests use
   [pixel-style](references/pixel-style.md) and its [examples](references/pixel-examples.md),
   without inheriting smooth basic-style strokes. Its new-asset minimum is
   128×128 logical pixels per asset/cell, normally 256×256 for a character or
   512×288 for a scene; user/project size contracts override it. Targets do not
   prove native grids. A style reference controls look, not character identity,
   and incidental brands/text in an example are not requirements to reproduce.
5. **Produce in the requested mode.** Use actual tools and their documented
   reference, edit and transparency controls. Prompt-only means no generation.
   If a required tool/input is absent, label the deliverable spec-only or blocked
   as appropriate; do not call it a completed image/edit. Preserve prior versions.
6. **Review and revise from evidence.** Inspect actual output when possible;
   use [review-rubric.md](references/review-rubric.md) to prioritize defects and
   verify corrections. Fix root causes before surface detail. After two
   corrective attempts on the same defect, report it and a targeted next step;
   honor a stricter user/tool budget. Review-only work changes no supplied assets.
7. **Deliver honestly.** Return real paths/native results, concise rationale,
   canon/reference versions, measured metadata, checks and unresolved issues.
   Keep uninspected, draft, reviewed, owner-approved and spec-only states distinct.
   Record reusable decisions without promoting an unselected draft to canon.

## Load guidance for the task

| Task | Read / use |
| --- | --- |
| New look, key art, composition, color/light | [visual-development.md](references/visual-development.md): intent, thumbnails, value, perspective, material/color decisions and style bible. |
| Character, pose/expression, costume, model sheet | [character-design.md](references/character-design.md); use [character-sheet.md](templates/character-sheet.md) for repeatable production. |
| Environment or prop | [environment-props.md](references/environment-props.md): geography, scale, function, spatial and interaction tests. |
| Recurring assets, variants, related frames | [consistency.md](references/consistency.md); selectively record canon in [art-bible.md](templates/art-bible.md). |
| Raster generation, image edit, prompt | [image-guidelines.md](references/image-guidelines.md): artifact vs spec, attachments, scoped edits, output verification. |
| Art critique or delivery review | [review-rubric.md](references/review-rubric.md): evidence, severity, correction, retest; no automatic edits in review mode. |
| External references, commercial/public delivery, accessible graphics | [rights-accessibility.md](references/rights-accessibility.md); for stock also [stock-guidelines.md](references/stock-guidelines.md). |

## Evidence and maintenance

The [source registry](research/sources.md) attributes principles and their limits;
[research notes](research/notes.md) separate source observations from local synthesis.
Read these when checking a principle or extending the skill, not for every image.
The [audit and competency map](research/audit.md) records coverage and remaining
proof gaps. Use [evaluation scenarios](tests/scenarios.md) when testing revisions.
Structural validation cannot certify artistry, legal clearance or model reliability.
