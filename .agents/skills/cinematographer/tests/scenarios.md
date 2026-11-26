# Cinematographer evaluation scenarios

Use each brief without showing the evaluator the worked answer first. For
independent testing, provide only the skill folder, brief and raw input artifacts
in an isolated workspace; record model/version/date, exact input/output and
allowed tools/budget. No subagent/model trial is implied by this document.

The current [worked exercises](../examples/worked-sequences.md) are same-author
illustrations. Apply the [rubric](../references/review-rubric.md), preserve actual
outputs and distinguish spec, static, artifact, receiver and audience evidence.

| ID / raw brief | Required observable behavior | Meaningful failure and next test |
| --- | --- | --- |
| T01 Silent 30 s: N finds toy bird, lifts/winds/releases it, bird moves, N responds. No indispensable text/audio. | Actual ordered shot specs; stable IDs/states, readable contact/mechanism and consequence, primary durations total 30 s, alternatives separate. | Pretty frames omit winding/release; test rendered mute animatic and uncoached event recall. |
| T02 Two seated speakers exchange envelope; seal must stay hidden; 20 s, static camera. Supply dialogue unchanged. | Space/axis map, reciprocal eyelines, consistent hands/prop/time, useful listener and action coverage. | Both singles look same way, or seal revealed. Inspect adjacent boards and a spoken/timed assembly. |
| T03 Courier sits, audience sees broken seal just before courier notices; culprit hidden. | Explicit visible/withheld ledger and ordered evidence/reaction, no added plot or sound clue. | Early frame/reflection exposes seal or culprit; inspect all frames before allowed reveal. |
| T04 Same 12 s slot: ball retrieval versus quiet contemplation after friend leaves. | Different information density/motion/coverage with preserved events; reasons and calm/action counterexamples. | Equating action with shaky cuts and sadness with blue; compare actual contact clarity/performance room. |
| T05 Adapt T02 for 1080×1920 with missing platform overlay. | Vertical staging/framing alternatives, provisional safe region, target preview size, essential-read and overlay test pending. | Center crop loses partner/hand; generate board and inspect at 270×480 with real UI overlay. |
| T06 Own-left cheek mark/right scarf knot; toy chipped left wing; reverse view requested without approved unseen-side art. | Preserve asset/version, ask for missing construction or label provisional; no mirroring or invented approved views. | Flipped identity or repaired wing accepted as canon; inspect approved multi-view/start-mid-end frames. |
| T07 Attention change without moving station; alternate brief requires seeing behind foreground leg. | Distinguish zoom/crop/focus from translation and parallax; correct physical explanation and feasible choices. | “Zoom around the leg”; test ideal geometry and actual clip/renderer. |
| T08 Lamp-motivated low light, textured shadows, readable token, no exposure measurements. | Source direction/quality/contrast, practical control, DOF/exposure trade-offs and test plan; no made-up measurements. | Universal ISO/f-stop guarantee or global darkness; inspect scopes and actual poses/clip. |
| T09 Deliberately cross axis at supplied turn, geography must remain legible. | Purpose, visible bridge/new side/recovery, state continuity and fallback. | Hard ban on crossing or unmotivated reverse with insert “fix”; inspect temporal previs. |
| T10 Synthetic failure report: extra key at 2.1 s, wing repairs after occlusion; missing clip, provider unknown. | Label report unverified; ask for evidence while drafting constrained v2, capability check, root-cause simplification, bounded fallback. | Pretend clip inspected or promise unsupported end control; then run actual bounded generation/revision if authorized/available. |
| T11 Story NB07 → script E02-S030/B01,B02; look v2; conflicting intact-seal draft asset. | Map typed IDs/versions, preserve raw fields, flag conflict; usable Artist/Editor/Sound packet and actual vs pending receipts. | Rename IDs, rewrite script, claim receiver accepted; send real packet only when authorized and record response. |

Include adversarial variants: missing screenplay/reference, contradictory locked
camera and action, script revision mid-plan, 30→20 s budget cut, deliberate
nonclassical discontinuity, culturally different color/angle interpretation,
review-only request and unavailable generation tool. A useful response can
continue unaffected planning while marking only the consequential gap blocked.

## Offline checks

From the repository root:

```bash
python3 skills/cinematographer/scripts/validate_packet.py --self-test
python3 scripts/validate_repository.py --root skills/cinematographer
```

The first performs subset semantic checks on the concrete JSON fixture plus
positive/negative cases; it is not a JSON Schema service or image inspection.
The second uses the existing inline Markdown-link checker; separately copy the
folder into a temporary directory and check it to establish package isolation.
Skill Creator's quick validator checks frontmatter/scaffold only. Source HTTP
access is recorded per inspected route in the registry, independent of packaging.
