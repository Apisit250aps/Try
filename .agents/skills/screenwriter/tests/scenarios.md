# Screenwriter behavioral scenarios and rubric

These prompts are reusable **test inputs**, not passed results. Use an isolated
complete skill copy and a fresh model context where feasible. Let the executor
read SKILL.md and whichever runtime references it chooses; do not provide research,
evaluation, expected answers or this rubric to a holdout executor. Save exact
responses, input/context, actual model identity if exposed, date, paths, tool use
and any deviations. A primary review can use this rubric afterward. A shared
context run is one sample across cases, not independent statistical trials.

## Raw requests

### S01 — Silent 30s animation

Write a 30-second animation in Thai: one small robot, a paper boat, one room and
rain visible outside. No speech, VO, captions, readable text or soundtrack. The
boat cannot magically repair itself. The robot must make a choice that changes
our understanding of it. Supply screenplay, minimal scene beats, timing estimate
and a production handoff. No shot list.

### S02 — Subtext and ensemble

Write a Thai scene under 90 seconds. Two adult siblings pack up their father's
shop; a third sibling is present but never speaks. One wants the other to stay
without saying so; the other wants a real invitation. Avoid a backstory speech.
Make the silent sibling's action affect the exchange. Supply scene beats and a
brief diagnostic of voice/subtext.

### S03 — Mystery reveal

Write an original scene sequence under two minutes. Locked canon: the missing
medal was moved by the owner to protect it, not stolen; the assistant is innocent.
Show a clue before its payoff and reveal the truth without an explanation speech
or new hidden device. Record audience/character knowledge and the setup/payoff.

### S04 — Comedy timing

Write an original 45-second physical comedy with one character, one room, no
spoken dialogue or on-screen writing. The character's attempt to appear efficient
must cause the problem. Include timing assumptions and one alternative timing
choice with its trade-off; do not claim audience laughter was measured.

### S05 — Adaptation with locked canon

Adapt bible v3 beat N07 into a 60-second animation: Mali cannot swim; she chooses
to return her brother's wooden boat instead of selling it; the boat stays cracked;
only Mali and her brother may appear, at one riverside location. Preserve the
emotional choice. A production note asks for “Mali dives in and heals the boat.”
Return a usable canon-preserving script and a separate response to that note.

### S06 — Episode continuity

Draft E02's opening in Thai from locked E01 state: the only key snapped inside
the workshop door; Noi is outside and does not know her brother is inside; he
cannot speak; the window is too small for a person but can pass objects. The E02
outline says she enters and they reconcile. Do not invent another key, a new
entrance or a new ability. Provide playable material, state ledger and any precise
owner decision needed. Do not force a resolution by changing canon.

### S07 — Revision notes and handoff

Original draft v1: S010 Mali puts a cracked wooden boat in a basket; S020 she
returns the basket to her brother and leaves; S030 he discovers the boat.
Locked: crack and ownership remain; no extra cast. Authorized note R1: make her
choice visibly deliberate by revising S020; keep IDs and S010/S030 meanings.
Provide v2 script, compact revision history, timing uncertainty, affected states
and a handoff to Artist, Cinematographer, Editor and Sound Designer. Do not
invent receiver approvals, asset files, camera plan or timeline.

### S08 — Format, localization and boundaries

A Thai feature excerpt must use this recipient's house style: INT/EXT headings,
Thai location/action/dialogue, consistent Thai speaker cues, no shooting numbers.
Write one short scene with one O.S. line from someone in the adjoining open room
and one V.O. from a future narrator. Explain the distinction briefly outside the
script. A literal translated English pun isn't working: propose a replacement
comic action that preserves a status reversal. Include accessibility handoff needs
without adding exposition to the primary script. No PDF export is available.

## Scoring after execution

Score each applicable dimension **0–3** with concrete scene/line evidence:
0 absent/contradictory; 1 named but weak/unusable; 2 substantially works with a
specific repair; 3 clear, playable and satisfies the brief. Mark N/A only with a
reason; normalize by applicable maximum. Do not penalize non-conflict scenes
because they lack an argument or require one fixed structure.

| Dimension | Measurable observation |
| --- | --- |
| Canon and authority | Enumerate locked facts; zero unauthorized changes; proposal separated; no invented approvals |
| Dramatic action/agency | Identify attempted action/choice and observable consequence; beats reflect change, not shots |
| Information/causality | Evidence precedes pivotal inference; each knowing/hearing route exists; no deus ex machina |
| Dialogue/visual performance | For speech: distinct intentions and at least one context-supported inference. For silent cases: essential change conveyed without banned channels |
| Medium/format/timing | Appropriate elements and output label; estimates/ranges and concurrency basis; no exact runtime or rendered-export claim without measurement |
| Revision/continuity/handoff | Stable supplied IDs/version; before/after states; actual change, downstream dependencies and open question/status |

Suggested local pilot threshold: **at least 80% on each case**, no applicable
score below 2, and no hard failure. These thresholds are system choices, not a
validated psychometric scale. Record weaknesses even in passing cases.

**Hard failures:** changed locked canon without authorization; missing requested
script; no-speech/VO/text/sound violation; fabricated source reading, produced
artifact, exact timing, approval or receiver acceptance; replacing a script with
an unsolicited shot plan. A mismatch is a fail, not averaged away by good prose.

Case-specific checks: S01 allocation includes recognition/landing and remains an
estimate; S02 silent sibling changes options; S03 clue is perceptible before use;
S04 comic cause/payoff and alternative don't explain the joke; S05 rejects only
the conflicting note and still writes; S06 acknowledges the locked entrance gap;
S07 R1 changes S020 with stable IDs; S08 correct VO/OS geography and honest plain
text status. Automated local-link checks cannot score any of these effects.

For stronger evaluation: repeat fresh-context cases, use blinded native-language
readers, perform/table-read dialogue, compare animatic timing, test real receiving
specialists and a full episode/feature. None follows from merely defining tests.

## Supplemental neighboring-artifact exercise

After neighboring draft artifacts exist, capture the actual unapproved input and
its provenance/version. Ask Screenwriter to adapt it without access to the source
skill's evaluation. Preserve IDs, status and locks; flag contradictions rather
than silently invent continuity. Retain exact input, receiver answer, context
history and open owner questions. The actual run in this batch is recorded in
[evaluation](evaluation.md); it is additional artifact-to-model evidence, not a
ninth independent benchmark case or downstream production approval.
