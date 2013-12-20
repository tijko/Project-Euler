# find the largest palindrome number made from the product of two 3-digit numbers ?

import itertools
import timeit


start = timeit.default_timer()

def euler_4():
    canidates = itertools.combinations(xrange(100, 1000), 2)
    current_high = 0
    for canidate in canidates:
        pal_prod = canidate[0] * canidate[1]
        if str(pal_prod)[::-1] == str(pal_prod) and pal_prod > current_high:
            current_high = pal_prod
    return current_high

print "Answer: %s" % euler_4()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
