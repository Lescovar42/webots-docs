# Chronus: Localization, Navigation, and Behavior Differences

**Branch:** `CHRONUS_NEW` | **Commit:** `54998e7c56e5b2cce4c1c533758c7d2f2cf7698b`
**Stage:** robot-differences | **Focus:** Navigation & behavior loop

---

## Scope

This card investigates localization, navigation, and high-level behavior differences observable in the `op3_demo` package on the `CHRONUS_NEW` branch. Four assigned source anchors were read in full or in range-sliced windows: `demo_node.cpp`, `op_demo.h`, `soccer_demo.h`, and `soccer_demo.cpp`. Two supporting headers (`ball_follower.h`, `ball_tracker.h`) were also inspected to understand the navigation dataflow. Many changed files in `DIFFERENCES.md` remain unexamined, including the ball detector config files, ball follower implementation, walking module configuration, and the bascorro_studio tooling.

---

## Observed Behavior

### No classical localization stack

The demo node does not subscribe to odometry, map services, or any SLAM/nav2 infrastructure. Motion is driven entirely by the `op3_walking_module` interface. The `BallFollower` class computes incremental walking commands (`setWalkingParam`) from camera-derived ball angles, not from a global map position [source/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/ball_follower.h:L96-L99](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/ball_follower.h#L96-L99). Navigation is therefore _reactive and vision-guided_ rather than map-based.

### Behavior state machine

The demo node (`demo_node.cpp`) manages a finite-state switch among `Ready`, `SoccerDemo`, `VisionDemo`, and `ActionDemo` [source/src/ROBOTIS-OP3-Demo/op3_demo/src/demo_node.cpp:L30-L37](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3-Demo/op3_demo/src/demo_node.cpp#L30-L37). Mode transitions are triggered by:
- Hardware button events on `/robotis/open_cr/button` [source/src/ROBOTIS-OP3-Demo/op3_demo/src/demo_node.cpp:L88-L89](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3-Demo/op3_demo/src/demo_node.cpp#L88-L89).
- Topic commands on `/robotis/mode_command` and `/robotis/demo_command` [source/src/ROBOTIS-OP3-Demo/op3_demo/src/demo_node.cpp:L90-L91](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3-Demo/op3_demo/src/demo_node.cpp#L90-L91).

Inside SoccerDemo, the robot cycles through states `Waited`, `TrackingAndFollowing`, `ReadyToKick`, `ReadyToCeremony`, `ReadyToGetup` [source/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/soccer_demo.h:L54-L60](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/soccer_demo.h#L54-L60), and fall-detection states `Stand`, `Fallen_Forward`, `Fallen_Behind` (thresholds at pitch ±60°) [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp:L28-L29](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp#L28-L29).

### Timing changes

Two reaction-time adjustments are present:

1. **Settle-after-start window** reduced from ~1 s to ~0.3 s (`SPIN_RATE * 3 / 10` instead of `1 * SPIN_RATE`) [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp:L159-L161](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp#L159-L161). The comment states the goal is for the robot to "react quickly to the Start button."
2. **Manager polling interval** shortened from 1 s to 250 ms on boot [source/src/ROBOTIS-OP3-Demo/op3_demo/src/demo_node.cpp:L120-L121](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3-Demo/op3_demo/src/demo_node.cpp#L120-L121).

### START/STOP debounce

A new member `stop_debounce_until_` (type `std::chrono::steady_clock::time_point`) was added to `SoccerDemo` to reject rapid START toggles after a STOP [source/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/soccer_demo.h:L144-L145](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/soccer_demo.h#L144-L145). The exact debounce window value is not declared in the inspected headers; it is inferred to be set in the `.cpp` implementation.

### Head-control toggle

Head participation in soccer tracking is configurable at runtime via the `use_head_control` ROS parameter, defaulting to `true` [source/src/ROBOTIS-OP3-Demo/op3_demo/src/demo_node.cpp:L107-L110](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3-Demo/op3_demo/src/demo_node.cpp#L107-L110). When disabled, the `BallTracker` suppresses head joint movement, leaving body-only following active.

---

## Interfaces / Configuration

| Interface | Transport | Role |
|---|---|---|
| `/robotis/open_cr/button` | `std_msgs/String` | Hardware button events (start/mode-long/user-long) |
| `/robotis/mode_command` | `std_msgs/String` | Remote mode selection (`soccer`/`vision`/`action`/`ready`) |
| `/robotis/demo_command` | `std_msgs/String` | Start/Stop/Restart soccer sub-commands |
| `/robotis/open_cr/imu` | `sensor_msgs/Imu` | IMU data for fall detection |
| `/ball_tracker/command` | `std_msgs/String` | Head-tracker start/stop issued by SoccerDemo |
| `/robotis/action/page_num` | `std_msgs/Int32` | Action page switching (page 2 = WALKING_READY) |
| Walking module srv | `SetJointModule` | Joint-to-module reassignment for demo mode |

Motion index values are enumeration literals in `op_demo.h` [source/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/op_demo.h:L31-L39](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/op_demo.h#L31-L39); e.g., `RightKick = 218`, `LeftKick = 104`, `GetUpFront = 85`.

---

## Untested Operation Notes

- The `dxlTorqueChecker()` helper publishes `"check"` to `/robotis/dxl_torque` before each demo start [source/src/ROBOTIS-OP3-Demo/op3_demo/src/demo_node.cpp:L351-L356](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3-Demo/op3_demo/src/demo_node.cpp#L351-L356). This command was found in source but was not executed.
- The `setLED()` helper drives RGB LEDs on the OpenCR board via `/robotis/sync_write_item` [source/src/ROBOTIS-OP3-Demo/op3_demo/src/demo_node.cpp:L328-L335](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3-Demo/op3_demo/src/demo_node.cpp#L328-L335). This command was found in source but was not executed.
- All walking commands flow through the private `op3_walking_module` service layer (`SetWalkingParam`, `GetWalkingParam`); the actual gait kinematics are outside the demo package and were not inspected here.

---

## Uncertainties and Conflicts

1. **Debounce window duration.** The `stop_debounce_until_` member exists [source/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/soccer_demo.h:L144-L145](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/soccer_demo.h#L144-L145) but the constant value assigned during initialization was not located in the inspected header region. The value may be inline in a portion of `soccer_demo.cpp` not read in this pass.
2. **Grass-surface adaptation.** A member `is_grass_` appears in the header [source/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/soccer_demo.h:L131](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/soccer_demo.h#L131) and is hard-coded to `false` in the constructor [source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp:L71-L72](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp#L71-L72), suggesting a dormant feature branch for different ground conditions.
3. **Ball-following kinematics.** The `calcFootstep` method [source/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/ball_follower.h:L99-L100](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/ball_follower.h#L99-L100) and the constants `MAX_FB_STEP`, `SPOT_FB_OFFSET`, etc. [source/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/ball_follower.h:L81-L93](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/ball_follower.h#L81-L93) contain navigation-relevant tuning values. Their definitions are in the unexamined `ball_follower.cpp`.
4. **Webots vs. physical robot.** The demo node subscribes to `/robotis/open_cr/imu` and `/robotis/open_cr/button`, which map to OpenCR hardware on a physical robot. In Webots simulation, these topics are supplied by the OpenCR emulator node. The source does not branch on simulation mode; behavior is expected to be identical, but actuator latency differences are not characterized.

---

## Sources

- `source/src/ROBOTIS-OP3-Demo/op3_demo/src/demo_node.cpp` (lines 1–418, full)
- `source/src/ROBOTIS-OP3-Demo/op3_demo/src/soccer/soccer_demo.cpp` (lines 1–479, partial)
- `source/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/op_demo.h` (lines 1–62, full)
- `source/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/soccer_demo.h` (lines 1–153, full)
- `source/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/ball_follower.h` (lines 1–137, full)
- `source/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/ball_tracker.h` (lines 1–121, full)
- `drafts/DIFFERENCES.md` (file-hash diff list)
- `drafts/SHARED-INDEX.md` (shared-code cross-reference)
