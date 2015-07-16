#!/usr/bin/python

import statsd
c = statsd.StatsClient('statsd', 8125)
c.incr('foo')

