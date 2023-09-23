#!/usr/bin/env python
# -*- coding: utf-8 -*-

# composite odd numbers that aren't the sum of a prime twice a square 

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
    for i in range(3, int(math.sqrt(x))+1, 2):
        if x % i == 0:
            return False
    return True

def composite_gen():
    composite = 2
    while True:
        if composite % 2 != 0 and not is_prime(composite):
            yield composite
        composite += 1

def composite_chk(comp, twice_sq, primes):
    for sq in twice_sq:
        for prime in primes:
            if sq + prime == comp:
                return False
    return True

def euler_46():   
    cg = composite_gen() 
    while True:
        composite = next(cg) 
        twice_sq = (2 * v**2 for v in range(int(math.sqrt(composite))))
        primes = [k for k in range(composite + 1) if is_prime(k)]
        if composite_chk(composite, twice_sq, primes): return composite        


print("Answer: %s" % euler_46())
stop = timeit.default_timer()
print("Time: %f" % (stop - start))
