> Shared file-content analysis, using the Alphonse snapshot. Robot-specific runtime conditions require separate review.

# Shared Code: Robot Localization and Navigation

**Stage:** shared-core — Canonical Alphonse snapshot (branch `ALPHONSE_NEW_V2`, commit `adacde8f6e01e6439d170fb6bce025acc051bfa3`)
**Scope:** The `humanoid_localization` ROS 2 package — representative investigation, not exhaustive source coverage.

---

## Scope

This card documents the `humanoid_localization` package found under Alphonse's `humanoid_navigation` workspace. The package implements a particle-filter-based simultaneous localization framework for humanoid robots using laser scans and point clouds against an octomap representation.[source/src/humanoid_navigation/humanoid_localization/CMakeLists.txt:L2-L2](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/humanoid_localization/CMakeLists.txt#L2-L2) Of 42 matching shared candidates across the Alphonse/Chronus/Orion snapshots, only the files listed below were inspected. Contents are byte-identical across all three snapshots, but runtime equivalence is not established.

**Unexamined files (present but not read):** source implementations (`HumanoidLocalization.cpp`, `MapModel.cpp`, `MotionModel.cpp`, `ObservationModel.cpp`, `RaycastingModel.cpp`, `EndpointModel.cpp`) and header utilities (`MotionModel.h`, `ObservationModel.h`, `MapModel.h`, `EndpointModel.h`, `RaycastingModel.h`, `tf2_utils.h`, `octomap_utils.h`, `transform_utils.h`, `humanoid_localization_defs.h`, `dynamicEDTOctomap.h`).

---

## Observed Behavior

