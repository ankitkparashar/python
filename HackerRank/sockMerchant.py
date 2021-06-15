# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 14:20:58 2020

@author: Ankit Parashar
"""
#! sockMerchant.py

def sockMerchant(n, ar):
    if n == 1:
        return 0
    else:
        pairs = {}
        numPairs = 0
        for i in ar:
            if str(i) in pairs.keys():
                pairs[str(i)] += 1
            else:
                pairs[str(i)] = 1
                
            if pairs[str(i)] % 2 == 0:
                numPairs += 1
        # for key in list(pairs.keys()):
        #     if pairs[key] % 2 == 0:
        #         numPairs += pairs[key] / 2
        #     else:
        #         if pairs[key] > 2:
        #             numPairs += pairs[key] // 2
        return numPairs
    
print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
#print(sockMerchant(7, [1, 2, 1, 2, 1, 3, 2]))