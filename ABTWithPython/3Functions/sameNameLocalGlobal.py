# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 19:43:52 2020

@author: Ankit Parashar
"""

def spam():
    global eggs
    eggs = 'spam'
    
def bacon():
    eggs = 'bacon'
    
def ham():
    print(eggs)    

    
eggs = 42
spam()
print(eggs)