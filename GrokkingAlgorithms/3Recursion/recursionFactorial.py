# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 17:57:15 2020

@author: Ankit Parashar
"""
#! recursionFactorial.py

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)
    
print(fact(3))