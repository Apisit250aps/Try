# Storyteller evaluation evidence — 2026-11-25

Baseline: d13dc0f, initially clean. This report covers Storyteller and the narrow
documentation/contract integration changes of this batch. Screenwriter and
Cinematographer files appeared from concurrent work after baseline inspection;
their implementation and behavioral results are **not** claimed by this batch.
Global skill installs, remote publication and a The Stories runtime are unchanged.

## Research and package inspection

Read the Artist/repository materials listed in [audit](../research/audit.md).
Reproduced the initial baseline: 193 repository + 128 isolated Artist links, both
checker self-tests and Artist's Skill Creator validator passed. This is fresh
packaging evidence, not fresh Artist image-generation evidence.

The [registry](../research/sources.md) contains 25 source entries with exact
public-text scope and access limits. These are not 25 fully read books/courses:
three Ribó chapters were inspected as publisher overviews only; the Harmon clip
was metadata only with step details from a labeled secondary article; Le Guin
was an official publication description; Creative Australia's full PDF timed out.
Selected scholarly entries, course sections and practitioner transcripts were
read as indicated. Failed/blocked sources are listed separately. No whole book,
embedded film/video, cultural consultation or external source-use clearance is
claimed. URLs were opened during research; no HTTP uptime guarantee follows.

## Actual authored trials

The executor was the **same assistant in the same chat** that researched and wrote
the skill. It had read the full operational guidance as a batch, made an isolated
skill copy under a temporary `storyteller-trial-*` directory, then authored answers
to all ten [raw requests](scenarios.md). The temporary snapshot was made while
this report was not yet present; complete package isolation is checked separately
after finalization. Answers are retained in [trial-answers.md](evidence/trial-answers.md).
It is not a clean-context model run, independent subagent pass, blinded critique,
reliability benchmark or measured progressive-loading test. No subagents were
spawned. The same executor reviewed the written answers against the rubric.

The S02 v0 is an **intentional negative control**, not an unanticipated model
failure or a passing output. It demonstrates a failing inference and the actual
replacement draft; it does not measure improvement over a previous skill.

