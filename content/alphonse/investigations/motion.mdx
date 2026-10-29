# Alphonse: Walking, Motion and Kinematic Differences

**Branch:** ALPHONSE_NEW_V2 · **Commit:** adacde8f6e01e6439d170fb6bce025acc051bfa3
**Scope:** Representative investigation of walking module, kinematics and demo preset configuration. 146+ eligible files in this branch; only four assigned anchors plus selective grep references were read. Unexamined files listed below.

---

## Scope and method

Read sources:
- `op3_walking_module/config/param.yaml` (85 lines) — base walking parameters
- `op3_demo/config/preset_walking.yaml` (453 lines) — six soccer-demo presets
- `op3_walking_module/src/op3_walking_module.cpp` (first 160 lines + grep hits)
- `op3_kinematics_dynamics/src/op3_kinematics_dynamics.cpp` (first 160 lines)

Additional grep across all `.cpp` files for symbols `loadWalkingParam`, `walking_bias`, `computeNeutralLegAngle`, `computeLegAngle`, `angle_move_amplitude`, and `turn_in`.

**Unexamined files in this group (partial):** all 20 scripts, every `*.md` documentation file, op3_manager.cpp, demo_node.cpp, soccer_demo.cpp, ball_follower.cpp, kick_geometry scripts, bascorro_studio Python modules, Webots integration code, and 130+ other changed files in DIFFERENCES.md. Claims below apply only to the inspected sources.

---

## Observed behaviour — key differences

### 1. Two-axis yaw rotation (new `angle_move_amplitude_turn_in`)

