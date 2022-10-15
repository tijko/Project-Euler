#!/usr/bin/env python
# -*- coding: utf-8 -*-

# How many continued fractions for N <= 10000 have an odd period?

from __future__ import print_function

import math
import timeit


start = timeit.default_timer()

def repeat(seq):
    for i in range(1,len(seq) - 1):
        j = len(seq)/i
        if seq[:i * j] == seq[:i] * j:
            return i

def euler_64():
    out = [i for i in range(1, 10001) if i**0.5 % 1 != 0]
    total = 0
    chek = []
    for i in out:
        constant_a = math.floor(math.sqrt(i))
        m0 =  constant_a 
        d0 = (i - (m0**2)) / 1
        a0 = int((constant_a + m0) / d0)
        for n in range(445):
            chek.append(a0)
            m1 = (d0 * a0) - m0
            d1 = (i - (m1**2)) / d0
            a1 = int((constant_a + m1) / d1)
            a0 = a1
            d0 = d1
            m0 = m1
        if repeat(chek) % 2 != 0:
            total += 1
        chek = []
    return total    

print("Answer: %s" % euler_64())
stop = timeit.default_timer()
print("Time: %f" % (stop - start))
 
