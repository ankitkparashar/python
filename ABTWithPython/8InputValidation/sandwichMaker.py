# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 22:56:15 2020

@author: Ankit Parashar
"""
import pyinputplus as pyip

breadChoices = {'Wheat': 1, 'White': 0.5, 'Sourdough': 2.5}
proteinChoices = {'Chicken': 2, 'Turkey': 2.25, 'Ham': 1.75, 'Tofu': 2}
cheeseChoices = {'Cheddar': 1, 'Swiss': 1.75, 'Mozzarella':1.5}
additionals = {'Mayo': 0.5, 'Mustard': 0.5, 'Lettuce': 0.75, 'Tomato': 0.5}
totalCost = 0
bread = pyip.inputMenu(list(breadChoices.keys()), prompt='Please select your Bread:\n')
totalCost += breadChoices[bread]
protein = pyip.inputMenu(list(proteinChoices.keys()), prompt='Please select your choice of Protien:\n')
totalCost += proteinChoices[protein]
cheese = pyip.inputYesNo('Would you like some cheese?\n')
if cheese == 'yes':
    cheeseChoice = pyip.inputMenu(list(cheeseChoices.keys()), 'Select from these cheese options:\n')
    totalCost += cheeseChoices[cheeseChoice]
additional = pyip.inputYesNo('Would you like some additionals on it?\n')
if additional == 'yes':
    for choice in additionals.keys():
        choiceAnswer = pyip.inputYesNo('Would you like '+choice+'?\n')
        if choiceAnswer == 'yes':
            totalCost += additionals[choice]
        
    
totalNos = pyip.inputNum('How many sandwiches would you like?\n', min=1)
print('Your total bill is ', totalNos * totalCost)