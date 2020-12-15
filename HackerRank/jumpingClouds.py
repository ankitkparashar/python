# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 23:41:20 2020

@author: Ankit Parashar
"""
#! jumpingClouds.py

def jumpingClouds(c, k):
    e = 100
    i = 0
    n = len(c)
    while True:
        if ((i + k) == n):
            i = 0
        elif ((i + k) > n):
            i = i + k - n
        else:
            i += k
        
        if i == 0:
            if c[i] == 0:
                return e-1
            else:
                return e-3
        elif c[i] == 0:
            e -= 1
        else:
            e -= 3
    return e

#print(jumpingClouds([0, 0, 1, 0, 0, 1, 1, 0], 2))
print(jumpingClouds([1, 1, 1, 0, 1, 1, 0, 0, 0, 0], 3))