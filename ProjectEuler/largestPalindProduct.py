# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 19:26:17 2020

@author: Ankit Parashar
"""
#! largestPalindProduct.py

def largestPalindProduct():
    largest = 0
    # i = 999
    # j = 999
    # while i >= 100:
    #     while j >= 100:
    #         product = i * j
    #         if ((isPalindromeNumber(product)) & (product > largest)):
    #             largest = product
    #             if largest != 0:
    #                 break
    #         j = j - 1
    #     i = i - 1
            
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if ((isPalindromeNumber(product)) & (product > largest)):
                largest = product
    return largest
                
def isPalindromeNumber(n):
    strNumber = str(n)
    numFirstPart = ""
    size = len(strNumber)
    if size > 2:
        if size % 2 == 0:
            mid = int((size / 2) - 1)
        else:
            if size == 3:
                if strNumber[0] == strNumber[-1]:
                    return True
            mid = int((size // 2) - 1)
        k = mid
        while k >= 0:
            numFirstPart = numFirstPart + strNumber[k]
            k = k - 1
        if size % 2 == 0:
            if numFirstPart == strNumber[mid+1:]:
                return True
        else:
            if numFirstPart == strNumber[mid+2:]:
                return True
    else:
        return True
    return False

print(largestPalindProduct())