# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 00:37:10 2020

@author: Ankit Parashar
"""
#! alphabetRangoli.py

def print_rangoli(size):
    lines = size * 2 - 1
    chars = lines * 2 - 1
    startValue = 65
    for i in range(1, lines + 1):
        for j in range(1, chars + 1):
            
            print('-'*((size - 1)*2), chr(startValue + size), '-'*((size - 1)*2))