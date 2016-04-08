# -*- coding: utf-8 -*- 
import re

import csv

datafile = r'inNingboData.csv'
csvfile = file(datafile,'r')
reader = csv.reader(csvfile)

pattern = r'浙江省宁波市'

districtDict = {
                'DISTRICT_BL' : r'北仑',
                'DISTRICT_YZ' : r'鄞州',
                'DISTRICT_HS' : r'海曙',
                'DISTRICT_JD' : r'江东',
                'DISTRICT_JB' : r'江北',
                'DISTRICT_XS' : r'象山',
                'DISTRICT_ZH' : r'镇海',
                'DISTRICT_YY' : r'余姚',
                'DISTRICT_FH' : r'奉化',
                'DISTRICT_CX' : r'慈溪',
                'DISTRICT_NH' : r'宁海'
                }
print districtDict.keys()


dataCount = {
             'DISTRICT_BL' : 0,
             'DISTRICT_YZ' : 0,
             'DISTRICT_HS' : 0,
             'DISTRICT_JD' : 0,
             'DISTRICT_JB' : 0,
             'DISTRICT_XS' : 0,
             'DISTRICT_ZH' : 0,
             'DISTRICT_YY' : 0,
             'DISTRICT_FH' : 0,
             'DISTRICT_CX' : 0,
             'DISTRICT_NH' : 0
             }

for line in reader:
    for key in districtDict.keys():
        if re.match(pattern+districtDict[key], line[0]):
            #print pattern+key
            dataCount[key]=dataCount[key]+1
print dataCount
    