#-*-coding:utf-8-*-
import json
import csv


csvfile = file('station.csv','r')
csvreader = csv.reader(csvfile)

f = open("./data.json",'r')
s = f.read()
		

s1 = json.loads(s)


datalist = []
for station in csvreader:
	count = 0
	for item in s1:		#csv23
		if (abs(float(station[1])-item["lng"])<=0.009) and (abs(float(station[2])-item["lat"])<=0.01):
			count += 1

	print station[0],count
	datalist.append({"addr":station[0], "lng": station[1], "lat": station[2], "count": count})
		
result = json.dumps(datalist)
print result

saveFile = open(r"./output.json","w")
saveFile.write(result)
saveFile.close()

csvfile.close()
f.close()