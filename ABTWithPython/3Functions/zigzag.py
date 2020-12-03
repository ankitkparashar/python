# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 20:00:08 2020

@author: Ankit Parashar
"""

import time, sys

indent = 0
indentIncreasing = True

try:
    while True:
        print(' '*indent, end = '')
        print('********')
        time.sleep(0.1)
        
        if indentIncreasing:
            indent = indent + 1
            if indent == 20:
                indentIncreasing = False
            
        else:
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True
            
        
    
except KeyboardInterrupt:
    sys.exit()