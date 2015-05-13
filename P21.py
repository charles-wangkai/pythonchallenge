#!/usr/bin/env python3

# Q: (From Level 20) A zip file including embedded 'readme.txt' and 'package.pack' files
# A: http://www.pythonchallenge.com/pc/hex/copper.html

import bz2
import zlib
import P20

def main():
    print(P20.read_zip_file('readme.txt').decode())
    
    data = P20.read_zip_file('package.pack')
    
    logs = ''
    tried_reverse = False
    while True:
        try:
            data = zlib.decompress(data)
            logs += '.'
            tried_reverse = False
            continue
        except:
            pass
        
        try:
            data = bz2.decompress(data)
            logs += '#'
            tried_reverse = False
            continue
        except:
            pass
        
        if tried_reverse:
            break
        
        data = data[::-1]
        logs += '\n'
        tried_reverse = True
    
    print(data.decode())
    print(logs)

if __name__ == '__main__':
    main()
