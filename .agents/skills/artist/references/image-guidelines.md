# Raster generation, editing, and prompt specifications

Use the project's selected visual style and relevant character records. The
[Wayu Arts preset](style-guide.md) is the default for an unspecified new look.
For a pixel-art brief, use [pixel-style.md](pixel-style.md) instead of the
basic-style line/rendering defaults; state logical grid and pixel-scale intent.
Use the available image tool and follow its own input/output contract; this
skill does not require a particular provider or invent tool parameters.

## Deliverable and tool behavior

- For **prompt-only** requests, return the finished specification. Do not spend
  generation calls or describe the prompt as an image.
- For **generation**, pass the specification to an available image tool and
  return the actual result. If none is available, label the output spec-only,
  state the missing capability, and leave image review unperformed.
- For **editing**, inspect the actual source first. Attach it using the tool's
  documented reference mechanism; preserve identity, unaffected content, and
  existing transparency unless the brief changes them. For a small correction,
  prefer editing the good base rather than recreating the entire design.
- If a required source or identity reference is unavailable, request that input;
  do not invent a replacement and call it an identity-preserving edit.
- Attach identity/style/pose references with clear roles where supported. A file
  path in prompt prose alone does not attach an image. Record relevant versions
  and actual model/settings only when available; seeds do not guarantee identity.

## Output defaults

For a scoped edit, state the intended region/change and preserved content. Use a
mask/region or reference controls only if the actual tool supports them; do not
invent parameters. Compare the returned result with the source beyond the edited
region, including face, marks, handedness, crop and alpha. If correction keeps
damaging preserved areas, stop at the retry limit and identify a more controlled
next step. Do not deliver a full regeneration as a verified local edit.

For isolated illustrations, icons and stickers, default to transparent background,
one readable subject, clean edges/silhouette, generous padding and no accidental
cropping. Request high resolution (prefer at least 1024×1024 when supported).
For pixel art, distinguish this presentation/export size from the logical grid:
use [pixel-style.md](pixel-style.md)'s minimum 128×128 per asset/cell and its
256×256 character / 512×288 scene defaults. Do not override an exact native-size
request with a generic high-resolution export or call an upscale a larger grid.
For environments, scene illustrations and keyframes, keep the requested setting,
background, lighting and aspect ratio; do not strip scenery under cutout defaults.
Honor intentional bust/close-up crops while keeping the requested content in frame.

Use actual transparency controls when the tool supports them. Never call white or
checkerboard pixels a transparent background. Verify format, dimensions and alpha
when inspection tools are available; otherwise mark them unverified. A requested
PNG is not satisfied by renaming a JPEG or wrapping a different file format.

## Specification template

Use this section order for complete generation specifications. Add relevant
canon/reference IDs and change constraints; omit irrelevant details for a simple
edit rather than forcing a full form into every call.

```text
SUBJECT
POSE
EXPRESSION
CHARACTER DESIGN
OBJECTS
COMPOSITION
COLOR PALETTE
LINE STYLE
LIGHTING
BACKGROUND
OUTPUT REQUIREMENTS
```

- **SUBJECT:** who/what, purpose, and supplied character/scene/shot IDs.
- **POSE:** action/posture, gaze, held hand, and blocking constraints.
- **EXPRESSION:** intended emotion in the project's facial construction.
- **CHARACTER DESIGN:** identity locks, proportions, silhouette, costume version,
  skin/hair/eye colors, and approved identity references.
- **OBJECTS:** relevant props, scale/ownership, and persistent scene state.
- **COMPOSITION:** focal point, frame/crop, balance, depth, negative space, accent
  density, and any exact requested caption. Do not add unsolicited text.
- **COLOR PALETTE:** named swatches plus hex values when useful; generated colors
  are approximate and need inspection.
- **LINE STYLE:** project outline/rendering rules. For Wayu Arts explicitly request
  bold black/charcoal rounded outlines and simple dot or arc eyes in basic-style.
  For pixel-style use discrete pixel clusters, stepped edges and hard shade bands.
- **LIGHTING:** direction, quality, shadow/color logic, and emotional intent. For
  basic-style use soft/flat minimal shading unless the brief requests a variation;
  pixel-style uses the discrete shade bands specified in its own preset.
- **BACKGROUND:** actual requested scene, white, or transparent; preserve source
  alpha during edits unless changed. Avoid drop shadows for cutouts unless wanted.
- **OUTPUT REQUIREMENTS:** requested format, aspect ratio/size, alpha, margins,
  exclusions, exact allowed changes, and what must stay unchanged.

## Worked example — default Wayu Arts illustration

Request: "Create a programmer happily working."

```text
SUBJECT: Original cheerful chibi programmer illustration.
POSE: Sitting behind a generic laptop, hands typing, relaxed shoulders.
EXPRESSION: Closed smiling eye arcs, soft blush, content mood.
CHARACTER DESIGN: Oversized rounded head, small simplified body, rosy cheeks,
  soft dark hair, smooth rounded shapes. New one-off design, no identity source.
OBJECTS: Generic laptop, small coffee cup and potted plant; no logos.
COMPOSITION: Centered half-body view, clear hand silhouette, balanced negative
  space and small heart/spark accents; no caption requested.
COLOR PALETTE: Soft teal #7FCDBB, warm coral #F4978E, cream #FFF6E9,
  soft blue #A7D8F0; dark outline and hair.
LINE STYLE: Thick, clean black/charcoal outlines, rounded caps and joins.
LIGHTING: Soft and flat with minimal shading, no drop shadow.
BACKGROUND: Transparent.
OUTPUT REQUIREMENTS: PNG, request 1024×1024 or higher if supported, clean edges,
  generous margin, no accidental cropping or incidental text/brand marks.
```

For stock requests also read [stock-guidelines.md](stock-guidelines.md). Keep
requested caption wording; the Wayu Arts preset suggests brief 2–5 word captions
in a bubble/note/banner. Check actual spelling and glyphs. If reliable text is
essential, propose adding editable type separately rather than claiming the
image model will reproduce it exactly.

## Inspect the result

Check intent, identity, anatomy/hands, silhouette, expression, pose, composition,
palette/lighting, props, caption accuracy, background/alpha and technical output.
For related frames use [consistency.md](consistency.md). Correct observed defects
with targeted edits and report unresolved drift at the workflow's retry limit.

Use [review-rubric.md](review-rubric.md) to record actual evidence and prioritize
corrections. Verify file metadata separately from visual review. Alpha-channel
presence alone does not prove transparent pixels exist; inspect pixel extrema or
equivalent evidence for a cutout. Keep actual native sources/layers if produced;
a flattened generated PNG is not a layered production file. Retain real inputs,
tool settings and revision lineage as described in
[rights-accessibility.md](rights-accessibility.md). Do not claim exact swatches,
native-grid alignment, model consistency or print readiness from prompt text.
