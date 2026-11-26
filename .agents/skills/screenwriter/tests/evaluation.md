# Screenwriter evaluation — 2026-11-25

This record separates packaging, source inspection, model writing, performance
and production evidence. Baseline d13dc0f. Work is scoped to Screenwriter while
Storyteller is being developed in the same checkout. No inherited Artist or
Storyteller result is counted as a Screenwriter pass.

## Research evidence

The [registry](../research/sources.md) records 19 actually opened public sources
and specific inspected portions: Academy, ACMI, BAFTA/BFI, author-hosted Scriptnotes,
ScreenSkills, WGA, W3C, a Routledge preview and two officially hosted screenplays.
Full books, full scripts, embedded clips and paywalled courses are not claimed read.
The BBC library landing failed; the direct BBC Detectorists PDF was readable.
Primary-source substitutions and other failures are preserved. No source text or
screenplay was copied into the skill; worked examples are original instructional
fragments. These access observations do not establish professional mastery.

Cross-validation covered formatting variants, scene purpose vs discovery,
visual action vs dialogue/VO, economy vs pauses, mystery vs confusion, and feature
vs episodic assumptions. The [knowledge map](../research/audit.md) and
[P01–P14](../research/notes.md) identify which details remain H/D synthesis.

## Neighbor contract inspection

Initially only Artist existed. Read its current entrypoint, production contract,
research/evaluation records and repository conventions. Artist's production gate
is still recorded open; no new Artist production test is claimed here.

During parallel work, Storyteller's SKILL.md, production-contract, story-bible and
story-outline became available and were actually read. Its story-level event,
revelation-order and canon authority align with Screenwriter's scene realization,
ID mapping, proposed story changes and version/status distinctions. Its optional
YAML-shaped packet uses task_id, status, story_id, version, supersedes, canon_used,
deliverables, assumptions, checks, pending and handoff. Screenwriter accepts those
semantics without requiring that exact serialization; script scene/beat IDs map
to the supplied narrative IDs. That comparison is **document-level compatibility inspection**. The later
artifact-to-model exercise below adds limited behavioral evidence; neither proves
versioned schema compatibility, production handoff acceptance or independent
acceptance of Storyteller's skill. Concurrent edits may drift.

## Static checks

First packaging run found missing evaluation files in both in-progress packages;
no attempt was made to alter Storyteller's files. Screenwriter frontmatter passed
using PyYAML in a temporary environment after system Python lacked PyYAML. No
repository dependency was added.

Final scoped packaging check: **55 local links/anchors in a temporary root plus
55 in its isolated skill copy, zero errors**; both checker self-tests pass.
Skill Creator frontmatter validation passes. All 19 registry IDs are cited in
research notes; 14 principle IDs resolve; all six runtime guides route to notes.
That coverage check is syntactic, not proof of semantic support. `git diff --check`
passes for tracked changes; new Markdown/YAML files were read as nonempty UTF-8.
Exact earlier [static outputs](evidence/static-validation.txt) retain the 54+54
pre-log-link count and a whole-tree snapshot with 20 missing-target reports, all
from the concurrently unfinished Cinematographer package (10 targets also checked
in isolation). That package was not created or edited by this task. Whole-tree
results are scoped snapshots, not a pass claim for every parallel skill.

Reproduce Screenwriter alone without requiring other in-progress roles:

```python
from pathlib import Path
from tempfile import TemporaryDirectory
import shutil, subprocess, sys
repo = Path.cwd()
with TemporaryDirectory() as tmp:
    root = Path(tmp)
    shutil.copytree(repo / "skills/screenwriter", root / "skills/screenwriter")
    subprocess.run([sys.executable, str(repo / "scripts/validate_repository.py"),
                    "--root", str(root), "--self-test"], check=True)
```

Run that snippet from the repository root. Whole-repository checks use
`python3 scripts/validate_repository.py --self-test`. Remote source access was
checked via actual browser-tool opens during research and logged in the registry,
not by this offline checker.

## Independent model execution and primary review

