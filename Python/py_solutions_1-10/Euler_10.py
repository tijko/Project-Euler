#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Find the sum of all the primes below two million. 

from __future__ import print_function

from math import sqrt
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
    for i in range(3, int(sqrt(n) + 1), 2):
        if n % i == 0:
            return False
    return True

def prime_gen_under_two_mil():
    n = 0
    while n < 2000000:
        if is_prime(n): yield n
        n += 1

def euler_10():
    return sum([i for i in prime_gen_under_two_mil()])

print('Answer: {}'.format(euler_10()))
stop = timeit.default_timer()
print('Time: {0:9.5f}'.format(stop - start))
