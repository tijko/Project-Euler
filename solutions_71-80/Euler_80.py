# sum of the first 100 natural numbers decimal square root 

import mpmath
import timeit


start = timeit.default_timer()

def euler_80():
    mpmath.mp.dps = 102
    total = 0
    roots = [i for i in xrange(1, 100) if i**0.5 % 1 != 0]
    for i in roots:
        total += sum([int(v) for v in str(mpmath.sqrt(i)) if v != '.'][:100])
    return total

print "Answer: %s" % euler_80()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)

