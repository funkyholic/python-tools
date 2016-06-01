
import pytesseract
import os

from PIL import Image,ImageEnhance

# def binarize_image(img):
#     pixdata = img.load()
#     for y in range(img.size[1]):
#         for x in range(img.size[0]):
#             if pixdata[x,y][0] < 100 or pixdata[x,y][1] < 100 or pixdata[x,y][2] < 100:
#                 pixdata[x,y] = (0,0,0,255)
#             else:
#                 pixdata[x, y] = (255, 255, 255, 255)
#
#     return img



for file in os.listdir("./char/"):
    if(file.endswith(".png")):
        image = Image.open("./char/"+file)
        text = pytesseract.image_to_string(image,lang="eng",config="-psm 8 hteawords")
        print(text)


