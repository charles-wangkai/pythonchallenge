#!/usr/bin/env python3

# Q: http://www.pythonchallenge.com/pc/def/oxygen.html
# A: http://www.pythonchallenge.com/pc/def/integrity.html

import re
import urllib
from PIL import Image

def is_gray(pixel):
    return pixel[0] == pixel[1] and pixel[1] == pixel[2]

def main():
    local_filename = urllib.request.urlretrieve('http://www.pythonchallenge.com/pc/def/oxygen.png')[0]
    image = Image.open(local_filename)
    width = image.size[0]
    
    y = 0
    while True:
        pixel = image.getpixel((0, y))
        if is_gray(pixel):
            break
        y += 1
    
    text = ''
    for x in range(0, width + 1, 7):
        pixel = image.getpixel((x, y))
        if not is_gray(pixel):
            break
        text += chr(image.getpixel((x, y))[0])
    print(text)
    
    print(''.join(map(chr, map(int, re.findall(r'\d+', text)))))

if __name__ == '__main__':
    main()
