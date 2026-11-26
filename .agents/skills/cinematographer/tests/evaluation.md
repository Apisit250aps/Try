# Current validation evidence

Scope: Cinematographer first implementation, 2026-11-25. This file distinguishes
authored planning outputs from deterministic checks and real production trials.
Use [scenarios](scenarios.md) for independent reruns; the
[rubric](../references/review-rubric.md) defines observable acceptance.

## Authored practice outputs

T01–T11 have concrete same-author answers in
[worked sequences](../examples/worked-sequences.md). T01 additionally has a
[complete JSON packet](../examples/silent-30s.json). These outputs exercise the
method and surface handoff/geometry/timing decisions; they were written while
developing the skill. They are not blind/independent model trials and no pass
rate or generalization score is inferred.

The T10 failure is a synthetic report, not an observed generated defect. T11 is
a semantic walkthrough using synthetic inputs, not a message or actual receiver
response. No sibling agent was started. No footage, boards, prompts executed
against a video model, timed animatic or audience result is claimed.

## Static checks actually executed

Python **3.14.7**. No repository dependency added; PyYAML/PDF inspection packages
were installed in a temporary environment. These checks passed on this package:

| Command / procedure | Observed result | Limit |
| --- | --- | --- |
| `python3 skills/cinematographer/scripts/validate_packet.py --self-test` | 3 test methods passed: valid 30 s sequence; 14 invalid mutations rejected; declared ellipsis/extra fields accepted. Six primary shots total 30 s. | Logical subset, not a complete schema or visual/timing evaluation. |
| `python3 scripts/validate_repository.py --root skills/cinematographer` | 58 inline local links/anchors, 0 errors. | Offline Markdown paths/anchors only. |
| Copy entire folder to a temporary directory; rerun link and packet checks | Passed without siblings; same 58 links and packet results. | Copy isolation, not CLI installation or discovery in another host. |
| Skill Creator `quick_validate.py skills/cinematographer` in temporary venv | `Skill is valid!` | Frontmatter/name/scaffold checks, not craft judgment. |
| Claim-ID audit across package Markdown | No undefined P01–P23 or S01–S04 claim IDs. | Does not establish the truth of claims or automate reading sources. |
| Source inspection | 22 accepted entries, with actual public-text/PDF locators and access limits. | Some ASC refetches failed; only the visible passage is evidence. No assertion every URL will remain reachable. |

The shared repository validator was also run once with `--self-test`: its 2
self-tests passed; at that snapshot it checked 444 repository links and isolated
all present skill folders, then reported **56 missing-target errors** in the
concurrently incomplete Director/Critic folders (repository and isolated-copy
reports count the same missing references twice). It reported no Cinematographer
link failures. This is an observed in-progress snapshot, not a claim about the
eventual state of those other tasks; no attempt was made to repair their files.

The initial tracked-file hash comparison detected concurrent changes outside
this task in README, CONTRIBUTING, INSTALLATION, SPECIALIST_ROADMAP and Artist's
contract. That preservation assertion could therefore not be used to certify an
unchanged whole worktree. All writes by this task were confined to
`skills/cinematographer/`; no reset, stash, commit or shared-file mutation occurred.

## Scoped manual review of authored outputs

Checked T01–T11 text against the scenario requirements: T01/T02/T03/T04 duration
allocations sum to 30/20/18/12 s respectively; T02 reciprocal look targets remain
on the south side; T03 exposes the seal after seating and before reaction; T05
labels its overlay unknown; T06 avoids mirroring; T07 distinguishes viewpoint
from magnification; T08 claims no measured exposure; T09 declares the crossing and
new side; T10 labels its failure report synthetic; T11 preserves separate beat
types and pending receipts. These are specification observations, not rubric
scores for rendered comprehension, performance or independent model behavior.

## Outstanding production evidence

- Independent fresh-brief model trials across all 11 scenarios, preserving raw
  answers and scoped rubric scores.
- Artist-rendered boards and target-size/9:16 overlay inspection, including
  asymmetric identity/prop-state checks from more than one angle.
- Mute 30-second animatic comprehension, spoken dialogue/action assembly and
  actual suspense disclosure windows; Editor-measured timing.
- Temporal test of deliberate crossing and zoom/dolly/focus distinctions.
- Bounded real AI-video generation → observed failure/diagnosis → revision;
  inspected intermediate frames/contact, actual provider capability and budget.
- Real incoming Storyteller/Screenwriter packets, local mapping, Artist/Editor /
  Sound/Director or user receipt and unresolved decisions. Draft contract inspection
  is useful compatibility evidence, not live interoperability certification.

The package can deliver researched, reviewable shot-design specifications now.
Claims of reliable visual production or professional mastery remain unproven.
