# Reduced Fractions 

import fractions
import math
import timeit


start = timeit.default_timer()

def euler_71():
    limit = 3.0 / 7
    best = 0
    for n in xrange(2, 1000001):
        for i in xrange(int(n * (3.0 / 7)), int(n * (2.0 / 5)) - 1, -1):
            if float(i) / n < best:
                break
            elif fractions.gcd(n, i) == 1:
                if float(i) / n > best and float(i) / n < limit:
                    best_N = i
                    best_D = n
                    best = float(i) / n
    return best_N

print "Answer: %s" % euler_71()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)

