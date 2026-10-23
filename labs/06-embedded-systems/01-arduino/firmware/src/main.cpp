#include <Arduino.h>
#include "led_protocol.h"
LedProtocol protocol(Serial, LED_BUILTIN);
void setup() { Serial.begin(115200); protocol.begin(); }
void loop() { protocol.poll(); }
