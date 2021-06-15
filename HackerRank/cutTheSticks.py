# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 17:58:41 2020

@author: Ankit Parashar
"""
#! cutTheSticks.py

def cutTheSticks(arr):
    sticks = []
    zeros = 0
    size = len(arr)
    while size > 0:
        cut = min(arr)
        sticks.append(len(arr))
        size = len(arr)
        for j in range(size):
            arr[j] = arr[j] - cut
            if arr[j] == 0:
                zeros += 1
        if zeros != 0:
            for k in range(zeros):
                arr.remove(0)
            zeros = 0
        size = len(arr)
    return sticks

#print(cutTheSticks([5, 4, 4, 2, 2, 8]))
print(cutTheSticks([1, 2, 3, 4, 3, 3, 2, 1]))