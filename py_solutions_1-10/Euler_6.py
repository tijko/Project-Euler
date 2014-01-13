# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum? 

import timeit


start = timeit.default_timer()

def euler_6():
    return sum(xrange(1, 101))**2 - sum(map(lambda x: x**2, xrange(1, 101)))

print "Answer: %s" % euler_6()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
