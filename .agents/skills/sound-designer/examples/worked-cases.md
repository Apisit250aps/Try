# Worked design cases and counterexamples

Original synthetic exercises, not approved story canon or produced audio.
Use [contract](../references/production-contract.md) semantics proportionally.

## A — Silence is an active choice

Brief: a 30-second animation shows a child restoring a wind-up bird; it must
remain understandable without sound. Proposed listening intent: care becomes
anticipation, then relief. Choose restrained contact/gear sounds with no score;
the emotional reading is a hypothesis. Do not add a spoken explanation or an
essential audio-only mechanism clue. The optional soundtrack must preserve the
silent comprehension requirement.

| Cue | Scene / shots | Plan / why | Timing and acceptance |
| --- | --- | --- | --- |
| SD-C010 | S010 / S010-SH020 | Gentle contact when toy reaches table; preserve material uncertainty until Artist reference arrives | Descriptive contact anchor, not measured; picture contact must match selected take |
| SD-C020 | S010 / S010-SH040 | One restrained winding gesture follows the one visible key turn | Exact transient position pending animatic; extra wind turns fail |
| SD-C030 | S010 / S010-SH050 | Intentional quiet during release/wait; no premature motor or score resolution | Hold as planned; don't “repair” quiet with a riser |
| SD-C040 | S010 / S010-SH060 | Small mechanical movement begins only with visible advance | Optional reinforcement; comprehension still tested muted |

Counterexample: a triumph chord at the start of the hold announces success
before the picture and removes uncertainty. Another failure is claiming
“silence tested” when only the script was read.

The [concrete adapter packet](windup-sound-packet.json) uses actual inspected
Cinematographer fixture IDs/estimated shot allocations. It includes a compact
snapshot of relevant input fields and its hash so the package has no runtime
sibling dependency. This is a text/metadata integration example, not audio sync.

## B — Hidden-source suspense with access

Brief: S020-SH010 holds on a listener facing a closed door. The source of three
knocks must remain unidentified until S030. Choose diegetic offscreen knocks
from behind the door, moderate obstruction, listener perspective inside the
room, no identifying voice or established villain motif. Leave a relative quiet
gap after knock three for the listener's reaction. Do not invent a pan direction
until geography exists; design temporal/timbral recognition that survives mono.

Caption proposal: “[three knocks behind door]” timed to the chosen events.
“[Mara knocks]” is a spoiler if hearing viewers cannot identify Mara. A caption
may need adjustment if the actual take sounds like a particular material/action;
text-only spotting cannot verify what a listener hears. Editor supplies cut
timing; Director/writer resolve any cue that changes disclosure.

## C — A line disappears under music

Brief: the critical phrase is “do **not** open it,” while a dense music accent
lands on “not.” No files supplied. Return diagnosis as a reported risk, not an
observation of played audio. Propose moving/thinning the accent or automating
music around the phrase, then targeted EQ/keyed dynamics if necessary. Protect
the negation and preserve score intent; don't simply raise the master or promise
a universal 3 kHz notch. Acceptance: with actual selected takes, a listener can
report the negation at intended level on target playback, including mono/mobile;
check codec output and captions too. All acoustic results remain not-assessed.

## D — Localization, consent and reconform

Brief: a Thai-English character says an approved name in both locales; a voice
sample is supplied for editing, no cloning consent. Create a profile and ask for
the intended spoken name/reference; offer licensed stock/human options. Do not
clone the sample. Native-language review, text approval and actual timed takes
are pending; changing spelling to force TTS pronunciation must not silently
change script/caption text.

If Editor inserts 12 frames before a phrase at 24 fps, the candidate shift is
0.5 seconds. That arithmetic is exact under the fixture assumptions, not proof
every affected cue should shift: verify anchors and any retimed/overlapping audio.
Update chosen take placement, viseme timeline offset, caption timing and stems;
remeasure changed exports. Keep cue/line IDs; increment versions. A recorded
“approved voice” label without a consent locator does not close the rights gate.

## E — One mix, two destinations

Brief: broadcast R128 linear delivery and a client-requested online profile of
−16 LUFS / −2 dBTP. Keep two profile IDs with separate spec authority, method,
tolerance and export/QC records. −23 → −16 is a proposed +7 LU change; finite
headroom and actual programme content determine whether gain alone is possible.
Do not turn up a silence-only cue, normalize each stem to the full-mix target,
or declare the online client values a YouTube rule. No media means both measured
columns stay empty/not-assessed. Creative approval does not prove either export
meets its delivery spec.
