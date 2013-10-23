#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Minimal path in 80x80 matrix, going from any node on left to
any node on right.  Moving only in up, down, or right directions.
'''

import timeit
import os

start = timeit.default_timer()

global edges
global traveled
global heap

path = os.getcwd().strip('py_solutions_81-90')

with open(path + 'euler_txt/matrix.txt') as f:
    grid = f.read()

edges = [[int(i) for i in v.split(',')] for v in grid.split('\r\n') if v]      

def traveler():
    paths = []
    for i in range(80): 
        row = ['inf'] * 80
        paths.append(row)
    return paths

traveled = traveler() 

def euler_82(y, x):
    bounds = 80 
    r_vertex = d_vertex = u_vertex = False 
    if traveled[y][x] == 'inf':
        traveled[y][x] = curr = edges[y][x]
    else:
        curr = traveled[y][x]
    if x + 1 >= bounds: 
        return
    if y + 1 < bounds:
        d_vertex = curr + edges[y+1][x]
        if traveled[y+1][x] == 'inf':
            traveled[y+1][x] = d_vertex
        elif curr + edges[y+1][x] < traveled[y+1][x]:
            traveled[y+1][x] = d_vertex 
        else:
            d_vertex = False
    if x + 1 < bounds:
        r_vertex = curr + edges[y][x+1]
        if traveled[y][x+1] == 'inf':
            traveled[y][x+1] = r_vertex
        elif curr + edges[y][x+1] < traveled[y][x+1]:
            traveled[y][x+1] = r_vertex
        else:
            r_vertex = False
    if y - 1 >= 0:  
        u_vertex = curr + edges[y-1][x]
        if traveled[y-1][x] == 'inf':
            traveled[y-1][x] = u_vertex
        elif curr + edges[y-1][x] < traveled[y-1][x]:
            traveled[y-1][x] = u_vertex
        else:
            u_vertex = False
    mvs = {d_vertex:'d_vertex',
           r_vertex:'r_vertex',
           u_vertex:'u_vertex'
          }
    if any(mvs):
        mvs = {k:v for k,v in mvs.items() if k}
        next_mv = min(mvs)
        if mvs[next_mv] == 'd_vertex':
            if 'r_vertex' in mvs.values():
                heap.append([y,x+1])
            if 'u_vertex' in mvs.values():
                heap.append([y-1,x])
            euler_82(y+1, x)
        elif mvs[next_mv] == 'r_vertex':
            if 'd_vertex' in mvs.values():
                heap.append([y+1,x])
            if 'u_vertex' in mvs.values():
                heap.append([y-1,x])
            euler_82(y, x+1)
        else:
            if 'd_vertex' in mvs.values():
                heap.append([y+1, x])
            if 'r_vertex' in mvs.values():
                heap.append([y,x+1])
            euler_82(y-1,x)
    else:
        return    

sopf = list()
cols = [[i, 0] for i in range(80)]  
for col in cols:
    heap = [col]
    while heap:
        y, x = heap.pop(0)
        euler_82(y, x)      
    small = [traveled[i][79] for i in range(80) if traveled[i][79] != 'inf']
    sopf.append(min(small))
    traveled = traveler()

stop = timeit.default_timer()
print "Answer: %d" % min(sopf)
print "Time: %f" % (stop - start)


