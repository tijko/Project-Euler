# find the largest palindrome number made from the product of two 3-digit numbers ?

import itertools
import timeit


start = timeit.default_timer()

def euler_4():
    canidates = [i for i in xrange(100, 1000)]
    canidates = [i for i in itertools.combinations(canidates, 2)]
    current_high = 0
    for canidate in canidates:
        new = canidate[0] * canidate[1]
        if str(new)[::-1] == str(new) and new > current_high:
            current_high = new
    return current_high

print "Answer: %s" % euler_4()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
