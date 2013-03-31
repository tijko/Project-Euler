# -*- coding: utf-8 -*-
'''
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
'''

import timeit


start = timeit.default_timer()

def euler_31():
    ways = 0
    for i in xrange(0, 201, 200):
        for j in xrange(0, 201, 100):
            for l in xrange(0, 201, 50):
                for v in xrange(0, 201, 20):
                    for k in xrange(0, 201, 10):
                        for m in xrange(0, 201, 5):
                            for e in xrange(0, 201, 2):
                                for x in xrange(201):
                                    chk = sum([i, j, l, v, k, m, e, x])
                                    if chk > 200:
                                        break
                                    if chk == 200:
                                        ways += 1
                                        break
    return ways


print "Answer: %s" % euler_31()
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)


