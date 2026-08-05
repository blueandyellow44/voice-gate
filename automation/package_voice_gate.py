#!/usr/bin/env python3
"""
package_voice_gate.py — preflight + package the standalone voice-gate plugin.

Re-runnable. Validates the plugin against the claude.ai desktop-uploader limits,
checks structure / required files, scans for Max-private leakage, and (unless
--check-only) builds a clean distributable zip into dist/.

Usage:
    python3 automation/package_voice_gate.py            # preflight + build zip
    python3 automation/package_voice_gate.py --check-only   # preflight only

Exit code is non-zero if any BLOCKER fails, so it can gate a commit.
"""
import json
import os
import re
import sys
import zipfile
from pathlib import Path

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLUGIN_DIR = os.path.join(ROOT, "voice-gate")
DIST_DIR = os.path.join(ROOT, "dist")

# Desktop-uploader hard limits (vault lessons 856 / 858).
PLUGIN_DESC_MAX = 500
SKILL_DESC_MAX = 1024

# Files every skill must carry.
REQUIRED_SKILL_FILES = ["SKILL.md"]

# Private-leak scan: terms that must NOT appear in the distributable plugin.
# The author's own name is allowed; the targets are real private references
# such as recipients, people, private file names, and private vault paths.
# The bare craft noun "dossier" is intentionally NOT a target — the skills
# legitimately use it to say "the gate never needs a dossier / do not build
# one", which is reassuring, not leaking.
#
# The patterns themselves are private, because a committed denylist publishes
# exactly the names it exists to protect. They live in an untracked file next
# to this script, one Python regex per line, blank lines and # comments
# ignored. See private-terms.example.txt; copy it to private-terms.txt and
# fill in your own. Without that file the structural checks still run and the
# leak scan reports as unconfigured rather than silently passing.
PRIVATE_TERMS_FILE = Path(__file__).with_name("private-terms.txt")


def _load_leak_patterns():
    if not PRIVATE_TERMS_FILE.exists():
        return None
    out = []
    for line in PRIVATE_TERMS_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            out.append(line)
    return out


LEAK_PATTERNS = _load_leak_patterns()
# Lines/files where an incidental match is legitimate (author credit, etc.).
LEAK_ALLOW_SUBSTR = [
    "Max Sheahan",         # author name
]

ANGLE_PLACEHOLDER = re.compile(r"<[A-Za-z][A-Za-z0-9 _/-]*>")

results = {"blocker": [], "ok": [], "warn": []}


def blocker(msg):
    results["blocker"].append(msg)


def ok(msg):
    results["ok"].append(msg)


def warn(msg):
    results["warn"].append(msg)


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def frontmatter_desc(text):
    m = re.search(r"^---\s*$(.*?)^---\s*$", text, re.M | re.S)
    if not m:
        return None
    fm = m.group(1)
    d = re.search(r"^description:\s*(.+?)\s*$", fm, re.M)
    return d.group(1).strip() if d else None


def frontmatter_name(text):
    m = re.search(r"^---\s*$(.*?)^---\s*$", text, re.M | re.S)
    if not m:
        return None
    n = re.search(r"^name:\s*(.+?)\s*$", m.group(1), re.M)
    return n.group(1).strip() if n else None


def preflight():
    # 1. plugin.json valid + description length
    pj_path = os.path.join(PLUGIN_DIR, ".claude-plugin", "plugin.json")
    if not os.path.isfile(pj_path):
        blocker("plugin.json missing at .claude-plugin/plugin.json")
        return None
    try:
        pj = json.loads(read(pj_path))
    except json.JSONDecodeError as e:
        blocker(f"plugin.json is invalid JSON: {e}")
        return None
    ok("plugin.json is valid JSON")

    for field in ("name", "version", "description"):
        if field not in pj:
            blocker(f"plugin.json missing required field: {field}")
    name = pj.get("name", "")
    version = pj.get("version", "")
    desc = pj.get("description", "")

    if len(desc) > PLUGIN_DESC_MAX:
        blocker(f"plugin description {len(desc)} > {PLUGIN_DESC_MAX}")
    else:
        ok(f"plugin description {len(desc)} <= {PLUGIN_DESC_MAX}")
    if ANGLE_PLACEHOLDER.search(desc):
        blocker("plugin description contains an <angle-bracket> placeholder")
    else:
        ok("plugin description has no angle-bracket placeholders")

    # 2. skills present + frontmatter validity
    skills_dir = os.path.join(PLUGIN_DIR, "skills")
    if not os.path.isdir(skills_dir):
        blocker("skills/ directory missing")
        return None
    skills = sorted(
        d for d in os.listdir(skills_dir)
        if os.path.isdir(os.path.join(skills_dir, d))
    )
    if not skills:
        blocker("no skills found under skills/")
    else:
        ok(f"skills present: {', '.join(skills)}")

    for s in skills:
        sdir = os.path.join(skills_dir, s)
        for req in REQUIRED_SKILL_FILES:
            if not os.path.isfile(os.path.join(sdir, req)):
                blocker(f"skill {s} missing required file {req}")
        skill_md = os.path.join(sdir, "SKILL.md")
        if not os.path.isfile(skill_md):
            continue
        t = read(skill_md)
        fname = frontmatter_name(t)
        fdesc = frontmatter_desc(t)
        if fname is None:
            blocker(f"skill {s}: SKILL.md frontmatter has no name")
        elif fname != s:
            warn(f"skill {s}: frontmatter name '{fname}' != dir name '{s}'")
        if fdesc is None:
            blocker(f"skill {s}: SKILL.md frontmatter has no description")
        else:
            if len(fdesc) > SKILL_DESC_MAX:
                blocker(f"skill {s}: description {len(fdesc)} > {SKILL_DESC_MAX}")
            else:
                ok(f"skill {s}: description {len(fdesc)} <= {SKILL_DESC_MAX}")
            if ANGLE_PLACEHOLDER.search(fdesc):
                blocker(f"skill {s}: description has an <angle-bracket> placeholder")
            else:
                ok(f"skill {s}: description has no angle-bracket placeholders")

    # 2b. agents present (optional) + frontmatter validity
    agents_dir = os.path.join(PLUGIN_DIR, "agents")
    if os.path.isdir(agents_dir):
        agent_files = sorted(f for f in os.listdir(agents_dir) if f.endswith(".md"))
        if agent_files:
            ok(f"agents present: {', '.join(a[:-3] for a in agent_files)}")
        for a in agent_files:
            t = read(os.path.join(agents_dir, a))
            aname = frontmatter_name(t)
            adesc = frontmatter_desc(t)
            stem = a[:-3]
            if aname is None:
                blocker(f"agent {a}: frontmatter has no name")
            elif aname != stem:
                warn(f"agent {a}: frontmatter name '{aname}' != file stem '{stem}'")
            if adesc is None:
                blocker(f"agent {a}: frontmatter has no description")
            else:
                if len(adesc) > SKILL_DESC_MAX:
                    blocker(f"agent {a}: description {len(adesc)} > {SKILL_DESC_MAX}")
                else:
                    ok(f"agent {a}: description {len(adesc)} <= {SKILL_DESC_MAX}")
                if ANGLE_PLACEHOLDER.search(adesc):
                    blocker(f"agent {a}: description has an <angle-bracket> placeholder")
                else:
                    ok(f"agent {a}: description has no angle-bracket placeholders")

    # 3. README present
    if os.path.isfile(os.path.join(PLUGIN_DIR, "README.md")):
        ok("README.md present (front door)")
    else:
        warn("README.md missing")

    return {"name": name, "version": version, "skills": skills}


