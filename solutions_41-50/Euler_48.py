## The last ten-digits of the sum of series 1**1 + 2**2 + 3**3 ..... + 1000**1000 ##

import timeit

start = timeit.default_timer()

def euler_48():
    return str(sum([i**i for i in range(1,1001)]))[-10:]

print "Answer: %s" % euler_48()
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)
