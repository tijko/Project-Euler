# -*- coding: utf-8 -*-
#!/usr/bin/env python


# Given that L is the length of the wire, for how many values of 
# L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?

import timeit
import collections

from functools import partial
from itertools import starmap
from operator import imul, add

start = timeit.default_timer()

def euler_75():
    triplet_count = collections.defaultdict(int)
    triplets = [(3, 4, 5)]
    while triplets:
        triplet = triplets.pop(0)
        triangle(triplets, triplet)
        a, b, c = triplet
        while sum([a, b, c]) <= 1500000:
            triplet_count[sum([a, b, c])] += 1
            a, b, c = map(sum, zip([a, b, c], triplet))
    return len([i for i in triplet_count if triplet_count[i] == 1])

def triangle(triplets, triplet):
    triangles = [[(1, -2, 2), (2, -1, 2), (2, -2, 3)],
                 [(1, 2, 2), (2, 1, 2), (2, 2, 3)],
                 [(-1, 2, 2), (-2, 1, 2), (-2, 2, 3)]]
    zip_trip = partial(zip, triplet)
    for triangle in triangles:
        new_triplet = [reduce(add, starmap(imul, i)) 
                       for i in map(zip_trip, triangle)]
        if sum(new_triplet) <= 1500000:
            triplets.append(new_triplet)


if __name__ == '__main__': 
    print "Answer: %s" % euler_75()
    stop = timeit.default_timer()
    print "Time: %f" % (stop - start)
