# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 17:10:05 2020

@author: Ankit Parashar
"""

def printTable(lists):
    colWidths = [0] * len(lists)
    for i in range(len(lists)):
        colLength = 0
        for word in lists[i]:
            if colLength < len(word):
                colLength = len(word)
            
        colWidths[i] = colLength
    
    for i in range(len(lists[0])):
        for j in range(len(lists)):
            print(lists[j][i].rjust(colWidths[j]), end = '\t')
        print()
    

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'Davidoff'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)