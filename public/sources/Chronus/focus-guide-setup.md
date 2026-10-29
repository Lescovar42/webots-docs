# Chronus Guide — Setup and Prerequisites

> **Scope:** Practical steps for preparing a host machine, building the Docker image, launching the container, and performing first-time health checks for the Chronus robot on branch `CHRONUS_NEW` (commit `54998e7c56e5b2cce4c1c533758c7d2f2cf7698b`).  
> **All commands below are untested suggestions** sourced from this repository. They must be verified on hardware before trust.

---

## 1 Overview

Chronus is a ROS 2 Humble-based robot stack running inside a single privileged Docker container that mounts the entire `/dev` namespace from the host. The workspace contains the OP3 firmware interface, walking/balance modules, YOLO-based ball detection, and Webots simulation. The canonical container lifecycle is managed exclusively by `scripts/op3_docker.sh`; other entry points (`script.sh` menu, `docker-compose.yml`) delegate to it [source/README.md:L62-L77](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/README.md#L62-L77).

### Shared reference cards

| Topic | Link |
|---|---|
| Workspace structure | [../Shared/focus-shared-workspace.md](../Shared/focus-shared-workspace.md) |
| Framework & device interfaces | [../Shared/focus-shared-framework.md](../Shared/focus-shared-framework.md) |
| ROS messages | [../Shared/focus-shared-messages.md](../Shared/focus-shared-messages.md) |
| Manager & hardware bringup | [../Shared/focus-shared-manager.md](../Shared/focus-shared-manager.md) |
| Webots simulation | [../Shared/focus-shared-webots.md](../Shared/focus-shared-webots.md) |
| Robot differences (Chronus vs Alphonse) | [focus-difference-setup.md](focus-difference-setup.md) |

---

## 2 Host Prerequisites

### 2.1 Hardware

| Component | Description | Evidence |
|---|---|---|
| U2D2 USB board (FTDI FT232H `0403:6014`) | Carries all DXL servo traffic, IDs 1–20 and sub-controller ID 200 | [source/README.md:L97-L102](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/README.md#L97-L102) |
| OpenCR board (micro-USB `0483:5740`) | Debug/flash console only; **does not** respond to DXL packets | [source/README.md:L101-L104](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/README.md#L101-L104) |
| USB joystick (optional) | For teleoperation | [source/Dockerfile:L75](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/Dockerfile#L75) `ros-humble-joy` |

The U2D2 board is mandatory. Without it, all 20 servos report "does NOT respond!!", which is a bus problem, not a servo fault [source/scripts/op3_docker.sh:L84-L88](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/scripts/op3_docker.sh#L84-L88).

### 2.2 udev rule (one-time host setup)

The robot expects `/dev/ttyOP3`, a udev symlink pointing to the U2D2 adapter. Install it on the host:

```bash
sudo cp scripts/99-op3-opencr.rules /etc/udev/rules.d/99-op3-opencr.rules
sudo udevadm control --reload-rules && sudo udevadm trigger
```

**Found in source but not executed:** [source/README.md:L105-L109](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/README.md#L105-L109). The `doctor` subcommand validates this rule at runtime [source/scripts/op3_docker.sh:L98-L132](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/scripts/op3_docker.sh#L98-L132).

### 2.3 Docker

Docker must be installed and the host user must have access to the Docker socket. The script detects this automatically [source/scripts/op3_docker.sh:L60-L63](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/scripts/op3_docker.sh#L60-L63).

---

## 3 Build the Docker Image

```bash
docker build -t op3-webots-ros2:humble .
```

Key build characteristics [source/Dockerfile:L25-L263](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/Dockerfile#L25-L263):

| Aspect | Detail |
|---|---|
| Base | `ros:humble-ros-base` (Ubuntu 22.04) |
| Webots | R2025a by default; disable with `--build-arg WITH_WEBOTS=0` |
| Vision stack | OpenCV 4.8.1 (built from source), OpenVINO 2025.4.0, PyTorch (CPU wheels), Ultralytics YOLO |
| Web tooling | Node.js 20.11.1, pnpm 9.15.4, `gum` 0.14.5, `ttyd` 1.7.7 |
| Workspace location | `/ros2_ws` inside the container; built with `--symlink-install` |
| Entrypoint | `/docker-entrypoint.sh` sources ROS Humble, workspace `install/`, and OpenVINO vars before exec |

The entrypoint has a known quirk: OpenVINO's `setupvars.sh` consumes positional parameters. The script stashes `$@` before sourcing and restores it before `exec` [source/docker-entrypoint.sh:L7-L39](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/docker-entrypoint.sh#L7-L39).

---

## 4 Container Lifecycle

### 4.1 Start

```bash
scripts/op3_docker.sh up
```

This is idempotent [source/scripts/op3_docker.sh:L305-L378](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/scripts/op3_docker.sh#L305-L378). The container runs detached (`sleep infinity`), uses `--init` (tini as PID 1), `--restart unless-stopped`, binds `/dev:/dev`, and mounts the workspace at `/ros2_ws`. It automatically runs the `doctor` health check after launch.

**Untested command** [source/README.md:L63](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/README.md#L63).

### 4.2 Open a shell

```bash
scripts/op3_docker.sh shell
```

This wraps `docker exec` through `/docker-entrypoint.sh`, ensuring ROS and workspace paths are available. You may call it multiple times [source/scripts/op3_docker.sh:L381-L389](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/scripts/op3_docker.sh#L381-L389). The `harden_container_shell` routine also injects auto-source into the container's `.bashrc` as a fallback [source/scripts/op3_docker.sh:L292-L303](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/scripts/op3_docker.sh#L292-L303).

### 4.3 Health check

```bash
scripts/op3_docker.sh doctor
```

Performs a seven-section diagnostic [source/scripts/op3_docker.sh:L81-L181](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/scripts/op3_docker.sh#L81-L181):

1. **Host USB devices** — checks for FTDI U2D2 and micro-USB OpenCR presence.
2. **udev symlink** — verifies the rule file content matches the repo and that `/dev/ttyOP3` points to `ttyUSB*` (not `ttyACM*`).
3. **USB stability** — counts kernel disconnect events in the last 30 minutes.
4. **OP3.robot port paths** — cross-references ports declared in the robot config file against `/dev`.
5. **Container device access** — inside-container test of port openability (only if running).
6. **Workspace integrity** — confirms `ros2` is on PATH and core packages are discoverable (only if running).
7. **ABI freshness** — ensures no artifact was built before the last `robotis_controller.h` change, which causes silent 100% CPU hangs in the action editor [source/scripts/op3_docker.sh:L242-L285](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/scripts/op3_docker.sh#L242-L285).

### 4.4 Stop

```bash
scripts/op3_docker.sh down
```

Removes the container. Unlike `docker stop`, this is compatible with the `--restart unless-stopped` policy — `down` counts as a deliberate stop and suppresses auto-restart [source/scripts/op3_docker.sh:L392-L396](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/scripts/op3_docker.sh#L392-L396).

---

## 5 Interactive Menu (Alternative Entry Point)

`script.sh` provides a `gum`-based terminal menu with choices for launch, build, health check, dependency install, ROS env tuning, and Docker build/run/stop [source/script.sh:L45-L364](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/script.sh#L45-L364). It delegates Docker operations to `scripts/op3_docker.sh` internally. This entry point requires `gum` on the host (auto-install prompt available).

---

## 6 Known Gaps and Uncertainties

| Area | Status | Detail |
|---|---|---|
| `docker-compose.yml` | **Needs review** | Exists in repo alongside `op3_docker.sh` but README says compose now delegates to the script; untested whether it works independently. |
| Non-Docker bare-metal build | **Pending** | README references an "OLD" path using `colcon build` directly on the host [source/README.md:L10-L35](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/README.md#L10-L35). Unexamined whether this still works. |
| `run/run_vision_and_webots.sh` | **Untested** | A newer launch script referenced in README [source/README.md:L37-L40](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/README.md#L37-L40). Path not located during this inspection. |
| `run_kill_all.sh` | **Needs review** | Listed in TODO as "masih belum nutup" (not closing properly) [source/README.md:L50](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/README.md#L50). |
| Webots reconnect after refresh | **Needs review** | README TODO notes webots disconnects on refresh [source/README.md:L51](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/README.md#L51). |
| Localization (UKF) | **Pending** | Marked TODO in README [source/README.md:L46-L47](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/README.md#L46-L47). |

---

## 7 Untested Operation Notes

The following commands are cited from source but **have not been executed** in this investigation:

- `sudo cp scripts/99-op3-opencr.rules /etc/udev/rules.d/99-op3-opencr.rules` [source/README.md:L106](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/README.md#L106)
- `sudo udevadm control --reload-rules && sudo udevadm trigger` [source/README.md:L107](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/README.md#L107)
- `docker build -t op3-webots-ros2:humble .` [source/README.md:L58](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/README.md#L58)
- `scripts/op3_docker.sh up` [source/README.md:L63](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/README.md#L63)
- `scripts/op3_docker.sh shell` [source/README.md:L64](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/README.md#L64)
- `scripts/op3_docker.sh doctor` [source/README.md:L65](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/README.md#L65)
- `scripts/op3_docker.sh down` [source/README.md:L66](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/README.md#L66)
- `colcon build --continue-on-error` [source/README.md:L14](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/README.md#L14)

---

## 8 Simulation vs Physical Notes

Webots simulation shares the same container images as physical robot operation. In simulation, the U2D2 board and `/dev/ttyOP3` symlink are irrelevant — simulated motor control goes through the Webots ROS 2 driver and its virtual controller [source/Dockerfile:L63](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/Dockerfile#L63). The `doctor` Section 2 warnings about missing hardware are expected and normal when running in simulation-only mode.

---

*This is a representative investigation of the setup path. Not all 896 eligible text files were examined (see FOCUSED-INDEX for deferred items). Commands marked untested must be verified before operational use.*
