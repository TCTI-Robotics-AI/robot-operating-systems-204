#include <Arduino.h>
#include <SPI.h>
#include <WiFiST.h>
#include <WiFiServerST.h>
#include <WiFiClientST.h>
#include "led_protocol.h"
#if __has_include("secrets.h")
#include "secrets.h"
#else
#include "secrets.example.h"
#endif

// Board-specific wiring of the onboard ISM43362 module (B-L475E-IOT01A).
SPIClass courseSPI(PC12, PC11, PC10);
WiFiClass WiFi(&courseSPI, PE0, PE1, PE8, PB13);
WiFiServer server(8766);
WiFiClient client;
// This Wi-Fi driver always returns 1 from available(). Use bulk reads instead
// of Stream polling, and send a complete acknowledgement in one Wi-Fi write.
class ReplyStream : public Stream {
 public:
  uint8_t data[64];
  size_t length = 0;
  int available() override { return 0; }
  int read() override { return -1; }
  int peek() override { return -1; }
  void flush() override {}
  size_t write(uint8_t value) override {
    if (length >= sizeof(data)) return 0;
    data[length++] = value;
    return 1;
  }
};
ReplyStream replies;
LedProtocol protocol(replies, LED_BUILTIN);
char courseSSID[] = COURSE_WIFI_SSID;
char coursePassword[] = COURSE_WIFI_PASSWORD;

void setup() {
  Serial.begin(115200);
  protocol.begin();
  while (WiFi.begin(courseSSID, coursePassword) != WL_CONNECTED) {
    Serial.println("Waiting for lab Wi-Fi");
    delay(10000);
  }
  Serial.print("STM32 address: ");
  Serial.println(WiFi.localIP());
  server.begin();
}

void loop() {
  client = server.available();
  if (!client) { delay(10); return; }
  protocol.resetInput();
  replies.length = 0;
  const uint32_t started = millis();
  while (client.connected() && static_cast<uint32_t>(millis() - started) < 3000) {
    uint8_t incoming[65] = {};
    const int received = client.read(incoming, 64);
    for (int index = 0; index < received; ++index) protocol.feed(static_cast<char>(incoming[index]));
    if (replies.length) {
      client.write(replies.data, replies.length);
      break;
    }
  }
  client.stop();
  server.begin();
}
