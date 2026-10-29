# Chronus: Walking, Motion and Kinematic Differences

**Branch:** `CHRONUS_NEW` &nbsp; **Commit:** `54998e7c56e5b2cce4c1c533758c7d2f2cf7698b`
**Stage:** robot-differences &nbsp; **Scope:** Representative — assigned anchors only; 14 changed candidate files exist, not all examined.

---

## 1. Scope

This card examines differences in walking gait parameters, inverse kinematics lengths, motion presets and balancing behaviour in the Chronus branch compared to the Alphonse reference. Four assigned source files were inspected:

| File | Lines inspected | Purpose |
|---|---|---|
| `source/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml` | full (22 lines) | Walking gait parameter YAML |
| `source/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp` | 1–320, 1141–1293 | Walking module: fallback params, IK, load/save, init-pose |
| `source/src/ROBOTIS-OP3/op3_kinematics_dynamics/src/op3_kinematics_dynamics.cpp` | 1–160 | Kinematics link tree (link data table) |
| `source/src/ROBOTIS-OP3-Tools/op3_gui_demo/config/gui_motion.yaml` | full (26 lines) | Motion presets for GUI demo |

**Unexamined scope per `drafts/DIFFERENCES.md`:** `op3_walking_module/include/op3_walking_module/op3_walking_module.h` (header, partially read but not fully examined for new members), `op3_action_module/src/action_module.cpp`, `op3_base_module/src/base_module.cpp`, `op3_tuning_module/src/tuning_module.cpp`, and all `bascorro_studio` files listed in the differences manifest. File hashes changed but runtime implications cannot be inferred from hashes alone.

---

## 2. Observed Behavior

### 2.1 Walking parameter file (`param.yaml`)

