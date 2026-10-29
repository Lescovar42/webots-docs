# Orion — Setup and Prerequisites Guide

> **Scope**: This guide documents the Docker-based build, container launch, health-check, and workspace initialization workflow for Orion on the target Jetson (arm64) platform. It draws on `scripts/op3_docker.sh`, `script.sh`, `docker-entrypoint.sh`, the `Dockerfile`, and `README.md`. All shell commands in this guide are **untested suggestions** derived from source inspection; they are offered as documentation, not verified operational instructions.

---

## 1 Hardware and Host Prerequisites

Orion runs on a **NVIDIA Jetson** board using the **arm64 (aarch64)** architecture. The following peripherals are expected on the host:

| Peripheral | USB ID | Required For | Note |
|---|---|---|---|
| FTDI FT232H adapter | `0403:6014` | Dynamixel servo bus (ID 1-20 + sub-controller 200) | Strictly required; without it all 20 joints report `does NOT respond!!` [source/README.md:L82-L84](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/README.md#L82-L84) |
| OpenCR micro-USB (optional) | `0483:5740` | Debug console only | Sub-controller ID 200 still routes through the TTL bus, not the OpenCR USB link [source/scripts/op3_docker.sh:L186-L191](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/scripts/op3_docker.sh#L186-L191) |
| V4L2 camera(s) (optional) | `/dev/video*` | Ball/YOLO vision nodes | Nodes remain silent without a camera; no crash [source/README.md:L196-L200](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/README.md#L196-L200) |

The DXL serial bus uses a **single master** topology. Port auto-detection scans `/dev/ttyUSB0-9` and uses whichever device opens successfully [source/scripts/op3_docker.sh:L107-L122](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/scripts/op3_docker.sh#L107-L122). You can force a specific port via the `OP3_DEVICE` environment variable [source/README.md:L125](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/README.md#L125).

---

## 2 Docker Image Build

The workspace builds a self-contained image named `motion_webots_new-op3_ros2:latest` [source/README.md:L61](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/README.md#L61). **Untested suggestion:**

```bash
docker build -t motion_webots_new-op3_ros2:latest .
```

The `Dockerfile` is a **multi-stage build** sourcing from `ros:humble-ros-base` (Ubuntu 22.04) [source/Dockerfile:L25](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/Dockerfile#L25). Key contents:

- **Webots R2025a** — downloaded in stage 1 and installed in stage 2; optional via `WITH_WEBOTS` build arg [source/Dockerfile:L1-L22](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/Dockerfile#L1-L22), [source/Dockerfile:L229-L243](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/Dockerfile#L229-L243). Required for simulation; harmless on the physical robot.
- **OpenCV 4.8.1** — compiled from source with adaptive parallelism (`-j2` on RAM < 10 GB to avoid OOM on Jetson's 7.4 GB) [source/Dockerfile:L91-L119](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/Dockerfile#L91-L119).
- **OpenVINO** — on arm64, only the Python `openvino` pip wheel is installed; the full x86_64 archive is skipped [source/Dockerfile:L126-L140](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/Dockerfile#L126-L140).
- **YOLO dependencies** — `numpy<2`, `torch` (CPU channel), `ultralytics`, `onnxruntime` [source/Dockerfile:L151-L155](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/Dockerfile#L151-L155). Pinned `numpy<2` prevents ABI breakage with ROS Humble's `cv_bridge` [source/Dockerfile:L143-L150](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/Dockerfile#L143-L150).
- **Node.js 20.11.1 + pnpm 9.15.4** — installed from official tarballs; no apt repo involvement [source/Dockerfile:L158-L178](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/Dockerfile#L158-L178).
- **System tools** — `tmux`, `gum` (0.14.5), `ttyd` (1.7.7) [source/Dockerfile:L180-L207](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/Dockerfile#L180-L207). See the [shared card](../Shared/focus-shared-tools.md) (needs_review) for tool purpose.

**Estimated build time**: 20-40 minutes on Jetson, dominated by the OpenCV compilation [source/README.md:L71](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/README.md#L71).

---

## 3 Container Launch

The single authoritative container definition lives in `scripts/op3_docker.sh` [source/README.md:L85-L88](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/README.md#L85-L88). Previous tmux menu and docker-compose entries now delegate to this script [source/README.md:L86-L92](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/README.md#L86-L92).

| Subcommand | Purpose |
|---|---|
| `scripts/op3_docker.sh up` | Create/start the detached container (idempotent) |
| `scripts/op3_docker.sh shell` | Open an interactive shell inside the container |
| `scripts/op3_docker.sh doctor` | Run a multi-section hardware and workspace health check |
| `scripts/op3_docker.sh down` | Stop and remove the container |

**Untested suggestion** — full start sequence:

```bash
scripts/op3_docker.sh up        # creates container 'op3' in detached mode
scripts/op3_docker.sh shell     # enter interactive shell with ROS 2 sourced
```

The container runs **detached** with PID 1 = `sleep infinity`, so it is not tied to a single terminal window and survives disconnection [source/scripts/op3_docker.sh:L21-L28](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/scripts/op3_docker.sh#L21-L28), [source/scripts/op3_docker.sh:L532-L549](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/scripts/op3_docker.sh#L532-L549). Auto-restart is enabled (`--restart unless-stopped`) so the container revives after reboot, unless it was explicitly stopped via `down` [source/scripts/op3_docker.sh:L522-L528](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/scripts/op3_docker.sh#L522-L528).

Key runtime characteristics:

- **`--privileged -v /dev:/dev`** — the full host `/dev` tree is bound so device nodes (FTDI, V4L2 cameras) follow the host live. Using a hardcoded `--device=/dev/ttyUSB0` is **discouraged** because FTDI re-enumeration on unplug resets the major:minor, leaving a stale file descriptor in the container [source/README.md:L97-L107](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/README.md#L97-L107).
- **`-v $WS:/ros2_ws`** — the host workspace is bind-mounted; `install/` is populated inside the container via `colcon build --symlink-install`, so C++ source changes only require rebuilding inside the container [source/README.md:L74-L75](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/README.md#L74-L75).
- **X11 forwarding** — present if `$DISPLAY` is set on the host, enabling GUI tools (rqt, action editor) [source/scripts/op3_docker.sh:L500-L507](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/scripts/op3_docker.sh#L500-L507).

---

## 4 Environment Initialization

The container's ENTRYPOINT is `/docker-entrypoint.sh` [source/Dockerfile:L276-L277](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/Dockerfile#L276-L277). It performs:

1. Stash positional args (workaround for OpenVINO `setupvars.sh` consuming `$@`) [source/docker-entrypoint.sh:L12-L13](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/docker-entrypoint.sh#L12-L13).
2. Conditionally source OpenVINO `setupvars.sh` if `OPENVINO_ROOT` is set — on this arm64 image the file does not exist, so this is a no-op but kept for cross-arch safety [source/docker-entrypoint.sh:L15-L21](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/docker-entrypoint.sh#L15-L21).
3. Source `/opt/ros/humble/setup.bash` — **required**; failure here exits immediately [source/docker-entrypoint.sh:L23-L26](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/docker-entrypoint.sh#L23-L26).
4. Source `/ros2_ws/install/setup.bash` if present — continues on failure [source/docker-entrypoint.sh:L28-L32](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/docker-entrypoint.sh#L28-L32).
5. Export Webots environment (`WEBOTS_HOME`, `LD_LIBRARY_PATH`) [source/docker-entrypoint.sh:L35-L37](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/docker-entrypoint.sh#L35-L37).
6. `exec "$@"` — delegates to the CMD (`bash` by default) [source/docker-entrypoint.sh:L41-L42](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/docker-entrypoint.sh#L41-L42).

Every shell opened via `scripts/op3_docker.sh shell` wraps through this entrypoint, so `ros2` is always on PATH [source/scripts/op3_docker.sh:L563-L580](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/scripts/op3_docker.sh#L563-L580). Plain `docker exec` bypasses the entrypoint, so the script also bind-mounts `scripts/container_bashrc` to `/root/.bashrc` for safety [source/scripts/op3_docker.sh:L539](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/scripts/op3_docker.sh#L539).

---

## 5 Interactive Menu Launcher

`script.sh` is a tmux-based interactive menu launcher [source/script.sh:L1-L375](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/script.sh#L1-L375). It delegates to `scripts/op3_tmux/main.sh` and provides:

- **Launch picker** — select simulation (`webots`) or real-robot profile [source/script.sh:L46](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/script.sh#L46)
- **Build workspace** — invoke `colcon build` inside the container [source/script.sh:L47](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/script.sh#L47)
- **Health check** — runs the `doctor` subcommand [source/script.sh:L48](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/script.sh#L48), [source/script.sh:L34-L35](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/script.sh#L34-L35)
- **Install deps** — system and Python dependency resolution [source/script.sh:L49](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/script.sh#L49)
- **ROS env** — configure `ROS_DOMAIN_ID`, `ROS_LOCALHOST_ONLY`, and action file selection [source/script.sh:L50](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/script.sh#L50), [source/script.sh:L14-L35](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/script.sh#L14-L35)
- **Docker build/run/stop** — delegates to `op3_docker.sh` [source/script.sh:L51-L54](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/script.sh#L51-L54)

The menu requires the `gum` CLI tool (pulled during Docker build) and exits with an error if it is missing on the host [source/script.sh:L203-L232](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/script.sh#L203-L232).

---

## 6 Health Check (Doctor)

The `doctor` subcommand provides a seven-section diagnostic:

| Section | Checks | Source |
|---|---|---|
| 1. Host peripherals | FTDI adapter, OpenCR USB, V4L2 cameras | [source/scripts/op3_docker.sh:L178-L200](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/scripts/op3_docker.sh#L178-L200) |
| 2. DXL ports | Which `/dev/ttyUSB*` is openable and who holds it | [source/scripts/op3_docker.sh:L202-L244](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/scripts/op3_docker.sh#L202-L244) |
| 3. USB stability | Kernel disconnect count in last 30 min | [source/scripts/op3_docker.sh:L246-L257](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/scripts/op3_docker.sh#L246-L257) |
| 4. OP3.robot config | Serial path consistency with host reality | [source/scripts/op3_docker.sh:L260-L274](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/scripts/op3_docker.sh#L260-L274) |
| 5. Container ports | Device bind correctness, port holders inside container | [source/scripts/op3_docker.sh:L334-L383](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/scripts/op3_docker.sh#L334-L383) |
| 6. Container workspace | `ros2` in PATH via entrypoint, core packages importable, YOLO Python modules present | [source/scripts/op3_docker.sh:L386-L431](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/scripts/op3_docker.sh#L386-L431) |
| 7. ABI freshness | Stale `robotis_controller.h` consumers detected by timestamp comparison | [source/scripts/op3_docker.sh:L434-L477](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/scripts/op3_docker.sh#L434-L477) |

Section 7 guards against a subtle ABI bug where `robotis_controller.h` changes silently break dependent shared objects built at the wrong time, manifesting as 100% CPU spin with no error messages [source/scripts/op3_docker.sh:L438-L446](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/scripts/op3_docker.sh#L438-L446). See the [shared card](../Shared/focus-shared-manager.md) for the manager node that loads these objects.

---

## 7 Simulation vs Physical Robot Notes

| Aspect | Webots Simulation | Physical Robot (Jetson) |
|---|---|---|
| Architecture | x86_64 or arm64 (host-dependent) | arm64 (NVIDIA Jetson) |
| Serial bus | Emulated by Webots driver | FTDI FT232H via `/dev/ttyUSB*` |
| OpenVINO | Full system archive installed (if x86_64) | pip wheel only (no system archive on arm64) |
| Camera | Optional (X11-forwarded) | V4L2 bound via `/dev:/dev` |
| RAM constraints | Host-dependent | 7.4 GB; OpenCV builds at `-j2` |
| Webots | Required for sim profile | Installed but unused in real-robot profile |

---

## 8 Review Gaps

- **Pending**: Exact ROS 2 domain ID conventions for multi-robot lab deployment are not codified in the script sources but inferred from the tmux profile layer.
- **Needs review**: Shared card `focus-shared-tools.md` referenced for studio/teaching tools cross-cutting setup notes [SHARED-INDEX.md:L20].
- **Needs review**: Shared card `focus-shared-actions.md` for action editor binary path configuration [SHARED-INDEX.md:L11].
- **Unknown**: Whether the `run/run_vision_and_webots.sh` script mentioned in the README is still maintained or superseded by the Docker workflow [source/README.md:L38-L41](https://github.com/ProgramBascorro/motion_webots/blob/dba5be3fefbada854b8d6c11d6655f479b482574/README.md#L38-L41).

---

*For shared module details, see: [Workspace and package structure](../Shared/focus-shared-workspace.md) · [Framework and device interfaces](../Shared/focus-shared-framework.md) · [Manager and hardware bringup](../Shared/focus-shared-manager.md) · [Webots and simulation integration](../Shared/focus-shared-webots.md).*
