# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 21:11:06 2020

@author: Ankit Parashar
"""
#! python3
# readDocx.py

import docx

def getText(fileName):
    doc = docx.Document(fileName)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)