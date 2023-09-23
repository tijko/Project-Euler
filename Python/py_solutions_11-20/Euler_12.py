# What is the value of the first triangle number to have over five-hundred divisors?

from __future__ import print_function

import math
import timeit
import sys


try:
    range = xrange
except NameError:
    pass

sys.setrecursionlimit(15000)
start = timeit.default_timer()

def factor_gen(tri):
    for i in range(2, int(math.sqrt(tri)) + 1):
        if tri % i == 0:
            yield i

def euler_12(n, tri):
    if sum([2 for i in factor_gen(tri)]) + 2 > 500:
        return tri
    return euler_12(n + 1, sum([tri, n, 1]))

print("Answer: {}".format(euler_12(1001, sum(range(1002)))))
stop = timeit.default_timer()
print("Time: {0:9.5f}".format(stop - start))
