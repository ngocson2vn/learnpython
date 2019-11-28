#!/usr/bin/env python3

import sys, time

#log = open('/tmp/clock.log', 'w')
log = sys.stdout

while True:
    log.write(time.strftime("%H:%M:%S") + "\n")
    log.flush()
    time.sleep(3)
