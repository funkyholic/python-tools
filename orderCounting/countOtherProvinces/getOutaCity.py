# -*- coding: utf-8 -*-

import re
import csv


datafile = r'outaNingboData.csv'
csvfile = file(datafile,'r')
reader = csv.reader(csvfile)


pattern = r'^(?P<province>.*?(?P<f1>省|市))(?P<city>.*?(?P<f2>市|区|县))'

testData = ['上海市虹口区虹口区梧州路299弄7号1605','广东省深圳市罗湖区东晓路3038号太白居']

datalist = {}

for line in reader:
    result = re.match(pattern,line[0])
    if result:
        if result.group('f1') == '市':
            if datalist.has_key(result.group('province')):
                datalist[result.group('province')] = datalist[result.group('province')]+1
            else:
                datalist[result.group('province')] = 1
        elif result.group('f1') == '省':
            if datalist.has_key(result.group('city')):
                datalist[result.group('city')] = datalist[result.group('city')]+1
            else:
                datalist[result.group('city')] = 1


for item in datalist:
    print item+','+str(datalist[item])+','
