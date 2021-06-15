# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 23:44:35 2021

@author: Ankit Parashar
"""
#!  serviceLane.py

def serviceLane(n, cases):
    width = []
    for i in range(n):
        width.append(int(input()))
    lanes = []
    for case in cases:
        lanes.append(min(width[case[0]: case[1] + 1]))
    return lanes

#print(serviceLane([2, 3, 2, 1], [[1, 2], [2, 4]]))
print(serviceLane([2, 3, 1, 2, 3, 2, 3, 3], [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]))