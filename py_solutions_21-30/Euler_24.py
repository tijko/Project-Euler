# -*-coding: utf-8 -*-

'''
A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

from itertools import permutations
import timeit


start = timeit.default_timer()

def euler_24():
    answer = 1 
    pandigital = permutations('0123456789')
    while answer < 1000000:
        pandigital.next()
        answer += 1
    return ''.join(pandigital.next())

print "Answer: %s" % euler_24()
stop = timeit.default_timer()
print "Time: %f" % (stop - start) 
