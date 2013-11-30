# Find the product of the coefficients, a and b, for the quadratic 
# expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

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


def euler_27():
    high = 0
    for i in xrange(-999, 1000):
        for v in xrange(-999, 1000):
            count = 0
            n = 0
            quad = n**2 + (n*v) + i
            while is_prime(abs(quad)):
                count += 1
                n += 1
                quad = n**2 + (n*v) + i
            if count > high:
                high = count
                total =  i*v
    return total


print "Answer: %s" % euler_27()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
