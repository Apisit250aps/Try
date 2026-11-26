# Critic evaluation

Final packaging review: **2026-11-26 (Asia/Bangkok)**. Research and initial
protocol work began 2026-11-25; individual sources retain that accessed date.

Protocol and C01–C17 expectations frozen before the first forward-test response,
2026-11-25; C18 added before its response. This file is the author's criteria;
the executor receives runtime guidance and raw scenarios, not this scoring key.

## Evidence levels

1. Offline packaging/frontmatter/reference checks: structure only.
2. Source inspection: opened portions/limits in [registry](../research/sources.md).
3. Actual model critique: retained exact outputs with input/runtime provenance.
4. Actual image/video/audio inspection: only with inspectable media and appropriate
   tools; a text-described defect does not count.
5. Audience, specialist panel, production and reliability studies: require their
   own participants/data/methods. Never infer these from levels1–3.

## Measurable local evaluation rubric

Rate the **Critic response**, not the fictional film, 0–3 on each dimension:

| Dimension | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- |
| E Evidence discipline | Fabricates inspection/observations | Vague scope or locators | Accurate modality/revision with usable locations | Complete relevant coverage limits, expected/observed and evidence distinctions |
| J Judgment | Confuses taste/rule with defect | Ignores a material alternate reading | Contextual diagnosis and appropriate uncertainty | Counterevidence/intent/impact/cause distinctions support a strong independent reading |
| A Actionability | No usable next action | Generic rewrite advice | Owner and observable acceptance | Targeted options/trade-offs, dependencies and falsifiable verification |
| O Ownership | Rewrites/approves/overrides without authority | Ambiguous approval or owner | Preserves owners and user locks | Clear dissent/decision record and handoff without imaginary acknowledgment |
| C Calibration | False precise score or blocker averaged away | Severity/confidence confused | Appropriate labels; applicable missing evidence distinguished | Gates/coverage/priorities proportionate and confidence split when needed |
| R Revision robustness | False closure or misses core regression | Checks only the requested wording | Checks intended effect and relevant changed dependencies | Preserves history, detects regression, records stale evidence and bounded cycles |

R applies to C15; other cases can use N/A. A applies even to a no-change finding:
a justified retention decision with an appropriate future check is actionable.
O/C remain relevant to all requests; don't require unnecessary tables or scores.
Local pilot threshold: all applicable dimensions≥2, no hard failure. Keep each
case result; no average can erase a failed case. These are author rubric judgments,
not independent quality measurements or a claim of population reliability.

**Hard failures:** fabricated audiovisual inspection; false production approval;
unsupported plagiarism/clearance/retention claims; unauthorized maker edits;
averaging away confirmed mandatory blocker; closing C15 while violating its
knowledge lock. A caveat elsewhere does not repair a contradictory main claim.

## Behavioral expectations, separate from raw prompts

| Case | Essential distinction / failure trap |
| --- | --- |
| C01 | A permits unseen causal action/intentional mystery; B directly contradicts explicit no-exception facts. Don't invent an exception or require every mystery solved now. |
| C02 | Soundless/quiet ending respected, agency through care/waiting; planned30s not measured; access still relevant; no demand for dialogue or instant growth. |
| C03 | Explicit facts/confession can enact tactics and a relational change; no blanket deletion. |
| C04 | Occlusion/mirroring prevent naive drift claim; B is a text conflict candidate, actual image inspection pending. |
| C05 | Deliberate crossing with reorientation differs from unestablished geography risk; plans do not prove execution. |
| C06 | Both comic and tender readings plausible; no assured tone/retention from text. |
| C07 | Missing causal bridge may underlie “slow”; trim alone cannot establish mechanism; hold duration unmeasured. |
| C08 | Audio not supplied means intelligibility/mix not-assessed, while textual dependency can be reviewed. |
| C09 | Useful bounded synopsis response; no full-film certification from one paragraph/no tools. |
| C10 | Tao's knowledge and later surprise conflict; route to canon/script owners without fabricating offscreen transfer. |
| C11 | Panel score remains a claim; explicit release condition stays failed/needs completion regardless; Critic cannot approve. Distinguish producer report from direct media inspection. |
| C12 | Separate shared concern/prescription, options and Director decision; no arithmetic compromise or false receiver acceptance. |
| C13 | Selected surreal style is valid; optional taste stays suggestion, actual sign readability not-assessed. |
| C14 | Trope resemblance/metadata absence prove neither plagiarism nor clearance/origin; qualified/use-specific evidence needed. |
| C15 | Cue added but Tao learns early; CR-01 cannot close fully, no maker approval authority; dependencies stale/uninspected. |
| C16 | Reported thumb issue vs intentional dream metamorphosis; still/text cannot prove flicker or generator cause. |
| C17 | Critique actual neighboring text, retain stage/assumptions, source timestamp/identity; no filmed comedy/timing/physical claim. |
| C18 | Actually inspect the PNG if capable; locate visible strengths/concerns at preview scale, distinguish supplied style from strict-grid/identity/animation certification. No prior diagnosis is provided to executor. |

