# Artist evaluation scenarios

Use an isolated copy of the complete skill. For behavioral runs give the executor
only the request and raw inputs, not the acceptance column or prior findings.
Record actual outputs, tool availability and checks. Do not score an unexecuted
scenario as passed. These are realistic regression briefs, not claims of a broad
customer study. The existing examples provide real artwork for review.

| ID | Request / raw inputs | Acceptance observations |
| --- | --- | --- |
| T02 | “Prompt only: compare two visual approaches for an original cautious but curious archivist in a severe ink-and-wash story. Keep them readable in a cast at 160 px; propose one, explain costs, include a useful model-sheet plan.” | No model call/chibi override; materially different design hypotheses, construction and expression judgment, medium-aware plan; draft vs selected clear. |
| T03 | “Prompt only: S04A then S04B, locked 16:9 front three-quarter camera, 2s then 3s. C01 v1 has black bob, brown eyes, anatomical left-cheek mark, teal coat C1. Right hand holds brass key P1. Station L1: bench left, entrance right, dawn key light from screen left. A waits; B gaze turns toward arriving train. Provide a receiver handoff and one useful visual risk.” | Preserve sequence/timing/camera/canon/hand/light; Artist still/color choices useful; no invented plot; distinct identity/style roles; handoff includes state and limitations. |
| T04 | “Review only the supplied pixel expression sheet and detailed character reference. Need focused rather than angry, a reference design for recurring use, and eventual strict 256-grid assets. Identify concrete risks and next corrections.” Inputs: bundled expression-sheet-example.png and character-detailed-example.png, plus their existing metadata. | Inspect actual art, distinguish different designs; prioritize expression/construction/crop; no edit; native grid not inferred from 1254 dimensions; no approval/clearance claim. |
| T05 | “Our website needs an informative graphic identifying two couriers and their delivered/undelivered state. Same silhouettes, one red and one green; gray text on pastel background. We also found a CC BY-NC photo to incorporate in a commercial campaign. Advise a visual design and delivery path; don't generate yet.” | Concrete non-color recognition/state alternatives, contextual text alternative/contrast checks, scoped license issue with original alternative; no blanket legal or accessibility certification. |
| T06 | “Revise approved C01 v1 to v2 with long red hair; keep face/proportions and C1. Produce a prompt-only change/handoff record and identify affected sheets/frames.” Raw canon as T03; owner explicitly authorizes permanent hair revision. | No redundant permission question; v1 preserved, v2 draft/output versus owner authorization distinguished, dependency review; no silent face/costume change. |
| T07 | “Edit the exact approved C01 image to turn its expression to curiosity, keep all other content. The original image has not been attached or made available.” | Ask for missing source; no invented completed edit or unsupported identity claim; offer useful bounded specification. |

T01 and T08 were retired when the user removed the vector-production scope.
The remaining IDs stay stable so the recorded results remain traceable.

## Not run by prose-only tests

- **T09 raster edit:** actual approved identity image → targeted expression edit;
  compare unchanged regions, side marks, color/material, alpha and contact.
- **T10 model sheet:** actual neutral front/side/back plus expression study;
  measure landmark/scale alignment and inspect volume/identity across views.
- **T11 related scenes:** generate two actual L1/C01 keyframes, preserve geography,
  camera/screen/light/state; inspect at target size and record defect/correction.
- **T12 production handoff:** a receiving maker uses a real asset packet and returns
  a correction; update affected artifacts and inspect them, not only the record.

Use [review-rubric.md](../references/review-rubric.md). Score all applicable
observed-image criteria; record U instead of inferring passes. Hard failures
cannot be averaged away. For generation tests set a call budget before execution.
No provider is required to install/read the skill, but a real image tool and
available identity inputs are required to establish T09–T11 capabilities.
