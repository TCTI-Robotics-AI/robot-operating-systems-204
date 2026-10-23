#!/usr/bin/env python3
import rospy
from std_msgs.msg import String


if __name__ == "__main__":
    rospy.init_node("course_listener")
    rospy.Subscriber("/course/chatter", String, lambda msg: rospy.loginfo("received: %s", msg.data), queue_size=10)
    rospy.spin()
