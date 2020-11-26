# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 21:13:21 2020

@author: Ankit Parashar
"""
#! multiplesOf3And5.py

def multiplesOf3And5(n):
    sum = 0
    for i in range(n):
        if (((i % 3) == 0) | ((i % 5) == 0)):
            sum += i
    return sum

print(multiplesOf3And5(1000))