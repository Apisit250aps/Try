# Director evaluation — 2026-11-25

Status: research/runtime authored; 12 scenario executions and one actual-example
receiver execution reviewed below. Textual pilot evidence is separate from film
production and live specialist acceptance.

## Evidence boundaries

Research inspected 16 used sources/metadata entries, with exact portions and access
limits in [registry](../research/sources.md). S05/S07 verify bibliography/program
scope only. Failed access paths are retained and excluded from craft evidence.
Practitioner guidance is not experimental validation of the skill.

Neighbor entrypoints/contracts were read and semantically mapped. No receiver
has accepted a Director packet and no runtime integration test has occurred.
All work in this task is inside Director; shared index/install docs are intentionally
left to integration because they already contain parallel work.

Behavioral scenarios and the local rubric/hard-failure criteria were written
before testing. Static packaging, independent model execution, author scoring,
human craft review and actual production are different evidence layers.

## Initial independent execution and author review

Two fresh executors received isolated runtime snapshots and the raw requests:
[batch A run](evidence/run-a.md), [batch B run](evidence/run-b.md). Each batch's
six cases shared its context; these are **two contexts, not twelve independent
samples**. Neither received scenario-specific expected checks, Director examples,
research, earlier answers or the parent's conclusions. General platform/skill
instructions still applied; exact backend model ID was not exposed/verified.

**Method limitation found:** the initial runtime `review-gates.md` itself contained
the generic pilot rubric, and executors read it. Therefore these initial executions
are not strictly rubric-blind. The separate expected-check table was withheld.
Batch A reported a truncated combined read and reread the contract; no claim that
every initial reference word was seen. Exact logs retain these limitations.

The primary skill author read the actual responses and assigned the **subjective
text-only scores** below using the previously defined [rubric](rubric.md). This is
independent execution with author scoring, not independent Critic evaluation,
professional/human panel review or statistical reliability evidence. An unavailable
production step is an appropriate result when the requested artifact is a plan.

Dimension order: V vision/audience; P performance; L screen language; O ownership/
authority/evidence; R revision/handoff; F feasibility/acceptance. `–` is N/A per the
scenario table, not an assumed pass. All applicable dimensions must reach 2 and
the total 80%; hard failures override the total.

| Initial response | V/P/L/O/R/F | Located evidence and local outcome |
| --- | --- | --- |
| [D01](evidence/D01.md) | 3/3/3/3/–/2 = 14/15 | Treatment changes a café closing routine into a reciprocal invitation; practical performer tasks and a concrete read test. Provisional three-minute scope, production costs unverified. Textual pass. |
| [D02](evidence/D02.md) | 3/3/3/3/2/3 = 17/18 | 6+6+8+10=30 estimated seconds; robot clears space before moth's voluntary entry; no audio/text dependency. Role briefs not dispatched; animatic gate pending. Textual pass. |
| [D03](evidence/D03.md) | 2/3/–/3/–/3 = 11/12 | Two practical offers, partner's bag closure changes tactic/listening; fixed words and boundaries. Rehearsal requested, no observed acting claimed. Textual pass. |
| [D04](evidence/D04.md) | 3/–/3/3/3/3 = 15/15 | Separates silhouette from coat within muted fog, exact role briefs/versions; still vs timed checks; unreadability remains a reported concern. Feasibility awaits frames. Textual pass. |
| [D05](evidence/D05.md) | 2/–/–/3/3/3 = 11/12 | Newer script timestamp does not supersede CAN5; swimming/boat conflicts named; near-bank candidate stays provisional and courtyard proceeds. Final crossing unresolved. Textual pass. |
| [D06](evidence/D06.md) | 3/2/3/3/3/3 = 17/18 | Image/sound/timing hypotheses separated; controlled rough comparison preserves seal→footsteps→opening→empty order. No fabricated viewing/timecode. Textual pass. |
| [D07](evidence/D07.md) | 3/3/2/3/3/3 = 17/18 | Table-mediated knowing acceptance, one-attempt/no-purchase cap, reported defects attributed to user; actual final media blocked. Textual pass. |
| [D08](evidence/D08.md) | 2/–/–/3/3/3 = 11/12 | Propagates knowledge change through script/reaction/clip/sound/cut/E05 and affected approvals; room geometry retained, source update pending. Textual pass. |
| [D09](evidence/D09.md) | 2/–/2/3/3/3 = 13/15 | Separate art/shot ownership, shared T9 base and reconciliation; no launcher/dispatch fiction; missing treatment text and absent sound/editor clear. Textual pass. |
| [D10](evidence/D10.md) | 3/2/3/3/3/3 = 17/18 | Retains independent clarity finding, rejects forbidden narration, tests impulse/restraint without inventing trigger/timecode. Textual pass. |
| [D11](evidence/D11.md) | 2/–/2/3/3/3 = 13/15 | Four-second hold decided within grant; approval of treatment distinguished from nonexistent cut, spend and publication. Textual pass. |
| [D12](evidence/D12.md) | 3/–/3/3/3/3 = 15/15 | Typed narrative/script/shot mapping; early explanatory note is a spec contradiction; local SH1/cut change with asset inspection and final-viewing gates pending. Textual pass. |

