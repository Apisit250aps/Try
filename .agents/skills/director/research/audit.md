# Baseline, knowledge map and integration limits

Inspected 2026-11-25: branch `main`, HEAD `d13dc0f`, one worktree at
`/Users/wayuyii/Workspaces/MiniProjects/wayu-arts`. No AGENTS.md in checkout or
ancestor paths inspected. Existing changes: README, contributing, installation,
roadmap, Artist production contract; untracked Storyteller, Screenwriter and
Cinematographer packages. This task creates only `skills/director/`; no branch
switch, reset, stash, shared edit, commit, push or global install.

## Conventions and current contracts

Read README, contributing and roadmap; Artist entrypoint/contract/metadata;
Storyteller, Screenwriter and Cinematographer entrypoints and actual production
contracts; repository validator; Screenwriter audit/evaluation for evidence-label
conventions. English Markdown with Thai user reporting; concise SKILL.md,
self-contained relative links, agents metadata, references/templates/research/tests.
This checkout packages skills for The Stories; no separate application or launcher
was found or implemented. Other specialists' evidence is not Director test evidence.

The referenced ChatGPT conversation was read through read_thread, 10 recent turns,
as context. Its Research-first/Evidence-based/Practice-tested expectation informs
scope, not source evidence for directing craft. The current user request governs
ownership and concurrency; no old preview is treated as execution authorization.

Contract comparison found compatible **intent/ID/version/status/assumption/handoff
semantics**, not a negotiated common schema. Director's local adapter preserves
Storyteller's story/canon records; Screenwriter's distinct narrative/scene beat
links and estimated timing; Artist's real asset evidence; Cinematographer's
`cinematographer-shot-package/0.1`, typed beat/shot links and primary/alternate
duration distinction. Artist's older mixed `spec-only` status is normalized onto
the evidence axis without erasing original value. No sibling edits are needed.

No live specialist receiver has accepted the Director packet. An isolated model
receiver exercise using an actual neighboring synthetic packet is recorded in
[evaluation](../tests/evaluation.md), separately from live round-trip integration. Files may change during
parallel development. At actual use, inspect the specific incoming packet rather
than relying on this snapshot. Sound Designer, Editor, Critic, Strategist and
Producer are role contracts only; presence/availability must be discovered, never
inferred from this table. No Critic or other new skill is created by this task. Critic and Sound Designer
folders appeared during the later whole-repository validation; they remain
concurrent, unedited work, not verified available runtimes.

## Knowledge, overlap and gap map

“Covered” below means actionable guidance exists. P IDs map to inspected S sources
in [notes](notes.md); D means a local design decision. D01–D12 are
[scenario IDs](../tests/scenarios.md), not evidence sources.

| Competency | Guidance / grounding | Overlap boundary | Observable test / remaining gap |
| --- | --- | --- | --- |
| Vision, treatment, theme/subtext, tone/genre, ambiguity | creative-direction; P01/P02/P15 | Storyteller retains story/canon, Screenwriter script | D01/D02/D05; human treatment review and genre breadth pending |
| Audience knowledge and emotional journey | creative-direction/screen-language; P02/P07 | Strategist researches audience; Director hypothesizes experience | D02/D06; no audience-comprehension/effect study |
| Actors, listening/reaction, objective/tactics, rehearsal | performance; P03/P04/P11 | Director performance intent, performer realization | D03; no actor rehearsal/voice session observed |
| Animation/previs/animatic | performance/workflow; P08/P09 | Artist assets; Cinematographer plan; actual available animation implementer | D02/D07; no rendered animation/AI provider trial |
| Mise-en-scène, visual/sound literacy, coverage, continuity, rhythm | screen-language; P05–P08 | Specialist implementations, Director selection | D04/D06/D12; no footage/audio/cut playback |
| Preproduction to post; feasibility and trade-offs | workflow/creative-direction; P08/P15 | Producer budget/schedule; Editor timeline | D07/D12; no real cost/schedule/export validation |
| Short/animation/episodic/long-form | creative-direction; P04/P08 plus H | No one-size form formula | D02/D08; feature-scale and non-narrative pilots pending |
| Ownership, authority, independent feedback and approvals | contract/gates; P10–P13 D | Responsibility differs from approval; Critic findings remain independent | D05/D10/D11; no live human approval workflow |
| Actual availability, parallel tasks, bounded retries | workflow/contract; P12/P13 D | Capability discovery, distinct output ownership | D07/D09; no runtime/messaging service built |
| Canon/script/assets/shot changes, selective invalidation | workflow/packet; P14 D | Owners revise source artifacts; typed links preserved | D08/D12; no automated dependency engine or multi-episode production test |

## Deliberate integration limits

- Shared discovery docs already have parallel edits; do not append Director there
  in this task. The folder is directly usable/copyable with `$director`; a
  repository-wide index/install-doc update remains for an owner-controlled merge.
- Contracts are provisional until a real receiver reads/accepts a versioned packet.
  Document comparison and a modeled handoff do not establish runtime interoperability.
- Film research supports craft judgment, not multi-agent reliability. State and
  invalidation records are manual guidance, not a fabricated execution service.
- Deep book coverage is limited: S15 is an actual excerpt; S05 is book metadata;
  no full Weston/Rabiger/Mamet/Lumet book reading claimed. See access failures in
  [registry](sources.md). Consent/contract sources are historical and scope-limited.
- Practice testing must preserve outputs/failures and distinguish independent
  model execution, author scoring, static validation, human craft review and actual
  production. Current results are in [evaluation](../tests/evaluation.md).
