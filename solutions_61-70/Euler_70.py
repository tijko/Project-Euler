# permutations of eulers totient function

import math
import timeit
import collections
import itertools


start = timeit.default_timer()

def is_prime(x):
    if x == 2:
        return True
    if x == 1 or x % 2 == 0:
        return False
    for i in range(3,int(math.sqrt(x)) + 1,2):
        if x % i == 0:
            return False
    return True

def euler_70():
    divisors = [i for i in xrange(1000, 10000) if is_prime(i)]
    canidates = [i[0] * i[1] for i in itertools.combinations(divisors, 2) if i[0] * i[1] < 10000000]
    whole = collections.defaultdict(list)
    for n in canidates:
        for i in xrange(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0 and is_prime(i):
                whole[n].append(i)
        if len(whole[n]) == 1:
            whole[n].append(n / whole[n][0])
    low = 10000000
    low_N = 0
    for k in whole.keys():
        total = k
        for v in whole[k]:
            total *= ((float(v) - 1) / v)
        if sorted([i for i in str(k)]) == sorted([i for i in str(int(total))]):
            if float(k) / total < low:
                low = float(k) / total
                low_N = k
    return low_N

print "Answer: %s" % euler_70()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)

