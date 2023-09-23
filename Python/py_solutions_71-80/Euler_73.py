#!/usr/bin/env python
# -*- coding: utf-8 -*-

# how many fractions between 1/2 and 1/3 in 12001 reduced 

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
    limit = 1.0 / 2
    total = 0
    for n in range(2, 12001):
        for i in range(int(n * (1.0 / 3)), int(n * (1.0 / 2)) + 1):
            if float(i) / n > limit:
                break
            elif fractions.gcd(n, i) == 1:
                if float(i) / n > 1.0 / 3 and float(i) / n < limit:
                    total += 1
    return total

print("Answer: %s" % euler_71())
stop = timeit.default_timer()
print("Time: %f" % (stop - start))
