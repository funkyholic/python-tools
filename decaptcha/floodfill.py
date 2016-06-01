
#迭代flood fill填充法
#from http://stackoverflow.com/questions/11746766/flood-fill-algorithm-python

def floodFill(x,y,g,h,i,image):
    toFill = set()
    toFill.add((x,y))
    while not toFill == set():
        (x,y) = toFill.pop()
        (a,b,c) = image.getpixel((x,y))
        if not (a,b,c) == (255, 255, 255):
            continue
        image.putpixel((x,y), (g,h,i))
        toFill.add((x-1,y))
        toFill.add((x+1,y))
        toFill.add((x,y-1))
        toFill.add((x,y+1))
    # image.save("flood.png")