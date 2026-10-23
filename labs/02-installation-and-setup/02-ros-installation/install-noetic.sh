#!/usr/bin/env bash
set -euo pipefail
source /etc/os-release
if [[ ${ID:-} != ubuntu || ${VERSION_ID:-} != 20.04 ]]; then
  echo "Requires Ubuntu 20.04; use the documented Noetic container on Pi 5." >&2; exit 2
fi
packages=(build-essential python3-dev python3-setuptools ros-noetic-ros-base ros-noetic-rviz ros-noetic-xacro ros-noetic-urdf
  ros-noetic-gazebo-ros-pkgs ros-noetic-gazebo-ros-control ros-noetic-controller-manager
  ros-noetic-effort-controllers ros-noetic-joint-state-controller
  ros-noetic-robot-state-publisher ros-noetic-joint-state-publisher
  ros-noetic-rqt-graph ros-noetic-rqt-publisher python3-rosdep python3-rosinstall
  python3-rosinstall-generator python3-wstool python3-pip python3-venv
  python3-serial liburdfdom-tools libportaudio2 espeak-ng alsa-utils)
if [[ ${1:-} != --apply ]]; then
  printf 'Packages planned for installation:\n'; printf '%s\n' "${packages[@]}"
  echo "Use --apply after configuring the official ROS repository."
  exit 0
fi
sudo apt-get update
sudo apt-get install -y "${packages[@]}"
echo 'Open a terminal and source /opt/ros/noetic/setup.bash'
