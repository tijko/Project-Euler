#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
The heart of this problem concerns the likelihood of visiting a particular 
square. That is, the probability of finishing at that square after a roll.
For this reason it should be clear that, with the exception of G2J for which
the probability of finishing on it is zero, the CH squares will have the 
lowest probabilities, as 5/8 request a movement to another square, and it is
the final square that the player finishes at on each roll that we are interested
in. We shall make no distinction between "Just Visiting" and being sent to JAIL,
and we shall also ignore the rule about requiring a double to "get out of jail",
assuming that they pay to get out on their next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 we can
concatenate these two-digit numbers to produce strings that correspond with 
sets of squares.

Statistically it can be shown that the three most popular squares, in order, 
are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and 
GO (3.09%) = Square 00. So these three most popular squares can be listed 
with the six-digit modal string: 102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the 
six-digit modal string.
'''

from __future__ import print_function

import timeit
from itertools import cycle
from random import choice, shuffle
from collections import defaultdict


def euler_84():
    squares = ['go', 'a1', 'cc1', 'a2', 't1', 'r1', 'b1', 'ch1', 'b2', 'b3',
               'jail', 'c1', 'u1', 'c2', 'c3', 'r2', 'd1', 'cc2', 'd2', 'd3',
               'fp', 'e1', 'ch2', 'e2', 'e3', 'r3', 'f1', 'f2', 'u2', 'f3',
               'g2j', 'g1', 'g2', 'cc3', 'g3', 'r4', 'ch3', 'h1', 't2', 'h2']
    visits = defaultdict(int)
    cc_cards = ['go', 'jail'] + [None] * 14 
    ch_cards = (['go', 'jail', 'c1', 'e3', 'h2', 'r1', 'nextr', 
                 'nextr', 'nextu', 'back'] + [None] * 6)
    shuffle(cc_cards); shuffle(ch_cards)
    cc, ch= cycle(cc_cards), cycle(ch_cards)
    rolls = [(i, j) for i in range(1, 5) for j in range(1, 5)]
    doubles = pos = 0 
    for _ in range(100000):
        roll = choice(rolls)
        if roll[0] == roll[1]:
            doubles += 1
            if doubles == 3:
                pos = squares.index('jail')
                visits['jail'] += 1
                doubles = 0
        else:
            doubles = 0 
            pos += sum(roll)
            pos = pos % 40
            sq = squares[pos]
            if sq.startswith('cc'):
                card = next(cc)
                if card is None:
                    visits[sq] += 1
                else:
                    pos = squares.index(card)
                    visits[card] += 1
            elif sq.startswith('ch'):
                card = next(ch)
                if card is None:
                    visits[sq] += 1
                else:
                    if card.startswith('next'):
                        if card == 'nextr':
                            if pos > 35 or pos < 5:
                                pos = 5
                            elif pos > 5 and pos < 15:
                                pos = 15
                            elif pos > 15 and pos < 25:
                                pos = 25
                            else:
                                pos = 35
                        else:
                            if pos > 28 or pos < 12:
                                pos = 12
                            else:
                                pos = 28
                    elif card == 'back':
                        pos -= 3
                        sq = squares[pos]
                        if sq == 'ch3':
                            card = next(cc)
                            if card is None:
                                visits[sq] += 1
                            else:
                                pos = squares.index(card)
                                visits[card] += 1
                    else:
                        pos = squares.index(card)
                        visits[card] += 1
            elif sq == 'g2j':
                pos = squares.index('jail')
                visits['jail'] += 1
            else:
                visits[sq] += 1 
    visit_items = visits.items()
    visit_items = sorted(visit_items, key=lambda x: x[1], reverse=True)
    return ''.join([str(squares.index(sq[0])) for sq in visit_items[:3]])
    
if __name__ == "__main__":
    start = timeit.default_timer()
    print('Answer: {}'.format(euler_84()))
    stop = timeit.default_timer()
    print('Time: {0:9.5f}'.format(stop - start))
