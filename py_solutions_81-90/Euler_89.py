#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
For a number written in Roman numerals to be considered valid there are basic 
rules which must be followed. Even though the rules allow some numbers to be 
expressed in more than one way there is always a "best" way of writing a 
particular number.

For example, it would appear that there are at least six ways of writing the
number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, and the last 
example is considered to be the most efficient, as it uses the least number 
of numerals.

Find the number of characters saved by writing each of these in their minimal
form.
'''

from __future__ import print_function

import os
import timeit

from math import floor
from itertools import groupby

from time import sleep

def euler_89():
    path = os.getcwd().strip('py_solutions_81-90')
    numeral_values = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    shorts = {'M':1000, 'CM':900, 'DCCC':800, 'DCC':700, 'DC':600, 'D':500, 
              'CD':400, 'CCC':300, 'CC':200, 'C':100, 'XC':90, 'LXXX':80,
              'LXX':70, 'LX':60, 'L':50, 'XL':40, 'XXX':30, 'XX':20, 'X':10, 
              'IX':9, 'VIII':8, 'VII':7, 'VI':6, 'V':5, 'IV':4, 'I':1}
    shorts = {v:k for k,v in shorts.items()}
    txt_value = {}
    saved_chars = 0
    with open(path + '/euler_txt/roman_numerals.txt') as f:
        numerals = [i.strip('\n') for i in f.readlines()]
    for numeral in numerals:
        lst = [[k,list(g)] for k,g in groupby(numeral, lambda n: numeral_values[n])]
        total = 0
        for i,v in enumerate(lst):
            try:
                if v[0] < lst[i + 1][0]:
                    total -= v[0] * len(v[1])
                else:
                    total += v[0] * len(v[1])
            except IndexError:
                total += v[0] * len(v[1])
        txt_value[numeral] = total
        low_str = ''
        for n in sorted(shorts.keys())[::-1]:
            if n > total: continue
            low_str += (floor(total / n) * shorts[n])
            total %= n
        if len(low_str) < len(numeral):
            saved_chars += (len(numeral) - len(low_str))
    return saved_chars

if __name__ == '__main__':
    start = timeit.default_timer()
    print("Answer: {}".format(euler_89()))
    stop = timeit.default_timer()
    print("Time: {0:9.5f}".format(stop - start))
