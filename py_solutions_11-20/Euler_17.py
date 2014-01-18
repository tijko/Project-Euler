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
    return len(''.join(['one' * 191, 'two' * 190, 'three' * 190, 'four' * 190,
                        'five' * 190, 'six' * 190, 'seven' * 190, 'eight' * 190,
                        'nine' * 190, 'ten' * 10, 'eleven' * 10, 'twelve' * 10,
                        'thirteen' * 10, 'fourteen' * 10, 'fifteen' * 10, 
                        'sixteen' * 10, 'seventeen' * 10, 'eighteen' * 10, 
                        'nineteen' * 10, 'twenty' * 100, 'thirty' * 100, 
                        'forty' * 100, 'fifty' * 100, 'sixty' * 100, 
                        'seventy' * 100, 'eighty' * 100, 'ninety' * 100, 
                        'hundredand' * 891, 'hundred' * 9, 'thousand' * 1]))

print "Answer: %s" % euler_17()
stop = timeit.default_timer()
print "Time: %f" % (stop - start)
