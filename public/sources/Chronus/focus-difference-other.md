# Chronus Studio, teleoperation and GUI review notes

This representative review covers Chronus's Studio README, selected joystick YAML, GUI initialization and controller declarations. The former claim supported only by an unread controller implementation has been removed. No complete cross-robot behavioral equivalence or operating test is claimed.

## Studio documentation

The README describes a React/Tailwind/ROS 2 dashboard, telemetry, vision, walking tuning, action editing and logs. Its feature list includes emergency-stop and initial-pose controls, but a README feature claim is not verification that an emergency stop works or prevents injury. The sampled startup section lists build/dependency steps; they were not executed here. [source/src/bascorro_studio/README.md:L1-L72](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/bascorro_studio/README.md#L1-L72)

## Joystick configuration

The YAML declares axis mappings, a deadman button, initial-pose long press, and requirements to release the deadman/stop before initial pose. Its `stop_button` is `-1`, with a comment saying a valid index is required to enable that binding. These values describe configuration intent, not verified input handling or a tested emergency-stop path. [source/src/op3_joy_teleop/config/op3_joy_teleop.yaml:L1-L11](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/op3_joy_teleop/config/op3_joy_teleop.yaml#L1-L11)

The same sampled range declares command limits, dead zone, publish rate, `dry_run: false`, input timeout and command/status topic names. It also contains acceleration/low-pass settings, gear scales, heading hold, turbo and turning options. Do not interpret the first three limits alone as the final physical motion envelope; the implementation and scaling combinations were not reviewed. [source/src/op3_joy_teleop/config/op3_joy_teleop.yaml:L13-L47](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/op3_joy_teleop/config/op3_joy_teleop.yaml#L13-L47)

## GUI and controller interface

The GUI creates publishers for joint-module selection, a module preset and action page numbers, plus status/module subscriptions and a present-module service client. It initializes demo/preview helpers and resolves the GUI YAML. This identifies source bindings only; it does not prove subscriber availability or action success. [source/src/ROBOTIS-OP3-Tools/op3_gui_demo/src/qnode.cpp:L57-L81](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3-Tools/op3_gui_demo/src/qnode.cpp#L57-L81)

The controller header declares module and sensor collections, sync/bulk-write/read structures, mode/thread state, and APIs for initialization, processing, modules, timers, offsets and ROS callbacks/services. The header does not establish how those operations are implemented or scheduled. [source/src/ROBOTIS-Framework/robotis_controller/include/robotis_controller/robotis_controller.h:L60-L105](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-Framework/robotis_controller/include/robotis_controller/robotis_controller.h#L60-L105) [source/src/ROBOTIS-Framework/robotis_controller/include/robotis_controller/robotis_controller.h:L124-L151](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-Framework/robotis_controller/include/robotis_controller/robotis_controller.h#L124-L151)

## Checks still required

Verify actual gamepad indexes, deadman/stop behavior, scale interactions and runtime topic connectivity on Chronus before operation. Studio feature claims, controller timing and motor response remain untested. No keyboard/gamepad input, robot command, dependency installer or configuration change was executed. Use the [operation guide](focus-guide-operation.md), [architecture guide](focus-guide-architecture.md) and [hash comparison](../BRANCH-COMPARISON.md) for navigation.
