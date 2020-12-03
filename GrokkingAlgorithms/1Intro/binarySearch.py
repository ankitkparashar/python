# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 15:09:49 2020

@author: Ankit  Parashar
"""
#! binarySearch.py

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

the_list = [1, 3, 5, 7, 9, 10]
print(binary_search(the_list, 5))