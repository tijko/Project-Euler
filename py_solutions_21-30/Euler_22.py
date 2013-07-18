## number amount of names ##

import timeit
import os


start = timeit.default_timer()

def euler_22():
    total = 0
    name = 0
    with open(os.path.abspath('').strip('solutions_21-30') + 
                                  '/euler_txt/names1.txt') as f:
        name_list = f.readlines()
    name_list = sorted([i for i in name_list[0].split('"') if i != ',' and i != ''])
    for v in xrange(len(name_list)):
        for i in name_list[v]:
            name += ord(i) - 64 
        total += name * (v + 1)
        name = 0
    return total

print "Answer: %s" % euler_22()
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)

