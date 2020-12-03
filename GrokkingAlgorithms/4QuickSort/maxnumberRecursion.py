# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 16:12:16 2020

@author: Ankit Parashar
"""
#! maxnumberRecursion.py

def maxNumber(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = maxNumber(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

print(maxNumber([2, 3, 4, 5, 6, 7, 8, 9]))