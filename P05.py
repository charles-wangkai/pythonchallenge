#!/usr/bin/env python3

# Q: http://www.pythonchallenge.com/pc/def/peak.html
# A: http://www.pythonchallenge.com/pc/def/channel.html

import pickle
import urllib.request

def main():
    f = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
    lines = pickle.load(f)
    for line in lines:
        print(''.join([elem[0] * elem[1] for elem in line]))

if __name__ == '__main__':
    main()
