> Shared file-content analysis, using the Alphonse snapshot. Robot-specific runtime conditions require separate review.

# Focus Card: Shared Joystick and Teleoperation — op3_joy_teleop

> **Scope**: Representative investigation of the shared package `op3_joy_teleop` (stage: shared-core).  
> **Canonical snapshot**: Alphonse, branch `ALPHONSE_NEW_V2`, commit `adacde8f6e01e6439d170fb6bce025acc051bfa3`.  
> Same SHA-256 content appears across Alphonse, Chronus, and Orion snapshots, but runtime equivalence is **not** established.

---

## 1. Package Overview

`op3_joy_teleop` is an Ament Python ROS 2 package (version 0.1.0, Apache-2.0) that bridges a gamepad controller to the OP3 walking module via ROS 2 topics and parameters [source/src/op3_joy_teleop/package.xml:L1-L24](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_joy_teleop/package.xml#L1-L24). It depends on standard ROS 2 libraries (`rclpy`, `sensor_msgs`, `std_msgs`), the `joy` driver package, and custom message packages `op3_walking_module_msgs` and `robotis_controller_msgs` [source/src/op3_joy_teleop/package.xml:L11-L16](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_joy_teleop/package.xml#L11-L16).

---

## 2. Launch Configuration

The launch file `op3_joy_teleop.launch.py` starts two nodes:

| Node | Package | Executable | Role |
|---|---|---|---|
| `joy_node` | `joy` | `joy_node` | Reads hardware gamepad input and publishes `/joy` messages |
| `op3_joy_teleop` | `op3_joy_teleop` | `op3_joy_teleop` | Translates joystick/gamepad input into walking and action commands |

The launch file exposes three configurable parameters [source/src/op3_joy_teleop/launch/op3_joy_teleop.launch.py:L14-L28](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_joy_teleop/launch/op3_joy_teleop.launch.py#L14-L28):

- **`config`**: Path to a YAML configuration file (default: `config/op3_joy_teleop.yaml` under the package share directory).
- **`joy_deadzone`**: Deadzone threshold for the `joy_node` (default: `0.05`).
- **`joy_autorepeat_rate`**: Autorepeat rate for `joy_node` (default: `30.0` Hz).

The configuration file is loaded as ROS 2 parameters into the teleop node [source/src/op3_joy_teleop/launch/op3_joy_teleop.launch.py:L42-L47](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_joy_teleop/launch/op3_joy_teleop.launch.py#L42-L47).

---

## 3. Observed Behavior — Kick Subsystem

The companion document `HOW_TO_KICK.md` [source/src/op3_joy_teleop/HOW_TO_KICK.md:L1-L154](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_joy_teleop/HOW_TO_KICK.md#L1-L154) describes the kicking interaction in detail:

### Deadman Switch Contract
- **L1 (button 6)** acts as a deadman switch. Walking requires L1 to be **held**[source/src/op3_joy_teleop/HOW_TO_KICK.md:L38](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_joy_teleop/HOW_TO_KICK.md#L38). Kicking requires L1 to be **released** [source/src/op3_joy_teleop/HOW_TO_KICK.md:L7-L18](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_joy_teleop/HOW_TO_KICK.md#L7-L18).
- A config parameter `require_deadman_released_for_kick: true` enforces this at the code level [source/src/op3_joy_teleop/HOW_TO_KICK.md:L10-L12](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_joy_teleop/HOW_TO_KICK.md#L10-L12).
- The implementation checks `self._deadman_active` and suppresses kick triggers while the deadman is held [source/src/op3_joy_teleop/HOW_TO_KICK.md:L14-L18](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_joy_teleop/HOW_TO_KICK.md#L14-L18).

### Kick Activation Sequence
1. **Release L1** to exit walking mode.
2. **Long-press Y (button 4)** for **0.5 seconds** to enter kick mode. A timeout window of **2.0 seconds** follows.
3. Press **L2 (button 8)** for a left kick (page 104) or **R2 (button 9)** for a right kick (page 218) [source/src/op3_joy_teleop/HOW_TO_KICK.md:L30-L32](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_joy_teleop/HOW_TO_KICK.md#L30-L32), [source/src/op3_joy_teleop/HOW_TO_KICK.md:L36-L42](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_joy_teleop/HOW_TO_KICK.md#L36-L42).
4. A **1.0-second cooldown** enforces minimum spacing between kicks. A **5.0-second timeout** aborts stale kick attempts [source/src/op3_joy_teleop/HOW_TO_KICK.md:L59-L61](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_joy_teleop/HOW_TO_KICK.md#L59-L61).

### ROS 2 Monitoring Topics
For debugging (commands cited from source; **not executed**), the document references [source/src/op3_joy_teleop/HOW_TO_KICK.md:L66-L93](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_joy_teleop/HOW_TO_KICK.md#L66-L93):
- `/robotis/enable_ctrl_module` — shows action module status
- `/robotis/action/page_num` — reports kick page number (104/left, 218/right)
- `/robotis/movement_done` — signals action completion
- `/joy` — raw joy topic for button state verification

---

## 4. Configuration Surface

| Parameter | Source (default) | Purpose |
|---|---|---|
| `require_deadman_released_for_kick` | config, true | Gating: kick only when deadman is off |
| `joy_deadzone` | launch, 0.05 | Filter small joystick drift |
| `joy_autorepeat_rate` | launch, 30.0 | Joystick input repeat rate |
| left kick page | config, 104 | Action module page for left kick |
| right kick page | config, 218 | Action module page for right kick |

Full parameter values live in `config/op3_joy_teleop.yaml`, which was **not read** to avoid branch-specific configuration drift (per correction note). The YAML is loaded via the `config` launch argument [source/src/op3_joy_teleop/launch/op3_joy_teleop.launch.py:L14-L18](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_joy_teleop/launch/op3_joy_teleop.launch.py#L14-L18).

---

## 5. Untested Operation Notes

- The `__init__.py` file is empty [source/src/op3_joy_teleop/op3_joy_teleop/__init__.py:L1](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_joy_teleop/op3_joy_teleop/__init__.py#L1); the package appears to rely on a `setup.py` or `setup.cfg` entry point (not assigned here) to register the `op3_joy_teleop` executable. The actual node logic is presumably in a separate module (likely `teleop_node.py` per the filesystem layout), which was **not inspected** to avoid branch-specific divergence.
- The `joy_node` is from the upstream `joy` package, not part of this shared code.
- No claims are made about correct operation on any specific physical robot or in Webots simulation. Timing constants (0.5 s long-press, 2.0 s window, 1.0 s cooldown, 5.0 s timeout) are documented values only [source/src/op3_joy_teleop/HOW_TO_KICK.md:L59-L61](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_joy_teleop/HOW_TO_KICK.md#L59-L61).

---

## 6. Uncertainties and Conflicts

| Issue | Detail |
|---|---|
| **Exec entry point unknown** | The `setup.py` was not assigned; we cannot confirm how `op3_joy_teleop` is registered as an executable. |
| **Core teleop logic unread** | The primary node implementation was not read. Our understanding of deadman, kick mode, and axis mapping comes entirely from `HOW_TO_KICK.md`. |
| **Config values assumed** | Page numbers, timing, and deadman toggle are cited from `HOW_TO_KICK.md` references to external config/code — not independently verified. |
| **L2/R2 reuse conflict** | Setting `require_deadman_released_for_kick: false` may conflict with L2/R2 being used for turning [source/src/op3_joy_teleop/HOW_TO_KICK.md:L129-L130](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_joy_teleop/HOW_TO_KICK.md#L129-L130). |
| **Cross-robot equivalence** | Identical SHA-256 content across Alphonse/Chronus/Orion does **not** imply identical hardware integration or calibration. |

---

## 7. Sources

- [source/src/op3_joy_teleop/package.xml:L1-L24](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_joy_teleop/package.xml#L1-L24)
- [source/src/op3_joy_teleop/launch/op3_joy_teleop.launch.py:L1-L51](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_joy_teleop/launch/op3_joy_teleop.launch.py#L1-L51)
- [source/src/op3_joy_teleop/op3_joy_teleop/__init__.py:L1](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_joy_teleop/op3_joy_teleop/__init__.py#L1)
- [source/src/op3_joy_teleop/HOW_TO_KICK.md:L1-L154](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_joy_teleop/HOW_TO_KICK.md#L1-L154)

*Files not examined*: `config/op3_joy_teleop.yaml`, `op3_joy_teleop/teleop_node.py`, `setup.py` — excluded per scope guidance to avoid branch-specific configuration drift.
