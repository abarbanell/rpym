#!/usr/bin/python

# code fragment to read the cpu percentage and print as float and integer 

import psutil

cpu = psutil.cpu_percent(interval=1)
print cpu
icpu = int(round(cpu))
print icpu

 


