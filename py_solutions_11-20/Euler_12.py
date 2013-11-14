# What is the value of the first triangle number to have over five-hundred divisors?

import math
import timeit
import sys


sys.setrecursionlimit(15000)
start = timeit.default_timer()

def euler_12(num):
    divisors = 2 
    tri = sum(xrange(1, num + 1))
    for i in xrange(2, int(math.sqrt(tri)) + 1):
        if tri % i == 0:
            divisors += 2
            if divisors > 500:
                return tri
    return euler_12(num + 1)

print "Answer: %s" % euler_12(1001)
stop = timeit.default_timer()
print ("Time: %f" % (stop - start))
