# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 13:16:25 2020

@author: Ankit Parashar
"""
#! saveThePrisoner.py

def saveThePrisoner(n, m, s):
    # i = 0
    # s = s-1
    # while i in range(m):
    #     s += 1
    #     i += 1
    #     if ((s == n) & (i != m)):
    #         s = 0
    
    # return s
    rem = m % n
    s = s - 1
    i = 0
    while i in range(m):
        if (i == rem):
            break       
        if s == n:
            s = 0
        i += 1
        s += 1
    return s

print(saveThePrisoner(436776012, 436776012, 436776011))
#print(saveThePrisoner(3, 7, 3))
#print(saveThePrisoner(7, 19, 2))