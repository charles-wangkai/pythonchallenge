#!/usr/bin/env python3

# Q: http://www.pythonchallenge.com/pc/def/ocr.html
# A: http://www.pythonchallenge.com/pc/def/equality.html

from collections import Counter
from operator import itemgetter
import re
import urllib


def main():
    source = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html').read().decode()
    mess = re.findall(r'(?<=<!--).*?(?=-->)', source, flags=re.DOTALL)[1].replace('\n', '')
    rares = ''.join(map(itemgetter(0), filter(lambda element: element[1] == 1, Counter(mess).most_common())))
    print(re.sub(r'[^' + rares + ']', '', mess))

if __name__ == '__main__':
    main()
