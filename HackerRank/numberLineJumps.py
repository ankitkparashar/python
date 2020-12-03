# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:31:20 2020

@author: Ankit Parashar
"""
#! numberLineJumps.py

def kangaroo(x1, v1, x2, v2):
    if (v2 > v1):
        return False
    elif (v2 < v1):
        if ((x2 - x1) % (v1-v2) == 0):
            return True
    return False

#print(kangaroo(0, 3, 4, 2))
#print(kangaroo(0, 2, 5, 3))
print(kangaroo(1408, 6689, 6730, 4028))