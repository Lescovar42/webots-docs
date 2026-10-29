# Orion Architecture, Interfaces, and Configuration Guide

> **Scope:** Orion branch `ORION_NEW` (commit `dba5be3fefbada854b8d6c11d6655f479b482574`).  
> **Status:** Draft — all commands are untested suggestions. No build or runtime was performed.

---

## 1 Overview

The Orion robot software follows a **supervisor-node architecture** in which a single ROS 2 node (`op3_manager`) orchestrates hardware bringup, sensor fusion, and all motion sub-systems for an OP3-family biped. The compiled executable is built from one source file — `op3_manager.cpp` ([source/src/ROBOTIS-OP3/op3_manager/src/op3_manager.cpp:L1-L464](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/src/op3_manager.cpp#L1-L464)) — linked against the shared ROBOTIS Framework libraries.

Three conceptual layers compose the stack:

| Layer | Role | Assigned source |
|---|---|---|
| **Supervisor / Manager** | ROS 2 node lifecycle, parameter loading, module registration, hardware callbacks | `op3_manager.cpp`, `op3_manager.launch.py` |
| **Controller & Device** | Serial port management, DYNAMIXEL read/ping/write, control-table access | `robotis_controller.h`, [shared card](../Shared/focus-shared-framework.md) |
| **Motion & Sensor Modules** | Walking, balance, head control, actions, direct control, online walking, tuning, OpenCR sensor bus | Internal packages (dependencies declared in [shared card](../Shared/focus-shared-manager.md)) |

---

## 2 Prerequisites

To use the instructions below, the workspace must be built with `colcon` under ROS 2 Humble (or later). The manager declares **22 compile-time** and **1 runtime** dependency, covering `rclcpp`, the Dynamixel SDK, the framework stack (`robotis_controller`, `robotis_device`, `robotis_framework_common`, `robotis_math`), and every OP3 domain module ([shared card](../Shared/focus-shared-manager.md)).

---

## 3 Boot Sequence (Physical Robot)

The following ordered steps describe observed behaviour during node startup on a physical robot.

1. **Serial port discovery.** The launch file scans `/dev/ttyUSB0`–`/dev/ttyUSB9` for the first openable port and patches the robot configuration file at launch time so that the controller opens the same device [source/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py:L22-L37](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py#L22-L37), [source/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py:L40-L58](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py#L40-L58). The `OP3_DEVICE` environment variable overrides auto-detection [source/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py:L28-L30](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py#L28-L30).

2. **Node and parameters initialize.** `main()` creates an `rclcpp::Node` and declares parameters for `simulation`, `robot_file_path`, `init_file_path`, `offset_file_path`, and `device_name` [source/src/ROBOTIS-OP3/op3_manager/src/op3_manager.cpp:L2-L20](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/src/op3_manager.cpp#L2-L20).

3. **Hardware connection.** If `simulation == false`, the node obtains a `RobotisController` singleton and calls connection routines [source/src/ROBOTIS-OP3/op3_manager/src/op3_manager.cpp:L20-L30](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/src/op3_manager.cpp#L20-L30). Torque is cycled and the OpenCR RGB LED is set to green [source/src/ROBOTIS-OP3/op3_manager/src/op3_manager.cpp:L321-L340](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/src/op3_manager.cpp#L321-L340).

4. **Controller initialization.** The robot description YAML (`OP3.robot`), the joint-initialization file (`dxl_init_OP3.yaml`), and an optional offset file are passed to `controller->initialize()` [source/src/ROBOTIS-OP3/op3_manager/src/op3_manager.cpp:L358-L367](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/src/op3_manager.cpp#L358-L367).

5. **Module registration.** Eight motion/sensor modules are registered with the controller in this order: OpenCR sensor, Action, Base, Head Control, Walking, Direct Control, Online Walking, and Tuning [source/src/ROBOTIS-OP3/op3_manager/src/op3_manager.cpp:L371-L381](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/src/op3_manager.cpp#L371-L381).

6. **Timer and init pose.** The controller timer starts and the node transitions to action page 2 (`WALKING_READY`) — an upright standing posture — [source/src/ROBOTIS-OP3/op3_manager/src/op3_manager.cpp:L383-L390](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/src/op3_manager.cpp#L383-L390).

7. **Health check service.** A `/robotis/health_check` ROS 2 service (standard `Trigger` interface) is created. Calling it pings every DYNAMIXEL on the bus and returns a JSON payload listing `ok`, `failed`, and per-joint error strings [source/src/ROBOTIS-OP3/op3_manager/src/op3_manager.cpp:L392-L457](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/src/op3_manager.cpp#L392-L457). In simulation mode, the service returns a skipped-response immediately [source/src/ROBOTIS-OP3/op3_manager/src/op3_manager.cpp:L399-L404](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/src/op3_manager.cpp#L399-L404).

8. **Spin.** The node enters `rclcpp::spin()` [source/src/ROBOTIS-OP3/op3_manager/src/op3_manager.cpp:L460](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/src/op3_manager.cpp#L460).

---

## 4 Boot Sequence (Simulation)

When the `simulation` parameter is `True` (default in `op3_simulation.launch.py` per the [shared card](../Shared/focus-shared-manager.md)), the hardware connection step is skipped, the node logs a warning, and the `simulation_robot_name` parameter is transferred to the controller's Gazebo name field [source/src/ROBOTIS-OP3/op3_manager/src/op3_manager.cpp:L341-L350](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/src/op3_manager.cpp#L341-L350). Module registration and the init-pose transition proceed identically.

---

## 5 Interfaces

### 5.1 Configuration Files

| File | Role | Key content |
|---|---|---|
| `OP3.robot` | Robot description | 20 DYNAMIXEL joints (IDs 1–20, model XM430-W350, Protocol 2.0) plus one OpenCR sensor device (ID 200); control cycle 8 ms [source/src/ROBOTIS-OP3/op3_manager/config/OP3.robot:L1-L30](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/config/OP3.robot#L1-L30) |
| `dxl_init_OP3.yaml` | Joint initialization | Per-joint position limits (0–4095 raw), operating mode 3 (position mode), P-gain 800, D/I gain 0, return delay 1. Five shoulder joints carry a `shutdown: 56` entry [source/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml:L1-L166](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml#L1-L166) |
| `offset.yaml` | Calibration offsets | 21-joint zero-offset values (head + 20 actuators), all defaulting to 0 [shared card](../Shared/focus-shared-manager.md) |

### 5.2 ROS 2 Services and Topics

- **`/robotis/health_check`** — `std_srvs/srv/Trigger`: returns JSON diagnostic payload [source/src/ROBOTIS-OP3/op3_manager/src/op3_manager.cpp:L392-L457](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/src/op3_manager.cpp#L392-L457).
- Module-specific services and topics are exposed through the framework's message package. See [shared card](../Shared/focus-shared-messages.md) for the full message and service type catalog.
- Walking and balance topics are described in [shared card](../Shared/focus-shared-walking.md).

### 5.3 Controller API Surface

The `RobotisController` class exposes DYNAMIXEL primitives: `ping`, `read`, `write`, `regWrite`, `readCtrlItem`, `writeCtrlItem` [source/src/ROBOTIS-Framework/robotis_controller/include/robotis_controller/robotis_controller.h:L1-L188](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-Framework/robotis_controller/include/robotis_controller/robotis_controller.h#L1-L188). These are the building blocks for every motion module registered in the manager.

---

## 6 Untested Operation Notes

- **No build or runtime was performed.** All commands below are untested suggestions.
- **Detected device auto-patching** writes a temporary `.robot` file via `tempfile.mkstemp()` and registers cleanup through `atexit` [source/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py:L40-L58](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py#L40-L58). If the process is killed (SIGKILL/SIGSEGV), the temp file may persist.
- **Offset values are shared defaults.** Do not transfer calibration offsets or per-robot PID values between physical units. See [shared card](../Shared/focus-shared-manager.md) and [shared card](../Shared/focus-shared-framework.md).

Untested suggestion — physical launch with auto-detected port:
```bash
ros2 launch op3_manager op3_manager.launch.py
```

Untested suggestion — force a specific device:
```bash
OP3_DEVICE=/dev/ttyUSB1 ros2 launch op3_manager op3_manager.launch.py
```

---

## 7 Uncertainty and Conflicts

- **Offset file path resolution:** The parameter `offset_file_path` defaults to a share-directory path at launch-time; if the file is empty string, `loadOffset()` is skipped silently [source/src/ROBOTIS-OP3/op3_manager/src/op3_manager.cpp:L366-L367](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/src/op3_manager.cpp#L366-L367). It is unclear whether a missing file at launch is caught earlier.
- **Gazebo vs Webots:** The manager distinguishes a boolean `gazebo` parameter and a `gazebo_robot_name` string [source/src/ROBOTIS-OP3/op3_manager/src/op3_manager.cpp:L14-L15](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/src/op3_manager.cpp#L14-L15), but the simulation card is Webots-focused per [shared card](../Shared/focus-shared-webots.md). The interaction between Gazebo-mode and Webots-mode has not been resolved.
- **Controller implementation gap:** The `robotis_controller.h` header was inspected, but the controller's `initialize()` method implementation and the `DeviceManager` class were not. See [shared card](../Shared/focus-shared-framework.md) for details on unexamined source.
- **Shared-card coverage applies to Alphonse baseline.** Identical SHA-256 content exists in Orion, but runtime equivalence is not established.

---

## 8 See Also

- [Shared Manager card](../Shared/focus-shared-manager.md) — package manifest, dependency tree, defaults
- [Shared Framework card](../Shared/focus-shared-framework.md) — device abstraction, PID state, clamping removal
- [Shared Messages card](../Shared/focus-shared-messages.md) — ROS message and service catalog
- [Shared Walking card](../Shared/focus-shared-walking.md) — gait parameters and balance loop
- [Focused Differences](./DIFFERENCES.md) — deterministic file differences against Alphonse baseline
