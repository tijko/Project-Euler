# Find the maximum total from top to bottom of the triangle below:

import os
import timeit


start = timeit.default_timer()

def euler_18():
    with open(os.path.abspath('').strip('solutions_11-20') + 'euler_txt/triangle1.txt') as f:
        x = list()
        for line in f.readlines():
            x.append(line.split())
    tot = 10
    row = 0
    position = 0
    tot += int(x[row][position])
    row += 1
    while row < len(x):
        if int(x[row][position]) > int(x[row][position+1]):
            tot += int(x[row][position])
        else:
            tot += int(x[row][position+1])
            position += 1
        row += 1
    return tot

print "Answer: %s" % euler_18()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
