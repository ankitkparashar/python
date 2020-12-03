# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 13:48:22 2020

@author: Ankit Parashar
"""
#! swapCase.py

def swapCase(s):
    sList = s.split()
    newList = []
    for i in sList:
        cList = []
        for c in i:
            if c.isalpha():
                if c.islower():
                    cList.append(c.upper())
                else:
                    cList.append(c.lower())
            else:
                cList.append(c)
        newList.append(''.join(cList))
    return ' '.join(newList)

if __name__ == '__main__':
    s = input()
    result = swapCase(s)
    print(result)