"""A loopback device agent, intended to be reached through an SSH tunnel."""

import argparse
import json
import os
import platform
import socketserver
import threading
from .devices import MockLamp, GPIOLamp


def handle_request(request, device):
    if not isinstance(request, dict) or type(request.get("seq")) is not int:
        raise ValueError("Integer sequence is required")
    if not 0 < request["seq"] < 2 ** 31:
        raise ValueError("Sequence out of range")
    if request.get("op") == "set":
        if type(request.get("on")) is not bool:
            raise ValueError("on must be a boolean")
        state = device.set(request["on"])
    elif request.get("op") == "get":
        state = device.read()
    else:
        raise ValueError("Unknown operation")
    return {"seq": request["seq"], "ok": True, "on": state,
            "simulated": device.simulated,
            "metadata": {"system": platform.system(), "machine": platform.machine(),
                         "hostname": platform.node(),
                         "load1": os.getloadavg()[0] if hasattr(os, "getloadavg") else None}}


class AgentServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True

    def __init__(self, address, device):
        self.device = device
        self.device_lock = threading.Lock()
        super().__init__(address, AgentHandler)


class AgentHandler(socketserver.StreamRequestHandler):
    def handle(self):
        self.request.settimeout(2.0)
        try:
            raw = self.rfile.readline(1025)
            if len(raw) > 1024 or not raw.endswith(b"\n"):
                raise ValueError("Incomplete or oversized request")
            request = json.loads(raw)
            with self.server.device_lock:
                response = handle_request(request, self.server.device)
        except (OSError, ValueError, TypeError, RuntimeError) as exc:
            response = {"ok": False, "error": str(exc)}
        self.wfile.write((json.dumps(response) + "\n").encode("utf-8"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--driver", choices=["mock", "gpio"], default="mock")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--bcm", type=int, default=17)
    parser.add_argument("--factory", choices=["lgpio", "rpigpio", "mock"], default="lgpio")
    parser.add_argument("--chip", type=int)
    args = parser.parse_args()
    device = MockLamp() if args.driver == "mock" else GPIOLamp(args.bcm, args.factory, args.chip)
    try:
        with AgentServer(("127.0.0.1", args.port), device) as server:
            print("Agent listening on loopback port {} (simulated={})".format(args.port, device.simulated), flush=True)
            server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        device.close()


if __name__ == "__main__":
    main()
