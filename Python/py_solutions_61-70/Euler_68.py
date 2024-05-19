#!/usr/bin/env python
# -*- coding: utf-8 -*-

# magic 5-gon ring

#import itertools
from __future__ import print_function

from itertools import combinations, permutations, chain
import timeit

try:
    range = xrange
except NameError:
    pass

start = timeit.default_timer()

def euler_68():
    rings = combinations(xrange(1, 11), 3)
    rings = [i for j in map(permutations, rings) for i in j]
    magic_gon = list()
    for c in chain.from_iterable(([i] * 10 for i in range(720))):
        pos = 1
        for i in rings:
            h = list()
            if (sum(i) == sum(rings[c]) and
                rings[c][0] < i[0] and
                rings[c][2] == i[1] and
                i[0] not in rings[c]):
                h.append(rings[c])
                h.append(i)
                for j in rings:
                    if pos > len(h) - 1:
                        break
                    if (sum(h[pos]) == sum(j) and
                        h[0][0] < j[0] and
                        h[pos][2] == j[1] and
                        j[0] not in h[pos] and
                        h[pos][0] not in j and
                        h[0][0] not in j):
                        candidate = ''.join(map(str, chain.from_iterable(h)))
                        if (j[0] not in [n[0] for n in h] and
                            str(j[0]) not in candidate):
                            h.append(j)
                            pos += 1
            if len(h) >= 4:
                if (h not in magic_gon and
                    not {t for r in h for t in r} ^ set(xrange(1, 11))):
                    magic_gon.append(h)
    magic_gon = filter(lambda s: len(s) == 16,
                       map(''.join, [map(str, chain.from_iterable(k))
                                                for k in magic_gon]))
    return max(map(int, magic_gon))

if __name__ == '__main__':
    print("Answer: %s" % euler_68())
    stop = timeit.default_timer()
    print("Time: %f" % (stop - start))
