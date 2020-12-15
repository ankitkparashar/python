# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 16:56:04 2020

@author: Ankit Parashar
"""
#!sherlockAndSquares.py
import math

def squares(a, b):
    # squareNos = 0
    # for i in range(a, b + 1):
    #     root = math.sqrt(i)
    #     if root - math.floor(root) == 0:
    #         squareNos += 1
    # return squareNos
    a1 = math.floor(math.sqrt(a))
    b1 = math.ceil(math.sqrt(b))
    return b1 - a1 + 1

print(squares(24, 49))