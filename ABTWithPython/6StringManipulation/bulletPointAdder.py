# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 21:34:45 2020

@author: Ankit Parashar
"""
#! python3
# bulletPointAdder.py - Adds bulet points to the start of each line

import pyperclip

text = pyperclip.paste()
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
    
text = '\n'.join(lines)
pyperclip.copy(text)