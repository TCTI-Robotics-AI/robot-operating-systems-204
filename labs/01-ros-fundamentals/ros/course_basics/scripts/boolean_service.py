#!/usr/bin/env python3
import rospy
from std_msgs.msg import Bool
from std_srvs.srv import SetBool, SetBoolResponse


if __name__ == "__main__":
    rospy.init_node("boolean_service")
    publisher = rospy.Publisher("/course/demo_state", Bool, queue_size=1, latch=True)
    publisher.publish(False)

    def handle(request):
        publisher.publish(request.data)
        return SetBoolResponse(True, "simulation only: {}".format(request.data))

    rospy.Service("/course/set_demo", SetBool, handle)
    rospy.spin()
