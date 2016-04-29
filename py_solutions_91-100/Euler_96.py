#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Su Doku (Japanese meaning number place) is the name given to a popular puzzle 
concept. Its origin is unclear, but credit must be attributed to Leonhard Euler 
who invented a similar, and much more difficult, puzzle idea called Latin 
Squares. The objective of Su Doku puzzles, however, is to replace the blanks (or 
zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 box contains 
each of the digits 1 to 9. Below is an example of a typical starting puzzle grid 
and its solution grid.

A well constructed Su Doku puzzle has a unique solution and can be solved by 
logic, although it may be necessary to employ "guess and test" methods in order 
to eliminate options (there is much contested opinion over this). The complexity 
of the search determines the difficulty of the puzzle; the example above is 
considered easy because it can be solved by straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), 
contains fifty different Su Doku puzzles ranging in difficulty, but all with 
unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the 
top left corner of each solution grid; for example, 483 is the 3-digit number 
found in the top left corner of the solution grid above.
'''

from __future__ import print_function
from os import getcwd

import timeit


def get_boards():
    cwd = getcwd()
    boards = []
    with open(cwd.strip('py_solutions_91-100') + 'euler_txt/sudoku.txt') as f:
        for line in f.readlines():
            if line.startswith('Grid'):
                boards.append([])
            else:
                grid_line = line.strip('\n')
                boards[-1].append(list(map(int, grid_line)))
    return boards

def get_row_neighbors(pos, board):
    neighbors = []
    y_pos = pos[1]
    for x in range(9):
        if not board[x][y_pos]: continue
        neighbors.append(board[x][y_pos]) 
    return neighbors

def get_col_neighbors(pos, board):
    neighbors = []
    x_pos = pos[0]
    for y in range(9):
        if not board[x_pos][y]: continue
        neighbors.append(board[x_pos][y])
    return neighbors

def get_sq_neighbors(pos, board):
    neighbors = []
    x_pos, y_pos = pos[0] - (pos[0] % 3), pos[1] - (pos[1] % 3)
    for x in range(3):
        for y in range(3):
            if not board[x_pos + x][y_pos + y]: continue
            neighbors.append(board[x_pos + x][y_pos + y])
    return neighbors

# could be used as a check
# e.g. if no positions available -> backtrack...
def find_options(pos, board):
    all_options = {i for i in range(1, 10)}
    row_neighbors = get_row_neighbors(pos, board)
    col_neighbors = get_col_neighbors(pos, board)
    sq_neighbors = get_sq_neighbors(pos, board)
    return sorted(list(all_options ^ {*row_neighbors, 
                                      *col_neighbors, 
                                      *sq_neighbors}))

def forward(x, y):
    x += 1
    if x > 8:
        x = 0
        y += 1
    return (x, y)

def backwards(x, y):
    x -= 1
    if x < 0:
        x = 8
        y -= 1
    return (x, y)    

def solver(board):
    x, y = (0, 0)
    # maintain positions, this allows
    # 1.) check if .get is None
    # 2.) check if .get is empty
    position_options = {}
    # use a direction vector
    mv_dir = forward
    while y < 9:
        opts = position_options.get((x, y))
        if opts is None and board[x][y]:
            position_options[(x, y)] = 'given'
            x, y = mv_dir(x, y)
        elif opts == 'given':
            x, y = mv_dir(x, y)    
        else:
            # exhaust the options list first before backtracking
            if opts is None or board[x][y] == 0:
                options = find_options((x, y), board)
            else:
                options = opts
            # check options length
            if len(options) == 0:
                # if backtracking is needed set back to zero
                board[x][y] = 0
                mv_dir = backwards
                x, y = mv_dir(x, y)
            else:
                position_options[(x, y)] = options[1:]
                board[x][y] = options[0]
                mv_dir = forward
                x, y = mv_dir(x, y)
    return int(''.join(map(str, board[0][:3])))

def euler_96():
    boards = get_boards()
    solved_total = 0
    for board in boards:
        solved_total += solver(board)
    return solved_total

if __name__ == '__main__':
    start = timeit.default_timer()
    print('Answer: {}'.format(euler_96()))
    stop = timeit.default_timer()
    print('Time: {0:9.5f}'.format(stop - start))