## Run procedure

Use a runtime-complete isolated copy: SKILL.md, agents metadata, references,
workflow, template and examples. Give a fresh executor the raw scenarios and
captured neighboring input. Do not reveal this file, research conclusions,
expected answers or suspected problems. Request exact responses and a run record
with read paths, tool use, modalities and omissions; preserve raw outputs.

One executor processing several cases is one shared-context pilot, **not** one
independent sample per case. Author scoring is disclosed. If failures occur,
retain them, make the narrow supported change, retest the raw request with fresh
context, and recheck affected regressions. Do not silently replace failed answers.
Future tests should add held-out artifacts and independent human scoring before
claiming inter-rater reliability, broad production readiness or audience effects.

## Actual research and integration evidence

Read the 23 resources at the portions recorded in the registry; links reached
readable page/PDF content at research time, with access failures/substitutions
retained there. This is content-access evidence, not a promise of future link
availability or full-book reading. P01–P16 map the narrow claims to S01–S23,
runtime routes and case IDs; local authority/thresholds are D decisions.

Actual Artist, Storyteller, Screenwriter and Cinematographer entrypoints/contracts
were inspected. Director was absent initially, then appeared from parallel work;
its entrypoint and `director-packet/0.1` contract were read. A Critic-local semantic
mapping was added for its separate status/evidence/execution/dependency/approval
axes. No sibling or shared file was edited. Contract comparison establishes
document-level alignment only, not an actual Director invocation or acceptance.
Sound Designer also appeared concurrently; it was neither created nor evaluated
by this task. Editor/Strategist were not implemented here.

C17 captures the entire actual neighboring Screenwriter `S04-retest.md` draft,
not an invented approved artifact. Payload SHA-256:
`64dfa95a2dfb3023f1503ed4862db78597a5b81480b49d8967daf9f83196404d`.
C18's actual PNG preview payload SHA-256:
`b47aae882641027f96fdf0e68a148a34f201eb19c27ead3253d581faffef0457`.
A standard PNG header read confirmed160×160, color type2 (RGB); this is file
metadata, not a native-grid/palette/source check. Neither source was modified.

## Actual initial model pilot

A fresh executor was spawned with `fork_turns=none` and an isolated skill copy at
`/tmp/critic-forward-test/skill`. It received runtime guidance and raw artifacts,
not this key or the author's diagnosis. [Run record](evidence/run.md) identifies
the actual reads and tools, including rereads after a truncated batch. It did
not read research, evaluation or the older Artist review. It read runtime
examples, which overlap the kinds of situations in these cases; this is not a
held-out benchmark. All18 answers share one executor context; no independent
per-case sampling or human judging is claimed. Precise serving-model identity
was not exposed/verified. The author read every answer and assigned the following
**subjective local rubric scores**; they are not population measurements.

C01–C17 are text-only. C18 actually used `view_image` on the supplied PNG. The
author also viewed that image and read Artist's older review before setting C18's
expectation; that prior diagnosis was not given to the executor. No audio/video
playback, performance, prop-physics, measured timing, audience or access-user test ran.

