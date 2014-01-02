# Find the highest sum of a number's digits for numbers a**b while a and b < 100 

import timeit
import itertools


start = timeit.default_timer()

def euler_56():
    return max([sum(map(int, str(i))) for i in [pow(l[0], l[1]) for l in itertools.product(xrange(100), xrange(100))]])

print "Answer: %s" % euler_56()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
