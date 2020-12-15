# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 23:00:15 2020

@author: HP
"""
#! amicableNumbers.py

def amicableNumbers(n):
    amicableNos = []
    a = n
    while a > 0:
        if a not in amicableNos:
            b = getDivisorSum(a)
            a1 = getDivisorSum(b)
            if ((a1 == a) & (a1 != b)):
                amicableNos.append(a)
                amicableNos.append(b)
        a -= 1
    print(amicableNos)
    return sum(amicableNos)

def getDivisorSum(n):
    i = n //2
    divisors = []
    while i > 0:
        if n % i == 0:
            divisors.append(i)
        i -= 1
    return sum(divisors)

print(amicableNumbers(10000))
#31626