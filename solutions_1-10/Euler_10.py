# Find the sum of all the primes below two million. 

from math import sqrt
import timeit


start = timeit.default_timer()

def is_prime(n):
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n) + 1), 2):
        if n % i == 0:
            return False
    return True

def euler_10(n):
    for i in xrange(1, n):
        if is_prime(i):
            yield i

print sum([i for i in euler_10(2000001)])
stop = timeit.default_timer()
print 'Time: %f' % (stop - start)

