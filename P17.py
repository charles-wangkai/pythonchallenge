#!/usr/bin/env python3

# Q: http://www.pythonchallenge.com/pc/return/romance.html
# A: http://www.pythonchallenge.com/pc/return/balloons.html

import bz2
import http.cookiejar
import re
import urllib.request, urllib.parse
import xmlrpc.client

def configure_cookies():
    cookie_jar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))
    urllib.request.install_opener(opener)
    return cookie_jar

def get_info_cookie(cookie_jar):
    for cookie in cookie_jar:
        if cookie.name == 'info':
            return cookie

def get_info_cookie_value(cookie_jar):
    return get_info_cookie(cookie_jar).value

def set_info_cookie_value(cookie_jar, value):
    get_info_cookie(cookie_jar).value = urllib.parse.quote_plus(value)

def main():
    cookie_jar = configure_cookies()
    
    urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php')
    print(get_info_cookie_value(cookie_jar))
      
    cookie_values = ''
    busynothing = 12345
    while True:
        source = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing={busynothing}'.format(busynothing=busynothing)).read().decode()
        print(source)
        cookie_values += get_info_cookie_value(cookie_jar)
          
        match = re.search(r'the next busynothing is (\d+)', source)
        if match:
            busynothing = int(match.group(1))
        else:
            break
    print(bz2.decompress(urllib.parse.unquote_to_bytes(cookie_values.replace('+', ' '))).decode())
    
    server = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
    print(server.phone('Leopold'))
    
    set_info_cookie_value(cookie_jar, 'the flowers are on their way')
    source = urllib.request.urlopen('http://www.pythonchallenge.com/pc/stuff/violin.php').read().decode()
    print(re.search(r'(.+)</font>', source).group(1))

if __name__ == '__main__':
    main()
