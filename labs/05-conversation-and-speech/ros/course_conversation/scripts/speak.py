#!/usr/bin/env python3
import subprocess
import threading
import rospy
from std_msgs.msg import String


if __name__ == "__main__":
    rospy.init_node("course_speaker")
    lock = threading.Lock()
    voice = rospy.get_param("~voice", "ar")

    def handle(message):
        with lock:
            try:
                result = subprocess.run(["espeak-ng", "-v", voice, "--", message.data[:500]],
                                        timeout=30, check=False)
                if result.returncode:
                    rospy.logwarn("Speech output failed, return code %s", result.returncode)
            except (OSError, subprocess.TimeoutExpired) as exc:
                rospy.logwarn("Speech output unavailable: %s", exc)

    rospy.Subscriber("/conversation/reply", String, handle, queue_size=1)
    rospy.spin()
