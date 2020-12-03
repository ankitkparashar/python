# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 15:20:22 2020

@author: Ankit Parashar
"""
#! python3
# mcb.pyw

import shelve, pyperclip, sys
mcbShelf = shelve.open('mcb')
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    
mcbShelf.close()