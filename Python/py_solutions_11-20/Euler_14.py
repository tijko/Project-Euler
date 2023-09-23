# -*- coding: utf-8 -*-

from __future__ import print_function

'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

import timeit


try:
    xrange = range
except NameError:
    pass

start = timeit.default_timer()

def collatz(n):
    count = 0
    while n != 1:
        if n & 1:
            n *= 3 
            n += 1
            count += 1
        if not n & 1:
            n >>= 1 
            count += 1
    return count 

def euler_14():
    canidates = xrange(3, 1000000, 2)
    number_sequences = {collatz(i):i for i in canidates}
    return number_sequences[max(number_sequences)]

print("Answer: {}".format(euler_14()))
stop = timeit.default_timer()
print("Time: {0:9.5f}".format((stop - start)))
