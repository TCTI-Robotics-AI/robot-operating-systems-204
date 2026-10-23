#!/usr/bin/env bash
set -euo pipefail
source /etc/os-release
if [[ ${ID:-} != ubuntu || ${VERSION_ID:-} != 20.04 ]]; then
  echo "This script is only for native Ubuntu 20.04. Pi 5 uses the container path." >&2
  exit 2
fi
if [[ -f /proc/device-tree/model ]] && grep -aq 'Raspberry Pi 5' /proc/device-tree/model; then
  echo "Do not apply the Ubuntu 20.04 native path to Pi 5." >&2; exit 2
fi
architecture=$(dpkg --print-architecture)
if [[ $architecture != amd64 && $architecture != arm64 ]]; then
  echo "Course paths target amd64 or arm64." >&2; exit 2
fi
if [[ ${1:-} != --apply ]]; then
  echo "Plan: install HTTPS/key tools, fetch the official ROS key, configure signed focal repository."
  echo "Run again with --apply to change this Ubuntu 20.04 system."
  exit 0
fi
sudo apt-get update
sudo apt-get install -y ca-certificates curl gnupg
key=$(mktemp)
trap 'rm -f -- "$key"' EXIT
curl --fail --location --proto '=https' https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o "$key"
gpg --batch --show-keys "$key"
sudo install -m 0644 "$key" /usr/share/keyrings/ros-archive-keyring.gpg
printf 'deb [arch=%s signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros/ubuntu focal main\n' "$architecture" | sudo tee /etc/apt/sources.list.d/ros-course204.list
sudo apt-get update
