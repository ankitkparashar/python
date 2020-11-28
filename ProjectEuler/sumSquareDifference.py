# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 21:27:06 2020

@author: Ankit Parashar
"""
#! sumSquareDifference.py

def sumOfSquares(n):
    if n == 0:
        return 0
    else:
        return pow(n, 2) + sumOfSquares(n - 1)
    
def sumOfNumbers(n):
    if n == 0:
        return 0
    else:
        return n + sumOfNumbers(n - 1)

print(pow(sumOfNumbers(100), 2) - sumOfSquares(100))