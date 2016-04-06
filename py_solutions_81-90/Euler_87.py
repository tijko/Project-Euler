#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
The smallest number expressible as the sum of a prime square, prime cube, and 
prime fourth power is 28. In fact, there are exactly four numbers below fifty 
that can be expressed in such a way:

28 = 22 + 23 + 24
33 = 32 + 23 + 24
49 = 52 + 23 + 24
47 = 22 + 33 + 24

How many numbers below fifty million can be expressed as the sum of a prime 
square, prime cube, and prime fourth power?
'''

from __future__ import print_function

import timeit
from math import sqrt

try:
    range = xrange
except NameError:
    pass


def is_prime(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0: return False
    return True

def euler_87():
    limit = 10**7 * 5
    sum_set = set()
    primes = list(filter(is_prime, range(2, int(sqrt(limit) + 1))))
    for x in primes:
        for y in primes:
            x_y = x**2 + y**3
            if x_y >= limit:
                break
            for z in primes:
                x_y_z = x_y + z**4
                if x_y_z < limit:
                    sum_set.add(x_y_z)
                else:
                    break
    return len(sum_set)

if __name__ == '__main__':
    start = timeit.default_timer()
    print('Answer: {}'.format(euler_87()))
    stop = timeit.default_timer()
    print('Time: {0:9.5f}'.format(stop - start))
