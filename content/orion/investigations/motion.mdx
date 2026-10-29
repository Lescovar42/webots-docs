# Orion: Walking, motion and kinematic differences

**Branch:** ORION_NEW — **Commit:** dba5be3fefbada854b8d6c11d6655f479b482574
**Stage:** robot-differences — **Scope:** Representative source investigation, not exhaustive.

---

## Scope and unexamined files

This card covers walking-gait parameters, balance gains, inverse-kinematics behavior, and the idle-stance mechanism in the OP3 walking module. The following 13 changed/unique files belonging to the broader "walking/motion/kinematics" group were listed in `drafts/DIFFERENCES.md` but not inspected in detail here:

- `source/src/ROBOTIS-OP3/op3_action_module/src/action_module.cpp`
- `source/src/ROBOTIS-OP3/op3_base_module/data/ini_pose.yaml`
- `source/src/ROBOTIS-OP3/op3_base_module/src/base_module.cpp`
- `source/src/ROBOTIS-OP3/op3_direct_control_module/src/direct_control_module.cpp`
- `source/src/ROBOTIS-OP3/op3_head_control_module/include/op3_head_control_module/head_control_module.h`
- `source/src/ROBOTIS-OP3/op3_head_control_module/src/head_control_module.cpp`
- `source/src/ROBOTIS-OP3/op3_manager/config/OP3.robot`
- `source/src/ROBOTIS-OP3/op3_manager/config/dxl_init_OP3.yaml`
- `source/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py`
- `source/src/ROBOTIS-OP3/op3_manager/src/op3_manager.cpp`
- `source/src/ROBOTIS-OP3/op3_tuning_module/src/tuning_module.cpp`
- `source/src/ROBOTIS-OP3/op3_walking_module/include/op3_walking_module/op3_walking_module.h`
- `source/src/ROBOTIS-OP3/open_cr_module/include/open_cr_module/open_cr_module.h`
- `source/src/ROBOTIS-OP3/open_cr_module/src/open_cr_module.cpp`

---

## Init-Pose offsets fitted to Orion hardware

