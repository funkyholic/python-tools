from PIL import Image,ImageFilter,ImageEnhance
from numpy import *
import os
from scipy.ndimage import filters
import rof

loadpath = "./captcha/"
savepath = "./char/"


#图像处理

for file in os.listdir(loadpath):
    if(file.endswith(".jpeg")):

        im = Image.open(loadpath+file).convert("L")

        w,h =im.size
        im = im.crop((1,1,w-1,h-1)) #去除黑边

        im = array(im)

        U,T = rof.denoise(im,im)

        img = Image.fromarray(U)

        img = img.convert("L")

        enhancer1 = ImageEnhance.Sharpness(img)
        img = enhancer1.enhance(10)

        # enhancer2 = ImageEnhance.Contrast(img)
        # img = enhancer2.enhance(10)

        # img.show()

        pixdata = img.load()

        w,h = img.size

        #二值化处理
        for y in range(h):
            for x in range(w):
                if pixdata[x,y] < 135:
                    pixdata[x,y] = 0
                else:
                    pixdata[x,y] = 255





        #图放大2倍
        img = img.resize((w*2,h*2),Image.NEAREST)


        img.save(savepath+file.split(".")[0]+".png")

