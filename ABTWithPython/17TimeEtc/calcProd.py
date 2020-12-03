# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 17:10:45 2020

@author: Ankit Parashar
"""
import time

def calcProd():
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long.'%len(str(prod)))
print('Took %s seconds to calculate.'%(endTime-startTime))