# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 13:22:30 2020

@author: Ankit Parashar
"""
#! appendAndDelete.py

def appendAndDelete(s, t, k):
    s = list(s)
    t = list(t)
    sLen = len(s)
    tLen = len(t)
    if sLen == tLen:
        if s == t:
            return "Yes"
        else:
            i = sLen
            sameCount = 0
            while i > 0:
                if s[i - 1] == t[i - 1]:
                    sameCount += 1
                else:
                    if sameCount != 0:
                        for j in range(sameCount):
                            s.pop()
                            k = k - 1
                    s.pop()
                    k = k - 1
                i -= 1
                        
            if len(s) == 0:
                k = k - tLen
            else:
                k = k + len(s) - tLen
        if k < 0:
            return "No"
        else:
            return "Yes"
    elif sLen < tLen:
        i = sLen
        sameCount = 0
        while i > 0:
            if s[i - 1] == t[i - 1]:
                sameCount += 1
            else:
                s.pop()
                k = k - 1
                k = k - sameCount
                sameCount = 0
            i -= 1
        if len(s) == 0:
            k = k - tLen
        else:
            k = k + len(s) - tLen
            
        if k < 0:
            return "No"
        else:
            return "Yes"
    else:
        diff = sLen - tLen
        for j in range(diff):
            s.pop()
            k -= 1
        i = len(s)
        sameCount = 0
        while i > 0:
            if s[i - 1] == t[i - 1]:
                sameCount += 1
            else:
                s.pop()
                k = k - 1
                k = k - sameCount
                sameCount = 0
            i -= 1
                        
        if len(s) == 0:
            k = k - tLen
        else:
            k = k + len(s) - tLen
        if k < 0:
            return "No"
        else:
            return "Yes"
            
#print(appendAndDelete('qwerasdf', 'qwerbsdf', 6))
print(appendAndDelete('y', 'yu', 2))