# -*- coding: utf-8 -*-

'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

import math
import itertools
import timeit


start = timeit.default_timer()

def is_prime(x):
    if x == 2:
        return True
    if x % 2 == 0 or x == 1:
        return False
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

def euler_49():
    primes = [set(int(''.join(v)) for v in itertools.permutations(str(i)) if 
              is_prime(int(''.join(v))) and int(''.join(v)) > 999) for i in 
              xrange(1000, 10000) if is_prime(i)]
    primes = [sorted(i) for i in primes if len(i) > 2]
    for prime in primes:
        if [str(prime[i]) + str(prime[i+1]) + str((prime[i+1] - prime[i]) + 
            prime[i+1])  for i in xrange(len(prime) - 1) if (prime[i+1] - 
            prime[i]) + prime[i+1] in prime]:
            return [str(prime[i]) + str(prime[i+1]) + str((prime[i+1] - prime[i]) 
                    + prime[i+1])  for i in xrange(len(prime) - 1) if (prime[i+1] - 
                    prime[i]) + prime[i+1] in prime][0]


print "Answer: %s" % euler_49()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
