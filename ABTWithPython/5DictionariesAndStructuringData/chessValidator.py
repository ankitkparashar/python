# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 12:28:42 2020

@author: Ankit Parashar
"""

def isValidChessBoard(chessBoard):
    isValid = True
    if (len(chessBoard) <= 32):
        validBoard = {'wking': 1, 'wqueen': 1, 'wrook': 2, 'wknight': 2, 'wbishop': 2, 'wpawn': 8, 
                      'bking': 1, 'bqueen': 1, 'brook': 2, 'bknight': 2, 'bbishop': 2, 'bpawn': 8}
        count = {}
        for k, v in chessBoard.items():
            count.setdefault(v, 0)
            count[v] = count[v] + 1
            
        for k in count.keys():
            if count[k] > validBoard[k]:
                isValid = False
                break
    
    return 'Valid Chess board' if isValid else 'Invalid Chess board'

print(isValidChessBoard({'1h': 'bking', '3h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}))