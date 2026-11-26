# Narrative design decisions

## Mechanism and topology

Linear/nonlinear describes event presentation; interactivity describes the
participant's influence. A nonlinear film need not respond to anyone. A linear
interactive scene can respond locally without changing the final event. Establish
who acts, what input is sensed, at what point, what changes, and feedback. Explicit
selection, behavioral triggers (e.g. exploration), and hybrids each need a real
mechanism. A vote may select one later release for a group; prerecorded alternatives
are navigable media, not per-viewer stateful adaptation.

Choose, combine or reject patterns [S01, S02]: tree (distinct routes, rapid content
growth); foldback/branch-and-bottleneck (shared events, preserve state and variants);
parallel paths (different perspectives, costly continuity); hub/spoke (revisitable
modules, ordering and repeats matter); loops (intentional repetition needs progress
or exit); storylets (eligible modules selected by state, priority/salience or user;
ordering, repetition and exhaustion need rules); open/emergent (interaction among
systems, hard to author/test, scope the simulation). These are trade-offs, not a
mandatory classification. Record node types such as scene, choice, gate, hub,
state update and ending; edges may represent selected option, automatic transition,
behavior trigger, conditional, random or return. A node may have multiple functions.

## Choices and consequences

For each choice specify available options, including nonbinary options or inaction
where meaningful, what the participant knows, intended trade-offs, what is hidden,
and feedback now and later. Informed choice needs enough legible information to
form intent, not perfect prediction; an uncertain risk can be fair if uncertainty
itself is communicated. Do not imply agency through labels leading to identical
responses unless an explicitly cosmetic choice is suitable. Local expression,
relationships or knowledge can matter without changing the global plot. Validate
that consequences are observable and causally connected [S02, S07].

Design dilemmas between credible competing values, with character motivation and
consequences, not a universal good/evil meter. Identify whose agency it is: a
character's believable decision is distinct from player control. Make hidden state
compatible with audience expectations; do not expose spoilers just to explain a
rule. Distinguish deliberate mystery from contradiction by checking what is known,
when evidence is supplied and whether a reveal can still explain it.

Start with thematic tensions and different final states if ending-first helps; work
back to enabling decisions, setup, feedback and reachable guards. Endings may be
bittersweet, ambiguous or asymmetric; do not force good/neutral/bad/secret. Test
whether outcomes feel earned and routes offer different experiences, not merely
whether labels differ. These are creative hypotheses until read or played by people.

## State and scope

Use only necessary flags, enums and bounded typed variables; record initial value,
domain, visibility, owner, lifecycle, updates and invariants. Relationship,
knowledge, inventory and time are optional dimensions. Separate canonical facts
from route-specific facts and transient state; never merge incompatible facts by
forgetting them. At a join list incoming states, required common truths and variants;
carry forward the consequential difference, or explicitly justify retirement.

Count separately paths, graph nodes/edges, reachable state combinations, unique
clips/assets/cuts and production effort. If n independent binary decisions never
merge, up to 2^n paths occur; this is not automatically 2^n nodes or clips. Loops can
make path count unbounded. Estimate story time, each clip duration, end-to-end path
and cost independently; show assumptions and uncertainty. Under budget pressure,
compare shared scenes with stateful variants, fewer bespoke routes, modular assets,
or a linear treatment; assess the lost experience and testing cost. Reuse cannot
be assumed free: list animation, edit, continuity, sound and QA work.

Adaptive/episodic systems require persistent state or an explicit recap/reset;
record episode version, import/migration, missing history/defaults and audience
entry points. Stochastic selection requires eligible set, distribution/seed policy,
priority, fallbacks and reproducibility; never call one random run exhaustive.
