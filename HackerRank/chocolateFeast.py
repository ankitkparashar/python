# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 22:57:37 2021

@author: Ankit Parashar
"""
#! chocolateFeast.py

def chocolateFeast(n, c, m):
    chocolates = n // c
    wraps = chocolates
    while wraps >= m:
        chocolates += wraps // m
        wraps = (wraps // m) + (wraps % m)
    return chocolates

#print(chocolateFeast(15, 3, 2))
#print(chocolateFeast(10, 2, 5))
#print(chocolateFeast(12, 4, 4))
print(chocolateFeast(6, 2, 2))