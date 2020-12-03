# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 15:55:41 2020

@author: Ankit Parashar
"""

def near_hundred(n):
  flag = False
  if ((abs(200 - n) <= 10) & (abs(200 - n) >= 0)) | ((abs(100 - n) <= 10) & (abs(100 - n) >= 0)):
    flag = True
  return flag

print(near_hundred(89))