# Pandigital number 987654321 --- say 39 * 186 = 7254 all 
# So whats the combinations of products to equal 9 digits?

import timeit
import itertools


start = timeit.default_timer()

def euler_32():
    pandigitals = set()
    pandigital = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
    for x,y in itertools.product(xrange(2, 100), xrange(100, 5000)):
        digi_str = ''.join(map(str, [x * y, x, y]))
        if len(digi_str) == 9 and {j for j in digi_str} == pandigital:
            pandigitals.add(x * y)
    return sum(pandigitals)

print "Answer: %s" % euler_32()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
