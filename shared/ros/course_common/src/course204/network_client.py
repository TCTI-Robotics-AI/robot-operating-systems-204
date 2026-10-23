import argparse
import json
from .devices import NetworkLamp


def main():
    parser = argparse.ArgumentParser(description="Inspect an agent or send one LED command")
    parser.add_argument("command", choices=["get", "on", "off"])
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    device = NetworkLamp(port=args.port)
    state = device.read() if args.command == "get" else device.set(args.command == "on")
    print(json.dumps({"on": state, "simulated": device.simulated, "metadata": device.last_metadata}, ensure_ascii=False))


if __name__ == "__main__":
    main()
