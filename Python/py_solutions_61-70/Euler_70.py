#!/usr/bin/env python
# -*- coding: utf-8 -*-

# permutations of eulers totient function

from __future__ import print_function

import math
import timeit
import operator
import itertools

try:
    range = xrange
except NameError:
    pass

start = timeit.default_timer()

def is_prime(x):
    if x == 2:
        return True
    if x == 1 or x % 2 == 0:
        return False
    for i in range(3,int(math.sqrt(x)) + 1,2):
        if x % i == 0:
            return False
    return True

def build_primes(limit):
    return [i for i in xrange(2, limit + 1) if is_prime(i)]

def build_canidates(start, end, primes):
    divisors = filter(lambda x: {x} & primes, range(start, end))
    canidates = []
    for i in itertools.combinations(divisors, 2):
        product = reduce(operator.imul, i)
        if product < 10**7:
            canidates.append(product)
    return canidates

def calculate_phi(n, primes):
    base = n
    for i in primes:
        if base % i == 0:
            n *= (1 - (1 / float(i)))
    return n

def euler_70():
    primes = build_primes(10000)
    canidates = build_canidates(1000, 10000, set(primes))
    low_phi, low = 10**7, 0
    for n in canidates:
        factor = int(math.sqrt(n))
        phi = calculate_phi(n, primes[:factor])
        if sorted(str(n)) == sorted(str(int(phi))):
            if n / phi < low_phi:
                low_phi, low = n / phi, n
    return low

if __name__ == '__main__':
    print("Answer: %s" % euler_70())
    stop = timeit.default_timer()
    print("Time: %f" % (stop - start))

