> Shared file-content analysis, using the Alphonse snapshot. Robot-specific runtime conditions require separate review.

# Shared tool metadata and action-editor interface

This card covers the matching tools README, mirror-pair configuration and selected C++ action-editor declarations. It is not a complete investigation of Bascorro Studio, every tool listed in the README, or actual editor behavior on a robot.

## Tool-family navigation

The tools README lists action editing, camera settings, GUI demo, navigation, offset tuning and web-setting tool references. It also contains Kinetic/Melodic-era badges and upstream repository/manual links. These are navigation and historical metadata, not proof that every listed tool has been ported to ROS 2, installed or tested in this checkout. [source/src/ROBOTIS-OP3-Tools/README.md:L1-L40](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Tools/README.md#L1-L40)

## Editor declarations

`ActionEditor` inherits from `rclcpp::Node`. Its header declares left-to-right, right-to-left and switching mirror command types, plus upper/lower/all-body targets. Initialization takes robot, initialization and offset file paths along with a simulation-mode boolean. These signatures must not be treated as a validated launch interface or evidence of safe simulation selection. [source/src/ROBOTIS-OP3-Tools/op3_action_editor/include/op3_action_editor/action_editor.h:L44-L74](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Tools/op3_action_editor/include/op3_action_editor/action_editor.h#L44-L74)

The sampled interface includes terminal cursor/page drawing, value editing and torque toggling. Later declarations include a Webots step-execution helper, position/radian conversion helpers, mirror-data loading, and publishers for module selection, sound and Webots action/joint messages. Declarations alone do not prove which publishers are created, which topics they use or which operations are safe to call. [source/src/ROBOTIS-OP3-Tools/op3_action_editor/include/op3_action_editor/action_editor.h:L76-L93](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Tools/op3_action_editor/include/op3_action_editor/action_editor.h#L76-L93) [source/src/ROBOTIS-OP3-Tools/op3_action_editor/include/op3_action_editor/action_editor.h:L125-L155](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Tools/op3_action_editor/include/op3_action_editor/action_editor.h#L125-L155)

## Mirror configuration

The YAML separates `upper_body` and `lower_body` and lists right/left ID pairs: upper-body pairs run 1:2 through 5:6; lower-body pairs run 7:8 through 17:18. This is the file's mapping, not proof of the actual joint layout or sign conventions on a particular robot. The conversion and loading implementations were not reviewed in this card. [source/src/ROBOTIS-OP3-Tools/op3_action_editor/config/config_mirror_joint.yaml:L1-L13](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-OP3-Tools/op3_action_editor/config/config_mirror_joint.yaml#L1-L13)

## Scope corrections and remaining work

The earlier draft attempted to cite an empty Python `__init__.py` as if it had a source line. That citation is removed. No Python-editor behavior is inferred from the marker file; useful implementation evidence here comes from the C++ interface and the YAML.

Studio backend startup and implementation details, executable discovery, terminal handling, mirror conversion, motion-file contents and hardware behavior remain separate investigations. In particular, the presence of Webots-related member names does not establish an operational simulator connection. No tool, torque operation, mirror transformation or robot command was executed.
