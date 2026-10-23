"""Device adapters: mock, checked USB serial acknowledgements, TCP and GPIO."""

import json
import socket
import threading
import time


class DeviceError(RuntimeError):
    pass


class MockLamp:
    simulated = True

    def __init__(self):
        self.state = False

    def set(self, on):
        self.state = bool(on)
        return self.state

    def read(self):
        return self.state

    def close(self):
        self.state = False


class GPIOLamp:
    simulated = False

    def __init__(self, bcm=17, factory="lgpio", chip=None):
        from gpiozero import OutputDevice
        if factory == "lgpio":
            from gpiozero.pins.lgpio import LGPIOFactory
            if chip is None or int(chip) < 0:
                raise DeviceError("Specify the gpiochip number found with gpiodetect")
            self.factory = LGPIOFactory(chip=int(chip))
        elif factory == "rpigpio":
            from gpiozero.pins.rpigpio import RPiGPIOFactory
            self.factory = RPiGPIOFactory()
        elif factory == "mock":
            from gpiozero.pins.mock import MockFactory
            self.factory = MockFactory()
            self.simulated = True
        else:
            raise DeviceError("Unknown GPIO factory")
        self.output = OutputDevice(int(bcm), initial_value=False, pin_factory=self.factory)

    def set(self, on):
        self.output.value = bool(on)
        return self.read()

    def read(self):
        return bool(self.output.value)

    def close(self):
        try:
            self.output.off()
            self.output.close()
        finally:
            self.factory.close()


class SerialLamp:
    simulated = False

    def __init__(self, port, baud=115200, timeout=2.0):
        import serial
        self.serial = serial.Serial(port, baud, timeout=0.1, write_timeout=timeout)
        self.timeout = timeout
        self.sequence = 0
        self.lock = threading.Lock()
        time.sleep(2.0)  # UNO resets on USB serial open.
        self.read()

    def exchange(self, state=None):
        with self.lock:
            self.sequence += 1
            seq = self.sequence
            request = "GET {}\n".format(seq) if state is None else "SET {} {}\n".format(int(state), seq)
            self.serial.reset_input_buffer()
            self.serial.write(request.encode("ascii"))
            self.serial.flush()
            deadline = time.monotonic() + self.timeout
            pending = bytearray()
            while time.monotonic() < deadline:
                raw = self.serial.read_until(b"\n", size=65)
                pending.extend(raw)
                if len(pending) > 64:
                    raise DeviceError("Oversized serial acknowledgement")
                if not pending.endswith(b"\n"):
                    continue
                try:
                    words = pending.decode("ascii").strip().split()
                except UnicodeDecodeError:
                    pending.clear()
                    continue
                pending.clear()
                if len(words) != 3 or words[0] != "STATE" or words[1] not in ("0", "1"):
                    continue
                if words[2] != str(seq):
                    continue
                actual = words[1] == "1"
                if state is not None and actual != bool(state):
                    raise DeviceError("Device acknowledged the wrong state")
                return actual
            raise DeviceError("No matching device acknowledgement before timeout")

    def set(self, on):
        return self.exchange(bool(on))

    def read(self):
        return self.exchange()

    def close(self):
        try:
            self.set(False)
        finally:
            self.serial.close()


class WiFiLamp:
    """The STM32 Wi-Fi firmware uses the same ASCII protocol as the USB lab."""
    simulated = False

    def __init__(self, host, port=8766, timeout=3.0):
        self.host, self.port, self.timeout = host, int(port), timeout
        self.sequence = 0
        self.lock = threading.Lock()
        self.read()

    def exchange(self, state=None):
        with self.lock:
            self.sequence += 1
            request = "GET {}\n".format(self.sequence) if state is None else "SET {} {}\n".format(int(state), self.sequence)
            try:
                with socket.create_connection((self.host, self.port), self.timeout) as connection:
                    connection.sendall(request.encode("ascii"))
                    with connection.makefile("rb") as stream:
                        raw = stream.readline(65)
                if len(raw) > 64 or not raw.endswith(b"\n"):
                    raise DeviceError("Incomplete or oversized STM32 reply")
                words = raw.decode("ascii").strip().split()
                if len(words) != 3 or words[0] != "STATE" or words[1] not in ("0", "1") or words[2] != str(self.sequence):
                    raise DeviceError("Invalid STM32 acknowledgement")
                actual = words[1] == "1"
                if state is not None and actual != bool(state):
                    raise DeviceError("STM32 reported a different output state")
                return actual
            except (OSError, ValueError) as exc:
                raise DeviceError(str(exc)) from exc

    def read(self):
        return self.exchange()

    def set(self, on):
        return self.exchange(bool(on))

    def close(self):
        self.set(False)


class NetworkLamp:
    def __init__(self, host="127.0.0.1", port=8765, timeout=2.0):
        self.host, self.port, self.timeout = host, int(port), timeout
        self.sequence = 0
        self.lock = threading.Lock()
        self.simulated = True
        self.last_metadata = {}
        self.read()

    def exchange(self, state=None):
        with self.lock:
            self.sequence += 1
            request = {"seq": self.sequence, "op": "get" if state is None else "set"}
            if state is not None:
                request["on"] = bool(state)
            try:
                with socket.create_connection((self.host, self.port), self.timeout) as sock:
                    sock.sendall((json.dumps(request) + "\n").encode("utf-8"))
                    with sock.makefile("rb") as stream:
                        data = stream.readline(4097)
                if len(data) > 4096 or not data.endswith(b"\n"):
                    raise DeviceError("Oversized or incomplete response")
                response = json.loads(data)
                if not isinstance(response, dict):
                    raise DeviceError("Expected an object response")
                if type(response.get("seq")) is not int or response.get("seq") != self.sequence or response.get("ok") is not True:
                    raise DeviceError("Remote request rejected or wrong sequence")
                actual = response["on"]
                if type(actual) is not bool or type(response.get("simulated")) is not bool:
                    raise DeviceError("Invalid state response")
                if state is not None and actual != bool(state):
                    raise DeviceError("Remote acknowledgement does not match requested state")
                self.simulated = response["simulated"]
                self.last_metadata = response.get("metadata", {})
                return actual
            except (OSError, ValueError, KeyError, TypeError) as exc:
                raise DeviceError(str(exc)) from exc

    def read(self):
        return self.exchange()

    def set(self, on):
        return self.exchange(bool(on))

    def close(self):
        self.set(False)
