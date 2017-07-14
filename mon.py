#!/usr/bin/python

# monitoring script to send off some system stats to statsd.
# this should be called from crontab like this: 
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
import subprocess

# get data 
host = os.uname()[1]
rasp = ('armv' in os.uname()[4])

cpu = psutil.cpu_percent(interval=1)
if rasp:
    f = open('/sys/class/thermal/thermal_zone0/temp', 'r')
    l = f.readline()
    temp = 1.0 * float(l)/1000
usage = psutil.disk_usage("/")
mem = psutil.virtual_memory()

# open and max files 
fds = subprocess.check_output(["sysctl", "-n", "fs.file-nr"]);
fdarr = [int(s) for s in fds.split() if s.isdigit()]
 

# send data
c = statsd.StatsClient('statsd', 8125, prefix=host)

c.incr('heartbeat')
c.gauge('cpu.percent', cpu)

if rasp:
    c.gauge('cpu.temp', temp)

c.gauge('disk.root.total', usage.total)
c.gauge('disk.root.used', usage.used)
c.gauge('disk.root.free', usage.free)
c.gauge('disk.root.percent', usage.percent)
c.gauge('mem.percent', mem.percent) 
c.gauge('files.open', fdarr[0])
c.gauge('files.max', fdarr[2])
