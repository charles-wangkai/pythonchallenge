#!/usr/bin/env python3

# Q: http://www.pythonchallenge.com/pc/return/good.html
# A: http://www.pythonchallenge.com/pc/return/bull.html

import re
import urllib
from PIL import Image, ImageDraw

def configure_auth():
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, 'http://www.pythonchallenge.com', 'huge', 'file')
    auth_handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    opener = urllib.request.build_opener(auth_handler)
    urllib.request.install_opener(opener)

def parse_points(source, keyword):
    return list(map(int, re.search(r'(?:' + keyword + ':)(.+?)(?:^$)', source, re.MULTILINE | re.DOTALL).group(1).replace('\n', '').split(sep=',')))

def main():
    configure_auth()
    source = urllib.request.urlopen('http://www.pythonchallenge.com/pc/return/good.html').read().decode()
    
    first = parse_points(source, 'first')
    second = parse_points(source, 'second')

    image = Image.new('1', (512, 512))
    draw = ImageDraw.Draw(image)
    draw.polygon(first, outline=1)
    draw.polygon(second, outline=1)
    image.show()
    image.close()
    
if __name__ == '__main__':
    main()
