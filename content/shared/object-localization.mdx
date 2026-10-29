> Shared file-content analysis, using the Alphonse snapshot. Robot-specific runtime conditions require separate review.

# Shared ball-localization documentation and launch contracts

This card covers matching README, tracker-configuration, launch and historical bug-note files across the three pinned snapshots. It does not certify identical Python implementations or operating behavior. The failed draft followed a differing `ball_localizer_node.py`; that implementation and its robot-specific behavior are deliberately excluded here. Alphonse provides the canonical source links.

## What the README describes

The README describes a ball-localization and approach workflow using `/vision/yolo/balls`: head scanning, body rotation after a scan timeout, head tracking and approach, followed by positioning and a configured kick action. These are claims made by the project documentation, not behavior reproduced during this review. [source/src/op3_ball_localization/README.md:L1-L11](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_ball_localization/README.md#L1-L11)

Its run example starts the YOLO launch file followed by `ball_localizer.launch.py`, and it asks for YOLO points in the `base` frame. The example configuration refers to a YOLO YAML file outside this card's shared scope. The example commands were not executed and are not evidence that a particular robot is configured correctly. [source/src/op3_ball_localization/README.md:L13-L25](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_ball_localization/README.md#L13-L25)

The README lists distance and kick parameters, approach limits, scan ranges and timeout, search yaw, and several head-tracking modes and geometry inputs. Actual values and interpretation must be checked against each robot's selected configuration and node implementation. [source/src/op3_ball_localization/README.md:L27-L43](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_ball_localization/README.md#L27-L43)

## Two distinct configuration identities

`ball_localizer.launch.py` declares a `config` argument defaulting to the package's `config/ball_localizer.yaml`. It starts executable `ball_localizer`, names the node `op3_ball_localizer`, and supplies that selected file as parameters. [source/src/op3_ball_localization/launch/ball_localizer.launch.py:L10-L28](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_ball_localization/launch/ball_localizer.launch.py#L10-L28)

The separately reviewed `simple_ball_tracker.yaml` has a `simple_ball_tracker` parameter namespace. It names detection and ball-center topics, a publish rate, head-scanning settings, a lost-detection timeout and a bounding-box distance-estimation section. It also contains approach gains/limits, head-joint names, and walking/head module settings. [source/src/op3_ball_localization/config/simple_ball_tracker.yaml:L1-L43](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_ball_localization/config/simple_ball_tracker.yaml#L1-L43)

These files must not be conflated: the inspected launch file does not select `simple_ball_tracker.yaml`. Its launch default is a different filename, and the reviewed tracker file has a different node key. This is an observed configuration distinction, not proof that either configuration works or fails at runtime. [source/src/op3_ball_localization/launch/ball_localizer.launch.py:L10-L24](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_ball_localization/launch/ball_localizer.launch.py#L10-L24) [source/src/op3_ball_localization/config/simple_ball_tracker.yaml:L1-L8](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_ball_localization/config/simple_ball_tracker.yaml#L1-L8)

## Historical message-format note

The bug note reports a previous `Point.radius` error and describes the circle encoding as normalized center coordinates in `Point.x`/`Point.y`, with radius in `Point.z`. It shows a proposed correction using `circle.z`, plus coordinate-normalization changes. [source/src/op3_ball_localization/BUGFIX_CIRCLE_FORMAT.md:L3-L46](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_ball_localization/BUGFIX_CIRCLE_FORMAT.md#L3-L46)

The same note lists rebuild and launch commands and claims a rebuilt package, while also saying “Ready for testing.” These are historical statements from the note. This review did not reproduce the fix or inspect the affected implementation. [source/src/op3_ball_localization/BUGFIX_CIRCLE_FORMAT.md:L48-L61](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_ball_localization/BUGFIX_CIRCLE_FORMAT.md#L48-L61)

## Remaining verification

Before operating a robot, its own implementation, selected YAML, detector output frame, message encoding and motion/action settings require review together. No kick-page number, safe walking gain, camera calibration or successful hardware behavior is established by this card. No build, launch or robot action was performed.
