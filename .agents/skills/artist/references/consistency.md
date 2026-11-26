# Visual and character continuity

## Establish the source of truth

Read the project's current art bible, relevant character sheets and approved
images. Keep the project's existing names/IDs and storage conventions. If there
is no bible, use the templates to capture only decisions that must survive
future tasks. A new design stays a draft until selected by the user/Director;
do not turn an attractive generation into canon without that decision.

For basic-style work, the [style preset](style-guide.md) and
[example images](../assets/basic-style/) define the collection's look. These
are style references, not recurring character identity references. Another
project can use a different approved look without inheriting chibi proportions,
pastel colors, or cheerful expression requirements.

For pixel art, use [pixel-style.md](pixel-style.md) and its
[examples](../assets/pixel-style/). Lock the logical canvas, pixel scale,
palette, outline-cluster width and shade steps across related assets; do not
mix smooth basic-style rendering into the same pixel collection.

## Character design and reference sheets

For construction, anatomy/stylization, costume and cross-view tests read
[character-design.md](character-design.md). This file owns the version/state
record; avoid maintaining a competing character specification elsewhere.

Translate supplied role/personality into readable shape language, posture,
silhouette and costume rather than adding new biography. Make characters in the
same cast distinguishable at thumbnail size. Record:

- Stable character ID, design version, and approval source/status.
- Identity locks: face shape, head/body and limb proportions, skin/fur tone,
  eye shape/color, hair silhouette and color, distinctive marks and their side,
  recognizable accessories, and relative height/scale against other characters.
- Palette/material swatches, costume variant IDs, and prop ownership/scale.
- Allowed changes: pose, expression, gaze and approved costumes; scene-specific
  state such as dirt, wetness, held objects, injury or age variant.
- Reference image paths, view labels, and what each reference controls.

For a reference sheet, choose views that production actually needs: front,
three-quarter, profile, back, facial close-up, key expressions or action poses.
Keep neutral lighting, scale, proportions, costume and distinguishing marks
consistent between views. Name profile sides and mark asymmetric features so a
mirrored view does not move them. An expression sheet must change facial action
without changing the face's construction. A written sheet alone does not prove
the generator can maintain identity across views.

## Project look and scene continuity

The art bible records palette and outline/rendering rules, proportion ranges,
shape/material language, detail level, lighting logic, environment geography,
scale relationships, framing conventions, caption treatment and exclusions.

For each related scene/frame, track only the state that matters:

- Character and costume/prop/location versions in use.
- Time, weather, light direction/color, and persistent environment landmarks.
- Pose, gaze and screen direction under the Director's blocking constraints.
- Which hand holds a prop, wear/damage, and any planned state transition.

Do not confuse a dark lighting pass with a new base costume color. Do not add a
new scar or accessory as decoration if it changes an established identity.

## Reusing references during production

Supply approved identity images to the image tool using its documented reference
mechanism; a path mentioned in a prompt is not necessarily an attached image.
Inspect references before editing and preserve transparency unless the brief
changes it. Use references by role: identity, style, pose, composition, costume.
Do not copy another image's character just because it is a style reference.

Repeat concise identity locks and the authorized changes in each prompt, with
versioned source paths in the handoff. Use the same tool/model settings and seed
when available and useful, but do not invent unsupported controls or claim a seed
guarantees identity. Prefer a targeted edit of a good base image for a small
change over regenerating the entire design.

## Review and correction

Compare actual output against approved references side by side where possible:

| Check | Failure example | Correction |
| --- | --- | --- |
| Identity | Face shape changes between front and profile. | Reuse approved face/reference and correct that view. |
| Proportions | Head or relative height drifts. | Restate ratios and scale anchors; adjust affected geometry/image. |
| Asymmetry | Left-cheek mark appears on the right. | Specify character's anatomical left; fix the mirrored detail. |
| Costume/prop | Pocket, sleeve color or held hand changes. | Restore the relevant variant and scene state. |
| Rendering | Thick outline becomes thin, flat art becomes glossy. | Reapply project line/material/light rules. |
| Scene | Light direction or landmark moves without a transition. | Restore established location/lighting and flag conflicting brief. |
| Delivery | White or checkerboard pixels are described as alpha. | Verify actual transparency or label it unverified. |

Record pass/fail/not-inspected and remaining drift. Correct the affected asset
and identify other assets that need the same revision; do not silently rewrite
the reference to fit a failure. Keep previous versions and record what changed.
Stop repeated correction at the retry limit in the main workflow and deliver an
honest review state. Prompt constraints reduce drift; they do not prove a match.

For a design revision, trace dependencies before handing off: character model
sheet → costume/prop attachments → scene assets/keyframes using that version.
Record which are updated, still valid or pending review. A new scene state does
not automatically require revising the neutral model sheet. Use the
[review rubric](review-rubric.md) for defect severity and acceptance evidence.
