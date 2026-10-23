#!/usr/bin/env python3
import argparse
from course204.speech import load_model, transcribe_wav, transcribe_microphone


def main():
    parser = argparse.ArgumentParser(description="Arabic offline recognition with Vosk")
    parser.add_argument("--model", required=True)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--wav")
    source.add_argument("--microphone", action="store_true")
    parser.add_argument("--duration", type=float, default=8)
    parser.add_argument("--device", type=int)
    args = parser.parse_args()
    model = load_model(args.model)
    text = transcribe_wav(model, args.wav) if args.wav else transcribe_microphone(model, args.duration, args.device)
    print(text)


if __name__ == "__main__":
    main()
