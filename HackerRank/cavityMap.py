# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 18:51:41 2021

@author: Ankit Parashar
"""
#! cavityMap.py

def cavityMap(grid):
    maxNum = 0
    size = len(grid)
    for row in grid:
        newMax = max(list(map(int, (i for i in row))))
        if newMax > maxNum:
            maxNum = newMax
    if size > 2:
        cavityPoints = []
        for i in range(1, size - 1):
            for j in range(1, size - 1):
                if grid[i][j] == str(maxNum):
                    if (int(grid[i][j]) > int(grid[i][j - 1])) & (int(grid[i][j]) > int(grid[i - 1][j])) & (int(grid[i][j]) > int(grid[i][j + 1])) & (int(grid[i][j]) > int(grid[i + 1][j])):
                        cavityPoints.append([i, j])
                        
        for point in cavityPoints:
            a, b = point
            grid[a] = grid[a][:b] + 'X' + grid[a][b + 1:]
            
    return grid
    
#print(cavityMap(['1112', '1912', '1892', '1234']))
#print(cavityMap(['989', '191', '111']))
print(cavityMap(['179443854', '961621369', '164139922', '968633951', '812882578', '257829163', '812438597', '176656233', '485773814']))