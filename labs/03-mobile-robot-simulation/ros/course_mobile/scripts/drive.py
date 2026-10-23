#!/usr/bin/env python3
"""Send bounded commands to the course simulator and finish with a stop."""
import argparse
import time
import rospy
from geometry_msgs.msg import Twist


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--linear", type=float, default=0.1)
    parser.add_argument("--angular", type=float, default=0.0)
    parser.add_argument("--seconds", type=float, default=2.0)
    args = parser.parse_args(rospy.myargv()[1:])
    if not (abs(args.linear) <= 0.2 and abs(args.angular) <= 1 and 0 < args.seconds <= 10):
        parser.error("Bounds: |linear| <= 0.2 m/s, |angular| <= 1 rad/s, duration <= 10 s")
    rospy.init_node("course_drive", anonymous=True)
    publisher = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
    deadline = time.monotonic() + 8
    while publisher.get_num_connections() == 0 and time.monotonic() < deadline:
        if rospy.is_shutdown():
            return
        time.sleep(0.1)
    if not publisher.get_num_connections():
        raise RuntimeError("No simulator is subscribed to /cmd_vel")
    command = Twist()
    command.linear.x, command.angular.z = args.linear, args.angular
    try:
        end = time.monotonic() + args.seconds
        while time.monotonic() < end and not rospy.is_shutdown():
            publisher.publish(command)
            time.sleep(0.05)
    finally:
        for _ in range(4):
            publisher.publish(Twist())
            time.sleep(0.05)


if __name__ == "__main__":
    main()
