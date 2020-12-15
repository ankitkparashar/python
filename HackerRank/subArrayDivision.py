# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 20:16:36 2020

@author: Ankit Parashar
"""
#! subArrayDivision.py

def birthday(s, d, m):
    noOfWays = 0
    size = len(s)
    if (size == 1) & (s[0] == d):
        noOfWays = 1
    else:
        for i in range(size - m + 1):
            sumSubArray = sum(s[i:i+m])
            if sumSubArray == d:
                noOfWays += 1
    return noOfWays

#print(birthday([1, 2, 1, 3, 2], 3, 2))
#print(birthday([1, 1, 1, 1, 1, 1], 3, 2))
#print(birthday([4], 4, 1))
print(birthday([2, 3, 4, 4, 2, 1, 2, 5, 3, 4, 4, 3, 4, 1, 3, 5, 4, 5, 3, 1, 1, 5, 4, 3, 5, 3, 5, 3, 4, 4, 
       2, 4, 5, 2, 3, 2, 5, 3, 4, 2, 4, 3, 3, 4, 3, 5, 2, 5, 1, 3, 1, 4, 2, 2, 4, 3, 3, 3, 3, 4, 
       1, 1, 4, 3, 1, 5, 2, 5, 1, 3, 5, 4, 3, 3, 1, 5, 3, 3, 3, 4, 5, 2], 26, 8))