# number amount of names

import timeit
import os


start = timeit.default_timer()

def euler_22():
    with open(os.path.abspath('').strip('py_solutions_21-30') + 
                                        '/euler_txt/names1.txt') as f:
        name_list = f.read()
    name_list = name_list.replace('"', '')
    name_list = sorted(name_list.split(','))
    return sum([(v + 1) * sum([ord(i) - 64 for i in k]) 
                for v,k in enumerate(name_list)])

print "Answer: %s" % euler_22()
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)

