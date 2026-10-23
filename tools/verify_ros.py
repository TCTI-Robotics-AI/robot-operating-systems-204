#!/usr/bin/env python3
"""Run bounded, isolated ROS/Gazebo integration checks on a prepared Linux host.

Source the built Catkin workspace first. Only processes started by this script
are stopped. This does not test physical boards, microphones or Pi graphics.
"""
import argparse
from datetime import datetime, timezone
import json
import math
import os
from pathlib import Path
import signal
import socket
import subprocess
import tempfile
import threading
import time
import xmlrpc.client

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--output", type=Path, required=True)
parser.add_argument("--ros-port", type=int, default=11411)
parser.add_argument("--gazebo-port", type=int, default=11445)
parser.add_argument("--only", help="Run only the named check")
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
os.environ["ROS_MASTER_URI"] = "http://127.0.0.1:{}".format(args.ros_port)
os.environ["ROS_IP"] = "127.0.0.1"
os.environ["GAZEBO_MASTER_URI"] = "http://127.0.0.1:{}".format(args.gazebo_port)
os.environ["GAZEBO_MODEL_DATABASE_URI"] = ""
logs = Path(tempfile.mkdtemp(prefix="course204-ros-check-"))
os.environ["ROS_LOG_DIR"] = str(logs / "ros")
children = []
results = []


def start(name, command):
    output = open(logs / (name + ".log"), "w")
    process = subprocess.Popen(command, stdout=output, stderr=subprocess.STDOUT,
                               start_new_session=True, env=os.environ.copy())
    children.append((process, output))
    return process


def stop(process):
    try:
        os.killpg(process.pid, signal.SIGINT)
    except ProcessLookupError:
        return
    try:
        process.wait(timeout=8)
    except subprocess.TimeoutExpired:
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        process.wait(timeout=3)


def until(predicate, timeout=30, reason="Condition not reached"):
    end = time.monotonic() + timeout
    while time.monotonic() < end:
        if predicate():
            return
        time.sleep(0.1)
    raise AssertionError(reason)


def run_case(name, function):
    if args.only and args.only != name:
        return
    started = time.monotonic()
    try:
        detail = function()
        results.append({"check": name, "status": "passed", "detail": detail,
                        "elapsed_seconds": round(time.monotonic() - started, 2)})
    except Exception as exc:
        results.append({"check": name, "status": "failed", "detail": str(exc),
                        "elapsed_seconds": round(time.monotonic() - started, 2)})
    print(json.dumps(results[-1], ensure_ascii=False), flush=True)


class Topic:
    def __init__(self, name, message_type):
        self.message = None
        self.count = 0
        self.subscription = rospy.Subscriber(name, message_type, self.receive, queue_size=20)

    def receive(self, message):
        self.message = message
        self.count += 1

    def close(self):
        self.subscription.unregister()


for port in [args.ros_port, args.gazebo_port]:
    with socket.socket() as probe:
        probe.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        probe.bind(("127.0.0.1", port))

