# -*- coding: utf-8 -*-

'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.
If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''

import timeit


start = timeit.default_timer()

def euler_40():
    irrational = ''.join(map(str, xrange(1000001)))
    return reduce(lambda x, y: x * y, map(int, [irrational[10**e] for e in xrange(6)]))

print "Answer: %s" % euler_40()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
