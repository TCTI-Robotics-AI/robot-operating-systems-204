"""Record and preserve five-second local microphone clips for playback and STT.

Requires ALSA arecord. Each recording starts only after Enter and a five-second
countdown. Raw audio stays in ~/.local/state/course204/audio with private access.
This tool sends no ROS or GPIO commands and uploads no audio.
"""
import array
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import time
import wave

parser = argparse.ArgumentParser()
parser.add_argument('--device', required=True, help='Explicit ALSA input, e.g. hw:CARD=EarPods,DEV=0')
parser.add_argument('--rate', type=int, default=48000, choices=(16000, 24000, 44100, 48000, 96000))
parser.add_argument('--capture-gain-db', type=float, default=0,
                    help='Report software gain already configured in ALSA; this option does not set gain')
parser.add_argument('--high-pass-hz', type=float, default=0)
args = parser.parse_args()
if not 0 <= args.capture_gain_db <= 36 or not 0 <= args.high_pass_hz <= 1000:
    parser.error('Capture gain and filter frequency are outside the supported range')
sample_rate = args.rate
settling_frames = sample_rate // 10
saved_frames = sample_rate * 5

folder = Path.home() / '.local/state/course204/audio'
folder.mkdir(parents=True, exist_ok=True, mode=0o700)
os.umask(0o077)
print(f'USB capture: {args.device}; {sample_rate} Hz, mono, 16-bit; additional software capture gain {args.capture_gain_db:g} dB; high-pass {args.high_pass_hz:g} Hz. Record 5 seconds; then playback.', flush=True)
while True:
    try:
        answer = input('Enter to record; q to quit / Enter للتسجيل، q للخروج: ')
    except EOFError:
        break
    if answer.strip().lower() == 'q':
        break
    stamp = time.strftime('%Y%m%d-%H%M%S') + '-' + str(time.time_ns() % 1000000000)
    raw = folder / ('native-' + stamp + '.wav')
    for seconds in range(5, 0, -1):
        print('GET READY / استعد: ' + str(seconds), flush=True)
        time.sleep(1)
    # Discard 100 ms of startup settling before the speaking cue; save exactly
    # five seconds of frames. Named ALSA devices own any capture gain.
    process = subprocess.Popen(['arecord', '-q', '-D', args.device,
                                '-t', 'raw', '-f', 'S16_LE', '-r', str(sample_rate), '-c', '1',
                                '-s', str(settling_frames + saved_frames)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    settling = process.stdout.read(settling_frames * 2)
    if len(settling) == settling_frames * 2:
        print('SPEAK NOW / تحدث الآن: 5 seconds', flush=True)
    captured = process.stdout.read(saved_frames * 2)
    error = process.stderr.read().decode('utf-8', errors='replace')
    code = process.wait(timeout=10)
    if code or len(settling) != settling_frames * 2 or len(captured) != saved_frames * 2:
        print(error, flush=True)
        print('RECORDING FAILED / تعذر التسجيل؛ لم يتغير ملف الاستماع', flush=True)
        continue
    with wave.open(str(raw), 'wb') as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)
        wav.writeframes(captured)
    with wave.open(str(raw), 'rb') as wav:
        rate, channels, width, count = wav.getframerate(), wav.getnchannels(), wav.getsampwidth(), wav.getnframes()
        pcm = array.array('h', wav.readframes(count))
    if sys.byteorder != 'little':
        pcm.byteswap()
    if (rate, channels, width, count) != (sample_rate, 1, 2, saved_frames):
        print('RECORDING FAILED / ملف غير مطابق لخمس ثوان', flush=True)
        continue
    peak = max(abs(v) for v in pcm)
    rms = math.sqrt(sum(v*v for v in pcm) / len(pcm))
    # Gentle first-order high-pass, initialized using the discarded settling
    # samples. This changes low-frequency response without an added volume gain.
    alpha = math.exp(-2*math.pi*args.high_pass_hz/rate)
    previous_x = previous_y = 0.0
    warmup = array.array('h', settling)
    if sys.byteorder != 'little':
        warmup.byteswap()
    for value in warmup:
        previous_y = alpha * (previous_y + value - previous_x)
        previous_x = value
    filtered = array.array('h')
    filter_clips = 0
    for value in pcm:
        output = alpha * (previous_y + value - previous_x)
        previous_x, previous_y = value, output
        sample = round(output)
        filter_clips += int(sample < -32768 or sample > 32767)
        filtered.append(max(-32768, min(32767, sample)))
    if sys.byteorder != 'little':
        filtered.byteswap()
    temporary = folder / 'microphone-gain-check.new.wav'
    with wave.open(str(temporary), 'wb') as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(rate)
        wav.writeframes(filtered.tobytes())
    destination = folder / 'microphone-gain-check.wav'
    os.replace(temporary, destination)
    report = {'duration_seconds': count/rate, 'sample_rate_hz': rate,
              'input': args.device, 'capture_software_gain_db': args.capture_gain_db,
              'raw_rms_dbfs': round(20*math.log10(max(rms, 1)/32768), 2),
              'raw_peak_dbfs': round(20*math.log10(max(peak, 1)/32768), 2),
              'raw_full_scale_percent': round(100*sum(v in (-32768,32767) for v in pcm)/len(pcm), 4),
              'playback_linear_gain_db': 0, 'raw_file': str(raw),
              'filter': {'type': 'first_order_high_pass' if args.high_pass_hz else 'none', 'cutoff_hz': args.high_pass_hz,
                         'clipped_sample_percent': round(100*filter_clips/len(pcm), 4)},
              'playback_file': str(destination)}
    (folder / 'microphone-latest.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2), flush=True)
    print('AUDIO_READY:' + hashlib.sha256(destination.read_bytes()).hexdigest(), flush=True)
    print('Recording complete / انتهى التسجيل. Listen before the next step.', flush=True)
