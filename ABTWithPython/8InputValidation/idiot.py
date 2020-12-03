# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 22:25:17 2020

@author: Ankit Parashar
"""

import pyinputplus as pyip

while True:
    prompt = 'Wnat to know how to keep an idiot busy for hours?\n'
    response = pyip.inputYesNo(prompt)
    if response == 'No':
        break
print('Thank you!. Have a nice day.')