The source adds a second yaw-rotation axis alongside the original ROBOTIS `angle_move_amplitude` [source/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp:L36-L57](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp#L36-L57):

- **`angle_move_amplitude`** — Original ROBOTIS behaviour: left hip yaw receives `+a`, right hip yaw receives `-a`. Both hips rotate in opposite directions during the swing phase (foot in the air). Unchanged.
- **`angle_move_amplitude_turn_in`** ("putar dalam" — "turn in") — New axis added on top. Both feet receive the **same sign** value, causing servo 7 and 8 to rotate in the same direction. The motion window shifts to the DSP (double-support phase) immediately *after* foot contact, not during swing. Sign of the value selects which leg is the "pivoting" leg:
  - `t > 0` → left leg pivots → clockwise body rotation
  - `t < 0` → right leg pivots → counter-clockwise body rotation

The negative side is formed as a true mirror (swap left/right roles + flip sign), not by passing negative values into the same formula [source/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp:L49-L54](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp#L49-L54). `computeLegAngle()` at line 1019 implements this [source/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp:L1019](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp#L1019). When `turn_in = 0`, the axis is disabled and the gait reverts to pure ROBOTIS.

**Effect in presets:** The `mencari_celah` preset uses `angle_move_amplitude: -0.2` with `turn_in: 0.0` to rotate in place [source/src/ROBOTIS-OP3-Demo/op3_demo/config/preset_walking.yaml:L206](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_demo/config/preset_walking.yaml#L206). Meanwhile `putar_kiri` and `putar_kanan` use *both* axes simultaneously with non-symmetric magnitudes [source/src/ROBOTIS-OP3-Demo/op3_demo/config/preset_walking.yaml:L238-L286](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_demo/config/preset_walking.yaml#L238-L286), e.g. `putar_kiri` has `angle: -0.070` and `turn_in: +0.015`, while `putar_kanan` has `angle: +0.015` and `turn_in: -0.090`. The source warns explicitly: "JANGAN PERNAH menurunkan satu sisi dari sisi lainnya" — never derive one side from the other [source/src/ROBOTIS-OP3-Demo/op3_demo/config/preset_walking.yaml:L288](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_demo/config/preset_walking.yaml#L288).

### 2. Walking bias and relative offsets

Walking offsets are **relative**, not absolute. On first enable, the module captures `walking_bias_` as the difference between the current `goal_position_` (WALKING_READY pose) and a neutral leg position computed via `computeNeutralLegAngle()` [source/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp:L608-L620](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp#L608-L620):

```
walking_bias_ = goal_position_ - neutral_leg
```

Then the robot's pose during walking is:
```
pose = page2_pose + [ neutral(preset) - neutral(param.yaml) ]
```

This formula appears in comments in both config files [source/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml:L35-L42](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml#L35-L42) [source/src/ROBOTIS-OP3-Demo/op3_demo/config/preset_walking.yaml:L99-L109](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_demo/config/preset_walking.yaml#L99-L109). The consequence is that `param.yaml` and the `jalan` preset **must not** have the same offset values; if they match, the difference is zero and the robot stays locked at the page-2 pose regardless of preset numbers. The current effective offset difference is: x −10.0 mm, pitch −2.8648 deg, hip_pitch +0.0229 deg [source/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml:L43](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml#L43).

### 3. Soft-start ramp behaviour

The `soft_start_time` parameter controls how long it takes for x, y, z, and angle amplitudes to ramp from zero to full value via `rampToward()` and `timeRampScale()` in op3_walking_module. The `jalan` preset explicitly raised this from 0.05 s to 0.9 s so that foot-lift height increases gradually [source/src/ROBOTIS-OP3-Demo/op3_demo/config/preset_walking.yaml:L124-L143](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_demo/config/preset_walking.yaml#L124-L143):

| soft_start_time | swing heights (mm) | full amplitude at |
|---|---|---|
| 0.05 s | 8.6 → 54.4 direct | immediate |
| 0.5 s | 4.6 → 54.4 | ~1.4 s |
| **0.9 s** | 35.6 → 54.4 | ~1.7 s (active) |
| 1.5 s | 22.2 → 54.4 | ~2.3 s |

Measured data cited in comments [source/src/ROBOTIS-OP3-Demo/op3_demo/config/preset_walking.yaml:L136-L143](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_demo/config/preset_walking.yaml#L136-L143). The other five presets intentionally keep short ramps (0.005–0.05 s) because the long ramp would consume the entire short motion [source/src/ROBOTIS-OP3-Demo/op3_demo/config/preset_walking.yaml:L142](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_demo/config/preset_walking.yaml#L142).

### 4. IK reachability failure on excessive x-offset

The `geser_kiri` and `geser_kanan` presets both have `init_x_offset: -0.03` despite the Studio-saved version containing `-0.18`. The source states `-0.18` m is **mechanically impossible**: the leg would be asked to reach 254.1 mm from the hip, but thigh + shank is only 220.2 mm. This was verified directly against `op3_kinematics_dynamics` inverse kinematics, which fails across the full range with "IK produced non-finite leg_angle[2]" logs [source/src/ROBOTIS-OP3-Demo/op3_demo/config/preset_walking.yaml:L343-L358](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_demo/config/preset_walking.yaml#L343-L358). The comment notes the failure manifested at 2026-09-08 02:08:41 UTC after the preset was applied.

### 5. Balance disabled everywhere

All six presets and `param.yaml` set `balance_enable: false` [source/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml:L78](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml#L78) [source/src/ROBOTIS-OP3-Demo/op3_demo/config/preset_walking.yaml:L153](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_demo/config/preset_walking.yaml#L153). The IMU-based balance correction is not used in any configured walking mode on this branch.

### 6. Unit conversion trap

`param.yaml` uses **degrees** and **milliseconds** for pose offsets and timing. `preset_walking.yaml` uses **radians** and **seconds** (matching Bascorro Studio units). The `loadWalkingParam()` function multiplies by `DEGREE2RADIAN` and `0.001` respectively [source/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml:L45](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml#L45). Field names also differ: `foot_height`/`swing_right_left`/`swing_top_down` (param.yaml) correspond to `z_move_amplitude`/`y_swap_amplitude`/`z_swap_amplitude` (Studio/preset).

---

## Interfaces and configuration

- **param.yaml** is read exactly once at boot by `loadWalkingParam()` [source/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml:L50](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml#L50). Changes require restarting `op3_manager` [source/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml:L51-L52](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml#L51-L52).
- The demo module overwrites x/y/angle move amplitudes on top of param.yaml via preset values and its own ramp logic [source/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml:L52](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml#L52).
- Sending "save" on `/robotis/walking/command` rewrites this file and drops comments [source/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml:L57](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml#L57).
- `walking_module` control cycle is 8 ms [source/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp:L63](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp#L63).
- Idle tracking is capped at 25 deg/s max step [source/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp:L125-L129](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp#L125-L129).

---

## Untested operation notes

Commands found in source were **not executed**:
- `op3_manager` restart to reload param.yaml (referenced at [source/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml:L51](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml#L51))
- Sending "save" on `/robotis/walking/command` to persist parameters ([source/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml:L57](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml#L57))
- Running demo with `kick_orbit_left_yaw_sign: -1.0` to invert turn direction ([source/src/ROBOTIS-OP3-Demo/op3_demo/config/preset_walking.yaml:L57](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_demo/config/preset_walking.yaml#L57))

No build, install, simulation or physical robot tests were performed. All parameter values, ramp timings and IK failure reports come from source comments and cited log timestamps.

---

## Uncertainty and conflicts

| Area | Status | Source |
|---|---|---|
| `geser_kiri` / `geser_kanan` true init_x_offset | Conflict: Studio stores `-0.18` but source kept `-0.03`. Speculation that intended value is `-0.018` (same as `mencari_celah`) has no confirmation. | [source/src/ROBOTIS-OP3-Demo/op3_demo/config/preset_walking.yaml:L343-L358](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_demo/config/preset_walking.yaml#L343-L358) |
| `geser_kanan` pelvis/hip_pitch offset | Values written explicitly as 0.05/0.14 on 2026-09-08 but Studio screenshot did not reach bottom of panel; may differ. | [source/src/ROBOTIS-OP3-Demo/op3_demo/config/preset_walking.yaml:L397-L400](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_demo/config/preset_walking.yaml#L397-L400) |
| `soft_start_time` in `jalan` | Deliberately set to 0.9 s in preset, different from saved Studio version. Comment says "SENGAJA BEDA — jangan dianggap kesalahan sinkronisasi" | [source/src/ROBOTIS-OP3-Demo/op3_demo/config/preset_walking.yaml:L124-L127](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_demo/config/preset_walking.yaml#L124-L127) |
| Balance gains | Present in config but unused because `balance_enable: false`. Whether these gains reflect tested tuning or carry-forward values is unknown. | [source/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml:L79-L82](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml#L79-L82) |
| Kinematic link masses/CoM | Values exist in `op3_kinematics_dynamics.cpp` but were only partially read (first 160 lines cover base–head links). Leg link parameters not inspected. | [source/src/ROBOTIS-OP3/op3_kinematics_dynamics/src/op3_kinematics_dynamics.cpp:L1-L160](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_kinematics_dynamics/src/op3_kinematics_dynamics.cpp#L1-L160) |

---

## Sources (files read)

- `source/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml` — full 85 lines
- `source/src/ROBOTIS-OP3-Demo/op3_demo/config/preset_walking.yaml` — full 453 lines
- `source/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp` — lines 1–160 + grep for 17 symbol matches
- `source/src/ROBOTIS-OP3/op3_kinematics_dynamics/src/op3_kinematics_dynamics.cpp` — lines 1–160
- `drafts/DIFFERENCES.md` — full file
- `drafts/SHARED-INDEX.md` — full file
