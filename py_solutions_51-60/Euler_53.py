# -*- coding: utf-8 -*-

'''How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?'''

from math import factorial as fac
import timeit


start = timeit.default_timer()

def euler_53():
    return sum([1 for i in [l for v in zip([1] * 100, xrange(1, 101)) for l in xrange(v[1]) if fac(v[1]) / (fac(l) * fac(v[1] - l)) > 1000000]])

print "Answer: %s" % euler_53()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
