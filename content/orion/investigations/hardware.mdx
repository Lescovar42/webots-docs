> Branch ORION_NEW, commit `dba5be3fefbada854b8d6c11d6655f479b482574`. Robot-specific hardware and device configuration.

# Orion: Hardware, Device and Calibration Differences

**Stage:** robot-differences &nbsp;|&nbsp; **Branch:** ORION_NEW &nbsp;|&nbsp; **Scope:** Representative investigation

> **GUIDES-FIRST SCOPE NOTE** — Two candidate files were assigned for this card: `OP3.robot` and `robot.cpp`. Both were inspected. One additional configuration anchor (`dxl_init_OP3.yaml`) was followed because it is co-located in the same config directory and directly supplements the device initialization semantics. This is a representative investigation. File hashes in drafts/DIFFERENCES.md mark these files as changed or unique relative to the Alphonse baseline; hash divergence alone does not establish runtime equivalence or inequivalence.

---

## Scope

| File | Status | Lines inspected |
|---|---|---|
| `source/src/ROBOTIS-OP3/op3_manager/config/OP3.robot` | Assigned — read fully | 1–30 |
| `source/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp` | Assigned — read fully | 1–499 |
| `source/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml` | Followed reference | 1–166 |
| `drafts/DIFFERENCES.md` | Read for hash evidence | 1–171 |
| `drafts/focus-shared-framework.md` | Read for shared context | 1–89 |

**Unexamined scope:** The `op3_manager/launch/op3_manager.launch.py`, `op3_manager/src/op3_manager.cpp`, `op3_tuning_module/`, `op3_walking_module/`, and `open_cr_module/` directories list changed files in `DIFFERENCES.md` but were not inspected for this card. The `.device` descriptor files (e.g., `XM430-W350.device`, `OPEN-CR.device`) referenced dynamically at parse time by `robot.cpp` were not found or examined.

---

## Observed Behavior

### Actuator Inventory (OP3.robot)

