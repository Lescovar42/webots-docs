> Shared file-content analysis, using the Alphonse snapshot. Robot-specific runtime conditions require separate review.

# Shared Code: ROBOTIS Framework & Device Interfaces

**Stage:** shared-core &nbsp;|&nbsp; **Canonical snapshot:** Alphonse (ALPHONSE_NEW_V2, `adacde8f`) &nbsp;|&nbsp; **Scope:** Representative investigation

> **GUIDES-FIRST SCOPE NOTE** — This card documents the shared ROBOTIS Framework code observed in the Alphonse snapshot. The same paths and identical SHA-256 content appear in the Chronus and Orion snapshots, but runtime equivalence has not been established. This is a representative investigation, not exhaustive source coverage. Code contracts are described; robot-wide runtime guarantees are not claimed.

---

## Scope

This card covers the `robotis_device` and `robotis_controller` portions of the ROBOTIS Framework as found under `source/src/ROBOTIS-Framework/`. Four assigned files were inspected directly, plus two included header references:

- `robotis_device/include/robotis_device/dynamixel.h` — Dynamixel actuator class header [source/src/ROBOTIS-Framework/robotis_device/include/robotis_device/dynamixel.h:L1-L83](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Framework/robotis_device/include/robotis_device/dynamixel.h#L1-L83)
- `robotis_device/src/robotis_device/dynamixel.cpp` — Dynamixel actuator implementation [source/src/ROBOTIS-Framework/robotis_device/src/robotis_device/dynamixel.cpp:L1-L138](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Framework/robotis_device/src/robotis_device/dynamixel.cpp#L1-L138)
- `robotis_device/include/robotis_device/device.h` — Abstract device base class [source/src/ROBOTIS-Framework/robotis_device/include/robotis_device/device.h:L1-L54](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Framework/robotis_device/include/robotis_device/device.h#L1-L54)
- `robotis_device/include/robotis_device/control_table_item.h` — Control table metadata descriptor [source/src/ROBOTIS-Framework/robotis_device/include/robotis_device/control_table_item.h:L1-L69](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Framework/robotis_device/include/robotis_device/control_table_item.h#L1-L69)
- `robotis_controller/package.xml` — ROS 2 controller package manifest [source/src/ROBOTIS-Framework/robotis_controller/package.xml:L1-L30](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Framework/robotis_controller/package.xml#L1-L30)
- `README.md` — Framework overview and external links [source/src/ROBOTIS-Framework/README.md:L1-L22](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Framework/README.md#L1-L22)

**Unexamined files:** The broader `robotis_controller/src/`, `robotis_framework_common/`, and remaining `robotis_device/` source trees were not inspected. The controller implementation and the DeviceManager class are present in the repository but outside the selected anchors for this card.

---

## Observed Behavior

### Device Abstraction Layer

The framework provides a base `Device` class in the `robotis_framework` namespace that holds per-actuator metadata: a numeric `id_`, a `protocol_version_` (float string for DXL bus protocol), a human-readable `model_name_`, and a serial `port_name_` [source/src/ROBOTIS-Framework/robotis_device/include/robotis_device/device.h:L37-L50](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Framework/robotis_device/include/robotis_device/device.h#L37-L50). Each device maintains a `ctrl_table_` map keyed by string item names to `ControlTableItem` pointers, and a separate `bulk_read_items_` vector for batch-read operations [source/src/ROBOTIS-Framework/robotis_device/include/robotis_device/device.h:L44-L46](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Framework/robotis_device/include/robotis_device/device.h#L44-L46).

### Control Table Items

`ControlTableItem` is a lightweight data descriptor used to characterize a register on a Dynamixel actuator [source/src/ROBOTIS-Framework/robotis_device/include/robotis_device/control_table_item.h:L43-L65](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Framework/robotis_device/include/robotis_device/control_table_item.h#L43-L65). It records the item name, bus address, access type (`Read` or `ReadWrite`), memory type (`EEPROM` or `RAM`), byte length, signedness, and min/max data bounds. Default construction yields a `Read`-only RAM item at address 0 with zero length and unsigned data.

### Dynamixel Conversion Logic

The `Dynamixel` class extends `Device` and adds unit-conversion methods for position (radians↔raw value), velocity, and torque/current [source/src/ROBOTIS-Framework/robotis_device/include/robotis_device/dynamixel.h:L39-L78](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Framework/robotis_device/include/robotis_device/dynamixel.h#L39-L78). The constructor initializes position limits to ±π radians, all PID gain pointers to null, and the zero-position offset to 0 [source/src/ROBOTIS-Framework/robotis_device/src/robotis_device/dynamixel.cpp:L28-L53](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Framework/robotis_device/src/robotis_device/dynamixel.cpp#L28-L53).

The `convertValue2Radian` / `convertRadian2Value` pair implements a piecewise-linear mapping centred on `value_of_0_radian_position_` [source/src/ROBOTIS-Framework/robotis_device/src/robotis_device/dynamixel.cpp:L62-L118](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Framework/robotis_device/src/robotis_device/dynamixel.cpp#L62-L118). Positive values scale proportionally between `value_of_0_radian_position_` and `value_of_max_radian_position_`; negative values scale between 0 and `value_of_min_radian_position_`. Clamping guards are *commented out* in both directions (lines 82–85 and 112–115), meaning out-of-range values pass through without saturation.

Velocity and torque conversions use simple ratio multiplication/division via `velocity_to_value_ratio_` and `torque_to_current_value_ratio_` [source/src/ROBOTIS-Framework/robotis_device/src/robotis_device/dynamixel.cpp:L120-L137](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Framework/robotis_device/src/robotis_device/dynamixel.cpp#L120-L137).

### Controller Package Contract

The `robotis_controller` package manifest (version 0.2.9) declares a ROS 2 (ament_cmake) dependency tree: it requires `rclcpp`, standard ROS message types (`std_msgs`, `sensor_msgs`), the `robotis_device` and `robotis_controller_msgs` packages, `dynamixel_sdk`, `robotis_framework_common`, and YAML-CPP for configuration [source/src/ROBOTIS-Framework/robotis_controller/package.xml:L17-L29](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Framework/robotis_controller/package.xml#L17-L29). The description targets "ROBOTIS's platform like Manipulator-H, THORMANG and OP series" [source/src/ROBOTIS-Framework/robotis_controller/package.xml:L6-L7](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Framework/robotis_controller/package.xml#L6-L7).

---

## Interfaces / Configuration

| Interface | Location | Purpose |
|---|---|---|
| `Device` base class | `device.h:L37-L50` | Common actuator metadata and control-table container |
| `ControlTableItem` | `control_table_item.h:L43-L65` | Register descriptor (address, type, range) |
| `Dynamixel` subclass | `dynamixel.h:L39-L78` | Unit conversions for position, velocity, torque |
| `package.xml` deps | `package.xml:L17-L29` | Build/runtime dependency list for the controller |

The YAML-CPP dependency in the controller suggests that actuator identities, ports, and control tables are resolved from external configuration rather than being compiled in. Specific YAML schema is not present in the inspected files and was not followed.

---

## Untested Operation Notes

- **No build or runtime was performed.** The package.xml and source were only read.
- The commented-out clamping in `convertValue2Radian` and `convertRadian2Value` [source/src/ROBOTIS-Framework/robotis_device/src/robotis_device/dynamixel.cpp:L82-L85](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Framework/robotis_device/src/robotis_device/dynamixel.cpp#L82-L85), [source/src/ROBOTIS-Framework/robotis_device/src/robotis_device/dynamixel.cpp:L112-L115](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Framework/robotis_device/src/robotis_device/dynamixel.cpp#L112-L115) means an actuator can be commanded past its configured mechanical limits at the conversion layer. Whether safety is enforced downstream (controller logic or firmware) was not inspected.
- All PID gain pointers on `Dynamixel` default to null [source/src/ROBOTIS-Framework/robotis_device/src/robotis_device/dynamixel.cpp:L44-L49](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Framework/robotis_device/src/robotis_device/dynamixel.cpp#L44-L49). It is inferred that a separate initialization routine populates these, but that routine was not observed.
- The framework README links to the `dynamixel_sdk` and `ROBOTIS-Framework-msgs` repositories [source/src/ROBOTIS-Framework/README.md:L16-L22](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Framework/README.md#L16-L22); those are external dependencies not present in this workspace.

---

## Uncertainty and Conflicts

- **Clamping removal ambiguity:** The position-conversion code has explicit clamping disabled via `#if 0`-style commenting. It is unclear whether this is intentional (offloading bounds checking to another layer) or an oversight.
- **Protocol version as float:** `protocol_version_` is a `float` rather than an enum or integer, which may accept non-canonical values [source/src/ROBOTIS-Framework/robotis_device/include/robotis_device/device.h:L41](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Framework/robotis_device/include/robotis_device/device.h#L41).
- **Webots vs physical robot behavior:** The source contains no Webots-specific logic. The framework targets physical Dynamixel actuators over serial/USB bus. Simulation behaviour in Webots would depend on separate controller nodes not inspected here.

---

## Sources

| File | Lines inspected |
|---|---|
| `source/src/ROBOTIS-Framework/README.md` | 1–22 |
| `source/src/ROBOTIS-Framework/robotis_controller/package.xml` | 1–30 |
| `source/src/ROBOTIS-Framework/robotis_device/include/robotis_device/dynamixel.h` | 1–83 |
| `source/src/ROBOTIS-Framework/robotis_device/src/robotis_device/dynamixel.cpp` | 1–138 |
| `source/src/ROBOTIS-Framework/robotis_device/include/robotis_device/device.h` | 1–54 |
| `source/src/ROBOTIS-Framework/robotis_device/include/robotis_device/control_table_item.h` | 1–69 |