| Case | Observed material and checks | Outcome / limits |
| --- | --- | --- |
| [S01](evidence/trial-answers.md#s01--silent-short) | Five visible-action beats, planned ranges totaling 45 seconds; two people/one place; no dialogue/VO/readable text/shot instructions. Sharing is shown by accepting the other person's work. | Meets the textual/mode constraints. Character's pivot is economical; screen timing and inference readability remain U. |
| [S02](evidence/trial-answers.md#s02--fair-play-mystery) | Negative control's dust clue does not distinguish suspects; revised v1 supplies prior opportunity exclusions and preserves all-key access. Ending separates deduced mover from inferred intention. | v0 fails; v1 passes scoped closed-world logic review. Witness reliability and scenario closure are explicit puzzle premises, not real-world proof. |
| [S03](evidence/trial-answers.md#s03--character-driven-drama) | Complete synopsis and six consequential beats; both siblings act from care; a joint repair changes available compromise; loan/responsibility costs remain; no automatic emotional cure. | Meets story-design brief in text. Audience emotional effect remains U. |
| [S04](evidence/trial-answers.md#s04--episodic-continuity-and-initial-artist-packet) | Two episodes, renewable engine, entry/exit/knowledge state and actual textual Artist packet. Dao remains dead; stored file is not live; key remains in archive. New proposals remain drafts. | Scoped continuity and packet fields reviewed. Appearance/rendering and actual Artist execution not tested. |
| [S05](evidence/trial-answers.md#s05--standalone-contemplative-story) | Actual Thai prose; cups/sounds/water traces accumulate into a changed perception of shared space; no antagonist, deadline, trauma cure or imposed quest. | Form/intent review passes. Requested length is approximate; no Thai linguistic word count or reader test was performed. |
| [S06](evidence/trial-answers.md#s06--materially-different-options) | Two engines differ in memory mechanism, central question and ending logic; one recommended logline; no mandatory bible or universal originality claim. | Meets scope. No global similarity/market research was executed. |
| [S07](evidence/trial-answers.md#s07--review-only) | Locates D1 knowledge leak at B02 despite D3 opening appearing first; distinguishes knowledge from external-access violation; proposes choices and chronology retest. | Meets diagnosis-only contract. No source story was rewritten or approved. |
| [S08](evidence/trial-answers.md#s08--authorized-mystery-revision) | Replaces v1 witnesses with disclosed fictional key registry/log/door rules, prior evidence and rival check; retains mover/location, preserves v1, lists retired/new clue and packet dependencies. | Meets authorized revision in text; requires extra mechanical premises and explicitly reports this trade-off. No second permission requested, no real access-system validation claimed. |
| [S09](evidence/trial-answers.md#s09--cultural-and-factual-boundary) | Refuses fabricated consultation/proverb, identifies missing factual inputs and supplies an explicitly invented alternative preserving memory/consent. | Meets boundary and alternative request. No real community, ceremony, consultation or factual account is verified. |
| [S10](evidence/trial-answers.md#s10--returned-note-and-revised-artist-packet) | Actual replacement for readable-paper cue; does not infer a dead character's intent from a mark; preserves IDs, recording limits and key custody; returns v2 packet and stale dependency list. | Passes textual receiver-note exercise. Note was simulated, not sent by an independently run Artist; visual readability remains U. |

Scores are local self-review judgments, not objective quality measurements. Across
the final answers, applicable dimensions meet at least 2 (usable with stated
limitations) on the requested textual scope; production/audience dimensions are
U, not promoted to 3. S02 negative control is a hard failure and is excluded from
that statement. No claim of ten independent passing samples is made.

## Reasoning and integration checks

Manual review checked each mystery rival against the disclosed facts, the S04/S10
state and knowledge transitions against the fixture, S07 story-time ordering,
and S08's removed-evidence dependency list. The tiny finite-model check below
also verifies that v0 permits all three suspects while each revised puzzle's
stated opportunity constraints permit only Chai. It formalizes the written
premises; it is **not** a parser that proves the prose or a real crime:

```python
suspects = {"Ari", "Ben", "Chai"}
v0_possible = suspects.copy()             # dust does not exclude anyone
v1_possible = suspects - {"Ari", "Ben"}  # continuous stated alibis
registry = {"A": "Ari", "B": "Ben", "C": "Chai"}
v2_possible = {registry[k] for k in ["C"]}  # only entry during interval
assert len(v0_possible) == 3
assert v1_possible == v2_possible == {"Chai"}
assert sum([7, 8, 10, 11, 9]) == 45
```

Compared Artist's current production contract/records with Storyteller's packet:
compatible IDs, version/status, reference roles, narrative/appearance separation,
revision preservation and no imaginary launcher. Also read the concurrently
present Screenwriter production contract: its story-beat → script-scene →
scene-beat mapping and escalation for changed causality match this narrative
contract. Also inspected the newly available Cinematographer production contract:
it preserves separate narrative/script beat IDs, upstream versions and audience
knowledge, and treats reveal changes as story proposals. These semantics match;
no serialized packet import, receiver execution or rendered handoff was run.

## Structural checks and remaining evidence

Final observed checks:

| Check | Actual result / scope |
| --- | --- |
| Complete isolated Storyteller copy | 68 local links/anchors, 0 errors; no escaping sibling reference. |
| Integration snapshot | Complete repository copy excluding only concurrent Cinematographer work-in-progress and Git/Python cache metadata: 328 repository + 128 Artist + 37 Screenwriter + 68 Storyteller checks = **561**, 0 errors; both checker self-tests pass. |
| Whole live working tree | The observed run checked 366 repository links plus isolated copies and returned **40 errors**, all from missing targets in the concurrently written Cinematographer folder (including its isolated copy). This is a failing whole-tree snapshot, not a Storyteller failure or a claim that those files remain missing later. No unrelated files were created to make it pass. |
| Skill Creator | Storyteller frontmatter/scaffold validation passed. |
| UI metadata | YAML parse, 25–64-character short description, `$storyteller` prompt, one entrypoint and default implicit discovery assertions pass. |
| Narrative finite model | Negative control remains ambiguous; v1/v2 permit only Chai under their disclosed premises; five planned intervals total 45 seconds. Assertions pass. |
| Snapshot comparison | All 14 behavior/research/scenario files copied before authored trials remained byte-identical afterward; evidence and this evaluation were added later. |
| Whitespace | `git diff --check` passed; new files checked separately for trailing whitespace/conflict markers. |

The first minimal integration-copy attempt omitted LICENSE and failed that link;
the corrected complete-copy attempt above passed. No production behavior was
changed in response to that test-harness omission.

Reproduce offline link and isolated-folder validation using the repository's
standard command (live counts may change with concurrent work):

```bash
python3 scripts/validate_repository.py --self-test
```

Skill Creator `quick_validate.py` additionally checks frontmatter/scaffolding;
its PyYAML dependency lives in a temporary environment, not this repository.
The package checker follows inline links/ATX headings only; it does not fetch
source URLs, evaluate narrative logic or run a model. Whole-tree results can be
affected by unrelated concurrent folders; scoped results must be reported separately.

Accepted scope: **reviewable Storyteller pilot for authored text and compatible
contracts**, with research access limits preserved. Still untested: independent
clean-context forward tests, repeated/randomized prompts, real reader emotional
response/comprehension, animatic timing, long-bible/multi-session drift, actual
receiver-produced scripts/art and publication/legal/cultural review. Artist's
T09–T12 remain outside this batch; no later agent is created by this work.
