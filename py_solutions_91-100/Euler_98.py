#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
By replacing each of the letters in the word CARE with 1, 2, 9, and 6 
respectively, we form a square number: 1296 = 362. What is remarkable is that, 
by using the same digital substitutions, the anagram, RACE, also forms a square 
number: 9216 = 962. We shall call CARE (and RACE) a square anagram word pair and 
specify further that leading zeroes are not permitted, neither may a different 
letter have the same digital value as another letter.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file 
containing nearly two-thousand common English words, find all the square anagram 
word pairs (a palindromic word is NOT considered to be an anagram of itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file.
'''

from __future__ import print_function
from collections import defaultdict
from math import sqrt
from os import getcwd

import timeit


def find_anagram_pairs():
    cwd = getcwd()
    with open(cwd.strip('py_solutions_91-100') + 'euler_txt/words1.txt') as f:
        word_list = [i.strip('\n').replace('"', '') for i in f.read().split(',')]
    anagram_pairs = dict()
    for idx, word1 in enumerate(word_list):
        for word2 in word_list[idx + 1:]:
            if sorted(word1) == sorted(word2):
                anagram_pairs[word1] = word2
    return anagram_pairs

def create_subs(sq_low, sq_high):
    # a dictionary of sq's
    # the key's are the total number of digits in the sq
    # the value is a list of the sq's themselves
    #
    # when going over each anagram pair checking their length
    # against this dict brings up the only possible solutions.
    possible_digit_subs = defaultdict(list)
    for sq in range(sq_low, sq_high + 1):
        sq *= sq
        sq_str = str(sq)
        sq_len = len(sq_str)
        # any sq's with repeat digits are not used
        if len({i for i in sq_str}) != sq_len: continue
        possible_digit_subs[sq_len].append(sq)
    return possible_digit_subs

def euler_98():
    anagram_pairs = find_anagram_pairs()
    # find the length of shortest anagram
    # this will narrow down the range of sq's to check on
    sq_low = 10**(len(min(anagram_pairs, key=len)) - 1)
    # find the length of longest anagram, upper bounds
    sq_high = int(sqrt(10**len(max(anagram_pairs, key=len)) - 1)) + 1
    sqs_dict = create_subs(sq_low, sq_high)
    high = 0
    for anagram1 in anagram_pairs:
        anagram2 = anagram_pairs[anagram1]
        anagram_length = len(anagram1)
        sqs_list = sqs_dict[anagram_length]
        for sq in sqs_list:
            # create a dict of letters of the first anagram zip
            # against the digits of the sq
            pair_sq_dict = dict(zip(anagram1, str(sq)))
            # join the letters in the second anagram
            # check if this integer in is a sq
            a2 = int(''.join([pair_sq_dict[i] for i in anagram2]))
            if a2 in sqs_list:
                pair_high = max([sq, a2])
                if pair_high > high:
                    high = pair_high
    return high

if __name__ == '__main__':
    start = timeit.default_timer()
    print('Answer: {}'.format(euler_98()))
    stop = timeit.default_timer()
    print('Time: {0:9.5f}'.format(stop - start)) 
