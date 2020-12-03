# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 15:11:38 2020

@author: Ankit Parashar
"""
#! sumRecursion.py

def sumz(arr):
    if arr == []:
        return 0
    return arr[0] + sumz(arr[1:])


print(sumz([2, 4]))