# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 14:45:58 2020

@author: Ankit Parashar
"""
#! permutationEquation.py

def permutationEquation(p):
    equation = []
    size = len(p)
    for x in range(1, size + 1):
        value = p.index(x) + 1
        equation.append(p.index(value) + 1)
    return equation

print(permutationEquation([5, 2, 1, 3, 4]))