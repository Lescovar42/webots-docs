> Shared file-content analysis, using the Alphonse snapshot. Robot-specific runtime conditions require separate review.

# Shared YOLO build, interface and launch contracts

This replacement covers four source files whose complete contents match across the pinned Alphonse, Chronus and Orion snapshots. Alphonse is the canonical citation target. The matching files establish a common build and entry-point contract; they do not establish identical configuration, inference results or robot behavior. This card was reviewed from numbered source ranges after the original run incorrectly included a branch-specific YAML file.

## Build and installed artifacts

`op3_yolo_vision` selects C++17 when a standard has not already been supplied. It declares ROS dependencies on `rclcpp`, image and geometry messages, `soccer_msgs`, and `ament_index_cpp`, alongside OpenCV. OpenVINO is first located quietly, with additional candidate CMake locations tried before a required lookup. This describes dependency discovery, not a successful build on this workstation. [source/src/op3_yolo_vision/CMakeLists.txt:L1-L34](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_yolo_vision/CMakeLists.txt#L1-L34)

The executable is named `yolo_detector` and combines `yolo_detector.cpp` with `yolo_detector_node.cpp`. Its link dependencies include OpenCV and `openvino::runtime`. Installation rules place the executable under the package's `lib` directory and install headers, launch files, configuration and model directories. An install rule does not prove that usable model weights exist or load successfully. [source/src/op3_yolo_vision/CMakeLists.txt:L41-L78](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_yolo_vision/CMakeLists.txt#L41-L78)

## Launch and process entry point

The launch description resolves the package share directory and declares a `params_file` argument defaulting to `config/yolo.yaml`. It launches package `op3_yolo_vision`, executable and node name `yolo_detector`, with that selected parameter file. [source/src/op3_yolo_vision/launch/yolo.launch.py:L9-L26](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_yolo_vision/launch/yolo.launch.py#L9-L26)

The executable initializes ROS, creates a two-thread `MultiThreadedExecutor`, constructs a `YoloDetector`, adds it to the executor and spins. Shutdown follows executor completion. This establishes the entry-point threading choice, not callback concurrency or throughput measurements. [source/src/op3_yolo_vision/src/yolo_detector_node.cpp:L18-L31](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_yolo_vision/src/yolo_detector_node.cpp#L18-L31)

## Declared detector interface

`YoloDetector` inherits from `rclcpp::Node`. Its header declares an image callback, model-loading and output-decoding helpers, and detection records containing a rectangle, class ID and score. These are declarations; the processing algorithm is implemented elsewhere. [source/src/op3_yolo_vision/include/op3_yolo_vision/yolo_detector.hpp:L33-L61](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_yolo_vision/include/op3_yolo_vision/yolo_detector.hpp#L33-L61)

The declared state includes topic and model-path strings, a device string, input size and suppression thresholds, debug and precision flags, an OpenVINO model/compiled-model/inference-request set, and an image subscription. Publisher types are image, `soccer_msgs::BoundingBoxes` and `geometry_msgs::PointStamped`. Literal topic names, parameter defaults and actual device selection cannot be inferred from these member names alone. [source/src/op3_yolo_vision/include/op3_yolo_vision/yolo_detector.hpp:L63-L89](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/op3_yolo_vision/include/op3_yolo_vision/yolo_detector.hpp#L63-L89)

## Branch-specific boundary and next checks

The failed draft read `config/yolo.yaml`, which the cross-branch guard identified as differing. Its topic values, class thresholds and device choices are intentionally excluded from this shared card. Consult each robot's vision-difference investigation and inspect its own configuration before deployment.

The main detector implementation, model contents, camera wiring, class definitions and runtime performance remain outside this reviewed scope. No Docker build, ROS launch, inference benchmark, simulator or physical-robot command was executed. Matching launch and header files must not be used to copy settings between robots.
