# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 22:51:00 2020

@author: Ankit Parashar
"""
#! aVeryBigSum.py

def aVeryBigSum(ar):
    if len(ar) == 1:
        return ar[0]
    else:
        return ar[0] + aVeryBigSum(ar[1:])
    
print(aVeryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]))