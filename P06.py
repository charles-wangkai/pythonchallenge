#!/usr/bin/env python3

# Q: http://www.pythonchallenge.com/pc/def/channel.html
# A: http://www.pythonchallenge.com/pc/def/oxygen.html

import re
import urllib.request
import zipfile

def main():
    local_filename = urllib.request.urlretrieve('http://www.pythonchallenge.com/pc/def/channel.zip')[0]
    zf = zipfile.ZipFile(local_filename)
    member = 'readme.txt'
    comments = ''
    while True:
        content = zf.read(member).decode()
        print(content)
        comments += zf.getinfo(member).comment.decode()

        match = re.search(r'(?:Next nothing is|start from) (\d+)', content)
        if match:
            nothing = int(match.group(1))
            member = '{nothing}.txt'.format(nothing=nothing)
        else:
            break
    print(comments)
    zf.close()

if __name__ == '__main__':
    main()
