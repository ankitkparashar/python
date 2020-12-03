# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 23:50:12 2020

@author: Ankit Parashar
"""

import random

messages = ['It is certain', 
            'It is decidedly so', 
            'Yes Definitely', 
            'Reply hazy try again', 
            'Ask again later', 
            'Concentrate and ask again', 
            'My reply is no', 
            'Outlook is not so good', 
            'Very doubtful']
print(messages[random.randint(1, len(messages) - 1)])