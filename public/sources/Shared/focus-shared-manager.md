> Shared file-content analysis, using the Alphonse snapshot. Robot-specific runtime conditions require separate review.

# Focus: Shared Manager and Hardware Bringup

Stage: **shared-core** | Snapshot: **ALPHONSE_NEW_V2** commit `adacde8f6e`

| Robot | Status |
|-------|--------|
| Alphonse | Canonical source snapshot |
| Chronus | Identical SHA-256 content in assigned paths |
| Orion | Identical SHA-256 content in assigned paths |

Runtime equivalence across robots is **not established**. This card documents code contracts only.

---

## 1 Scope

This card covers the `op3_manager` ROS 2 package — a single-executable node that orchestrates hardware bringup for an OP3 family robot. Four source artefacts were inspected:

| File | Role | Lines |
|------|------|-------|
| `package.xml` | Package manifest, dependency declaration | [source/src/ROBOTIS-OP3/op3_manager/package.xml:L1-L47](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/package.xml#L1-L47) |
| `CMakeLists.txt` | Build configuration, linkage | [source/src/ROBOTIS-OP3/op3_manager/CMakeLists.txt:L1-L106](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/CMakeLists.txt#L1-L106) |
| `config/offset.yaml` | Default joint offset calibration values | [source/src/ROBOTIS-OP3/op3_manager/config/offset.yaml:L1-L42](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/config/offset.yaml#L1-L42) |
| `launch/op3_simulation.launch.py` | Simulation launch entry point | [source/src/ROBOTIS-OP3/op3_manager/launch/op3_simulation.launch.py:L1-L29](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/launch/op3_simulation.launch.py#L1-L29) |

The compiled executable `op3_manager` is built from **one source file** — `src/op3_manager.cpp` [source/src/ROBOTIS-OP3/op3_manager/CMakeLists.txt:L70](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/CMakeLists.txt#L70) — which is a branch-specific implementation file and was **not** inspected for this shared card. An additional launch file `op3_manager.launch.py` exists [glob result: launch directory scan] but was not assigned for reading.

---

## 2 Observed Behaviour

### 2.1 Package Identity

The package declares itself as version `0.2.1` under an Apache 2.0 license, authored for the ROBOTIS OP3 platform [source/src/ROBOTIS-OP3/op3_manager/package.xml:L4-L8](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/package.xml#L4-L8). It is an ROS 2 (Humble or later) package using `ament_cmake` as its build system [source/src/ROBOTIS-OP3/op3_manager/package.xml:L16](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/package.xml#L16), [source/src/ROBOTIS-OP3/op3_manager/package.xml:L44-L46](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/package.xml#L44-L46).

### 2.2 Dependency Footprint

The manager depends on **22 compile-time ROS 2 and library packages** and **1 additional runtime dependency**:

- **Core ROS 2**: `rclcpp`, `std_srvs`, `ament_index_cpp` [source/src/ROBOTIS-OP3/op3_manager/package.xml:L18-L20](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/package.xml#L18-L20)
- **Dynamixel SDK**: `dynamixel_sdk` for DirectX motor communication [source/src/ROBOTIS-OP3/op3_manager/package.xml:L25](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/package.xml#L25)
- **ROBOTIS framework**: A family of internal packages — `robotis_framework_common`, `robotis_device`, `robotis_controller`, `robotis_math` — plus controller-specific ROS interfaces (`robotis_controller_msgs`) [source/src/ROBOTIS-OP3/op3_manager/package.xml:L21-L29](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/package.xml#L21-L29)
- **OP3 domain modules**: Kinematics, balance, walking, action, head control, direct control, online walking, tuning, and base modules (with corresponding `*_msgs` message packages) [source/src/ROBOTIS-OP3/op3_manager/package.xml:L30-L41](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/package.xml#L30-L41)
- **OpenCR hardware bridge**: `open_cr_module` [source/src/ROBOTIS-OP3/op3_manager/package.xml:L32](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/package.xml#L32)
- **Runtime-only**: `op3_localization` (exec_depend) [source/src/ROBOTIS-OP3/op3_manager/package.xml:L42](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/package.xml#L42)

This breadth of dependencies indicates that `op3_manager` acts as a **supervisor node** that instantiates or communicates with all sub-systems rather than implementing their logic inline.

### 2.3 Build Configuration

The `CMakeLists.txt` resolves every dependency via `find_package` [source/src/ROBOTIS-OP3/op3_manager/CMakeLists.txt:L4-L27](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/CMakeLists.txt#L4-L27) and uses `yaml-cpp` (version ≥ 0.5 detected at build time) [source/src/ROBOTIS-OP3/op3_manager/CMakeLists.txt:L29-L42](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/CMakeLists.txt#L29-L42) for YAML configuration parsing. All include directories are forwarded to the single executable target [source/src/ROBOTIS-OP3/op3_manager/CMakeLists.txt:L44-L68](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/CMakeLists.txt#L44-L68). The binary is installed to `lib/op3_manager` and the `config/` and `launch/` directories are installed to `share/op3_manager` [source/src/ROBOTIS-OP3/op3_manager/CMakeLists.txt:L98-L104](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/CMakeLists.txt#L98-L104).

### 2.4 Default Joint Offsets

The file `config/offset.yaml` defines a flat structure with two top-level keys [source/src/ROBOTIS-OP3/op3_manager/config/offset.yaml:L1-L42](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/config/offset.yaml#L1-L42):

- **`offset`**: Per-joint zero-offset corrections for **21 joints** (head, left arm, left leg, right arm, right leg). All values default to `0` [source/src/ROBOTIS-OP3/op3_manager/config/offset.yaml:L2-L21](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/config/offset.yaml#L2-L21).
- **`init_pose_for_offset_tuner`**: Identical 21-joint pose definition, also all zeros, intended as a starting posture for an offset calibration tool [source/src/ROBOTIS-OP3/op3_manager/config/offset.yaml:L22-L42](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/config/offset.yaml#L22-L42).

**These are shared default values. They are NOT robot-specific calibrations.** Actual per-unit offsets must be determined by a calibration or tuning procedure on the physical robot and stored in a local override file. Do not transfer offset values between robots.

### 2.5 Simulation Launch File

The launch file `op3_simulation.launch.py` declares a single `op3_manager` node with the following parameter defaults [source/src/ROBOTIS-OP3/op3_manager/launch/op3_simulation.launch.py:L14-L29](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/launch/op3_simulation.launch.py#L14-L29):

| Parameter | Default Value | Source |
|-----------|---------------|--------|
| `simulation` | `True` | [source/src/ROBOTIS-OP3/op3_manager/launch/op3_simulation.launch.py:L7](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/launch/op3_simulation.launch.py#L7) |
| `simulation_robot_name` | `'robotis_op3'` | [source/src/ROBOTIS-OP3/op3_manager/launch/op3_simulation.launch.py:L8](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/launch/op3_simulation.launch.py#L8) |
| `offset_file_path` | share dir + `/config/offset.yaml` | [source/src/ROBOTIS-OP3/op3_manager/launch/op3_simulation.launch.py:L9](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/launch/op3_simulation.launch.py#L9) |
| `robot_file_path` | share dir + `/config/OP3.robot` | [source/src/ROBOTIS-OP3/op3_manager/launch/op3_simulation.launch.py:L10](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/launch/op3_simulation.launch.py#L10) |
| `init_file_path` | share dir + `/config/dxl_init_OP3.yaml` | [source/src/ROBOTIS-OP3/op3_manager/launch/op3_simulation.launch.py:L11](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/launch/op3_simulation.launch.py#L11) |
| `device_name` | `'/dev/ttyUSB0'` | [source/src/ROBOTIS-OP3/op3_manager/launch/op3_simulation.launch.py:L12](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/launch/op3_simulation.launch.py#L12) |

This launch file is intended for **Webots or ROS 2 simulation** mode. The `simulation: True` parameter indicates the node should avoid opening real serial ports. The `device_name` parameter (`/dev/ttyUSB0`) would be irrelevant in simulation but is provided as a compile-time default.

An untested suggestion for running this launch is:
```
ros2 launch op3_manager op3_simulation.launch.py
```
**This command was found by reading the source but was not executed.**

---

## 3 Interfaces and Configuration

### 3.1 ROS 2 Parameters

The manager exposes six configurable parameters at node startup, discoverable from the launch file [source/src/ROBOTIS-OP3/op3_manager/launch/op3_simulation.launch.py:L20-L27](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/launch/op3_simulation.launch.py#L20-L27):

1. **`simulation`** (`bool`): When true, the node operates against simulated hardware. When false, it attempts to communicate with physical Dynamixel servos via the OpenCR board.
2. **`simulation_robot_name`** (`string`): The identifier of the simulated robot model.
3. **`offset_file_path`** (`string`): Absolute path to the YAML file containing joint offset values.
4. **`robot_file_path`** (`string`): Path to the `.robot` descriptor file defining joint topology and Dynamixel IDs.
5. **`init_file_path`** (`string`): Path to the YAML file specifying per-servo initialization parameters (mode, torque enable, goal position, etc.).
6. **`device_name`** (`string`): Serial device path for the OpenCR board.

### 3.2 Configuration Files Not Inspected

Two additional configuration files are referenced by the launch file but were **not assigned for reading**:

- `config/OP3.robot` — referenced at [source/src/ROBOTIS-OP3/op3_manager/launch/op3_simulation.launch.py:L10](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/launch/op3_simulation.launch.py#L10)
- `config/dxl_init_OP3.yaml` — referenced at [source/src/ROBOTIS-OP3/op3_manager/launch/op3_simulation.launch.py:L11](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/launch/op3_simulation.launch.py#L11)

Their contents and structure are unknown to this card.

---

## 4 Untested Operation Notes

The following commands are derived solely from reading configuration and launch files. They have **not been executed or verified**:

- `ros2 launch op3_manager op3_simulation.launch.py` — launches the manager in simulation mode [source/src/ROBOTIS-OP3/op3_manager/launch/op3_simulation.launch.py:L14-L29](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/launch/op3_simulation.launch.py#L14-L29).
- A second (non-simulation) launch file `op3_manager.launch.py` exists in the launch directory [glob result] and likely sets `simulation: False` to communicate with physical hardware. It was **not inspected**.

The simulation mode (`simulation: True`) runs against a Webots or Gazebo virtual robot. The parameter `simulation_robot_name: 'robotis_op3'` is passed to the node and presumably selected for loading a simulation model. Physical hardware behavior is gated by `simulation: False` and the `device_name` parameter. The two modes have different failure modes — simulation may fail if the model is not found in the simulation environment; physical mode may fail if the serial port is unavailable or Dynamixel bus is unresponsive.

---

## 5 Uncertainty and Conflicts

| Issue | Detail |
|-------|--------|
| **Unread source file** | The single implementation file `src/op3_manager.cpp` [source/src/ROBOTIS-OP3/op3_manager/CMakeLists.txt:L70](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/CMakeLists.txt#L70) was **not inspected** to comply with shared-card scope rules. All behavioural claims above are inferred from build dependencies, parameter declarations, and config file structure. |
| **Second launch file unexamined** | `op3_manager.launch.py` exists but was not assigned; its parameter defaults are unknown. |
| **Robot config files unexamined** | `OP3.robot` and `dxl_init_OP3.yaml` are referenced but unread. |
| **Offset calibration ownership** | The `offset.yaml` values are all zero defaults. It is unclear whether these are meant to be overridden per-unit or whether a tuning module writes them back. The dependency `op3_tuning_module` [source/src/ROBOTIS-OP3/op3_manager/package.xml:L39](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/package.xml#L39) suggests the latter. |
| **Cross-robot equivalence** | While SHA-256 hashes of the assigned files match across Alphonse, Chronus, and Orion, runtime equivalence depends on the unexamined implementation file and any robot-specific launch overrides. |

---

## 6 Sources

All paths are relative to the workspace root.

1. [source/src/ROBOTIS-OP3/op3_manager/package.xml:L1-L47](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/package.xml#L1-L47) — Package manifest and dependency list.
2. [source/src/ROBOTIS-OP3/op3_manager/CMakeLists.txt:L1-L106](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/CMakeLists.txt#L1-L106) — Build system configuration.
3. [source/src/ROBOTIS-OP3/op3_manager/config/offset.yaml:L1-L42](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/config/offset.yaml#L1-L42) — Default joint offset configuration.
4. [source/src/ROBOTIS-OP3/op3_manager/launch/op3_simulation.launch.py:L1-L29](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/launch/op3_simulation.launch.py#L1-L29) — Simulation launch entry point and parameter defaults.
