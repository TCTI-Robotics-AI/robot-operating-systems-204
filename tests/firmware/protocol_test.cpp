#include <cassert>
#include <deque>
#include <string>
#include "led_protocol.h"
class TestStream : public Stream {
 public:
  std::deque<char> input;
  std::string output;
  int available() override { return static_cast<int>(input.size()); }
  int read() override { char value = input.front(); input.pop_front(); return value; }
  size_t write(uint8_t value) override { output += static_cast<char>(value); return 1; }
  void receive(const std::string& value) { for (char c : value) input.push_back(c); }
};
int main() {
  TestStream stream;
  LedProtocol protocol(stream, 13);
  protocol.begin();
  assert(outputValue == LOW);
  stream.receive("SET 1 "); protocol.poll(); assert(outputValue == LOW);
  stream.receive("1\nGET 2\n"); protocol.poll();
  assert(outputValue == HIGH);
  assert(stream.output == "STATE 1 1\r\nSTATE 1 2\r\n");
  stream.output.clear();
  stream.receive("SET 0 3 extra\nSET 0 0\nSET 0 2147483648\n"); protocol.poll();
  assert(outputValue == HIGH);
  assert(stream.output == "ERR command\r\nERR command\r\nERR command\r\n");
  stream.output.clear();
  stream.receive(std::string(80, 'X') + "\nSET 0 4\n"); protocol.poll();
  assert(outputValue == LOW);
  assert(stream.output == "ERR length\r\nSTATE 0 4\r\n");
  stream.output.clear();
  stream.receive(std::string("SET 1 5\0junk\n", 13)); protocol.poll();
  assert(outputValue == LOW);
  protocol.resetInput();
  protocol.feed('G'); protocol.feed('E'); protocol.feed('T');
  protocol.feed(' '); protocol.feed('6'); protocol.feed('\n');
  assert(stream.output.find("STATE 0 6\r\n") != std::string::npos);
}
