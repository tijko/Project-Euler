# Calculate the sum of all amicable pairs below 10000 

from __future__ import print_function

import timeit
import functools

try:
    range = xrange
except NameError:
    pass

start = timeit.default_timer()

def mod_zero(dividend, divisor):
    return True if dividend % divisor == 0 else False

def euler_21():
    total = 0
    for i in range(1, 10000):
        p1 = sum(filter(functools.partial(mod_zero, i), range(1, i // 2 + 1)))  
        p2 = sum(filter(functools.partial(mod_zero, p1), range(1, p1 // 2 + 1)))
        if p2 == i != p1: 
            total += i
    return total


print("Answer: {}".format(euler_21()))
stop = timeit.default_timer()
print("Time: {0:9.5f}".format(stop - start))
