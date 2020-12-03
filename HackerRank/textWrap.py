# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 00:38:38 2020

@author: HP
"""
#! textWrap.py

def textWrap(string, max_width):
    newString = ""
    size = len(string)
    if size % max_width == 0:
        lines = size / max_width
    else:
        lines = (size // max_width) + 1
    for i in range(lines):
        if i == lines - 1:
            newString = newString + string[max_width * i:]
        else:
            newString = newString + string[max_width * i:max_width * i + max_width] + '\n'
    return newString

print(textWrap("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 4))