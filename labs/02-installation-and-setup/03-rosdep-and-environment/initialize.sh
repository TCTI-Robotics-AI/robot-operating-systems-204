#!/usr/bin/env bash
set -euo pipefail
if ! command -v rosdep >/dev/null; then echo "Install python3-rosdep first." >&2; exit 2; fi
if [[ ! -e /etc/ros/rosdep/sources.list.d/20-default.list ]]; then sudo rosdep init; fi
rosdep update --rosdistro noetic --include-eol-distros
if [[ -n ${1:-} ]]; then
  test -d "$1/src"
  rosdep install --from-paths "$1/src" --ignore-src --rosdistro noetic -r -y
fi
