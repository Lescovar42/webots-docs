> Shared file-content analysis, using the Alphonse snapshot. Robot-specific runtime conditions require separate review.

# Shared demo build, launch and action interfaces

This card describes matching source anchors in the three pinned robot snapshots. It covers the read/write demo build file, face-tracking launch XML, and selected `ActionDemo` declarations and implementation ranges. It does not establish identical soccer strategy, action-page numbering, motion data or complete demo wiring. The failed draft crossed that boundary by reading a differing `op_demo.h` base header.

## Read/write executable contract

The `op3_read_write_demo` build file uses `ament_cmake` and declares dependencies on `rclcpp`, `sensor_msgs`, `std_msgs` and `robotis_controller_msgs`. It builds an executable named `read_write` from `src/read_write.cpp`, installs it under the package's `lib` directory, and installs the launch directory under the package share directory. The reviewed file does not establish what the executable reads or writes at runtime; its implementation is outside this card. [source/src/ROBOTIS-OP3-Demo/op3_read_write_demo/CMakeLists.txt:L1-L35](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_read_write_demo/CMakeLists.txt#L1-L35)

## Face-tracking launch configuration

The XML declares five cascade-file arguments from the `face_detection` package, then passes them to its `face_tracking` executable. It assigns input `/usb_cam_node/image_raw/compressed`, output `/facerec/image_raw`, and the parameters `displayed_Image=0`, `publish=3` and `start_condition=false`. These are literal launch settings, not evidence that the camera topics, cascade assets or tracking behavior work on a particular robot. [source/src/ROBOTIS-OP3-Demo/op3_demo/launch/face_detection_op3.launch.xml:L1-L22](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_demo/launch/face_detection_op3.launch.xml#L1-L22)

## Action interface and initialization

`ActionDemo` derives from `OPDemo`. Its public interface includes enable/disable methods, `process`, node injection through `setNode`, and button/demo-command callbacks. Its protected interface declares playlist controls, action playback/status methods and module-selection helpers. A declaration alone does not prove that a callback or publisher is connected by a running node. [source/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/action_demo.h:L37-L94](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_demo/include/op3_demo/action_demo.h#L37-L94)

The constructor initializes playback state, starts disabled, selects the package's `list/action_script.yaml` and the playlist name `default`, then parses the script. Parameter-fetching, subscription creation and thread-launch examples in this inspected constructor are commented out. They must not be described as active wiring. [source/src/ROBOTIS-OP3-Demo/op3_demo/src/action/action_demo.cpp:L25-L52](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_demo/src/action/action_demo.cpp#L25-L52)

`setNode` stores a supplied ROS node pointer. Enabling the demo selects `action_module`, marks it enabled, calls `playAction(InitPose)` and starts the selected playlist. Disabling stops processing, clears the enabled flag and empties the playlist. `InitPose` is a symbol here; this card does not assign it a numeric page or certify its physical effect. [source/src/ROBOTIS-OP3-Demo/op3_demo/src/action/action_demo.cpp:L58-L84](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_demo/src/action/action_demo.cpp#L58-L84)

## Script data contract

`parseActionScript` loads YAML and logs/returns on a loading exception. It reads the `action_and_sound` mapping as integer action indexes to string sound paths, and optionally reads the `default` sequence into the playlist. This establishes the parser's expected structure; no actual playlist or sound asset was validated in this review. [source/src/ROBOTIS-OP3-Demo/op3_demo/src/action/action_demo.cpp:L206-L234](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_demo/src/action/action_demo.cpp#L206-L234)

## Branch-specific boundary and remaining work

The base header that supplies inherited demo definitions is not part of this shared proof. Neither its motion enumeration nor any numeric kick, recovery or initial-pose mapping is transferred between robots. Each robot's own base header, action files, manager setup and calibration must be reviewed together before operation.

The full processing state machine, callback routing, read/write node, sound playback and physical motion remain outside the inspected ranges. No demo executable, face tracker, ROS launch, action or robot command was run. Use this as a source-navigation card and consult the robot-specific guides for configuration context.
