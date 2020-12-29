# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 20:47:03 2020

@author: Ankit Parashar
"""
#!theTimeInWords.py

def timeInWords(h, m):
    oneToNine = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 
                   8: "eight", 9: "nine"}
    tens = {10: "ten", 20: "twenty", 30: "thirty"}
    quarters = {15: "quarter", 45: "quarter"}
    elevenToNineteen = {11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 
                        16: 'sixteen', 17: "seventeen", 18: "eighteen", 19: "nineteen"}
    hour = int(h)
    minute = int(m)
    if minute > 30:
        minute = 60 - minute
        timing = "to"
        if hour == 12:
            hour = 1
        else:
            hour += 1
    else:
        timing = "past"
        
    hours = ""
    minutes = ""
    if hour < 10:
        hours = oneToNine[hour]
    elif hour == 10:
        hours = tens[hour]
    else:
        hours = elevenToNineteen[hour]        
    
    if minute > 0:
        if minute < 10:
            minutes = oneToNine[minute] + (" minute" if oneToNine[minute] == "one" else " minutes")
        elif minute % 10 == 0:
            if minute == 30:
                minutes = "half"
            else:
                minutes = tens[minute] + " " + "minutes"
        elif ((minute == 15) | (minute == 45)):
            minutes = quarters[minute]
        else:
            minuteTens = minute // 10
            minuteOnes = minute % 10
            if minuteTens == 1:
                minutes = elevenToNineteen[minute] + " " + "minutes"
            else:
                minutes = tens[10*minuteTens] + " " + oneToNine[minuteOnes] + " " + "minutes"
    else:
        return hours + " o' clock"
    

    return minutes + " " + timing + " " + hours

print(timeInWords("10", "57"))           