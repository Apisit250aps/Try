# Animation, previs and AI video

Read for medium-aware shot design, board/frame handoff and generation revision.
Use the [contract](production-contract.md) for IDs/states and
[rubric](review-rubric.md) for acceptance. Claims resolve in
[notes](../research/notes.md).

## Animation and layout

Disney's public layout account connects camera, staging and rough performance
with neighboring shots; final layout returns to framing/focus and continuity
after animation. This is evidence for iteration, not a demand for its studio
pipeline or permission to change The Stories canon. [P18: C]

Design a shot in the actual medium. In 3D, specify gate/FOV, scale, camera path,
focus and lighting coordinates where useful. In 2D/cutout, plan perspective layers,
overlap, transforms and required redraws; a pan across a flat background is not a
3D dolly. For pixel animation, preserve the approved logical grid/rendering policy:
interpolated zooms, subpixel camera motion, DOF or blur can destroy cluster clarity.
Ask Artist for missing turnaround/prop faces rather than inventing a new design
behind an orbit. For stop motion, test repeatability and focus through small
increments; don't assume a virtual move is physically available. [H]

Boards describe composition, acting keys and transitions. Previs tests spatial
and motion relationships; an animatic tests proposed timing with images/audio.
Give Artist panel IDs under shot IDs, viewpoint, subject silhouettes/placement,
layer order, light direction, asset/version locks and camera/subject arrows with
different labels. Include an intermediate panel when endpoints conceal a risky
crossing, occlusion or hand contact. A textual panel spec is not drawn artwork.
Give Editor proposed duration ranges, critical reads, optional trims and handles;
use Sound Designer early when a cue motivates a look/reveal. [P16/P17: C; H]

## Keep shot design separate from the provider adapter

The design packet states desired observations. The adapter records actual
provider/model/version, supported durations/ratios, image roles, reference limit,
start/end support, camera controls, prompt/negative syntax, audio support and
budget. Check current official docs and available tool schema before execution.
Unsupported controls remain desired conditions, not invented API parameters.
Never claim literal millimeters, keyframes or an end pose are enforced merely
because they appear in prompt text. [S03]

Runway's Gen-4 guide recommends simple motion descriptions and incremental
iteration; its negative-prompt advice is model-specific. Google's frame/reference
documentation demonstrates that endpoint frames and subject references are
different capabilities with model-specific support. Neither proves exact
continuity for this skill. [P19/P20/P21: technical documentation]

## A feasible shot unit

Record these before prompt translation (H/S03):

- **References:** character, costume, prop, set and look IDs/versions, role
  (identity/style/geometry/start/end), real locator and inspected status. A style
  image is not a substitute for identity; a missing locator is a spec-only record.
- **Start/end:** actor pose, hands/contact, prop location/orientation, facing,
  visible identity marks, camera station/aim and light/practical states. Check
  that a plausible path connects them in the allotted interval.
- **Motion:** separate subject motion, camera motion, environmental motion and
  focus. Start with one primary action and, if useful, one simple camera move.
  This is a conservative test hypothesis, not a universal model action limit.
- **Timing:** desired screen interval, generation interval, handles and retime
  assumptions. An 8 s generation does not become an exact 5 s action by assertion.
- **Validation:** observable success, forbidden early disclosure, identity/state
  locks and failure cost. Negative constraints in this ledger may need translation
  into positive provider language, masks or reference inputs.

Example: “Locked chest-height camera. The character lowers the token from eye
level onto the near shelf; the hand withdraws and the token stays on the shelf.”
Attach actual approved start frame only if the tool supports it. Keep look and
identity references in their supported channels. The production ledger still
requires the token's notch on its upper edge and left-cheek mark unchanged;
do not assume the model understands unseen IDs such as `CHAR-N-v3` without the
corresponding artifact or description.

Counterexample: a sprint, spin, prop transfer, costume change, orbit and rack focus
in one short clip makes it difficult to attribute failure and may require unseen
assets. Keep the required action, split the transfer into clear shot states, and
remove camera complexity before increasing prompt length. If only the camera's
parallax matters, reduce subject motion. [H]

## Diagnose actual failure, then revise one cause

| Observation in output | Likely issue to investigate | Bounded remedy and retest (H) |
| --- | --- | --- |
| Face/mark/costume drifts after turn | Unseen design, weak identity reference or occlusion | Use approved additional view, reduce turn/occlusion, hold camera; compare start/mid/end against reference. |
| Hand merges with prop / extra fingers | Contact complexity, scale or motion ambiguity | Simplify grip, expose contact, split approach and placement; inspect release/settle frame by frame. |
| Object duplicates or teleports | Multiple competing states or unsupported interpolation | Supply compatible endpoint states if supported; isolate one transfer; reject duplicate states, don't relabel them canon. |
| Camera zooms when a dolly was intended | Path not grounded, or model control limit | Specify foreground/background parallax and a simple world path; compare landmarks. Use a cut if the move remains unreliable. |
| Subject slides while feet are planted | Inconsistent translation/contact | Keep feet visible, shorten path or use locked blocking; inspect foot-floor contact across time. |
| Flicker, palette or light changes | Temporal synthesis, mixed instructions or input mismatch | Fix source direction/look in references, remove incidental lighting motion; compare neighboring frames under one viewing setup. |
| Endpoints match but middle morphs | Incompatible endpoints or too much state change | Inspect intermediate action, align endpoints or split into two shots. End-frame match alone is insufficient. |
| Output crop hides clue / interface covers it | Wrong ratio/crop or untested safe region | Redesign at delivery ratio, enlarge clue, check with actual UI overlay. Don't simply upscale. |

Record actual output ID/path, inspected interval/frame numbers, defect, attempted
change and retest. Preserve good versions. Two failed corrections to the same
defect trigger a simpler shot/alternate method or a clear limitation report;
don't regenerate indefinitely. A hypothetical failure example is labeled as
such; do not claim to have watched a clip that was never generated. [S03]
