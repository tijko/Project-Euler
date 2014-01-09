# decrypt file 

import itertools
import timeit
import os


start = timeit.default_timer()

def euler_59():
    frequent_wrds = {'the', 'of', 'and', 'a', 'to', 'in', 'is', 'you', 'that', 'it'}
    '''
        "frequent_wrds" is a list of the top ten most frequently
        used words in english.  According to --->
        http://duboislc.org/EducationWatch/First100Words.html
    '''
    strip = lambda s: s.strip('\r\n')
    alpha = lambda a: chr(int(a, 2))
    binry = lambda b: b[2:][::-1]
    with open(os.path.abspath('').strip('py_solutions_51-60') + 
              '/euler_txt/cipher1.txt') as f:
        encrypted_message = map(strip, f.read().split(',')) 
    keys = itertools.combinations(xrange(97, 123), 3)
    message = map(int, encrypted_message)
    for key in keys:
        for i in itertools.permutations(key):
            msg = '' 
            kyd = itertools.cycle(map(bin, i)) 
            for x in map(binry, map(bin, message)):
                y = binry(kyd.next())
                msg += alpha((''.join('0' if x[j] == y[j] else '1' for 
                              j in xrange(len(x))) + y[len(x):])[::-1])
            if len(frequent_wrds.intersection(msg.split())) > 5:                
                return ''.join(msg) 

print "Answer: %s" % euler_59()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
