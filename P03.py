#!/usr/bin/env python3

# Q: http://www.pythonchallenge.com/pc/def/equality.html
# A: http://www.pythonchallenge.com/pc/def/linkedlist.php

import re
import urllib.request

def main():
    source = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/equality.html').read().decode()
    mess = re.findall(r'(?<=<!--).*?(?=-->)', source, flags=re.DOTALL)[0].replace('\n', '')
    print(''.join(re.findall(r'(?<=[^A-Z][A-Z]{3})[a-z](?=[A-Z]{3}[^A-Z])', mess)))

if __name__ == '__main__':
    main()
