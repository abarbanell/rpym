rpym is the Raspberry Python Monitoring tool

It can log data via small python scripts to your statsd server.

See details on my [blog](http://blog.abarbanell.de/raspberry/2015/07/18/Raspberry-Pi-Monitoring-With-Statsd/)

We have twop monitoring scripts: 

- mon.py: to capture system related data like cpu usage, disk usage, and cpu temperature. The first ones work on any Linux like system, the CPU temperature only on a Raspberry Pi.
- mon-dht.py: read the data from a DHT-22 temperature and humidity sensor, which is connected via an arduino on a USB connection. 

The Arduino sketch for this is like this: 

```
// Get humidity (in Percent) and temperature (in Celsius) from DHT22 and output as JSON
// over serial wire
// by Tobias Abarbanell
// Inspired by ladyada, public domain

#include "DHT.h"

#define DHTPIN 2     // what pin we're connected to

// Uncomment whatever type you're using!
//#define DHTTYPE DHT11   // DHT 11
#define DHTTYPE DHT22   // DHT 22  (AM2302)
//#define DHTTYPE DHT21   // DHT 21 (AM2301)

// Connect pin 1 (on the left) of the sensor to +5V
// NOTE: If using a board with 3.3V logic like an Arduino Due connect pin 1
// to 3.3V instead of 5V!
// Connect pin 2 of the sensor to whatever your DHTPIN is
// Connect pin 4 (on the right) of the sensor to GROUND
// Connect a 10K resistor from pin 2 (data) to pin 1 (power) of the sensor

// Initialize DHT sensor.
// Note that older versions of this library took an optional third parameter to
// tweak the timings for faster processors.  This parameter is no longer needed
// as the current DHT reading algorithm adjusts itself to work on faster procs.
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);

  dht.begin();
}

void loop() {
  // Wait a few seconds between measurements.
  delay(2000);

  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  float h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();


  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t) ) {
    Serial.println("{ \"err\": \"Failed to read from DHT sensor!\" }");
    return;
  }




  Serial.print("{\"humidity\": ");
  Serial.print(h);
  Serial.print(", ");
  Serial.print("\"temperature\": ");
  Serial.print(t);
  Serial.println("}");
}
```


