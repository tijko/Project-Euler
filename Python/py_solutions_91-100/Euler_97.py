#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
The first known prime found to exceed one million digits was discovered in 1999, 
and is a Mersenne prime of the form 26972593−1; it contains exactly 2,098,960 
digits. Subsequently other Mersenne primes, of the form 2p−1, have been found 
which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 
2,357,207 digits: 28433×27830457+1.

Find the last ten digits of this prime number.
'''

from __future__ import print_function

import sys
import timeit


sys.set_int_max_str_digits(20000000)

def euler_97():
    massive_prime = 28433 * 2**7830457 + 1
    massive_prime_str = str(massive_prime)
    massive_prime_str_len = len(massive_prime_str)
    return massive_prime_str[massive_prime_str_len - 10:]

if __name__ == '__main__':
    start = timeit.default_timer()
    print('Answer: {}'.format(euler_97()))
    stop = timeit.default_timer()
    print('Time: {0:9.5f}'.format(stop - start))
