#!/usr/bin/env python
# -*- coding: utf-8 -*-

# what is the first number to have 5000 different ways to sum with prime
# numbers? 

from __future__ import print_function

import math
import timeit

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
    for i in range(3,int(math.sqrt(x))+1,2):
        if x % i == 0:
            return False
    return True

def prime_sum(lim):
    lim += 1
    o_set = [i for i in range(lim - 1) if is_prime(i)][::-1]
    s_set = [0] * len(o_set)
    ways, pos, flag = 0, -2, 0
    while True:
        for n in range(0, lim, o_set[-1]):
            if sum(s_set[:-1] + [n]) == (lim - 1):
                ways += 1
                s_set = s_set[:-1] + [n]
                flag = 1
                break
            if sum(s_set[:-1] + [n]) > (lim - 1):
                s_set = s_set[:-1] + [n]
                flag = 1
                break
        if pos < -(len(o_set)):
            return ways
        if flag == 1 and pos < -2:
            for i, v in enumerate(s_set[pos:][::-1], 1):
                if v != 0:
                    s_set[-i] = 0
                    s_set[-i - 1] += o_set[-i - 1]
                    flag = 0
                    if s_set[pos] >= (lim - 1):
                        pos -= 1
                    break
        elif s_set[pos] <= (lim - 1):
            if s_set[pos] == (lim - 1):
                pos -= 1
            for i, v in enumerate(s_set[pos:-1][::-1], 2):
                if v < (lim - 1):
                    s_set[-i] += o_set[-i]
                    break
                if v >= (lim - 1):
                    s_set[-i] = 0
        elif s_set[pos] >= (lim - 1) and pos == -2:
            pos -= 1

def euler_77():
    start, ways = 10, 0
    while ways < 5000:
        start += 1
        ways = prime_sum(start)
    return start

print("Answer: %s" % euler_77())
stop = timeit.default_timer()
print("Time: %f" % (stop - start))
