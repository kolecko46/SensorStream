#include <DHT11.h>
#include <Ethernet.h>
#include <EthernetUdp.h>
#include <TimeLib.h>
#include <SPI.h>
#include <NTPClient.h>

byte mac[] = {0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED};
IPAddress server(192,168,0,105);
IPAddress ip(192, 168, 0, 101);
EthernetClient client;

DHT11 dht11(4);

EthernetUDP ntpUDP;
NTPClient timeClient(ntpUDP, "pool.ntp.org", 3600, 60000);

void setup() {

  Serial.begin(9600);
  // Initialize Ethernet
  if (Ethernet.begin(mac) == 0) {
    Serial.println("Failed to configure Ethernet using DHCP");
    while (true); // Halt the program if Ethernet initialization fails
  }

  // start the Ethernet connection:
  Ethernet.begin(mac, ip);
  Serial.println(Ethernet.localIP()); 
  delay(1000);
  Serial.print("connecting to ");
  Serial.println(server);
  
  if (client.connect(server, 8000)) {
    Serial.println("Connected to server.");
    
    // Send an HTTP GET request
    client.println("GET /arduino/test HTTP/1.1");
    client.println("Host: 192.168.0.105");
    client.println("Connection: close");
    client.println();
  } else {
    Serial.println("Connection to server failed.");
  }

  dht11.setDelay(300000); 

  timeClient.begin();
}

void loop() {
    int temperature = 0;
    int humidity = 0;
    int result = dht11.readTemperatureHumidity(temperature, humidity);
    setTime(timeClient.getEpochTime());
    
    if (client.connect(server, 8000)) {
      if (result == 0) {
          timeClient.update();
          Serial.print("Temperature: ");
          Serial.print(temperature);
          Serial.print(" °C\tHumidity: ");
          Serial.print(humidity);
          Serial.println(" %");

          String datetime = String(year()) + "." + (month() < 10 ? "0" : "") + String(month()) + "." + (day() < 10 ? "0" : "") + String(day()) + "-" + 
                      (hour() < 10 ? "0" : "") + String(hour()) + ":" + 
                      (minute() < 10 ? "0" : "") + String(minute()) + ":" + 
                      (second() < 10 ? "0" : "") + String(second());
          
          Serial.println(datetime);

          // String body = "temperature=" + String(temperature) + 
          //               "&humidity=" + String(humidity) + 
          //               "&date_time=" + datetime;

          String body = "{\"temperature\":\"" + String(temperature) + 
                        "\",\"humidity\":\"" + String(humidity) + 
                        "\",\"date_time\":\"" + datetime + "\"}";

          Serial.println(body);

          client.println("POST /arduino/dht11 HTTP/1.1");
          client.println("Host: 192.168.0.105");
          client.println("Content-Type: application/json");
          client.println("Connection: close");
          client.print("Content-Length: ");
          client.println(body.length());
          client.println(); // End of headers

          // Send the body
          client.println(body);


      } else {
          // Print error message based on the error code.
          Serial.println(DHT11::getErrorString(result));

        }
    } 
}
