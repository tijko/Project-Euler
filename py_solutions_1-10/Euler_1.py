## sum of all multiples of 3 and 5 below 1000? ##

import timeit


start = timeit.default_timer()

def euler_1():
    return sum([i for i in xrange(1, 1000) if i % 3 == 0 or i % 5 == 0])

print "Answer: %s" % euler_1()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
