# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 22:29:23 2020

@author: Ankit Parashar
"""

import pyinputplus as pyip
import random, time

numberOfQuesions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuesions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    
    prompt = '#%s: %s x %s = '%(questionNumber, num1, num2)
    try:
        pyip.inputStr(prompt, allowRegexes=['^%s$'%(num1 * num2)], 
                      blockRegexes=[('.*', 'Incorrect!')], 
                      timeout=8, limit = 3)
    except pyip.TimeoutException:
            print('Out of time!')
    except pyip.RetryLimitException:
            print('Out of Tries!')
            
    else:
        print('Correct!')
        correctAnswers += 1
        
    time.sleep(1)
print('Score: %s / %s' %(correctAnswers, numberOfQuesions))