try:
    master = start("master", ["roscore", "-p", str(args.ros_port)])

    def master_ready():
        try:
            return xmlrpc.client.ServerProxy(os.environ["ROS_MASTER_URI"]).getPid("/verification")[0] == 1
        except OSError:
            return False

    until(master_ready, reason="ROS master did not start")
    import rospy
    from std_msgs.msg import Bool, String
    from std_srvs.srv import SetBool
    from course_common.srv import SetLamp, Talk

    rospy.init_node("course204_verification", disable_signals=True)

    def basics():
        process = start("basics", ["roslaunch", "course_basics", "communication.launch"])
        topic = Topic("/course/chatter", String)
        try:
            until(lambda: topic.count >= 2, reason="No repeated talker messages")
            rospy.wait_for_service("/course/set_demo", timeout=10)
            service = rospy.ServiceProxy("/course/set_demo", SetBool)
            assert service(True).success and service(False).success
            return "Repeated topic messages and true/false service calls succeeded"
        finally:
            topic.close()
            stop(process)

    run_case("ros_topic_and_service", basics)

    def conversation():
        lamp = start("mock-lamp", ["roslaunch", "course_devices", "lamp.launch"])
        talk_process = start("conversation", ["roslaunch", "course_conversation", "conversation.launch", "execute_lamp:=true"])
        state = Topic("/lamp/state", Bool)
        reply = Topic("/conversation/reply", String)
        publisher = rospy.Publisher("/speech/text", String, queue_size=2)
        try:
            rospy.wait_for_service("/conversation/talk", timeout=20)
            rospy.wait_for_service("/lamp/set", timeout=10)
            talk = rospy.ServiceProxy("/conversation/talk", Talk)
            assert "مرحب" in talk("مرحبا").reply
            assert talk("شغل اللمبة").intent == "on"
            assert talk("لا تشغل اللمبة").intent == ""
            until(lambda: publisher.get_num_connections() > 0 and state.message is not None)
            publisher.publish("شغل اللمبة")
            until(lambda: state.message.data is True, reason="Conversation did not switch mock lamp on")
            previous = reply.count
            publisher.publish("لا تشغل اللمبة")
            until(lambda: reply.count > previous)
            assert state.message.data is True
            publisher.publish("طفي اللمبة")
            until(lambda: state.message.data is False, reason="Conversation did not switch mock lamp off")
            return "AIML service, topic interaction and mock lamp on/off; negated phrase did not execute"
        finally:
            publisher.unregister()
            state.close()
            reply.close()
            stop(talk_process)
            stop(lamp)

    run_case("ros_conversation_mock_device", conversation)

    def network():
        from course204.agent import AgentServer
        from course204.devices import MockLamp
        with AgentServer(("127.0.0.1", 0), MockLamp()) as agent:
            worker = threading.Thread(target=agent.serve_forever, daemon=True)
            worker.start()
            bridge = start("network-bridge", ["roslaunch", "course_devices", "lamp.launch", "backend:=network",
                                               "network_port:=" + str(agent.server_address[1])])
            try:
                rospy.wait_for_service("/lamp/set", timeout=15)
                service = rospy.ServiceProxy("/lamp/set", SetLamp)
                answer = service(True)
                assert answer.success and answer.state and agent.device.read()
                answer = service(False)
                assert answer.success and not answer.state and not agent.device.read()
                return "ROS service reached real TCP loopback agent and confirmed mock output state"
            finally:
                stop(bridge)
                agent.shutdown()
                worker.join(3)

    run_case("ros_network_device_bridge", network)

    def mobile():
        from nav_msgs.msg import Odometry
        odom = Topic("/odom", Odometry)
        process = start("mobile", ["roslaunch", "course_mobile", "gazebo.launch", "gui:=false"])
        try:
            until(lambda: odom.count >= 10, timeout=50, reason="Gazebo mobile odometry not available")
            first = odom.message.pose.pose.position
            x, y = first.x, first.y
            subprocess.run(["rosrun", "course_mobile", "drive.py", "--linear", "0.1", "--seconds", "3"], check=True, timeout=20)
            count = odom.count
            until(lambda: odom.count >= count + 30, timeout=10)
            last = odom.message
            distance = math.hypot(last.pose.pose.position.x - x, last.pose.pose.position.y - y)
            assert distance > 0.04, "Robot did not move: {} m".format(distance)
            assert abs(last.twist.twist.linear.x) < 0.05, "Robot did not stop"
            return {"travel_m": round(distance, 4), "stopped_linear_m_s": round(last.twist.twist.linear.x, 4)}
        finally:
            odom.close()
            stop(process)
            rospy.set_param("/use_sim_time", False)

    run_case("gazebo_mobile_motion_and_stop", mobile)

    def arm():
        from sensor_msgs.msg import JointState
        states = Topic("/arm/joint_states", JointState)
        process = start("arm", ["roslaunch", "course_arm", "gazebo.launch", "gui:=false"])
        try:
            until(lambda: states.count >= 10, timeout=50, reason="Arm controllers did not publish states")
            subprocess.run(["rosrun", "course_arm", "pose.py"], check=True, timeout=25)
            targets = {"shoulder_joint": 0.25, "elbow_joint": -0.4, "wrist_joint": 0.2, "gripper_joint": 0.02}

            def at_target():
                values = dict(zip(states.message.name, states.message.position))
                return all(name in values and abs(values[name] - target) < (0.007 if name == "gripper_joint" else 0.1)
                           for name, target in targets.items())

            try:
                until(at_target, timeout=20, reason="Simulated joints did not reach commanded positions")
            except AssertionError as exc:
                raise AssertionError(str(exc) + ": " + str(dict(zip(states.message.name, states.message.position))))
            return {name: round(value, 4) for name, value in zip(states.message.name, states.message.position)}
        finally:
            states.close()
            stop(process)
            rospy.set_param("/use_sim_time", False)

    run_case("gazebo_arm_position_control", arm)
finally:
    for process, output in reversed(children):
        stop(process)
        output.close()
    report = {"date": datetime.now(timezone.utc).date().isoformat(), "environment": "WSL Ubuntu 20.04 amd64 / ROS Noetic / Gazebo Classic 11",
              "physical_hardware_tested": False, "checks": results,
              "not_tested": ["Pi 4", "Pi 5", "Arduino USB", "STM32 USB or Wi-Fi", "Odroid",
                             "microphone and Arabic Vosk recognition accuracy", "RViz/Gazebo interactive GUI"]}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Diagnostic logs: " + str(logs), flush=True)

raise SystemExit(0 if results and all(item["status"] == "passed" for item in results) else 1)
