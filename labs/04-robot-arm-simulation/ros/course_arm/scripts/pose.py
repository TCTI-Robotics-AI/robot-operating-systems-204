#!/usr/bin/env python3
import argparse
import time
import rospy
from std_msgs.msg import Float64


def main():
    parser = argparse.ArgumentParser(description="Move the simulated arm within its URDF limits")
    parser.add_argument("--shoulder", type=float, default=0.25)
    parser.add_argument("--elbow", type=float, default=-0.4)
    parser.add_argument("--wrist", type=float, default=0.2)
    parser.add_argument("--gripper", type=float, default=0.02)
    args = parser.parse_args(rospy.myargv()[1:])
    values = [args.shoulder, args.elbow, args.wrist, args.gripper]
    if not all(low <= value <= high for value, (low, high) in zip(
            values, [(-1.2, 1.2), (-1.5, 1.5), (-1.5, 1.5), (0, 0.035)])):
        parser.error("Target is outside the URDF joint limits")
    rospy.init_node("arm_pose", anonymous=True)
    names = ["shoulder", "elbow", "wrist", "gripper"]
    publishers = [rospy.Publisher("/arm/{}_controller/command".format(n), Float64, queue_size=1) for n in names]
    deadline = time.monotonic() + 15
    while not all(p.get_num_connections() for p in publishers):
        if rospy.is_shutdown() or time.monotonic() >= deadline:
            raise RuntimeError("Arm controllers are not available")
        time.sleep(0.1)
    for _ in range(10):
        for publisher, value in zip(publishers, values):
            publisher.publish(value)
        time.sleep(0.1)


if __name__ == "__main__":
    main()
