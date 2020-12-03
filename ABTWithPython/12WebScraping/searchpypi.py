# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 17:42:10 2020

@author: HP
"""
#! python3
# searchpypi.py
import sys, webbrowser, bs4, requests

print('Searching...')
res = requests.get('https://google.com/search?q=' 'https://pypi.org/search/?q='+ ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElems = soup.select('.package-snippet')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org'+linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)