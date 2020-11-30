# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 00:11:18 2020

@author: Ankit Parashar
"""
#! specialPythagoreanTriplet.py

def specialPythagoreanTriplet(n):
    for a in range(1, n+1):
        for b in range(a+1, n+1):
            c = n - (a + b)
            if pow(a, 2) + pow(b, 2) == pow(c, 2):
                return a*b*c
            
print(specialPythagoreanTriplet(1000))