# Review notes and operating limits

On 2026-10-29, Codex reviewed and rewrote all 13 remaining flagged focused drafts against printed source ranges and snapshot hashes.
Five previously failed tasks had already received source-reviewed replacements. The remaining 28 reports retain their original automated source checks.
All 46 reports pass their applicable citation checks. This is not a claim of exhaustive semantic or hardware validation.

## Corrections in this review

| Robot | Document | Checked references |
|---|---|---:|
| Alphonse | [Shared code: Workspace and package structure](Shared/focus-shared-workspace.md) | 6 |
| Alphonse | [Shared code: Action and motion modules](Shared/focus-shared-actions.md) | 5 |
| Alphonse | [Shared code: Ball and face detection](Shared/focus-shared-detectors.md) | 5 |
| Alphonse | [Shared code: Studio and robot development tools](Shared/focus-shared-tools.md) | 5 |
| Alphonse | [Alphonse: Environment, startup and launch differences](Alphonse/focus-difference-setup.md) | 9 |
| Alphonse | [Alphonse: Other changed files and remaining uncertainty](Alphonse/focus-difference-other.md) | 6 |
| Chronus | [Chronus: Other changed files and remaining uncertainty](Chronus/focus-difference-other.md) | 6 |
| Orion | [Orion: Environment, startup and launch differences](Orion/focus-difference-setup.md) | 9 |
| Orion | [Orion: Camera, perception and vision differences](Orion/focus-difference-vision.md) | 11 |
| Orion | [Orion: Other changed files and remaining uncertainty](Orion/focus-difference-other.md) | 5 |
| Alphonse | [Alphonse guide: Robot-specific settings, differences and review gaps](Alphonse/focus-guide-differences.md) | 7 |
| Chronus | [Chronus guide: Operation and troubleshooting](Chronus/focus-guide-operation.md) | 10 |
| Chronus | [Chronus guide: Robot-specific settings, differences and review gaps](Chronus/focus-guide-differences.md) | 5 |

Malformed/unknown paths and citations to unread or empty files were corrected through reviewed replacements. Unverified package-wide claims were narrowed to inspected evidence.

## Known issues requiring separate runtime work

- Launch/node simulation parameter names differ in the reviewed Alphonse and Chronus paths; effective behavior is not verified.
- Serial topology, action files, offsets, walking gains and UI/native-value conversion remain specific to each robot.
- Some launch/helper paths can probe ports, rewrite device links, install dependencies or alter settings; documentation review did not execute them.
- Orion vision source uses pixel-valued radii alongside normalized center coordinates; consumer integration and model quality remain untested.
- README descriptions and historical benchmark/build statements are attributed to source and are not reproduced results.

Original drafts and review evidence are backed up on the workstation. This archive omits those internal backup paths and the deferred historical audit.
