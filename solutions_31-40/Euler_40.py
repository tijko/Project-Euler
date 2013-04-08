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
    string = ''.join([str(i) for i in xrange(1, 1000500)])
    string = '0' + string
    return int(string[1]) * int(string[10]) * int(string[100]) * int(string[1000]) * int(string[10000]) * int(string[100000]) * int(string[1000000])


print "Answer: %s" % euler_40()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
