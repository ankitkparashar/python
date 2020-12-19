# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 19:58:48 2020

@author: Ankit Parashar
"""
#!fibonacci1000Digit.py

def fibonacciNumbers(n):
    fibSeries = [1, 1]
    i = len(fibSeries)
    while i > 0:
        nextTerm = fibSeries[i - 1] + fibSeries[i - 2]
        fibSeries.append(nextTerm)
        i += 1
        if len(str(nextTerm)) == n:
            return i
        
#print(fibonacciNumbers(3))
print(fibonacciNumbers(1000))