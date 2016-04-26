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

proper_divisors_cache = {}
no_chain = set()
chains = set()

def find_divisor_sum(n):
    divisors_sum = proper_divisors_cache.get(n)
    if divisors_sum is None:
        divisors_sum = sum([sum([i, n / i]) for i in 
                            range(2, int(sqrt(n)) + 1) if n % i == 0]) + 1
        proper_divisors_cache[n] = divisors_sum
        return divisors_sum
    return divisors_sum
    
def euler_95():
    longest_chain = 0
    element_limit = 10**6
    limit = element_limit * 2
    smallest_element = 0
    for canidate in range(2, limit):
        if is_prime(canidate): continue
        if no_chain & {canidate}: continue
        if chains & {canidate}: continue
        chain = {canidate}
        divisors = find_divisor_sum(canidate)
        while divisors < element_limit and divisors != canidate:
            if {divisors} & chain:
                no_chain.add(canidate)
                break
            else: chain.add(divisors)
            divisors = find_divisor_sum(divisors)
            if divisors == canidate:
                if len(chain) > longest_chain:
                    chains.update(chain)
                    longest_chain = len(chain)
                    smallest_element = sorted(list(chain))[0] 
    return smallest_element

if __name__ == '__main__':
    start = timeit.default_timer()
    print('Answer: {}'.format(euler_95()))
    stop = timeit.default_timer()
    print('Time: {0:9.5f}'.format(stop - start))
