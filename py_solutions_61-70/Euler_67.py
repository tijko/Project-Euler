#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# larger triangle path 

from __future__ import print_function

import timeit
import os

try:
    range = xrange
except NameError:
    pass

start = timeit.default_timer()

def euler_67():
    with open('/home/tijko/Project-Euler/euler_txt/triangle2.txt') as f:
        triangle = f.readlines()
    r = [[int(i) for i in v.split()] for v in triangle]
    r = r[::-1]
    for x in range(0, len(r) - 1):
	    for y in range(0,len(r[x + 1])):
		    r[x + 1][y] = max(r[x][y]+r[x + 1][y],r[x][y + 1]+r[x + 1][y])
    return r[len(r) - 1][0]

print("Answer: %s" % euler_67())
stop = timeit.default_timer()
print("Time: %f" % (stop - start))

