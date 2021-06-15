# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 16:01:55 2020

@author: Ankit Parashar
"""
#!biggerIsGreater.py

from itertools import permutations

def biggerIsGreater(w):  
    sortedWord = ''.join(sorted(list(w)))
    permutationList = [''.join(list(i)) for i in permutations(sortedWord)]
    if permutationList.index(w) == len(permutationList) - 1:
        return "no answer"
    else:
        if permutationList[permutationList.index(w) + 1] != w:
            return permutationList[permutationList.index(w) + 1]
        else:
            return "no answer"
    
# print(biggerIsGreater('lmno'))
# print(biggerIsGreater('dcba'))
# print(biggerIsGreater('dcbb'))
# print(biggerIsGreater('abdc'))
# print(biggerIsGreater('abcd'))
print(biggerIsGreater('imllmmcslslkyoegymoa'))