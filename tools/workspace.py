#!/usr/bin/env python3
"""Link this course's Catkin packages into an isolated, non-destructive workspace."""
import argparse
from pathlib import Path
import shlex
import xml.etree.ElementTree as ET


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", type=Path, default=Path.home() / "course204_ws")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    workspace = args.workspace.expanduser().resolve()
    if workspace == root or root in workspace.parents and workspace.name == "src":
        parser.error("Choose a dedicated workspace, not the repository or its source directories")
    source = workspace / "src"
    source.mkdir(parents=True, exist_ok=True)
    names = set()
    for base in [root / "shared" / "ros", root / "labs"]:
        for manifest in sorted(base.rglob("package.xml")):
            name = ET.parse(manifest).getroot().findtext("name")
            if not name or name in names:
                raise RuntimeError("Missing or duplicate package name: {}".format(name))
            names.add(name)
            target = source / name
            if target.is_symlink() and target.resolve() == manifest.parent.resolve():
                continue
            if target.exists() or target.is_symlink():
                raise RuntimeError("Refusing to replace existing workspace entry: {}".format(target))
            target.symlink_to(manifest.parent.resolve(), target_is_directory=True)
    print("Linked {} packages into {}".format(len(names), source))
    print("cd {} && catkin_make".format(shlex.quote(str(workspace))))
    print("source {}".format(shlex.quote(str(workspace / "devel" / "setup.bash"))))


if __name__ == "__main__":
    main()
