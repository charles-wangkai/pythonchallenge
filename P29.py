#!/usr/bin/env python3

# Q: http://www.pythonchallenge.com/pc/ring/guido.html
# A: http://www.pythonchallenge.com/pc/ring/yankeedoodle.html

import bz2
import urllib.request

def configure_auth():
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, 'http://www.pythonchallenge.com', 'repeat', 'switch')
    auth_handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    opener = urllib.request.build_opener(auth_handler)
    urllib.request.install_opener(opener)

def main():
    configure_auth()
    source = urllib.request.urlopen('http://www.pythonchallenge.com/pc/ring/guido.html').read().decode()
    
    print(bz2.decompress(''.join(map(chr, map(len, filter(lambda line: not line.strip(), source.split('\n'))))).encode('latin-1')).decode())

if __name__ == '__main__':
    main()
