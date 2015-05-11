#!/usr/bin/env python3

# Q: http://www.pythonchallenge.com/pc/def/integrity.html
# A: http://www.pythonchallenge.com/pc/return/good.html (username: huge / password: file)

import ast
import bz2
import re
import urllib.request

def main():
    source = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/integrity.html').read().decode()
    un = re.search(r'un: \'(.+)\'', source).group(1)
    pw = re.search(r'pw: \'(.+)\'', source).group(1)
    
    username = bz2.decompress(ast.literal_eval('b"{un}"'.format(un=un))).decode()
    password = bz2.decompress(ast.literal_eval('b"{pw}"'.format(pw=pw))).decode()
    print('username:', username)
    print('password:', password)

if __name__ == '__main__':
    main()
