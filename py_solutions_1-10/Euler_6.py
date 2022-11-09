# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum? 

from __future__ import print_function

import timeit

try:
    range = xrange
except NameError:
    pass

start = timeit.default_timer()

def euler_6():
    return sum(range(1, 101))**2 - sum(map(lambda x: x**2, range(1, 101)))

print("Answer: {}".format(euler_6()))
stop = timeit.default_timer()
print("Time: {0:9.5f}".format(stop - start))
