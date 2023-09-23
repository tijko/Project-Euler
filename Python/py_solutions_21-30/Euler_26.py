# Largest sequence of repeating numbers of n < 1000 of 1/d

from __future__ import print_function

import timeit
import math

try:
    range = xrange
except NameError:
    pass

start = timeit.default_timer()

def is_prime(x):
    if x == 2:
        return True
    if x % 2 == 0 or x == 1:
        return False
    for i in range(3, int(math.sqrt(x) + 1), 2):
        if x % i == 0:
            return False
    return True


def euler_26():
    primes_to_onethousand = list(filter(is_prime, range(1, 1000)))
    return primes_to_onethousand[len(primes_to_onethousand) - 3]


print("Answer: {}".format(euler_26()))
stop = timeit.default_timer()
print("Time: {0:9.5f}".format(stop - start))
