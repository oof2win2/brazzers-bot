# This file is here just to test things using the different libraries so it isn't in main.py
# Shouldn't be in final release (idk)

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

choice = 2
# attempts to open the image from input.extension and converts to RGBA
img = Image.open('input.jpg').convert('RGBA')

# outputs the size of the image
width, height = img.size
#print('original width, height: ', width, height) #debug output

# creates the watermark as a new image, as if just overlaying one image with the other
if (choice == 1):
    #Brazzers watermark
    watermark = Image.open('watermarks/brazzers.png').convert('RGBA')
elif (choice == 2):
    #FakeTaxi watermark
    watermark = Image.open('watermarks/faketaxi.png').convert('RGBA')
watermark = watermark.resize((round(width/3.375), round(height/6))) ##resizes watermark to make it smaller and make it be in a 16:9 aspect ratio
w, h = watermark.size

#print('overlay width, height', w, h) #debug output

img.paste(watermark, (width - w - round(width/50), height - h), watermark) #pasting the watermark onto the import image
img.save('out.png')
img.show() #debug output
