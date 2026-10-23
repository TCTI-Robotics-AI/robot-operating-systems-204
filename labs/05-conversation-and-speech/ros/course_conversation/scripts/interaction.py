#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from course_common.srv import Talk, SetLamp


if __name__ == "__main__":
    rospy.init_node("interaction")
    execute = rospy.get_param("~execute_lamp", False)
    publisher = rospy.Publisher("/conversation/reply", String, queue_size=5)
    rospy.wait_for_service("/conversation/talk", timeout=15)
    talk = rospy.ServiceProxy("/conversation/talk", Talk)

    def handle(message):
        try:
            result = talk(message.data)
            reply = result.reply
            if execute and result.intent in ("on", "off"):
                rospy.wait_for_service("/lamp/set", timeout=2)
                state = rospy.ServiceProxy("/lamp/set", SetLamp)(result.intent == "on")
                reply = state.message if state.success else "تعذر التنفيذ: " + state.message
            publisher.publish(reply)
        except (rospy.ROSException, rospy.ServiceException) as exc:
            publisher.publish("الخدمة غير متاحة: " + str(exc))

    rospy.Subscriber("/speech/text", String, handle, queue_size=5)
    rospy.spin()
