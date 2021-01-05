# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 21:18:18 2021

@author: Ankit Parashar
"""
#! latticePaths.py

def latticePaths(n):
    
    pascalTriangle = [[1], [1, 1]]
    for i in range(2, (n * 2) + 1):
        prevArray = pascalTriangle[i - 1]
        pascalTriangle.append(createNext(prevArray))
    
    return pascalTriangle[-1][len(pascalTriangle[-1]) // 2]
        
        
def createNext(line):
    newLine = [1]
    for i in range(len(line) - 1):
        newItem = line[i] + line[i + 1]
        newLine.append(newItem)
    newLine.append(1)
    return newLine

print(latticePaths(20))