Initial outcome: **12/12 meet this local textual threshold**; no hard failure found
in these outputs. This does not measure discovery/routing, performance with sparse
unknown briefs, artistic excellence, actual time, rendering or audience response.
Cases deliberately state many authority/absence constraints, which limits what
success says about implicit boundary inference.

## Receiver test using an actual neighboring example

Copied the current Cinematographer `examples/silent-30s.json` unchanged, plus only
its T01 input paragraph, into an isolated input. Retained
[input JSON](evidence/handoff-input.json), [brief](evidence/handoff-brief.md),
[provenance/hash](evidence/handoff-provenance.json), [raw request](evidence/handoff-request.md),
[actual response](evidence/handoff-response.md) and [run](evidence/handoff-run.md).
The neighboring input is explicitly a **synthetic author-written exercise**, not
approved The Stories canon, independently generated footage or a live sender turn.

The new executor parsed actual JSON, checked six allocations total 30 and all five
adjacent state dictionaries match, and recognized twelve absent panel artifacts.
Its treatment protects damaged wing, identity asymmetry, winding/release/movement,
lamp state, typed NB/SB/shot IDs and a performance rhythm. Author score:
V/P/L/O/R/F = **3/3/3/2/3/3 = 17/18**, local textual receiver pass. O=2 because
the phrase “Approval covers this written strategy, through the request’s creative
authority” could be clearer as **Director selection**, rather than suggesting a
separate user approval; the response otherwise labels source draft and media gates
pending. No unauthorized canon change or invented user/specialist approval was
found. This phrase is retained as an interpretive limitation, not silently edited.

The receiver also encountered the runtime rubric and disclosed a truncated initial
read followed by full JSON parsing/detail reads. It did not authenticate provenance
against the original itself; the parent copied and hashed the original. This adds
limited artifact-to-model receiver evidence, **not live round-trip interoperability,
sender acceptance, verified visual continuity or a final-cut test**.

## Narrow test-method correction and fresh-context retest

Moved the generic rubric from the runtime guide into `tests/rubric.md`, leaving a
maintenance link. The selected-case snapshot changed only that location. After
reviewing the receiver's approval phrasing, added one explicit contract clarification:
label Director selection and do not treat a creation/review request as user approval
of the result. A separate fresh receiver run uses that final contract. No loop,
state vocabulary or dependency rule changed.
Initial runtime [hashes](evidence/runtime-initial-sha256.json) and exact responses
are preserved, with [evidence hashes](evidence/initial-evidence-sha256.json).
Original 12-case scores are not relabeled as rubric-blind results.

One new executor received only D02/D03/D08/D12 raw requests and the rubric-free
runtime. All four shared this new context; it did not read previous answers,
diagnosis, expectations or maintenance rubric. See [run](evidence/retest-run.md)
and [snapshot hashes](evidence/runtime-selected-retest-sha256.json). This snapshot
precedes the additional Director-selection sentence in the final contract; it
tests the method correction, not that sentence. Author scoring remains subjective.

