# Alphonse: Camera, Perception and Vision Differences

**Branch:** `ALPHONSE_NEW_V2` &nbsp; **Commit:** `adacde8f6e` &nbsp; **Stage:** robot-differences

## Scope

This draft examines how the Alphonse branch (ALPHONSE_NEW_V2) differs from shared code and other branches in its **camera capture pipeline**, **ball perception**, and **goal-line vision geometry**. It covers the `op3_ball_detector` package and the `op3_demo` ball tracker module. Unexamined files in this scope include `yolo_ball_detector.py`, `yolo_field_detector.py`, `yolo_goalline_detector.py`, `yolo_landmark_detector.py`, and all config YAML files under `op3_ball_detector/config/` except `camera_param.yaml`.

## Observed Behavior — Camera Capture

The camera is configured at 640×360 resolution and 24 Hz frame rate, targeting `/dev/video0` (a Logitech C920). These values are not arbitrary: the configuration carries detailed commentary explaining why 720p@30 FPS was discarded and why 24 Hz was chosen over 25 Hz.

- Resolution was reduced from 1280×720 to 640×360 because the MJPEG decode at 720p consumed 73% of a CPU core, producing frame ages of ~996 ms — the head would chase where the ball was one second ago and never lock on [source/src/ROBOTIS-OP3-Demo/op3_ball_detector/config/camera_param.yaml:L9-L17](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_ball_detector/config/camera_param.yaml#L9-L17). After the reduction, frame age dropped to ~170 ms.
- Frame rate progressed 15 → 20 → 24 FPS between August and September 2026 [source/src/ROBOTIS-OP3-Demo/op3_ball_detector/config/camera_param.yaml:L30-L38](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_ball_detector/config/camera_param.yaml#L30-L38). The value 24 is hardware-bound: the camera only advertises 30/24/20/15/10/7.5/5 at 640×360; setting it to 25 would silently snap to the nearest rate.
- The 16:9 aspect ratio is intentionally preserved (not changed to 640×480) so that `fov_width_deg`/`fov_height_deg` values in `head_tracking.yaml` remain valid [source/src/ROBOTIS-OP3-Demo/op3_ball_detector/config/camera_param.yaml:L20-L22](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_ball_detector/config/camera_param.yaml#L20-L22).
- Exposure is capped by frame rate: 24 FPS imposes exposure ≤ 41.7 ms, reducing light by ~0.68 EV compared to 15 FPS [source/src/ROBOTIS-OP3-Demo/op3_ball_detector/config/camera_param.yaml:L43-L49](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_ball_detector/config/camera_param.yaml#L43-L49). Gain is already at maximum (255), so the only compensation is brighter field illumination or falling back to 20 FPS.
- The frame rate setting is only a *request*: if `v4l2-ctl -c exposure_dynamic_framerate=0` is not applied via the launch file, the camera can independently slow to 15 FPS [source/src/ROBOTIS-OP3-Demo/op3_ball_detector/config/camera_param.yaml:L51-L54](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_ball_detector/config/camera_param.yaml#L51-L54). **Command found in source but not executed.**

## Observed Behavior — Ball Perception Pipeline

The ball tracker in `op3_demo` is a C++ ROS 2 component. It subscribes to `CircleSetStamped` messages published by the YOLO ball detector and converts 2D image positions into head pan/tilt commands.

### Field of View constants

The tracker uses hardcoded intrinsic values for the camera field of view:

- `FOV_WIDTH = 35.2°` (radians: `35.2 * π / 180`) [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/ball_tracker.cpp:L26](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/ball_tracker.cpp#L26)
- `FOV_HEIGHT = 21.6°` (radians: `21.6 * π / 180`) [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/ball_tracker.cpp:L27](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/ball_tracker.cpp#L27)

These are `const double` members initialized in the constructor [source/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/ball_tracker.h:L80-L81](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/ball_tracker.h#L80-L81). They are not loadable parameters — changing the camera lens or resolution would require recompiling. The 35.2° × 21.6° field of view is consistent with the 16:9 sensor ratio.

### Tracking control loop

The PID gains for head tracking are hardcoded (parameter declarations are commented out): `P = 0.45, I = 0.0, D = 0.045` [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/ball_tracker.cpp:L50-L52](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/ball_tracker.cpp#L50-L52). The tracker maintains a three-state machine: `NotFound (-1)`, `Waiting (0)`, `Found (1)` [source/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/ball_tracker.h:L43-L47](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/ball_tracker.h#L43-L47). Thresholds for state transitions are `NOT_FOUND_THRESHOLD = 50` frames and `WAITING_THRESHOLD = 5` frames [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/ball_tracker.cpp:L28-L29](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/ball_tracker.cpp#L28-L29).

### Callback and publisher lifecycle

A regression fix was added: publishers for head control (`/robotis/head_control/set_joint_states_offset`, etc.) are now created once in `setNode()` rather than inlined per call. The previous inline creation caused DDS discovery to miss early messages, making the head scan indefinitely even after the ball was detected [source/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/ball_tracker.h:L91-L96](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/ball_tracker.h#L91-L96) [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/ball_tracker.cpp:L77-L86](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/ball_tracker.cpp#L77-L86). This is an Alphonse-specific behavioral difference affecting physical robot head motion reliability.

## Observed Behavior — Goal-Line Vision

The goal-line detector is a separate Python pipeline standing apart from ball detection. It uses a 5-class YOLOv8n model (`best_landmark_v8n`) trained on landmarks: `L`, `T`, `X`, `goalpost`, `center_circle` [source/src/ROBOTIS-OP3-Demo/op3_ball_detector/README_GOALLINE.md:L4-L5](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_ball_detector/README_GOALLINE.md#L4-L5).

### Geometric reconstruction

There is no "goal line" class in the model. The line is reconstructed from detections in five steps [source/src/ROBOTIS-OP3-Demo/op3_ball_detector/README_GOALLINE.md:L49-L66](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_ball_detector/README_GOALLINE.md#L49-L66):

1. Each `goalpost` box contributes its foot point (bottom-centre of the bounding box) [source/src/ROBOTIS-OP3-Demo/op3_ball_detector/scripts/goalline_core.py:L192-L195](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_ball_detector/scripts/goalline_core.py#L192-L195).
2. A line is fitted through the foot points using **total least squares via SVD**, not ordinary regression, because frontal goal views produce vertical screen projections that blow up `y = ax + b` [source/src/ROBOTIS-OP3-Demo/op3_ball_detector/scripts/goalline_core.py:L195](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_ball_detector/scripts/goalline_core.py#L195).
3. L/T/X junctions within `landmark_band_px` (default 40 px) of the line are pulled in and the fit is redone, stabilising the angle [source/src/ROBOTIS-OP3-Demo/op3_ball_detector/scripts/goalline_core.py:L196-L198](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_ball_detector/scripts/goalline_core.py#L196-L198).
4. The fit is rejected if support points lack collinearity (`min_linearity = 0.90`) or segment length is under 30 px [source/src/ROBOTIS-OP3-Demo/op3_ball_detector/scripts/goalline_core.py:L207-L208](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_ball_detector/scripts/goalline_core.py#L207-L208).
5. Endpoints are exponentially smoothed (EMA, `smoothing = 0.5`) and the previous line is held for `hold_sec = 0.4 s` on failed frames [source/src/ROBOTIS-OP3-Demo/op3_ball_detector/scripts/goalline_core.py:L202-L204](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_ball_detector/scripts/goalline_core.py#L202-L204) [source/src/ROBOTIS-OP3-Demo/op3_ball_detector/scripts/goalline_core.py:L240-L260](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_ball_detector/scripts/goalline_core.py#L240-L260).

The estimator requires at least `min_goalposts = 2` detections to produce output [source/src/ROBOTIS-OP3-Demo/op3_ball_detector/README_GOALLINE.md:L214-L215](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_ball_detector/README_GOALLINE.md#L214-L215). It publishes a `PolygonStamped` (pixel coordinates), a normalized `PointStamped` in `[-1, 1]` range, and a `Bool` for validity [source/src/ROBOTIS-OP3-Demo/op3_ball_detector/README_GOALLINE.md:L77-L83](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_ball_detector/README_GOALLINE.md#L77-L83).

### Performance characteristics

Measured on hardware (NUC10i5, OpenVINO INT8, 640 px), the goal-line model runs at ~35.5 FPS offline and ~26 FPS pinned to cores 0–3 under load [source/src/ROBOTIS-OP3-Demo/op3_ball_detector/README_GOALLINE.md:L196-L202](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_ball_detector/README_GOALLINE.md#L196-L202). The default `detection_rate` is intentionally held at 10 Hz because it shares cores with the ball detector and walking controller.

## Interfaces and Configuration

| Component | Config file | Key parameters |
|---|---|---|
| Camera capture | `camera_param.yaml` | `video_device`, `framerate`, `image_width/height` [source/src/ROBOTIS-OP3-Demo/op3_ball_detector/config/camera_param.yaml:L3-L56](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_ball_detector/config/camera_param.yaml#L3-L56) |
| Ball tracker FOV | `ball_tracker.cpp` | Hardcoded `FOV_WIDTH`, `FOV_HEIGHT` [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/ball_tracker.cpp:L26-L27](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/ball_tracker.cpp#L26-L27) |
| Ball tracker PID | `ball_tracker.cpp` | Commented-out `declare_parameter`, inline assignment [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/ball_tracker.cpp:L43-L52](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/ball_tracker.cpp#L43-L52) |
| Goal-line estimator | `goalline_core.py` | `min_goalposts`, `landmark_band_px`, `min_linearity`, `smoothing`, `hold_sec` [source/src/ROBOTIS-OP3-Demo/op3_ball_detector/scripts/goalline_core.py:L207-L217](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_ball_detector/scripts/goalline_core.py#L207-L217) |
| FPS meter | `detector_fps.py` | Shared `FpsMeter` class, `window_sec = 2.0`, `keep_samples = 20000` [source/src/ROBOTIS-OP3-Demo/op3_ball_detector/scripts/detector_fps.py:L59-L60](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_ball_detector/scripts/detector_fps.py#L59-L60) |

The `FpsMeter` utility is imported by four detector scripts and the offline benchmark, deliberately avoiding any `rclpy` dependency to keep the benchmark ROS-free [source/src/ROBOTIS-OP3-Demo/op3_ball_detector/scripts/detector_fps.py:L27-L36](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_ball_detector/scripts/detector_fps.py#L27-L36).

## Untested Operation Notes

The following commands appear in source documentation but were **not executed**:

- `v4l2-ctl -d /dev/video0 --list-formats-ext` — to enumerate camera frame rates [source/src/ROBOTIS-OP3-Demo/op3_ball_detector/config/camera_param.yaml:L36](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_ball_detector/config/camera_param.yaml#L36)
- `v4l2-ctl -c exposure_dynamic_framerate=0` — to disable adaptive frame-rate on the camera device [source/src/ROBOTIS-OP3-Demo/op3_ball_detector/config/camera_param.yaml:L52](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_ball_detector/config/camera_param.yaml#L52)
- `ros2 run op3_ball_detector goalline_fps_benchmark.py` — offline FPS measurement [source/src/ROBOTIS-OP3-Demo/op3_ball_detector/README_GOALLINE.md:L15-L17](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_ball_detector/README_GOALLINE.md#L15-L17)
- `ros2 launch op3_ball_detector yolo_goalline_detector.launch.py` — live goal-line detection [source/src/ROBOTIS-OP3-Demo/op3_ball_detector/README_GOALLINE.md:L19-L30](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_ball_detector/README_GOALLINE.md#L19-L30)

All are found in source but remain untested suggestions.

## Distinguishing Simulated vs Physical Behavior

- The ball tracker hardcodes FOV angles that assume the physical Logitech C920 attached to `/dev/video0`. Webots simulation uses a different camera model with its own intrinsics; there is no evidence that `FOV_WIDTH`/`FOV_HEIGHT` are overridden for simulation.
- The goal-line detector documentation explicitly warns that the model produces false positives on robot frames in indoor lab recordings — a `goalpost` was detected with 0.70 confidence on the robot's upright black chassis [source/src/ROBOTIS-OP3-Demo/op3_ball_detector/README_GOALLINE.md:L217-L223](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_ball_detector/README_GOALLINE.md#L217-L223). This is a training-data limitation rather than a code issue.
- FPS figures are measured on physical hardware (NUC10i5) only [source/src/ROBOTIS-OP3-Demo/op3_ball_detector/README_GOALLINE.md:L195-L202](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_ball_detector/README_GOALLINE.md#L195-L202). No simulation benchmarks are provided.

## Uncertainties and Conflicts

1. The ball tracker PID parameters are not exposed as ROS 2 parameters (the `declare_parameter` calls are commented out) [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/ball_tracker.cpp:L43-L49](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/ball_tracker.cpp#L43-L49). It is unclear whether other branches expose these as runtime-configurable parameters.
2. The FOV values 35.2° × 21.6° are source-code constants. If the camera or lens is changed on another branch, these would need recompilation. No evidence was found for a configuration file overriding FOV at runtime.
3. The `camera_param.yaml` commentary references `aux_cpu_affinity` in `yolo_ball_detector_openvino.launch.py` but this launch file was not inspected. The CPU pinning claim could not be verified.
4. Shared-index indicates the "Camera and YOLO integration" shared card has **failed** status [drafts/SHARED-INDEX.md:L15]. The differences reported here may partially overlap with changes in other branches that have not yet been reconciled.

## Sources

- `source/src/ROBOTIS-OP3-Demo/op3_ball_detector/config/camera_param.yaml` — camera resolution, frame rate, and rationale [L3-L69]
- `source/src/ROBOTIS-OP3-Demo/op3_ball_detector/scripts/detector_fps.py` — shared FpsMeter utility [L1-L210]
- `source/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/ball_tracker.h` — ball tracker class declaration, FOV members, publishers, state machine [L1-L124]
- `source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/ball_tracker.cpp` — FOV initialization, PID gains, callback, publisher lifecycle fix [L20-L119]
- `source/src/ROBOTIS-OP3-Demo/op3_ball_detector/scripts/goalline_core.py` — goal-line reconstruction algorithm, smoothing, rejection thresholds [L187-L266]
- `source/src/ROBOTIS-OP3-Demo/op3_ball_detector/README_GOALLINE.md` — goal-line detector documentation, performance figures, model limitations [L1-L228]
- `drafts/DIFFERENCES.md` — deterministic file-list of changed/unique files [L1-L160]
- `drafts/SHARED-INDEX.md` — shared-code navigation status [L1-L21]
