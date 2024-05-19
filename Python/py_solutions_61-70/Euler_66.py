#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Diophantine equation

from __future__ import print_function

import timeit
import math

try:
    range = xrange
except NameError:
    pass

start = timeit.default_timer()

def euler_66():
    candidates = filter(lambda i: i**0.5 % 1 != 0, range(1001))
    high_x = high_D = 0
    for candidate in candidates:
        const_a = math.floor(math.sqrt(candidate))
        m0 = const_a
        d0 = (candidate - (m0**2)) / 1
        a0 = int((const_a + m0) / d0)
        x0 = const_a
        y0 = 1
        x1 = x0 * a0 + 1
        y1 = y0 * a0
        m0 = (d0 * a0) - m0
        d0 = (candidate - (m0**2)) / d0
        a0 = int((const_a + m0) / d0)
        k = x1**2 - candidate * y1**2
        if k == 1:
            if x1 > high_x:
                high_x = x1
                high_D = candidate
        x2 = x1 * a0 + x0
        y2 = y1 * a0 + y0
        while k != 1:
            x0, y0 = x1, y1
            x1, y1 = x2, y2
            m1 = (d0 * a0) - m0
            d1 = (candidate - (m1**2)) / d0
            a1 = (const_a + m1) / d1
            a0 = long(a1)
            d0, m0 = d1, m1
            x2 = long(x1) * a0 + long(x0)
            y2 = long(y1) * a0 + long(y0)
            k = x2**2 - candidate * y2**2
            if k == 1:
                if x2 > high_x:
                    high_x = x2
                    high_D = candidate
    return high_D

if __name__ == '__main__':
    print("Answer: %s" % euler_66())
    stop = timeit.default_timer()
    print("Time: %f" % (stop - start))
