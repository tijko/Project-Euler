# -*- coding: utf-8 -*-

'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

import timeit
import operator


start = timeit.default_timer()

def collatz(n):
    var = []
    while n != 1:
        if n % 2 != 0:
            n = (n * 3) + 1
            var.append(n)
        if n % 2 == 0:
            n = n / 2 
            var.append(n)
    return len(var)


def euler_14():
    data = map(collatz,range(1,1000000))
    enum_data = list(enumerate(data, 1))
    enum_data.sort(key=operator.itemgetter(1))
    return enum_data[len(enum_data)-1]  


print "Answer: %s" % euler_14()[0]
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)
