"""Behavioral tests for command handling, transport and actual AIML matching."""
import json
from pathlib import Path
import socket
import socketserver
import threading
import unittest
from unittest.mock import Mock, patch

from course204.agent import AgentServer, handle_request
from course204.commands import intent
from course204.conversation import Conversation
from course204.devices import DeviceError, GPIOLamp, MockLamp, NetworkLamp, SerialLamp, WiFiLamp


class CommandsTest(unittest.TestCase):
    def test_arabic_normalization(self):
        self.assertEqual(intent("  أَطْفِئ اللمبة!  "), "off")
        self.assertEqual(intent("شَغِّل الـلمبة"), "on")

    def test_unrecognized_and_negated_requests_do_not_execute(self):
        for text in ["لا تشغل اللمبة", "هل شغل اللمبة؟", "شغل", "", "شغل اللمبة بعد ساعة"]:
            self.assertIsNone(intent(text), text)

    def test_actual_aiml_interpreter(self):
        path = Path(__file__).resolve().parents[1] / "labs/05-conversation-and-speech/ros/course_conversation/aiml/course.aiml"
        talk = Conversation(path)
        self.assertIn("مرحب", talk.respond("مَرْحَبًا")[0])
        self.assertEqual(talk.respond("شغل اللمبة")[1], "on")
        self.assertEqual(talk.respond("لا تشغل اللمبة")[1], "")
        self.assertIn("لم أفهم", talk.respond("كلام غير معروف")[0])


class DeviceTest(unittest.TestCase):
    def test_wifi_ascii_transport_and_wrong_acknowledgement(self):
        class Handler(socketserver.StreamRequestHandler):
            def handle(self):
                words = self.rfile.readline().decode("ascii").split()
                if words[0] == "SET":
                    self.server.state = words[1] == "1"
                seq = words[-1] if not self.server.bad_sequence else "0"
                self.wfile.write("STATE {} {}\n".format(int(self.server.state), seq).encode("ascii"))
        with socketserver.TCPServer(("127.0.0.1", 0), Handler) as server:
            server.state, server.bad_sequence = False, False
            worker = threading.Thread(target=server.serve_forever, daemon=True)
            worker.start()
            try:
                lamp = WiFiLamp("127.0.0.1", port=server.server_address[1])
                self.assertTrue(lamp.set(True))
                self.assertTrue(lamp.read())
                self.assertFalse(lamp.simulated)
                server.bad_sequence = True
                with self.assertRaises(DeviceError):
                    lamp.read()
                server.bad_sequence = False
                lamp.close()
                self.assertFalse(server.state)
            finally:
                server.shutdown()
                worker.join(3)

    def test_gpio_mock_backend_does_not_claim_hardware(self):
        lamp = GPIOLamp(factory="mock")
        try:
            self.assertTrue(lamp.simulated)
            self.assertFalse(lamp.read())
            self.assertTrue(lamp.set(True))
            self.assertFalse(lamp.set(False))
        finally:
            lamp.close()

    def test_rejected_request_does_not_modify_output(self):
        lamp = MockLamp()
        for request in [{"seq": True, "op": "set", "on": True},
                        {"seq": 1, "op": "set", "on": "false"},
                        {"seq": 1, "op": "delete"}]:
            with self.assertRaises(ValueError):
                handle_request(request, lamp)
            self.assertFalse(lamp.read())

    def test_real_loopback_network_round_trip(self):
        with AgentServer(("127.0.0.1", 0), MockLamp()) as server:
            worker = threading.Thread(target=server.serve_forever, daemon=True)
            worker.start()
            try:
                client = NetworkLamp(port=server.server_address[1])
                self.assertTrue(client.set(True))
                self.assertTrue(client.read())
                self.assertTrue(client.simulated)
                with socket.create_connection(server.server_address) as connection:
                    connection.sendall(b'{"seq":2,"op":"set","on":"false"}\n')
                    response = json.loads(connection.makefile("rb").readline())
                self.assertFalse(response["ok"])
                self.assertTrue(client.read())
                client.close()
                self.assertFalse(server.device.read())
            finally:
                server.shutdown()
                worker.join(3)

    def make_serial(self, frames):
        port = Mock()
        port.read_until.side_effect = frames
        with patch("serial.Serial", return_value=port), patch("course204.devices.time.sleep"):
            lamp = SerialLamp("unused", timeout=0.02)
        return lamp, port

    def test_partial_and_stale_serial_acknowledgements(self):
        lamp, port = self.make_serial([b"STA", b"TE 0 1\n", b"STATE 0 1\n", b"STATE 1 2\n"])
        self.assertTrue(lamp.set(True))
        self.assertEqual(port.write.call_args.args[0], b"SET 1 2\n")

    def test_wrong_serial_state_is_failure(self):
        lamp, _ = self.make_serial([b"STATE 0 1\n", b"STATE 0 2\n"])
        with self.assertRaises(DeviceError):
            lamp.set(True)

    def test_serial_timeout_is_failure(self):
        lamp, port = self.make_serial([b"STATE 0 1\n"])
        port.read_until.side_effect = None
        port.read_until.return_value = b""
        with self.assertRaises(DeviceError):
            lamp.set(True)


if __name__ == "__main__":
    unittest.main()
