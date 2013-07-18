# decrypt file 

import itertools
import timeit
import os


start = timeit.default_timer()

def euler_59():
    frequent_wrds = ['the ', 'of ', 'and ', 'a ', 'to ', 'in ', 'is ', 'you ', 'that ', 'it ']
    '''
        "frequent_wrds" is a list of the top ten most frequently
        used words in english.  According to --->
        http://duboislc.org/EducationWatch/First100Words.html
    '''
    with open(os.path.abspath('').strip('solutions_51-60') + '/euler_txt/cipher1.txt') as f:
        encrypted_message = f.read() 
    keys = [i for i in xrange(97, 123)]
    keys = [i for i in itertools.combinations(keys, 3)] 
    message = [int(i.strip('\r\n')) for i in encrypted_message.split(',')]
    for key in keys:
        for i in [v for v in itertools.permutations(key)]:
            msg = list()
            kyd = 0 
            for x in message:
                cip = ''
                x = bin(x) 
                y = bin(i[kyd]) 
                x = x[2:][::-1] 
                y = y[2:][::-1] 
                for j in xrange(len(x)):
                    if y[j] == x[j]: 
                        cip += '0' 
                    if y[j] != x[j]: 
                        cip += '1' 
                cip += y[len(x):]
                cip = cip[::-1] 
                cip = chr(int(cip, 2)) 
                msg.append(cip)
                kyd += 1
                if kyd == 3:
                    kyd = 0 
            if len([i for i in frequent_wrds if i in ''.join(msg)]) > 5:
                print sum([ord(i) for i in ''.join(msg)])
                return ''.join(msg) + '\n'

print "Answer: %s" % euler_59()
stop = timeit.default_timer()
print "Time: %s" % str(stop - start)
