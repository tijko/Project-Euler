#!/usr/bin/env python
# -*- coding: utf-8 -*-

# smallest prime for which replacing part of the number you can form 8 different primes 
# Example: 189-00-37, 189-33-37, 189-44-37, 189-55-37, 189-66-37, 189-77-37, 189-88-37, 189-99-37 
# the replacement digits do not have to be adjacent or consecutive but, have to be the same 

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
    if x == 1 or x % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

def prime_gen():
    replace_number = 10000
    repeats = lambda x: any(x.count(v) > 2 for v in x)
    while True:
        if is_prime(replace_number) and repeats(str(replace_number)): 
            yield str(replace_number)
        replace_number += 1    

def prime_replace(prime):
    for i in prime:
        if sum([1 for v in range(1, 10) if 
                is_prime(int(prime.replace(i, str(v))))]) > 7:
            return True
    return False
        
def euler_51():
    primes = prime_gen()
    while True:
        prime = next(primes)
        if any(prime.count(i) > 2 for i in prime) and prime_replace(prime):
            return prime

print("Answer: %s" % euler_51())
stop = timeit.default_timer()
print("Time: %s" % str(stop - start))
