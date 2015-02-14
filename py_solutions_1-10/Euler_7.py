# What is the 10001st prime number?

from __future__ import print_function

import math
import timeit

try:
    range = xrange
except NameError:
    pass

start = timeit.default_timer()

def is_prime(n):
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n) + 1), 2):
        if n % i == 0:
            return False
    return True

def prime_gen():
    number_prime = n = 0
    while number_prime < 10001:
        if is_prime(n):
            number_prime += 1
            yield n
        n += 1

def euler_7():
    return [i for i in prime_gen()][-1]

print("Answer: {}".format(euler_7()))
stop = timeit.default_timer()
print("Time: {0:9.5f}".format(stop - start))    
