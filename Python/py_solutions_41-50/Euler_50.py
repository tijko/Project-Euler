#!/usr/bin/env python
# -*- coding: utf-8 -*-

# prime under a million that is the biggest of the sum of the most consecutive primes 

from __future__ import print_function
import math
import timeit


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
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

def euler_50():
    high = 0
    top = 0
    primes = [i for i in range(3944) if is_prime(i)]
    for prime in primes:
        total = 0
        for i in range(primes.index(prime), len(primes)):
            total += primes[i]
            if is_prime(total):
                if high < primes.index(primes[i]) - primes.index(prime):
                    high = primes.index(primes[i]) - primes.index(prime) 
                    top = total
    return top

print("Answer: %s" % euler_50())
stop = timeit.default_timer()
print("Time: %f" % (stop - start))    
