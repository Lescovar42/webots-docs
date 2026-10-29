# Chronus — Camera, Perception and Vision Differences

## Scope

This card surveys the camera hardware interface, the YOLO-based ball detector, and the downstream soccer perception pipeline in the **CHRONUS_NEW** branch (commit `54998e7`). It is a representative investigation; files listed in `drafts/DIFFERENCES.md` as changed or unique but not examined here are noted below. All runtime claims remain untested suggestions.

**Source files inspected in this card:**

| File | Role |
| --- | --- |
| `source/src/ROBOTIS-OP3-Demo/op3_ball_detector/config/camera_param.yaml` [camera_param.yaml] | usb_cam node parameters |
| `source/src/ROBOTIS-OP3-Demo/op3_ball_detector/scripts/yolo_ball_detector.py` [yolo_ball_detector.py] | YOLO detector node (Python / rclpy) |
| `source/src/ROBOTIS-OP3-Demo/op3_ball_detector/README_YOLO.md` [README_YOLO.md] | Detector documentation |
| `source/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/ball_follower.h` [ball_follower.h] | Ball-following behavior header |
| `source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/ball_tracker.cpp` [ball_tracker.cpp] | Ball tracking + head PID implementation |
| `source/src/ROBOTIS-OP3-Demo/op3_demo/launch/demo.launch.xml` [demo.launch.xml] | Primary demo launch file |
| `source/src/ROBOTIS-OP3-Demo/op3_demo/launch/demo_yolo.launch.xml` [demo_yolo.launch.xml] | Alternate YOLO-bridge demo launch file |

**Unexamined changed files relevant to vision (deferred):**

- `op3_ball_detector/config/yolo_ball_detector_params.yaml`, `*_onnx_params.yaml`, `*_openvino_params.yaml` – parameter variants
- `op3_ball_detector/launch/*.launch.py` – individual detector launch files
- `op3_ball_detector/CMakeLists.txt`, `package.xml`, `requirements_yolo.txt` – build/dependency scaffolding
- `op3_demo/include/op3_demo/ball_tracker.h`, `demo_node.cpp`, `soccer/demo*.cpp` – demo orchestration
- `op3_yolo_vision/src/yolo_detector.cpp`, `op3_yolo_vision/config/yolo.yaml` – alternative C++ YOLO path
- `op3_ball_localization/` (entire package) – bridge, head tracking, localizer nodes

---

## Camera Interface

The `camera_param.yaml` configures `usb_cam` with `/dev/video0` at 1280 × 720 @ 30 fps, using `mjpeg2rgb` pixel format and memory-mapped I/O [camera_param.yaml:L1-L23]. Auto-white-balance and auto-exposure are enabled; white balance is set to 4000 K and exposure default is 100 [camera_param.yaml:L18-L23]. This is identical to the classic pipeline camera configuration.

---

## YOLO Ball Detector

### Architecture

The `yolo_ball_detector.py` node [yolo_ball_detector.py:L58-L380] is a **drop-in replacement** for the original C++ Hough-circle `ball_detector_node`. It subscribes to camera images (either `CompressedImage` or raw `Image` on `image_in`, defaulting to compressed [yolo_ball_detector.py:L130-L137]), runs an Ultralytics YOLO model on the latest available frame at a fixed rate (`detection_rate` parameter, default 30 Hz [yolo_ball_detector.py:L85-L86]), and publishes detections as `op3_ball_detector_msgs/CircleSetStamped` on `circle_set` [yolo_ball_detector.py:L116-L117].

Because it publishes on the same topic and in the same format as the original C++ detector, downstream consumers (`BallTracker`, `BallFollower`) remain unchanged [yolo_ball_detector.py:L19-L36].

### Coordinate Convention

Detected bounding boxes are converted to circle tuples `(norm_x, norm_y, radius_px, conf)`:

- `x` and `y` are **normalized** coordinates in `[-1, 1]` (left → right, top → bottom) [yolo_ball_detector.py:L27-L28, L307-L310].
- `z` encodes **ball radius in pixels** (mean half-side of the bounding box) [yolo_ball_detector.py:L308, L322].
- Circles are sorted descending by radius so downstream picks the largest ball first [yolo_ball_detector.py:L314-L315].

### Head-Tracking Side Channel

