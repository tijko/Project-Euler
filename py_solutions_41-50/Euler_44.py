# -*- coding: utf-8 -*-

'''
Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?
'''

import timeit
import itertools


start = timeit.default_timer()

def euler_44():
    pent  = {i * ((3 * i) - 1) / 2 for i in xrange(1, 6000)}
    for i in itertools.combinations(pent, 2):
        if i[1] + i[0] in pent and i[1] - i[0] in pent:
            return i[1] - i[0]

print "Answer: %s" % euler_44()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
