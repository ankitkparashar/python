# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 15:23:43 2020

@author: Ankit Parashar
"""
#! queensAttack.py

def queensAttack(n, k, r_q, c_q, obstacles):
    attacks = 0
    if n == 1:
        return 0
    else:
        if obstacles != []:
            obstacles = [(obs[0], obs[1]) for obs in obstacles]
        r, c = r_q, c_q
        #to the right
        while c_q < n:
            c_q += 1
            if (r_q, c_q) in obstacles:
                break
            else:
                attacks += 1
        #to the left
        r_q, c_q = r, c
        while c_q > 1:
            c_q -= 1
            if (r_q, c_q) in obstacles:
                break
            else:
                attacks += 1
        #downwards            
        r_q, c_q = r, c
        while r_q < n:
            r_q += 1
            if (r_q, c_q) in obstacles:
               break
            else:
                attacks += 1
        #upwards            
        r_q, c_q = r, c
        while r_q > 1:
            r_q -= 1
            if (r_q, c_q) in obstacles:
                break
            else:
                attacks += 1
        #toprightdiagonal
        r_q, c_q = r, c
        while ((r_q > 1) & (c_q < n)):
            r_q -= 1
            c_q += 1
            if (r_q, c_q) in obstacles:
                break
            else:
                attacks += 1
        #belowrightdiagonal
        r_q, c_q = r, c
        while ((r_q < n) & (c_q < n)):
            r_q += 1
            c_q += 1
            if (r_q, c_q) in obstacles:
                break
            else:
                attacks += 1
        #topleftdiagonal
        r_q, c_q = r, c
        while ((r_q > 1) & (c_q > 1)):
            r_q -= 1
            c_q -= 1
            if (r_q, c_q) in obstacles:
                break
            else:
                attacks += 1
        #belowleftdiagonal
        r_q, c_q = r, c
        while ((r_q < n) & (c_q > 1)):
            r_q += 1
            c_q -= 1
            if (r_q, c_q) in obstacles:
                break
            else:
                attacks += 1
    return attacks

#print(queensAttack(1, 0, 1, 1, obstacles=[]))
print(queensAttack(5, 3, 4, 3, obstacles=[[5, 5], [4, 2], [2, 3]]))
#print(queensAttack(8, 1, 4, 4, obstacles=[(3, 5)]))