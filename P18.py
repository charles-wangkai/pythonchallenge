#!/usr/bin/env python3

# Q: http://www.pythonchallenge.com/pc/return/balloons.html
# A: http://www.pythonchallenge.com/pc/hex/bin.html (username: butter / password: fly)

from difflib import Differ
import gzip
import tempfile
import urllib.request
from PIL import Image
import PC_Util

def main():
    PC_Util.configure_auth()
    local_filename = urllib.request.urlretrieve('http://www.pythonchallenge.com/pc/return/deltas.gz')[0]
    f = gzip.open(local_filename)
    lines = f.read().decode().splitlines()
    
    lefts = []
    rights = []
    for line in lines:
        lefts.append(line[:53])
        rights.append(line[56:])
    
    diff_result = list(Differ().compare(lefts, rights))
    
    for marker in ['  ', '+ ', '- ']:
        out_file = tempfile.TemporaryFile()
        out_file.write(bytearray(list(map(lambda x: int(x, base=16), ''.join(map(lambda line: line[1:], filter(lambda line: line.startswith(marker), diff_result))).split()))))
        Image.open(out_file).show()

if __name__ == '__main__':
    main()
