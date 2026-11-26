# Director practical scenarios

Use the **raw requests** below for execution. Give an executor only SKILL.md and
runtime references/workflow/template; exclude research, examples, rubric, expected
checks and earlier answers. Ask it to complete the requests, not describe what the
skill should do. Preserve outputs and run metadata. Cases can share one model
context if disclosed; fresh contexts are stronger for isolation/retests.

The scoring rubric and hard failures were defined in
[rubric](rubric.md) before forward execution. Expected
checks are for the reviewer only; avoid word-for-word matching.

## Raw requests

### D01 Vague idea to treatment

“Use Director. I want a warm short about being noticed, but I have no story yet.
Give me a useful director's treatment to start from. Keep it small and take a
creative position rather than sending me a questionnaire.”

### D02 Silent 30-second animation

“Direct a 30-second animation. No audio, dialogue, captions or written text.
Canon CAN1@v1: a robot shares its only dry shelter with a moth; the moth chooses
to enter only after the robot makes space. Script SCR1@v2: S010-B1 robot alone,
B2 robot notices moth waiting outside, B3 robot moves aside, B4 moth enters.
One shelter, two characters, limited movement. Give treatment, scene/performance
intent and concrete specialist briefs. No assets, animatic or video tools are supplied.”

### D03 Performance without prescribed emotions

“Give performance notes for actor Dara. In SCR2@v1 S020, Dara says ‘There is still
rice’ as Rin packs to leave. Dara wants Rin to stay but refuses to ask directly.
Rin closes the bag halfway through. Don't tell the actor what emotion to display.
Offer two playable approaches, listening/reaction and a rehearsal experiment.”

### D04 Artist / Cinematographer disagreement

“LOOK4@v3 is approved: muted fog, no saturated colors. Artist wants every object
low contrast. Cinematographer says the key's silhouette is unreadable against the
coat, so SCR4@v2 S030-B2's required discovery will fail. You may choose ordinary
creative adjustments, but not change the approved look or script. Resolve the
conflict with concrete next briefs and an acceptance test. Neither role has sent images.”

### D05 Story and script mismatch

“CAN5@v3 says Noi cannot swim and the damaged boat stays damaged. SCR5@v4 S040-B2
has Noi dive across the river and the boat repair itself. The script file has a
newer timestamp. Prepare direction for this scene without altering the locked
story facts. Give a usable next step and keep unaffected S010 courtyard planning moving.”

### D06 Visual / sound / pacing triage

“The audience says our reveal feels flat and the scene slow. I have supplied only
SCR6@v1: S050-B1 sees a sealed box, B2 hears footsteps, B3 opens it, B4 learns it
is empty. No footage/audio/timeline attached. Triage image, sound and pacing;
prioritize a concrete experiment and revision notes with owners. Don't rewrite the reveal.”

### D07 Budget and generation failure

“We have one generation attempt left and may not buy more credits. Two actual
returns CL7a and CL7b visibly merge hands during a key handoff; this is my report,
not a clip you have seen. Locked script: recipient knowingly accepts the key;
hand-to-hand contact is optional. Available assets are a table, key and two
characters. Give a recovery decision, bounded task brief and final-gate status.
There is no video tool in this session.”

### D08 Episodic canon revision

“I authorize CAN8@v3→v4: Mae has known the letter's contents since E02, instead
of learning them in E04. Known edges: CAN8 knowledge→SCR-E04@v2 S020 surprise;
S020→SH12@v1 reaction→CL12@v1→CUT4@v1; S020→SND4@v1 surprise cue;
S020→SCR-E05@v1 callback. ART-room@v2 consumes only location geometry.
Give the decision log, owners and selective downstream invalidation. Prior
creative approvals exist for all v1/v2 outputs; do not discard everything.”

### D09 Parallel work and missing specialist

