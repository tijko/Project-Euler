# -*- coding: utf-8 -*-
'''
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
'''

import timeit

start = timeit.default_timer()


try:
    range = xrange
except NameError:
    pass


def euler_31():
    limit = 200
    currency = [1, 2, 5, 10, 20, 50, 100, 200]
    no_currency = len(currency)
    amount = [0] * no_currency
    idx = ways = 0
    while idx < no_currency:
        amount[idx] += currency[idx]
        total = sum(amount)
        if total < limit:
            idx = 0
        else:
            amount[idx] = 0
            if total == limit: ways += 1
            idx += 1
    return ways

print('Answer: {}'.format(euler_31()))
stop = timeit.default_timer()
print('Time: {0:9.5}'.format(stop - start))

