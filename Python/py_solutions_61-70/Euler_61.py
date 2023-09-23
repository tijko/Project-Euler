#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cyclic number of six 4-digit that are in one of each and doesn't have to be 
# in ranking order (i.e. tri,sq,pent...) 

from __future__ import print_function

import itertools
import timeit


try:
    range = xrange
except NameError:
    pass

start = timeit.default_timer()

def euler_61():
    three = [(i * (i + 1) / 2) for i in range(45, 141)]
    four = [(i**2) for i in range(32, 100)]
    five = [(i * ((3 * i) - 1) / 2) for i in range(26, 82)]
    six = [(i * ((2 * i) - 1)) for i in range(23, 71)]
    seven = [(i * ((5 * i) - 3) / 2) for i in range(21, 64)]
    eight = [(i * ((3 * i) - 2)) for i in range(19, 59)]
    cyclic = [i for i in itertools.permutations([three, four, five, six, seven, eight])]
    for n in range(len(cyclic)):
        for p in range(len(cyclic[n][1])):
            for i in cyclic[n][0]:
                if str(i)[2:] == str(cyclic[n][1][p])[:2]:
                    for k in cyclic[n][2]:
                        if str(cyclic[n][1][p])[2:] == str(k)[:2]:
                            for v in cyclic[n][3]:
                                if str(k)[2:] == str(v)[:2]:
                                    for j in cyclic[n][4]:
                                        if str(v)[2:] == str(j)[:2]:
                                            for s in cyclic[n][5]:
                                                if str(j)[2:] == str(s)[:2] and str(s)[2:] == str(i)[:2]:
                                                    return sum([i, cyclic[n][1][p], k, v, j, s])                                            

print("Answer: %s" % euler_61())
stop = timeit.default_timer()
print("Time: %f" % (stop - start))
