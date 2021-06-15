# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 21:44:31 2021

@author: Ankit Parashar
"""
#! flatlandSpaceStations.py

def flatlandSpaceStations(n, c):
    maxDist = 0
    c = sorted(c)
    size = len(c)
    for i in range(size - 1):
        if i != size - 2:
            dist = (c[i + 1] - c[i]) // 2
        else:
            dist = n - 1 - c[i + 1]
        if dist > maxDist:
            maxDist = dist
    return maxDist

# print(flatlandSpaceStations(5, [0, 4]))
# print(flatlandSpaceStations(99989, [75453, 36129, 64502, 46817]))
# print(flatlandSpaceStations(100, [99]))