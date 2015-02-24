# what is the sum of the digits 2**1000 ? 

from __future__ import print_function

import timeit


start = timeit.default_timer()

def euler_16():
    return sum(map(int, str(2**1000)))

print("Answer: {}".format(euler_16()))
stop = timeit.default_timer()
print("Time: {0:9.5f}".format(stop - start))
