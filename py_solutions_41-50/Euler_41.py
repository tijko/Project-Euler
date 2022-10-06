#!/usr/bin/env python
# -*- coding: utf-8 -*-

# largest prime pan-digital number 

from __future__ import print_function

import timeit
import math
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

def euler_41():
    pandigital = '987654321'
    while True:
        primes = [i for i in itertools.permutations(pandigital) if
                     is_prime(int(''.join(i)))]
        if primes:
            return ''.join(max(primes))
        pandigital = pandigital[1:]                    

print("Answer: %s" % euler_41())
stop = timeit.default_timer()
print("Time: %f" % (stop - start))
