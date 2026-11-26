# Pixel Style — Worked Briefs

Read [pixel-style.md](pixel-style.md) for resolution and rendering requirements.
These are adaptable brief examples. They are not additional generated artifacts;
actual images and provenance live in the [example gallery](../assets/pixel-style/README.md).
An explicit existing project contract can override the default resolution policy.

## 1. Simple prop — minimum 128×128

**Request:** "A pixel-art field notebook icon, readable and reusable."

- Logical canvas: 128×128; optional 4× export at 512×512 or 8× at 1024×1024.
- Subject: closed teal notebook with coral elastic band and a cream leaf emblem.
- Composition: three-quarter view, object large enough to show cover/spine,
  comfortable padding; transparent background when actually generated as a cutout.
- Rendering: intentional 1-pixel contour clusters, 16–24-color planning budget,
  3 hard shade steps; light from upper left, no smooth gradient or drop shadow.
- Review: cover/spine geometry, clear silhouette, no incidental text, actual alpha.
- Deliver: native/editable source if available plus PNG export; label any
  generator-only logical-grid target unverified.

Do not create a 32×32 icon and enlarge it four times to claim a 128-grid design.

## 2. Detailed full-body character — default 256×256

**Request:** "An original botanical explorer, pixel style with visible costume detail."

- Logical canvas: 256×256, desired export 1024×1024 at 4× from a verified source.
- Subject: friendly explorer, auburn bob, sage-teal jacket, cream shirt, plum
  trousers, tan boots, coral satchel and a field notebook.
- Framing: full body, face/hands readable, separated silhouette and padded edges.
- Rendering: fine consistent pixel clusters, selective 1–2-pixel contours,
  24–32-color planning budget and 3 discrete shades per material.
- Materials: layered fabric, leather satchel straps and a small metal buckle
  expressed with different cluster shapes; avoid uniform grain.
- Canon: a new draft design; do not silently replace an established character.
- Review: hands actually contact the notebook, eyes/hair construction stay coherent,
  boots/feet fit the frame, light direction and pixel scale are consistent.

For a tall coat/pose that needs more room, use 256×384 rather than shrinking the
figure until its face loses detail.

## 3. Expression sheet — at least 128×128 per cell

**Request:** "Neutral, happy, focused and surprised expressions for the same character."

- Layout: 2×2; 128×128 drawing cells minimum, total 256×256 before gutters.
  Prefer 256×256 cells / 512×512 total when finer facial nuance is necessary.
- Repeat the same head scale, angle, hair silhouette, eye construction, costume
  collar, light and palette in all cells. Change brows, eyes and mouth only as
  required by each expression.
- Lock the source character ID/version and anatomical side of any mark or hair
  clip. Attach the actual approved identity image when the tool supports it.
- Use a plain backdrop; separate cells with negative space, not invented UI/text.
- Review each face independently and compare against the source and other cells.
  Label drift rather than claiming the sheet proves consistent identity.
- Deliver: actual sheet layout/cell dimensions and review status. Do not infer cell
  source resolution merely by dividing a generated image's width by two.

For the bundled [expression illustration](../assets/pixel-style/expression-sheet-example.png),
the logical cell sizes are generation targets until verified, not native-source metadata.

## 4. Character turnaround — 256×256 per view

**Request:** "Front, profile and back references for approved explorer C01 v2."

- Layout: 3×1, cells 256×256, total 768×256 before gutters; a 2× enlarged export
  would be 1536×512 before scaled gutters if the native sheet is verified.
- Source: approved C01 v2 face, proportions, hair, jacket J1, satchel P1; do not
  invent a new biography or redesign the character to fill a missing back view.
- Keep baseline, relative height, head/body ratio, costume seams/material colors
  and neutral lighting stable. Name the profile side in the delivery record.
- Maintain anatomical side for asymmetrical straps/marks even when their apparent
  screen position changes. Distinguish planned hidden detail from approved canon.
- Review scale/alignment, accessory placement and head/face identity across views.
- Deliver a draft for unresolved design decisions; do not mark an unselected back
  design as approved. This is a written workflow example, not a supplied image sheet.

## 5. Detailed environment — default 512×288

**Request:** "A peaceful canal-side bookshop in warm afternoon light, 16:9 pixel art."

- Logical canvas: 512×288; a verified 4× export is 2048×1152.
- Focal point: teal/cream timber bookshop with coral awning, warm windows, visible
  book masses and one parked bicycle. No readable shop signage unless requested.
- Depth: stone walkway in foreground, shop in middle ground, canal/bridge and
  trees in background. Keep perspective, walkway/door scale and light direction
  coherent; no need to add story characters.
- Rendering: 32–48-color planning budget, 3–4 hard shade bands per material,
  deliberate roof/wood/stone clusters; reduce detail in the distant background.
- Review: focal hierarchy, bicycle/architecture readability, clean contours,
  no smooth atmospheric gradients, no noisy leaf texture or accidental writing.

For a simpler square location vignette, 256×256 is a useful starting point. For a
dense establishing scene use 768×432/1024×576 only when that extra design detail
is actually needed; avoid turning the larger grid into smooth painting.

## 6. Two related keyframes — preserve pixel density and Director intent

**Request:** "Shots A then B in the same station; Mali waits, then looks at a train."

- Both logical canvases: 512×288, with the same pixel scale, palette and light.
- Canon: Mali v1, short black bob, brown eyes, left-cheek mark, teal coat C1;
  brass key stays in her anatomical right hand. Reuse approved identity references.
- A: supplied waiting pose. B: only the gaze change and arriving train specified
  by the Director. Preserve platform landmarks, outfit and prop state.
- Do not rewrite shot order, durations, motivation, camera movement or dialogue.
  Mark any proposed visual rearrangement as a proposal.
- Check A/B side by side for identity, outline scale, clothing colors, handedness,
  environment scale and lighting drift. Matching export size alone is insufficient.
- Deliver two real images when generation is requested, or two labeled specs for
  a prompt-only request; report unverified grid/visual checks accurately.
