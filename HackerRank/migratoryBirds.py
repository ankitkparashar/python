# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 21:54:13 2020

@author: Ankit Parashar
"""
#! migratoryBirds.py

def migratoryBirds(arr):
    sightings = {}
    for i in arr:
        if str(i) not in sightings.keys():
            sightings[str(i)] = 1
        else:
            sightings[str(i)] += 1
    return min([int(i) for i in list(sightings.keys()) if sightings[i] == max(sightings.values())])


#print(migratoryBirds([1, 4, 4, 4, 5, 3]))
print(migratoryBirds([1, 1, 2, 2, 3]))