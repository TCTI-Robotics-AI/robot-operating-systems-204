#!/usr/bin/env python3
"""Expose actual acknowledged device state through a ROS service."""
import json
import threading
import rospy
from std_msgs.msg import Bool, String
from course_common.srv import SetLamp, SetLampResponse
from course204.devices import MockLamp, GPIOLamp, SerialLamp, NetworkLamp, WiFiLamp


def main():
    rospy.init_node("lamp_server")
    backend = rospy.get_param("~backend", "mock")
    if backend == "mock":
        device = MockLamp()
    elif backend == "gpio":
        device = GPIOLamp(rospy.get_param("~bcm", 17), rospy.get_param("~factory", "lgpio"),
                          rospy.get_param("~chip", None))
    elif backend == "serial":
        device = SerialLamp(rospy.get_param("~port"), rospy.get_param("~baud", 115200))
    elif backend == "network":
        device = NetworkLamp(rospy.get_param("~host", "127.0.0.1"), rospy.get_param("~network_port", 8765))
    elif backend == "wifi":
        device = WiFiLamp(rospy.get_param("~host"), rospy.get_param("~network_port", 8766))
    else:
        raise ValueError("Unknown backend: " + backend)
    lock = threading.Lock()
    state_pub = rospy.Publisher("/lamp/state", Bool, queue_size=1, latch=True)
    mock_pub = rospy.Publisher("/lamp/simulated", Bool, queue_size=1, latch=True)
    metadata_pub = rospy.Publisher("/device/status", String, queue_size=1, latch=True)
    state = device.read()
    state_pub.publish(state)
    mock_pub.publish(device.simulated)

    def handle(request):
        nonlocal state
        with lock:
            try:
                actual = device.set(request.on)
                if actual != request.on:
                    raise RuntimeError("Requested and reported states differ")
                state = actual
                state_pub.publish(actual)
                mock_pub.publish(device.simulated)
                metadata_pub.publish(json.dumps(getattr(device, "last_metadata", {})))
                mode = "افتراضية" if device.simulated else "خرج الجهاز"
                return SetLampResponse(True, actual, mode + (": تشغيل" if actual else ": إطفاء"))
            except Exception as exc:
                rospy.logerr("Device operation failed: %s", exc)
                return SetLampResponse(False, state, "فشل التنفيذ؛ آخر حالة مؤكدة فقط: " + str(exc))

    def shutdown():
        with lock:
            try:
                device.close()
            except Exception as exc:
                rospy.logerr("Could not confirm output off during shutdown: %s", exc)

    rospy.on_shutdown(shutdown)
    rospy.Service("/lamp/set", SetLamp, handle)
    rospy.spin()


if __name__ == "__main__":
    main()