The walking configuration file defines 22 key-value pairs [source/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml:L1-L22](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml#L1-L22). Key values include:

- **Period time:** 700 ms (gait cycle length).
- **DSP ratio:** 0.30 (double-support phase fraction).
- **Foot height:** 50 mm (z-axis foot trajectory amplitude).
- **Offsets:** `x_offset = -15 mm`, `y_offset = +15 mm`, `z_offset = +75 mm`, `pitch_offset = 4.0 deg`, `hip_pitch_offset = 8.0 deg`.
- **Swing amplitudes:** `swing_right_left = 2 mm`, `swing_top_down = 6 mm`.
- **Balance gains:** hip roll 0.35, knee 0.40, ankle roll 0.70, ankle pitch 0.90.
- **PID gains:** p, i, d are all explicitly zero.

These values are loaded at module initialization via `loadWalkingParam()` [source/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp:L1141-L1188](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp#L1141-L1188) which maps YAML keys to `walking_param_` struct fields with unit conversions (ms to seconds for period, degrees to radians for angular offsets).

### 2.2 Hardcoded fallback parameters

A distinctive feature of the Chronus branch is a documented "FALLBACK DARURAT" (emergency fallback) block [source/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp:L111-L154](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp#L111-L154). The `initialize()` method sets hardcoded walking parameters that mirror the values in `param.yaml`. If `loadWalkingParam()` fails to parse the YAML file, the robot still runs the same gait the operator expects rather than a stock factory gait. The comment explicitly warns that earlier defaults (period 600 ms, y_swap 0.020 m, arm_swing 1.5) would cause unexpected behaviour if left in place. Three locations share identical numeric values: `param.yaml`, `op3_walking_module.cpp`, and `bascorro_studio/web/src/walkingParams.js` (the third location was not read in this pass).

### 2.3 Inverse kinematics limb lengths

The IK solver in `WalkingModule::computeIK()` uses hardcoded limb dimensions [source/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp:L273-L279](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp#L273-L279):

| Segment | Length |
|---|---|
| Thigh | 93.0 mm |
| Calf | 93.0 mm |
| Ankle | 33.5 mm |
| Total leg | 219.5 mm |

These are embedded constants, not loaded from configuration. The neutral leg angle computation [source/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp:L1242-L1263](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp#L1242-L1263) derives endpoints from `op3_kd_->thigh_length_m_` etc., meaning the `OP3KinematicsDynamics` class must carry the same values. The kinematics dynamics constructor [source/src/ROBOTIS-OP3/op3_kinematics_dynamics/src/op3_kinematics_dynamics.cpp:L40-L160](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_kinematics_dynamics/src/op3_kinematics_dynamics.cpp#L40-L160) builds a link tree (WholeBody topology) with per-link mass, center-of-mass, inertia, and joints. Link 29 (pelvis) carries the highest mass value in the inspected section: 1.349 kg [source/src/ROBOTIS-OP3/op3_kinematics_dynamics/src/op3_kinematics_dynamics.cpp:L140](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_kinematics_dynamics/src/op3_kinematics_dynamics.cpp#L140).

### 2.4 Motion presets (`gui_motion.yaml`)

The GUI demo configuration maps integer motion indices to named gestures [source/src/ROBOTIS-OP3-Tools/op3_gui_demo/config/gui_motion.yaml:L1-L26](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3-Tools/op3_gui_demo/config/gui_motion.yaml#L1-L26). Notable soccer-related motions: WALKING_READY (2), Right Kick (121), Left Kick (120), Keeper Ready (60). The index 0 (neutral/idle) is commented out. Action demo motions include Foot play (200), Roll back (202), etc.

### 2.5 Init-pose trajectory fix

The Chronus source contains a fix in `iniPoseTraGene()` [source/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp:L1265-L1292](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp#L1265-L1292). The step count computation was corrected to use `round()` instead of `int()`, preventing an Eigen resize assertion that would abort `op3_manager` with SIGABRT when the walking module was enabled. This is a runtime stability change specific to this branch.

---

## 3. Interfaces and Configuration

- **ROS 2 topics:** The walking module subscribes to `/robotis/walking/command` (string commands: start, stop, balance on/off, save) and `/robotis/walking/set_params` (WalkingParam message) [source/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp:L209-L212](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp#L209-L212).
- **ROS 2 services:** `/robotis/walking/get_params` returns the current walking parameter snapshot [source/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp:L205-L206](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp#L205-L206).
- **Parameter path:** Declared as ROS 2 parameter `walking_param_path`, defaulting to the package share directory's `config/param.yaml` [source/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp:L186-L188](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp#L186-L188).
- **Walking stance capture:** When the module is enabled (`onModuleEnable`), `capture_init_pose_` is set to true, locking the gait oscillation to whatever joint pose the robot occupies at activation time, offset by `walking_bias_` [source/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp:L1225-L1230](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp#L1225-L1230)[source/src/ROBOTIS-OP3/op3_walking_module/include/op3_walking_module/op3_walking_module.h:L149-L153](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_walking_module/include/op3_walking_module/op3_walking_module.h#L149-L153).

---

## 4. Untested Operation Notes

- The YAML load/save round-trip was not executed. Commands found in source: sending `"save"` on `/robotis/walking/command` triggers `saveWalkingParam()` [source/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp:L249-L250](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp#L249-L250) but this was not tested.
- The `balance on` / `balance off` commands set `walking_param_.balance_enable` but the actual balancing feedback loop implementation was not traced in this pass.
- PID gains in the YAML are all zero; the practical effect is unknown without observing the control stack downstream of the walking module.

---

## 5. Uncertainty and Conflicts

| Question | Status |
|---|---|
| Do the hardcoded IK lengths (93/93/33.5 mm) differ from Alphonse? | Unknown — Alphonse source was not inspected side-by-side in this pass. |
| Does `balance_enable` originate from YAML or code? | Code only. The comment at L144-145 states `balance_enable` is **not** read by `loadWalkingParam()` and always comes from the fallback block value (`true`) [source/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp:L144-L146](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp#L144-L146). This means the YAML cannot disable balance. |
| Are the three synchronized parameter copies (YAML, C++, JS) consistent in production? | They are consistent in the inspected source, but the third copy (`bascorro_studio/web/src/walkingParams.js`) was not read. |
| Do removed files (e.g., `preset_walking.yaml` from Alphonse) indicate a parameter migration? | Plausible but unconfirmed. File absence alone does not prove parameter relocation. |
| Webots simulation vs real robot: do parameters behave identically? | Unknown. The walking module shares the same param file, but Webots executor paths were not inspected here. |

---

## 6. Sources

- `source/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml` — lines 1–22
- `source/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp` — lines 1–320, 1141–1293
- `source/src/ROBOTIS-OP3/op3_walking_module/include/op3_walking_module/op3_walking_module.h` — lines 1–160
- `source/src/ROBOTIS-OP3/op3_kinematics_dynamics/src/op3_kinematics_dynamics.cpp` — lines 1–160
- `source/src/ROBOTIS-OP3-Tools/op3_gui_demo/config/gui_motion.yaml` — lines 1–26
- `drafts/DIFFERENCES.md` — lines 1–168
- `drafts/SHARED-INDEX.md` — lines 1–21
