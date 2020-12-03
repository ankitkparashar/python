# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 22:44:09 2020

@author: Ankit Parashar
"""
while True:
    print("Who are you?")
    name = input()
    if name != "Joe":
        continue
    print("Hello, Joe. What is the password? (It is a fish.)")
    password = input()
    if password == "swordfish":
        break
    
print("Access granted.")