# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 19:38:55 2020

@author: Ankit Parashar
"""

def spam():
    global eggs
    eggs = 'spam'
    
eggs = 'global'
spam()
print(eggs)