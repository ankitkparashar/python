# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 14:56:59 2020

@author: Ankit Parashar
"""
#! selectionSort.py

def findSmallest(arr):
    size = len(arr)
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, size):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
        
    return smallest_index

def selectionSort(arr):
    newArr = []
    size = len(arr)
    for i in range(size):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))