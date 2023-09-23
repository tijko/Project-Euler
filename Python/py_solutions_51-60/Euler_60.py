#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Find lowest sum of set of five primes, that any two can be joined to form a 
# prime in any order.

from __future__ import print_function

import math
import itertools
import timeit

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

def prime_combos(canidates):
    for i in itertools.combinations(canidates, 2):
        if not is_prime(int(i[0] + i[1])) or not is_prime(int(i[1] + i[0])):
            return False    
    return True

def euler_60(primes=None, combos=None):
    if not combos:
        primes = [w for w in range(7, 10000) if is_prime(w)]
        for i in primes:
            combos = euler_60(primes[primes.index(i) + 1:], [str(i)])         
            if len(combos) == 5:
                return sum(map(int, combos))
    else:
        for j in primes:
            if prime_combos(combos + [str(j)]):
                if len(combos + [str(j)]) == 5:
                    combos.append(str(j))
                    return combos
                combos = euler_60(primes[primes.index(j) + 1:], 
                                      combos + [str(j)])
            if len(combos) == 5:
                return combos
        combos.pop(-1)
        return combos 

print("Answer: %s" % euler_60())
stop = timeit.default_timer()
print("Time: %f" % (stop - start))
