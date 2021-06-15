# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 22:49:49 2020

@author: Ankit Parashar
"""
#! magicSquare.py

def magicSquare(matr):
    sumvalues = sumOfMatrix(matr)
    sumvaluesSet = set(sumvalues)
    cost = 0
    for value in sumvaluesSet:
        while True:
            
    
def sumOfMatrix(matr):
    sumr1 = sum(matr[0])
    sumr2 = sum(matr[1])
    sumr3 = sum(matr[2])
    sumc1 = sum([matr[i][0] for i in range(3)])
    sumc2 = sum([matr[i][1] for i in range(3)])
    sumc3 = sum([matr[i][2] for i in range(3)])
    sumprd = sum([matr[i][j] for i in range(3) for j in range(3) if i == j])
    sumsed = sum([matr[i][j] for i in range(3) for j in range(3) if i+j == 2])
    sumMatr = [sumr1, sumr2, sumr3, sumc1, sumc2, sumc3, sumprd, sumsed]
    return sumMatr
    
#print(sumOfMatrix([[4, 8, 2], [4, 5, 7], [6, 1, 6]]))
#print(sumOfMatrix([[5, 3, 4], [1, 5, 8], [6, 4, 2]]))