The node additionally publishes the best ball center as a `geometry_msgs/PointStamped` on `/vision/yolo/ball_center` [yolo_ball_detector.py:L96-L101, L327-L333]. This topic uses **`[0, 1]`** coordinates (different from the `[-1, 1]` circle convention) so that the `op3_ball_localization/head_tracking_node` can drive head scan/track [yolo_ball_detector.py:L93-L98]. This topic is only published when a ball is detected; absence signals the tracker to scan.

### Model Loading and Backends

The node accepts `.pt`, `.onnx`, and OpenVINO directory models via the `model_path` parameter [yolo_ball_detector.py:L156-L184]. The default model is `best.pt` with class name `"Bola-baru"` [yolo_ball_detector.py:L68, L82-L84]. Three launch variants exist (PyTorch, ONNX, OpenVINO) and the OpenVINO backend is the default in `demo.launch.xml` [demo.launch.xml:L12]. OpenVINO is documented as fastest and most stable on Intel CPUs [README_YOLO.md:L131-L146].

The `imgsz` parameter controls input resolution (default 640) [yolo_ball_detector.py:L77]. For ONNX/OpenVINO it must match the export size, or the runtime rejects the shape [README_YOLO.md:L128-L129].

### Performance Configuration

Per [README_YOLO.md:L148-L163], the primary performance levers are input size (`imgsz`), model variant (`v8n` vs `v8s`), and backend choice. The recommended `detection_rate` cap (e.g. 15 Hz in OpenVINO config) prevents inference from starving the walking module.

---

## Ball Tracker and Head Control

The `BallTracker` class [ball_tracker.cpp:L7-L338] subscribes to `/ball_detector_node/circle_set` [ball_tracker.cpp:L74]. When a ball is found, it converts normalized circle coordinates to desired head angles using atan-based projection with FOV of 35.2° horizontal / 21.6° vertical [ball_tracker.cpp:L26-L27, L201-L204]. A PD controller drives head joint offsets via `/robotis/head_control/set_joint_states_offset` [ball_tracker.cpp:L205-L229, L265-L289]. Gains are P = 0.45, D = 0.045, I = 0.0 [ball_tracker.cpp:L49-L51].

In `demo.launch.xml`, the demo node sets `use_head_control = false` [demo.launch.xml:L50], meaning head control is handed off to the external `op3_ball_localization/head_tracking_node` [demo.launch.xml:L20-L30]. The `BallTracker`'s own `publishHeadJoint` method exits early when `use_head_control_` is `false` [ball_tracker.cpp:L266-L268].

### Alternate Launch Path

`demo_yolo.launch.xml` [demo_yolo.launch.xml] uses the C++ `op3_yolo_vision` detector plus a `yolo_to_demo_bridge` node to convert to `CircleSetStamped`. This is a **parallel** pipeline: it keeps the same downstream `SoccerDemo` and ball tracker semantics but replaces the detector hardware path.

---

## Differences from Alphonse (by file hash)

Per `drafts/DIFFERENCES.md`, the following vision-related files are marked changed or unique in this branch:

- `op3_ball_detector/` (scripts, configs, launch, CMakeLists, package.xml, requirements) — new YOLO detector package
- `op3_demo/launch/demo.launch.xml` — default switched to OpenVINO YOLO [demo.launch.xml:L5-L12]
- `op3_demo/launch/demo_yolo.launch.xml` — new alternate launch file
- `op3_demo/include/op3_demo/ball_follower.h` — subscription to `CircleSetStamped` [ball_follower.h:L32]
- `op3_yolo_vision/` — C++ YOLO detector and config (changed)
- `op3_ball_localization/` — bridge, head tracking, localizer (changed)

Conversely, these vision-related files **present in Alphonse but absent** in this branch ([DIFFERENCES.md:L102-L168]):

- `scripts/quantize_ball_int8.py`, `scripts/compare_ball_models.py`
- `op3_ball_detector/README_GOALLINE.md`, `README_LANDMARK.md`
- Config files for goal-line, field, and landmark detectors (`yolo_*_detector_params.yaml`)
- Launcher files for field/goal-line/landmark detectors
- Scripts: `detector_fps.py`, `goalline_core.py`, `yolo_field_detector.py`, `yolo_landmark_detector.py`

This suggests the **goal-line, field, and landmark detection capabilities** have been **removed** in this branch, narrowing vision scope to ball detection only.

