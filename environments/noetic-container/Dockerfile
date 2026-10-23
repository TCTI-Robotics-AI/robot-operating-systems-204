FROM ros:noetic-ros-base-focal
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential python3-dev python3-setuptools \
    ros-noetic-rviz ros-noetic-xacro ros-noetic-urdf \
    ros-noetic-gazebo-ros-pkgs ros-noetic-gazebo-ros-control \
    ros-noetic-controller-manager ros-noetic-effort-controllers \
    ros-noetic-joint-state-controller ros-noetic-joint-state-publisher \
    ros-noetic-robot-state-publisher ros-noetic-rqt-graph ros-noetic-rqt-publisher \
    python3-pip python3-serial python3-rosdep liburdfdom-tools libportaudio2 espeak-ng \
    && rm -rf /var/lib/apt/lists/*
RUN python3 -m pip install --no-cache-dir python-aiml==0.9.3
WORKDIR /course
CMD ["bash"]
