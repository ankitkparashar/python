# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 20:46:48 2020

@author: Ankit Parashar
"""
#! divisibleSumPairs.py

from itertools import combinations

def divisibleSumPairs(n, k, ar):
    if n == 2:
        if sum(ar) % k == 0:
            return 1
        else:
            return 0
    if k == 1:
        return len(list(combinations(ar, 2)))
    
    pairs = 0
    for i in range(n):
        for j in range(i + 1, n):
            if ((ar[i] + ar[j]) % k) == 0:
                pairs += 1
    return pairs

#print(divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]))
print(divisibleSumPairs(6, 5, [1, 2, 3, 4, 5, 6]))