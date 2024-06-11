/*
  This program monitors two digital inputs
  and controls two Tasmota A1T devices
  using Web requests

  Why not controlling directly, without Arduino?
  Because the robot that is the source of the digital signals can't
  send them throgh the web, so Arduino as as mediator

  Circuit:
   * Uno R4 WiFi
   * Tasmota A1T

  Based on
  https://raw.githubusercontent.com/arduino/ArduinoCore-renesas/main/libraries/WiFiS3/examples/WiFiWebClientRepeating/WiFiWebClientRepeating.ino

  Fernando S. Pacheco
  06-2024
 */

#include <WiFiS3.h>
#include "arduino_secrets.h"
/* arduino_secrets.h with the definitions:
#define SECRET_SSID ""
#define SECRET_PASS ""
*/ 

char ssid[] = SECRET_SSID;    // your network SSID (name)
char pass[] = SECRET_PASS;    // your network password (use for WPA, or use as key for WEP)
int status = WL_IDLE_STATUS;  // the WiFi radio's status

// server addresses
IPAddress deviceA(172,28,171,56);
IPAddress deviceB(172,28,171,57);

// digital input pins
int pinA = 6;
int pinB = 7;

// to store the digital input signals
int signalA = 0;
int signalB = 0;
int oldSignalA = 0;
int oldSignalB = 0;

// Initialize the WiFi client library
WiFiClient client;

unsigned long lastConnectionTime = 0;            // last time you connected to the server, in milliseconds
const unsigned long postingInterval = 200L; // delay between updates, in milliseconds

void setup() {
  //Initialize serial and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  Serial.println("Initializing...");
  // check for the WiFi module:
  if (WiFi.status() == WL_NO_MODULE) {
    Serial.println("Communication with WiFi module failed!");
    // don't continue
    while (true);
  }

  String fv = WiFi.firmwareVersion();
  if (fv < WIFI_FIRMWARE_LATEST_VERSION) {
    Serial.println("Please upgrade the firmware");
  }
  // attempt to connect to WiFi network:
  while (status != WL_CONNECTED) {
    Serial.print("Attempting to connect to WPA SSID: ");
    Serial.println(ssid);
    // Connect to WPA/WPA2 network:
    status = WiFi.begin(ssid, pass);

    // wait 10 seconds for connection:
    delay(10000);
  }
  printWifiStatus();

  // initialize the digital inputs
  pinMode(pinA, INPUT);
  pinMode(pinB, INPUT);
}

/* just wrap the received data up to 80 columns in the serial print*/
/* -------------------------------------------------------------------------- */
void read_request() {
/* -------------------------------------------------------------------------- */  
  uint32_t received_data_num = 0;

  while (client.available()) {
    /* actual data reception */
    char c = client.read();
    /* print data to serial port */
    Serial.print(c);
    /* wrap data to 80 columns*/
    received_data_num++;
    if(received_data_num % 80 == 0) { 
    }
  }  
}

/* -------------------------------------------------------------------------- */
void loop() {
/* -------------------------------------------------------------------------- */  
  // if there's incoming data from the net connection.
  // send it out the serial port.  This is for debugging
  // purposes only:
  read_request();
  
  // if some time has passed since last check
  if (millis() - lastConnectionTime > postingInterval) {
    signalA = digitalRead(pinA);
    if (signalA != oldSignalA) {
      // update
      Serial.println("Time to update A");
      httpRequest(deviceA, signalA);
      oldSignalA = signalA;
    }

    signalB = digitalRead(pinB);
    if (signalB != oldSignalB) {
      // update
      Serial.println("Time to update B");
      httpRequest(deviceB, signalB);
      oldSignalB = signalB;
    }
    // note the time that the checking was made:
    lastConnectionTime = millis();
  }

}

// this method makes a HTTP connection to the server:
/* -------------------------------------------------------------------------- */
void httpRequest(IPAddress device, int signal) {
/* -------------------------------------------------------------------------- */  
  // close any connection before send a new request.
  // This will free the socket on the NINA module
  client.stop();

  // if there's a successful connection:
  if (client.connect(device, 80)) {
    Serial.println("connecting...");
    // send the HTTP GET request:
    // Create the URL for the request
    String urlCommand="/cm?cmnd=Power%20";
    if (signal==0) {
      urlCommand = urlCommand + "Off";
    }
    if (signal==1) {
      urlCommand = urlCommand + "On";
    }

    Serial.print("Requesting URL: ");
    Serial.println(device);
    Serial.println(urlCommand);

    // This will send the request to the server
    client.print(String("GET ") + urlCommand + " HTTP/1.1\r\n" +
               "Host: " + device + "\r\n" +
               "Connection: close\r\n\r\n");    
  } else {
    // if you couldn't make a connection:
    Serial.println("connection failed");
  }
}

/* -------------------------------------------------------------------------- */
void printWifiStatus() {
/* -------------------------------------------------------------------------- */  
  // print the SSID of the network you're attached to:
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());

  // print your board's IP address:
  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);

  // print the received signal strength:
  long rssi = WiFi.RSSI();
  Serial.print("signal strength (RSSI):");
  Serial.print(rssi);
  Serial.println(" dBm");
}