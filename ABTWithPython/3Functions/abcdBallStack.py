# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 19:21:21 2020

@author: Ankit Parashar
"""

def a():
    b()
    d()
    print('a() returns')
    
def b():
    print('b() starts')
    c()
    print('b() returns')
    
def c():
    print('c() starts')
    print('c() returns')
    
def d():
    print('d() starts')
    print('d() returns')
    
a()