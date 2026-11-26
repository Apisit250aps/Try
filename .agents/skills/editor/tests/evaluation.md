# Evaluation evidence

Authoring date: **2026-11-26**. This package is a portable Editor skill. Evaluation
results and limits are recorded here as checks complete; scenario definitions
alone are never counted as executed tests. Only `skills/editor/` is changed.

## Evidence classes

- Research: [25 consulted sources](../research/sources.md), bounded body/section
  access and exclusions; [claim traceability](../research/notes.md).
- Static metadata: [timeline tests](test_timeline.py), source-hash comparison,
  packaging/isolated links and frontmatter. These do not prove media quality.
- Model behavior: raw requests, retained actual outputs, reviewer relationship
  and scoped scoring must be identified before a behavior claim.
- Synthetic media: actual renderer/decoder/version/commands, hashes, frame/sample
  measurements and inspected scope required; no dramatic-quality inference.
- Real production: actual footage/performance, full picture/audio review,
  calibrated color, captions/player, destination delivery and live receiver
  acceptance remain separate gates.

## Actual results

| Check | Observed result | Limit |
| --- | --- | --- |
| Timeline unit tests | 8 test methods passed; 34 invalid mutation cases rejected plus targeted sync, dissolve-handle, reveal-order, lock-version and verification-evidence counterprobes. | Metadata only; exact linear subset, no media opening. |
| Real-source mapping | Cinematographer fixture SHA-256 `bf956f2a0bb3ad2d0a8de2ec18542b20e7d10fed483d90db7a65a370bb8b54a8`; primary order, scene/typed beats, locks and estimated durations match; six events total 720 frames/30 s at 24. | Real document mapping, no produced upstream picture/audio or receiver acceptance. |
| Fresh-context model | Five actual raw briefs and outputs in [forward evidence](evidence/forward/), followed by [evaluator self-review](evidence/forward/self-review.md) and distinct [parent review](evidence/forward/parent-review.md). Parent scores 17/18, 14/15, 10/12, 14/15, 16/18; no hard failure found. | Independent response generation from development context, not a production or statistical benchmark. Initial read-time hash/model ID unavailable; scoring/coverage limits retained. |
| Development-context model | Ten [same-author responses/self-scores](author-trials.md), all at/above local text threshold; no hard failure identified in that review. | Criteria visible; no blind/independent scoring claim. |
| Silent schematic render | Actual 320×180 H.264 MP4, 720 decoded frames at 24 fps, no audio stream; geometric motion illustrates allocations, not character performance. [Media results](evidence/media/results.json). | Full technical decode; twelve sampled contact-sheet frames visually inspected. No full perceptual playback, upstream appearance/continuity or dramatic-quality pass. |
| Mixed-rate render | Actual 25 fps and 24 fps sources trimmed from nonzero source in-points and conformed/concatenated to 192 output frames at 24 fps; color join at frame 96. | Simple synthetic constant-rate sources; no VFR, nonlinear retime, real motion/cadence-quality certification. |
| J/L and sync | Separate synthetic PCM streams decoded: incoming nonzero samples `[168000,264000)`, outgoing `[0,216000)` at 48 kHz around picture change frame 96. Entry = record 84, outgoing end = 108. Separate flash frame 96 / pulse sample 192000 agree with zero computed offset. | Synthetic timing only; no speech/lip-sync, creative bridge, listening or mix-quality claim. |
| Build comparison | Corrected harness passes under Python 3.9.6 with FFmpeg 7.1 and 9.0. [Second-build report](evidence/ffmpeg7-retest-results.json). | Exact tested binaries/settings only, not all FFmpeg builds/codecs. |
| OTIO core | OTIO 0.18.1 on Python 3.9.6 wrote/read a real `.otio`: six clips, source ranges, record parent starts, custom scalar JSON metadata and 720-frame duration preserved. [Actual file](evidence/media/silent-paper-edit.otio). | MissingReference media; **no NLE import/render/receiver**, CMX EDL/FCPXML/plugin support. Python 3.14 attempts failed as below. |
| HTTP | 26 distinct source/discovery URLs checked with curl HEAD/redirects and TLS verification enabled: 25 HTTP 200, ScreenSkills 403. [Raw log](http-links.json). | Web reader separately returned ScreenSkills body. Believer body reader 403 vs curl HEAD 200 remains a discrepancy, not consulted-body evidence. Reachability is not claim verification. |
| Packaging | Repository link/self-tests, isolated-copy checks, Skill Creator validation, UI YAML, JSON/CSV parsing and whitespace scan passed at recorded runs. [Command evidence](evidence/static-checks.json). | Offline structure only; broad repo scan does not certify neighboring roles. |