An executor received the eight raw requests in [scenarios](scenarios.md) and an
isolated runtime-complete snapshot at `/tmp/screenwriter-forward-test/skill`.
Its snapshot preceded this evaluation file and later research expansion; the full
final package's isolation is checked separately. It read SKILL.md, all six runtime
guides and the packet template as a batch. It was told not to read research,
tests, rubric, expected answers or the parent conversation, and reports that it
did not. No per-task loading or token saving is measured. Actual
[run record](evidence/run.md) and exact S01–S08 responses are retained below.

This is **one shared-context execution across eight cases**, not eight independent
samples. Specific runtime model ID was not exposed/verified; no cross-model or
statistical reliability claim is made. The primary skill author then read the
responses and assigned the following **subjective rubric judgments**, not an
independent Critic or native-language panel score. All runtime numbers remain
planning estimates. No read-through, image/video generation or audience test ran.

Dimensions in order: C canon/authority, D dramatic action, I information/causality,
V dialogue/visual performance, T medium/format/timing, R revision/continuity/handoff.
Each is 0–3. “–” is N/A (R was not requested for S02–S04; their requested beat/
knowledge records are assessed under D/I). Threshold was set in the scenario
rubric before outputs: ≥80%, all applicable scores ≥2, no hard failure.

| Case / exact initial output | C/D/I/V/T/R | Result and located evidence |
| --- | --- | --- |
| [S01](evidence/S01.md) silent 30s | 3/3/3/3/2/3 = 17/18 | Textual pilot pass. Hand almost releases boat into bin, then supports its still-torn hull; no forbidden audio/text. Allocations sum to 30 but 28–35s is explicitly unmeasured. Boat/water contact still needs production testing. |
| [S02](evidence/S02.md) subtext/ensemble | 3/3/3/3/2/– = 14/15 | Textual pilot pass. Packing/food invitations progress from evasion to a real invitation; silent May removes completed work and nearly removes the chair, forcing a tactic change. Final candor is an earned change, not a backstory speech. 72–87s unmeasured. |
| [S03](evidence/S03.md) mystery | 3/2/1/2/2/– = 10/15 | **Fail for requested audience mystery.** The opening shows the owner move/hide the medal in full before the search; knowledge table confirms viewers already know. This creates dramatic irony instead of preserving a puzzle for viewers. Canon itself is preserved. |
| [S04](evidence/S04.md) comedy | 3/2/1/2/2/– = 10/15 | **Fail for causal clarity.** The last pen is swept into the drawer, yet the later release depends on a pen propping its edge; that position is claimed in notes but not planted clearly in the screenplay. Shirt trapping is readable; the final mechanical payoff needs repair. No measured laughter claimed. |
| [S05](evidence/S05.md) canon adaptation | 3/3/3/3/2/3 = 17/18 | Textual pilot pass. Maps bible v3/N07; dry walkway return, crack retained, only siblings present; conflicting dive/heal note becomes a separate canon-change question. Full bible not claimed read. |
| [S06](evidence/S06.md) episode continuity | 3/2/3/2/2/3 = 15/18 | Textual pilot pass within blocked-entry scope. Door/key state retained; brother signals without speaking; Noi learns his presence only after evidence; playable contact precedes a precise owner decision for entry/reconciliation. Window staging and the interpretation of a jammed door are provisional, not verified set facts. |
| [S07](evidence/S07.md) authorized revision | 3/3/3/3/2/3 = 17/18 | Textual pilot pass. S020 adds taking back/choosing to leave the basket; S010/S030 meanings and IDs remain; brother learns after departure; R1 implemented without repeated permission. Four receiver packets prepared, none called accepted. |
| [S08](evidence/S08.md) format/localization | 3/2/3/3/2/3 = 16/18 | Textual pilot pass. Thai house cues, adjacent-room O.S. and future V.O., no shooting numbers/PDF claim; status reversal replaces an unavailable pun function, with that input limit stated. Caption/description requirements kept outside primary script. Chair mechanics and translated performance untested. |

Initial outcome: **6/8 meet the local textual pilot threshold; two observed
failures retained**, not converted into successes by averaging. T is never scored
3 because timing/layout remains inferred, not independently checked in delivery.