---

## Interfaces and Configuration Summary

| Interface | Topic | Type | Direction |
| --- | --- | --- | --- |
| Camera stream | `image_in` | `CompressedImage` / `Image` | sub |
| Ball detections | `circle_set` | `CircleSetStamped` | pub |
| Ball center for head | `/vision/yolo/ball_center` | `PointStamped` | pub |
| Enable/disable detection | `enable` | `std_msgs/Bool` | sub |
| Annotated debug image | `image_out` | `sensor_msgs/Image` | pub |
| PID head offsets | `/robotis/head_control/set_joint_states_offset` | `JointState` | pub (by Tracker) |
| Head scan command | `/robotis/head_control/scan_command` | `std_msgs/String` | pub (by Tracker) |

---

## Untested Operation Notes

All commands below are **found in source but not executed**:

- `ros2 launch op3_demo demo.launch.xml` — primary demo launch with OpenVINO YOLO [README_YOLO.md:L39-L41]
- `ros2 launch op3_ball_detector yolo_ball_detector.launch.py` — standalone detector [README_YOLO.md:L101-L102]
- Switching backends via `ball_detector_launch` argument [README_YOLO.md:L44-L54]
- pip install of `ultralytics`, `torch`, `onnxruntime`, `openvino` inside containers [README_YOLO.md:L58-L85]

---

## Uncertainties and Conflicts

1. **Circle `z` semantics**: the YOLO node stores radius in pixels (`z`) [yolo_ball_detector.py:L308], matching the doc comment [yolo_ball_detector.py:L30]. The `BallTracker.selectLargestBall` (implied by `ballPositionCallback`) picks the circle with the largest `z` value [ball_tracker.cpp:L82-L91]. This is consistent but was not validated with a live camera.

2. **Dual head control**: `demo.launch.xml` sets `use_head_control = false` on the demo node [demo.launch.xml:L50] and launches an external `head_tracking_node` [demo.launch.xml:L27-L30]. If `head_tracking_node` fails to start, the BallTracker's internal `publishHeadJoint` would be dead code — no fallback head control exists.

3. **Missing landmark/goal-line detection**: The absence of `yolo_landmark_detector.py`, `yolo_goalline_detector.py`, and `yolo_field_detector.py` in this branch indicates these capabilities were dropped. The impact on soccer behaviors (field boundary awareness, goal alignment) is not examined here.

4. **Webots vs physical hardware**: In Webots simulation, the camera topic typically originates from `webots_camera_driver` nodes rather than `usb_cam`. The `demo_yolo.launch.xml` path may be intended for simulation while `demo.launch.xml` with OpenVINO + `usb_cam` targets physical hardware. This distinction is inferred, not confirmed by source.

5. **`demo_yolo.launch.xml` usage**: This file exists in this branch but is not referenced by `demo.launch.xml`. It is unclear whether it is an active alternative, a migration artifact, or a simulation-only path. Commands to launch it are untested suggestions.

---

## Sources

- [source/src/ROBOTIS-OP3-Demo/op3_ball_detector/config/camera_param.yaml:L1-L23](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3-Demo/op3_ball_detector/config/camera_param.yaml#L1-L23)
- [source/src/ROBOTIS-OP3-Demo/op3_ball_detector/scripts/yolo_ball_detector.py:L19-L380](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3-Demo/op3_ball_detector/scripts/yolo_ball_detector.py#L19-L380)
- [source/src/ROBOTIS-OP3-Demo/op3_ball_detector/README_YOLO.md:L1-L197](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3-Demo/op3_ball_detector/README_YOLO.md#L1-L197)
- [source/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/ball_follower.h:L7-L137](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/ball_follower.h#L7-L137)
- [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/ball_tracker.cpp:L7-L338](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/ball_tracker.cpp#L7-L338)
- [source/src/ROBOTIS-OP3-Demo/op3_demo/launch/demo.launch.xml:L1-L52](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3-Demo/op3_demo/launch/demo.launch.xml#L1-L52)
- [source/src/ROBOTIS-OP3-Demo/op3_demo/launch/demo_yolo.launch.xml:L1-L30](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3-Demo/op3_demo/launch/demo_yolo.launch.xml#L1-L30)
- [drafts/DIFFERENCES.md:L1-L168]
- [drafts/SHARED-INDEX.md:L1-L21]
