# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 18:23:03 2021

@author: Ankit Parashar
"""
#! fairRations.py

def fairRations(b):
    loaves = 0
    people = len(b)
    for i in range(people):
        if b[i] % 2 != 0:
            if i != people - 1:
                b[i] += 1
                loaves += 1
                b[i + 1] += 1
                loaves += 1
    for a in b:
        if a % 2 != 0:
            return "NO"
    return loaves

#print(fairRations([2, 3, 4, 5, 6]))
#print(fairRations([4, 5, 6, 7]))
print(fairRations([1, 2]))