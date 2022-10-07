#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Find the highest sum of a number's digits for numbers a**b while a and b < 100 

from __future__ import print_function

import timeit
import itertools


try:
    range = xrange
except NameError:
    pass

start = timeit.default_timer()

def euler_56():
    return max([sum(map(int, str(i))) for i in [pow(l[0], l[1]) for l in itertools.product(range(100), range(100))]])

print("Answer: %s" % euler_56())
stop = timeit.default_timer()
print("Time: %f" % (stop - start))
