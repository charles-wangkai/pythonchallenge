#!/usr/bin/env python3

# Q: http://www.pythonchallenge.com/pc/hex/copper.html
# A: http://www.pythonchallenge.com/pc/hex/bonus.html

import urllib.request
from PIL import Image

BLACK_COLOR = [0, 0, 0]
ORIGIN_X, ORIGIN_Y = 100, 100
OUT_WIDTH, OUT_HEIGHT = 400, 200
OUT_INIT_X, OUT_INIT_Y = 10, 100
OUT_INTERVAL_X = 50

def configure_auth():
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, 'http://www.pythonchallenge.com', 'butter', 'fly')
    auth_handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    opener = urllib.request.build_opener(auth_handler)
    urllib.request.install_opener(opener)

def find_bright(image):
    palette = image.getpalette()
    width, height = image.size
    
    for y in range(height):
        for x in range(width):
            color_index = image.getpixel((x, y))
            if palette[color_index * 3:color_index * 3 + 3] != BLACK_COLOR:
                return x, y

def compute_offset(x, y):
    return x - ORIGIN_X, y - ORIGIN_Y
            
def main():
    configure_auth()
    local_filename = urllib.request.urlretrieve('http://www.pythonchallenge.com/pc/hex/white.gif')[0]
    image = Image.open(local_filename)
    
    out_image = Image.new('1', (OUT_WIDTH, OUT_HEIGHT))
    
    x, y = OUT_INIT_X, OUT_INIT_Y
    while True:
        offset_x, offset_y = compute_offset(*find_bright(image))
        
        if (offset_x, offset_y) == (0, 0):
            offset_x += OUT_INTERVAL_X
        
        x, y = x + offset_x, y + offset_y
        out_image.putpixel((x, y), 1)
        
        try:
            image.seek(image.tell() + 1)
        except EOFError:
            break
        
    out_image.show()
    out_image.close()

if __name__ == '__main__':
    main()
