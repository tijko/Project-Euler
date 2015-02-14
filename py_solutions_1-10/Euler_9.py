# Find the only pythagorean triplet that a + b + c = 1000 

from __future__ import print_function

import math
import timeit

try:
    range = xrange
except NameError:
    pass

start = timeit.default_timer()

def euler_9():
    for a in range(1, 3000):
        b = a + 1
        for b in range(b, 3000):
            c = sum([a, b, (math.sqrt(a**2 + b**2))])
            if c == 1000:
                return int(a * b * (math.sqrt(a**2 + b**2)))
            elif c > 1000:
                break

print('Answer: {}'.format(euler_9()))
stop = timeit.default_timer()
print('Time: {0:9.5f}'.format(stop - start))
