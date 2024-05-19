#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Reduced Fractions

from __future__ import print_function

import fractions
import math
import timeit

try:
    range = xrange
except NameError:
    pass


start = timeit.default_timer()

def euler_71():
    limit = 3.0 / 7
    best = 0
    for n in range(2, 1000001):
        for i in range(int(n * (3.0 / 7)), int(n * (2.0 / 5)) - 1, -1):
            if float(i) / n < best:
                break
            elif fractions.gcd(n, i) == 1:
                if float(i) / n > best and float(i) / n < limit:
                    best_N = i
                    best_D = n
                    best = float(i) / n
    return best_N

print("Answer: %s" % euler_71())
stop = timeit.default_timer()
print("Time: %f" % (stop - start))

