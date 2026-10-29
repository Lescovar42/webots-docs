# Chronus: Hardware, Device and Calibration Differences

## Scope

This card covers hardware topology, device enumeration and calibration parameters observed in the Chronus branch (CHRONUS_NEW, commit `54998e7c56e5b2cce4c1c533758c7d2f2cf7698b`). It focuses on two assigned files—`OP3.robot` and `robot.cpp`—and follows two additional references (`op3_manager.launch.py` and `param.yaml`) to round out the hardware-and-calibration picture. It does not claim exhaustive source coverage; unexamined device-description files (`.device` payloads in the `dynamixel/` and `sensor/` subdirectories) are noted below. Content differences versus the Alphonse branch are listed in `drafts/DIFFERENCES.md` [drafts/DIFFERENCES.md:L29-L30, L69].

## Observed Hardware Topology

The robot description lives in `OP3.robot` [source/src/ROBOTIS-OP3/op3_manager/config/OP3.robot:L1-L35](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_manager/config/OP3.robot#L1-L35). It declares a **single serial port**, `/dev/ttyOP3`, operating at 2 000 000 baud. All 20 Dynamixel servos (IDs 1–20, model `XM430-W350`, Protocol 2.0) and the OpenCR sub-controller (ID 200, model `OPEN-CR`) share that port:

- Servos cover standard OP3 joints: shoulders (pitch/roll), elbows, hips (yaw/roll/pitch), knees, ankles (pitch/roll) and head (pan/tilt) [source/src/ROBOTIS-OP3/op3_manager/config/OP3.robot:L15-L34](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_manager/config/OP3.robot#L15-L34).
- The OpenCR sensor provides IMU (gyro x/y/z, acc x/y/z, roll, pitch, yaw), button state, and bus voltage [source/src/ROBOTIS-OP3/op3_manager/config/OP3.robot:L35](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_manager/config/OP3.robot#L35).

The config file comment explicitly notes the wiring: the OpenCR serves sub-controller ID 200 on `DXL_PORT = Serial3`, the same TTL bus as the servos, so one port carries everything [source/src/ROBOTIS-OP3/op3_manager/config/OP3.robot:L6-L10](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_manager/config/OP3.robot#L6-L10). The micro-USB CDC endpoint (`/dev/ttyACM0`) is a debug-only console and never answers DXL packets.

## Port Probing at Launch

`op3_manager.launch.py` adds an `ensure_ports()` stage [source/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py:L97-L163](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py#L97-L163) that:

1. Enumerates `/sys/class/tty` for `ttyUSB*` and `ttyACM*` entries [source/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py:L55-L84](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py#L55-L84).
2. Sends a raw Protocol 2.0 ping to each candidate to find which port answers servo ID 1 and which answers sub-controller ID 200 [source/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py:L18-L52](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py#L18-L52).
3. Creates or repairs symlinks `/dev/ttyOP3` → the discovered live device [source/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py:L123-L162](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py#L123-L162).

Commands found in source but **not executed here**: the `_dxl_answers()` raw-serial ping [source/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py:L18-L52](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py#L18-L52) and the symlink-maintenance in `point()` [source/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py:L123-L136](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py#L123-L136).

The code warns if no servo replies (suspecting a missing U2D2/FTDI adapter) and distinguishes the stock single-port wiring from a board flashed with `opencr_op3_usb`, where ID 200 lives on a separate micro-USB port [source/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py:L138-L162](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py#L138-L162).

## Device Parsing Framework

`robot.cpp` [source/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp:L69-L232](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp#L69-L232) parses the three `[ control info ]`, `[ port info ]` and `[ device info ]` sessions from `OP3.robot`. Dynamixel and sensor entries are resolved by loading external `.device` description files (e.g. `dynamixel/XM430-W350.device`) at runtime [source/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp:L320-L494](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp#L320-L494). Key calibration knobs embedded in those description files—`value_of_0_radian_position`, `min_radian`, `max_radian`—are read by `getDynamixel()` [source/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp:L388-L397](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp#L388-L397) but the actual `.device` payloads were **not inspected**; only the parsing logic is observed.

### Unexamined files

- `Robotis-Framework/robotis_device/src/robotis_device/dynamixel/*.device` — description payloads for servo calibration constants (0-radian value, min/max radian, torque-to-current ratio, velocity ratio). No `.device` files exist at the globbed path under the workspace root; they may live elsewhere on the host and are not included in this artifact set.
- `Robotis-Framework/robotis_device/src/robotis_device/sensor/*.device` — analogous sensor description files (e.g. `OPEN-CR.device`). Same status.

## Calibration Parameters

The walking module config `param.yaml` [source/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml:L1-L22](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml#L1-L22) carries per-axis calibration offsets:

| Parameter | Value |
|---|---|
| x_offset | −0.015 m |
| y_offset | +0.015 m |
| z_offset | +0.075 m |
| pitch_offset | 4.0° |
| hip_pitch_offset | 8.0° |
| foot_height | 0.050 m |
| pelvis_offset | 0.500 |

These values are specific to the Chronus branch and must not be transferred to a different physical robot. Balance gains (hip-roll 0.35, knee 0.40, ankle-roll 0.70, ankle-pitch 0.90) and motion-timing knobs (period 700 ms, DSP ratio 0.30) [source/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml:L8-L22](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml#L8-L22) are similarly robot-specific.

The initial-pose file `ini_pose.yaml` [source/src/ROBOTIS-OP3/op3_base_module/data/ini_pose.yaml:L34-L63](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_base_module/data/ini_pose.yaml#L34-L63) stores asymmetric joint targets. A comment on that file notes the values were captured from an older action page ("INIT_BARU") and that boot actually goes through `op3_manager`'s `goToInitActionPage`, making `ini_pose.yaml` relevant only when a caller explicitly requests base_module to move to ini_pose [source/src/ROBOTIS-OP3/op3_base_module/data/ini_pose.yaml:L35-L41](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_base_module/data/ini_pose.yaml#L35-L41).

## Interfaces and Configuration Summary

| Aspect | Observed value |
|---|---|
| Control cycle | 8 ms [source/src/ROBOTIS-OP3/op3_manager/config/OP3.robot:L2](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_manager/config/OP3.robot#L2) |
| Bus | Single `/dev/ttyOP3` @ 2 Mbps [source/src/ROBOTIS-OP3/op3_manager/config/OP3.robot:L11](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_manager/config/OP3.robot#L11) |
| Actuators | 20 × XM430-W350, Protocol 2.0 [source/src/ROBOTIS-OP3/op3_manager/config/OP3.robot:L15-L34](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_manager/config/OP3.robot#L15-L34) |
| IMU/sub-controller | OpenCR, ID 200, same TTL bus [source/src/ROBOTIS-OP3/op3_manager/config/OP3.robot:L35](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_manager/config/OP3.robot#L35) |
| Servo bulk reads | present_position + P/I/D gains [source/src/ROBOTIS-OP3/op3_manager/config/OP3.robot:L15](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_manager/config/OP3.robot#L15) |
| IMU bulk reads | button, voltage, gyro×3, acc×3, Euler angles×3 [source/src/ROBOTIS-OP3/op3_manager/config/OP3.robot:L35](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_manager/config/OP3.robot#L35) |

## Webots vs Physical Robot

The OP3.robot file and the launch probe logic target physical serial hardware. Webots simulation uses a different backend (the `gazebo` parameter in `op3_manager.launch.py` defaults to `False` [source/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py:L168](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py#L168)). No Webots-specific device description or calibration overlay was observed in the assigned files. Any difference between simulated and physical joint offsets must be confirmed by inspecting the Webots world files, which were **not examined**.

## Uncertainties and Conflicts

- The `.device` calibration files that supply per-axis position-center values and radian limits are missing from the workspace tree. Without them, the effective servo-to-CRC mapping at parse time cannot be verified.
- `ini_pose.yaml` carries a snapshot of a deprecated action page; the comment [source/src/ROBOTIS-OP3/op3_base_module/data/ini_pose.yaml:L35-L41](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_base_module/data/ini_pose.yaml#L35-L41) flags a naming change from "INIT_BARU" to "WALKING_READY" but does not say whether the numeric values remain correct.
- The port-probing script assumes a privileged container with root access [source/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py:L60-L61](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py#L60-L61); behavior outside that environment (e.g. a desktop ROS 2 host) is not documented.
- Hash-only differences from `drafts/DIFFERENCES.md` are structural navigation aids and do not prove runtime behavior. The claims above rest solely on the inspected source lines cited here.

## Sources

- `source/src/ROBOTIS-OP3/op3_manager/config/OP3.robot` — lines 1–35
- `source/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp` — lines 69–499
- `source/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py` — lines 1–204
- `source/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml` — lines 1–22
- `source/src/ROBOTIS-OP3/op3_base_module/data/ini_pose.yaml` — lines 1–63
- `source/src/ROBOTIS-OP3/open_cr_module/src/open_cr_module.cpp` — lines 1–160
