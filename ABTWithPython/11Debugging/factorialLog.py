# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 17:51:03 2020

@author: Ankit Parashar
"""
import logging
logging.basicConfig(level = logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of the program')

def factorial(n):
    logging.debug('Start of factorial (%s)' %(n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of Factorial (%s)' %(n))
    return total

print(factorial(5))
logging.debug('End of program.')