The package provides a single ROS 2 node (`localization_node`) that instantiates `HumanoidLocalization`[source/src/humanoid_navigation/humanoid_localization/src/localization_node.cpp:L6-L24](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/humanoid_localization/src/localization_node.cpp#L6-L24). The class subscribes to laser scan (`sensor_msgs/LaserScan`), point cloud (`sensor_msgs/PointCloud2`), and IMU (`sensor_msgs/IMU`) topics, as well as an initial-pose topic (`PoseWithCovarianceStamped`).[source/src/humanoid_navigation/humanoid_localization/include/humanoid_localization/HumanoidLocalization.h:L64-L80](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/humanoid_localization/include/humanoid_localization/HumanoidLocalization.h#L64-L80)

### Localization pipeline (inferred from interface)

1. **Particle filter:** The class maintains a particle set (`Particles m_particles`)[source/src/humanoid_navigation/humanoid_localization/include/humanoid_localization/HumanoidLocalization.h:L165](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/humanoid_localization/include/humanoid_localization/HumanoidLocalization.h#L165), with methods for resampling, weight normalization, and effective particle count (nEff).[source/src/humanoid_navigation/humanoid_localization/include/humanoid_localization/HumanoidLocalization.h:L82-L97](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/humanoid_localization/include/humanoid_localization/HumanoidLocalization.h#L82-L97)
2. **Motion model:** A dedicated `MotionModel` library handles pose propagation between timesteps.[source/src/humanoid_navigation/humanoid_localization/CMakeLists.txt:L88-L98](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/humanoid_localization/CMakeLists.txt#L88-L98)
3. **Observation & raycasting:** `ObservationModel` and `RaycastingModel` compare sensor data against an octomap-based map.[source/src/humanoid_navigation/humanoid_localization/CMakeLists.txt:L100-L130](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/humanoid_localization/CMakeLists.txt#L100-L130) Raycasting can be toggled via the `use_raycasting` parameter.[source/src/humanoid_navigation/humanoid_localization/config/localization_conf_motion_test.yaml:L5](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/humanoid_localization/config/localization_conf_motion_test.yaml#L5)
4. **Distance transform:** The `dynamicEDT3D` component computes incremental 3D Euclidean distance transforms, used by the endpoint model for proximity evaluation.[source/src/humanoid_navigation/humanoid_localization/include/dynamicEDT3D/dynamicEDT3D.h:L47-L48](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/humanoid_localization/include/dynamicEDT3D/dynamicEDT3D.h#L47-L48)[source/src/humanoid_navigation/humanoid_localization/CMakeLists.txt:L132-L144](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/humanoid_localization/CMakeLists.txt#L132-L144)
5. **Pose output:** Best-particle, mean-particle, and full-pose-array estimates are published on dedicated topics.[source/src/humanoid_navigation/humanoid_localization/include/humanoid_localization/HumanoidLocalization.h:L132-L134](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/humanoid_localization/include/humanoid_localization/HumanoidLocalization.h#L132-L134)

### Control services

Three ROS service callbacks (type `std_srvs/Trigger`) expose:
- `globalLocalizationCallback` — triggers a global re-localization.[source/src/humanoid_navigation/humanoid_localization/include/humanoid_localization/HumanoidLocalization.h:L67-L70](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/humanoid_localization/include/humanoid_localization/HumanoidLocalization.h#L67-L70)
- `pauseLocalizationSrvCallback` / `resumeLocalizationSrvCallback` — pause and resume particle integration.[source/src/humanoid_navigation/humanoid_localization/include/humanoid_localization/HumanoidLocalization.h:L71-L78](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/humanoid_localization/include/humanoid_localization/HumanoidLocalization.h#L71-L78)

A boolean subscription (`pauseLocalizationCallback`) provides an alternative pause mechanism.[source/src/humanoid_navigation/humanoid_localization/include/humanoid_localization/HumanoidLocalization.h:L79](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/humanoid_localization/include/humanoid_localization/HumanoidLocalization.h#L79)

---

## Interfaces and Configuration

### Build system

| Component | Build target |
|---|---|
| Main node | `localization_node` executable[source/src/humanoid_navigation/humanoid_localization/CMakeLists.txt:L201-L208](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/humanoid_localization/CMakeLists.txt#L201-L208) |
| Shared library | `humanoidlocalization` (shared)[source/src/humanoid_navigation/humanoid_localization/CMakeLists.txt:L166-L191](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/humanoid_localization/CMakeLists.txt#L166-L191) |
| Sub-libraries | `transform_utils`, `mapmodel`, `motionmodel`, `observationmodel`, `raycastingmodel`, `dynamicedt3d`, `endpointmodel`[source/src/humanoid_navigation/humanoid_localization/CMakeLists.txt:L64-L161](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/humanoid_localization/CMakeLists.txt#L64-L161) |

C++17 is the minimum standard.[source/src/humanoid_navigation/humanoid_localization/CMakeLists.txt:L6-L8](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/humanoid_localization/CMakeLists.txt#L6-L8) OpenMP is hard-required for raycasting parallelism.[source/src/humanoid_navigation/humanoid_localization/CMakeLists.txt:L45](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/humanoid_localization/CMakeLists.txt#L45) SBPL (stochastic sampling-based planning library) is optional; if found, a `USE_SBPL` compile definition is added.[source/src/humanoid_navigation/humanoid_localization/CMakeLists.txt:L50-L56](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/humanoid_localization/CMakeLists.txt#L50-L56)

### Runtime parameters (from test config)

The file `localization_conf_motion_test.yaml` provides a minimal configuration sample:[source/src/humanoid_navigation/humanoid_localization/config/localization_conf_motion_test.yaml:L1-L26](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/humanoid_localization/config/localization_conf_motion_test.yaml#L1-L26)

| Parameter category | Notable values |
|---|---|
| `use_raycasting` | `true` |
| `init_from_truepose` | `true` |
| `num_particles` | 1 (degenerate test case) |
| `neff_factor` | 0 (disabled resampling threshold) |
| `initial_std` (6-DoF) | All zeros — no initial uncertainty |
| `motion_noise` (xx/yy/zz/RR/PP/YY) | All zeros — no motion noise |

These zero-motion-noise values indicate this is a test fixture, not a production deployment profile.[source/src/humanoid_navigation/humanoid_localization/config/localization_conf_motion_test.yaml:L20-L26](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/humanoid_localization/config/localization_conf_motion_test.yaml#L20-L26)

### Launch file

The launch script `nao_localization_laser.launch.py` accepts a `config_file` argument (default: `nao_localization_laser.yaml` from the package share directory)[source/src/humanoid_navigation/humanoid_localization/launch/nao_localization_laser.launch.py:L17-L24](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/humanoid_localization/launch/nao_localization_laser.launch.py#L17-L24) and spawns the `localization_node` under the name `humanoid_localization`.[source/src/humanoid_navigation/humanoid_localization/launch/nao_localization_laser.launch.py:L28-L34](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/humanoid_localization/launch/nao_localization_laser.launch.py#L28-L34) It validates file existence before launching.[source/src/humanoid_navigation/humanoid_localization/launch/nao_localization_laser.launch.py:L9-L13](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/humanoid_localization/launch/nao_localization_laser.launch.py#L9-L13)

---

## Untested Operation Notes

- The command `ros2 launch humanoid_localization nao_localization_laser.launch.py` is referenced by the launch file[source/src/humanoid_navigation/humanoid_localization/launch/nao_localization_laser.launch.py:L15-L34](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/humanoid_localization/launch/nao_localization_laser.launch.py#L15-L34) but has **not been executed**.
- No build, install, or runtime commands have been tested.
- The particle filter behavior in real or simulated (Webots) environments is entirely inferred from header declarations; internal implementation details in `.cpp` files were not read.
- IMU-based Z/R/P initialization appears supported via `initZRP`[source/src/humanoid_navigation/humanoid_localization/include/humanoid_localization/HumanoidLocalization.h:L109](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/humanoid_localization/include/humanoid_localization/HumanoidLocalization.h#L109) and `m_useIMU`[source/src/humanoid_navigation/humanoid_localization/include/humanoid_localization/HumanoidLocalization.h:L199](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/humanoid_localization/include/humanoid_localization/HumanoidLocalization.h#L199), but the exact fusion strategy is not visible from headers alone.

---

## Uncertainty and Conflicts

| Area | Status |
|---|---|
| Full parameter list | Unknown — the main `.cpp` source was not inspected; the header shows ~30 member variables but default values are unclear. |
| Coordinate frame conventions | The class declares `m_odomFrameId`, `m_targetFrameId`, `m_baseFrameId`, `m_baseFootprintId`, `m_globalFrameId`[source/src/humanoid_navigation/humanoid_localization/include/humanoid_localization/HumanoidLocalization.h:L145-L149](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/humanoid_localization/include/humanoid_localization/HumanoidLocalization.h#L145-L149) but their semantic mapping is implementation-dependent. |
| Ground-plane filtering | Methods `filterGroundPlane` and flags `m_groundFilterPointCloud` exist[source/src/humanoid_navigation/humanoid_localization/include/humanoid_localization/HumanoidLocalization.h:L88-L90](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/humanoid_localization/include/humanoid_localization/HumanoidLocalization.h#L88-L90)[source/src/humanoid_navigation/humanoid_localization/include/humanoid_localization/HumanoidLocalization.h:L187-L191](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/humanoid_localization/include/humanoid_localization/HumanoidLocalization.h#L187-L191), but threshold semantics are opaque without reading the source. |
| Cross-robot calibration transfer | Calibration values in the test config are all zeros; these must not be transferred to Chronus or Orion robots. Robot-specific offsets must be determined independently. |
| SBPL integration | The SBPL path planning extension is conditionally compiled[source/src/humanoid_navigation/humanoid_localization/CMakeLists.txt:L50-L56](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/humanoid_navigation/humanoid_localization/CMakeLists.txt#L50-L56); its impact on localization behavior is unknown. |

---

## Sources

| Path | Lines | Purpose |
|---|---|---|
| `source/src/humanoid_navigation/humanoid_localization/CMakeLists.txt` | L1-L254 | Build targets, dependencies, optional SBPL |
| `source/src/humanoid_navigation/humanoid_localization/config/localization_conf_motion_test.yaml` | L1-L26 | Test configuration (zero-noise fixture) |
| `source/src/humanoid_navigation/humanoid_localization/launch/nao_localization_laser.launch.py` | L1-L35 | ROS 2 launch entry point |
| `source/src/humanoid_navigation/humanoid_localization/include/dynamicEDT3D/dynamicEDT3D.h` | L1-L142 | Incremental 3D distance transform (BSD-licensed) |
| `source/src/humanoid_navigation/humanoid_localization/include/humanoid_localization/HumanoidLocalization.h` | L1-L208 | Main localization class interface |
| `source/src/humanoid_navigation/humanoid_localization/src/localization_node.cpp` | L1-L25 | Node entry point |
