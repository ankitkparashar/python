# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 16:10:27 2020

@author: Ankit Parashar
"""
#! namesScores.py

def namesScores():
    names = []
    with open('p022_names.txt') as file:
        names.append(file.read())
        
    names = names[0].split(',')
    names = sorted(names)
    size = len(names)
    scores = []
    for i in range(size):
        nameScore = 0
        for j in names[i]:
            if j.isalpha():
                nameScore = nameScore + (ord(j) + 26 - 90)
        scores.append((i + 1) * nameScore)
    return sum(scores)

print(namesScores())