> Shared file-content analysis, using the Alphonse snapshot. Robot-specific runtime conditions require separate review.

# Shared Core — Kinematics and Mathematics (FOCUS)

| Field | Value |
|---|---|
| **Snapshot** | Alphonse, branch `ALPHONSE_NEW_V2`, commit `adacde8f` |
| **Stage** | shared-core |
| **Scope** | Representative investigation of `ROBOTIS-Math` shared library |
| **Assigned anchors** | `source/src/ROBOTIS-Math/` subtree |

---

## 1 Scope and Purpose

This card documents a subset of the `ROBOTIS-Math` ROS 2 package found under `source/src/ROBOTIS-Math/`. The shared library (`robotis_math`) supplies 2-D Bézier curve evaluation, basic polynomial helpers, and an Eigen-based linear-algebra / kinematics utility set. It is built as a shared library via `ament_cmake` and consumed by downstream manipulator modules.

The assigned anchors have identical SHA-256 content across all three robot snapshots examined. This card describes the *code contracts* observable in the source; it does **not** establish runtime equivalence between Alphonse, Chronus, or Orion.

---

## 2 Observed Behaviour

### 2.1 Bézier Curve Evaluation

The `BezierCurve` class (`robotis_framework` namespace) supports 2-D point generation along a parametric Bézier curve:

