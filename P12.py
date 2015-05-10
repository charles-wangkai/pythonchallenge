#!/usr/bin/env python3

# Q: http://www.pythonchallenge.com/pc/return/evil.html
# A: http://www.pythonchallenge.com/pc/return/disproportional.html

import subprocess
import tempfile
import time
import urllib

def configure_auth():
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, 'http://www.pythonchallenge.com', 'huge', 'file')
    auth_handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    opener = urllib.request.build_opener(auth_handler)
    urllib.request.install_opener(opener)
    
def main():
    configure_auth()
    local_filename = urllib.request.urlretrieve('http://www.pythonchallenge.com/pc/return/evil2.gfx')[0]
    content = open(local_filename, 'r+b').read()
    
    PART_NUM = 5
    for i in range(PART_NUM):
        out_file = tempfile.NamedTemporaryFile()
        out_file.write(content[i::PART_NUM])
        subprocess.call(['open', '-a', '/Applications/Firefox.app', out_file.name])
        time.sleep(1)

if __name__ == '__main__':
    main()
