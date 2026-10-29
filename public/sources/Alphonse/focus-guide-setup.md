# Alphonse: Setup and Prerequisites

**Scope:** This card covers how to obtain, build, and prepare the Alphonse development and runtime environment on branch `ALPHONSE_NEW_V2` (commit `adacde8f6e01e6439d170fb6bce025acc051bfa3`). It focuses on Docker construction, the container lifecycle, serial-port setup and the diagnostic "doctor" routine, and ROS 2 domain isolation. Detailed package contents and ROS message types are covered by later shared cards. Hardware calibration remains a robot-specific investigation.

**Status:** Draft. Claims tied directly to source files are cited. Docker build and runtime commands below are found in source but were **not executed** and remain untested.

---

## Prerequisites at a glance

| Requirement | Where enforced | Notes |
|---|---|---|
| Docker (CLI) with user access to socket | [source/scripts/op3_docker.sh:L59-L62](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/scripts/op3_docker.sh#L59-L62) | Script auto-prefers bare `docker`; falls back to `sudo docker`. |
| ROS 2 Humble container base (`ros:humble-ros-base`); this does not establish the host OS requirement | [source/Dockerfile:L25](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/Dockerfile#L25) | |
| Optional match-mode profile written for a particular i5-10210U host (4 physical / 8 logical cores) | [source/scripts/op3_docker.sh:L146](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/scripts/op3_docker.sh#L146) | A source-specific tuning assumption, not a minimum CPU requirement or a profile verified for this research PC. |
| X11 display (optional) for GUI: Webots, rqt_image_view | [source/scripts/op3_docker.sh:L520-L527](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/scripts/op3_docker.sh#L520-L527) | Forwarded conditionally when `$DISPLAY` is set. |
| U2D2 USB-to-Dynamixel board (FTDI FT232H) + OpenCR board | [source/README.md:L63-L67](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/README.md#L63-L67); [source/scripts/op3_docker.sh:L278-L288](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/scripts/op3_docker.sh#L278-L288) | Physical robot only. Simulation omits USB hardware. |
| `v4l2-ctl` on host (optional) for camera checks inside `doctor` | [source/scripts/op3_docker.sh:L243-L244](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/scripts/op3_docker.sh#L243-L244) | Warns and skips if absent. |

---

## 1. Build the Docker image

```bash
sudo docker build -t op3-webots-ros2:humble .
```

Found in [source/README.md:L57](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/README.md#L57). **Untested.**

The image is a two-stage build:

1. **Stage 1** (`webots_downloader`) downloads the Webots R2025a tarball from GitHub if `WITH_WEBOTS=1` (the default). Can be skipped via `--build-arg WITH_WEBOTS=0` [source/Dockerfile:L3-L27](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/Dockerfile#L3-L27).

2. **Stage 2** starts from `ros:humble-ros-base` (Ubuntu 22.04) and installs:
   - System build tools, Eigen, YAML-cpp, Boost, Qt5, OpenCV dev libs, ROS 2 Humble packages (`cv-bridge`, `webots-ros2-driver`, `rosbridge-server`, `usb-cam`, joint-state-publisher, RViz2, foxglove-bridge, rqt-image-view, joy, octomap packages, etc.) [source/Dockerfile:L51-L86](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/Dockerfile#L51-L86).
   - OpenCV 4.8.1 built from source for ONNX DNN compatibility [source/Dockerfile:L91-L116](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/Dockerfile#L91-L116).
   - OpenVINO runtime 2025.4.0 [source/Dockerfile:L119-L136](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/Dockerfile#L119-L136).
   - Node.js 20.11.1 via official tarball, pnpm 9.15.4 via Corepack [source/Dockerfile:L138-L159](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/Dockerfile#L138-L159).
   - `gum` 0.14.5 (CLI menu framework) and `ttyd` 1.7.7 (web terminal) from GitHub releases [source/Dockerfile:L161-L188](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/Dockerfile#L161-L188).
   - Mujoco Python wheel via pip [source/Dockerfile:L88](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/Dockerfile#L88).

The workspace source is copied into `/ros2_ws/src/` and scripts into `/ros2_ws/scripts/` [source/Dockerfile:L234-L241](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/Dockerfile#L234-L241). The entry point `/docker-entrypoint.sh` is bind-mounted from the host at container start to avoid rebuilding when it changes [source/scripts/op3_docker.sh:L531-L532](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/scripts/op3_docker.sh#L531-L532).

**Important:** The workspace is built with `--symlink-install` *inside the container*, so installed packages point to absolute paths under `/ros2_ws` that only exist there. Running `ros2 run` on the host will answer "Package not found" even if you source `install/setup.bash` [source/README.md:L104-L109](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/README.md#L104-L109).

---

## 2. Start the container

The single source of truth for container lifecycle is `scripts/op3_docker.sh` [source/README.md:L75-L78](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/README.md#L75-L78). All other callers (`./script.sh` menu items, `docker-compose.yml`) delegate to this script.

### 2.1 Start (or restart)

```bash
scripts/op3_docker.sh up
```

Found in [source/scripts/op3_docker.sh:L28-L37](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/scripts/op3_docker.sh#L28-L37). **Untested.**

This command:
- Removes any stale container with the same name [source/scripts/op3_docker.sh:L505-L507](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/scripts/op3_docker.sh#L505-L507).
- Verifies the image exists; aborts if missing [source/scripts/op3_docker.sh:L508-L511](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/scripts/op3_docker.sh#L508-L511).
- Starts a **detached** container running `sleep infinity` as PID 1 (wrapped by `--init`/tini) [source/scripts/op3_docker.sh:L543-L560](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/scripts/op3_docker.sh#L543-L560). Detached mode prevents the container from dying when a terminal window closes.
- Uses `--privileged -v /dev:/dev` so the container's `/dev` tree tracks the host live, avoiding the problem where a USB re-enumeration freezes the device node inside the container [source/scripts/op3_docker.sh:L15-L19](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/scripts/op3_docker.sh#L15-L19); [source/README.md:L89-L96](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/README.md#L89-L96).
- Sets `--restart unless-stopped` so the container auto-recovers after a host reboot [source/scripts/op3_docker.sh:L535](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/scripts/op3_docker.sh#L535).
- Passes `ROS_DOMAIN_ID=42` and `ROS_LOCALHOST_ONLY=1` to isolate this robot's DDS graph from other lab robots on domain 0 [source/scripts/op3_docker.sh:L50-L51](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/scripts/op3_docker.sh#L50-L51); [source/docker-entrypoint.sh:L30-L47](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/docker-entrypoint.sh#L30-L47).
- Injects host group IDs for `input` and `dialout` [source/scripts/op3_docker.sh:L514-L527](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/scripts/op3_docker.sh#L514-L527).
- Adds real-time scheduling capabilities (`rtprio=99`, `memlock=-1`, `SYS_NICE`, `SYS_RESOURCE`) [source/scripts/op3_docker.sh:L556-L557](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/scripts/op3_docker.sh#L556-L557).

After start, it automatically runs the **doctor** diagnostic and sets up auto-sourcing of ROS environment in the container's `.bashrc` [source/scripts/op3_docker.sh:L497-L499](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/scripts/op3_docker.sh#L497-L499); [source/scripts/op3_docker.sh:L464-L495](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/scripts/op3_docker.sh#L464-L495).

### 2.2 Open a shell inside the container

```bash
scripts/op3_docker.sh shell
```

**Untested.** This wraps the exec through `/docker-entrypoint.sh` so ROS 2 Humble and the workspace are sourced automatically [source/scripts/op3_docker.sh:L576-L584](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/scripts/op3_docker.sh#L576-L584). Without entrypoint wrapping, `docker exec -it op3 bash` gives a bare shell where `ros2` is not on PATH (historical bug, partially mitigated by `.bashrc` injection [source/README.md:L115-L119](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/README.md#L115-L119)).

### 2.3 Stop the container

```bash
scripts/op3_docker.sh down
```

Removes the container. Because `down` is a "stop" (not a crash), the `unless-stopped` restart policy will not revive it [source/README.md:L112-L113](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/README.md#L112-L113).

---

## 3. Diagnostic routine (`doctor`)

```bash
scripts/op3_docker.sh doctor
```

**Untested.** The `doctor` subcommand performs seven checks ([source/scripts/op3_docker.sh:L275-L459](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/scripts/op3_docker.sh#L275-L459)):

1. **Host devices** — verifies U2D2 FTDI and OpenCR appear in `/dev/serial/by-id/`, sets FTDI latency timer to 1 ms (default Linux 16 ms would make 8 ms control cycles jittery) [source/scripts/op3_docker.sh:L79-L103](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/scripts/op3_docker.sh#L79-L103).
2. **USB stability** — counts USB disconnect messages in kernel journal of the last 30 minutes [source/scripts/op3_docker.sh:L300-L309](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/scripts/op3_docker.sh#L300-L309).
3. **OP3.robot port paths** — confirms each by-id serial path in the robot config file actually exists on the host [source/scripts/op3_docker.sh:L312-L325](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/scripts/op3_docker.sh#L312-L325).
4. **Inside container** — checks `/dev` bind, tests that each port can be opened for read-write, and scans for stray processes holding the serial port ([source/scripts/op3_docker.sh:L328-L374](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/scripts/op3_docker.sh#L328-L374)).
5. **Workspace health** — verifies `ros2` is on PATH from both entrypoint and interactive shells, and that core packages (`op3_action_editor`, `op3_manager`, `op3_action_module`) resolve [source/scripts/op3_docker.sh:L377-L400](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/scripts/op3_docker.sh#L377-L400).
6. **ROS 2 network isolation** — confirms `ROS_LOCALHOST_ONLY=1` and domain ID are correct [source/scripts/op3_docker.sh:L402-L418](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/scripts/op3_docker.sh#L402-L418).
7. **ABI freshness** — checks that no package was last built before the current `robotis_controller.h` (stale ABI causes silent memory corruption, not link errors) [source/scripts/op3_docker.sh:L421-L459](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/scripts/op3_docker.sh#L421-L459).

---

## 4. Entry-point behaviour

The container entrypoint (`source/docker-entrypoint.sh`) performs these steps on every launch:

- Stashes the CLI arguments, then sources OpenVINO `setupvars.sh` if present (which strips `$@` from the env, hence the stash) [source/docker-entrypoint.sh:L9-L17](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/docker-entrypoint.sh#L9-L17).
- Sources `/opt/ros/humble/setup.bash` and `/ros2_ws/install/setup.bash` [source/docker-entrypoint.sh:L19-L28](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/docker-entrypoint.sh#L19-L28).
- Sets `ROS_DOMAIN_ID=42` (overridable by env) and `ROS_LOCALHOST_ONLY=1` to prevent cross-robot interference on shared lab LAN [source/docker-entrypoint.sh:L30-L47](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/docker-entrypoint.sh#L30-L47).
- Replays the stashed arguments via `exec` [source/docker-entrypoint.sh:L54-L57](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/docker-entrypoint.sh#L54-L57).

---

## 5. CPU match mode (competition tuning)

```bash
scripts/op3_docker.sh match-mode status
```

**Untested.** The example queries status. The source also provides separate `on` and `off` modes. Enabling its source-specific profile pins the desktop session to logical CPUs 3 and 7, assuming the documented i5-10210U topology. Inspect that topology before using this optional tuning on another machine. Source comments report a prior 40.3 ms versus 84.2 ms inference comparison; those figures were not measured or validated here [source/scripts/op3_docker.sh:L146-L168](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/scripts/op3_docker.sh#L146-L168). Requires root. Settings are runtime-only (`--runtime`) and vanish on reboot.

---

## 6. Alternate menu interface

`./script.sh` provides an interactive `gum`-based menu that includes the same Docker commands (build, start, stop, health check, match mode, etc.) [source/script.sh:L62-L77](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/script.sh#L62-L77). It delegates Docker operations to `scripts/op3_docker.sh` rather than duplicating them.

---

## Known gaps and uncertainties

| Area | Status | Detail |
|---|---|---|
| Webots simulation prerequisites | **Needs review** | Dockerfile includes Webots R2025a with optional install; simulation-specific setup (worlds and launch files) is still pending; consult the [shared-card index](../Shared/README.md) as it fills in. |
| Per-robot serial port mapping | **Needs review** | Alphonse uses non-standard port assignments as a U2D2 bus-workaround. Full details are in `scripts/op3_serial_setup.py --apply` ([source/README.md:L63-L66](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/README.md#L63-L66)), not yet inspected. |
| `docker-compose.yml` contents | **Pending** | Referenced but not yet read. It should delegate to `scripts/op3_docker.sh` per README note [source/README.md:L76-L77](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/README.md#L76-L77). |
| `SETUP_ROBOT_BARU.md` | **Pending** | Referenced for deploying to another robot like CHRONUS [source/README.md:L63-L66](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/README.md#L63-L66). |
| Host-side `udev` rules for FTDI latency | **Untested suggestion** | The script recommends a persistent rule at `/etc/udev/rules.d/99-dynamixelsdk-usb.rules` [source/scripts/op3_docker.sh:L99-L102](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/scripts/op3_docker.sh#L99-L102), but this was not verified. |

---

## Cross-references

For additional context, see:

- [shared card](../Shared/focus-shared-workspace.md) — Workspace and package structure (needs-review draft; do not treat as verified).
- Shared code: Webots and simulation integration — pending; see the [guide index](../FOCUSED-GUIDES.md).

## Source citations

- `source/README.md` — container build/run overview, Docker section, legacy commands warning [source/README.md:L54-L128](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/README.md#L54-L128).
- `source/Dockerfile` — full build definition, stages, installed packages, entrypoint wiring [source/Dockerfile:L1-L251](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/Dockerfile#L1-L251).
- `source/docker-entrypoint.sh` — OpenVINO/ROS sourcing, domain isolation, argument passthrough [source/docker-entrypoint.sh:L1-L57](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/docker-entrypoint.sh#L1-L57).
- `source/scripts/op3_docker.sh` — container lifecycle, doctor checks, match-mode, FTDI latency, port isolation [source/scripts/op3_docker.sh:L1-L644](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/scripts/op3_docker.sh#L1-L644).
- `source/script.sh` — interactive menu shell, enum labels, delegation [source/script.sh:L1-L157](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/script.sh#L1-L157).
