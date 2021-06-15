# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 00:12:31 2021

@author: Ankit Parashar
"""
#! lisaWorkbook.py

def lisaWorkbook(n, k, arr):
    quesOnPages = {}
    pages = 1
    specials = 0
    for i in range(n):
        for j in range(arr[i]):
            if pages in quesOnPages.keys():
                quesOnPages[pages].append(j + 1)
            else:
                quesOnPages[pages] = [j + 1]
                
            if len(quesOnPages[pages]) > k - 1:
                pages += 1
        if pages in quesOnPages.keys():
            pages += 1
    
    for key in quesOnPages:
        if key in quesOnPages[key]:
            specials += 1
                
    return specials

print(lisaWorkbook(5, 3, [4, 2, 6, 1, 10]))