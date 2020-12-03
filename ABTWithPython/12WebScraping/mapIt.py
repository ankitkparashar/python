# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 13:00:26 2020

@author: Ankit Parashar
"""
#! python3
# mapIt.py

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    #Get address from command line
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
    
#address = pyperclip.paste()
print(address)
webbrowser.open('https://www.google.com/maps/place/'+address)