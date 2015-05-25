#!/usr/bin/env python3

import urllib.request

def configure_auth():
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    
    password_mgr.add_password(None, 'http://www.pythonchallenge.com/pc/return/', 'huge', 'file')
    password_mgr.add_password(None, 'http://www.pythonchallenge.com/pc/hex/', 'butter', 'fly')
    password_mgr.add_password(None, 'http://www.pythonchallenge.com/pc/ring/', 'repeat', 'switch')
    password_mgr.add_password(None, 'http://www.pythonchallenge.com/pc/rock/', 'kohsamui', 'thailand')
    
    auth_handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    opener = urllib.request.build_opener(auth_handler)
    urllib.request.install_opener(opener)
