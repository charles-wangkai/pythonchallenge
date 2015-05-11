#!/usr/bin/env python3

# Q: http://www.pythonchallenge.com/pc/return/disproportional.html
# A: http://www.pythonchallenge.com/pc/return/italy.html

import re
import urllib
import xmlrpc.client

def configure_auth():
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, 'http://www.pythonchallenge.com', 'huge', 'file')
    auth_handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    opener = urllib.request.build_opener(auth_handler)
    urllib.request.install_opener(opener)
    
def main():
    configure_auth()
    pic_content = urllib.request.urlopen('http://www.pythonchallenge.com/pc/return/evil4.jpg').read().decode()
    print(pic_content)
    evil = re.search(r'(.+) is evil', pic_content).group(1)
    
    server = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
    print(server.phone(evil))

if __name__ == '__main__':
    main()
