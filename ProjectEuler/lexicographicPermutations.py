# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 19:34:26 2020

@author: Ankit Parashar
"""
#! lexicographicPermutations.py

from itertools import permutations

def lexicographicPermutations(n):
    perm = []
    for i in permutations(range(n)):
        a = ''.join(list(map(str, i)))
        perm.append(a)
    return perm[999999]

print(lexicographicPermutations(10))