# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 20:14:56 2020

@author: Ankit Parashar
"""

def collatz(number):
    output = 0
    if number % 2 == 0:
        output = number // 2
    else:
        output = 3 * number + 1
    return output

callCollatz = True

while callCollatz:
    print('Enter a number\n')
    try:
        numEntered = int(input())
        calcNum = collatz(numEntered)
        print(calcNum)
        if calcNum == 1:
            callCollatz = False
    except ValueError:
        print('Please enter an integer value')