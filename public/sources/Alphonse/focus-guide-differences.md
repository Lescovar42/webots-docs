# Alphonse settings, calibration boundaries and review gaps

This guide records selected values and configuration ownership in the pinned Alphonse snapshot. It does not prescribe new tuning values or establish successful calibration. References that previously pointed to unread or path-only sources have been replaced with exact reviewed ranges.

## Distinct configuration layers

`offset.yaml` contains two separate maps, `offset` and `init_pose_for_offset_tuner`, with zero values in the reviewed file. Zero entries are file contents, not evidence of physical alignment, a calibrated robot or an appropriate offset-tuner pose. Do not conflate these maps with walking-preset pose fields. [source/src/ROBOTIS-OP3/op3_manager/config/offset.yaml:L1-L42](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/config/offset.yaml#L1-L42)

The walking YAML has a long restoration/history note followed by actual parameter values. Among the declared values are `x_offset=-0.02`, `period_time=800`, `dsp_ratio=0.58`, `soft_start_time=2000`, and `balance_enable=false`. These are snapshot observations, not recommended settings for another robot or proof of the currently loaded runtime state. [source/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml:L58-L85](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml#L58-L85)

Comments distinguish file units/names from Studio's runtime representation, describe reading at boot, and warn that saving can rewrite the file and drop comments. The claimed loader conversions and historical restoration behavior require implementation verification; this review inspected the YAML and its comments, not the full walking module. Use the [Studio review notes](focus-difference-other.md) when interpreting display deltas versus native values. [source/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml:L1-L57](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_walking_module/config/param.yaml#L1-L57)

## Selected paths, action file and serial roles

The manager launch resolves offset, robot-description and Dynamixel-init files from package shares, selects `ALPHONSE.bin`, and declares separate servo-bus and OpenCR device arguments with distinct by-id defaults. The README describes the split as an Alphonse-specific workaround. Actual serial identities and board condition remain hardware checks, not shared configuration. [source/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py:L13-L39](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py#L13-L39) [source/README.md:L62-L66](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/README.md#L62-L66)

`boot_init_page` is declared with default 2 and explicit integer conversion; the comments describe positive, zero and negative modes. This is the source configuration contract, not a verified page-content or physical-pose guarantee. The same launch parameter dictionary sets `angle_unit`, `gazebo` and configuration paths. Consult the [architecture guide](focus-guide-architecture.md) for the unresolved launch/node simulation-name mismatch. [source/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py:L41-L78](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py#L41-L78)

## Review before operation

1. Confirm the intended robot branch and installed package paths; source-tree values alone do not prove the running installation uses them.
2. Check native parameter names and units before moving a value between YAML, UI and ROS interfaces.
3. Verify the robot's own action file, offsets, serial mapping and effective simulation setting. Do not substitute another robot's data because the code structure looks similar.
4. Treat historical comments and GUI labels as evidence to investigate, not measurements of the present robot.

The README describes container-based workspace lookup and warns about host/container setup differences. Those troubleshooting statements were not reproduced here. [source/README.md:L102-L119](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/README.md#L102-L119)

No configuration, calibration, action binary or hardware state was changed; no robot command or motion was executed.
