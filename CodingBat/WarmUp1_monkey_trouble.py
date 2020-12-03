# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 17:01:18 2020

@author: Ankit Parashar
"""
#! WarmUp1_monkey_trouble.py

def monkey_trouble(a_smile, b_smile):
  if (a_smile & b_smile) | ((not a_smile) & (not b_smile)):
    return True
  else:
    return False

print(monkey_trouble(True, True))
print(monkey_trouble(False, False))
print(monkey_trouble(True, False))