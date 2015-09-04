#!/usr/bin/python
#Time intervals are floating-point numbers in units of seconds. Particular instants in time are expressed in seconds
#since 12:00am, January 1, 1970(epoch).

import time; # This is required to include time module.
ticks = time.time()

#The function time.time() returns the current system time in ticks since
#12:00am, January 1, 1970(epoch)
print ("Number of ticks since 12:00am, January 1, 1970:", ticks)

localtime = time.localtime(time.time())
print ("Local current time :", localtime)

#formated time using asctime
localtimenext = time.asctime( time.localtimenext(time.time()) )
print ("Local current time :", localtimenext)
