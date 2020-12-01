# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 20:11:22 2020

@author: Ankit Parashar
"""
#! largestPrimeFactor.py
import math

def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, math.floor((math.sqrt(n) + 1))):
            if n % i == 0:
                return False
    return True

def largestPrimeFactor(n):
    largest = 2
    for i in range(2, math.floor((math.sqrt(n) + 1))):
        if n % i == 0:
            if isPrime(i):
                if i > largest:
                    largest = i
    return largest

#print(largestPrimeFactor(13195))
print(largestPrimeFactor(600851475143))