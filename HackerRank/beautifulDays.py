# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 15:16:06 2020

@author: HP
"""
#!beautifulDays.py

def beautifulDays(i, j, k):
    bDays = 0
    for num in range(i, j + 1):
        revNum = int(''.join(list(reversed(list(str(num))))))
        if abs(revNum - num) % k == 0:
            bDays += 1
    return bDays

print(beautifulDays(20, 23, 6))