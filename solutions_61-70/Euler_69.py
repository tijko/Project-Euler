# Euler's Totient Function 

import math
import timeit
import collections


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

def euler_69():
    high = 0
    high_N = 0
    whole = collections.defaultdict(list)
    for n in xrange(2, 1000001):
        for i in xrange(2, int(math.sqrt(n)) + 2):
            if n % i == 0 and is_prime(i):
                whole[n].append(i)
    for k in whole.keys():
        phi = k
        for v in whole[k]:
            phi *= ((float(v) - 1) / v)
        if float(k) / phi > high:
            high = float(k) / phi 
            high_N = k
    return high_N

print "Answer: %s" % euler_69()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)

