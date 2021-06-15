# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 22:04:07 2020

@author: Ankit Parashar
"""
#! nonDivisibleSubset.py

from itertools import permutations

def nonDivisibleSubset(k, s):
    subset = []
    for a in permutations(s, 2):
        sumP = sum(a)
        if ((sumP % k) != 0):
            subset.append(a[0])
            subset.append(a[1])
    return len(set(subset))

#print(nonDivisibleSubset(3, [1, 7, 2, 4])
print(nonDivisibleSubset(7, [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]))