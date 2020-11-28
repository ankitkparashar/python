# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 21:48:17 2020

@author: Ankit Parashar
"""
#! 10001stPrime.py
import math

def isPrime(n):
    for i in range(2, math.floor((math.sqrt(n) + 1))):
        if n % i == 0:
            return False
    return True

i = 2
count = 0
while True:
    if isPrime(i):
        count += 1
        if count == 10001:
            print(i)
            break
    i+= 1