# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 23:14:27 2020

@author: Ankit Parashar
"""
import sys

while True:
    print("Type to exit.")
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' +response+'.')