def leak_scan():
    hits = []
    if LEAK_PATTERNS is None:
        blocker(
            f"private-leak scan UNCONFIGURED: {PRIVATE_TERMS_FILE.name} not found. "
            f"Copy {PRIVATE_TERMS_FILE.with_name('private-terms.example.txt').name} "
            "to it and add your own terms. Refusing to report a clean scan that never ran."
        )
        return hits
    if not LEAK_PATTERNS:
        blocker(f"private-leak scan UNCONFIGURED: {PRIVATE_TERMS_FILE.name} is empty.")
        return hits
    pats = [re.compile(p) for p in LEAK_PATTERNS]
    for dirpath, dirnames, filenames in os.walk(PLUGIN_DIR):
        if ".git" in dirpath:
            continue
        for fn in filenames:
            if fn == ".DS_Store" or fn.endswith(".pyc"):
                continue
            fp = os.path.join(dirpath, fn)
            rel = os.path.relpath(fp, ROOT)
            try:
                text = read(fp)
            except (UnicodeDecodeError, IsADirectoryError):
                continue
            for i, line in enumerate(text.splitlines(), 1):
                if any(a in line for a in LEAK_ALLOW_SUBSTR):
                    continue
                for pat in pats:
                    if pat.search(line):
                        hits.append((rel, i, pat.pattern, line.strip()[:100]))
    if hits:
        for rel, i, pat, snippet in hits:
            blocker(f"LEAK {rel}:{i} matched /{pat}/ -> {snippet}")
    else:
        ok("private-leak scan clean (no dossier/family/friend/private terms)")
    return hits


def build_zip(meta):
    os.makedirs(DIST_DIR, exist_ok=True)
    name = f"{meta['name']}-{meta['version']}.zip"
    out = os.path.join(DIST_DIR, name)
    if os.path.exists(out):
        os.remove(out)
    count = 0
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for dirpath, dirnames, filenames in os.walk(PLUGIN_DIR):
            dirnames[:] = [d for d in dirnames if d not in (".git", "__pycache__")]
            for fn in filenames:
                if fn == ".DS_Store" or fn.endswith(".pyc"):
                    continue
                fp = os.path.join(dirpath, fn)
                # arcname keeps a top-level voice-gate/ folder inside the zip
                arc = os.path.join(
                    meta["name"], os.path.relpath(fp, PLUGIN_DIR)
                )
                z.write(fp, arc)
                count += 1
    return out, count


def main():
    check_only = "--check-only" in sys.argv
    print("== voice-gate preflight ==")
    meta = preflight()
    leak_scan()

    print("\n-- OK --")
    for m in results["ok"]:
        print(f"  [ok] {m}")
    if results["warn"]:
        print("\n-- WARN --")
        for m in results["warn"]:
            print(f"  [warn] {m}")
    if results["blocker"]:
        print("\n-- BLOCKER --")
        for m in results["blocker"]:
            print(f"  [BLOCK] {m}")
        print("\nPREFLIGHT FAILED")
        sys.exit(1)

    print("\nPREFLIGHT PASSED")

    if check_only or meta is None:
        return
    out, count = build_zip(meta)
    print(f"\n== packaged ==\n  {out}\n  {count} files")


if __name__ == "__main__":
    main()
