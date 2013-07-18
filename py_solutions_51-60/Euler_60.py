# Find lowest sum of a set of fives primes for which any two can be concatenated to form a prime in any order

import math
import itertools
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

def prime_combos(*args):
    for i in itertools.combinations(args, 2):
        if not is_prime(int(i[0] + i[1])) or not is_prime(int(i[1] + i[0])):
            return False
    return True

def euler_60():
    prime = [w for w in xrange(1, 10000) if is_prime(w) and w != 5 and w != 2]
    for i in prime:
        for j in prime[prime.index(i):]:
            if prime_combos(str(i), str(j)):
                for v in prime[prime.index(j):]:
                    if prime_combos(str(i), str(j), str(v)):
                        for e in prime[prime.index(v):]:
                            if prime_combos(str(i), str(j), str(v), str(e)):
                                for x in prime[prime.index(e):]:
                                    if prime_combos(str(i), str(j), str(v), str(e), str(x)):
                                        return sum([i, j, v, e, x])

print "Answer: %s" % euler_60()
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)

