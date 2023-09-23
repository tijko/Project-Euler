#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
The proper divisors of a number are all the divisors excluding the number 
itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the 
sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the 
proper divisors of 284 is 220, forming a chain of two numbers. For this reason,
220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we 
form a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding 
one million.
'''

from __future__ import print_function
from collections import defaultdict
from math import sqrt

import timeit

try:
    range = xrange
except NameError:
    pass


def is_prime(n):
    if n == 2: return True
    if n < 2: return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0: return False
    return True

proper_divisors_cache = defaultdict(set)
checked = set()

limit = 10**6

def find_factors(limit):
    for i in range(2, limit + 1):
        # enumerate a range starting at the current integer x2
        # stepping by the size of the integer to the limit
        for idx, f in enumerate(range(i + i, limit, i), 2):
            # using 'f' which is the current integer along the stepped range
            # as the key, add to the factors value-list the step size
            # and its index enumerated from base 2
            proper_divisors_cache[f].update({i, idx})

def find_chain(canidate):
    chain = {canidate}
    divisors = sum(proper_divisors_cache[canidate]) + 1
    while divisors < limit:
        if {divisors} & chain:
            # not a complete chain, add starting canidate to checked
            checked.add(canidate)
            return {} # return empty set, no use checking incomplete chains
        else: 
            chain.add(divisors)
        divisors = sum(proper_divisors_cache[divisors]) + 1
        # divisors equal starting canidate, is a complete chain
        if divisors == canidate:
            checked.update(chain)
            return chain 
    return {} # return empty set, no use checking incomplete chains

def euler_95():
    longest_chain_len = 0
    # build a factors dict having the number and list as
    # a list of integers as the key, value respectively.
    find_factors(limit)
    for canidate in range(2, limit):
        # if canidate is in checked, it was already in another 
        # chain-series or if it is prime no use checking.
        if is_prime(canidate) or checked & {canidate}: continue
        chain = find_chain(canidate)
        chain_len = len(chain)
        if chain_len > longest_chain_len:
            longest_chain_len = chain_len
            longest_chain = chain
    return sorted(list(longest_chain))[0]

if __name__ == '__main__':
    start = timeit.default_timer()
    print('Answer: {}'.format(euler_95()))
    stop = timeit.default_timer()
    print('Time: {0:9.5f}'.format(stop - start))
