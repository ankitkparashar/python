# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 23:57:12 2020

@author: Ankit Parashar
"""
import os

workingDirectory = os.path.abspath('D:/Ankit')
for folderName, subfolder, fileNames in os.walk(workingDirectory):
    for fileName in fileNames:
        if os.path.getsize(folderName+'/'+fileName) > 500000000:
            print(print(folderName+'/'+fileName))