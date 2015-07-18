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

host = os.uname()[1]
cpu = psutil.cpu_percent(interval=1)

c = statsd.StatsClient('statsd', 8125, prefix=host)

c.incr('heartbeat')

c.gauge('cpu.percent', cpu)
 


