# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 21:39:07 2021

@author: Ankit Parashar
"""
#! numberLetterCounts.py

def numberLetterCounts(limit):
    numbers = {1: "one", 2: "two", 3: "three", 4: "four", 5:"five", 6:"six", 7: "seven", 8: "eight", 
               9: "nine", 10: "ten", 11: 'eleven', 12: "twelve", 13: "thirteen", 14: "fourteen", 
               15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 
               20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 
               80: "eighty", 90: "ninety", 100: "onehundred", 1000: "onethousand"}
    
    letterCount = 0
    numInWords = ""
    for i in range(1, limit + 1):
        if i % 1000 == 0:
            numInWords = numbers[i]
        elif i % 100 == 0:
            if i == 100:
                numInWords = numbers[i]
            else:
                q = i // 100
                numInWords = numbers[q] + numbers[100][3:]
        else:
            if len(str(i)) == 3:
                h = i // 100
                if i % 100 in numbers:
                    numInWords = numbers[h] + numbers[100][3:] + "and" + numbers[i % 100]
                else:
                    t = (i - (100 * h)) // 10
                    ones = i - ((100 * h) + (10 * t))
                    numInWords = numbers[h] + numbers[100][3:] + "and" + numbers[10 * t] + numbers[ones]
            elif len(str(i)) == 2:
                if i in numbers:
                    numInWords = numbers[i]
                else:
                    t = i // 10
                    ones = i - (10 * t)
                    if ones == 0:
                        numInWords = numbers[10 * t]
                    else:
                        numInWords = numbers[10 * t] + numbers[ones]
            else:
                numInWords = numbers[i]

        letterCount += len(numInWords)
    return letterCount

print(numberLetterCounts(1000))