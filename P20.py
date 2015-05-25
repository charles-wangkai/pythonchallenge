#!/usr/bin/env python3

# Q: http://www.pythonchallenge.com/pc/hex/idiot2.html
# A: A zip file including embedded 'readme.txt' and 'package.pack' files

import re
import tempfile
import urllib.request
import zipfile
import PC_Util

content_length = None
zip_file = None
pwd = None

def request_url(bytes_start=None):
    headers = {}
    if bytes_start:
        headers = {'Range': 'bytes={bytes_start}-{content_length}'.format(bytes_start=bytes_start, content_length=content_length)}
    
    request = urllib.request.Request('http://www.pythonchallenge.com/pc/hex/unreal.jpg', headers=headers)
    return urllib.request.urlopen(request)

def extract_content_range(f):
    content_range = f.info().get('Content-Range')
    match = re.search(r'(\d+)-(\d+)/(\d+)', content_range)
    return (int(match.group(1)), int(match.group(2)), int(match.group(3)))

def download_zip_file():
    global content_length, zip_file, pwd
    
    PC_Util.configure_auth()
    
    bytes_end, content_length = extract_content_range(request_url())[1:3]
    
    bytes_start = bytes_end + 1
    while True:
        try:
            f = request_url(bytes_start)
        except urllib.error.HTTPError:
            break
        
        content = f.read().decode()
        print(content)
        
        match = re.search(r'ok, (\w+)', content)
        if match:
            nickname = match.group(1)
            pwd = nickname[::-1].encode()
        
        bytes_start = extract_content_range(f)[1] + 1
    
    bytes_start = content_length
    while True:
        try:
            f = request_url(bytes_start)
        except urllib.error.HTTPError:
            break
        
        content = f.read().decode()
        print(content)
        
        match = re.search(r'it is hiding at (\d+)', content)
        if match:
            hiding_bytes_start = int(match.group(1))
        
        bytes_start = extract_content_range(f)[0] - 1
    
    local_file = tempfile.TemporaryFile()
    local_file.write(request_url(hiding_bytes_start).read())
    
    zip_file = zipfile.ZipFile(local_file)

def read_zip_file(name):
    if not zip_file:
        download_zip_file()
    return zip_file.open(name, pwd=pwd).read()

def main():
    print(read_zip_file('readme.txt').decode())

if __name__ == '__main__':
    main()
