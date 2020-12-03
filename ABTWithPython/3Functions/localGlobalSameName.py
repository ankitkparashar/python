# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 19:33:33 2020

@author: Ankit Parashar
"""

def spam():
    eggs = 'spam local'
    print(eggs)
    
def bacon():
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs)
    
eggs = 'global'
bacon()
print(eggs)