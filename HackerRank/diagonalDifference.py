# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 22:56:39 2020

@author: Ankit Parashar
"""
#! diagonalDifference.py

def diagonalDifference(ar):
    if len(ar) == len(ar[0]):
        size = len(ar)
        sumPd = 0
        sumSd = 0
        for i in range(size):
            for j in range(size):
                if (i == j):
                    sumPd += ar[i][j]
                
        a = 0
        b = size - 1
        while a < size:
            while b >= 0:
                sumSd += ar[a][b]
                b -= 1
                break
            a += 1
            
    return abs(sumPd - sumSd)

print(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))