The parametric starting stance in [source/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml:L1-L24](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml#L1-L24) is annotated as being fitted to *action page 2 (WALKING_READY) of `motion_4095_ORION.bin`*. The file comments state that the IK-reachable joints match page 2 within ~1.6 degrees and that the knees absorb the remainder through `walking_bias_` because page 2 stands slightly beyond full extension (right −12 deg, left −22 deg past straight) [source/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml:L5-L7](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml#L5-L7).

Selected offsets differ from the module's C++ defaults:

| Parameter | param.yaml (Orion) | C++ default |
|---|---|---|
| `period_time` | 780 ms | 600 ms ([op3_walking_module.cpp:L127](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp#L127)) |
| `dsp_ratio` | 0.3 | 0.1 ([op3_walking_module.cpp:L128](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp#L128)) |
| `step_forward_back_ratio` | 0.25 | 0.28 ([op3_walking_module.cpp:L129](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp#L129)) |
| `foot_height` (z_move_amplitude) | 0.033 m | 0.040 m ([op3_walking_module.cpp:L133](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp#L133)) |
| `pitch_offset` | 9.4 deg | 9.4 deg (same) |
| `hip_pitch_offset` | 9.4 deg | 9.4 deg (same) |
| `arm_swing_gain` | 0.2 | 1.5 ([op3_walking_module.cpp:L144](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp#L144)) |

The `y_offset` of 0.025 is explicitly noted as the knob for foot separation *while walking* because `computeNeutralLegAngle()` excludes it from the reference stance, meaning it survives the `walking_bias_` subtraction [source/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml:L16-L20](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml#L16-L20).

---

## Balance gains

The Orion-tuned balance gains are notably smaller than defaults:

| Gain | param.yaml | C++ default |
|---|---|---|
| `balance_hip_roll_gain` | 0.35 | 0.5 |
| `balance_knee_gain` | 0.4 | 0.3 |
| `balance_ankle_roll_gain` | 0.7 | 1.0 |
| `balance_ankle_pitch_gain` | 0.9 | 0.9 |

These multiply gyro-error signals in `sensoryFeedback()` with an internal scaling factor of 0.05 [source/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp:L1137-L1164](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp#L1137-L1164). The reduced hip-roll and ankle-roll gains infer a more cautious roll-correction on Orion, possibly to reduce lateral oscillation.

---

## walking_bias_ and idle stance tracking

The walking module captures the current joint goals into `captured_init_pose_` when walking is first enabled, then computes `walking_bias_` as `captured − neutral_IK_stance` [source/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp:L506-L522](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp#L506-L522). During idle (module running but gait not started), legs track the *current* param.yaml offsets via `computeNeutralLegAngle()`, rate-limited to 25 deg/s per 8 ms control cycle, rather than a frozen copy [source/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp:L529-L578](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp#L529-L578). This means publishing updated offsets on `/robotis/walking/set_params` (the Apply button in Bascorro Studio) moves the robot immediately without starting the gait.

---

## Inverse kinematics clamping

The IK solver in `op3_kinematics_dynamics.cpp` has an added safeguard: law-of-cosines arguments passed to `acos()` and `asin()` are clamped to [−1, +1] [source/src/ROBOTIS-OP3/op3_kinematics_dynamics/src/op3_kinematics_dynamics.cpp:L1006-L1032](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_kinematics_dynamics/src/op3_kinematics_dynamics.cpp#L1006-L1032). The source comment explains that without clamping, an out-of-reach foot pose produces NaN, which freezes the legs while the arm swing continues [source/src/ROBOTIS-OP3/op3_kinematics_dynamics/src/op3_kinematics_dynamics.cpp:L1011-L1013](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_kinematics_dynamics/src/op3_kinematics_dynamics.cpp#L1011-L1013). With clamping, IK degrades gracefully to the nearest reachable pose. This is an Orion-specific robustness improvement.

---

## Motion presets in gui_motion.yaml

The GUI demo config defines motion indices [source/src/ROBOTIS-OP3-Tools/op3_gui_demo/config/gui_motion.yaml:L1-L26](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Tools/op3_gui_demo/config/gui_motion.yaml#L1-L26). Index 2 maps to `WALKING_READY` (the soccer-specific preparation pose), and index 9 maps to `Walk Ready`. The distinction between index 2 (labeled "WALKING_READY" under the soccer section) and index 9 ("Walk Ready" in the general section) suggests two different preparation postures exist in the motion binary.

---

## Untested operation notes

All operational descriptions above are derived from source inspection. No commands were executed, no tests were run, and no simulation or physical robot runs were performed. The following items are found in source but remain unverified suggestions:

- The 25 deg/s rate limit on idle tracking ([op3_walking_module.cpp:L95-L98](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp#L95-L98)) -- actual servo response may differ on physical hardware vs simulation.
- The NaN-clamping behavior ([op3_kinematics_dynamics.cpp:L1006-L1032](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_kinematics_dynamics/src/op3_kinematics_dynamics.cpp#L1006-L1032)) -- graceful degradation was inferred from comments, not observed.

---

## Uncertainty and conflicts

- The param.yaml comment claims knee joints "cannot be matched because page 2 stands slightly past full extension" [source/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml:L5-L7](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml#L5-L7), but the comment does not specify which knee encoder sign convention is used; this may affect whether −12 deg means over-extended or under-extended relative to the IK model.
- The `hip_pitch_offset` is said to "cancel out of the gait" (subtracted via `walking_bias_`) [source/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml:L21-L23](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml#L21-L23), yet it is explicitly forwarded to `BallFollower` as the torso lean for distance estimation. This dual use was not traced in the demo source during this investigation.
- Whether the reduced balance gains (0.35 hip roll, 0.7 ankle roll) are physically necessary or were chosen for simulation stability in Webots is unknown.

---

## Sources inspected

| File | Lines read |
|---|---|
| `source/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml` | L1-L46 |
| `source/src/ROBOTIS-OP3/op3_walking_module/src/op3_walking_module.cpp` | L1-L160, L500-L579, L1120-L1199 |
| `source/src/ROBOTIS-OP3/op3_kinematics_dynamics/src/op3_kinematics_dynamics.cpp` | L1-L160, L1000-L1079 |
| `source/src/ROBOTIS-OP3-Tools/op3_gui_demo/config/gui_motion.yaml` | L1-L26 |
| `drafts/DIFFERENCES.md` | L1-L171 |
| `drafts/SHARED-INDEX.md` | L1-L21 |
