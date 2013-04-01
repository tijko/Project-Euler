## composite odd numbers that aren't the sum of a prime twice a square ##

import timeit
import math


start = timeit.default_timer()

def is_prime(x):
    if x == 2:
        return True
    if x % 2 == 0 or x == 1:
        return False
    for i in xrange(3, int(math.sqrt(x))+1, 2):
        if x % i == 0:
            return False
    return True

def euler_46():   
    composites = [i for i in xrange(5000, 10000) if i % 2 != 0 and not is_prime(i)]
    for composite in composites:
        total = [(2 * (v**2)) for v in xrange(composite + 1) if (2 * (v**2)) < composite]
        primes = [k for k in xrange(composite + 1) if is_prime(k)]
        for v in range(len(total)): 
            for j in primes: 
                odds = total[v] + j 
                if odds == composite: 
                    break 
            if odds == composite: 
                break 
            if v >= len(total) - 1: 
                return composite

print "Answer: %s" % euler_46()
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)
