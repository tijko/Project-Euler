## Pandigital number 987654321 --- say 39 * 186 = 7254 all ##

## So whats the combinations of products to equal 9 digits? ##

import timeit
import string


start = timeit.default_timer()

def euler_32():
    x = xrange(2, 100)
    y = xrange(100, 5000)
    pandigitals = set()
    pandigital = {n for n in string.digits[1:]}
    for k in range(len(x)):
        for i in y:
            digi_str = ''.join(map(str, [x[k] * i, x[k], i]))
            if len(digi_str) == 9 and {j for j in digi_str} == pandigital:
                pandigitals.add(x[k] * i)
    return sum(pandigitals)

print "Answer: %s" % euler_32()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
