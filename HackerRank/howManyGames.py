# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 14:59:48 2020

@author: Ankit Parashar
"""
#! howManyGames.py

def howManyGames(p, d, m, s):
        games = 0
        costs = []
        cost = p
        while True:
            if games == 0:
                costs.append(cost)
            else:
                cost = costs[games - 1] - d
                if cost <= m:
                    cost = m
                costs.append(cost)
            s = s - cost
            if s < 0:
                return games
            games += 1
        
# print(howManyGames(20, 3, 6, 80))
# print(howManyGames(20, 3, 6, 85))
# print(howManyGames(20, 3, 6, 70))
# print(howManyGames(100, 1, 1, 99))
# print(howManyGames(100, 12, 55, 95))
# print(howManyGames(100, 11, 10, 1))