#!/usr/bin/env python3

# Q: http://www.pythonchallenge.com/pc/return/italy.html
# A: http://www.pythonchallenge.com/pc/return/uzi.html

import urllib.request
from PIL import Image
import PC_Util

index = 0
x, y = -1, 0

def fill(image, out_image, offset_x, offset_y, step):
    global index, x, y
    for _ in range(step):
        x += offset_x
        y += offset_y
        out_image.putpixel((x, y), image.getpixel((index, 0)))
        index += 1

def main():
    PC_Util.configure_auth()
    local_filename = urllib.request.urlretrieve('http://www.pythonchallenge.com/pc/return/wire.png')[0]
    image = Image.open(local_filename)
    
    out_width, out_height = 100, 100
    out_image = Image.new('RGBA', (out_width, out_height))
    
    step = 100
    while step:
        fill(image, out_image, 1, 0, step)
        step -= 1
        fill(image, out_image, 0, 1, step)
        fill(image, out_image, -1, 0, step)
        step -= 1
        fill(image, out_image, 0, -1, step)
    out_image.show()
    out_image.close()

if __name__ == '__main__':
    main()
