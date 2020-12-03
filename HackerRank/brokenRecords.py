# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 17:10:00 2020

@author: Ankit Parashar
"""
#! breakingRecords.py

def breakingRecords(scores):
    records = [0, 0]
    lowest = 0
    highest = 0
    size = len(scores)
    for i in range(size):
        if i == 0:
            highest = scores[i]
            lowest = scores[i]
        else:
            if scores[i] > highest:
                highest = scores[i]
                records[0] += 1
            if scores[i] < lowest:
                lowest = scores[i]
                records[1] += 1
    return records

print(breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]))
#print(breakingRecords([0, 9, 3, 10, 2, 20]))