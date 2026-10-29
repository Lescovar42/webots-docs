"""Import the retained documentation snapshot into Nextra MDX pages.

Run `python scripts/import-docs.py` from any directory, or pass --source PATH.
Only Python's standard library is needed. The generated content is committed;
normal npm development and production builds do not need Python.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import html
import json
from pathlib import Path, PurePosixPath
import posixpath
import re
from urllib.parse import unquote, urlsplit, urlunsplit


ROOT = Path(__file__).resolve().parents[1]
ROOT_PAGES = {
    "README.md": "/",
    "FOCUSED-GUIDES.md": "/guides",
    "BRANCH-COMPARISON.md": "/branch-comparison",
    "REVIEW-NOTES.md": "/review-notes",
}
GUIDES = {"setup": "Setup & prerequisites", "architecture": "Architecture & interfaces", "operation": "Operation & troubleshooting", "settings": "Settings & review gaps"}
INVESTIGATIONS = {"setup": "Environment & startup", "hardware": "Hardware & calibration", "motion": "Motion & kinematics", "vision": "Camera & perception", "navigation": "Navigation & behavior", "other": "Other changes & uncertainty"}
SHARED = {
    "workspace": "Workspace & packages", "framework": "Framework & devices",
    "messages": "Messages & services", "manager": "Manager & bringup",
    "walking": "Walking & balance", "actions": "Actions & motion",
    "kinematics": "Kinematics & mathematics", "webots": "Webots & simulation",
    "teleop": "Joystick & teleoperation", "yolo": "Camera & YOLO",
    "detectors": "Ball & face detection", "object-localization": "Object & ball localization",
    "localization": "Robot localization", "footsteps": "Footstep planning",
    "demo": "Demo & soccer behavior", "tools": "Development tools",
}
LINK_DESTINATION = re.compile(r"(?<=\]\()([^\s)]+)(?=\))")
REFERENCE_DESTINATION = re.compile(r"^([ \t]{0,3}\[[^\]\n]+\]:[ \t]*)(<?)([^\s>]+)(>?)", re.M)
EXTERNAL_URL = re.compile(r"https?://[^\s)>]+")
INLINE_CODE = re.compile(r"(?<!`)(`+)(?!`)([\s\S]*?)(?<!`)\1(?!`)")


def route_for(relative: str) -> str:
    if relative in ROOT_PAGES:
        return ROOT_PAGES[relative]
    group, filename = relative.split("/", 1)
    slug = group.lower()
    stem = PurePosixPath(filename).stem
    if stem == "README":
        return f"/{slug}"
    if stem == "DIFFERENCES":
        return f"/{slug}/changed-files"
    if stem.startswith("focus-guide-"):
        name = stem.removeprefix("focus-guide-")
        return f"/{slug}/{'settings' if name == 'differences' else name}"
    if stem.startswith("focus-difference-"):
        return f"/{slug}/investigations/{stem.removeprefix('focus-difference-')}"
    if stem.startswith("focus-shared-"):
        return f"/shared/{stem.removeprefix('focus-shared-')}"
    raise ValueError(f"No route mapping for {relative}")


def mdx_path(route: str, source_path: str) -> str:
    if route == "/":
        return "index.mdx"
    if source_path.endswith("/README.md"):
        return route.lstrip("/") + "/index.mdx"
    return route.lstrip("/") + ".mdx"


def protect_code(text: str, protected: list[str]) -> str:
    def save(value: str) -> str:
        key = f"\x00PROTECTED{len(protected)}\x00"
        protected.append(value)
        return key
    lines = text.splitlines(keepends=True)
    pieces = []
    index = 0
    while index < len(lines):
        match = re.match(r"^[ \t]{0,3}(`{3,}|~{3,})", lines[index])
        if not match:
            pieces.append(lines[index])
            index += 1
            continue
        marker = match.group(1)
        block = [lines[index]]
        index += 1
        while index < len(lines):
            block.append(lines[index])
            is_end = re.match(r"^[ \t]{0,3}" + re.escape(marker[0]) + "{" + str(len(marker)) + r",}[ \t]*(?:\r?\n)?$", lines[index])
            index += 1
            if is_end:
                break
        pieces.append(save("".join(block)))
    return INLINE_CODE.sub(lambda match: save(match.group(0)), "".join(pieces))


def restore(text: str, protected: list[str]) -> str:
    return re.sub(r"\x00PROTECTED(\d+)\x00", lambda match: protected[int(match.group(1))], text)


def transform(raw: str, relative: str, routes: dict[str, str], known_files: set[str], report: dict) -> str:
    protected: list[str] = []
    text = protect_code(raw, protected)
    def rewrite(href):
        parsed = urlsplit(href)
        if parsed.scheme or parsed.netloc:
            return href
        path = unquote(parsed.path)
        target = posixpath.normpath(posixpath.join(posixpath.dirname(relative), path)) if path else relative
        fragment = parsed.fragment
        if relative == "Orion/focus-guide-differences.md" and not path and fragment == "sources":
            fragment = "6-sources"
            report["anchor_aliases_fixed"].append({"source": relative, "from": href, "to": "#6-sources"})
        if not path:
            new_href = urlunsplit(("", "", "", parsed.query, fragment))
        elif target in routes:
            new_href = urlunsplit(("", "", routes[target], parsed.query, fragment))
        elif target in known_files:
            new_href = urlunsplit(("", "", "/sources/" + target, parsed.query, fragment))
        else:
            report["unresolved_links"].append({"source": relative, "href": href, "resolved_source": target})
            return href
        report["local_links_rewritten"] += 1
        report["link_mappings"].append({"source": relative, "from": href, "to": new_href})
        return new_href
    text = LINK_DESTINATION.sub(lambda match: rewrite(match.group(0)), text)
    def rewrite_reference(match):
        report["reference_definitions_rewritten"] += 1
        return match.group(1) + match.group(2) + rewrite(match.group(3)) + match.group(4)
    text = REFERENCE_DESTINATION.sub(rewrite_reference, text)
    # Link destinations are URLs, not MDX prose or JSX. Keep every external
    # pinned citation byte-for-byte while escaping prose outside code spans.
    def protect_destination(match):
        key = f"\x00PROTECTED{len(protected)}\x00"
        protected.append(match.group(0))
        return key
    text = LINK_DESTINATION.sub(protect_destination, text)
    def protect_reference(match):
        key = f"\x00PROTECTED{len(protected)}\x00"
        protected.append(match.group(0))
        return key
    text = REFERENCE_DESTINATION.sub(protect_reference, text)
    entities = {"{": "&#123;", "}": "&#125;", "<": "&lt;", ">": "&gt;"}
    output_lines = []
    for line in text.splitlines(keepends=True):
        # Preserve Markdown blockquote markers, including nested blockquotes.
        prefix = re.match(r"^[ \t]*(?:>[ \t]*)*", line).group(0)
        body = line[len(prefix):]
        for char, entity in entities.items():
            count = body.count(char)
            report["prose_characters_escaped"][char] += count
            body = body.replace(char, entity)
        output_lines.append(prefix + body)
    output = restore("".join(output_lines), protected)
    original_external = Counter(EXTERNAL_URL.findall(raw))
    output_external = Counter(EXTERNAL_URL.findall(output))
    if original_external != output_external:
        report["external_url_mismatches"].append(relative)
    report["external_url_occurrences_preserved"] += sum(original_external.values())
    return output


def write_meta(folder: Path, entries: dict):
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "_meta.js").write_text("export default " + json.dumps(entries, ensure_ascii=False, indent=2) + ";\n", encoding="utf-8", newline="\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=ROOT / "public" / "sources")
    args = parser.parse_args()
    source = args.source.resolve()
    content = ROOT / "content"
    files = sorted(p for p in source.rglob("*") if p.is_file())
    known_files = {p.relative_to(source).as_posix() for p in files}
    markdown = [p for p in files if p.suffix.lower() == ".md"]
    routes = {p.relative_to(source).as_posix(): route_for(p.relative_to(source).as_posix()) for p in markdown}
    if len(set(routes.values())) != len(routes):
        raise ValueError("Duplicate content routes")
    report = {
        "markdown_pages": len(markdown), "source_files": len(files),
        "manifest_files_verified": 0, "manifest_failures": [],
        "local_links_rewritten": 0, "unresolved_links": [],
        "reference_definitions_rewritten": 0,
        "anchor_aliases_fixed": [], "prose_characters_escaped": Counter(),
        "external_url_occurrences_preserved": 0, "external_url_mismatches": [],
        "link_mappings": [],
    }
    manifest = json.loads((source / "manifest.json").read_text(encoding="utf-8-sig"))
    for item in manifest["files"]:
        data = (source / item["path"]).read_bytes()
        if len(data) != item["bytes"] or hashlib.sha256(data).hexdigest() != item["sha256"]:
            report["manifest_failures"].append(item["path"])
        report["manifest_files_verified"] += 1
    if report["manifest_failures"]:
        raise ValueError(f"Source snapshot hash mismatch: {report['manifest_failures']}")

    content.mkdir(exist_ok=True)
    route_file = ROOT / "content-routes.json"
    if route_file.exists():
        previous = json.loads(route_file.read_text(encoding="utf-8"))
        for relative, old_route in previous.items():
            old = (content / mdx_path(old_route, relative)).resolve()
            if content.resolve() in old.parents and old.is_file() and relative not in routes:
                old.unlink()
    for path in markdown:
        relative = path.relative_to(source).as_posix()
        target = content / mdx_path(routes[relative], relative)
        target.parent.mkdir(parents=True, exist_ok=True)
        raw = path.read_text(encoding="utf-8-sig")
        target.write_text(transform(raw, relative, routes, known_files, report), encoding="utf-8", newline="\n")

    root_meta = {
        "index": "Overview", "alphonse": "Alphonse", "chronus": "Chronus",
        "orion": "Orion", "shared": "Shared", "branch-comparison": "Branch comparison",
        "review-notes": "Review notes & limits", "guides": {"title": "Guide index", "display": "hidden"},
    }
    write_meta(content, root_meta)
    for robot in ("alphonse", "chronus", "orion"):
        write_meta(content / robot, {"index": "Overview", **GUIDES, "investigations": "Investigations", "changed-files": "Changed files"})
        write_meta(content / robot / "investigations", INVESTIGATIONS)
    write_meta(content / "shared", {"index": "Overview", **SHARED})
    route_file.write_text(json.dumps(routes, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    report["meta_files"] = len(list(content.rglob("_meta.js")))
    report["prose_characters_escaped"] = dict(report["prose_characters_escaped"])
    (ROOT / "content-validation.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    summary = {k: v for k, v in report.items() if k != "link_mappings"}
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if report["unresolved_links"] or report["external_url_mismatches"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
