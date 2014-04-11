# Number amount of names

import timeit
import os


start = timeit.default_timer()

def euler_22():
    with open(os.path.abspath('').strip('py_solutions_21-30') + 
                                        '/euler_txt/names1.txt') as f:
        name_list = f.read()
    name_list = name_list.replace('"', '')
    name_list = sorted(name_list.split(','))
    return sum([v * sum(map(lambda x: ord(x) - 64, k)) 
                for v, k in enumerate(name_list, 1)])

print "Answer: %s" % euler_22()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)

