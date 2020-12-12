# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 17:17:55 2020

@author: Ankit Parashar
"""
#! electronicsShop.py

def getMoneySpent(keyboards, drives, b):
    options = []
    for i in keyboards:
        for j in drives:
            if i + j <= b:
                options.append(i + j)
    return max(options) if len(options) != 0 else -1

#print(getMoneySpent([4], [5], 5))
print(getMoneySpent([3, 1], [5, 2, 8], 10))