#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Euler's Totient Function 

from __future__ import print_function, division

import math
import timeit


try:
    range = xrange
except NameError:
    pass

def is_prime(x):
    if x == 2:
        return True
    if x % 2 == 0 or x == 1:
        return False
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

def build_primes_list(limit):
    return list(filter(is_prime, range(2, limit)))

def calculate_phi(phi, primes):
    base = phi
    for v in primes:
        if base % v == 0:
            phi *= (1 - (1 / v))
    return phi

def euler_69():
    high, high_phi = 0, 0
    limit = 1000001
    primes_list = build_primes_list(int(math.sqrt(limit)) + 1)
    for i in range(2, limit):
        prime_factor = int(math.sqrt(i)) 
        phi = calculate_phi(i, primes_list[:prime_factor])
        current = i / phi
        if current > high_phi:
            high_phi, high = (current, i)
    return high

if __name__ == '__main__':
    start = timeit.default_timer()
    print('Answer: {}'.format(euler_69()))
    stop = timeit.default_timer()
    print('Time: {0:9.5f}'.format(stop - start))
