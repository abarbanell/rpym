#!/usr/bin/python

# code fragment to read the cpu percentage and print as float and integer 

import psutil
import os

host = os.uname()[1]

rasp = ('armv' in os.uname()[4])

print 'get CPU usage in Percent'

cpu = psutil.cpu_percent(interval=1)
print cpu
icpu = int(round(cpu))
print icpu

if rasp:
    print 'Raspberry: get CPU temperatur in C'
    f = open('/sys/class/thermal/thermal_zone0/temp', 'r')
    l = f.readline()
    print l
    temp = 1.0 * float(l)/1000
    print "{:.2f} C".format(temp)
else:
    print 'Not a Raspberry, no CPU temperature' 


