# The last ten-digits of the sum of series 1**1 + 2**2 + 3**3 ..... + 1000**1000 

import timeit


start = timeit.default_timer()

def euler_48():
    pwrofself = lambda x: x**x
    return str(sum(map(pwrofself, xrange(1001))))[-10:]

print "Answer: %s" % euler_48()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
