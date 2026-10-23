// Minimal host test double for the protocol, not a microcontroller emulator.
#pragma once
#include <cstddef>
#include <cstdint>
#include <string>
constexpr int OUTPUT = 1, HIGH = 1, LOW = 0;
inline int outputValue = LOW;
inline void pinMode(uint32_t, int) {}
inline void digitalWrite(uint32_t, int value) { outputValue = value; }
inline int digitalRead(uint32_t) { return outputValue; }
class Stream {
 public:
  virtual int available() = 0;
  virtual int read() = 0;
  virtual size_t write(uint8_t) = 0;
  void print(const char* value) { while (*value) write(static_cast<uint8_t>(*value++)); }
  void print(int value) { print(std::to_string(value).c_str()); }
  void print(char value) { write(static_cast<uint8_t>(value)); }
  void println(unsigned long value) { print(std::to_string(value).c_str()); print("\r\n"); }
  void println(const char* value) { print(value); print("\r\n"); }
};
