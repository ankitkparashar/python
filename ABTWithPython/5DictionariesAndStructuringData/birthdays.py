# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 00:56:49 2020

@author: Ankit Parashar
"""

birthdays = {'Ankit': 'Aug 25', 'Prateek': 'Oct 1', 'Tushar': 'Jan 25', 'Namrata': 'Dec 19'}

while True:
    print('Enter a name (blank to quit): ')
    name = input()
    if name == '':
        break
    
    if name in birthdays:
        print(birthdays[name]+' is the birthday of '+name)
    else:
        print('I do not have the birthday information for '+name)
        print('When is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated!')