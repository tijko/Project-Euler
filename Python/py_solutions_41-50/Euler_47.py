#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Find the first of the four consecutive integers to have four distinct prime factors.

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
    if x % 2 == 0 or x == 1:
        return False
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

def comp_gen():
    composite = 10 
    while True:
        if not is_prime(composite):
            yield composite
        composite += 1
 
def prime_gen(comp, p):
    comp_range = (i for i in p if comp % i == 0)
    while comp_range:
        yield next(comp_range)

def four_factors(comp, p_gen):
    factors = 0
    while factors < 4:
        try:
            curr_gen = next(p_gen)
            if comp % curr_gen == 0:
                factors += 1
        except RuntimeError:
            return False
    return True

def euler_47():
    consecutive = 0
    prev_comp = 0
    comp = comp_gen()
    primes = [i for i in range(2, 5000) if is_prime(i)]
    while consecutive < 4:
        cur_comp = next(comp)
        p_gen = prime_gen(cur_comp, primes)
        if four_factors(cur_comp, p_gen) and cur_comp - 1 == prev_comp:
            consecutive += 1
        else:
            consecutive = 0
        prev_comp = cur_comp
    return cur_comp - 3                                     

print("Answer: %d" % euler_47())
stop = timeit.default_timer()
print("Time: %f" % (stop - start))