- **Constructor / destructor**: Empty bodies; no internal state beyond a `std::vector<Point2D>` member. [source/src/ROBOTIS-Math/robotis_math/src/bezier_curve.cpp:L28-L36](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Math/robotis_math/src/bezier_curve.cpp#L28-L36)
- **`setBezierControlPoints`**: Replaces the internal control-point list by copying its argument. [source/src/ROBOTIS-Math/robotis_math/src/bezier_curve.cpp:L38-L42](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Math/robotis_math/src/bezier_curve.cpp#L38-L42)
- **`getPoint(double t)`**: Returns the curve position at parameter `t ∈ [0, 1]`. Values outside this range are clamped to 0 or 1. [source/src/ROBOTIS-Math/robotis_math/src/bezier_curve.cpp:L46-L49](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Math/robotis_math/src/bezier_curve.cpp#L46-L49) If fewer than two control points are present, the function returns `(0, 0)`. [source/src/ROBOTIS-Math/robotis_math/src/bezier_curve.cpp:L56-L57](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Math/robotis_math/src/bezier_curve.cpp#L56-L57) The implementation manually unrolls the standard Bernstein-polynomial sum, treating the first and last control points as special cases and iterating the interior points with a combination (binomial coefficient) helper. [source/src/ROBOTIS-Math/robotis_math/src/bezier_curve.cpp:L59-L71](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Math/robotis_math/src/bezier_curve.cpp#L59-L71)

### 2.2 Base Math Helpers

Header `robotis_math_base.h` provides:

- `Point2D` — a plain struct with `double x, y` members. [source/src/ROBOTIS-Math/robotis_math/include/robotis_math/robotis_math_base.h:L48-L51](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Math/robotis_math/include/robotis_math/robotis_math_base.h#L48-L51)
- `powDI(double a, int b)` — a recursive integer-power utility handling `b = 0`, positive, and negative exponents. [source/src/ROBOTIS-Math/robotis_math/include/robotis_math/robotis_math_base.h:L39-L42](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Math/robotis_math/include/robotis_math/robotis_math_base.h#L39-L42)
- `combination(int n, int r)` — signature declared here; body implemented in the corresponding `.cpp`. [source/src/ROBOTIS-Math/robotis_math/include/robotis_math/robotis_math_base.h:L46](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Math/robotis_math/include/robotis_math/robotis_math_base.h#L46)
- Degree ↔ radian conversion macros (`DEGREE2RADIAN`, `RADIAN2DEGREE`). [source/src/ROBOTIS-Math/robotis_math/include/robotis_math/robotis_math_base.h:L36-L37](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Math/robotis_math/include/robotis_math/robotis_math_base.h#L36-L37)

### 2.3 Linear Algebra / Kinematics Utilities

Header `robotis_linear_algebra.h` declares functions operating on `Eigen::Matrix*` and `Eigen::Vector3d` types. Highlights include:

- Rigid-body transforms: `getTransformationXYZRPY`, `getInverseTransformation`, `getTranslation4D`, `getRotation4d`. [source/src/ROBOTIS-Math/robotis_math/include/robotis_math/robotis_linear_algebra.h:L39-L46](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Math/robotis_math/include/robotis_math/robotis_linear_algebra.h#L39-L46)
- Orientation conversions: RPY ↔ rotation matrix ↔ quaternion (six symmetric functions). [source/src/ROBOTIS-Math/robotis_math/include/robotis_math/robotis_linear_algebra.h:L48-L53](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Math/robotis_math/include/robotis_math/robotis_linear_algebra.h#L48-L53)
- Lie-algebra helpers: `calcHatto`, `calcRodrigues`, `convertRotToOmega`, `calcCross`, `calcInner`. [source/src/ROBOTIS-Math/robotis_math/include/robotis_math/robotis_linear_algebra.h:L55-L59](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Math/robotis_math/include/robotis_math/robotis_linear_algebra.h#L55-L59)
- A pose extraction helper `getPose3DfromTransformMatrix`. [source/src/ROBOTIS-Math/robotis_math/include/robotis_math/robotis_linear_algebra.h:L61](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Math/robotis_math/include/robotis_math/robotis_linear_algebra.h#L61)

The linear-algebra module disables Eigen's debug assertions via `EIGEN_NO_DEBUG` and `EIGEN_NO_STATIC_ASSERT`. [source/src/ROBOTIS-Math/robotis_math/include/robotis_math/robotis_linear_algebra.h:L28-L29](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Math/robotis_math/include/robotis_math/robotis_linear_algebra.h#L28-L29)

### 2.4 Compilation Targets

`CMakeLists.txt` compiles nine source files into the `robotis_math` shared library, including trajectory calculators (minimum-jerk, fifth-order polynomial, trapezoidal velocity profile), preview control, and the Bézier curve module. The library links against `rclcpp` and `Eigen3`. [source/src/ROBOTIS-Math/robotis_math/CMakeLists.txt:L16-L28](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Math/robotis_math/CMakeLists.txt#L16-L28)

---

## 3 Interfaces and Configuration

| Entry point | Signature / detail |
|---|---|
| `BezierCurve::setBezierControlPoints` | `void setBezierControlPoints(const std::vector<Point2D>&)` [source/src/ROBOTIS-Math/robotis_math/include/robotis_math/bezier_curve.h:L41](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Math/robotis_math/include/robotis_math/bezier_curve.h#L41) |
| `BezierCurve::getPoint` | `Point2D getPoint(double t)` — `t` clamped to `[0,1]` [source/src/ROBOTIS-Math/robotis_math/src/bezier_curve.cpp:L46-L49](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Math/robotis_math/src/bezier_curve.cpp#L46-L49) |
| Linear algebra functions | Declared in `robotis_framework` namespace; operate on Eigen dense types [source/src/ROBOTIS-Math/robotis_math/include/robotis_math/robotis_linear_algebra.h:L38-L62](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Math/robotis_math/include/robotis_math/robotis_linear_algebra.h#L38-L62) |
| Build system | ament_cmake, minimum CMake 3.5 [source/src/ROBOTIS-Math/robotis_math/CMakeLists.txt:L1-L2](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Math/robotis_math/CMakeLists.txt#L1-L2) |

No external configuration files were observed in the assigned paths.

---

## 4 Untested Operation Notes

- All compilation and linking commands in `CMakeLists.txt` are found in source but have **not been executed**. [source/src/ROBOTIS-Math/robotis_math/CMakeLists.txt:L16-L44](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Math/robotis_math/CMakeLists.txt#L16-L44)
- The Bézier implementation's correctness for higher-degree curves depends on the `combination` helper; overflow behaviour for large `n` is not addressed in the inspected code.
- Eigen debug macros are disabled unconditionally, which suppresses static assertion diagnostics during compilation. [source/src/ROBOTIS-Math/robotis_math/include/robotis_math/robotis_linear_algebra.h:L28-L29](https://github.com/ProgramBascorro/motion_webots/blob/adacde8f6e01e6439d170fb6bce025acc051bfa3/src/ROBOTIS-Math/robotis_math/include/robotis_math/robotis_linear_algebra.h#L28-L29)

---

## 5 Uncertainty, Conflicts, and Gaps

| Concern | Detail |
|---|---|
| **Runtime equivalence** | Identical SHA-256 hashes do not guarantee identical runtime behaviour across robots; build flags, Eigen versions, or downstream consumers may differ. |
| **Bézier degree** | The code iterates `points_num - 1` times, implying an arbitrary-degree Bernstein polynomial. No upper bound on degree is enforced. |
| **`powDI` recursion depth** | Negative-integer exponents recurse; extreme values could cause stack overflow on constrained platforms. |
| **Unexamined files** | `robotis_math_base.cpp`, `robotis_linear_algebra.cpp`, trajectory calculators, and `preview_control.cpp` were *not* read in their source form; only their headers or CMake references were inspected. |
| **Webots simulation** | If this library is consumed by a Webots simulation of Alphonse, Chronus, or Orion, the Bézier and linear-algebra routines would execute identically in simulated time-steps. Physical robot timing, sensor feedback, and motor discretisation are *not* represented in this shared code. |

---

## 6 Sources

| Path | Lines | Description |
|---|---|---|
| `source/src/ROBOTIS-Math/robotis_math/src/bezier_curve.cpp` | L28-L72 | Bézier curve implementation |
| `source/src/ROBOTIS-Math/robotis_math/include/robotis_math/bezier_curve.h` | L35-L48 | Bézier curve header |
| `source/src/ROBOTIS-Math/robotis_math/include/robotis_math/robotis_math_base.h` | L32-L51 | Base types and helpers |
| `source/src/ROBOTIS-Math/robotis_math/include/robotis_math/robotis_linear_algebra.h` | L1-L67 | Linear algebra / kinematics declarations |
| `source/src/ROBOTIS-Math/robotis_math/CMakeLists.txt` | L1-L44 | Build configuration |
| `source/src/ROBOTIS-Math/README.md` | L1-L36 | Package metadata |
