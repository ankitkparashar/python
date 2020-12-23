# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 20:47:47 2020

@author: Ankit Parashar
"""
#! encryption.py

import math

def encryption(s):
    size = len(s)
    charArray = []
    for i in range(size):
        if s[i].isalpha():
            charArray.append(s[i])
    sizeCArray = len(charArray)
    r = math.floor(math.sqrt(sizeCArray))
    c = math.ceil(math.sqrt(sizeCArray))
    if (r * c) < sizeCArray:
        r = c
    
    grid = []
    ind = 0
    for i in range(r):
        row = []
        for j in range(c):
            if ind < sizeCArray:
                row.append(charArray[ind])
                ind += 1
        grid.append(row)
        
    gridRows = len(grid)
    
    j = 0
    encMessage = []
    while True:
        encString = []
        for i in range(gridRows):
            if j < len(grid[i]):
                encString.append(grid[i][j])
        j += 1
        encMessage.append(encString)
        if j > c:
            break
        
    encryptedString = ""
    for message in encMessage:
        encryptedString = encryptedString + ''.join(message) + ' '
        
    return encryptedString.strip()
        
#print(encryption("if man was meant to stay on the ground god would have given us roots"))
#print(encryption("haveaniceday"))
#print(encryption("feedthedog"))
print(encryption("chillout"))