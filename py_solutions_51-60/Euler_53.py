# -*- coding: utf-8 -*-

'''How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?'''

import math
import timeit


start = timeit.default_timer()

def euler_53():
    values = [i for i in xrange(1, 101)]
    count = 0
    for i in values:
        r = xrange(1, i)
        for v in r:
            if math.factorial(i) / (math.factorial(v) * math.factorial(i - v)) > 1000000:
                count += 1
    return count

print "Answer: %s" % euler_53()
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)
