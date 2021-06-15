# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 00:10:59 2020

@author: Ankit Parashar
"""
#!pickingNumbers.py

def pickingNumbers(a):
    size = len(a)
    if size == 2:
        if abs(a[0] - a[1]) <= 1:
            return 2
        else:
            return 0
    else:
        subarr = []
        for i in a:
            for j in range(1, size):
                if len(subarr) == 0:
                    if abs(i - a[j]) <= 1:
                        subarr.append(i)
                        subarr.append(a[j])
                else:

def createSubarr(arr, e):
    subArr = []
    for 