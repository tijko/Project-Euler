# larger triangle path 

import timeit
import os


start = timeit.default_timer()

def euler_67():
    with open(os.path.abspath('').strip('solutions_61-70') + '/euler_txt/triangle2.txt') as f:
        triangle = f.readlines()
    r = [[int(i) for i in v.split()] for v in triangle]
    r = r[::-1]
    for x in xrange(0, len(r) - 1):
	    for y in xrange(0,len(r[x + 1])):
		    r[x + 1][y] = max(r[x][y]+r[x + 1][y],r[x][y + 1]+r[x + 1][y])
    return r[len(r) - 1][0]

print "Answer: %s" % euler_67()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)

