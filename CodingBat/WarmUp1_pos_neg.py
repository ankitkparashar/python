# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 16:42:47 2020

@author: Ankit Parashar
"""
#! WarmUp1_pos_neg

def pos_neg(a, b, negative):
  flag = False
  if negative:
    if (a < 0) & (b < 0):
      flag = True
  else:
    if ((a > 0) & (b < 0)) | ((a < 0) & (b > 0)):
      flag = True
    
  return flag

print(pos_neg(1, -1, False))