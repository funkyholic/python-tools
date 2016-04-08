'''
Created on Jan 27, 2016

@author: htea
'''

import urllib,urllib2
import json
import csv
import time
import socket

datafile = r'addressTable.csv'
csvfile = file(datafile,'r')
reader = csv.reader(csvfile)

output = file('./output.json', 'w')	#
info = file('./info.txt','a')	#


#Geo
#'http://api.map.baidu.com/geocoder/v2/?
#
#ak=.....	
#output=json	json

url = r'http://api.map.baidu.com/geocoder/v2/?ak=DQlcYg7B3xmcie53rjENGnak&output=json&'
headers = {'User-agent' : 'Mozilla/5.0'}
count = 0

for line in reader:
    count=count+1

    try:
        values = {
                  'address':line[0],
                  }
        data = urllib.urlencode(values)	#url
        request = urllib2.Request(url+data)	# "&"
        response = urllib2.urlopen(request,timeout=3)	#http
        jsob = json.loads(response.read())	#json
        
    except urllib2.HTTPError,e:	#http
        print e.reason
    except socket.error,e:	#socket3
        print e
        time.sleep(3)
        
#     
    if jsob.has_key('result'):
        location = jsob["result"]["location"]
        location['address'] = line[0]
        writedata = json.dumps(location)
        print count,writedata
        output.write(writedata+',')
    else:
        info.write('line%d no response --(%s)\n' %(count,line[0]))	#info.txt 
#     
    if (count%100) == 0:	#100 
        output.flush()
        info.write('%d addresses have been saved\n' % (count))
        info.flush()
    
        
info.close()
csvfile.close()
output.close()
    
        