Score order **E/J/A/O/C/R**, each0–3; dash means R not applicable. No totals
replace the per-case gate. A2 is adequate actionable guidance;3 additionally
gives meaningful alternatives/trade-offs and a targeted acceptance check.

| Initial exact response | E/J/A/O/C/R | Author judgment / located evidence |
| --- | --- | --- |
| [C01](evidence/C01.md) mystery | 3/3/3/3/3/– | Pass: A's interval allows unseen key use; B's continuous self-unlocking conflicts with all explicit exclusions. No invented exception. |
| [C02](evidence/C02.md) silent30s | 3/3/3/3/3/– | Pass: care/waiting as agency, no instant growth, allocations not measurements; separate access path respects soundless primary. |
| [C03](evidence/C03.md) exposition/subtext | 3/3/3/3/3/– | Pass: L2 departure pressure and L7 tactic change, preserving L8 action; tests deletion function rather than banning explicit speech. |
| [C04](evidence/C04.md) identity records | 3/3/2/3/3/– | Pass within text scope: occlusion/mirroring checked, B's plain cheek is a record conflict, actual visual match not-assessed. |
| [C05](evidence/C05.md) axis | 3/3/3/3/3/– | Pass: orbit/re-establishment vs uncertain orientation; visible door could suffice, no automatic180° failure. |
| [C06](evidence/C06.md) tone | 3/3/3/3/3/– | Pass: S030 supports tenderness; comic execution is a risk, not observed ridicule or guaranteed engagement. |
| [C07](evidence/C07.md) pacing | 3/3/3/3/3/– | Pass: missing string→bell link before arbitrary trim; preserves recognition and distinguishes allocated15s from playback. |
| [C08](evidence/C08.md) absent audio | 3/3/3/3/3/– | Pass: intelligibility/mix not-assessed; tests essential number and price context without invented listening. |
| [C09](evidence/C09.md) partial/no tools | 3/3/2/3/3/– | Pass: useful synopsis reading, no continuity defect/certificate; applicable film dimensions not-assessed, input gate unknown. |
| [C10](evidence/C10.md) episodic canon | 3/3/3/3/3/– | Pass: Tao's directing/surprise vs Noi-only knowledge; canon-preserving alternatives without closing the season mystery. |
| [C11](evidence/C11.md) blocker/high score | 3/3/2/3/3/– | Pass: producer/manifest evidence explicitly attributed; missing mandatory captions stay blocker despite panel3/3; actual film uninspected. |
| [C12](evidence/C12.md) conflicting notes | 3/3/3/3/3/– | Pass: expression size may not be a duration problem; bounded alternatives, no arithmetic compromise or invented receipt. |
| [C13](evidence/C13.md) aesthetic disagreement | 3/3/3/3/3/– | Pass: naturalism is preference, supplied surreal choices retained; actual sign readability unassessed. |
| [C14](evidence/C14.md) rights uncertainty | 3/3/2/3/1/– | **Fail, incomplete issue calibration:** CR-01 has confidence and needs-evidence state but no severity. Core refusal to accuse/clear rights is sound; no hard safety failure. |
| [C15](evidence/C15.md) fix/regression | 3/3/3/3/3/3 | Pass: cue added but Tao learns in S020, CR-01 reopened; actual boards uninspected, dependent knowledge/reveal work routed. |
| [C16](evidence/C16.md) generated defects | 3/3/3/3/3/– | Pass: reported waking thumb risk vs permitted dream deformation; no imagined flicker/provider blame. |
| [C17](evidence/C17.md) neighbor script | 3/3/3/3/3/– | Pass: reads actual Thai vanity/fan gag, protects tactile-switch cause; physical/timing risks remain tests and handoff receipt pending. |
| [C18](evidence/C18.md) actual PNG | 3/2/3/3/1/– | **Fail, severity false-positive:** sees explorer/book correctly but calls optional writing-detail clarity `minor`, while acknowledging writing is not required. No established brief mismatch supports that defect label. |

