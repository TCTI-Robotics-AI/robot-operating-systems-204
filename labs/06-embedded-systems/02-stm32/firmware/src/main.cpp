#include <Arduino.h>
#include "led_protocol.h"
// USART2 PA3 RX / PA2 TX connects to ST-LINK VCP on the reference MB1136 board.
HardwareSerial CourseSerial(PA3, PA2);
LedProtocol protocol(CourseSerial, LED_BUILTIN);
void setup() { CourseSerial.begin(115200); protocol.begin(); }
void loop() { protocol.poll(); }
