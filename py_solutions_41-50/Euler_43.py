# -*- coding: utf-8 -*-

'''
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, 
but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
'''

import itertools
import timeit


start = timeit.default_timer()

def euler_43():
    return sum([int(''.join(i)) for i in itertools.permutations('9876543210') if not sum(map(lambda x: x[0] % x[1], zip(map(int, [''.join(i)[j:j+3] for j in xrange(1, 8)]), [2, 3, 5, 7, 11, 13, 17])))]) 

print "Answer: %s" % euler_43()
stop = timeit.default_timer() 
print "Time: %f" % (stop - start)
