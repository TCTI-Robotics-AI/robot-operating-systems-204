#!/usr/bin/env python3
"""Exercise the course AIML interpreter without starting ROS."""
import argparse
from pathlib import Path
from course204.conversation import Conversation

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("text")
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
path = root / "labs/05-conversation-and-speech/ros/course_conversation/aiml/course.aiml"
reply, intent = Conversation(path).respond(args.text)
print(reply)
print("intent=" + (intent or "none"))
