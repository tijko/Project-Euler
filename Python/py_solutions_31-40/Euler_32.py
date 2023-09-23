# Pandigital number 987654321 --- say 39 * 186 = 7254 all 
# So whats the combinations of products to equal 9 digits?

import timeit
import itertools


try:
    range = xrange
except NameError:
    pass

start = timeit.default_timer()

def euler_32():
    pandigitals = set()
    pandigital = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
    for x, y in itertools.product(range(2, 100), range(100, 5000)):
        digi_str = ''.join(map(str, [x * y, x, y]))
        if len(digi_str) == 9 and {i for i in digi_str} == pandigital:
            pandigitals.add(x * y)
    return sum(pandigitals)

print('Answer: {}'.format(euler_32()))
stop = timeit.default_timer()
print('Time: {0:9.5f}'.format(stop - start))
