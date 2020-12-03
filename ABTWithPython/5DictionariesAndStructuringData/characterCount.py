# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 01:08:35 2020

@author: Ankit Parashar
"""
import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
    
pprint.pprint(count)