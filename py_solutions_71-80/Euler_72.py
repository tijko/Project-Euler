# --*-- coding: utf-8 --*--

# How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?

import timeit
import math


start = timeit.default_timer()

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    for i in xrange(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def euler_72():
    p = [i for i in xrange(2, int(math.sqrt(1000001)) + 1) if is_prime(i)]
    grand = 0
    for x in xrange(2, 1000001):
        total = x
        if is_prime(x):
            grand += (total - 1)
        else:
            primes = [i for i in p if x % i == 0]
            pl = x
            for v in primes:
                while pl % v == 0:
                    pl /= v
                    if is_prime(pl) and pl not in primes:
                        primes.append(pl)
            for v in primes:
                total *= (float(v - 1) / v)
            grand += int(total)
    return grand


print "Answer: %s" % euler_72()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)