## Corrections and fresh-context retests

Two narrow changes followed actual failures:

1. `references/scene-craft.md`, information section: distinguish an audience mystery
   from a character-only puzzle when the viewer has already seen the whole answer.
2. `references/revision-production.md`, evidence check: a ledger/explanation cannot
   plant a prop position or mechanical cause absent from the screenplay itself.

Each raw failed-case request was then given to a **new executor with a fresh
context**, no prior answer, diagnosis or expected response, using an updated
runtime snapshot. S03's snapshot contains change 1; S04's contains both changes.
S03 was not rerun after change 2; it only clarifies the same evidence principle.
Other cases were not rerun after these two additions. Research-only expansion
changed attribution, not the initial executor's runtime instructions.

| Retest / record | Scores | Observed change / limit |
| --- | --- | --- |
| [S03 retest](evidence/S03-retest.md), [run](evidence/S03-retest-run.md) | 3/3/3/3/2/– = 14/15 | Passes scoped text review: wet display base and a cloth edge in a pre-existing tin precede disclosure; the owner opens it later and rewraps against the water. Audience has clues but not the full answer at entry; innocence/reason remain intact. No viewer-comprehension or timed performance test. |
| [S04 retest](evidence/S04-retest.md), [run](evidence/S04-retest-run.md) | 3/3/3/3/2/– = 14/15 | Passes scoped text review: fan, paper, bin and speed/direction changes appear in the screenplay before the cascade; same fan becomes paperweight. Speed variant and uncertainty stated. Fan/paper physics still need practical/animation testing. |

The S04 executor reports some batched reference output was truncated. Its record
names the files requested and acknowledges partial displayed content; no claim
that every reference reached that context untruncated is made. The initial executor
and S03 retester report reading all six guides. These are execution disclosures,
not tool-by-tool independent instrumentation. Improvement on two single samples
does not isolate the prompt change's causal effect or establish reliability.

## Actual neighboring-artifact exercise

An excerpt of the concurrently authored Storyteller S01 draft was captured
verbatim in [handoff input](evidence/handoff-input.md), including B01–B05, two
children/one planting table, its planned 45s and unapproved status. This is an
actual authored neighboring artifact, not a fabricated approved bible. The original eight-case executor then read the current runtime and that input
as a receiving Screenwriter; this was **the same context after eight cases**,
not another independent fresh-context sample. Exact
[receiver answer](evidence/handoff-receiver.md) and [run record](evidence/handoff-run.md)
are retained. Primary inspection found:

- All B01–B05 map to S010/SB01–SB05; two children, one table, no speech/VO/text,
  and unapproved status remain. No shot plan or created visual assets are claimed.
- It identifies a real incoming state ambiguity: B02 puts soil in both pots,
  B03 calls one pot empty. It offers a clearly provisional partially filled
  realization and asks Storyteller to resolve that exact fact before lock.
- It also discloses its angled-pot interpretation and asks about shared watering-can
  feasibility; it does not turn these choices into approved canon.
- Planned 45s is separated from estimated 40–55s and downstream production work.

This is a useful artifact-consumption/contract exercise. It is not a returned
Storyteller decision, bidirectional approval, multi-agent orchestration or a
successful production. The input ambiguity remains open with its narrative owner;
Screenwriter's skill creation does not depend on silently resolving it.

## Remaining verification

No performers, native-language panel, viewer study, read-through, animatic,
rendered film, provider-specific generation, paginated screenplay PDF/FDX or
actual downstream visual/audio/timeline production receiver has been tested. No empirical reliability,
measured audience impact, accessibility compliance, professional credit or
legal clearance is claimed. No global installation, commit, push or other agent
implementation is included in this task.

Accepted scope: **reviewable Screenwriter pilot for text generation/revision and
prepared production packets**, with observed failure/correction evidence. Six
initial cases meet the local rubric; S03/S04 meet it only in their retained retests.
The extra neighboring-artifact exercise preserved status and exposed a continuity
question. This is not certification that all covered specialties or neighboring
skills passed. Mystery/localization/long-form reliability and practical animation
constraints remain bounded by the research and testing gaps above.
