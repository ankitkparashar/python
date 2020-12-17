# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 20:55:16 2020

@author: Ankit Parashar
"""
#! equalizeArray.py

def equalizeArray(arr):
    counts = {}
    for i in arr:
        if i not in counts:
            counts[i] = 1
        else:
            counts[i] += 1
    return len(arr) - max(counts.values())

#print(equalizeArray([3, 3, 2, 1, 3]))
print(equalizeArray([1, 2, 2, 3]))