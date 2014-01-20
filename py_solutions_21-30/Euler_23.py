# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers. 

import timeit
import itertools


start = timeit.default_timer()


def euler_23():
    abundant = (i for i in xrange(28124) if i < 
                sum(itertools.ifilterfalse(lambda x, i=i: i % x, xrange(1, i / 2 + 1))))
    abundant_sums = {i for i in combo_gen(abundant)}
    return sum(abundant_sums.symmetric_difference(xrange(28124)))

def combo_gen(x):
     for i in itertools.combinations_with_replacement(x, 2):
         if sum(i) < 28124:
            yield sum(i)


print "Answer: %s" % euler_23()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
