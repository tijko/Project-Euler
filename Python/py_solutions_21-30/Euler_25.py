# What is the first fibonacci number to have 1000 digits in it? 

from __future__ import print_function

import timeit
import sys


sys.setrecursionlimit(10000)
start = timeit.default_timer()

def euler_25(x, y):
    if len(str(x)) >= 1000: return 0 
    return euler_25((x << 1) + y, x + y) + 2


print("Answer: {}".format(euler_25(1, 0)))
stop = timeit.default_timer()
print("Time: {0:9.5f}".format(stop - start))