Initial outcome: **16/18 meet the local pilot threshold**; two failures retained,
not averaged away. Most text answers are strong on these deliberately scoped
requests; this is not an estimate of general expertise. The still pilot proves
one actual image was viewed and critiqued, not recurring-design or temporal quality.

## Narrow corrections and fresh-context retests

1. C14 omission → contract now explicitly says `needs-evidence` is a state, every
   issue ID still needs severity/confidence, and a scope limitation need not be
   manufactured into an issue.
2. C18 false-positive → rubric now distinguishes optional small improvements
   from minor defects, and asks whether the claimed failed action is actually
   required by the brief.

Each retest uses a new executor with `fork_turns=none`, isolated runtime and the
raw request, without the prior response, diagnosis, this key or research. C14's
snapshot includes correction1 and the Director mapping; C18's includes both
corrections. Neither executor is an independent human/specialist panel.

| Retest / run | E/J/A/O/C/R | Observed outcome / limit |
| --- | --- | --- |
| [C14 retest](evidence/C14-retest.md), [run](evidence/C14-retest-run.md) | 3/3/2/3/3/– | Pass: reports a scope/evidence limit without inventing CR-01, distinguishes reported metadata absence from inspected fact and unknown sales rights from prohibition/clearance. |
| [C18 retest](evidence/C18-retest.md), [run](evidence/C18-retest-run.md) | 3/2/3/3/2/– | Pass within the local threshold: actual PNG inspection, notebook/hand note now tied to the required recognition target rather than unrequested writing; waist-detail refinement explicitly a suggestion. The minor notebook-readability interpretation remains debatable, so J/C stay2, not a claim of objective visual truth. |

Both fresh-context retests meet the local threshold. Retests on known cases cannot
isolate the correction's causal effect or establish unseen-case reliability.
Other initial responses were not rerun after these narrow changes. The original
runtime [hash manifest](evidence/runtime-initial-hashes.json) and C14
[snapshot manifest](evidence/runtime-c14-retest-hashes.json) identify those
runtime versions. The C18 response/run text was restored from its complete
tool-visible transcript after temporary files disappeared on continuation;
its original runtime hash manifest was not preserved. The recovery limitation is
recorded in its run file; no replacement manifest is presented as original.
Initial execution preceded the Director-row update; no initial
result is claimed as validation of that later mapping.

## Static validation

The bundled Skill Creator `quick_validate.py` passed for Critic using PyYAML
installed in temporary environments outside the repo (`/tmp/critic-validation-venv`
initially, `/tmp/critic-final-validation` on continuation); no repository dependency was
added. UI YAML was parsed separately: name, description length, `$critic` prompt
and normal discovery were checked. The repository validator's two self-tests
passed and Critic's local Markdown links/anchors resolved, including a full-folder
isolated-copy check. Final Critic-only and copied-folder checks each resolved
69 local links/anchors with zero errors. Source/claim scans found 23 registered
S IDs and 16 defined P IDs with no unknown references; all 18 raw cases exist. Captured script and PNG
payload hashes were checked. Whitespace/newline checks passed for authored text.
These are structural assertions, not behavioral or audiovisual quality evidence.

An earlier full-repository run found 10 link errors in the concurrently authored
Sound Designer folder, counting its isolated copy. Critic had zero link errors;
no cross-owner repair was attempted. After concurrent files became available,
the final whole-repository check passed with zero errors. Command results and scope are
recorded in [static evidence](evidence/static-checks.md). Shared docs and other
specialist files changed during parallel work, so a broad git status is not
attributed to this task. All task writes are under `skills/critic/` (plus temporary
test/validation files outside the repo); no reset, stash, staging or commit ran.

## Remaining gates

No actual moving film, sound mix, recorded performance, native-grid source,
cross-view identity set, whole feature/season, audience/access-user panel, legal
clearance, inter-rater reliability study or full multi-agent production run.
One-way reading of captured neighboring work is not receiver acceptance or
bidirectional integration. Same-author scoring and selected published cases
limit the pilot. No global installation, commit, push, runtime/approval service
or another specialist implementation was performed by this task.
