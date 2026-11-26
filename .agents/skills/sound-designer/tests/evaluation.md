# Evaluation evidence and remaining gates

Date: **2026-11-25**. Scope: only this Sound Designer package. This is a new skill
folder in the existing The Stories skill checkout, not an installed agent runtime.
No shared documentation, neighboring skill, global install or remote was changed
by this task. Other worktree edits belong to parallel work.

## Evidence classes

| Class | Evidence / scope | Status |
| --- | --- | --- |
| Research | [Registry](../research/sources.md), 17 identified sources with read portions, access dates, claims and limits; additional/failed consultations explicit | Completed at stated access scope; not acoustic proof |
| Static packaging | Repository link/isolation checker, Skill Creator quick validation, UI metadata and JSON checks | See command results below |
| Model text | Ten [author-applied outputs](text-trials.md), same chat/context with visible probes | Authored and self-reviewed; not blind/independent evaluation |
| Metadata integration | Actual Cinematographer source snapshot/hash → [sound packet](../examples/windup-sound-packet.json); [example assertions](check_example.py) | Static mapping only; no receiver response |
| Audio generation/edit/mix | No actual source audio, cut or connected audio generator supplied; FFmpeg not found on PATH | Not performed |
| Audio evaluation | Silence export, suspense, masking, mono/mobile, pronunciation, lip sync, continuity, AI artifacts, meters, stems/M&E and decoded delivery | Not-assessed; follow [audio protocol](../references/review-rubric.md#actual-audio-exercise-protocol) |
| Rights/access/production | No project consent/licenses, native reviewer, timed captions/player, audience study or live Editor handoff | Not-assessed; no production readiness claim |

## Reproducible checks

From repository root:

```bash
python3 scripts/validate_repository.py --root skills/sound-designer --self-test
python3 scripts/validate_repository.py --self-test
python3 skills/sound-designer/tests/check_example.py --source skills/cinematographer/examples/silent-30s.json
```

`check_example.py` works independently of siblings without `--source`; the optional
comparison checks the exact authoring input hash and mappings. It intentionally
does not accept arbitrary contract variants or certify generated audio. Ten
invalid metadata variants probe dangling/duplicate IDs, typed-beat/scene mismatch,
invalid bounds, duration/timebase mismatch, false measured status/anchors/audio
and fictitious receipt. It is not a semantic judgment of the soundtrack.

Skill Creator's `quick_validate.py` requires PyYAML; a temporary environment at
`/tmp/sound-designer-skill-validation` was used, without adding repo dependencies.
It validates frontmatter/scaffold, not behavior. YAML interface metadata is checked
separately for valid strings and `$sound-designer` invocation.

### Recorded command outcomes

Final outcomes are recorded after running the complete package. A preliminary
link run correctly reported two missing links to this not-yet-created evaluation
record; those are construction findings, not an ignored passing run.

- Scoped link/anchor scan: 64 references, zero errors; validator's 2 self-tests
  passed. An independent temporary copy had the same 64 resolving references and
  passed the bundled example tests without sibling files.
- Full repository scan at that run: 572 references, zero errors; seven skills
  passed isolated-copy reference checks. This checks packaging only, including
  parallel work as it existed then, and does not certify another role's behavior.
- Skill Creator quick validation passed; UI YAML parsed, short description met
  its length requirement and default prompt contained `$sound-designer`; JSON
  parsed. Entry point is 78 lines.
- Example checker: 2 test methods passed, including 10 rejected invalid variants;
  optional real-source comparison confirmed SHA-256, primary sequence, locks,
  scene/typed-beat fields and estimated duration mapping. Source hash:
  `bf956f2a0bb3ad2d0a8de2ec18542b20e7d10fed483d90db7a65a370bb8b54a8`.
- [HTTP link evidence](http-links.json): 22 distinct URLs checked. Local Python
  CA verification failed for all initially; system curl with TLS verification
  enabled returned 19 HTTP 200, one AES landing 403 and two 404 responses
  (YouTube settings and the unused/inaccessible Berklee sound-designer URL).
  Web reader separately returned the YouTube/AES source bodies. These client/
  method discrepancies are retained, not called broken-source proof or hidden
  as an all-links pass. The unused Berklee URL is labeled failed in the registry.
- ITU PDF body later downloaded through system curl and selected text sections
  were actually read with pypdf; registry records the recovered access and hash.
  Neither a successful PDF HEAD nor text extraction proves meter compliance.

Final scoped recheck after documentation updates: **66 local references, zero
errors**, both validator self-tests passed; both example test methods (10 invalid
variants) and the exact-source comparison passed again. Skill Creator validation
passed again; all **25 package files** had zero trailing-whitespace findings.
No new dependencies were added to this repository.

## Files added

All authored files are under `skills/sound-designer/`: `SKILL.md`,
`agents/openai.yaml`; seven craft/contract/rubric references; one workflow; five
templates; three research records; two examples; and five test/evidence files
(scenarios, retained text trials, this evaluation, example checker, HTTP log).
Shared README/install/roadmap integration was deliberately left to its owner
under the user's folder-only instruction. Whole-folder copying preserves all
runtime references; this change does not update global discovery/installations.

## Trial interpretation and next gates

T01–T10 cover every requested adversarial case at text/metadata level. The
author's review found no hard-gate contradiction in the retained responses;
there is no independent numeric score. This does not test whether a fresh model
will discover/load the right reference or reproduce the judgment. Run fresh
context and independent review when authorized, using the raw scenarios without
expected failure columns, then retain actual outputs and any failures/retests.

For acoustic closure supply authorized media, actual capable tools, delivery
specs and a receiver. Test the final files with real logs/listening evidence and
language/device reviews. Missing capability is a reported limit, not a passing
result or a reason to fabricate production. See [gap map](../research/audit.md).
