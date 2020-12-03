# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 18:44:00 2020

@author: Ankit Parashar
"""
import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    #guess = 0 if guess == 'tails' else 1
toss = random.randint(0, 1) # 0 is tails, 1 is heads
toss = 'tails' if toss == 0 else 'heads'
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    #guesss = input()
    guess = input()
    #guess = 0 if guess == 'tails' else 1
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')