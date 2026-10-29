> Shared file-content analysis, using the Alphonse snapshot. Robot-specific runtime conditions require separate review.

# Shared Code: ROS Messages and Service Interfaces

**Project:** Alphonse (canonical snapshot) | **Branch:** `ALPHONSE_NEW_V2` | **Commit:** `adacde8f6e01e6439d170fb6bce025acc051bfa3`
**Stage:** shared-core | **Scope:** 8 shared-type definitions across two ROS message packages

---

## 1 Scope and Coverage

This card documents four ROS message and service definition files selected as representative anchors from the shared-core stage. They live inside two packages:

| Package | Type | File | Lines |
|---|---|---|---|
| `robotis_controller_msgs` | msg | `JointCtrlModule.msg` | [source/src/ROBOTIS-Framework-msgs/robotis_controller_msgs/msg/JointCtrlModule.msg:L1-L2](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Framework-msgs/robotis_controller_msgs/msg/JointCtrlModule.msg#L1-L2) |
| `robotis_controller_msgs` | srv | `SetJointModule.srv` | [source/src/ROBOTIS-Framework-msgs/robotis_controller_msgs/srv/SetJointModule.srv:L1-L4](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Framework-msgs/robotis_controller_msgs/srv/SetJointModule.srv#L1-L4) |
| `robotis_controller_msgs` | msg | `StatusMsg.msg` | [source/src/ROBOTIS-Framework-msgs/robotis_controller_msgs/msg/StatusMsg.msg:L1-L10](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Framework-msgs/robotis_controller_msgs/msg/StatusMsg.msg#L1-L10) |
| `op3_online_walking_module_msgs` | msg | `WalkingParam.msg` | [source/src/ROBOTIS-OP3-msgs/op3_online_walking_module_msgs/msg/WalkingParam.msg:L1-L5](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-msgs/op3_online_walking_module_msgs/msg/WalkingParam.msg#L1-L5) |

All four files are small (2–10 lines each); they were read in full, so no content was skipped. Three additional search calls (glob, glob, grep) were performed to look for cross-references and variant definitions:

- No `*.cpp`, `*.h`, `*.hpp`, or `*.launch` files in the `source/src` tree reference `JointCtrlModule`, `SetJointModule`, `WalkingParam`, or `StatusMsg` by name.
- No `msg` stub subdirectories contain generated C++ header variants for these types.

This is a **representative** investigation. 78 matching shared candidates exist; only the four anchors above are assigned. Runtime equivalence across Alphonse, Chronus, and Orion is **not established** by inspection of message definitions alone.

---

## 2 Interfaces and Observed Behavior

### 2.1 `JointCtrlModule.msg`
[source/src/ROBOTIS-Framework-msgs/robotis_controller_msgs/msg/JointCtrlModule.msg:L1-L2](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Framework-msgs/robotis_controller_msgs/msg/JointCtrlModule.msg#L1-L2)

A flat message carrying two parallel string arrays:
- `string[] joint_name`
- `string[] module_name`

The contract implied by the names is that each joint at index *i* is associated with the controller module at the same index. There is no explicit length constraint or key field; the consumer is responsible for length correspondence.

### 2.2 `SetJointModule.srv`
[source/src/ROBOTIS-Framework-msgs/robotis_controller_msgs/srv/SetJointModule.srv:L1-L4](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Framework-msgs/robotis_controller_msgs/srv/SetJointModule.srv#L1-L4)

A service interface with the same two string arrays as the request, separated by `---`, and returning a single `bool result`. The request fields match `JointCtrlModule.msg` field-for-field, suggesting that the service reuses the same pairing convention. The response is a bare success/failure flag; there is no error string or partial-result field.

### 2.3 `StatusMsg.msg`
[source/src/ROBOTIS-Framework-msgs/robotis_controller_msgs/msg/StatusMsg.msg:L1-L10](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Framework-msgs/robotis_controller_msgs/msg/StatusMsg.msg#L1-L10)

A status-reporting message that defines four enumerated constants:

| Constant | Value | Source lines |
|---|---|---|
| `STATUS_UNKNOWN` | 0 | [source/src/ROBOTIS-Framework-msgs/robotis_controller_msgs/msg/StatusMsg.msg:L2](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Framework-msgs/robotis_controller_msgs/msg/StatusMsg.msg#L2) |
| `STATUS_INFO` | 1 | [source/src/ROBOTIS-Framework-msgs/robotis_controller_msgs/msg/StatusMsg.msg:L3](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Framework-msgs/robotis_controller_msgs/msg/StatusMsg.msg#L3) |
| `STATUS_WARN` | 2 | [source/src/ROBOTIS-Framework-msgs/robotis_controller_msgs/msg/StatusMsg.msg:L4](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Framework-msgs/robotis_controller_msgs/msg/StatusMsg.msg#L4) |
| `STATUS_ERROR` | 3 | [source/src/ROBOTIS-Framework-msgs/robotis_controller_msgs/msg/StatusMsg.msg:L5](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Framework-msgs/robotis_controller_msgs/msg/StatusMsg.msg#L5) |

Payload fields:
- `std_msgs/Header header` — ROS timestamp and frame.
- `uint8 type` — one of the four constants above.
- `string module_name` — identifies the originating module.
- `string status_msg` — the human-readable text payload.

### 2.4 `WalkingParam.msg`
[source/src/ROBOTIS-OP3-msgs/op3_online_walking_module_msgs/msg/WalkingParam.msg:L1-L5](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-msgs/op3_online_walking_module_msgs/msg/WalkingParam.msg#L1-L5)

Five `float64` fields parameterizing an online walking controller:

| Field | Type | Likely meaning |
|---|---|---|
| `dsp_ratio` | float64 | Double-support-phase ratio |
| `lipm_height` | float64 | Linear Inverted Pendulum Model height |
| `foot_height_max` | float64 | Maximum foot lift height |
| `zmp_offset_x` | float64 | ZMP offset on the sagittal axis |
| `zmp_offset_y` | float64 | ZMP offset on the frontal axis |

No default values, bounds, or units are declared in the definition itself. The naming strongly implies a ZMP-based bipedal walking strategy.

---

## 3 Configuration and Dependencies

- `StatusMsg.msg` imports `std_msgs/Header`, establishing a dependency on the standard `std_msgs` ROS package.
- No `CMakeLists.txt` or `package.xml` files were assigned or read for these packages; build-time and dependency graphs are not captured here.
- No numeric calibration values (ZMP offsets, joint angles, etc.) appear in these definition files. Any such values would reside in configuration YAML or launch files not covered by this scope.

---

## 4 Untested Operation Notes

The following commands were identified as typical operational procedures for working with ROS messages but were **found only in source context and not executed**:

| Operation | Status |
|---|---|
| Compiling the message packages via `catkin_make` or `colcon build` | Not executed |
| Publishing a `WalkingParam` message on the correct topic | Not executed |
| Calling the `SetJointModule` service | Not executed |
| Monitoring `StatusMsg` on a status topic | Not executed |

None of these operations were performed. There is no evidence of actual runtime behavior, correct topic naming, or message serialization.

---

## 5 Uncertainties and Conflicts

1. **No cross-references found.** Grep of the `source/src` tree turned up zero consumer references to any of the four types. They may be used in packages outside the scanned path, or they may be defined but currently dormant.
2. **No length invariant on parallel arrays.** `JointCtrlModule.msg` and `SetJointModule.srv` rely on equal-length arrays but encode no constraint. A consumer receiving mismatched lengths would have undefined behavior.
3. **Units are unspecified.** The five fields of `WalkingParam.msg` carry no unit annotations. Values imported from simulation (e.g., Webots) cannot be confidently transferred to physical hardware without separate calibration.
4. **Shared content ≠ runtime equivalence.** The same SHA-256 bytes exist across the three robot snapshots (Alphonse, Chronus, Orion) for these files, but this only proves source text identity. Runtime loading, node topology, and module implementations differ between robots and are not covered.
5. **Only four of 78 candidates examined.** Unexamined shared definitions may define additional contracts or reveal inconsistencies not visible here.

---

## 6 Sources

| # | Path | Lines |
|---|---|---|
| 1 | `source/src/ROBOTIS-Framework-msgs/robotis_controller_msgs/msg/JointCtrlModule.msg` | L1-L2 |
| 2 | `source/src/ROBOTIS-Framework-msgs/robotis_controller_msgs/srv/SetJointModule.srv` | L1-L4 |
| 3 | `source/src/ROBOTIS-Framework-msgs/robotis_controller_msgs/msg/StatusMsg.msg` | L1-L10 |
| 4 | `source/src/ROBOTIS-OP3-msgs/op3_online_walking_module_msgs/msg/WalkingParam.msg` | L1-L5 |
