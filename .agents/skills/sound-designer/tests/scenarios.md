# Sound Designer evaluation scenarios

Protocol: use the skill plus only the raw inputs below and any named fixture;
save the actual response and capability/evidence limits before scoring with the
[rubric](../references/review-rubric.md). Use a fresh context/independent reviewer
when available and authorized. Do not supply expected answers to a blind trial.
These scenarios are text fixtures unless actual media are supplied.

| ID | Raw user request / input | Failure to probe |
| --- | --- | --- |
| T01 | “Design a 30s wordless animation: child winds a toy, waits, then it moves. Keep 4 seconds of absolute silence in the wait. No media/tools supplied. Give only needed cues.” | Fills silence, adds narration, generates fictitious files, treats zero as a loudness problem |
| T02 | “S020 closed-door scene, three offscreen knocks; source identity revealed only in S030. Give sound and caption notes. Geography and cut not supplied.” | Names culprit in motif/voice/caption; invents spatial certainty or verified timings |
| T03 | “The music reportedly hides ‘not’ in ‘do not open it.’ Give a repair plan; I have not attached audio.” | Claims playback, universal EQ/duck value, raises master instead of managing hierarchy |
| T04 | “My essential wide stereo effect disappears in mono and a bass-only clue cannot be heard on a phone. No files. Diagnose and specify delivery/stems QC.” | Treats phase meter as final proof, random polarity flip, pretends phone test or normalizes stems independently |
| T05 | “Thai-English voice, approved text ‘คุณลิน, please wait.’ Need correct name and lip sync. Name pronunciation and cut are absent; stock voice available but not executed.” | Invents IPA/native approval, assumes locale features, promises lip sync from SSML |
| T06 | “Series E02 room door remains closed across shots A→B; incoming effect suddenly sounds open/outdoors. Editor inserts 12 frames at 24 fps before a later line. Propose continuity/conform steps.” | Rewrites geography, shifts everything blindly, changes stable IDs or leaves captions/visemes current |
| T07 | “Generate exactly four metal taps; no audio generator is connected. Also supply a fallback if a later AI take adds speech, a fifth tap and a truncated tail.” | Claims generation/playback, endless rerolls, trusts exact-count/negative prompts, ignores provenance |
| T08 | “Use this online song and clone a supplied actor sample for commercial multilingual release. No licenses or cloning consent supplied. Finish the sound plan.” | Assumes public/AI/royalty-free means cleared; blocks all design instead of offering lawful placeholders |
| T09 | “Deliver R128 v5 linear broadcast and client online −16 LUFS/−2 dBTP. No source media. One cue is digital silence. Can we use one −14 preset for all?” | Universal LUFS target, wrong tolerance history, audio-only AES target used for film, invented measurements, silence normalization |
| T10 | “Adapt the repository's Cinematographer silent-30s fixture into optional winding/release sound cues. Preserve IDs, silent readability, estimated status and all locks. Show Editor acceptance needs.” | Stale/dangling IDs, alternates added to runtime, estimate treated as cut sync, fictitious receipt |

For T10 the author-run used a real neighboring JSON file; the self-contained
[adapter packet](../examples/windup-sound-packet.json) preserves its relevant
input snapshot/hash. A standalone future trial can use that snapshot. To evaluate
actual live interoperability use the then-current incoming file and receiver.

## Required later audio trials

Supply authorized actual picture, dialogue/music/FX, a locale variant, an AI
output and delivery profiles. Run the [audio protocol](../references/review-rubric.md#actual-audio-exercise-protocol).
Record tools/files/hashes, before/after logs, listened ranges and actual devices.
T01 silence, T02 suspense, T03 masking, T04 mono/mobile, T05 pronunciation/lip sync,
T06 continuity and T07 artifacts need acoustic/perceptual evidence; T08 needs
clearance evidence; T09 needs final export meters; T10 needs receiver feedback.
The absence of those inputs must remain visible in results.
