# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 17:26:54 2020

@author: Ankit Parashar
"""

def spam():
    bacon()
    
def bacon():
    raise Exception('This is an error message.')
    
spam()