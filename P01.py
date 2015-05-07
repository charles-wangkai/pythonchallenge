#!/usr/bin/env python3

# Q: http://www.pythonchallenge.com/pc/def/map.html
# A: http://www.pythonchallenge.com/pc/def/ocr.html

import string

def decode(text):
    alphabet = string.ascii_lowercase
    return text.translate(str.maketrans(alphabet, alphabet[2:] + alphabet[:2]))

def main():
    origin = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    print(decode(origin))
    
    print(decode("map"))

if __name__ == '__main__':
    main()
