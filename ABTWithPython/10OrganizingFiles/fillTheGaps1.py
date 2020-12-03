# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 15:20:23 2020

@author: Ankit Parashar
"""
import os

files = {}
suffixToBeChanged = 0
for file in os.listdir('./fillingGaps'):
    files[file] = int(file.split('.')[0][4:])

#print(files)
suffixes = sorted(list(files.values()))
diff = 0   
if suffixes[0] == 1:
    for i in range(len(suffixes) - 1):
        diff = suffixes[i + 1] - suffixes[i]
        toBeChanged = suffixes[i + 1]
        if diff > 1:
            suffixes[i + 1] = suffixes[i] + 1
            files['spam00'+str(toBeChanged)+'.txt'] = suffixes[i+1]
else:
    suffixes = [i+1 for i in range(len(suffixes))]
    
#print(files)