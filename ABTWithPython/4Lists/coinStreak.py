# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 21:49:38 2020

@author: Ankit Parashar
"""

import random

numberOfStreaks = 0
for experimentNumber in range(10000):
    experimentList = []
    for i in range(100):
        outcome = random.randint(0, 1)
        if outcome == 0:
            experimentList.append('H')
        else:
            experimentList.append('T')
            
    for j in range(len(experimentList)):
        if j+6 <= 99:
            tempList = experimentList[j:j+6]
            if tempList[0] == 'H':
                if 'T' in tempList:
                    continue
                else:
                    numberOfStreaks += 1
            else:
                if 'H' in tempList:
                    continue
                else:
                    numberOfStreaks += 1
        else:
            break
    

print('Chance of streak: %s%%' % (numberOfStreaks / 100))