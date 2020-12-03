# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 16:47:09 2020

@author: Ankit Parashar
"""
#! quickSort.py

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    
print(quicksort([2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7]))