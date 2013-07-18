# triangle numbers and a word list 

import timeit
import os


start = timeit.default_timer()

def euler_42():
    total = 0
    triangle_numbers = [int((i * 0.5) * (i + 1)) for i in xrange(1, 101)]
    with open(os.path.abspath('').strip('solutions_41-50') + '/euler_txt/words1.txt') as f:
        words = f.read()
    words = [i for i in words.split('"') if i != ',' and i != '']
    for word in words:
        wrd_value = 0
        for i in word:
            wrd_value += (ord(i) - 64)       
        if wrd_value in triangle_numbers:
            total += 1
    return total    

print "Answer: %s" % euler_42()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
