# Find the product of the coefficients, a and b, for the quadratic 
# expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

from __future__ import print_function

import math
import timeit
import itertools

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
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True


def euler_27():
    max_primes = 0
    quadratic = lambda x, y, z: x**2 + (x * y) + z
    for i, v in itertools.product(range(-999, 1000), range(-999, 1000)):
        primes = 0
        q = quadratic(primes, v, i) 
        while is_prime(abs(q)):
            primes += 1
            q = quadratic(primes, v, i)
        if primes > max_primes:
            max_primes = primes
            co_prod =  i * v
    return co_prod


print("Answer: {}".format(euler_27()))
stop = timeit.default_timer()
print("Time: {0:9.5f}".format(stop - start))
