#!/usr/bin/env python3

# Q: http://www.pythonchallenge.com/pc/hex/speedboat.html
# A: http://www.pythonchallenge.com/pc/ring/bell.html (username: repeat / password: switch)

import builtins
import bz2
import keyword
import urllib.request
from PIL import Image
import PC_Util

def is_reserved_word(word):
    return word in keyword.kwlist or word in dir(builtins)

def main():
    PC_Util.configure_auth()
    local_filename = urllib.request.urlretrieve('http://www.pythonchallenge.com/pc/hex/zigzag.gif')[0]
    image = Image.open(local_filename)
    
    original_content = ''.join(map(chr, image.getdata()))
    
    translated_content = original_content.translate(str.maketrans(''.join([chr(i) for i in range(256)]), ''.join(map(chr, image.getpalette()[::3]))))
    
    content_pairs = list(zip(original_content[1:], translated_content[:-1]))
    
    new_im = Image.new('1', image.size)
    new_im.putdata([pair[0] == pair[1] for pair in content_pairs])
    new_im.show()
    
    diffs = list(filter(lambda pair: pair[0] != pair[1], content_pairs))
    words = bz2.decompress(''.join(list(zip(*diffs))[0]).encode('latin-1')).decode().split()
    
    for word in set(words):
        if not is_reserved_word(word):
            print(word)

if __name__ == '__main__':
    main()
