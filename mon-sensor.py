#!/usr/bin/python

# monitoring script to send off sensor data from DHT22 sensor  to statsd.
# this should be called from crontab loke this: 
# 
# m h  dom mon dow   command
# * * * * * $HOME/github/abarbanell/rpym/mon-sensor.py
#
# this expects the statsd server listed in the /etc/hosts table like this: 
#
# 192.160.100.100 statsd
#


import statsd
import serial
import json
import os

# setup
host = os.uname()[1]
ser = serial.Serial('/dev/ttyACM0', 9600)

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

