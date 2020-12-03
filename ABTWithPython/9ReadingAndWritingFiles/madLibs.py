# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 15:39:34 2020

@author: Ankit Parashar
"""
import pyinputplus as pyip

fileObj = open('madLibs.txt', 'r')
fileText = fileObj.read()
fileObj.close()
#print(len(fileText.split('.')))
newText = []
for line in fileText.split('.'):
    if line != ' ':
        for i in range(len(line.split(' '))):
            print(line[i])
            if line[i] in ['NOUN', 'ADJECTIVE', 'VERB']:
                newNavWord = pyip.inputStr('Enter a'+'n '+line[i].lower() if line[i] == 'ADJECTIVE' 
                                           else 'Enter a '+line[i].lower())
                if i == len(line) - 1:
                    word = newNavWord+'.'
                else:
                    word = newNavWord
                newText.append(word)
        
#newTextString = ' '.join(newText)
#print(newTextString)      