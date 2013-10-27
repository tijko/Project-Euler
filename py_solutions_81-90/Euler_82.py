#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Minimal path in 80x80 matrix, going from any node on left to
any node on right.  Moving only in up, down, or right directions.
'''

import timeit
import os

start = timeit.default_timer()

path = os.getcwd().strip('py_solutions_81-90')

with open(path + 'euler_txt/matrix.txt') as f:
    grid = f.read()

edges = [[int(i) for i in v.split(',')] for v in grid.split('\r\n') if v]      

traveler = lambda: [['inf'] * 80 for i in xrange(80)]

def euler_82(y, x):
    bounds = 80 
    r_vertex = d_vertex = u_vertex = False 
    if traveled[y][x] == 'inf':
        traveled[y][x] = curr = edges[y][x]
    else:
        curr = traveled[y][x]
    if x + 1 >= bounds: 
        if traveled[y][x] < sopf[0]:
            sopf[0]= traveled[y][x]
        return
    if y + 1 < bounds:
        d_vertex = d_edge(y, x, curr)
    if x + 1 < bounds:
        r_vertex = r_edge(y, x, curr)
    if y - 1 >= 0:  
        u_vertex = u_edge(y, x, curr)
    mvs = {d_vertex:'d_vertex',
           r_vertex:'r_vertex',
           u_vertex:'u_vertex'
          }
    mvs = {k:v for k,v in mvs.items() if k}
    if any(mv<sopf[0] for mv in mvs):
        min_mv(mvs, y, x)
    else:
        return    

def d_edge(y, x, curr):
    d_vertex = curr + edges[y+1][x]
    if traveled[y+1][x] == 'inf':
        traveled[y+1][x] = d_vertex
    elif d_vertex < traveled[y+1][x]:
        traveled[y+1][x] = d_vertex 
    else:
        d_vertex = False
    return d_vertex

def r_edge(y, x, curr):
    r_vertex = curr + edges[y][x+1]
    if traveled[y][x+1] == 'inf':
        traveled[y][x+1] = r_vertex
    elif r_vertex < traveled[y][x+1]:
        traveled[y][x+1] = r_vertex
    else:
        r_vertex = False
    return r_vertex

def u_edge(y, x, curr):
    u_vertex = curr + edges[y-1][x]
    if traveled[y-1][x] == 'inf':
        traveled[y-1][x] = u_vertex
    elif u_vertex < traveled[y-1][x]:
        traveled[y-1][x] = u_vertex
    else:
        u_vertex = False
    return u_vertex

def min_mv(mvs, y, x):
    next_mv = min(mvs)
    heap_mv = [mv for mv in mvs.values() if mv != mvs[next_mv]]
    push_heap(y, x, heap_mv)
    if mvs[next_mv] == 'd_vertex':
        euler_82(y+1, x)
    elif mvs[next_mv] == 'r_vertex':
        euler_82(y, x+1)
    else:
        euler_82(y-1,x)
    return

def push_heap(y, x, heap_mv):
    mv_coor = {'d_vertex':[y+1,x],
               'r_vertex':[y,x+1],
               'u_vertex':[y-1,x]
              }
    heap.extend([mv_coor[i] for i in heap_mv])
    return

sopf = [999999] 
cols = [[i, 0] for i in xrange(80)]  
for col in cols:
    heap = [col]
    traveled = traveler()
    while heap:
        y, x = heap.pop(0)
        euler_82(y, x)      

stop = timeit.default_timer()
print "Answer: %d" % sopf[0]
print "Time: %f" % (stop - start)
