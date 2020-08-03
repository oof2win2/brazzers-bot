import sys
import time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# attempts to open the image from input.extension and converts to RGBA
img = Image.open('input.jpg').convert('RGBA')

# outputs the size of the image
width, height = img.size
#print('width is: ', width)
#print('height is:', height)

# creates the watermark as a new image, as if just overlaying one image with the other
# watermark = Image.new('watermark.png', (width, height), color=(255, 255, 255, 0))

fnt = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 192)
a = ImageDraw.Draw(img)
a.text((10, 10), "Hello World", font=fnt, fill = (63, 63, 63))

img.save('out.png')
"""
# output process
img.paste(watermark, (0, 0), watermark)
watermark.close()
#display the output image
img.show()
img.save('out.png')
img.close()
"""