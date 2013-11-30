# triangle numbers and a word list 

import timeit
import os


start = timeit.default_timer()

def euler_42():
    triangle_numbers = [int((i * 0.5) * (i + 1)) for i in xrange(1, 101)]
    with open(os.path.abspath('').strip('py_solutions_41-50') + 
                                        '/euler_txt/words1.txt') as f:
        words = f.read()
    words = [i for i in words.split('"') if i and i != ',']
    return sum([1 for i in words if 
               sum([ord(j) - 64 for j in i]) in triangle_numbers])

print "Answer: %s" % euler_42()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
