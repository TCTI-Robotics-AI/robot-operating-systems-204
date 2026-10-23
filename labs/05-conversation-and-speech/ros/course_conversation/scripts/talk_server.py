#!/usr/bin/env python3
from pathlib import Path
import rospkg
import rospy
from course_common.srv import Talk, TalkResponse
from course204.conversation import Conversation


if __name__ == "__main__":
    rospy.init_node("talk_server")
    default = Path(rospkg.RosPack().get_path("course_conversation")) / "aiml" / "course.aiml"
    conversation = Conversation(rospy.get_param("~aiml", str(default)))

    def handle(request):
        try:
            reply, command = conversation.respond(request.text)
            return TalkResponse(reply, command)
        except ValueError as exc:
            return TalkResponse(str(exc), "")

    rospy.Service("/conversation/talk", Talk, handle)
    rospy.spin()