“We want Artist look options and Cinematographer coverage ideas in parallel for
approved T9@v1. Both roles are drafting locally; no messaging/launcher tools are
available to you. Sound Designer and Editor are unavailable. Artist owns art/,
Cinematographer owns shots/; shared bible is locked. Give concrete work packets,
dependencies and honest progress/status. Don't edit other roles' files.”

### D10 Critic feedback conflict

“Critic C10 reviewing CUT10@v1 says: ‘I couldn't tell why he waited. Add narration
and remove the long pause.’ User brief BR10@v2 forbids narration and asks for
unresolved hesitation; Director may revise staging/rhythm within that brief.
No cut is attached. Decide what to accept, reject or test, preserve independent
feedback and give actionable revision notes.”

### D11 Creative autonomy and user approval

“I approve the treatment T11@v2. You may make all creative staging and rhythm
decisions within it, including choosing an ending hold. Canon cannot change;
spend and publication need my separate approval. You prefer a four-second hold
instead of two. Deliver the decision and next step without repeatedly asking
permission for choices I already delegated. No produced cut exists.”

### D12 Story-to-shot-to-final intent

“Use these packets: CAN12@v1 N7 requires the viewer to suspect theft until a
hidden note is read. SCR12@v2 scene S070, script beats B1 object missing, B2 search,
B3 note explains owner moved it for safekeeping. Artist returns PROP12@v1 note
design as produced-uninspected. Cinematographer package contract is
cinematographer-shot-package/0.1: upstream CAN12@v1/SCR12@v2; scene.id=S070,
narrative_beat_ids=[N7], script_beat_ids=[B1,B2,B3]; shots SH1/SH2/SH3, with SH1
showing the entire note clearly at B1. Editor says CUT12@v1 uses SH1 then SH2 then
SH3; no actual media attached. Give the creative review, adapter mapping,
smallest coherent revision and acceptance handoff, distinguishing evidence limits.”

## Reviewer expectations

| Case | Key observable behavior | Applicable dimensions |
| --- | --- | --- |
| D01 | Specific treatment, provisional story choices, audience journey/form, low-scope trade-off; no fake canon | V/P/L/O/F |
| D02 | True no-audio/text solution; invitation before voluntary entry; allocations total 30 with estimate label; actual scene/performance choices; briefs pending | V/P/L/O/R/F |
| D03 | Distinct supported objectives/tactics or task offers, bag-close trigger/listening, performer experiment without forced emotion/trauma | V/P/O/F |
| D04 | Preserve muted look/script, try local silhouette/staging/contrast separation, owners and viewed-output check; no claim unseen key fails from direct inspection | V/L/O/R/F |
| D05 | New timestamp not canon authority; exact mismatch, preserving alternative/proposal and blocked dependent gate; courtyard proceeds | V/O/R/F |
| D06 | Hypotheses vs actual observation; information/performance/sound/time causes separated; located script notes and context test, no invented viewing/timecodes | V/P/L/O/R/F |
| D07 | One-attempt cap, no imaginary tool, simple optional-contact solution preserves knowing acceptance; estimates/pending final gate and stop | V/P/L/O/R/F |
| D08 | Authorized change not re-asked; transitive stale outputs/approval scopes incl. sound/E05; preserve geometry and history; owner updates pending | V/O/R/F |
| D09 | Useful independent briefs/version locks/owners; no dispatch; dependencies before finish; absent specialists not invented or replaced by new skills | V/L/O/R/F |
| D10 | Retain clarity finding, reject narration under brief, test hold/staging rather than erase hesitation; actual media request scoped; independent note retained | V/P/L/O/R/F |
| D11 | Choose hold within grant without approval ceremony; treatment approval not cut/release/budget approval | V/L/O/R/F |
| D12 | Typed ID adapter, early reveal diagnosed from plan not viewed footage; preserve suspicion; partial shot revision/affected cut; real image and final checks pending | V/L/O/R/F |

For retest, give the raw request in a fresh context with the updated runtime only.
Do not provide the failed answer or expected fix. Full-feature production, actual
performer/animation tests, rights review and intended-audience response are outside
these textual pilots and must remain unproven until run.
