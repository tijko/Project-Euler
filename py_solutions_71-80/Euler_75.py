# --*-- coding: utf-8 --*--

# Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?

import collections
import timeit


start = timeit.default_timer()

def euler_75():
    seen = collections.defaultdict(int)
    while triplets:
        triple = triplets.pop(0)
        a1, b1, c1 = triple
        triangle1(a1, b1, c1)
        triangle2(a1, b1, c1)
        triangle3(a1, b1, c1)
        (a2, b2, c2) = (a1, b1, c1)
        while sum([a1, b1, c1]) <= 1500000:
            seen[sum([a1, b1, c1])] += 1
            (a1, b1, c1) = map(sum, zip([a1, b1, c1], [a2, b2, c2]))
    return len([i for i in seen if seen[i] == 1])

def triangle1(a, b, c):
    a2 = (a - (2 * b)) + (2 * c)
    b2 = (2 * a) - b + (2 * c)
    c2 = (2 * a) - (2 * b) + (3 * c)
    if sum([a2, b2, c2]) <= 1500000:
        triplets.append([a2, b2, c2])

def triangle2(a, b, c):
    a2 = a + (2 * b) + (2 * c)
    b2 = (2 * a) + b + (2 * c)
    c2 = (2 * a) + (2 * b) + (3 * c)
    if sum([a2, b2, c2]) <= 1500000:
        triplets.append([a2, b2, c2])

def triangle3(a, b, c):
    a2 = -a + (2 * b) + (2 * c)
    b2 = (-2 * a) + b + (2 * c)
    c2 = (-2 * a) + (2 * b) + (3 * c)
    if sum([a2, b2, c2]) <= 1500000:
        triplets.append([a2, b2, c2])

    
triplets = [[3, 4, 5]]
print "Answer: %s" % euler_75()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
