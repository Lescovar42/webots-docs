> Shared file-content analysis, using the Alphonse snapshot. Robot-specific runtime conditions require separate review.

# Shared action-module contracts and base-state initialization

The reviewed build file, action-format header, action API and base-state constructor match across the three pinned snapshots. This is an interface and data-layout investigation. It does not establish that action binaries, calibration or physical motions are interchangeable.

## Build and action interface

`op3_action_module` builds a shared library from `src/action_module.cpp`. Its CMake dependencies include ROS, Dynamixel SDK, controller/action messages and framework/device packages. Installation exports the library and headers and installs the `data` directory. This is not evidence that a particular action file loads successfully. [source/src/ROBOTIS-OP3/op3_action_module/CMakeLists.txt:L1-L50](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_action_module/CMakeLists.txt#L1-L50)

`ActionModule` derives from `MotionModule`, `Singleton<ActionModule>` and `rclcpp::Node`. It declares initialization/processing, file creation/loading, starts by page number or name, stop/brake/status functions, and page load/save/reset operations. The sampled private declarations include checksum helpers and action callbacks. Runtime callback wiring, error handling and exact playback behavior require the implementation. [source/src/ROBOTIS-OP3/op3_action_module/include/op3_action_module/action_module.h:L41-L106](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_action_module/include/op3_action_module/action_module.h#L41-L106)

## Declared action-file structure

The format header declares limits of 256 pages, seven steps, a 13-character name limit and 31 joint slots, along with speed/time schedule constants and invalid/torque-off bit masks. These are format constants; 31 slots must not be described as proof of 31 physical robot joints. [source/src/ROBOTIS-OP3/op3_action_module/include/op3_action_module/action_file_define.h:L27-L36](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_action_module/include/op3_action_module/action_file_define.h#L27-L36)

The declared `PageHeader` contains name, repetition/schedule, step count, speed/acceleration, next/exit links, checksum and gain fields. A `Step` contains joint-position storage, pause and time fields; a `Page` contains a header and the step array. Comments describe intended byte sizes, but this review did not compile a layout/ABI test or validate any binary action data. [source/src/ROBOTIS-OP3/op3_action_module/include/op3_action_module/action_file_define.h:L38-L69](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_action_module/include/op3_action_module/action_file_define.h#L38-L69)

## Base-state defaults

`BaseModuleState` starts with `is_moving_` false, counters reset, a 1.0 movement-time value and a 0.008 sample-time value. It allocates zeroed trajectory, pose and via-point matrices using `MAX_JOINT_ID + 1`. That symbol's numeric definition was not reviewed here, so no numeric joint-ID limit is inferred. Constructor defaults also do not establish the controller's measured operating rate. [source/src/ROBOTIS-OP3/op3_base_module/src/base_module_state.cpp:L24-L45](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3/op3_base_module/src/base_module_state.cpp#L24-L45)

## Open questions

Actual action-page meanings, loaded binary selection, offsets, torque state and safe movement remain robot-specific. Check the manager's selected action file and the appropriate settings guide before interpreting an action number. This card does not supply an action-execution command.

No action file was modified, no build was performed, and no motion or hardware API was invoked. The earlier citation to an unread kinematics-definition header has been replaced with the narrower constructor evidence above.
