#! /usr/bin/python


import os,sys
import math
from PIL import Image
import configparser 


P = 20037508.3427892   #perimeter of earth
WORLDBOUND = (-P,-P,P,P)	#world bound by meters
WORLDLNGLAT = (-180,-85.05112877980659,180,85.05112877980659) #world bound by longitude/latitude
levels = range(1,20)	#level 0-19
resolution = [(P*2/256/(2**z)) for z in levels]	# meter/pixel

tileSize = (256,256)
levelRange = (14,16)	#(min,max)
#center = (0,0)	# center of image


def calImageBound(level, image, center):
	width,height = image.size
	xmin = 0
	xmax = int(width/256)
	ymin = 0
	ymax = int(height/256)

	west = center[0]-width/2*resolution[level-1]
	south = center[1]-height/2*resolution[level-1]
	east = center[0]+width/2*resolution[level-1]
	north = center[1]+height/2*resolution[level-1]

	f=open("./output.txt","a")

	f.write("\n---------------\nwest:%.15f\nsouth:%.15f\neast:%.15f\nnorth:%.15f\n"%(west,south,east,north))
	f.close()



#
def cutImage(level, image, center):
	width,height = image.size

	xmin = 0
	xmax = int(width/256)
	ymin = 0
	ymax = int(height/256)

	west = center[0]-width/2*resolution[level-1]
	south = center[1]-height/2*resolution[level-1]
	east = center[0]+width/2*resolution[level-1]
	north = center[1]+height/2*resolution[level-1]

	for j in range(ymin, ymax):
		for i in range(xmin, xmax):
			left = int(math.floor((west+P)/resolution[level-1]/256)) + i
			top = int(math.floor((P-north)/resolution[level-1]/256)) + j

			box = (256*i,256*j,256*(i+1),256*(j+1))		
			# top = int(math.floor((P-north)/256))
			# bottom = int(math.floor((P-south)/256+1))
			# left = int(math.floor((west+P)/256))
			# right = int(math.floor((east+P)/256+1))
			
			im = image.crop(box)
			saveurl = './tile/%d/%d/'%(level,left)
			if not os.path.exists(saveurl):
				os.makedirs(saveurl)
			im.save(saveurl+str(top)+".png", "PNG")



def doCut(configfile):
	scp = configparser.ConfigParser()
	scp.read(configfile)
	x = float(scp["base"]["center-x"])
	y = float(scp["base"]["center-y"])
	center = (x,y)
	filename = scp["base"]["filename"]

	img = Image.open(filename)
	if(img.size[0]%256 != 0 or img.size[1]%256 != 0):
		print("resolution not fit requirement, please provide image with right resolution")
		os.exit(1)

	tileNos = min(img.size[0],img.size[1])/256
	span = math.log(tileNos)/math.log(2)
	zmax = int(scp["base"]["zmax"])
	zmin = zmax-int(span)+1


	print("The size of image is: %dpx wide and %dpx height\n"%(img.size[0],img.size[1]))
	print("" + str(img.size[0]/256) + " tiles horizontally")
	print("" + str(img.size[1]/256) + " tiles vertically")
	print("minimum spilt: " + str(tileNos) + " tiles at most")
	print("The split span should be no more than " + str(span) + " levels")
	print("The current level is " + str(zmax))
	print("the target level is " + str(zmax-int(span)+1))

	#calculate image Bound
	calImageBound(zmax,img,center)
	#cut tiles
	cutImage(zmax,img,center)
	for level in range(zmax-1,zmin-1,-1):
		width,height = img.size
		width = width+256 if int(width/256)&1 else width
		height = height+256 if int(height/256)&1 else height
		
		
		img = img.resize((int(width/2),int(height/2)), Image.ANTIALIAS)
		cutImage(level, img, center)

	print("imageCutting Completed!")


if __name__ == "__main__":
	doCut("input.conf")









