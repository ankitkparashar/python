# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 13:34:28 2020

@author: Ankit Parashar
"""
#! leaderboard.py

def leaderboard(ranked, player):
    positions = []
    ranking = {}
    sortedScores = sorted(set(ranked), reverse=True)
    for i in range(1, len(sortedScores) + 1):
        ranking[i] = sortedScores[i - 1]
        
    rankingReversed = list(reversed(list(ranking.keys())))
    
    for score in player:
        for k in rankingReversed:
            if score < ranking[k]:
                positions.append(k + 1)
            elif score == ranking[k]:
                    positions.append(k)
            else:
                if k == 1:
                    positions.append(k)
                else:
                    continue
            break
    return positions

print(leaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102]))
#print(leaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))
#print(leaderboard([100, 90, 90, 80,], [70, 80, 105]))