#!/usr/bin/env python3
import argparse
import json
import rospy
from course_common.srv import Talk


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", required=True)
    args = parser.parse_args(rospy.myargv()[1:])
    rospy.init_node("talk_client", anonymous=True)
    rospy.wait_for_service("/conversation/talk", timeout=10)
    response = rospy.ServiceProxy("/conversation/talk", Talk)(args.text)
    print(json.dumps({"reply": response.reply, "intent": response.intent}, ensure_ascii=False))
