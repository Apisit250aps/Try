# Wayu Arts — Pixel Style Preset

Use for explicit pixel-art, pixel character, sprite, tile or pixel-scene requests.
This is a rendering preset inside Artist, not another skill. Follow existing
project canon first; a style request does not authorize identity/story changes.

Read the [visual examples](../assets/pixel-style/README.md) and, when planning or
writing a brief, the [worked examples](pixel-examples.md). Keep
[basic-style references](../assets/basic-style/) separate: their smooth curves
and stroke treatment are not pixel rendering targets.

## Resolution policy

For this project, use **at least 128 logical pixels on each canvas dimension**
for new pixel assets. The general single-character default is **256×256**; a
landscape story frame defaults to **512×288**. This is a project convention for
readable, detailed pixel illustration, not a universal rule for all pixel art.
Do not select 32×32 or 64×64 as a default. A user-requested smaller asset or an
existing engine/project specification can override this convention; state the
exception instead of silently changing that contract.

Choose resolution from the intended detail and final use:

| Asset / use | Logical canvas | Why / limits | Example enlarged export |
| --- | --- | --- | --- |
| Simple prop, icon or compact portrait | 128×128 minimum | Distinct silhouette and simple material cues; do not cram complex faces/text into it. | 1024×1024 at 8× |
| Full-body character, ordinary default | 256×256 | Room for face, hands, layered costume and recognizable accessories. | 1024×1024 at 4× |
| Tall detailed character | 256×384 | Extra room for a long costume/pose while keeping a comparable character pixel scale. | 1024×1536 at 4× |
| Detailed face / expression cell | 128×128 minimum; prefer 256×256 when facial nuance matters | Size applies to each cell, not the entire sheet. | 512×512 per 128-cell at 4× |
| Compact square environment | 256×256 minimum | Readable location and one primary focal point; enlarge the logical canvas for dense architecture. | 1024×1024 at 4× |
| Story environment / keyframe, default | 512×288 (16:9) | Foreground, subject and background can carry purposeful detail. | 2048×1152 at 4× |
| Vertical scene | 288×512 (9:16) | Same scene detail budget with portrait framing. | 1152×2048 at 4× |
| Dense establishing scene | 768×432 or 1024×576 | Use only when needed for architecture/cast detail; keep pixel clusters visible and detail hierarchy controlled. | 1536×864 at 2× for 768×432 |

A larger canvas is not automatically better. If the subject still occupies a tiny
area, increasing export size adds no design detail. Make the face and hands large
enough for their intended expression/action; simplify the shot or increase logical
resolution when those features cannot be read. Do not fill empty space with noise.

### Native canvas versus export

- **Logical/native resolution** is the design grid on which pixel clusters are
  constructed. **Export resolution** is the saved image's actual width/height.
  Record both, plus the scale factor and whether the grid was verified.
- `128×128 → 1024×1024` is an 8× enlargement. It is still a 128-grid design.
  `256×256 → 1024×1024` is 4× and can hold more designed detail at the same export.
- Use integer nearest-neighbor enlargement for verified pixel sources. Do not
  stretch one axis, use bilinear/bicubic smoothing, or upscale a 64-grid sprite and
  describe it as a new 128-grid design.
- Image generators may return arbitrary dimensions and approximate pixel-like
  shapes. Ask for the intended logical grid, but do not claim exact grid, integer
  scale or palette compliance from the prompt alone. Record a target as a target;
  actual file dimensions do not establish a native grid.
- If exact pixel-aligned production files are required, inspect the native source
  and export. Use an available pixel editor/tool that can obey the grid, or report
  the missing capability. A visual-reference PNG does not complete that task.

### Sheets, frames and tile contracts

Apply the minimum to **each individual view, expression or frame**. For example,
a 2×2 expression sheet with 128×128 cells is at least 256×256 before gutters;
a 3×1 turnaround with 256×256 cells is at least 768×256 before gutters. State the
cell rectangle, row/column count, padding/gutters and frame order. Gutter space
does not count toward a cell's 128×128 drawing area.

Keep character scale, baseline, head/face construction, light and palette fixed
between cells. A back view must not introduce a different coat or hair length.
A 512×512 sheet can still fail if gutters reduce sixteen nominal 128×128 cells
below the required drawing-canvas size, or if each figure was copied from a much
smaller source. Intentional composition padding inside a valid cell is allowed.

For tileable/engine assets, use the actual tile/frame dimensions, edge behavior,
collision/anchor conventions and export contract supplied by the project. Do not
force the illustration default onto an existing tile map or invent animation
frames when only a style reference was requested.

## Rendering language

### Clusters, contours and anatomy

