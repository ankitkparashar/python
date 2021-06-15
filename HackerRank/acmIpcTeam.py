# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 16:50:01 2020

@author: Ankit Parashar
"""
#! acmIpcTeam.py

from itertools import permutations
import numpy as np

def acmIpcteam(topic):
    n = len(topic)
    skills = {}
    topic = [list(x) for x in topic]
    for i in permutations(range(1, n + 1), 2, r=None):
        commonSkills = np.bitwise_or([int(x) for x in topic[i[0] - 1]], 
                                     [int(x) for x in topic[i[1] - 1]])
        skills[i] = sum(commonSkills)
    maxSkills = max(skills.values())
    teams = len([a for a in skills.keys() if skills[a] == maxSkills])
    print(skills)
    return (maxSkills, teams)
    
#print(acmIpcteam(['10101', '11110', '00010']))
print(acmIpcteam(['10101', '11100', '11010', '00101']))