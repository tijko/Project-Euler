# find all paths in 20 X 20 grid

from math import factorial
import timeit


start = timeit.default_timer()

def euler_15():
    return (factorial(40) / (factorial(20) * factorial(20)))

print "Answer: %s" % euler_15()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
