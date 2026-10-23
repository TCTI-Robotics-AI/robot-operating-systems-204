#!/usr/bin/env python3
import rospy
from std_msgs.msg import String


if __name__ == "__main__":
    rospy.init_node("course_talker")
    publisher = rospy.Publisher("/course/chatter", String, queue_size=10)
    rate = rospy.Rate(2)
    number = 0
    while not rospy.is_shutdown():
        publisher.publish("مرحبا من مقرر الروبوتات {}".format(number))
        number += 1
        rate.sleep()
