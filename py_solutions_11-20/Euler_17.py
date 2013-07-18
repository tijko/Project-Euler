# -*- coding: utf-8 -*-

'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
'''

import timeit


start = timeit.default_timer()

def euler_17():
    new = ''
    new += 'one' * 191 
    new += 'two' * 190
    new += 'three' * 190
    new += 'four'  * 190
    new += 'five'  * 190
    new += 'six'  * 190
    new += 'seven'  * 190
    new += 'eight'  * 190
    new += 'nine' * 190
    new += 'ten' * 10
    new += 'eleven' * 10
    new += 'twelve' * 10
    new += 'thirteen' * 10
    new += 'fourteen' * 10
    new += 'fifteen' * 10
    new += 'sixteen' * 10
    new += 'seventeen' * 10
    new += 'eighteen' * 10
    new += 'nineteen' * 10
    new += 'twenty' * 100
    new += 'thirty' * 100
    new += 'forty' * 100
    new += 'fifty' * 100
    new += 'sixty' * 100
    new += 'seventy' * 100
    new += 'eighty' * 100
    new += 'ninety' * 100
    new += 'hundredand' * 891
    new += 'hundred' * 9
    new += 'thousand' * 1
    return len(new)

print "Answer: %s" % euler_17()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
