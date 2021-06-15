# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 14:22:48 2020

@author: Ankit Parashar
"""
#! minimumDistances.py

def minimumDistances(a):
    size = len(a)
    minDist = float("inf")
    for i in range(size):
        num = a[i]
        for j in range(i + 1, size):
            if a[j] == num:
                if ((j - i) < minDist):
                    minDist = j - i
                    break
    return minDist if minDist != float("inf") else -1

print(minimumDistances([7, 1, 3, 4, 1, 7]))