# Baseline, knowledge map and gap analysis

Inspected 2026-11-25: clean baseline **d13dc0f**, branch main, one worktree; no
AGENTS.md in checkout/ancestor chain. English Markdown, self-contained skill folders,
relative inline links, agents/openai.yaml, references/templates/research/tests and
the stdlib offline link/isolation checker are the actual conventions. No application,
agent service, dependency manifest or global install was changed.

## Neighbor evidence and concurrency

Read Artist SKILL.md, production-contract, evaluation, research audit/notes/sources,
metadata and repository README, contributing, installation, roadmap and validator.
This is a scoped contract/research inspection, **not** a re-audit of all Artist
assets or a rerun of its production tests. Its recorded production gate remains
open (T09–T12 pending); existing text/spec trials do not certify image production.

No Storyteller skill was present at the initial filesystem inspection. A read-only
status of the concurrent “สร้าง Storyteller Agent skill” chat confirmed active
work in the same checkout. The user explicitly directs parallel development, so
Screenwriter proceeds independently rather than claiming a completed prior gate.
The actual later Storyteller contract/template inspection is recorded in
[evaluation](../tests/evaluation.md). No claim of both specialists being validated
is made. No sibling package is a runtime dependency, and Artist sources are not
used as evidence for screenwriting craft.

## Knowledge map and claim-to-source coverage

“Covered” means actionable guidance was written, not that mastery was demonstrated.
P IDs resolve in [notes](notes.md); S source IDs resolve in [registry](sources.md).
Test IDs below refer to [scenarios](../tests/scenarios.md), not source IDs.

| Competency / deliverable | Guidance and principle → evidence | Observable check / remaining gap |
| --- | --- | --- |
| Bible/outline adaptation; locked canon | production-contract, format-medium, template; P10/P12 → D, S12/S19 partial | S05 plus actual Storyteller draft receiver exercise; owner clarification and rights review separate |
| Objective, obstacle, tactics, turn, entry/exit, causality/stakes | scene-craft; P01/P03 → S04 + H | S01/S02/S05; quiet-scene and long-form tests needed |
| Scene beats, agency, ensemble | scene-craft; P01/P04 → S04 + H | S02/S08; longer ensemble performance not established |
| Dialogue voice/intention/subtext/rhythm, silence | dialogue-action; P07 → S05/S06/S07/S08 | S02; real performers/native speakers still needed |
| Visual action, prose, showing/telling, VO | dialogue-action; P06/P08 → S03/S05/S06/S10/S12/S13 | S01/S03; no film readability proof |
| Format: slug/time/action/cue/dialogue/parenthetical/VO/OS/transitions | format-medium; P09 → S01/S02/S03/S13/S14 | S08; PDF layout and other house templates untested |
| Knowledge control, irony, tension, setup/payoff | scene-craft; P02/P03 → S09/S16/S04 + H | S03/S06; no puzzle-comprehension trial |
| Comedy and non-dialogue | scene-craft, examples; P05/P06 → S09/S14/S03/S10 | S01/S04; no laughter/comprehension study |
| Short 15–60s vs long-form | format-medium; P03/P11 → S04/S10/S17 + H | S01/S04; full feature not generated/evaluated |
| Episodic/serial and localization | format-medium; P12 → S17/S19 + H/D | S06/S08; bilingual/series-room expertise not established |
| AI/animation constraints, breakdown | revision-production/template; P12 → S12/S18 + D risk hypotheses | S01/S05; no provider/video test |
| Accessibility and provenance | revision-production; P14 → S15/S11 + D | S08; no rendered media/player or legal conformance claim |
| Revision, continuity/history, handoff | revision-production/contract/template; P10/P13 → D/S10/S07/S18/S19 | S06/S07; real downstream owner acceptance pending |

## Gap decisions

- **No pre-existing Screenwriter:** build only this role. Do not fix Artist gates,
  implement Storyteller, launch orchestration or create future agent folders.
- **Broad craft vs thin evidence:** scene/dialogue/format have cross-source grounding;
  mystery and serial/adaptation now have direct practitioner grounding; ensemble
  ledger details, localization and AI-specific methods remain explicitly H/D
  extensions. They are useful hypotheses, not comprehensively researched standards.
  Expand those areas using inspected practitioner/production material when real
  use reveals a decision the current guidance cannot resolve.
- **No full craft books available:** S12 is a real inspected preview; Field/Snyder/
  McKee are not claimed read. The preview does not substantiate unviewed chapters.
- **No universal formatting:** don't add a screenplay linter that rejects legitimate
  variants. Use recipient requirements plus an actual export check when requested.
- **Practice evidence:** use realistic model tasks and retain actual outputs,
  including failures. Distinguish author self-review, independent model execution,
  human craft review, read-through and rendered-production evidence. No aggregate
  number should erase a hard canon/authority violation.
- **No source-count gate:** a supported decision with a stated limit is more useful
  than an inaccessible textbook name. No empirical “expert-level” quality claim.

## Integration scope

The new package reuses existing repository validation; it adds no dependency or
sibling runtime link. Shared docs may be edited concurrently by the Storyteller
chat; preserve those changes and avoid rewriting its status. Record any remaining
parallel handoff mismatch precisely in the evaluation rather than asserting a
fictional shared schema. The current semantic split is mandated by the user's task.
