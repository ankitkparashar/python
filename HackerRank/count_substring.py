# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 14:29:21 2020

@author: Ankit Parashar
"""
#! count_substring.py

def count_substring(string, sub_string):
    count = 0
    sizeString = len(string)
    sizeSubString = len(sub_string)
    for i in range(sizeString - sizeSubString + 1):
        if string[i:sizeSubString + i] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
