## Truncatable primes from left to right ---> Ex: 3797 ~ 797 ~ 97 ~ 7 and 3797 ~ 379 ~ 37 ~ 3 ##

import math
import timeit


start = timeit.default_timer()

def is_prime(x):
    if x == 2: 
        return True
    if x % 2 == 0 or x == 1:
        return False
    for i in xrange(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

def euler_37():
    truncatable = list()
    primes = [i for i in xrange(11, 1000000) if is_prime(i) and 
             not any([v for v in str(i) if int(v) in [0, 4, 6, 8]])]
    for prime in primes:
        if (all([is_prime(int(str(prime)[:-v])) for v in xrange(1, len(str(prime)))]) and
            all([is_prime(int(str(prime)[v:])) for v in xrange(1, len(str(prime)))])):
            truncatable.append(prime)
    return sum(truncatable)


print "Answer: %s" % euler_37()
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)
