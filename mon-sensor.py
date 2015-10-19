#!/usr/bin/python

# monitoring script to send off sensor data from DHT22 sensor  to statsd and limitless-garden.
# this should be called from crontab loke this: 
# 
# m h  dom mon dow   command
# * * * * * THREESCALE_USER_KEY=your_key_here $HOME/github/abarbanell/rpym/mon-sensor.py
#
# this expects the statsd server listed in the /etc/hosts table like this: 
#
# 192.160.100.100 statsd
#
# this version is for an Arduino Micro (connected as /dev/ttyACM0) which should be running this sketch: 
#
# https://github.com/abarbanell/arduino-sensor/tree/master/sensor-json
#
# this will be continualy sending measurement data every 2 sec but we only read in intervals given by crontab, so most measurements are lost.



import statsd
import serial
import json
import os
import time
import requests
import datetime

# setup
host = os.uname()[1]
ser = serial.Serial('/dev/ttyACM0', 9600)
# if we want to send commands we need to first wait for the Arduino to reset, otherwise the sent data will be lost.
# not a problem here since we are only ready when ready.
# time.sleep(2)

# get data 
msg = ser.readline()
res = json.loads(msg)
humidity = res[u"humidity"]
celsius = res[u"temperature"]
soil = res[u"soil"]

# send data
c = statsd.StatsClient('statsd', 8125, prefix=host)

c.gauge('sensor.humidity', humidity)
c.gauge('sensor.celsius', celsius)
c.gauge('sensor.soil', soil)


# send data to limitless-garden (and ignore result) 
url='http://limitless-garden-9668.herokuapp.com/api/collections/sensor'
querypayload={'user_key': os.getenv('THREESCALE_USER_KEY')};

res[u"host"] = host;
res[u"sensor"] = ['soil', 'humidity', 'temperature'];
res[u"timestamp"] = datetime.datetime.utcnow().isoformat();

r = requests.post(url, params=querypayload, json=res)



