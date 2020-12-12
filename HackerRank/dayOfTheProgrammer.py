# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 22:12:26 2020

@author: Ankit Parashar
"""
#! dayOfTheProgrammer.py

def dayOfTheProgrammer(year):
    isLeap = False
    if ((year >= 1700) & (year <= 1917)):
        if ((year % 4) == 0):
            isLeap = True
    elif year == 1918:
        return '26.09.1918'
    else:
        if ((year % 400) == 0):
            isLeap = True
        elif (((year % 4) == 0) & ((year % 100) != 0)):
            isLeap = True
    
    numOfDays = 0
    for i in range(8):
        if i + 1 == 2:
            if isLeap:
                days = 29
            else:
                days = 28
        elif ((i + 1 == 4) | (i + 1 == 6)):
            days = 30
        else:
            days = 31
        numOfDays += days
        
    return str(256-numOfDays)+'.09.'+str(year)

print(dayOfTheProgrammer(1800))