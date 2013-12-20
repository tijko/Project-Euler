# Find the maximum total from top to bottom of the triangle below:

import os
import timeit


start = timeit.default_timer()

def euler_18():
    path = os.getcwd().strip('py_solutions_11-20')
    with open(path + '/euler_txt/triangle1.txt') as f:
        tri = [map(int, i.split()) for i in f.readlines()]
    col = 0
    total = tri[0][0] + 10
    for row in xrange(1, len(tri)):
        if tri[row][col] > tri[row][col + 1]:
            total += tri[row][col]
        else:
            total += tri[row][col + 1]
            col += 1
    return total

print "Answer: %s" % euler_18()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
