## Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers. ##

import timeit
import itertools


start = timeit.default_timer()

def euler_23():
    abundant = list()
    for i in xrange(1, 28124):
        if i < sum([v for v in xrange(1, (i/2) + 1) if i % v == 0]):
            abundant.append(i)
    abundant_sums = set([i for i in combo_gen(abundant)]) 
    return sum(set(xrange(1, 28124)).difference(abundant_sums))


def combo_gen(x):
     for i in itertools.combinations_with_replacement(x, 2):
         if sum(i) < 28124:
            yield sum(i)


print "Answer: %s" % euler_23()
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)
