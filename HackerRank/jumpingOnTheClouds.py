# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 20:20:07 2020

@author: Ankit Parashar
"""
#! jumpingOntheClouds.py

def jumpingOntheClouds(c):
    clouds = len(c)
    i = 0
    moves = 0
    while i != clouds-1:
        if (i + 2) < clouds:
            if c[i + 2] == 1:
                i += 1
            else:
                i += 2
        else:
            i += 1
        moves += 1
    return moves

print(jumpingOntheClouds([0, 0, 1, 0, 0, 1, 0]))
#print(jumpingOntheClouds([0, 1, 0, 0, 0, 1, 0]))
#print(jumpingOntheClouds([0, 0, 0, 1, 0, 0]))