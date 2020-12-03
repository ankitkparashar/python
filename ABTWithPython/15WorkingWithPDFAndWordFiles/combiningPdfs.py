# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 14:30:04 2020

@author: Ankit Parashar
"""
#! python3
# combinePdfs.py: Combines all PDFs in a directory into a single PDF
import PyPDF2, os

pdfFiles = []
for fileName in os.listdir('.'):
    if fileName.endswith('pdf'):
        pdfFiles.append(fileName)
    
pdfFiles.sort(key = str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

for pdfFile in pdfFiles:
    pdfFileObj = open(pdfFile, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    
outputPdfFile = open('outputPdfFile.pdf', 'wb')
pdfWriter.write(outputPdfFile)
outputPdfFile.close()