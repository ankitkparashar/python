# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 16:10:42 2020

@author: Ankit Parashar
"""
#! python3
# readCensusExcel.py
import openpyxl, pprint

print('Opening Workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countydata = {}
print('Reading rows.')
for row in range(2, sheet.max_row+1):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value
    countydata.setdefault(state, {})
    countydata[state].setdefault(county, {'tracts':0, 'pop':0})
    countydata[state][county]['tracts'] += 1
    countydata[state][county]['pop'] += int(pop)
    
print('Writing results.')
resultFile = open('census2010.txt', 'w')
resultFile.write(pprint.pformat(countydata))
resultFile.close()
print('Done')