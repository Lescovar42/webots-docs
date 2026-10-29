> Shared file-content analysis, using the Alphonse snapshot. Robot-specific runtime conditions require separate review.

# Shared Code: Webots & Simulation Integration

**Scope:** Canonical snapshot `ALPHONSE_NEW_V2`, commit `adacde8f6e01e6439d170fb6bce025acc051bfa3`. This card covers the shared simulation integration layer connecting the OP3 robot platform to two ROS 2-compatible physics engines: **Webots** (via `op3_webots_ros2`) and **Gazebo Sim** (via `op3_gazebo_ros2`). The content of the referenced source files is identical across the Alphonse, Chronus, and Orion snapshots by SHA-256; however, runtime equivalence has not been established. This investigation is representative, not exhaustive. Only the four assigned source paths were inspected.

---

## 1. Webots Integration (`op3_webots_ros2`)

### Package Definition

The `op3_webots_ros2` package is an `ament_cmake` ROS 2 package declaring dependencies on `rclcpp`, `geometry_msgs`, `sensor_msgs`, `std_msgs`, `nav_msgs`, and the external `webots_ros2_driver` bridge [source/src/ROBOTIS-OP3-Simulations/op3_webots_ros2/package.xml:L1-L24](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Simulations/op3_webots_ros2/package.xml#L1-L24). It is licensed under Apache-2.0 and authored by Jay and Zerom.

### Launch Contract

The launch file `robot_launch.py` produces a ROS 2 `LaunchDescription` with three active actions and one conditional action:

| Action | Purpose | Parameters |
|---|---|---|
| `WebotsLauncher` | Starts the Webots simulator | World file: `robotis_op3_extern.wbt` [source/src/ROBOTIS-OP3-Simulations/op3_webots_ros2/launch/robot_launch.py:L33-L35](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Simulations/op3_webots_ros2/launch/robot_launch.py#L33-L35) |
| `op3_extern_controller` | Webots controller node (ROS 2 bridge inside the sim) | `gain_file_path` → `op3_pid_gain_default.yaml` [source/src/ROBOTIS-OP3-Simulations/op3_webots_ros2/launch/robot_launch.py:L38-L43](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Simulations/op3_webots_ros2/launch/robot_launch.py#L38-L43) |
| `op3_gc_bridge` | Game Controller (RoboCup Soccer) network bridge | `gc_host: 127.0.0.1`, `control_port: 3838`, `status_port: 3939`, `team_number: 1`, `player_number: 1`, `rx_period_ms: 20`, `tx_period_ms: 500` [source/src/ROBOTIS-OP3-Simulations/op3_webots_ros2/launch/robot_launch.py:L44-L57](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Simulations/op3_webots_ros2/launch/robot_launch.py#L44-L57) |
| `robot_state_publisher` | Publishes TF tree from URDF | Remaps `/joint_states` → `/robotis_op3/joint_states`; enabled by launch arg `enable_robot_state_publisher` (default `true`) [source/src/ROBOTIS-OP3-Simulations/op3_webots_ros2/launch/robot_launch.py:L58-L64](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Simulations/op3_webots_ros2/launch/robot_launch.py#L58-L64) |

The URDF description is resolved through `op3_description` package and processed via `xacro` at launch time [source/src/ROBOTIS-OP3-Simulations/op3_webots_ros2/launch/robot_launch.py:L22-L24](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Simulations/op3_webots_ros2/launch/robot_launch.py#L22-L24). A commented-out alternative path (lines 67-76) shows a previous pattern using an `OnProcessExit` event handler to shut down the launch when Webots exits, but this is not active.

### RoboCup Scene Assets

The proto file `RoboCupBackground.proto` defines a VRML-SIM `Background` node with a JavaScript template layer. It accepts a `texture` field (one of seven preset stadium/skybox textures), a `luminosity` value, and a `skybox` boolean [source/src/ROBOTIS-OP3-Simulations/op3_webots_ros2/protos/robocup_field/RoboCupBackground.proto:L3-L9](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Simulations/op3_webots_ros2/protos/robocup_field/RoboCupBackground.proto#L3-L9). Texture image files are resolved as `{texture}_{side}.png` from within a `backgrounds/` subdirectory [source/src/ROBOTIS-OP3-Simulations/op3_webots_ros2/protos/robocup_field/RoboCupBackground.proto:L25-L44](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Simulations/op3_webots_ros2/protos/robocup_field/RoboCupBackground.proto#L25-L44). This proto is a simulation-only visual asset; it has no effect on physical robot behavior.

---

## 2. Gazebo Sim Integration (`op3_gazebo_ros2`)

### Launch Contract

The file `robot_sim.launch.py` provides a parallel simulation path using Gazebo Sim (the ROS 2 `ros_gz` bridge). It declares:

1. **Gazebo Sim** launched via `gz_sim.launch.py` with a configurable `world` argument (default `empty`) [source/src/ROBOTIS-OP3-Simulations/op3_gazebo_ros2/launch/robot_sim.launch.py:L36-L38](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Simulations/op3_gazebo_ros2/launch/robot_sim.launch.py#L36-L38), [source/src/ROBOTIS-OP3-Simulations/op3_gazebo_ros2/launch/robot_sim.launch.py:L41-L51](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Simulations/op3_gazebo_ros2/launch/robot_sim.launch.py#L41-L51).
2. **robot_state_publisher** processing the same `robotis_op3.urdf.xacro` file with `use_sim:=true` [source/src/ROBOTIS-OP3-Simulations/op3_gazebo_ros2/launch/robot_sim.launch.py:L53-L54](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Simulations/op3_gazebo_ros2/launch/robot_sim.launch.py#L53-L54), [source/src/ROBOTIS-OP3-Simulations/op3_gazebo_ros2/launch/robot_sim.launch.py:L58-L63](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Simulations/op3_gazebo_ros2/launch/robot_sim.launch.py#L58-L63).
3. **Entity spawn** at position `(0.0, 0.0, 0.285)` with no rotation, named `robotis_op3` [source/src/ROBOTIS-OP3-Simulations/op3_gazebo_ros2/launch/robot_sim.launch.py:L65-L78](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Simulations/op3_gazebo_ros2/launch/robot_sim.launch.py#L65-L78).
4. **rf_gz_bridge** for ROS↔Gazebo joint topic translation, configured via `op3_joint_list.yaml` [source/src/ROBOTIS-OP3-Simulations/op3_gazebo_ros2/launch/robot_sim.launch.py:L80-L88](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Simulations/op3_gazebo_ros2/launch/robot_sim.launch.py#L80-L88).
5. **ros_gz_bridge** parameter bridge driven by `bridge_parameters.yaml` [source/src/ROBOTIS-OP3-Simulations/op3_gazebo_ros2/launch/robot_sim.launch.py:L102-L111](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Simulations/op3_gazebo_ros2/launch/robot_sim.launch.py#L102-L111).
6. **Controller loading** chained via `OnProcessExit` event handlers: `joint_state_broadcaster` loads after entity spawn, then `robotis_op3_position` loads after joint broadcaster [source/src/ROBOTIS-OP3-Simulations/op3_gazebo_ros2/launch/robot_sim.launch.py:L90-L100](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Simulations/op3_gazebo_ros2/launch/robot_sim.launch.py#L90-L100), [source/src/ROBOTIS-OP3-Simulations/op3_gazebo_ros2/launch/robot_sim.launch.py:L122-L134](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Simulations/op3_gazebo_ros2/launch/robot_sim.launch.py#L122-L134).

A commented-out `rviz2` node (lines 112-120) suggests visualization support was planned but is not active.

---

## 3. Untested Operation Notes

The following commands appear in source but were **not executed**:

- `ros2 control load_controller --set-state active joint_state_broadcaster` [source/src/ROBOTIS-OP3-Simulations/op3_gazebo_ros2/launch/robot_sim.launch.py:L90-L93](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Simulations/op3_gazebo_ros2/launch/robot_sim.launch.py#L90-L93)
- `ros2 control load_controller --set-state active robotis_op3_position` [source/src/ROBOTIS-OP3-Simulations/op3_gazebo_ros2/launch/robot_sim.launch.py:L96-L99](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Simulations/op3_gazebo_ros2/launch/robot_sim.launch.py#L96-L99)
- `ros2 launch op3_webots_ros2 robot_launch.py` (implied by the launch file's existence but not invoked)

No build, install, or runtime verification was performed. The Gazebo `parameter_bridge` process and the Webots `WebotsLauncher` external dependency are both assumed to function but remain untested.

---

## 4. Uncertainties and Conflicts

| Area | Observation |
|---|---|
| **PID gains** | The Webots launch references `op3_pid_gain_default.yaml` [source/src/ROBOTIS-OP3-Simulations/op3_webots_ros2/launch/robot_launch.py:L21](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Simulations/op3_webots_ros2/launch/robot_launch.py#L21) but this file was not inspected. Gain values cannot be stated. |
| **Shared URDF** | Both launch files process the same `robotis_op3.urdf.xacro` but were not inspected. Joint names, link topology, and collision geometry are assumed identical but unverified. |
| **Gazebo spawn height** | The Gazebo path spawns the robot at `z=0.285` meters [source/src/ROBOTIS-OP3-Simulations/op3_gazebo_ros2/launch/robot_sim.launch.py:L70](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Simulations/op3_gazebo_ros2/launch/robot_sim.launch.py#L70). This offset is specific to the Gazebo simulation environment and must not be transferred to Webots or physical robot operation. |
| **GC bridge defaults** | The Webots GC bridge binds to loopback `127.0.0.1` [source/src/ROBOTIS-OP3-Simulations/op3_webots_ros2/launch/robot_launch.py:L49](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Simulations/op3_webots_ros2/launch/robot_launch.py#L49), which implies local-only RoboCup Game Controller connectivity. Remote deployment would require parameter override. |
| **Webots world** | The primary world file `robotis_op3_extern.wbt` [source/src/ROBOTIS-OP3-Simulations/op3_webots_ros2/launch/robot_launch.py:L34](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Simulations/op3_webots_ros2/launch/robot_launch.py#L34) was not inspected. Scene contents, sensor models, and physics parameters are unknown. |
| **Inactive code** | Commented-out blocks in both launch files (Webots exit handler, Gazebo rviz) represent design intent that is not active and should not be treated as deployed behavior. |

---

## 5. Sources

| File | Path |
|---|---|
| Webots launch | `source/src/ROBOTIS-OP3-Simulations/op3_webots_ros2/launch/robot_launch.py` (76 lines) |
| Webots package.xml | `source/src/ROBOTIS-OP3-Simulations/op3_webots_ros2/package.xml` (24 lines) |
| Gazebo launch | `source/src/ROBOTIS-OP3-Simulations/op3_gazebo_ros2/launch/robot_sim.launch.py` (143 lines) |
| RoboCup background proto | `source/src/ROBOTIS-OP3-Simulations/op3_webots_ros2/protos/robocup_field/RoboCupBackground.proto` (45 lines) |

No additional source files were followed. The files listed above were read in their entirety. The `op3_pid_gain_default.yaml`, `bridge_parameters.yaml`, URDF xacro, and world files are unexamined dependencies inferred from the inspected launch scripts.
