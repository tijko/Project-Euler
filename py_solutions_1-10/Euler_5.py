# What is the smallest number that can be divided evenly by all the numbers from 1-20?  

import timeit

from functools import partial
from operator import mod 


start = timeit.default_timer()

def euler_5():
    dividend = 20
    divisors = xrange(1, 21)
    while True:
        if (dividend % 7 != 0 or dividend % 9 != 0 or dividend % 3 != 0 or
            sum(map(partial(mod, dividend), divisors)) != 0):
            dividend += 20
        else:
            return dividend

print "Answer: %s" % euler_5()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
