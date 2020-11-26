# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 21:30:24 2020

@author: Ankit Parashar
"""
#! evenFibonacci.py

def evenFibonacci(n):
    fibonacci = []
    fibonacci.insert(0, 1)
    fibonacci.insert(1, 2)
    i = 2
    while i >= 2:
        print(i)
        if((fibonacci[i-1] + fibonacci[i-2]) < n):
            fibonacci.insert(i, fibonacci[i-1] + fibonacci[i-2])
            i = i+1
        else:
            break
    return sum([evenValue for evenValue in fibonacci if evenValue % 2 == 0])

print(evenFibonacci(4000000))