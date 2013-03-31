## largest concatenated pandigital number from product ##

import timeit
from string import digits


start = timeit.default_timer()

def pandigitize(x, y):
    return x * y

def euler_38():
    pandigital = max([''.join([i for i in str(map(pandigitize, [i] * 2, [1, 2])) if i.isdigit()]) for i in xrange(192, 10000) 
                     if ''.join(sorted([k for k in str(map(pandigitize, [i] * 2, [1, 2])) if k.isdigit()])) == digits[1:]])
    return pandigital

print "Answer: %s" % euler_38() 
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)

