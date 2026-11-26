# Inventory, competency map and integration gaps

Inspected 2026-11-25 in `wayu-arts`, the skill package used for The Stories.
Baseline branch `main`, HEAD `d13dc0f` (Artist deepening/removal of SVG).
Initially untracked Storyteller work; Screenwriter files appeared during this
task. No AGENTS.md was found in the checkout or ancestor chain. No separate
The Stories service/runtime or shared machine contract was found.

## Inspected owning sources

Read repository README, SPECIALIST_ROADMAP, CONTRIBUTING, structure validator;
Artist's latest SKILL, production contract, source registry, audit/notes and
evaluation conventions; discovery metadata. Read Storyteller's draft SKILL and
production contract, Screenwriter's draft production contract and script-packet
template after they appeared. These are point-in-time reads, not stable frozen
contracts. This task owns only `skills/cinematographer/`.

Existing conventions retained: English repository guidance, user-language
deliverables, concise SKILL with progressive disclosure, relative links and
self-contained copied folder, optional discovery metadata, research separate
from runtime, scenarios separate from claimed evidence. No sibling import or
shared-file edit is necessary. The user's explicit parallel-role request takes
precedence over the older roadmap's sequential creation advice; this batch does
not assert that Artist's pending artifact gates were completed.

## Competency and evidence map

“Implemented” means usable guidance/examples exist, not proven mastery.
Claim IDs resolve through [notes](notes.md) and [sources](sources.md).

| Competency / observable decision | Initial gap / source basis | Implemented location | Proof still needed |
| --- | --- | --- | --- |
| Translate script/vision into visual inference without canon edits | Artist only named future role; P01/P02/P04 | Strategy + contract; T01/T03/T11 | Fresh independent briefs and owner selections |
| Shot size/function, master/coverage/singles/two shot/OTS/POV/reaction/insert/cutaway | No camera skill; P01/P03 | Strategy function table; T02/T03 | Actual coverage assembled in a cut |
| Hierarchy/depth/negative space/balance/framing; ratio/safe-area/9:16 | Still guidance existed in Artist; P04 + S02 | Strategy; T05 | Rendered vertical frames/host overlay and viewer recognition |
| Viewpoint, angles, motion families; zoom/dolly/focus distinction | No owned shot method; P01/P07/P14 | Camera optics; T07/T09 | Previs/clip with measured paths/parallax |
| Gate/FOV/distance/aperture/DOF/exposure/shutter/fps/focus/DR/WB | No scoped technical reference; P07–P14 | Camera optics; T07/T08 | Specific lens/camera or renderer tests, calibrated viewing |
| Light direction/quality/contrast/motivation/practicals/continuity | Artist owns global look, not every shot; P05/P10/P11/P15 | Lighting; T08 | Actual frame/scopes and reverse-light comparison |
| Blocking, staging, axes, eyelines, 180/30 and intentional exceptions | No shared geometry proof; P06/P23 + H | Continuity; T02/T04/T09 | Boards/previs/real performance read |
| Spatial/temporal/action/identity/knowledge continuity | Canon guidance does not specify shot transitions; P06 + S02 | Continuity ledgers + packet checker | Real adjacent clips; checker cannot see pictures |
| Reveal/withholding, motifs and contrast | Crosses story ownership; P02/P04/P05/P22 | Strategy; T03/T04 | Contextual audience test; culturally varied cases |
| Sequencing, coverage, duration and Editor collaboration | Needs primary/alternate distinction; P03/P06 | Workflow/contract; T01/T02 | Measured animatic and actual Editor response |
| Genre/style/medium differences | No camera presets should become laws; P04/P15/P18 + H | Strategy + animation reference | Diverse shorts/live action/animation trials |
| Animation/layout and board/previs specification | Related Artist handoff available; P16–P18 | Animation + template/packet | Artist-rendered boards and temporal previs |
| AI start/end/reference roles, motion/action budget, failure/revision | Provider-specific capability risk; P19–P21 + S03 | Animation/AI; T06/T10 | Actual provider tool + inspected outputs/revision |
| Production constraints, versioning and interoperable handoff | Parallel contracts provisional; S01/S02 | Workflow/contract; T11 | Incoming real packet mapped and accepted by receivers |
| Evaluate/diagnose/revise with evidence | No camera trial baseline; S04 | Rubric + scenarios/evaluation | Independent forward tests, not source count or self-score |

## Gap and overlap decisions

- **Storyteller:** keep narrative disclosure constraints and canon upstream;
  Cinematographer chooses how the approved access becomes visible. A changed
  identity/reveal order is an explicit proposal.
- **Screenwriter:** script beat and narrative beat are separate ID types. Camera
  coverage does not rewrite dialogue, add events or turn every beat into a shot.
- **Artist:** use existing look/identity and return shot-specific frame/light
  requirements. Artist renders boards/assets; this skill specifies and checks
  their function. Do not duplicate Wayu style assets or create a competing bible.
- **Director:** owns integrated interpretation, performance and approvals; direct
  user briefs work without a Director installation. No Director skill is created.
- **Editor/Sound:** provide coverage/timing proposal and sync/geography needs;
  neither final cut nor audio treatment is silently claimed.

The standalone packet is a reversible adapter choice, not a shared contract
rollout. At initial inspection README/roadmap described the earlier Artist batch.
During validation, concurrent tracked edits appeared in README, CONTRIBUTING,
INSTALLATION, SPECIALIST_ROADMAP and Artist's contract, plus new Director/Critic
folders. This task neither created nor edited those files. The read-only Artist
contract diff changed availability wording, not the camera/asset boundary.
Preserve all concurrent work; shared documentation remains outside this task's
ownership. Skills CLI/package installation and a real multi-role run are not
changed or claimed here.

## Remaining limits

The source set covers baseline design, optics, lighting and pipeline judgment;
it cannot supply measured model fidelity, cultural universals or hardware
calibration. Specialty engineering, real-time engines, stereoscopy, high-speed
capture and complex VFX require scoped additional research. Evidence of current
static checks and authored exercises is in [evaluation](../tests/evaluation.md).
No source, board, code or task count substitutes for these remaining practice gaps.
