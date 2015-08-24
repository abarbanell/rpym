#!/usr/bin/python

# code fragment to read the the dht sensor connected on the arduino via usbserial

import serial
import json


ser = serial.Serial('/dev/ttyACM0', 9600)


while 1: 
    msg = ser.readline()
    print 'JSON: ', msg
    res = json.loads(msg)
    print res
    print "HUM: ", res[u"humidity"]
    print "CEL: ", res[u"temperature"]


