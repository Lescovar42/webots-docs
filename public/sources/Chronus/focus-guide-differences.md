# Chronus settings and calibration review boundaries

This guide reviews Chronus's offset map, walking YAML, manager launch function and README. It replaces claims based on unread robot-description, simulation and manager/walking implementations. Values below describe this pinned source snapshot, not a verified live robot or a tuning recommendation.

## Offset and walking data

The offset file contains zero-valued `offset` and `init_pose_for_offset_tuner` maps. These separate sections do not prove that the physical joints are aligned or that an offset-tuning pose has been validated. [source/src/ROBOTIS-OP3/op3_manager/config/offset.yaml:L1-L42](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_manager/config/offset.yaml#L1-L42)

The walking YAML declares, among other values, an x/y offset near −0.015/+0.015, `period_time=700`, a double-support ratio near 0.3, foot height near 0.05, balance gains and PID gain fields. Exact literals are available in the cited file. Their interpretation, unit conversion, loading time and interaction with other presets require the consumer implementation and runtime to be checked. The file alone does not establish a safe gait. [source/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml:L1-L22](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml#L1-L22)

## Manager and serial configuration

The launch function calls `ensure_ports()`, resolves manager offset/robot/init files, and supplies both `device_name` and `sub_controller_device_name` with `/dev/ttyOP3` defaults. It also supplies `angle_unit=30.0` and `gazebo`-named parameters. This review does not execute the launch or certify that those launch parameters map to the manager's actual simulation switch; that mismatch is documented in the [architecture guide](focus-guide-architecture.md). [source/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py:L165-L204](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py#L165-L204)

The README describes `/dev/ttyOP3` as a U2D2 udev symlink and reports stock OpenCR firmware serving the sub-controller on the servo bus. It distinguishes that setup from the OpenCR micro-USB debug port and lists rule-installation commands. These are the snapshot author's wiring and setup statements, not a port probe performed by this review. [source/README.md:L96-L111](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/README.md#L96-L111)

The README's container section directs users to the repository Docker helper, describes historical device-binding and terminal-lifetime failures, and says menu/compose definitions were unified. The relevant code and deployment need checking together; documentation alone does not prove that every current container uses that definition. [source/README.md:L54-L94](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/README.md#L54-L94)

## Practical checks and unresolved scope

Confirm the selected Chronus installation and actual serial symlink target, then compare loaded parameters with the branch's own files. Keep joint offsets, walking pose parameters, UI display values and action-page data as separate layers. Do not import Alphonse's serial argument spelling, split-port profile or motion file merely because package names match.

The robot-description file, simulation launch, manager implementation and walking implementation were not used as evidence for this replacement. Read the [operation guide](focus-guide-operation.md) for the source-reviewed port-probing side effects and profile choices. Action contents, motor state, physical calibration and successful simulation still require runtime investigation.

No udev rule, YAML file, action binary or live parameter was changed. No build, launch, port access, torque or motion command was executed.
