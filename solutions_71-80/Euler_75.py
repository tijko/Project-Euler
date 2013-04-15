# --*-- coding: utf-8 --*--

# Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?

import collections
import timeit


start = timeit.default_timer()

def euler_75():
    triplets = [[3, 4, 5]]
    seen = collections.defaultdict(int)
    while triplets:
        triple = triplets.pop(0)
        a, b, c = triple[0], triple[1], triple[2]
        new_a = (a - (2 * b)) + (2 * c)
        new_b = (2 * a) - b + (2 * c)
        new_c = (2 * a) - (2 * b) + (3 * c)
        if sum([new_a, new_b, new_c]) <= 1500000:
            triplets.append([new_a, new_b, new_c])
        new_a = a + (2 * b) + (2 * c)
        new_b = (2 * a) + b + (2 * c)
        new_c = (2 * a) + (2 * b) + (3 * c)
        if sum([new_a, new_b, new_c]) <= 1500000:
            triplets.append([new_a, new_b, new_c])
        new_a = -a + (2 * b) + (2 * c)
        new_b = (-2 * a) + b + (2 * c)
        new_c = (-2 * a) + (2 * b) + (3 * c)
        if sum([new_a, new_b, new_c]) <= 1500000:
            triplets.append([new_a, new_b, new_c])
        old_a = a
        old_b = b
        old_c = c
        while sum([a, b, c]) <= 1500000:
            seen[sum([a, b, c])] += 1
            a += old_a
            b += old_b
            c += old_c
    return len([i for i in seen.keys() if seen[i] == 1])
    
print "Answer: %s" % euler_75()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
