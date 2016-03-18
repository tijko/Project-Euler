#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
A number chain is created by continuously adding the square of the digits in a 
number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless 
loop. What is most amazing is that EVERY starting number will eventually arrive
at 1 or 89.

How many starting numbers below ten million will arrive at 89?
'''

from __future__ import print_function

import timeit

try:
    range = xrange
except NameError:
    pass


chain = lambda n: sum([int(i)**2 for i in str(n)])

def euler_92():
    eighty_nine = 0
    chains = {}
    for start in range(1, 10000000):
        sq_sum = chain(start)
        sub_chain = []
        while sq_sum != 89 and sq_sum != 1 and not chains.get(sq_sum):
            sub_chain.append(sq_sum)
            sq_sum = chain(sq_sum)
        sub_chain.append(sq_sum)
        if sq_sum != 89 and sq_sum != 1:
            sq_sum = chains.get(sq_sum)
        for sub in sub_chain:
            chains[sub] = sq_sum
        if sq_sum == 89:
            eighty_nine += 1
    return eighty_nine    

if __name__ == "__main__":
    start = timeit.default_timer()
    print("Answer: {}".format(euler_92()))
    stop = timeit.default_timer()
    print("Time: {0:9.5f}".format(stop - start))
