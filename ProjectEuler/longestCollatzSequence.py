# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 00:37:48 2020

@author: Ankit Parashar
"""
#! longestCollatzSequence.py

def longestCollatzSequence(n):
    longestLength = 0
    number = 0
    for i in range(1, n):
        length = len(generateSequence(i))
        if length > longestLength:
            longestLength = length
            number = i
    return number

def generateSequence(num):
    origNum = num
    sequence = []
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = (3 * num) + 1
        
        sequence.append(num)
    
    sequence.insert(0, origNum)
    return sequence
    
#print(generateSequence(13))
print(longestCollatzSequence(1000000))
#837799