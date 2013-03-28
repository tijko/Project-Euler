## What is the value of the first triangle number to have over five hundred divisors? ##

from math import sqrt
from operator import mul
import timeit


start = timeit.default_timer()

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    for i in range(3, int(sqrt(n) + 1), 2):
        if n % i == 0:
            return False
    return True


def decompose(n, divisors):
    total = []
    for i in divisors:
        count = 0
        while n % i == 0:
            count += 1
            n /= i
        if count > 0:
            count += 1
            total.append(count)
    return reduce(mul, total)


def euler_12():
    canidates = [i for i in xrange(1000, 25000)]
    for i in canidates:
        chk = sum(range(i))
        prime_divisors = [v for v in range(1, int(sqrt(chk) + 1)) if is_prime(v)]
        if decompose(chk, prime_divisors) > 500:
            return chk

print "Answer: %s" % euler_12() 
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)
