#!/usr/bin/env python3

# Q: http://www.pythonchallenge.com/pc/ring/guido.html
# A: http://www.pythonchallenge.com/pc/ring/yankeedoodle.html

import bz2
import urllib.request
import PC_Util

def main():
    PC_Util.configure_auth()
    source = urllib.request.urlopen('http://www.pythonchallenge.com/pc/ring/guido.html').read().decode()
    
    print(bz2.decompress(''.join(map(chr, map(len, filter(lambda line: not line.strip(), source.split('\n'))))).encode('latin-1')).decode())

if __name__ == '__main__':
    main()
