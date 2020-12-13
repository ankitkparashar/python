# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 12:46:55 2020

@author: Ankit Parashar
"""
#! viralAdvt.py

def viralAdvt(n):
    cumSum = 0
    for i in range(n):
        if i == 0:
            shares = 5
            
        likes = shares // 2
        cumSum += likes
        shares = likes * 3
    return cumSum

#print(viralAdvt(3))
print(viralAdvt(5))