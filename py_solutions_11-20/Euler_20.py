# find the sum of the digits in !100 ? 

from __future__ import print_function

import math
import timeit


start = timeit.default_timer()

def euler_20():
    return sum(map(int, str(math.factorial(100))))

print("Answer: {}".format(euler_20()))
stop = timeit.default_timer()
print("Time: {0:9.5f}".format(stop - start))

