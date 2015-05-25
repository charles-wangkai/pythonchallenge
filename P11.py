#!/usr/bin/env python3

# Q: http://www.pythonchallenge.com/pc/return/5808.html
# A: http://www.pythonchallenge.com/pc/return/evil.html

import urllib.request
from PIL import Image
import PC_Util

def main():
    PC_Util.configure_auth()
    local_filename = urllib.request.urlretrieve('http://www.pythonchallenge.com/pc/return/cave.jpg')[0]
    image = Image.open(local_filename)
    width, height = image.size
    
    out_width = width // 2
    out_height = height // 2
    out_image = Image.new('RGBA', (out_width, out_height))
    for y in range(out_height):
        for x in range(out_width):
            out_image.putpixel((x, y), image.getpixel((x * 2, y * 2)))
    out_image.show()
    out_image.close()

if __name__ == '__main__':
    main()
