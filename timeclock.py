#The method clock() returns the current processor time as a floating point number expressed in seconds on Unix.
#The precision depends on that of the C function of the same name, but in any case, this is the function to use for
#benchmarking Python or timing algorithms

#!/usr/bin/python
import time
def procedure():
    time.sleep(2.5)

# measure process time

t0 = time.clock()
procedure()
print (time.clock() - t0, "seconds process time")

# measure wall time

t0 = time.time()
procedure()
print (time.time() - t0, "seconds wall time")
