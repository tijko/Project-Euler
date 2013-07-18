# grid array with primes on the diagonals at a certain percent 

import timeit
import math

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

def euler_58():
    n = 16
    d = 33
    three = [i for i in xrange(66, 200000,8)]
    five = [i for i in xrange(68, 200000,8)]
    seven = [i for i in xrange(70, 200000,8)]
    nine = [i for i in xrange(72, 200000,8)]
    row_3 = 241
    row_5 = 257
    row_7 = 273
    row_9 = 289
    lin = 11
    count = 0
    while float(n) / d * 100 >= 10:
        row_3 = row_3 + three[count]
        row_5 = row_5 + five[count]
        row_7 = row_7 + seven[count]
        row_9 = row_9 + nine[count]
        d += 4
        if is_prime(row_3):
          n += 1
        if is_prime(row_5):
          n+= 1
        if is_prime(row_7):
          n+= 1
        if is_prime(row_9):
          n += 1
        count += 1
        lin += 2
    return lin

print "Answer: %s" % euler_58()
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)
