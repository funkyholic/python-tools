from PIL import Image
import os


import algorithm

loadpath = "./captcha/"
savepath = "./char/"

for file in os.listdir(loadpath):
    if(file.endswith(".jpeg")):

        img = Image.open(loadpath+file).convert("L")

        # img = ImageEnhance.Sharpness(img).enhance(10)

        #两次4邻域去噪
        img = algorithm.depoint(img)
        img = algorithm.depoint(img)

        w,h = img.size
        img = img.crop((2,2,w-2,h-2))
        img.save(savepath + file.split(".")[0] + ".png")




