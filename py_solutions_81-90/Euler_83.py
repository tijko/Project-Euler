#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Minimal path in a 80x80 matrix, from top left node to bottom right node.
Moving up, down, left, or right directions.
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

traveled = [['inf'] * 80 for i in xrange(80)]

x = y = 0
heap = [[y, x]]

def euler_83(y, x):
    bounds = 80 
    r_vertex = d_vertex = u_vertex = l_vertex = False 
    if traveled[y][x] == 'inf':
        traveled[y][x] = curr = edges[y][x]
    else:
        curr = traveled[y][x]
    if x + 1 >= bounds and y + 1 >= bounds: 
        return
    if y + 1 < bounds:
        d_vertex = d_edge(y, x, curr)
    if x + 1 < bounds:
        r_vertex = r_edge(y, x, curr)
    if y - 1 >= 0:  
        u_vertex = u_edge(y, x, curr)
    if x - 1 >= 0:
        l_vertex = l_edge(y, x, curr)
    mvs = {d_vertex:'d_vertex',
           r_vertex:'r_vertex',
           u_vertex:'u_vertex',
           l_vertex:'l_vertex'
          }
    if any(mvs):
        mvs = {k:v for k,v in mvs.items() if k}
        next_mv = min(mvs)
        heap_mv = [mv for mv in mvs.values() if mv != mvs[next_mv]]
        push_heap(y, x, heap_mv)
        if mvs[next_mv] == 'd_vertex':
            euler_83(y+1, x)
        elif mvs[next_mv] == 'r_vertex':
            euler_83(y, x+1)
        elif mvs[next_mv] == 'u_vertex':
            euler_83(y-1,x)
        else:
            euler_83(y,x-1)
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

def l_edge(y, x, curr):
    l_vertex = curr + edges[y][x-1]
    if traveled[y][x-1] == 'inf':
        traveled[y][x-1] = l_vertex
    elif l_vertex < traveled[y][x-1]:
        traveled[y][x-1] = l_vertex
    else:
        l_vertex = False
    return l_vertex

def push_heap(y, x, heap_mv):
    mv_coor = {'d_vertex':[y+1,x],
               'r_vertex':[y,x+1],
               'u_vertex':[y-1,x],
               'l_vertex':[y,x-1]
              }
#    [heap.append(mv_coor[i]) for i in heap_mv]
    heap.extend([mv_coor[i] for i in heap_mv])
    return

while heap:
    y, x = heap.pop(0)
    euler_83(y, x)      

stop = timeit.default_timer()
print "Answer: %d" % traveled[79][79]
print "Time: %f" % (stop - start)