The 15 actual text outputs jointly exercise all 17 scenario topics: F01→T01,
F02→T02, A01→T03, A02→T04, A03→T05, A04→T06, F03→T07/T09, A05→T08,
A06→T10, F05→T11/T16, A07→T12, A08→T13, A09→T14, A10→T15, F04→T17.
These are topic mappings, not 17 separate fresh-model runs. T12's lack of
authority and T17's explicit authority are tested in separate responses.

## Failures retained and corrected

See [observed failures](evidence/failures/observed-failures.md): initial missing
HTTP-log link; OTIO dictionary/manifest `bad any cast` failures in Python 3.14;
FFmpeg 7.1 automatic-rate mismatch (199 frames at 25 instead of 192 at 24).
Explicit output `-r 24` fixed the media harness; both binary builds were rerun.
OTIO support remains scoped to the successful Python 3.9.6 environment. Do not
call the Python 3.14 path supported or silently omit those failed attempts.

## Reproduce

From repository root, Python standard library only:

```bash
python3 scripts/validate_repository.py --root skills/editor --self-test
python3 scripts/validate_repository.py --self-test
python3 skills/editor/tests/test_timeline.py
python3 skills/editor/tests/test_timeline.py --source skills/cinematographer/examples/silent-30s.json
python3 skills/editor/scripts/validate_timeline.py skills/editor/examples/silent-30s.timeline.json
```

The `--source` comparison is optional and intentionally hash-pinned; without it
the copied package is independent. The standard library validator does not
require FFmpeg, OTIO, PyYAML or sibling packages. Skill Creator's external
`quick_validate.py` needs PyYAML; it was run in a temporary environment.

Optional media harness: explicitly provide an installed FFmpeg binary and an
environment with `opentimelineio` (tested 0.18.1/Python 3.9.6). It downloads no
tools or media and requires a **new** output directory:

```bash
python3 skills/editor/tests/run_media_smoke.py --output /tmp/editor-new-smoke --ffmpeg /absolute/path/to/ffmpeg
```

Temporary environments were `/tmp/the-stories-editor-validation` (Python 3.14,
PyYAML/imageio-ffmpeg/OTIO/pypdf) and `/tmp/the-stories-editor-otio39` (Python
3.9.6, imageio-ffmpeg/OTIO). They supplied downloaded test binaries only; no repo
dependency or global installation was changed. Final report commands retain
their original temporary paths and output hashes; matching artifacts are copied
into `evidence/media/`. FFmpeg 7.1's successful report is retained without a
duplicate set of media; that report's original test files remain temporary.

## Scope, compatibility and remaining gates

Initial worktree, hashes and current comparison are in
[worktree-scope.json](evidence/worktree-scope.json). HEAD/branch remained
`d13dc0f1ed3b0f11a5c584213131eecb1d77df53` / `main`. No commit, reset, stash,
push or global skill installation was performed. This task created only Editor.
During authoring, concurrent work added Strategist files and changed Critic
evidence; those outside-scope changes were observed and left untouched. They
are not attributed to this task or included in its behavior claims.

Shared README/install/roadmap integration remains with its owner. Current
neighbor contracts have compatible semantics and the Cinematographer example
was mapped against actual bytes, but `editor-timeline/0.1` is still a provisional
adapter. No automatic orchestrator, live dispatch, receipt or receiver acceptance
was implemented. Copy the complete Editor folder for portable use.

Real footage/performance selection, dialogue/lip sync, suspense/comedic effect,
emotional rhythm, full animation/episode continuity, generated-media defect
repair, phone-size/9:16 viewing, calibrated grade, audible mix/stems, timed
captions/player checks and actual delivery-profile compliance remain unassessed.
So do CMX EDL/FCPXML round trips and live Critic/Director revision acceptance.
The independent textual response to CR7 is **not** a real Critic approval.
These require actual authorized media, capable tools, destination requirements
and relevant reviewers; their absence does not turn into a pass.
