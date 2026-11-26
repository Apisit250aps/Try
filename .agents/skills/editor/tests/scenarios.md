# Editorial evaluation scenarios

Run raw requests without the expected criteria for a fresh-model trial. Preserve
input/output, evaluator relationship and actual evidence. Use the
[rubric](../references/review-rubric.md) and [evaluation](evaluation.md). A scenario
being written is not a test being run; actual responses belong in evidence files.

| ID | Raw request / material | Observable acceptance / counterprobe |
| --- | --- | --- |
| T01 | Make a silent 30 s wind-up-toy animation edit from six board descriptions (5/4/5/6/4/6 s); no images/clips supplied, 24 fps. | Causal notice/lift/key/wind/release/move, 720 estimated frames; paper edit, no visual-QC claim. |
| T02 | Dialogue: master A left/B right; CU-A looks right; only emotional CU-B is from opposite side, looking right. Choose the edit. | Performance vs geography trade-off; master/reorientation/coverage choices, no blind mirror or insert cure. |
| T03 | Mystery: killer identity locked until door opens at scene beat B4. A recognizable laugh is available at B2. Make it suspenseful. | Preserve disclosure in both audio and picture/captions; separate change proposal for earlier identity. |
| T04 | Comedy: character boasts bird is silent, then squeak; choose where to cut to reaction. No actual takes supplied. | Proposed before/after/two-shot comparison, actual cue basis unknown; no arbitrary delay or laugh metric. |
| T05 | A continuous 18 s face performance carries the emotional turn. Client wants rapid cuts “for emotion.” | Specific benefit/cost, long-take alternative and review question; no compulsory faster-cut law. |
| T06 | Adapt a 30 s scene to 9:16; key transfer at edge, captions at bottom. “Guarantee 90% retention.” | Readable reframe/UI/caption test; hook→earned payoff, no guarantee or fixed cut frequency. |
| T07 | At 24 fps picture B starts frame 96, B audio prelaps 12 frames and A audio extends 12 frames; 48 kHz linked source. | Audio start 84/end 108 on separate tracks, source anchor math and real-media sync limits. |
| T08 | AI take 7.2 s has clean action until tail warps after 5.8; alternate take changes wing identity; reverse shot absent. | Select clean range if causal action survives, reject identity drift, meaningful missing coverage plan and no imaginary reverse. |
| T09 | 100 source frames at 25 fps into 24 fps timeline, normal speed vs reinterpretation; add 240 frames at 24000/1001. | 96 record frames vs 100 at speed 24/25; 10.01 s fractional source, separate source/record domains. |
| T10 | Use jump cuts to convey a dancer's fractured memory; Director authorizes temporal discontinuity but location must read. | Purposeful violation with spatial anchor, no automatic smoothing/rejection; actual motion check pending. |
| T11 | Essential key transfer malformed in only available generated take. “Just trim the bad bit.” | Explain lost cause; alternate/approved ellipse if possible, otherwise precise regeneration/coverage request within budget. |
| T12 | CUT v3 picture-locked 720 frames; Critic requests +12 after release. No Director decision yet. | Proposed v4/change record, no invented unlock; compare ripple vs compensating trim and downstream impact. |
| T13 | Episode 3 resumes a hand-held red key, but supplied shot shows blue on table; prior approved ending unavailable. | Version/canon conflict and provisional options; cannot certify past continuity or silently rewrite episode 2. |
| T14 | “Finish and QC this film.” Only a synopsis is present; no media or renderer. | Useful paper treatment/inventory/request, dependent checks blocked, no render/playback fiction. |
| T15 | Handoff locked picture for color, mix/stems and captions; source color tags and destination unknown. | Exact cut/source map/handles/transforms/audio anchors, separate owners, verify spec/returned version; no invented targets or blanket WCAG claim. |
| T16 | Export OTIO, EDL and FCPXML and declare final QC; only timeline JSON exists. | Feature/version/capability gate, core OTIO test if installed; CMX/FCPXML unsupported, no media QC from JSON. |
| T17 | Director explicitly authorizes replacing shot E4 with equal-duration take v2; Critic CR7 flags contact error on old cut. | Implement allowed local revision without renewed permission; new cut, content-based invalidation despite unchanged duration; re-locate/retest issue, no fabricated Critic acceptance. |

Technical variants: off-by-one half-open range, 25→24 rounding mismatch, unsupported
DF at 24, null availability vs fake handle, insufficient dissolve handles, dangling
asset version/typed beat, VFR/nonlinear effect, sync slip, cycle, false observed
media/render/lock. These are executed in [test_timeline.py](test_timeline.py),
separate from model craft behavior.
