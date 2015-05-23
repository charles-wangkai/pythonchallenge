#!/usr/bin/env python3

# Q: http://www.pythonchallenge.com/pc/ring/yankeedoodle.html
# A: http://www.pythonchallenge.com/pc/ring/grandpa.html

import urllib.request
from PIL import Image

def configure_auth():
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, 'http://www.pythonchallenge.com', 'repeat', 'switch')
    auth_handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    opener = urllib.request.build_opener(auth_handler)
    urllib.request.install_opener(opener)

def factorize(n):
    for i in range(2, n):
        if n % i == 0:
            return n // i, i

def main():
    configure_auth()
    local_filename = urllib.request.urlretrieve('http://www.pythonchallenge.com/pc/ring/yankeedoodle.csv')[0]
    numbers = open(local_filename).read().replace(',', '').split()
    
    width, height = factorize(len(numbers))
    out_image = Image.new('L', (width, height))
    
    index = 0
    for x in range(width):
        for y in range(height):
            out_image.putpixel((x, y), float(numbers[index]) * 256)
            index += 1
    
    out_image.show()
    out_image.close()
    
    print(''.join(map(lambda x: chr(int(x)), [str(numbers[i])[5] + str(numbers[i + 1])[5] + str(numbers[i + 2])[6] for i in range(0, ((len(numbers) + 2) // 3 - 1) * 3, 3)])))

if __name__ == '__main__':
    main()