- Build shapes from deliberate connected square-pixel clusters. Curves use
  controlled stair-step runs with a consistent rhythm. Avoid random single-pixel
  speckles, stray outlines and disconnected highlight dots.
- Keep one coherent pixel scale for character, props and nearby environment.
  Do not combine tiny smooth facial detail with huge coarse body pixels.
- Use selective charcoal/colored outlines, typically 1–2 logical pixels for a
  256-grid character, adjusted to its silhouette. Larger export strokes are not
  additional logical pixels. Avoid thick smooth vector strokes and black halos.
- Preserve readable face, hands and object contact. Use pose/negative space to
  separate limbs and held props; do not rely on decorative texture to hide them.
- Chibi or realistic proportions are both valid when the brief calls for them.
  Preserve recurring-character ratios and anatomical sides from approved canon.

### Palette, light and materials

- Use cohesive palette families: teal, coral, cream, muted blue and charcoal are
  Wayu Arts starting points, not mandatory colors for every project.
- Palette planning targets: roughly 16–24 colors for a simple 128-grid prop,
  24–32 for a detailed character, and 32–48 for a layered scene. Reuse ramps across
  materials. These are planning budgets, not verified counts for generated PNGs.
- Shade with about 3 discrete value steps per character material and 3–4 where a
  complex scene needs it. Establish one key-light direction and readable contrast.
  Represent warm window light or atmosphere through hard-edged color clusters,
  not continuous glow, gradients or airbrush effects.
- Distinguish cloth, wood, metal and foliage using cluster shape, contrast and
  selective highlights. Do not add uniform grain/noise to every surface.
- Dithering is optional and intentional; avoid it as a replacement for clear
  color masses. No painterly texture, blur, glossy 3D or pixel-filtered photography.

### Composition and type

Use a focal point, intentional depth and controlled detail density. Group shapes
into foreground/middle/background for scenes; keep a complete silhouette and
padding for cutouts. Backgrounds follow the brief rather than automatic removal.
Do not add captions, UI, frame borders or checkerboard pixels. If text is required,
use the exact supplied wording and a suitable pixel font/grid; verify its glyphs
or propose a separate editable type layer.

## Production workflow and delivery

1. Identify asset type, intended use and canon; select logical dimensions from
   the table. Set per-cell dimensions separately for sheets.
2. Plan silhouette, face/hand size, cluster scale, palette ramps, material shade
   steps and light direction. Record reusable choices in the art bible.
3. Supply a brief containing the target logical size, aspect ratio, actual export
   requirement, references, identity locks, background, allowed changes and avoid
   list. Use the [worked briefs](pixel-examples.md) as examples, not mandatory prose.
4. Generate or construct using available tools. A prompt-only request stays
   prompt-only. Do not apply smoothing or infer that high-resolution output proves
   a compliant pixel grid.
5. Inspect actual output at native size and enlarged without smoothing. Correct
   observed issues within Artist's normal retry budget and preserve earlier versions.
6. Deliver the actual artifact, source/export dimensions, per-cell layout where
   relevant, palette/grid verification status, alpha status and unresolved drift.

Use [normal continuity rules](consistency.md) for face, hair, costume/prop IDs,
marks, handedness, location state and light. A style image is not an identity
reference. Use a shared pixel scale across frames rather than just matching their
export dimensions.

Deliver raster PNG and retain the actual editable pixel source when produced.
Verify the source grid and export separately; a flattened PNG is not an editable
pixel-project file.

## Acceptance checklist

| Check | Pass evidence / corrective action |
| --- | --- |
| Resolution | Logical canvas meets the chosen preset, each sheet cell meets its own minimum, or a documented project override exists. Unverified generated targets stay labeled unverified. |
| Native/export distinction | Actual image dimensions are recorded separately; any claimed integer scaling is verified. No low-grid upscale is relabeled as higher-grid art. |
| Pixel treatment | Deliberate stepped contours, coherent cluster scale, no softened edges or stray/noisy pixels. Inspect at normal and enlarged size. |
| Detail/readability | Face, expression, hands, clothing layers and held props read at intended display size; focal point survives thumbnail viewing. |
| Palette/materials | Shared color ramps, clear shade bands, consistent light; actual palette count is claimed only when measured. |
| Identity/scene | Face/hair/proportions, marks, costume, handedness and persistent scene state match canon. |
| Technical output | Correct format, dimensions, alpha/background, crop and sheet layout; tileability/animation are checked only when requested. |

The [included PNGs](../assets/pixel-style/README.md) are generated visual references,
not certified native-grid sprites, indexed-palette sheets or tileable textures.
Use the guide as production acceptance criteria and report any output that falls
short; do not promote generated examples into exact technical standards.
