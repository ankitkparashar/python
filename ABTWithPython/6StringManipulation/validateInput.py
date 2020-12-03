# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 18:18:17 2020

@author: Ankit Parashar
"""

while True:
    print("Enter your age:")
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age')
    
while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')