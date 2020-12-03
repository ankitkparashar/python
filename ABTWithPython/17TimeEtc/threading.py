# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 01:54:09 2020

@author: Ankit Parashar
"""
#! python3
# threading.py

import threading, time

print('Start of the program.')

def takeANap():
    time.sleep(5)
    print('Wake up!')
    
threadObj = threading.Thread(target = takeANap)
threadObj.start()

print('End of the program.')