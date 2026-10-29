> Shared file-content analysis, using the Alphonse snapshot. Robot-specific runtime conditions require separate review.

# Shared Code: Footstep Planning — Stage: shared-core

**Snapshot:** Alphonse, branch `ALPHONSE_NEW_V2`, commit `adacde8f6e01e6439d170fb6bce025acc051bfa3`
**Scope:** Representative investigation of `footstep_planner` package under `source/src/humanoid_navigation/footstep_planner/`. Selected source paths share identical SHA-256 content across Alphonse, Chronus, and Orion snapshots. This card documents code contracts observed in the Alphonse canonical snapshot; it does not establish runtime equivalence across robots.

---

## 1. Scope

This card covers the `footstep_planner` ROS 2 package, which implements a discrete-space footstep planner for humanoid locomotion. All four assigned files were inspected. Two additional headers were followed as references: `PlanningState.h` and `FootstepPlanner.h`. Several source `.cpp` files in `src/` were not read in full and are listed in §6.

The package builds a shared library (`libfootstep_planner`) plus three executables, depends on the SBPL planner library, `gridmap_2d`, and standard ROS 2 navigation stacks.

---

## 2. Observed Behavior

### 2.1 Planning Architecture

The core planner is `FootstepPlanner` (`FootstepPlanner.h`), which inherits from `rclcpp::Node` [source/src/humanoid_navigation/footstep_planner/include/footstep_planner/FootstepPlanner.h:L32](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/footstep_planner/include/footstep_planner/FootstepPlanner.h#L32). It wraps an SBPL planner instance (`SBPLPlanner` via `ivPlannerPtr` at line 91) operating over a discrete grid map (`ivPlannerEnvironmentPtr` at line 89). Planning states are represented by `PlanningState`, which encodes a discretized `(x, y, theta)` position plus a `Leg` enum (left/right) [source/src/humanoid_navigation/footstep_planner/include/footstep_planner/PlanningState.h:L12-L46](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/footstep_planner/include/footstep_planner/PlanningState.h#L12-L46).

The `Footstep` class defines individual step displacement vectors and their forward/reverse application on planning states [source/src/humanoid_navigation/footstep_planner/include/footstep_planner/Footstep.h:L14-L20](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/footstep_planner/include/footstep_planner/Footstep.h#L14-L20). Each `Footstep` stores precomputed discrete successor/predecessor position deltas for both left and right legs [source/src/humanoid_navigation/footstep_planner/include/footstep_planner/Footstep.h:L35-L38](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/footstep_planner/include/footstep_planner/Footstep.h#L35-L38).

### 2.2 Build Targets

The CMake configuration [source/src/humanoid_navigation/footstep_planner/CMakeLists.txt:L42-L86](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/footstep_planner/CMakeLists.txt#L42-L86) defines:
- **Shared library** `footstep_planner` from 13 source files (lines 42-52).
- **Executables:** `footstep_planner_node`, `footstep_planner_walls`, `footstep_navigation_node` (lines 76-86).
- Key link dependencies: `sbpl`, `gridmap_2d`, `OpenCV`, and all standard ROS 2 nav/TF2 packages (line 74).

### 2.3 Configuration

The file `footsteps_asimo.yaml` provides displacement parameterization modeled after large humanoids like ASIMO/HRP-2 [source/src/humanoid_navigation/footstep_planner/config/footsteps_asimo.yaml:L1-L29](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/footstep_planner/config/footsteps_asimo.yaml#L1-L29). It specifies:
- 14 step displacement vectors in `(x, y, theta)` (lines 6-10).
- Foot geometry: `0.16 × 0.10 × 0.015 m` with `0.14 m` separation (lines 13-15).
- Max step reach: `{x: 0.22, y: 0.28, theta: 0.7}` (line 18).
- Step range bounding box (lines 26-29).

### 2.4 Launch Composition

`fake_loc_from_odom.launch.py` [source/src/humanoid_navigation/footstep_planner/launch/fake_loc_from_odom.launch.py:L1-L27](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/footstep_planner/launch/fake_loc_from_odom.launch.py#L1-L27) composes:
- `fake_localization` node with `base_frame_id: torso` and zero pose offsets (lines 8-20).
- A `corrected_initialpose` helper node (lines 22-26).

---

## 3. Interfaces and Configuration

| Interface | Type | Description |
|---|---|---|
| `planFootsteps` | ROS 2 Service (`humanoid_nav_msgs/srv/PlanFootsteps`) | Plan footsteps between poses [source/src/humanoid_navigation/footstep_planner/include/footstep_planner/FootstepPlanner.h:L44-L45](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/footstep_planner/include/footstep_planner/FootstepPlanner.h#L44-L45) |
| `planFootstepsBetweenFeet` | ROS 2 Service (`humanoid_nav_msgs/srv/PlanFootstepsBetweenFeet`) | Plan with explicit foot-pose constraints [source/src/humanoid_navigation/footstep_planner/include/footstep_planner/FootstepPlanner.h:L46-L47](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/footstep_planner/include/footstep_planner/FootstepPlanner.h#L46-L47) |
| `mapCallback` | Subscription (`nav_msgs/OccuracyGrid`) | Map updates trigger re-planning [source/src/humanoid_navigation/footstep_planner/include/footstep_planner/FootstepPlanner.h:L59](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/footstep_planner/include/footstep_planner/FootstepPlanner.h#L59) |
| `goalPoseCallback` / `startPoseCallback` | Subscriptions | Update goal/start poses dynamically [source/src/humanoid_navigation/footstep_planner/include/footstep_planner/FootstepPlanner.h:L57-L58](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/footstep_planner/include/footstep_planner/FootstepPlanner.h#L57-L58) |
| Visualization publishers | `MarkerArray`, `Path`, `PointCloud` | Expanded states, heuristic paths, and footstep sequences [source/src/humanoid_navigation/footstep_planner/include/footstep_planner/FootstepPlanner.h:L99-L110](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/footstep_planner/include/footstep_planner/FootstepPlanner.h#L99-L110) |

Planner-tunable members include `ivMaxSearchTime`, `ivInitialEpsilon`, `ivSearchUntilFirstSolution`, and `ivPlannerType` [source/src/humanoid_navigation/footstep_planner/include/footstep_planner/FootstepPlanner.h:L119-L124](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/footstep_planner/include/footstep_planner/FootstepPlanner.h#L119-L124).

---

## 4. Untested Operation Notes

The following commands and operations are found in source but have **not been executed**:
- CMake build via the `CMakeLists.txt` configuration [source/src/humanoid_navigation/footstep_planner/CMakeLists.txt:L72-L86](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/footstep_planner/CMakeLists.txt#L72-L86). Three executables would be produced but remain unbuilt in this investigation.
- Launch via `fake_loc_from_odom.launch.py` [source/src/humanoid_navigation/footstep_planner/launch/fake_loc_from_odom.launch.py:L5-L27](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/footstep_planner/launch/fake_loc_from_odom.launch.py#L5-L27) — this would start `fake_localization` and the `corrected_initialpose` node.
- Runtime service calls to `planFootsteps` and `planFootstepsBetweenFeet` [source/src/humanoid_navigation/footstep_planner/include/footstep_planner/FootstepPlanner.h:L44-L47](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/footstep_planner/include/footstep_planner/FootstepPlanner.h#L44-L47).
- The SBPL-based search in `FootstepPlanner::run()` is referenced but the implementation was not inspected.

---

## 5. Uncertainty and Conflicts

- **Runtime equivalence**: Identical file hashes are observed across Alphonse, Chronus, and Orion snapshots for the selected paths, but no build or execution was performed. Shared code does not guarantee shared runtime behavior.
- **Calibration values**: The `footsteps_asimo.yaml` parameters (foot size, step reach, displacements) [source/src/humanoid_navigation/footstep_planner/config/footsteps_asimo.yaml:L13-L29](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/footstep_planner/config/footsteps_asimo.yaml#L13-L29) are modeled after ASIMO/HRP-2. They should not be transferred as robot-specific calibration values for Alphonse, Chronus, or Orion.
- **Frame convention**: The launch file uses `base_frame_id: torso` [source/src/humanoid_navigation/footstep_planner/launch/fake_loc_from_odom.launch.py:L16](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/footstep_planner/launch/fake_loc_from_odom.launch.py#L16). Whether this matches the actual TF tree of the target robots is unknown.
- **Planner type selection**: The `ivPlannerType` member [source/src/humanoid_navigation/footstep_planner/include/footstep_planner/FootstepPlanner.h:L124](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/footstep_planner/include/footstep_planner/FootstepPlanner.h#L124) suggests multiple algorithm backends; which is active at runtime depends on unexamined configuration.

---

## 6. Unexamined Source Files

The following files are present but were **not read** due to scope constraints:

- `src/FootstepPlanner.cpp`, `src/FootstepNavigation.cpp`, `src/FootstepPlannerNode.cpp`, `src/FootstepPlannerEnvironment.cpp`, `src/Footstep.cpp`, `src/PlanningState.cpp`, `src/Heuristic.cpp`, `src/helper.cpp`, `src/PathCostHeuristic.cpp`, `src/PlanningStateChangeQuery.cpp`, `src/State.cpp` — core implementation (12 files)
- `src/footstep_planner.cpp`, `src/footstep_planner_walls.cpp`, `src/footstep_navigation.cpp` — entry-point executables (3 files)
- Headers: `FootstepNavigation.h`, `FootstepPlannerNode.h`, `FootstepPlannerEnvironment.h`, `Heuristic.h`, `PathCostHeuristic.h`, `PlanningStateChangeQuery.h`, `State.h`, `helper.h`, `XmlRpc.h`, `XmlRpcException.h`, `XmlRpcValue.h` (11 headers)

---

## 7. Sources

| File | Lines |
|---|---|
| `CMakeLists.txt` | L1-L108 |
| `config/footsteps_asimo.yaml` | L1-L29 |
| `launch/fake_loc_from_odom.launch.py` | L1-L27 |
| `include/footstep_planner/Footstep.h` | L1-L43 |
| `include/footstep_planner/FootstepPlanner.h` | L1-L131 |
| `include/footstep_planner/PlanningState.h` | L1-L50 |
