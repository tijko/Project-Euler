#!/usr/bin/env python
# -*- coding: utf-8 -*-

# How many positive n-digit numbers exist which are also n'th powers?

from __future__ import print_function

import timeit

try:
    range = xrange
except NameError:
    pass

start = timeit.default_timer()

def euler_63():
    total = 0
    for n in range(1, 100):
        for i in range(1, 100):
            if len(str(i**n)) == n:
                total += 1
    return total

if __name__ == '__main__':
    print("Answer: {}".format(euler_63()))
    stop = timeit.default_timer()
    print("Time: {:.4f}".format(stop - start))
