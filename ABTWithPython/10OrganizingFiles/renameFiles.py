# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 21:35:13 2020

@author: Ankit Parashar
"""
#! python3
# renameDates.py

import shutil, os, re

datePattern = re.compile(r"""^(.*?)
                         ((0|1)?\d)-
                         ((0|1|2|3)?\d)-
                         ((19|20)\d\d)
                         (.*?)$
                         """, re.VERBOSE)
                         
for amerFileName in os.listdir('.'):
    mo = datePattern.search(amerFileName)
    
    if mo == None:
        continue
    
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
    
    euroFileName = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    
    absWorkingDir = os.path.abspath('.')
    amerFileName = os.path.join(absWorkingDir, amerFileName)
    euroFileName = os.path.join(absWorkingDir, euroFileName)
    
    print(f'Renaming "{amerFileName}" to "{euroFileName}"...')
    shutil.move(amerFileName, euroFileName)