# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 22:37:58 2020

@author: Ankit Parashar
"""
import shutil, os

workingDirectory = os.path.abspath('D:/Ankit')
targetDirectory = os.path.abspath('./copiedFiles')

for folderName, subfolder, fileNames in os.walk(workingDirectory):
    if folderName != targetDirectory:
        for fileName in fileNames:
            if fileName.endswith('.pdf') or fileName.endswith('.jpeg'):
                #print(fileName)
                shutil.copy(folderName+'/'+fileName, targetDirectory+'/'+fileName)