# Chronus operation entry points and troubleshooting

This is a source-reviewed navigation guide for the pinned Chronus launcher. It does not certify a running stack or safe robot motion. The earlier shortened `scripts/profiles.sh` citation is corrected to the actual `scripts/op3_tmux/lib/profiles.sh` path.

## Launcher structure and profiles

`main.sh` enforces/re-executes Bash, enables strict shell options, sources its library files, and defines a main function that calls the dispatcher. Reviewing this loader does not review every sourced command handler. [source/scripts/op3_tmux/main.sh:L1-L41](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/scripts/op3_tmux/main.sh#L1-L41)

The `webots` profile defines a Webots launch and simulation-manager command. The `real_robot` profile defines a bringup-with-camera manager command and different delay/stagger/domain defaults. Both profiles define numerous other command strings; their definition does not establish that every pane runs or that each referenced launch file works. [source/scripts/op3_tmux/lib/profiles.sh:L1-L40](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/scripts/op3_tmux/lib/profiles.sh#L1-L40)

The profile function selects `motion_4095_CHRONUS.bin` for its action seed/path unless environment overrides are supplied, then applies command and timing overrides. Verify which profile and overrides are actually active. A default path is not proof of the contents or safety of the selected motion file. [source/scripts/op3_tmux/lib/profiles.sh:L42-L67](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/scripts/op3_tmux/lib/profiles.sh#L42-L67)

## Environment and preference checks

The health helper checks for tmux and may offer an interactive package installation. It also chooses a preference-file path and can write shell preferences. It contains ROS package lookup and Webots-binary checks, plus logic to align the setup-script extension and shell runner. These helpers have side effects or environment dependencies; they are not all read-only health queries. None was executed here. [source/scripts/op3_tmux/lib/health.sh:L1-L68](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/scripts/op3_tmux/lib/health.sh#L1-L68) [source/scripts/op3_tmux/lib/health.sh:L134-L163](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/scripts/op3_tmux/lib/health.sh#L134-L163) [source/scripts/op3_tmux/lib/health.sh:L209-L252](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/scripts/op3_tmux/lib/health.sh#L209-L252)

For a missing package, inspect the effective `SETUP` file, shell runner and package lookup result together rather than assuming a successful `source` established the correct workspace. For a missing Webots binary, the sampled helper checks the configured path and executable names; it does not install or validate Webots itself. [source/scripts/op3_tmux/lib/health.sh:L134-L163](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/scripts/op3_tmux/lib/health.sh#L134-L163)

## Serial startup can modify device links

`ensure_ports()` gathers openable USB serial ports and asks which answer servo/sub-controller probes. Its `point` helper can remove an existing symlink and create a new one; it leaves a real device node alone and logs errors. A manager launch is therefore not a harmless preview of configuration. No probe or symlink change was performed in this review. [source/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py:L97-L145](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py#L97-L145)

The remaining branches report missing servo/sub-controller responses and differing-port situations. `generate_launch_description()` calls this helper before creating the manager node, with both serial defaults named `/dev/ttyOP3` in the reviewed function. Actual firmware, permissions and bus ownership must be established on Chronus. [source/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py:L147-L164](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py#L147-L164) [source/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py:L165-L196](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/src/ROBOTIS-OP3/op3_manager/launch/op3_manager.launch.py#L165-L196)

## Operating checklist

Confirm branch, container/workspace environment, selected profile, action-file override and actual serial ownership before invoking any robot-stack command. Consult the [settings guide](focus-guide-differences.md) and [architecture guide](focus-guide-architecture.md) for calibration boundaries and the unresolved simulation parameter-name mismatch. No startup, package installation, port probe, device-link rewrite or robot action was executed here.
