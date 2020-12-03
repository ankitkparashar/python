# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 22:02:43 2020

@author: Ankit Parashar
"""
#! python3
#backupToZip.py

import zipfile, os
from pathlib import Path
p = Path.cwd()

def backupToZip(folder):
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break
        number  = number + 1
        
    print(f'Creating {zipFileName}...')
    backupZip = zipfile.ZipFile(zipFileName, 'w')
    
    for foldername, subfolder, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        backupZip.write(foldername)
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done')
    
backupToZip('D:/Ankit/Learn/Python/ABTWithPython')