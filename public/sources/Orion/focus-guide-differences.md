# Orion guide: Robot-specific settings, differences and review gaps

> **Scope.** This guide collects the settings and behaviors unique to the *Orion* unit (branch `ORION_NEW`, commit `dba5be3fefbada854b8d6c11d6655f479b482574`). General OP3 architecture, simulation setup, and shared modules are covered by the linked shared cards and are not repeated here. Claims are drawn from the source files listed in [Sources](#sources) beneath; they have **not** been executed on hardware or in simulation.

---

## Shared references

| Card | Published link | Status |
|---|---|---|
| Workspace & package structure | [shared card](../Shared/focus-shared-workspace.md) | needs_review |
| Framework & device interfaces | [shared card](../Shared/focus-shared-framework.md) | done |
| ROS messages & services | [shared card](../Shared/focus-shared-messages.md) | done |
| Manager & hardware bringup | [shared card](../Shared/focus-shared-manager.md) | done |
| Walking & balance modules | [shared card](../Shared/focus-shared-walking.md) | done |
| Kinematics & mathematics | [shared card](../Shared/focus-shared-kinematics.md) | done |
| Webots & simulation | [shared card](../Shared/focus-shared-webots.md) | done |
| Joystick & teleoperation | [shared card](../Shared/focus-shared-teleop.md) | done |

---

## 1 Prerequisites and environment

### 1.1 Single-container Docker stack

Orion consolidates its runtime into **one** Docker container definition. All prior menu/tmux and `docker-compose` entry-points are thin wrappers around `scripts/op3_docker.sh` [source/README.md:L84-L89](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/README.md#L84-L89). The container image must be `motion_webots_new-op3_ros2:latest`; older images lack PyTorch/YOLO and the ball detector will silently fail to start [source/README.md:L64-L68](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/README.md#L64-L68).

> **Untested command.** All shell commands below are found in source but were **not** executed.

| Action | Command | Source |
|---|---|---|
| Build | `docker build -t motion_webots_new-op3_ros2:latest .` | [source/README.md:L58-L60](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/README.md#L58-L60) |
| Start | `scripts/op3_docker.sh up` | [source/README.md:L78](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/README.md#L78) |
| Shell | `scripts/op3_docker.sh shell` | [source/README.md:L79](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/README.md#L79) |
| Diagnostics | `scripts/op3_docker.sh doctor` | [source/README.md:L80](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/README.md#L80) |
| Stop | `scripts/op3_docker.sh down` | [source/README.md:L82](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/README.md#L82) |

### 1.2 Serial port is auto-detected — and patchable at runtime

The FTDI FT232H adapter enumerates under different `/dev/ttyUSB*` numbers across plug-cycles. The launch file **does not pin** a fixed port. Instead:

- `detect_dynamixel_device()` scans `/dev/ttyUSB0`–`/dev/ttyUSB9`, picks the first openable device, and falls back to `/dev/ttyOP3` or `/dev/ttyUSB0` [source/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py:L22-L37](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py#L22-L37).
- `robot_file_with_device()` rewrites `OP3.robot` into a temp copy, substituting the detected port for every hardcoded path, then cleans up via `atexit` [source/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py:L40-L58](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py#L40-L58).
- Override with `OP3_DEVICE=/dev/ttyUSB1` environment variable [source/README.md:L117](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/README.md#L117).

**Bus is single-master.** `op3_manager` and `op3_action_editor` must **not** hold the port simultaneously, or packets corrupt with `first bulk read fail!!` [source/README.md:L128-L131](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/README.md#L128-L131).

### 1.3 Device cleanup on exit

Previous tmux-based sessions left orphaned processes gripping the serial port. Orion now kills every descendant via PPID tree, then sweeps any process still holding `ttyUSB0-9` (including deleted inodes), SIGTERM first, SIGKILL after a 2-second grace [source/README.md:L140-L169](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/README.md#L140-L169). The helper is `scripts/lib/proc_tree.sh` [source/README.md:L169-L171](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/README.md#L169-L171).

---

## 2 Robot-specific configuration

### 2.1 Joint offsets are all zero

`offset.yaml` lists every joint (20 servos + head) with offset `0` for both the primary `offset` and the `init_pose_for_offset_tuner` sections [source/src/ROBOTIS-OP3/op3_manager/config/offset.yaml:L1-L42](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/config/offset.yaml#L1-L42). This differs from other units that carry per-joint calibration residuals.

### 2.2 Walking parameters are tuned per-robot

`param.yaml` carries Orion-specific neutral-stance offsets fitted to action page 2 (`WALKING_READY` in `motion_4095_ORION.bin`) [source/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml:L1-L24](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml#L1-L24). Key values:

| Parameter | Value | Note |
|---|---|---|
| `x_offset` | `-0.015` | Foot centering (m) |
| `y_offset` | `0.025` | Foot separation; ~31 mm effective gap [source/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml:L18-L20](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml#L18-L20) |
| `z_offset` | `0.0` | Raise for crouch, but gait lift is reduced [source/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml:L8-L9](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml#L8-L9) |
| `pitch_offset` | `9.4` | Torso forward lean; mirrors `hip_pitch_offset` and is read by BallFollower [source/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml:L22-L24](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml#L22-L24) |
| `hip_pitch_offset` | `9.4` | Cancelled inside gait (bias subtracts), but exported to BallFollower |
| `period_time` | `780` | ms per step cycle |
| `foot_height` | `0.033` | Swing clearance (m) |

> **Warning.** Publishing "save" on `/robotis/walking/command` **rewrites** this file and drops all comments [source/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml:L25](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml#L25).

Orion's walking module captures pose at runtime (capture/bias mechanism at `op3_walking_module.cpp` ~504–544) instead of relying on FK-derived offsets, so the zero `offset.yaml` is intentional: the walking module reads the true held pose from the controller and biases the gait on top [source/scripts/action_page_fk.py:L26-L30](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/scripts/action_page_fk.py#L26-L30).

### 2.3 Standing tracks current params live

Since 2026-08-13, the legs follow the neutral stance defined by current offsets even **before** walking starts (rate-limited to 25 deg/s). Publishing to `/robotis/walking/set_params` (the "Apply" button in Bascorro Studio) moves the robot immediately, with no jump at `start` [source/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml:L10-L15](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml#L10-L15).

### 2.4 Device list

OP3 defines 20 Dynamixel XM430-W350 servos (IDs 1–20) and one OpenCR sub-controller (ID 200) on a single TTL bus through `/dev/ttyUSB0` at 2 Mbaud, control cycle 8 ms [source/src/ROBOTIS-OP3/op3_manager/config/OP3.robot:L1-L30](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/config/OP3.robot#L1-L30). The launch file patches the port path dynamically [source/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py:L40-L58](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py#L40-L58).

---

## 3 Diagnostics utility (Orion-specific)

### 3.1 `scripts/op3_ping.py`

A zero-dependency Protocol 2.0 ping tool. Scans IDs 1–20 and 200. Reports hardware-error latch bits (overload, overheating, etc.) [source/scripts/op3_ping.py:L1-L38](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/scripts/op3_ping.py#L1-L38).

> **Untested command.** `scripts/op3_docker.sh shell -c 'python3 scripts/op3_ping.py'` [source/README.md:L118](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/README.md#L118)

### 3.2 `scripts/action_page_fk.py`

Reads action pages directly from `motion_4095_ORION.bin` and prints joint values + FK offsets for comparison. **Do not copy FK offsets to `param.yaml`** — Orion's servo zero calibration differs from the reference robot, so FK-derived values are misleading [source/scripts/action_page_fk.py:L17-L30](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/scripts/action_page_fk.py#L17-L30).

> **Untested command.** `python3 scripts/action_page_fk.py` [source/README.md:L208-L211](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/README.md#L208-L211), [source/scripts/action_page_fk.py:L38-L42](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/scripts/action_page_fk.py#L38-L42)

---

## 4 Robot behavior vs simulation

| Aspect | Orion (physical) | Webots simulation |
|---|---|---|
| Serial port | Auto-detected `/dev/ttyUSB*` via launch file | Emulated via `RobotisController` Webots node; no serial scan |
| Servo zero calibration | Non-standard; FK script warns against use | Assumed ideal (raw 2048 = straight) |
| Gait capture | Runtime capture/bias from controller pose at start | FK-based initial pose |
| Container | Single privileged Docker container | Separate Webots process on host |

---

## 5 Known gaps and conflicts

| Topic | Status | Notes |
|---|---|---|
| Calibration differences to Alphonse | Needs review | Prior draft `focus-difference-hardware.md` is checked; cross-check zero-offset claim [source/src/ROBOTIS-OP3/op3_manager/config/offset.yaml:L1-L42](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/config/offset.yaml#L1-L42) |
| Walking module capture code | Needs review | Referenced at `op3_walking_module.cpp:504-544` in comments but not directly read here |
| Camera presence | Needs review | README says camera is optional; `op3_ball_detector` runs silently with no topics if camera absent [source/README.md:L188-L205](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/README.md#L188-L205) |
| Docker image build | Needs review | README documents arm64 Jetson build; not applicable to x86 host development machines |
| `run/run_vision_and_webots.sh` | Needs review | Referenced in README as the "new" run method but file itself was not examined [source/README.md:L38-L41](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/README.md#L38-L41) |

---

## 6 Sources

| File | Lines read | Role |
|---|---|---|
| `source/README.md` | 1–254 | Docker stack, serial port policy, cleanup, camera, diagnostics |
| `source/src/ROBOTIS-OP3/op3_manager/config/offset.yaml` | 1–42 | Zero joint offsets |
| `source/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml` | 1–46 | Per-robot walking parameters |
| `source/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py` | 1–97 | Auto-detect port, dynamic robot-file patching |
| `source/src/ROBOTIS-OP3/op3_manager/config/OP3.robot` | 1–30 | Device list, baud rate, control cycle |
| `source/scripts/action_page_fk.py` | 1–80 | FK tool documentation and usage warnings |
| `source/scripts/op3_ping.py` | 1–80 | Ping tool documentation and error decoding |
| `drafts/DIFFERENCES.md` | 1–171 | Changed/absent file inventory |
| `drafts/FOCUSED-INDEX.md` | 1–60 | Cross-reference to sibling drafts |
| `drafts/SHARED-INDEX.md` | 1–21 | Published shared-card links |
