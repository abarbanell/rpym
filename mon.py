#!/usr/bin/python

# monitoring script to send off some system stats to statsd.
# this should be called from crontab loke this: 
# 
# m h  dom mon dow   command
# * * * * * $HOME/github/abarbanell/rpym/mon.py
#
# this expects the statsd server listed in the /etc/hosts table like this: 
#
# 192.160.100.100 statsd
#


import statsd
import os
import psutil

# get data 
host = os.uname()[1]
cpu = psutil.cpu_percent(interval=1)
f = open('/sys/class/thermal/thermal_zone0/temp', 'r')
l = f.readline()
temp = 1.0 * float(l)/1000
usage = psutil.disk_usage("/")
 

# send data
c = statsd.StatsClient('statsd', 8125, prefix=host)

c.incr('heartbeat')
c.gauge('cpu.percent', cpu)
c.gauge('cpu.temp', temp)
c.gauge('disk.root.total', usage.total)
c.gauge('disk.root.used', usage.used)
c.gauge('disk.root.free', usage.free)
c.gauge('disk.root.percent', usage.percent)
 

