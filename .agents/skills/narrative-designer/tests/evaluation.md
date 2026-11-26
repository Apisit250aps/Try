# Evaluation and evidence

Snapshot 2026-11-26. The scenario suite is a plan, not a report of model passes.
This package is skill instructions, not a player, generic validator or agent runtime.

| Check | Actual evidence / result | Limits |
| --- | --- | --- |
| Research and overlap | Registry with access limits, source-to-principle map and repository/Studio Audit review | Selected sections only; source fidelity was manually examined, not independently audited. |
| Executed graph probe | `python3 skills/narrative-designer/tests/graph-probe.py` passed: 7 reachable node-state pairs; both example endings reachable; join state retained; overlap and uncovered state witnesses; unreachable third ending; two specified loop structures | Synthetic finite fixture only; hard-coded assumptions and assertions, not a reusable validator or exhaustive scenario suite. Guard gap witness is an arbitrary state, not proven reachable. Cycle checks inspect edges, not temporal model checking. |
| Worked cases | Authored examples and counterexamples in package | Self-authored text; not a separate model or human evaluation, production clip, real runtime or receiver. |
| Skill discovery / integration | Source entrypoint and README pointer added | No install, host reload, discovery run, receipt or shared contract change. Storyteller description overlaps. |
| Fresh-context model scenario suite | Not run | No model performance claim; N01–N14 remain open. |
| Audience / player / platform / production | Not run | No agency, creative impact, native feature, timing, cost or live media evidence. |

Structural validation and quick-validation outcomes are recorded below after running;
they do not establish semantic quality. Re-run after changes. The fixture script is
retained as reproducible evidence, not a recommended production validation engine.

Final structural run: `python3 scripts/validate_repository.py --self-test` passed
2 self-tests, 917 repository links and 13 links in the isolated new skill (0
errors). This validator checks inline Markdown links/anchors only, not remote URLs,
semantics or actual host loading. Skill Creator `quick_validate.py` passed using
`/tmp/the-stories-editor-validation/bin/python`; the default `python3` initially
failed because PyYAML is absent. No dependency was installed. `git diff --check`
passed for tracked modifications; untracked files were separately checked for
trailing whitespace. Results describe this snapshot only.
