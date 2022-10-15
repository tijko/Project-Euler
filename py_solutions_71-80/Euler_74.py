#!/usr/bin/env python
# -*- coding: utf-8 -*-

# factorial of each digit of a number to sequence 
# all numbers under a million max have 60 length sequence 

from __future__ import print_function

import math
import timeit

try:
    range = xrange
except NameError:
    pass

start = timeit.default_timer()

def euler_74():
    total = 0
    chain = list()
    for n in range(1, 1000001):
        if len(chain) >= 60:
            total += 1
        chain = [n]
        pos = 0    
        while True:
            next_term = sum([math.factorial(int(v)) for v in [j for j in str(chain[pos])]])
            if set(chain).intersection([next_term]):
                break
            chain.append(next_term)
            pos += 1
            if len(chain) >= 60:
                break
    return total

print("Answer: %s" % euler_74())
stop = timeit.default_timer()
print("Time: %f" % (stop - start))
                
