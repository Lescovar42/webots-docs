## Objective
- Document localization, navigation, and behavior differences for the Alphonse robot branch (`ALPHONSE_NEW_V2`, commit `adacde8f6e01e6439d170fb6bce025acc051bfa3`) in `drafts/focus-difference-navigation.md`.

## Important Details
- Stage: `robot-differences`; focus strictly on localization, navigation, and behavior.
- Constraint: Max 8 exploration tool calls (budget exhausted); proceed to draft writing.
- Citation format: Must use exact inspected paths and line ranges, e.g., `[source/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/kick_alignment_policy.h:L10-L15](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/kick_alignment_policy.h#L10-L15)`.
- Content requirements: 300-600 words; must include scope, observed behavior, interfaces/configuration, untested operation notes, uncertainty/conflicts, and sources.
- Must distinguish hash changes, source-observed behavior, inference, and missing evidence.
- Must differentiate simulated Webots behavior from physical robot behavior.
- Assigned anchors were prioritized; unexamined files in the broader scope must be explicitly listed.

## Work State
### Completed
- Read context anchors: `drafts/DIFFERENCES.md` and `drafts/SHARED-INDEX.md`.
- Inspected navigation/localization source files: `config/README.md`, `config/KALIBRASI_TENDANG_2026-09-07.md`, `src/demo_node.cpp`, `include/op3_demo/kick_alignment_policy.h`, `include/op3_demo/ball_follower.h`, `include/op3_demo/ball_tracker.h`.
- Extracted walking preset flow, yaw alignment mapping, kick distance calibration baseline, demo status enums, and ball tracking state machines.

### Active
- Synthesizing inspected source behaviors and configuration differences into the structured draft.
- Formatting citations to match exact line ranges and applying scope/uncertainty tags.

### Blocked
- (none)

## Next Move
1. Write `drafts/focus-difference-navigation.md` integrating all inspected source findings, ensuring 300-600 word limit and strict citation formatting.
2. Validate that Webots vs physical behavior distinctions are explicit, and that unexamined scope files are listed per instructions.

## Relevant Files
- `drafts/DIFFERENCES.md`: Deterministic file-hash differences and representative scope anchors.
- `drafts/SHARED-INDEX.md`: Cross-branch shared code navigation references and status.
- `source/src/ROBOTIS-OP3-Demo/op3_demo/config/README.md`: Demo preset flow, walking parameter limits, yaw alignment mapping, and startup cycle.
- `source/src/ROBOTIS-OP3-Demo/op3_demo/config/KALIBRASI_TENDANG_2026-09-07.md`: Kick geometry calibration baseline, sensor observation logs, and unvalidated left-foot contact notes.
- `source/src/ROBOTIS-OP3-Demo/op3_demo/src/demo_node.cpp`: Demo status enumeration (`Ready`, `SoccerDemo`, `VisionDemo`, `ActionDemo`), callback routing, and initialization sequence.
- `source/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/kick_alignment_policy.h`: `KickPositionDecision` enum, ground distance calculation, and heading tolerance evaluation.
- `source/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/ball_follower.h`: Ball tracking states (`NotFound`, `OutOfRange`, `OnRight`, `OnLeft`), walking integration, and YAML parameter loading.
- `source/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/ball_tracker.h`: Head/servo tracking status enums, start/stop control methods, and scan configuration.