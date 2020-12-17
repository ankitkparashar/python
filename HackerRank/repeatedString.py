# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 17:22:37 2020

@author: Ankit Parashar
"""
#! repeatedString.py

def repeatedString(s, n):
    if s == 'a':
        return n
    else:
        aCount = s.count('a')
        size = len(s)
        if n > size:
            itr = n // size
            rem = n % size
            return (itr * aCount) + s[:rem].count('a')
        elif n == size:
            return aCount
        else:
            return s[:n].count('a')
            
    
print(repeatedString('abcac', 10))
#print(repeatedString('aba', 10))
#print(repeatedString('ebcdddafdfeffaddbceddebafbbebebbbcefcbcdfbaabecfaaeeaaffdfccffbdeeaabcfeecfcecbfebacefebdfaeedadebdf', 561984209086))