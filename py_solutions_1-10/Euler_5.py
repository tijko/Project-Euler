# What is the smallest number that can be divided evenly by all the numbers from 1-20?  

from __future__ import print_function

import timeit

from functools import partial
from operator import mod 

try:
    range = xrange
except NameError:
    pass

start = timeit.default_timer()

def euler_5():
    dividend = 20
    divisors = range(1, 21)
    while True:
        if (dividend % 7 != 0 or dividend % 9 != 0 or dividend % 3 != 0 or
            sum(map(partial(mod, dividend), divisors)) != 0):
            dividend += 20
        else:
            return dividend

print("Answer: {}".format(euler_5()))
stop = timeit.default_timer()
print("Time: {0:9.5f}".format(stop - start))
