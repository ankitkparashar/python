# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 14:50:55 2020

@author: Ankit Parashar
"""
#! drawingBook.py

def drawingBook(n, p):
    if n % 2 == 0:
        lastPage = 'left'
    else:
        lastPage = 'right'
    if ((p == 1) | (p == n)):
        return 0
    else:
        if lastPage == 'left':
            half = n / 2
            if p <= half:
                return p // 2
            else:
                diff = n - p
                return (diff + 1) // 2
        else:
            half = n // 2
            if p <= half:
                return p // 2
            else:
                diff = n - p
                return diff // 2
            
print(drawingBook(6, 4))
#print(drawingBook(99, 44))