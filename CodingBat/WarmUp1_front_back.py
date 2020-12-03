# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 16:26:11 2020

@author: Ankit Parashar
"""
#! WarmUp_1_front_back.py

def front_back(string):
    newStr = []
    size = len(string)
    if size > 1:
        first = string[0]
        last = string[-1]
        mid = string[1:-1]
        newStr.append(last)
        newStr.append(mid)
        newStr.append(first)
        string = ''.join(newStr)
    return string

print(front_back('code'))