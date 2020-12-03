# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 17:22:49 2020

@author: Ankit Parashar
"""
#! compareTriplets.py

def compareTriplets(a, b):
    scores = [0, 0]
    for i in range(len(a)):
        if a[i] > b[i]