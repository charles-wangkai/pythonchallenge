#!/usr/bin/env python3

# Q: http://www.pythonchallenge.com/pc/ring/grandpa.html
# A: http://www.pythonchallenge.com/pc/rock/arecibo.html (username: kohsamui / password: thailand)

import urllib.request, urllib.parse
import webbrowser
from PIL import Image
import PC_Util

MIN_X, MIN_Y, RANGE_X, RANGE_Y = 0.34, 0.57, 0.036, 0.027
MAX_ITERATION = 128

def compute_mandelbrot(c):
    z = 0
    for i in range(MAX_ITERATION):
        z = z * z + c
        if abs(z) >= 2:
            break
    return i

def factorize(n):
    for i in range(2, n):
        if n % i == 0:
            return i, n // i

def main():
    webbrowser.open('https://www.google.com/#newwindow=1&q={keywords}'.format(keywords=urllib.parse.quote_plus('grandpa rock')))
    
    PC_Util.configure_auth()
    local_filename = urllib.request.urlretrieve('http://www.pythonchallenge.com/pc/rock/mandelbrot.gif')[0]
    image = Image.open(local_filename)
    width, height = image.size
    
    diffs = []
    for y in range(height):
        for x in range(width):
            mandelbrot_iter = compute_mandelbrot(complex(MIN_X + RANGE_X / width * x, MIN_Y + RANGE_Y / height * (height - 1 - y)))
            pixel = image.getpixel((x, y))
            if mandelbrot_iter != pixel:
                diffs.append(mandelbrot_iter < pixel)
    
    out_width, out_height = factorize(len(diffs))
    out_image = Image.new('1', (out_width, out_height))
    out_image.putdata(diffs)
    
    out_image.show()
    out_image.close()
    
    webbrowser.open('http://en.wikipedia.org/wiki/Arecibo_message')

if __name__ == '__main__':
    main()
