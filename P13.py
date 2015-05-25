#!/usr/bin/env python3

# Q: http://www.pythonchallenge.com/pc/return/disproportional.html
# A: http://www.pythonchallenge.com/pc/return/italy.html

import re
import urllib.request
import xmlrpc.client
import PC_Util

def main():
    PC_Util.configure_auth()
    pic_content = urllib.request.urlopen('http://www.pythonchallenge.com/pc/return/evil4.jpg').read().decode()
    print(pic_content)
    evil = re.search(r'(.+) is evil', pic_content).group(1)
    
    server = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
    print(server.phone(evil))

if __name__ == '__main__':
    main()
