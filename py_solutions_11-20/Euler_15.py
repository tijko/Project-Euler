# find all paths in 20 X 20 grid

import math
import timeit


start = timeit.default_timer()

def euler_15():
    new = math.factorial(40)
    return (new / (math.factorial(20) * math.factorial(20)))

print "Answer: %s" % euler_15()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
