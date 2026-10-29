# Chronus: Environment, Startup and Launch — Differences

> Stage: `robot-differences` · Branch: `CHRONUS_NEW` · Commit: `54998e7c56e5b2cce4c1c533758c7d2f2cf7698b`

## Scope

This draft covers how the **Chronus** branch sets up its runtime environment, bootstraps Docker containers, and launches OP3 processes — and how that differs from earlier Alphonse configurations. Anchors inspected: `source/Dockerfile`, `source/scripts/op3_docker.sh`, `source/script.sh`, `source/docker-entrypoint.sh`, `source/README.md`. Of the 28 changed/unique candidates listed in [`drafts/DIFFERENCES.md`](DIFFERENCES.md), many remain unexamined. This is a *representative* investigation, not an exhaustive audit.

## Single-Source Container Definition

Chronus consolidates container definition into one script, `scripts/op3_docker.sh` — replacing what was once **three** conflicting sources (the tmux menu, `docker-compose.yml`, and the README's manual `docker run`).

- The README documents the convergence: "`scripts/op3_docker.sh` adalah satu-satunya tempat container didefinisikan. `./script.sh` ... dan `docker-compose.yml` sekarang memakai container yang sama (`op3`)" [source/README.md:L69-L77](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/README.md#L69-L77).
- `script.sh` menu items `M_DOCKER_RUN` / `M_DOCKER_COMPOSE_UP` / `M_DOCKER_STOP` delegate to `op3_tmux_main --docker-run/up/down` [source/script.sh:L339-L353](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/script.sh#L339-L353), no longer embedding mount mode choices. A past default of "Cache (src read-only)" was removed because it made `/ros2_ws/src` unwritable, preventing the action editor from saving `.bin` files [source/script.sh:L341-L343](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/script.sh#L341-L343).
- `op3_docker.sh` is the sole launcher: `up`, `shell`, `doctor`, `down` [source/scripts/op3_docker.sh:L39-L43](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/scripts/op3_docker.sh#L39-L43).

## Dockerfile Image Composition

The image `op3-webots-ros2:humble` is built from a multi-stage Dockerfile with two phases:

1. **Stage 1 (`webots_downloader`)** — conditionally fetches the Webots tarball (R2025a default), gated by build arg `WITH_WEBOTS` [source/Dockerfile:L1-L21](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/Dockerfile#L1-L21).
2. **Stage 2** — installs ROS Humble base, system deps, OpenCV 4.8.1 (compiled from source), OpenVINO 2025.4.0, Node.js 20.11.1, pnpm 9.15.4, `gum` 0.14.5, and `ttyd` 1.7.7 [source/Dockerfile:L25-L189](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/Dockerfile#L25-L189). The workspace is copied into `/ros2_ws` and the entrypoint `docker-entrypoint.sh` is installed [source/Dockerfile:L246-L263](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/Dockerfile#L246-L263).

Key version pins not seen in the older branch: OpenCV is compiled inside the image (not installed via apt), OpenVINO has explicit `OPENVINO_ROOT`/`OpenVINO_DIR` env vars [source/Dockerfile:L226-L231](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/Dockerfile#L226-L231), and NumPy is held `<2` to match ROS Humble's `cv_bridge` [source/Dockerfile:L235-L243](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/Dockerfile#L235-L243).

## Entrypoint and Shell Hardening

The entrypoint script fixes a concrete bug: OpenVINO's `setupvars.sh` consumed Docker's `$@` positional parameters, causing the container to `exec` nothing and exit 0 on startup. Chronus stashes the command before sourcing OpenVINO, then restores it [source/docker-entrypoint.sh:L6-L11](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/docker-entrypoint.sh#L6-L11), [source/docker-entrypoint.sh:L37](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/docker-entrypoint.sh#L37). It then sources ROS Humble and the installed workspace, exports Webots env vars, and `exec`s the saved command [source/docker-entrypoint.sh:L21-L40](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/docker-entrypoint.sh#L21-L40).

`op3_docker.sh` further hardens shell access. Because `docker exec` bypasses `ENTRYPOINT`, a bare `docker exec -it op3 bash` would have no ROS in PATH. The script injects auto-source into `/root/.bashrc` inside the container via `harden_container_shell()` [source/scripts/op3_docker.sh:L292-L303](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/scripts/op3_docker.sh#L292-L303), and the `shell` subcommand wraps `docker exec` through `/docker-entrypoint.sh` [source/scripts/op3_docker.sh:L389](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/scripts/op3_docker.sh#L389).

## Serial Port and udev Configuration

Chronus uses a **udev symlink** `/dev/ttyOP3` instead of hard-coding `/dev/ttyUSB0`. This is a robot-specific difference flagged in the source:

- `/dev/ttyOP3` points to the U2D2 FTDI adapter (VID `0403:6014`), carrying servo IDs 1–20 plus sub-controller ID 200 [source/README.md:L98-L102](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/README.md#L98-L102).
- `/dev/ttyACM0` (micro-USB OpenCR) is debug-only and must *never* be used for DXL packets [source/README.md:L101-L103](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/README.md#L101-L103).
- The container mounts the *entire* `/dev` device tree (`-v /dev:/dev`) rather than passing individual `--device` flags, so udev symlinks update live when the adapter re-enumerates [source/scripts/op3_docker.sh:L18-L22](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/scripts/op3_docker.sh#L18-L22), [source/scripts/op3_docker.sh:L354](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/scripts/op3_docker.sh#L354).

A host-side udev rule (`scripts/99-op3-opencr.rules`) must be installed with `sudo udevadm control --reload-rules && sudo udevadm trigger` [source/README.md:L105-L108](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/README.md#L105-L108). The `doctor` subcommand validates this in step 2 [source/scripts/op3_docker.sh:L98-L132](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/scripts/op3_docker.sh#L98-L132).

## Container Lifecycle Differences

| Behavior | Chronus (`op3_docker.sh`) | Old / Alphonse-adjacent |
|---|---|---|
| PID 1 | `sleep infinity` (detached, persistent) | `-it --rm ... bash` (interactive, dies on SIGHUP) |
| Restart policy | `--restart unless-stopped` [source/scripts/op3_docker.sh:L343](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/scripts/op3_docker.sh#L343) | Not set; container vanishes after reboot |
| Privileged mode | `--privileged -v /dev:/dev` [source/scripts/op3_docker.sh:L354-L356](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/scripts/op3_docker.sh#L354-L356) | `--device=/dev/ttyUSB0` (frozen major:minor) |
| Init system | `--init` (tini reaps zombies) [source/scripts/op3_docker.sh:L352](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/scripts/op3_docker.sh#L352) | None |
| Entry command | Bind-mounts `docker-entrypoint.sh` at runtime [source/scripts/op3_docker.sh:L357](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/scripts/op3_docker.sh#L357) | Baked into image |

The `--restart unless-stopped` policy is explicitly tied to the `--symlink-install` build strategy: because `install/` symlinks into `/ros2_ws`, the container must exist for ROS commands to resolve packages [source/README.md:L118-L130](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/README.md#L118-L130).

## X11 Forwarding

GUI apps (rqt_image_view, Webots) are forwarded when `DISPLAY` is set. `cmd_up()` assembles `-e DISPLAY`, binds `/tmp/.X11-unix`, and mounts the Xauthority file [source/scripts/op3_docker.sh:L329-L334](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/scripts/op3_docker.sh#L329-L334).

## Untested Operation Notes

All commands discussed — `scripts/op3_docker.sh up`, `scripts/op3_docker.sh doctor`, `docker build -t op3-webots-ros2:humble .`, `sudo udevadm control --reload-rules` — are **found in source but not executed**. No build or container lifecycle was run during this investigation.

## Uncertainties and Conflicts

- The `run_vision_and_webots.sh` path referenced in the README [source/README.md:L38-L41](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/README.md#L38-L41) does not exist in the current tree. This may indicate a deleted or planned migration.
- The Dockerfile's `WITH_WEBOTS=0` build path is untested; Webots may fail to start if the download stage is skipped but runtime deps are not.
- The `docker-compose.yml` / `docker-compose.yolo.yml` files appear in the changed-files list but were not inspected; their delegation depth to `op3_docker.sh` is inferred from the README [source/README.md:L70-L71](https://github.com/ProgramBascorro/motion_webots/blob/54998e7c56e5b2cce4c1c533758c7d2f2cf7698b/README.md#L70-L71).
- Serial port layout (`ttyOP3` → U2D2) is robot-specific to Chronus and must not be ported to other robots.

## Sources

| File | Lines | Role |
|---|---|---|
| `source/README.md` | 1–135 | Environment docs, port layout, startup notes |
| `source/Dockerfile` | 1–263 | Image build, dep versions, entrypoint install |
| `source/scripts/op3_docker.sh` | 1–407 | Container definition, launch, doctor, lifecycle |
| `source/script.sh` | 1–364 | Interactive menu, delegation to tmux launcher |
| `source/docker-entrypoint.sh` | 1–40 | Entrypoint env setup, $@ restore fix |
| `drafts/DIFFERENCES.md` | 1–168 | Changed/unique file inventory |
| `drafts/SHARED-INDEX.md` | 1–21 | Cross-reference to shared documentation |
