#!/usr/bin/env python3

# Q: http://www.pythonchallenge.com/pc/rock/beer.html
# A: http://www.pythonchallenge.com/pc/rock/gremlins.html

import math
from operator import itemgetter
import time
import urllib.request
from PIL import Image
import PC_Util

def main():
    PC_Util.configure_auth()
    local_filename = urllib.request.urlretrieve('http://www.pythonchallenge.com/pc/rock/beer2.png')[0]
    image = Image.open(local_filename)
    colors = image.getcolors()
    data = image.getdata()
    
    for i in range(len(colors) // 2, 0, -1):
        size = int(math.sqrt(sum(map(itemgetter(0), colors[:i * 2]))))
        
        out_image = Image.new('L', (size, size))
        color_limit = colors[i * 2 - 1][1]
        out_image.putdata([255 / color_limit * pixel for pixel in data if pixel <= color_limit])
     
        out_image.show()
        out_image.close()
        
        time.sleep(2)

if __name__ == '__main__':
    main()
