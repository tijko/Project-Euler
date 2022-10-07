#!/usr/bin/env python
# -*- coding: utf-8 -*-

# grid array with primes on the diagonals at a certain percent 

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
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

def euler_58():
    n, d = 16, 33
    add = lambda x: x[0] + x[1]
    row_pos = range(66, 73, 2)
    row_cnt = range(241, 290, 16)
    lin = 11
    while float(n) / d * 100 >= 10:
        row_cnt = map(add, zip(row_cnt, row_pos))
        row_pos = map(add, zip(row_pos, [8] * 4))
        if any(is_prime(i) for i in row_cnt):
            n += sum([1 for i in row_cnt if is_prime(i)])
        lin += 2
        d += 4
    return lin

print("Answer: %s" % euler_58())
stop = timeit.default_timer()
print("Time: %f" % (stop - start))
