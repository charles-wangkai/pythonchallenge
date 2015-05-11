#!/usr/bin/env python3

# Q: http://www.pythonchallenge.com/pc/def/linkedlist.php
# A: http://www.pythonchallenge.com/pc/def/peak.html

import re
import urllib.request

def main():
    nothing = 12345
    while True:
        source = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing}'.format(nothing=nothing)).read().decode()
        print(source)
        
        match = re.search(r'the next nothing is (\d+)', source)
        if match:
            nothing = int(match.group(1))
        elif 'Divide by two' in source:
            nothing /= 2
        else:
            break

if __name__ == '__main__':
    main()
