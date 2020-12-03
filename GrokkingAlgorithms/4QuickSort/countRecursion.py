# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 16:04:32 2020

@author: Ankit Parashar
"""
#! countRecursion.py

def counts(arr):
    if arr == []:
        return 0
    return 1 + counts(arr[1:])

print(counts([2, 3, 4, 5, 6, 7, 8, 9]))