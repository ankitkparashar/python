# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 20:27:54 2020

@author: Ankit Parashar
"""
#! kaprekarNumbers.py

import math

def karpekarNumbers(p, q):
    kaprekars = []
    for i in range(p, q + 1):
        sqr = int(math.pow(i, 2))
        strSqr = str(sqr)
        d = len(str(i))
        lenSqr = len(strSqr)
        l = 0
        r = 0
        if (lenSqr == 2 * d):
            l = strSqr[:d]
            r = strSqr[d:]
        elif (lenSqr == ((2 * d) - 1)):
             ind = lenSqr // 2
             if ind == 0:
                 l = 0
             else:
                l = strSqr[:ind]
             r = strSqr[ind:]
        
        if (int(l) + int(r) == i):
            kaprekars.append(i)
    
    if len(kaprekars) == 0:
        print("INVALID RANGE")
    else:
        for kaprekar in kaprekars:
            print(kaprekar, end=' ')
    
karpekarNumbers(1, 100)