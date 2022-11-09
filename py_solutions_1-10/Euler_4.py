# Find the largest palindrome number made from the product of two 3-digit 
# numbers?

from __future__ import print_function

import timeit

try:
    range = xrange
except NameError:
    pass

start = timeit.default_timer()

def euler_4():
    high = 0
    for x in range(100, 1000):
        for y in range(x, 1000):
            product = x * y
            if product < high: continue
            if str(product) == str(product)[::-1]:
                high = product
    return high

print("Answer: {}".format(euler_4()))
stop = timeit.default_timer()
print("Time: {0:9.5f}".format(stop - start))
