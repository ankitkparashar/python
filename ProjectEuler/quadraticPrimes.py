# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 15:50:49 2020

@author: Ankit Parashar
"""
#!quadraticPrimes.py

def quadraticPrimes():
    
    
def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, math.floor((math.sqrt(n) + 1))):
            if n % i == 0:
                return False
    return True