The `.robot` configuration declares **20 Dynamixel XM430-W350** servo actuators on a single USB-serial port (`/dev/ttyUSB0`), all at 2 Mbaud, all using Dynamixel Protocol 2.0 [source/src/ROBOTIS-OP3/op3_manager/config/OP3.robot:L1-L29](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/config/OP3.robot#L1-L29). Actuators are assigned sequential IDs 1–20 and mapped to logical joint names covering both limbs symmetrically (right shoulder pitch through head tilt). An additional **OPEN-CR** sensor board (ID 200) is attached to the same port and supplies button state, voltage, gyroscope (x/y/z), accelerometer (x/y/z), and fused IMU angles (roll/pitch/yaw) [source/src/ROBOTIS-OP3/op3_manager/config/OP3.robot:L30](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/config/OP3.robot#L30).

Every servo requests bulk reads of four items: `present_position`, `position_p_gain`, `position_i_gain`, and `position_d_gain` [source/src/ROBOTIS-OP3/op3_manager/config/OP3.robot:L10-L29](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/config/OP3.robot#L10-L29). The control cycle is pinned at **8 ms** [source/src/ROBOTIS-OP3/op3_manager/config/OP3.robot:L2](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/config/OP3.robot#L2).

### Device Parsing Semantics (robot.cpp)

The framework constructor `Robot::Robot()` reads `.robot` files line by line, stripping comments and whitespace, and dispatching on session headers (`[control info]`, `[port info]`, `[device info]`) [source/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp:L69-L232](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp#L69-L232). For each dynamixel entry, it:

1. Constructs a path to a model-specific `.device` descriptor file (e.g., `dynamixel/XM430-W350.device`) [source/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp:L130](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp#L130).
2. Calls `getDynamixel()` which parses the `.device` file to populate the control table, type metadata (radian conversion constants, PID gain item names), and bulk-read item list [source/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp:L320-L494](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp#L320-L494).
3. Falls back to indirect-address bulk reads if `INDIRECT_ADDRESS_1` is present in the device's control table; otherwise uses direct control-table pointers [source/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp:L143-L179](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp#L143-L179).

The same two-branch strategy applies to sensors, including the OPEN-CR board [source/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp:L181-L224](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp#L181-L224).

### Calibration and Initialization Parameters (dxl_init_OP3.yaml)

The companion YAML file initializes every joint to **operating_mode: 3** (position control mode), uniform **position_p_gain: 800**, and zero I/D gains [source/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml:L1-L166](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml#L1-L166). Position limits are 0–4095 raw counts for all joints. Return delay time is set to 1 on every actuator.

A subset of six shoulder/elbow actuators carries an extra `shutdown: 56` field: `l_el`, `l_sho_pitch`, `l_sho_roll`, `r_el`, `r_sho_pitch`, `r_sho_roll` [source/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml:L41](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml#L41), [source/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml:L82](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml#L82), [source/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml:L91](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml#L91), [source/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml:L116](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml#L116), [source/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml:L157](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml#L157), [source/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml:L165](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml#L165). The semantic meaning of `shutdown: 56` is not defined in any inspected source file and is left as an open question.

---

## Interfaces / Configuration

| Interface | Location | Role |
|---|---|---|
| `.robot` session parser | `robot.cpp:L69-L232` | Translates `[control info]`, `[port info]`, `[device info]` sections into runtime objects |
| `.device` descriptor loader | `robot.cpp:L320-L494`, `L234-L318` | Loads per-model control table and type info (radian offsets, gain names) |
| Bulk-read item assembly | `robot.cpp:L128-L179` (DXL), `L191-L223` (sensor) | Indirect-address or direct-pointer bulk read paths |
| Init YAML overrides | `dxl_init_OP3.yaml:L1-L166` | Per-joint operating mode, PID gains, position limits |

---

## Untested Operation Notes

- **No build, deployment, or runtime was performed.** All files were read as static text.
- The command `ros2 launch op3_manager op3_manager.launch.py` would presumably load `OP3.robot` and `dxl_init_OP3.yaml` at startup, but this launch file was not inspected. This command is noted for reference only and has not been executed.
- The `.device` descriptor files required by `getDynamixel()` and `getSensor()` at runtime [source/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp:L130](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp#L130), [source/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp:L183](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp#L183) were not located in this workspace. If missing at runtime, the framework prints "Unable to open file" and returns a null pointer [source/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp:L229-L231](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp#L229-L231), [source/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp:L490-L491](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp#L490-L491).
- Position-conversion clamping is **disabled** in the shared `Dynamixel` class (documented in `drafts/focus-shared-framework.md`), so raw values 0–4095 in `dxl_init_OP3.yaml` could theoretically map to out-of-bounds radians without saturation at the framework layer.

---

## Uncertainty and Conflicts

- **`shutdown: 56` semantics:** Six shoulder/elbow joints declare `shutdown: 56` in the init YAML [source/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml:L41](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml#L41), [source/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml:L82](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml#L82), [source/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml:L91](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml#L91), [source/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml:L116](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml#L116), [source/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml:L157](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml#L157), [source/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml:L165](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml#L165). No code in `robot.cpp`, the `.robot` parser, or the shared framework card references this key. Its runtime effect — whether it triggers torque-off, a specific shutdown register, or a higher-level policy — is unknown.
- **Single-port topology:** All 20 servos and the OPEN-CR sensor share `/dev/ttyUSB0`. If a bus fault occurs, the entire robot is affected. A bus-isolation strategy was not observed.
- **Hash changes vs observed differences:** `DIFFERENCES.md` lists `OP3.robot` and `robot.cpp` as changed relative to Alphonse. The actual content inspected above matches the expected XP3-style 20-joint XM430 hardware. The precise hash-level diff was not decomposed; we report only what the source says, not what the hash implies.
- **Webots vs physical robot:** The hardware configuration targets physical Dynamixel hardware. Webots simulation behaviour would depend on separate sim-controller nodes (outside this card's anchors) and may use different device descriptors or bypass the serial bus entirely.
- **Missing evidence:** The `op3_tmux/` scripts that may perform runtime device bringup, and the `open_cr_module/` that consumes the OPEN-CR sensor, were listed as changed but not inspected.

---

## Sources

| Source path | Lines inspected |
|---|---|
| `source/src/ROBOTIS-OP3/op3_manager/config/OP3.robot` | L1–L30 |
| `source/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp` | L1–L499 |
| `source/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml` | L1–L166 |
| `drafts/DIFFERENCES.md` | L1–L171 |
| `drafts/focus-shared-framework.md` | L1–L89 |
