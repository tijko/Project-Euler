# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

from __future__ import print_function

import timeit
from itertools import takewhile

try:
    range = xrange
except NameError:
    pass

start = timeit.default_timer()

def grid(step, axis):
    total = step
    for i in takewhile(lambda x: x + step < axis[-1], axis):
        step += i
        total += step                        
    return total

 
def euler_28():
    diag = 3
    total = sum(map(lambda x: x**2, range(1, 1002, 2)))
    for i in range(10, 15, 2):
        total += grid(diag, range(i, 1002002, 8))
        diag += 2
    return total


print("Answer: {}".format(euler_28()))
stop = timeit.default_timer()
print("Time: {0:9.5f}".format(stop - start))
