# trivial example = 30/50 = 3/5 
# non-trivial example = 49/98 = 4/8 

# There are 4 non-trivial types of these fractions < 1 and both numerator and 
# denominator contain two digits find the the product of the four in its lowest 
# common terms, what is the denominator? 

import timeit
import itertools


start = timeit.default_timer()

def euler_33():
    numerators = list()
    denominators = list()
    product = lambda x, y: x * y
    fractions = [f for f in itertools.permutations(xrange(10, 100), 2) 
                 if f[0] < f[1] and not any(i % 10 == 0 or 
                                            i / 10 == i % 10 for i in f)]
    for f in fractions:
        n_cpm = {d for d in str(f[0])}
        d_cpm = {d for d in str(f[1])}
        if n_cpm.intersection(d_cpm):
            shared_d = list(n_cpm.intersection(d_cpm))
            new_n = str(f[0]).replace(shared_d[0], '')
            new_d = str(f[1]).replace(shared_d[0], '')          
            if float(new_n) / int(new_d) == float(f[0]) / f[1]:
                numerators.append(f[0])
                denominators.append(f[1])
    fin_n = reduce(product, numerators)
    fin_d = reduce(product, denominators)
    n_lcms = [i for i in xrange(2, fin_n + 1) if fin_d % i == 0 and fin_n % i == 0]
    return fin_d / n_lcms[-1]    

print "Answer: %s" % euler_33()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
