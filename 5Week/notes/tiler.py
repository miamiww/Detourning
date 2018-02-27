import glob
from PIL import Image
import random

blank_image = Image.new('RGB', (500,500), (255,255,255))

x=0
y=0

#lets you get lists of files
jpegs = glob.glob('babies/*.jpg')
for jpg in jpegs:
    im = Image.open(jpg)
    im.thumbnail((201,201))
    width = im.size[0]
    height = im.size[1]
    # x = random.randint(0,500)
    # y = random.randint(0,500)
    blank_image.paste(im,(x,y))
    x = x+width
    if x > 500:
        x = 0
        y = y+height

blank_image.save('allbabies.jpg')
