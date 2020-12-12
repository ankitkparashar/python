# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 22:48:46 2020

@author: Ankit Parashar
"""
#! billDivision.py

def bonAppetit(bill, k, b):
    total = sum(bill)
    if (b == (total / 2)):
        print(int(b - ((total - bill[k]) / 2)))
    else:
        print('Bon Appetit')
    
#print(bonAppetit([3, 10, 2, 9], 1, 7))
print(bonAppetit([3, 10, 2, 9], 1, 12))