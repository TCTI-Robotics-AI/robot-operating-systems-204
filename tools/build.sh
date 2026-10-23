#!/usr/bin/env bash
set -eo pipefail
repository=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)
workspace=${1:-"$HOME/course204_ws"}
if [[ ! -f /opt/ros/noetic/setup.bash ]]; then
  echo "ROS Noetic is missing. Follow the course environment guide." >&2
  exit 1
fi
source /opt/ros/noetic/setup.bash
python3 "$repository/tools/workspace.py" --workspace "$workspace"
cd -- "$workspace"
catkin_make -DPYTHON_EXECUTABLE="$(command -v python3)"
