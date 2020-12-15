# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 00:25:49 2020

@author: Ankit Parashar
"""
#!factorials.py

def factorials(n):
    if n <= 1:
        return 1
    else:
        return n * factorials(n - 1)

print(sum([int(i) for i in str(factorials(100))]))