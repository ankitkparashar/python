# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 16:48:46 2020

@author: Ankit Parashar
"""
#! countingValleys.py

def countingValleys(steps, path):
    if steps == 2:
        return len(set(path) - 1)
    else:
        level = 0
        valleys = 0
        for step in path:
            if step == 'U':
                level += 1
                if level == 0:
                    valleys += 1
            else:
                level -= 1
    return valleys

print(countingValleys(8, ['U', 'D', 'D', 'D', 'U', 'D', 'U', 'U']))