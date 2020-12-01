# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 15:34:22 2020

@author: Ankit Parashar
"""
#! summationOfPrimes.py

import math

# def summationOfPrimes(n):
#     if n >= 2:
#         if isPrime(n):
#             return n + summationOfPrimes(n-1)
#         else:
#             return summationOfPrimes(n-1)
#     return 0

def summationOfPrimes(n):
    sumOfPrimes = 0
    while n >= 2:
        if isPrime(n):
            sumOfPrimes += n
        n = n-1
    return sumOfPrimes

        
def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, math.floor((math.sqrt(n) + 1))):
            if n % i == 0:
                return False
    return True

print(summationOfPrimes(2000000))
#print(isPrime(19))