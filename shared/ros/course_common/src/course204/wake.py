"""Strict Arabic wake-phrase matching, separate from actuator commands."""
from course204.commands import normalize
import array
from collections import deque
import math
import sys


def matches_wake_phrase(text, phrase="يا مساعد"):
    expected = normalize(phrase)
    if not expected:
        raise ValueError("Wake phrase must not be empty")
    compact = normalize(text).replace(" ", "")
    key = expected.replace(" ", "")
    return any(compact == key * repetitions for repetitions in (1, 2, 3))


def pcm_rms(data):
    samples = array.array("h", data)
    if sys.byteorder != "little":
        samples.byteswap()
    return math.sqrt(sum(value*value for value in samples) / len(samples)) / 32768 if samples else 0.0


class SpeechSegmenter:
    """Bounded 20 ms mono PCM segmentation; no speech model or device access."""
    def __init__(self, threshold, frame_seconds=0.02, trailing_silence=0.6,
                 maximum_seconds=4.0, pre_roll=0.3, minimum_speech=0.12):
        self.threshold = threshold
        self.silence_limit = round(trailing_silence/frame_seconds)
        self.maximum_frames = round(maximum_seconds/frame_seconds)
        self.minimum_frames = round(minimum_speech/frame_seconds)
        self.pre_roll = deque(maxlen=max(1, round(pre_roll/frame_seconds)))
        self.frames = None
        self.voiced = self.silent = 0

    def feed(self, block):
        speech = pcm_rms(block) >= self.threshold
        if self.frames is None:
            self.pre_roll.append(block)
            if not speech:
                return None
            self.frames = list(self.pre_roll)
            self.voiced, self.silent = 1, 0
        else:
            self.frames.append(block)
            self.voiced += int(speech)
            self.silent = 0 if speech else self.silent + 1
        if self.silent >= self.silence_limit or len(self.frames) >= self.maximum_frames:
            result = b"".join(self.frames) if self.voiced >= self.minimum_frames else None
            self.frames = None
            self.pre_roll.clear()
            self.voiced = self.silent = 0
            return result
        return None
