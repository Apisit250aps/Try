# Research synthesis and claim-to-source traceability

Research-first sequence: inspected current repo/contracts → opened sources and
bounded consulted sections → mapped competencies/gaps → wrote actionable skill
and tests. Access details/limits belong to the [registry](sources.md); coverage
and overlap belong to [audit](audit.md). A source listing is not evidence of
reading its linked books/videos. No craft principle becomes a technical standard
because it appears in this skill.

| Claim | Evidence class / sources | Observation → Editor decision | Runtime application / test |
| --- | --- | --- | --- |
| P01 Grammar and information | H/C; S01 | Editing creates spatial/temporal/associative relations. Local synthesis: motivate devices with information/state changes instead of a transition menu. | Editing craft; T01–T03/T10. |
| P02 Rhythm beyond cut frequency | H; S03 | Companion prose distinguishes timing/pacing/phrasing and movement across shots. Local synthesis tests holds and contrast at several scales; no universal interval. | Craft/format reference; T04–T06. |
| P03 Performance/listening selection | H; S02 | Interview discusses shifting attention during dialogue, performance-led rhythm and script timing. Preserve listening turns and label script timing estimates. | Selects, dialogue, long-take alternatives; T02/T05. |
| P04 Animation editorial begins early | C/H; S06–S08 | Professional descriptions and panel account place editorial across production, including boards and replacement stages. Version each replacement and re-evaluate timing. | Workflow, animatic example; T01/T13. |
| P05 Continuity is contextual | E abstract + H; S10/S01 | Edit-detection study reports task-specific continuity-related blindness; guide discusses intentional discontinuity. This does not establish dramatic or retention superiority. | Compare intended disorientation with clarity needs; T02/T10. |
| P06 Exact clocks and DF labels | T/standard; S11/S12 | Fractional playback rate, counting compensation and source display differ. Local record uses rational arithmetic and separate origins; no timecode serializer promised. | Time/media, validator; T09 and mutation tests. |
| P07 Proxy vs original evidence | T/H; S14/S22/S02 | Proxy workflows and proxy-export setting require actual relink/export checks; historical interview notes preview-scale limits. | Ingest/conform/QC; T15. |
| P08 J/L and sync | T definitions + local design; S13 | Offset picture/audio boundaries deliberately while preserving source sync. Anchor/tolerance/check record is our design, not an Adobe schema. | Timeline and worked J/L; T07. |
| P09 Rate conversion vs retime | T; S15 | Avid documents project-rate adaptation for mixed-rate clips. Distinguish cadence conversion from reinterpretation; arithmetic example is independently derived. | Time/media; T09 and rate tests. |
| P10 Interchange limits | T; S16–S18 | Tracks/ranges/transitions and native vs plugin adapters have defined but limited semantics. Validate actual serialization/receiver behavior per feature. | Timeline contract; OTIO smoke, T16. |
| P11 Executable timestamp handling | T; S19/S20 | Trim does not reset timestamps; concat and cadence/stream selection need explicit treatment. Test actual binary output, not just command syntax. | Finishing; synthetic media smoke. |
| P12 Color and delivery interpretation | T; S21/S22; S23 listing route only | Source/working/output interpretation and format-specific export options matter. Destination profile and calibration evidence remain project-specific. | Finishing/handoff; T15/T16. |
| P13 Accessibility | T/guidance; S24 | Captions need speech and relevant nonspeech content with verified accuracy. Review automatic captions, timing and actual player placement. | Export/QC; T06/T15. |
| P14 Scope of practitioner evidence | H/context; S09 and registry limits | A festival report, author hypothesis or training listing is not a full lecture, controlled experiment or completed exercise. | Evidence labels throughout; evaluation gates. |
| P15 Timeline and validator | **D**, user scope + inspected neighbor contracts; S11/S16–S18 inform time/range semantics only | Local schema, half-open convention, strict available-range check, typed IDs, statuses, linear subset and exactness are implementation choices. | Contract/example/validator/tests. |
| P16 Ownership/workflow/revision | **D** user/repo + H S04/S05/S25 | Explicit role boundaries and selective invalidation implement this project's grant. Practitioner collaboration/episode insights inform craft, not authority. | Production/workflow/lock records; T12–T17. |
| P17 AI defect decisions | **D** local risk policy derived from requested failure cases | Observe clean ranges, identity/contact across generations, choose trim/alternate/regenerate by protected function and available media. No model capability is assumed. | AI reference, selects; T08/T11. |
| P18 Rubric and acceptance | **D** local test design | 0–3 dimensions, ≥80% scoped threshold and hard gates are chosen for this package; not an industry or empirical quality scale. | Review rubric, scenarios and actual run evidence. |

## Synthesis notes

**Craft:** choose a cut because the audience needs a new relationship, inference
or performance emphasis. A sustained face can do more work than a new angle.
Form a testable hypothesis about the moment, then compare actual material.
Continuity is a means of making intended relationships legible; intentional
rupture needs its own criteria. Neither “always invisible” nor “always dynamic”
is an adequate editorial policy.

**Evidence:** the one empirical source used here was read at abstract scope. It
supports a bounded claim about detection in that task, not comprehension,
emotion, quality or attention on present-day vertical feeds. Interviews/essays
are professional judgments. Source counts and named experts cannot close a
media or independent-behavior gate.

**Technical:** time values carry a domain, unit/rate and origin. Exact arithmetic
can catch impossible trims and sync mappings but cannot prove the intended clue
was visible. OTIO serialization may accept missing or beyond-available media;
stricter executable checks and rendered conform remain our responsibility.

**Design:** preserve a usable standalone skill and the current parallel work.
Use adapters here rather than changing shared contracts. Missing runtime/media
blocks only dependent proof. The user asked for Editor only; no Strategist or
orchestrator is created, no global install/commit/publish follows implicitly.
