#pragma once
#include <Arduino.h>
#include <stdio.h>
#include <string.h>

// ASCII protocol, bounded buffer, no dynamic allocation. Output is the onboard LED.
class LedProtocol {
 public:
  explicit LedProtocol(Stream& serial, uint32_t led) : serial_(serial), led_(led) {}
  void begin() { pinMode(led_, OUTPUT); digitalWrite(led_, LOW); }
  void resetInput() { length_ = 0; overflow_ = false; }
  void poll() {
    while (serial_.available()) {
      feed(static_cast<char>(serial_.read()));
    }
  }
  void feed(char c) {
      if (c == '\r') return;
      if (c == '\n') {
        if (!overflow_) { buffer_[length_] = '\0'; execute(); }
        else serial_.println("ERR length");
        length_ = 0; overflow_ = false;
      } else if (c >= 32 && c <= 126 && length_ < sizeof(buffer_) - 1 && !overflow_) {
        buffer_[length_++] = c;
      } else { overflow_ = true; }
  }
 private:
  void execute() {
    unsigned long seq = 0;
    int requested = 0, end = 0;
    bool valid = false;
    if (sscanf(buffer_, "SET %d %lu%n", &requested, &seq, &end) == 2 &&
        end == static_cast<int>(strlen(buffer_)) && (requested == 0 || requested == 1) && seq > 0 && seq < 2147483648UL) {
      state_ = requested == 1; digitalWrite(led_, state_ ? HIGH : LOW); valid = true;
    } else {
      end = 0;
      valid = sscanf(buffer_, "GET %lu%n", &seq, &end) == 1 &&
              end == static_cast<int>(strlen(buffer_)) && seq > 0 && seq < 2147483648UL;
    }
    if (!valid) { serial_.println("ERR command"); return; }
    serial_.print("STATE "); serial_.print(digitalRead(led_) == HIGH ? 1 : 0);
    serial_.print(' '); serial_.println(seq);
  }
  Stream& serial_;
  uint32_t led_;
  char buffer_[40] = {};
  size_t length_ = 0;
  bool overflow_ = false;
  bool state_ = false;
};