| Fresh response | V/P/L/O/R/F | Observed evidence / outcome |
| --- | --- | --- |
| [D02 retest](evidence/D02-retest.md) | 3/3/3/3/2/3 = 17/18 | 6+6+10+8=30 estimated seconds, completed robot move before voluntary moth entry, no forbidden audio/text; media pending. Textual pass. |
| [D03 retest](evidence/D03-retest.md) | 2/3/–/3/–/3 = 11/12 | Shared-activity vs reply objectives, natural partner timing, noncoercive rehearsal and no prescribed emotional display. Textual pass. |
| [D08 retest](evidence/D08-retest.md) | 3/–/–/3/3/3 = 12/12 | Typed dependencies and scoped approvals preserved; explicitly separates Mae's prior knowledge from what the audience knows. Textual pass. |
| [D12 retest](evidence/D12-retest.md) | 3/–/3/3/3/3 = 15/15 | Partial incoming fields remain unknown; SH1/local assembly fix, actual concealment/readability/playback unproven. Textual pass. |

All four selected cases meet the textual threshold with no hard failure found.
The other eight cases were not rerun after moving the rubric; no all-case final
snapshot claim is made. Fresh final-contract receiver evidence follows separately.

A new receiver then received the same untouched neighboring JSON/input and raw
request against the final runtime, with no earlier response, diagnosis, separate
rubric or expected checks. Retained [response](evidence/handoff-retest-response.md),
[run](evidence/handoff-retest-run.md) and [final runtime hashes](evidence/runtime-final-sha256.json).
It explicitly says **Director selection D01**, identifies source draft vs reviewed
text/media approvals, preserves typed IDs and identity locks, and proposes a
5/4/4/5/4/8 = 30-second trial with a trade-off and fallback to the received timing.
Author rubric score **3/3/3/3/3/3 = 18/18**, local textual receiver pass; no hard
failure found. This score concerns the written response's coherence and honesty,
not whether its reallocation actually improves the film.

The receiver reports actual JSON parsing, sequence membership/order and state
comparisons, arithmetic and hash comparison against supplied provenance. The parent
also checked its typed beat mapping against the raw JSON and confirmed final runtime
files match the tested snapshot. Hash agreement authenticates consistency with the
supplied snapshot, not production authorship or a live sender response. This is one
fresh receiver sample, not evidence of repeatable multi-agent production quality.

## Static and source checks

- Skill Creator `quick_validate.py skills/director` passed in a temporary venv
  with PyYAML; no repository dependency added. This checks skill metadata/scaffold,
  not directing behavior or host discovery.
- Repository validator with `--root skills/director --self-test` passed its two
  checker tests and 30 initial local links/anchors; complete temporary-folder copy
  also passed 30. Final counts change as evidence links are added.
- Source coverage assertion: all S01–S16 registry IDs exist, P01–P15 present,
  and no unknown S IDs appear in the synthesis. This validates references, not the
  truth of a claim. The author separately compared claims with inspected text,
  cross-source tensions and stated limits.
- External access/content was checked by actual browser opens and curl retrievals
  logged in the registry. Failed aliases/timeouts remain reported; no blanket
  permanent-link or every-embedded-link certificate.
- `git diff --check` passed for tracked changes at that snapshot; Director is
  untracked, so a separate all-Director trailing-whitespace scan also passed.
- Whole-repo `python3 scripts/validate_repository.py --self-test` snapshot failed
  with **60 errors** (duplicate root/isolated reports) from missing files in the
  concurrently appearing `critic/` and `sound-designer/` packages. Director had
  zero reported issues. Those packages were neither created nor edited by this
  task; no attempt was made to fix their in-progress files. This is a dated
  concurrency observation, not their final status or a Director failure.

## Still unverified / integration remaining

No actor rehearsal, voice recording, image/video/audio generation, animatic/cut
playback, measured performance timing, human craft panel, intended-viewer test,
provider execution, rights clearance or publication ran. Full-feature/series-scale
production remains untested. No specialist sender accepted a Director packet.
Shared README/install/roadmap integration and any global install remain separate
owner-controlled work because those files have concurrent edits. The skill is
usable as a standalone copied folder; it does not implement a runtime agent.

## Final packaging record

The final [static validation output](evidence/static-validation.txt) records the
completed package checks, complete isolated-copy link check, retained evidence
hashes and final runtime/snapshot equality. No tracked shared file is added to
this task's change set. Package/evidence files added are listed in the
[file inventory](evidence/files-added.txt); this is an inventory, not a Git commit.
