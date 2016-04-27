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
    sqs_list = [i*i for i in range(sq_low, sq_high + 1)]
    possible_digit_subs = defaultdict(list)
    for sq in sqs_list:
        sq_str = str(sq)
        sq_len = len(sq_str)
        if len({i for i in sq_str}) != sq_len: continue
        possible_digit_subs[sq_len].append(sq)
    return possible_digit_subs

def euler_98():
    anagram_pairs = find_anagram_pairs()
    sq_low = 10**(len(min(anagram_pairs, key=len)) - 1)
    sq_high = int(sqrt(10**len(max(anagram_pairs, key=len)) - 1)) + 1
    sqs_dict = create_subs(sq_low, sq_high)
    high = 0
    for anagram1 in anagram_pairs:
        anagram2 = anagram_pairs[anagram1]
        anagram_length = len(anagram1)
        sqs_list = sqs_dict[anagram_length]
        for sq in sqs_list:
            pair_sq_dict = dict(zip(anagram1, str(sq)))
            a1 = int(''.join([pair_sq_dict[i] for i in anagram1]))
            a2 = int(''.join([pair_sq_dict[i] for i in anagram2]))
            if a2 in sqs_list:
                pair_high = max([a1, a2])
                if pair_high > high:
                    high = pair_high
    return high

if __name__ == '__main__':
    start = timeit.default_timer()
    print('Answer: {}'.format(euler_98()))
    stop = timeit.default_timer()
    print('Time: {0:9.5f}'.format(stop - start)) 
