# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 14:24:04 2020

@author: Ankit Parashar
"""
#! graphImplementation.py

from collections import deque

def person_is_seller(name):
    return name[-1] == 'm'

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def search(name):  
    search_queue = deque()
    search_queue += graph["you"]
    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person):
            print(person+" is a mango seller!")
            return True
        else:
            search_queue += graph[person]
    return False

search("you")