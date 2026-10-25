# Minimal Noetic environment for embedded integration on low-memory boards.
FROM ros:noetic-ros-base-focal
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential python3-serial \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /course_ws
COPY shared/ros/course_common/ src/course_common/
COPY labs/06-embedded-systems/ros/course_devices/ src/course_devices/
RUN /bin/bash -c 'source /opt/ros/noetic/setup.bash && catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3 -j2'
COPY environments/noetic-device/entrypoint.sh /course-entrypoint.sh
RUN chmod 0755 /course-entrypoint.sh
ENTRYPOINT ["/course-entrypoint.sh"]
CMD ["roslaunch", "course_devices", "lamp.launch", "backend:=network"]
