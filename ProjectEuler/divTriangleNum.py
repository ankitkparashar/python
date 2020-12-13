# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 22:11:38 2020

@author: Ankit Parashar
"""
#! divTriangleNum.py

import math

def divTriangleNum(n):
    current_most_divisors = 0
    triangle_number = 1
    index = 2
    while True:
        current_divisors = find_divisors(triangle_number)
        number_of_current_divisors = len(current_divisors)
        if number_of_current_divisors > current_most_divisors:
            current_most_divisors = number_of_current_divisors
        if current_most_divisors > n:
            break
        triangle_number, index = next_triangle_number(triangle_number, index)
        
    return triangle_number
    
    
def next_triangle_number(number, index):
    return (number + index, index + 1)

def find_divisors(number):
    potential_divisor = 1
    half_divisors = []
    sqrt = math.sqrt(number)
    sqrt = math.ceil(sqrt)
    while potential_divisor < sqrt:
        if number % potential_divisor == 0:
            half_divisors.append(potential_divisor)
        potential_divisor += 1
    
    divisors = half_divisors
    for divisor in half_divisors[::-1]:
        divisors.append(number / divisor)
        
    return divisors

print(divTriangleNum(500))