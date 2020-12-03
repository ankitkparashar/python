# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 00:11:19 2020

@author: Ankit Parashar
"""
#! stringFormatting.py

def print_formatted(number):
    maxPadding = len(bin(number)[2:])
    for i in range(1, number + 1):
        print(str(i).rjust(maxPadding, ' '), oct(i)[2:].rjust(maxPadding, ' '), 
              hex(i)[2:].upper().rjust(maxPadding, ' '), bin(i)[2:].rjust(maxPadding, ' '))
        
print_formatted(2)