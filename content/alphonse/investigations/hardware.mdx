# Alphonse: Hardware, Device and Calibration Differences

**Branch:** `ALPHONSE_NEW_V2` — commit `adacde8f6e01e6439d170fb6bce025acc051bfa3`
**Stage:** robot-differences
**Scope:** Two changed/unique anchors from the hash-difference list: `OP3.robot` and `robot.cpp`.

---

## 1 Scope and unexamined files

This draft covers the two files flagged in `drafts/DIFFERENCES.md` [drafts/DIFFERENCES.md:L55] and [drafts/DIFFERENCES.md:L115]:

| File | Role |
|---|---|
| `OP3.robot` | Device-topology and bulk-read configuration |
| `robot.cpp` | Robot-description parser (device/sensor registration) |

These files were fully read. One closely related reference was also inspected — `dxl_init_OP3.yaml` [source/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml:L1-L116](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml#L1-L116) — which provides per-joint calibration init values. Many other changed files in the difference list (e.g., `robotis_controller.cpp`, `op3_manager.cpp`, walking-module sources, calibration scripts) were **not** examined and remain deferred.

---

## 2 Observed behavior and hardware differences

### 2.1 Port wiring and OpenCR attachment

`OP3.robot` declares two physical ports [source/src/ROBOTIS-OP3/op3_manager/config/OP3.robot:L4-L12](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/config/OP3.robot#L4-L12):

- **U2D2 servo bus** (`/dev/serial/by-id/usb-FTDI_USB__-__Serial_Converter_FT3WKHM6-if00-port0`): carries all 20 Dynamixel joints (IDs 1–20), XM430-W350, Protocol 2.0 [source/src/ROBOTIS-OP3/op3_manager/config/OP3.robot:L32-L51](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/config/OP3.robot#L32-L51).
- **OpenCR USB CDC** (`/dev/serial/by-id/usb-ROBOTIS_OpenCR_Virtual_ComPort_in_FS_Mode_FFFFFFFEFFFF-if00`): carries the OpenCR controller (ID 200) [source/src/ROBOTIS-OP3/op3_manager/config/OP3.robot:L8-L12](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/config/OP3.robot#L8-L12).

The file comments explicitly state that OpenCR is connected via micro-USB **not** via the TTL bus bridge on the OpenCR board. The TTL bridge is non-responsive — pinging ID 200 produces no response at any baud rate 9600–4 M — while the MCU/firmware/IMU are healthy over USB (model `0x7400`, acc_z ≈ 17616 (1g), 12.5 V) [source/src/ROBOTIS-OP3/op3_manager/config/OP3.robot:L8-L11](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/config/OP3.robot#L8-L11). This is a hardware-level difference: the OpenCR serial interface is disabled and the bus uses a separate U2D2 adapter instead of the built-in OpenCR TTL.

Both ports share a USB hub; the comment notes that OpenCR full-speed mode (12 Mbit) competes with U2D2 for the same hub bandwidth [source/src/ROBOTIS-OP3/op3_manager/config/OP3.robot:L25-L26](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/config/OP3.robot#L25-L26).

### 2.2 Bulk-read optimization

All 20 servos are configured with bulk-read items set to `present_position` only [source/src/ROBOTIS-OP3/op3_manager/config/OP3.robot:L31-L51](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/config/OP3.robot#L31-L51). The comments explain that earlier configurations included `position_p_gain`, `position_i_gain`, and `position_d_gain` alongside `present_position`. Because `GroupBulkRead` uses the **lowest** address as the bulk-read start offset (address 132, `present_position`), any items at higher addresses (80–84) would never be readable via `isAvailable()`. The net effect was extending each servo response from 4 bytes to 10 bytes for no functional gain. Removing the gain items reduces total bulk traffic by approximately 29% (420 → 300 bytes), cutting round-trip latency from ~3.79 ms to ~2.81 ms [source/src/ROBOTIS-OP3/op3_manager/config/OP3.robot:L15-L30](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/config/OP3.robot#L15-L30). Gains are still read once at init via per-item reads.

### 2.3 Per-joint init calibration

`dxl_init_OP3.yaml` configures per-joint boot-time calibration [source/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml:L1-L10](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml#L1-L10):

- All servos: `position_p_gain = 800`, `position_d_gain = 0`, `position_i_gain = 0`, `return_delay_time = 1`.
- Five joints carry an additional `shutdown: 56` entry: `l_el` [L36], `l_sho_pitch` [L62-63], `l_sho_roll` [L68-69], `r_el` [L84-85], `r_sho_pitch` [L110-111], `r_sho_roll` [L115-116].
- Factory-default EEPROM values (`operating_mode`, `max/min_position_limit`) were deliberately removed to avoid redundant bus writes; each per-servo EEPROM read was estimated to cost ~15 ms over the OpenCR USB↔TTL bridge [source/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml:L5-L8](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml#L5-L8).

---

## 3 Interfaces and configuration

### 3.1 Parser changes in `robot.cpp`

The device parser was modified to improve startup diagnostic readability. A new helper `shortPortName()` resolves a path via `realpath()` and extracts the final symlink component (e.g., `ttyUSB1`, `ttyACM1`) [source/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp:L34-L51](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp#L34-L51). The long `/dev/serial/by-id/…` paths produce a 70-character string; using them in every device-line log entry pushed useful columns so far right that they wrapped [source/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp:L34-L39](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp#L34-L39). The short name replaces the full path on device-print lines, while the full path remains emitted once in the port-section header [source/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp:L137-L138](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp#L137-L138).

The bulk-read registration logic (lines 170–206, 226–253) was _not_ altered in this file; it still uses the `INDIRECT_ADDRESS_1` / `INDIRECT_DATA_1` redirection mechanism described in the OP3.robot comments. The parser behavior is therefore consistent with the reduced bulk-read item list in the config file.

### 3.2 Sensor bulk items

The OpenCR sensor (ID 200) reads twelve items via bulk-read: `button`, `present_voltage`, three gyro axes, three accelerometer axes, three IMU Euler angles (`roll`, `pitch`, `yaw`), and `mag_status` [source/src/ROBOTIS-OP3/op3_manager/config/OP3.robot:L52](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/config/OP3.robot#L52).

---

## 4 Untested operation notes

The following commands and values appear in source but were **not executed or verified**:

- The `control_cycle = 8` ms setting in `OP3.robot` [source/src/ROBOTIS-OP3/op3_manager/config/OP3.robot:L2](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/config/OP3.robot#L2) is a target; actual timing depends on bus load and USB hub contention, not measured here.
- The measured round-trip figures (3.79 ms → 2.81 ms) are quoted from source comments [source/src/ROBOTIS-OP3/op3_manager/config/OP3.robot:L23-L24](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/config/OP3.robot#L23-L24), not independently reproduced.
- The `realpath()` symlink resolution in `shortPortName()` [source/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp:L43-L45](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp#L43-L45) may fail or return the full path on systems where the symlink chain differs from the developer machine.

**Webots/simulation:** This investigation does not cover simulation-specific hardware emulation. The port paths and U2D2 wiring are physical-device concerns; Webots may abstract them differently. No Webots-specific evidence was found in the two assigned files.

---

## 5 Uncertainty and conflicts

- The `else // INDIRECT_ADDRESS_1 exist` comment at line 248 [source/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp:L248](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp#L248) appears to copy-paste the wrong label and should plausibly read `INDIRECT_ADDRESS_1 not exist`. This is cosmetic but may confuse maintainers.
- The device descriptor directory path (`dev_desc_dir_path`) is a parameter passed at runtime. Its value on this branch is not observed in the assigned files, so the actual `.device` files loaded are not confirmed.
- The specific USB hub model, cable lengths, and whether the two ports truly share the same hub on a given robot build are not specified beyond the comment annotation.

---

## 6 Sources

| Source | Lines inspected |
|---|---|
| `source/src/ROBOTIS-OP3/op3_manager/config/OP3.robot` | L1–52 (full file) |
| `source/src/ROBOTIS-Framework/robotis_device/src/robotis_device/robot.cpp` | L1–529 (full file) |
| `source/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml` | L1–116 (full file) |
| `drafts/DIFFERENCES.md` | L1–167 (full file) |
| `drafts/SHARED-INDEX.md` | L1–21 (full file) |
