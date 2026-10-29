> Shared file-content analysis, using the Alphonse snapshot. Robot-specific runtime conditions require separate review.

# Shared ball and face detection entry points

This card reviews matching build, launch, parameter and interface files in the pinned snapshots. It describes source contracts, not proven detector accuracy or a camera calibration suitable for all three robots.

## Face-tracking build

The `face_detection` CMake file uses `ament_cmake`, declares ROS/image/OpenCV dependencies, and builds `face_tracking` from `src/face_tracking.cpp`. It installs that executable, headers and launch/include resources. The link list still mentions `${catkin_LIBRARIES}` alongside OpenCV; this is an observed build-file detail, not proof of a failed or successful build. The implementation and actual cascade assets were not reviewed here. [source/src/face_detection/CMakeLists.txt:L1-L52](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/face_detection/CMakeLists.txt#L1-L52)

## USB-camera ball-detector launch

`ball_detector_from_usb_cam.launch.py` constructs a `usb_cam_node_exe` node using package configuration `camera_param.yaml`, then creates `ball_detector_node` with `ball_detector_params.yaml`. Camera settings themselves are outside this card's reviewed sources. [source/src/ROBOTIS-OP3-Demo/op3_ball_detector/launch/ball_detector_from_usb_cam.launch.py:L6-L24](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_ball_detector/launch/ball_detector_from_usb_cam.launch.py#L6-L24)

The detector's image input is remapped to `/usb_cam_node/image_raw/compressed`, and camera-info input to `/usb_cam_node/camera_info`. Parameters include both a `yaml_path` entry and the detector YAML file. The two nodes are added to the returned launch description. These declarations do not verify the live publisher names, transport compatibility or a successful launch. [source/src/ROBOTIS-OP3-Demo/op3_ball_detector/launch/ball_detector_from_usb_cam.launch.py:L25-L37](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_ball_detector/launch/ball_detector_from_usb_cam.launch.py#L25-L37)

## Declared processing interface and settings

`BallDetector` derives from `rclcpp::Node`. Its header declares image-availability checks, processing, image and circle publication, a compressed-image callback, a camera-info callback, enable/parameter callbacks and parameter services. The header establishes intended interface types; it does not show the actual callback bindings or full algorithm. [source/src/ROBOTIS-OP3-Demo/op3_ball_detector/include/op3_ball_detector/ball_detector.h:L49-L96](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_ball_detector/include/op3_ball_detector/ball_detector.h#L49-L96)

The reviewed YAML uses a wildcard ROS parameter namespace. It contains Gaussian blur, Canny/Hough and radius settings, a primary HSV filter, a second filter enabled by default, ellipse size and debug settings. Matching YAML contents are not evidence that those thresholds are suitable for each robot's camera, optics or lighting. [source/src/ROBOTIS-OP3-Demo/op3_ball_detector/config/ball_detector_params.yaml:L1-L28](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Demo/op3_ball_detector/config/ball_detector_params.yaml#L1-L28)

## Verification still needed

Camera calibration and resolution, actual topic publishers, detector implementation and runtime quality remain untested. Treat the launch file as an entry-point map. The previous path-only citation now has concrete reviewed line ranges; no detector or simulator was launched and no configuration was copied between robots.
