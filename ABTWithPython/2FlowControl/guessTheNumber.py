# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 23:22:50 2020

@author: Ankit Parashar
"""
import random

secretNumber = random.randint(1, 20)
print("I'm thinking of a number between 1 and 20")
for guessesTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())
    
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break
    
if guess == secretNumber:
    print("Good job! You guessed my number in "+str(guessesTaken))
else:
    print("Nope. The number I was thinking of was "+str(secretNumber))