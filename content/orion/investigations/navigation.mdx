# Orion: Localization, Navigation and Behavior Differences

## Scope

This card examines how navigation and behavioral state management differ between Orion (branch `ORION_NEW`, commit `dba5be3f`) and Alphonse. It focuses on the `SoccerDemo` entry point, its interaction with the walking/following stack, and related configuration changes. Sources inspected: `op_demo.h` (62 lines), `soccer_demo.h` (153 lines), `demo_node.cpp` (417 lines), and `soccer_demo.cpp` (847 lines). Four changed eligible files from `drafts/DIFFERENCES.md` in the `op3_demo` package were targeted; files outside this package (ball detector configs, walking module, base module, head control, etc.) are **not** re-inspected here. Several changed files remain unexamined (ball follower, ball tracker sources, action/vision demo sources, and launch files).

---

## Observed Behavior

### Demo lifecycle and mode selection

`demo_node.cpp` maintains a `Demo_Status` state machine (`Ready`, `SoccerDemo`, `VisionDemo`, `ActionDemo`) [source/src/ROBOTIS-OP3-Demo/op3_demo/src/demo_node.cpp:L30-L37](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/src/demo_node.cpp#L30-L37). Mode switching is triggered either by a button callback on `/robotis/open_cr/button` or by a text command on `/robotis/mode_command` [source/src/ROBOTIS-OP3-Demo/op3_demo/src/demo_node.cpp:L87-L91](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/src/demo_node.cpp#L87-L91). Both paths converge on the same `apply_desired` gate [source/src/ROBOTIS-OP3-Demo/op3_demo/src/demo_node.cpp:L147-L184](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/src/demo_node.cpp#L147-L184), which disables the current demo before transitioning.

### Soccer demo start / stop

When `SoccerDemo::setDemoEnable()` runs, it publishes `"start"` on `/ball_tracker/command` and calls `startSoccerMode()` [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp:L107-L117](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp#L107-L117). `startSoccerMode()` performs a deliberate hand-off sequence:

1. Switches all joints to `action_module` [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp:L584](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp#L584)
2. Plays the `WalkingReady` motion index (page 2 per `op_demo.h`) [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp:L586](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp#L586)
3. Polls `/robotis/action/is_running` until the pose completes [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp:L591-L592](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp#L591-L592)
4. Reassigns the body to `walking_module` and the head to `head_control_module` [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp:L594](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp#L594)

This explicit calibration-step before walking ensures the robot stands in a known pose before navigation begins.

The `stopSoccerMode()` path zeroes walking amplitudes via `ball_follower_.stopFollowing()`, stops head tracking, and sets an 800 ms debounce window so rapid double-presses do not inadvertently restart walking [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp:L604-L630](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp#L604-L630). This debounce was introduced as an Orion-specific safety measure; the timestamp is tracked in the `stop_debounce_until_` member [source/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/soccer_demo.h:L145-L146](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/soccer_demo.h#L145-L146).

### Ball following and kick decision

When ball tracking reports `BallTracker::Found`, the follower issues walk commands using pan/tilt from the tracker [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp:L181-L191](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp#L181-L191). Once the ball is in range (`ball_follower_.isBallInRange()`), following stops and `handleKick()` fires [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp:L237-L243](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp#L237-L243). `handleKick()` sleeps 2 s, switches back to `action_module`, determines kick side (`OnRight`/`OnLeft`), plays the appropriate motion (RightKick=218, LeftKick=104 per `op_demo.h` [source/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/op_demo.h:L35-L37](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/op_demo.h#L35-L37)), then schedules a restart via `restart_soccer_ = true` [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp:L674-L725](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp#L674-L725).

### Fall detection

Fall state is derived from IMU pitch with exponential smoothing (α = 0.4) [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp:L560-L564](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp#L560-L564). Thresholds are ±60° forward/backward [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp:L28-L29](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp#L28-L29). If a fall is detected during the main process loop, `handleFallen()` plays the appropriate get-up action (GetUpFront=85 / GetUpBack=86) [source/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/op_demo.h:L33-L34](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/op_demo.h#L33-L34) and re-enters soccer mode after recovery [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp:L728-L766](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp#L728-L766).

---

## Interfaces and Configuration

| Channel | Direction | Purpose |
|---------|-----------|---------|
| `/robotis/open_cr/imu` | Subscribe | IMU for fall detection [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp:L90-L91](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp#L90-L91) |
| `/ball_tracker/command` | Publish | Start/stop head tracking [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp:L94](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp#L94) |
| `/robotis/action/is_running` | Service | Query action completion [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp:L807](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp#L807) |
| `/robotis/set_present_joint_ctrl_modules` | Service | Reassign joint control ownership [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp:L405](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp#L405) |
| `/robotis/action/page_num` | Publish | Trigger discrete motions [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp:L777](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp#L777) |
| `/robotis/button` | Subscribe | Physical button events [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp:L58](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp#L58) |
| `/robotis/mode_command` | Subscribe | Remote mode switching [source/src/ROBOTIS-OP3-Demo/op3_demo/src/demo_node.cpp:L90](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/src/demo_node.cpp#L90) |
| `/robotis/demo_command` | Subscribe | Remote start/stop [source/src/ROBOTIS-OP3-Demo/op3_demo/src/demo_node.cpp:L91](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/src/demo_node.cpp#L91) |

Head tracking is controlled by the `use_head_control` parameter (declared in `demo_node.cpp` with default `true`) [source/src/ROBOTIS-OP3-Demo/op3_demo/src/demo_node.cpp:L107-L110](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/src/demo_node.cpp#L107-L110) and forwarded to `ball_tracker_` via `setUsingHeadControl()` [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp:L102-L105](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp#L102-L105).

Joint-to-ID mapping is loaded at construction from `op3_gui_demo/config/gui_config.yaml` via the `gui_demo` package path [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp:L47-L51](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp#L47-L51).

---

## Untested Operation Notes

All commands and topics listed above were **found in source but not executed**. Boot-time pose initialization in `demo_node` avoids duplicating the `WALKING_READY` action page because `op3_manager` already runs it — a note visible in a source comment [source/src/ROBOTIS-OP3-Demo/op3_demo/src/demo_node.cpp:L135-L138](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/src/demo_node.cpp#L135-L138). The node waits for `/op3_manager` using `checkManagerRunning()` before entering its main loop [source/src/ROBOTIS-OP3-Demo/op3_demo/src/demo_node.cpp:L117-L128](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/src/demo_node.cpp#L117-L128). The settle-delay to `action_module` is 500 ms [source/src/ROBOTIS-OP3-Demo/op3_demo/src/demo_node.cpp:L54](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/src/demo_node.cpp#L54).

The original thread-based architecture (`processThread`, `trackingThread`) has been **commented out** and replaced by a single-loop `spin_some` design driven by `demo_node` [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp:L261-L279](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp#L261-L279). This architectural shift was observed in source but not validated at runtime.

---

## Simulated vs Physical Robot Behavior

This branch has a `webots_executor.py` tool in `op3_action_editor` (listed in `DIFFERENCES.md` line 56), allowing action playback in Webots simulation. However, the `SoccerDemo` code path exercises real IMU data, real servo control modules (`walking_module`, `action_module`, `head_control_module`), and physical button inputs. No equivalent simulated soccer demo was inspected. All navigation claims refer to **physical robot behavior only**.

---

## Uncertainty and Conflicts

- **Kick geometry calibration files are absent**: `DIFFERENCES.md` lists several files present in Alphonse but missing here: `op3_demo/config/KALIBRASI_TENDANG_2026-09-07.md`, `op3_demo/config/preset_walking.yaml`, and `kick_alignment_policy.h` with its test [drafts/DIFFERENCES.md:L147-L152]. Alphonse had explicit kick alignment logic and parameter presets; Orion's `handleKick()` uses a simpler pan/tilt decision via `ball_follower_.decideBallPositin()` [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp:L685](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp#L685). The practical navigation impact of this simplification is unknown without runtime data.
- **`is_grass_` is hardcoded to `false`**: The constructor hardcodes `is_grass_ = false` [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp:L72](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp#L72), even though the kick and get-up logic branches on it. The parameter declaration that would allow toggling it is commented out [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp:L70-L71](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp#L70-L71). This suggests the surface-adaptive motion offset is permanently disabled in this branch.
- **Ball follower/tracker source is unexamined**: The `BallFollower::isBallInRange()`, `BallFollower::getBallPosition()`, and `BallTracker::processTracking()` internals would contain the actual localization thresholds and navigation geometry. These files (`ball_follower.cpp`, `ball_tracker.cpp`) are marked as changed in `DIFFERENCES.md` but were not re-read here.
- **No autonomous localization stack**: Inspected source only covers reactive ball-following. There is no SLAM, map, or global planner reference in these files. Localization in this context means *ball position estimation from camera pan/tilt*, not robot localization in map coordinates.

---

## Sources

- `source/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/op_demo.h` — motion index enum, parent class
- `source/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/soccer_demo.h` — state enums, debouce member, service/publisher declarations
- `source/src/ROBOTIS-OP3-Demo/op3_demo/src/demo_node.cpp` — node lifecycle, mode selection, init pose guard
- `source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp` — soccer behavior: start/stop, kick, fall, IMU tracking
- `drafts/DIFFERENCES.md` — changed/missing file inventory relative to Alphonse
