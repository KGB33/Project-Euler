# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 00:28:55 2018

@author: kelto
"""
"""
Lattice paths
Problem 15 
Starting in the top left corner of a 2×2 grid, and only being able to move 
to the right and down, there are exactly 6 routes to the bottom right corner.

https://projecteuler.net/project/images/p015.gif

How many such routes are there through a 20×20 grid?
"""

"""
Note, each route for a NxN grid has N Right arrows, and N Down Arrows
thus the permuataion of [R1, R2, ..., Rn, D1, D2, ... Dn]
gives all possible routes

i.e N!
"""

"""
Answer: Incompleat
"""
import time, random

def main(start_time):
    size = 20
    down_moves = gen_moves('D', size)
    right_moves = gen_moves('R', size)
    paths = []
    now = time.clock()
    while now < start_time + 20000:
    #for k in range(1000000):
        path = []
        for i in range(size * 2):
            #if the bottom row has been reached, adds the remaining right moves
            if set(down_moves).issubset(path):
                for move in right_moves:
                    if move not in path:
                        path = path + [move]
                        #print("all r moves", path)
            #if the rightmost collom has been reached, adds the remaining down moves
            elif set(right_moves).issubset(path):
                for move in down_moves:
                    if move not in path:
                        path = path + [move]
                        #print("all d moves", path)
            else:
                right_or_down = bool(random.getrandbits(1))
                if right_or_down:
                    for move in right_moves:
                        if move not in path:
                            path = path + [move]
                            #print('add r move ', path)
                            break
                else:
                    for move in down_moves:
                        if move not in path:
                            path = path + [move]
                            #print('add d move', path)
                            break
                        
        #print ("Final path: ", path, '\n\n')
        now = time.clock()
        
        if path not in paths:
            paths = paths + [path]
        
    print (len(paths))

def gen_moves(direction, size):
    moves = [direction + str(n) for n in range(size)]
    return moves
 
    

print("Running, do not shut off Computer...")
start_time = time.clock()
main(start_time)
print("Time: ", time.clock() - start_time)