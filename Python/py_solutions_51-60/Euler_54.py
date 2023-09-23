#!/usr/bin/env python
# -*- coding: utf-8 -*-

# poker hands -- calculate the amount of winning hands for player-one for the 
# last thousand hands vs. player-two

from __future__ import print_function

import timeit
import os


start = timeit.default_timer()

def score(hand):
    hand_value = {'RFlsh':1000, 'Str8Flsh':900, '4kind':800, 'Flhse':700, 'Flsh':600,
                   'Str8':500, '3kind':400, '2pair':300, '1kind':200, 'Hcard':100}
    pair_value = {17:'4kind', 13:'Flhse', 11:'3kind', 9:'2pair', 7:'1kind', 5:'Hcard'}
    card_value = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10, '9':9, 
                  '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}
    suits = [i[1] for i in hand]
    cards = [i[0] for i in hand]
    if all(suits.count(i) == 5 for i in suits):
        str8_chk = sorted([card_value[i] for i in cards])        
        if str8_chk == range(str8_chk[0], str8_chk[4] + 1):
            if sum(str8_chk) == 60:
                return hand_value['RFlsh']
            return hand_value['Str8Flsh']
        return hand_value['Flsh'] 
    total = hand_value[pair_value[sum([cards.count(i) for i in cards])]]       
    card = [cards.count(i) for i in cards]
    card = cards[card.index(max(card))]
    if total == 100:
        str8_chk = sorted([card_value[i] for i in cards])
        if str8_chk == range(str8_chk[0], str8_chk[4] + 1):
            return hand_value['Str8']
        return max([card_value[i] for i in cards])
    return total + card_value[card]

def euler_54():
    p1_wins = 0
    with open('/home/tijko/Project-Euler/euler_txt/poker.txt') as f:
        hands = [i.strip('\n') for i in f.readlines()]
    p1 = [i[:14] for i in hands]
    p2 = [i[15:] for i in hands]
    for i in zip(p1, p2):
        if score(i[0].split()) > score(i[1].split()):
            p1_wins += 1
    return p1_wins


print("Answer: %s" % euler_54())
stop = timeit.default_timer()
print("Time: %s" % str(stop - start))

