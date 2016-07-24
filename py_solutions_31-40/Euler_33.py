# trivial example = 30/50 = 3/5 
# non-trivial example = 49/98 = 4/8 

# There are 4 non-trivial types of these fractions < 1 and both numerator and 
# denominator contain  two digits find the the product of the four in its 
# lowest common terms, what is the denominator? 

import timeit
import itertools

from functools import reduce
from operator import mul, truediv

try:
    range = xrange
except NameError:
    pass

start = timeit.default_timer()


def euler_33():
    numerators = list()
    denominators = list()
    fractions = (f for f in itertools.combinations(range(10, 100), 2)
                 if not any(i % 10 == 0 or i % 11 == 0 for i in f))
    floordiv = lambda v: v // 10
    mod = lambda v: v % 10
    for fraction in fractions:
        numerator, denominator = fraction
        if mod(numerator) == mod(denominator):
            ops = (floordiv, floordiv)
        elif mod(numerator) == floordiv(denominator):
            ops = (floordiv, mod)
        elif floordiv(numerator) == mod(denominator):
            ops = (mod, floordiv)
        elif floordiv(numerator) == floordiv(denominator):
            ops = (mod, mod)
        else: continue
        numerator, denominator = ops[0](numerator), ops[1](denominator)
        if truediv(numerator, denominator) == reduce(truediv, fraction):
            numerators.append(fraction[0])
            denominators.append(fraction[1])
    final_numerator = reduce(mul, numerators)
    final_denominator = reduce(mul, denominators)
    n_lcms = [i for i in range(2, final_numerator + 1) if 
              final_denominator % i == 0 and final_numerator % i == 0]
    return final_denominator / n_lcms[-1]    

print('Answer: {}'.format(euler_33()))
stop = timeit.default_timer()
print('Time: {0:9.5f}'.format(stop - start))
