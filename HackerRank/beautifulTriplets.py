# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 22:44:07 2020

@author: Ankit Parashar
"""
#!beautifulTriplets.py

def beautifulTriplets(d, arr):
    triplets = []
    triplet = []
    size = len(arr)
    i = 0
    while i < size:
        a = i
        for j in range(i + 1, size):
            if arr[j] - arr[i] == d:
                if arr[j] not in triplet:
                    if len(triplet) == 2:
                        triplet.append(arr[j])
                    else:
                        triplet.append(arr[i])
                        triplet.append(arr[j])
                    i = j
                    if len(triplet) == 3:
                        break
            elif arr[j] - arr[i] > d:
                break

        if len(triplet) == 3:        
            triplets.append(triplet)
            triplet = []
        if i == size - 1:
            break
        i = a
        i += 1
     
    return triplets

print(beautifulTriplets(18, sorted([19693, 19711, 19729, 19698, 19716, 19722, 19707, 19725, 19727])))