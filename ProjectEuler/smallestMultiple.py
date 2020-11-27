# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 23:40:31 2020

@author: Ankit Parashar
"""
#! smallestMultiple.py

def isDivisible1ton(num, n):
    for i in range(2, n+1):
        if num % i != 0:
            return False
    return True

number = 20
while True:
    if (isDivisible1ton(number, 20)):
        break
    number += 20
    
print(number)