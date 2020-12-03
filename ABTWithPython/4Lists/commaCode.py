# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 00:32:45 2020

@author: Ankit Parashar
"""

def commaCode(inputList):
    outputString = ''
    inputLen = len(inputList)
    for element in inputList:
        if inputList.index(element) == inputLen - 2:
            outputString += str(element) +' and '
        elif inputList.index(element) == inputLen - 1:
            outputString += str(element)
        else:
            outputString += str(element) + ', '
    
    return outputString

spam = ['Apple', 'Banana', 'Peaches']
print(commaCode(spam))