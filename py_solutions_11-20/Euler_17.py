# -*- coding: utf-8 -*-

from __future__ import print_function

'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in 
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
'''

import timeit


start = timeit.default_timer()

def euler_17():
    number_words = [['', 'one', 'two', 'three', 'four', 'five', 
                     'six', 'seven', 'eight', 'nine'], 
                    ['ten', 'eleven', 'twelve', 'thirteen', 
                     'fourteen', 'fifteen', 'sixteen', 
                     'seventeen', 'eighteen', 'nineteen'],
                    ['twenty', 'thirty', 'forty', 'fifty', 
                     'sixty', 'seventy', 'eighty', 'ninety'],
                    ['hundred', 'hundredand'],
                    ['thousand']]
    letter_count = number = 0
    while number < 1000:
        number += 1
        curr = number
        if curr // 1000:
            letter_count += (len(number_words[0][curr // 1000]) +
                             len(number_words[4][0]))
        curr %= 1000
        if curr // 100 and not curr % 100:
            letter_count += (len(number_words[0][curr // 100]) + 
                             len(number_words[3][0]))
            continue
        if curr // 100:
            letter_count += (len(number_words[0][curr // 100]) +
                             len(number_words[3][1]))
        curr %= 100
        if curr // 10 == 1:
            letter_count += len(number_words[1][curr % 10])
            continue
        if curr // 10:
            letter_count += len(number_words[2][(curr // 10) - 2])
        curr %= 10
        letter_count += len(number_words[0][curr % 10])
    return letter_count


print("Answer: {}".format(euler_17()))
stop = timeit.default_timer()
print("Time: {0:9.5f}".format(stop - start))
