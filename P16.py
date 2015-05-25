#!/usr/bin/env python3

# Q: http://www.pythonchallenge.com/pc/return/mozart.html
# A: http://www.pythonchallenge.com/pc/return/romance.html

import urllib.request
from PIL import Image
import PC_Util

MARKER_LEFT_COLOR = [255, 0, 255]

def find_offset(image, y):
    palette = image.getpalette()
    for x in range(image.size[0]):
        color_index = image.getpixel((x, y))
        if palette[color_index * 3:color_index * 3 + 3] == MARKER_LEFT_COLOR:
            return x - 1

def main():
    PC_Util.configure_auth()
    local_filename = urllib.request.urlretrieve('http://www.pythonchallenge.com/pc/return/mozart.gif')[0]
    image = Image.open(local_filename)
    width, height = image.size
    
    out_image = Image.new('P', (width, height))
    out_image.putpalette(image.getpalette())
    for y in range(height):
        offset = find_offset(image, y)
        for x in range(width):
            out_image.putpixel((x, y), image.getpixel(((x + offset) % width, y)))
    out_image.show()
    out_image.close()

if __name__ == '__main__':
    main()
