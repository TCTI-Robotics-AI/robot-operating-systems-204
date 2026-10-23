#!/usr/bin/env python3
import time
import rospy
from std_msgs.msg import String
from course204.speech import load_model, transcribe_wav, transcribe_microphone


if __name__ == "__main__":
    rospy.init_node("arabic_speech")
    publisher = rospy.Publisher("/speech/text", String, queue_size=1, latch=True)
    model = load_model(rospy.get_param("~model"))
    wav = rospy.get_param("~wav", "")
    text = transcribe_wav(model, wav) if wav else transcribe_microphone(
        model, rospy.get_param("~duration", 8.0), rospy.get_param("~device", None))
    deadline = time.monotonic() + 5
    while not publisher.get_num_connections() and time.monotonic() < deadline and not rospy.is_shutdown():
        rospy.sleep(0.1)
    if text:
        publisher.publish(text)
        rospy.loginfo("Recognized text: %s", text)
    else:
        rospy.logwarn("No words recognized; no command was published")
    rospy.spin()
