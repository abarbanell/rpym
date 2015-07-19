#!/usr/bin/python

# code fragment to read the disk percentage and print as float and integer 

import psutil


print 'get disk usage in MB'

usage = psutil.disk_usage("/")
print "{:.1f} MB".format(float(usage.total) / 1024/1024)
print "{:.1f} MB".format(float(usage.free) / 1024 / 1024)
print "{:.1f} MB".format(float(usage.used) / 1024 / 1024)

print 'and in percent'
print usage.percent

