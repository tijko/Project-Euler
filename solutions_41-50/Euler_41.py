# largest prime pan-digital number 

import timeit
import math
import itertools


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

def euler_41():
    pandigital = '987654321'
    while True:
        primes = [i for i in list(itertools.permutations(pandigital)) if
                     is_prime(int(''.join(i)))]
        if primes:
            prime = ''.join(max(primes))
            break
        if not primes:
            pandigital = pandigital[1:]                    
    return prime

print "Answer: %s" % euler_41()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
