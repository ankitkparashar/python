# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 00:14:30 2020

@author: Ankit Parashar
"""
import os

prefix = input('Provide the prefix for the file\n')
suffixes = []
for file in os.listdir('./fillingGaps'):
    fileName = file.split('.')[0]
    suffixes.append(int(fileName[len(prefix):]))
suffixes = sorted(suffixes)
suffixToBeChanged = 0
if suffixes[0] == 1:
    for i in range(len(suffixes) - 1):
        if suffixes[i + 1] - suffixes[i] > 1:
            suffixToBeChanged = suffixes[i + 1]
            break
else:
    suffixes = [i+1 for i in range(len(suffixes))]

if suffixToBeChanged != 0:
    print(suffixToBeChanged)