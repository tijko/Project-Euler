## Pandigital number 987654321 --- say 39 * 186 = 7254 all ##
## So whats the combinations of products to equal 9 digits? ##

import timeit


start = timeit.default_timer()

def euler_32():
    x = xrange(2, 100)
    y = xrange(100, 5000)
    pandigitals = []
    for k in range(len(x)):
        for i in y:
            chk = str(x[k] * i) + str(x[k]) + str(i)
            if len(chk) == 9:
                if sorted([int(v) for v in chk]) == range(1, 10):
                    pandigitals.append(x[k] * i)
    return sum(set(pandigitals))


print "Answer: %s" % euler_32()
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)
