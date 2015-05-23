#!/usr/bin/env python3

# Q: http://www.pythonchallenge.com/pc/ring/bell.html
# A: http://www.pythonchallenge.com/pc/ring/guido.html

import urllib.request
from PIL import Image

def configure_auth():
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, 'http://www.pythonchallenge.com', 'repeat', 'switch')
    auth_handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    opener = urllib.request.build_opener(auth_handler)
    urllib.request.install_opener(opener)

def whodunnit():
    return 'Guido van Rossum'.lower()

def main():
    configure_auth()
    local_filename = urllib.request.urlretrieve('http://www.pythonchallenge.com/pc/ring/bell.png')[0]
    image = Image.open(local_filename)
    width, height = image.size
    
    message = ''
    for y in range(height):
        for x in range(0, width, 2):
            green_pair_diff = abs(image.getpixel((x, y))[1] - image.getpixel((x + 1, y))[1])
            if green_pair_diff != 42:
                message += chr(green_pair_diff)
    print(message)
    
    print(whodunnit().split()[0])

if __name__ == '__main__':
    main()
