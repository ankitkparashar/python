# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 00:21:47 2020

@author: Ankit Parashar
"""
#! findDigits.py

def findDigits(n):
    d = 0
    for i in str(n):
        if int(i) != 0:
            if n % int(i) == 0:
                d += 1
    return d

print(findDigits(124))