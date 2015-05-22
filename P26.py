#!/usr/bin/env python3

# Q: http://www.pythonchallenge.com/pc/hex/decent.html
# A: http://www.pythonchallenge.com/pc/hex/speedboat.html

from email.mime.text import MIMEText
import getpass
import hashlib
import imaplib
import re
import smtplib
import tempfile
import time
import zipfile
from PIL import Image
import P19
import P24

def send_email(from_addr, password, to_addr, subject):
    msg = MIMEText('')
    msg['From'], msg['To'] = from_addr, to_addr
    msg['Subject'] = subject
    
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login(from_addr, password)
    smtp.sendmail(from_addr, to_addr, msg.as_string())
    smtp.quit()

def receive_email(user, password, sender):
    imap4 = imaplib.IMAP4_SSL('imap.gmail.com')
    imap4.login(user, password)
    imap4.select()
    last_msgnum = imap4.search(None, '(FROM "{sender}")'.format(sender=sender))[1][0].split()[-1]
    body = imap4.fetch(last_msgnum, '(BODY[TEXT])')[1][0][1].decode()
    return body

def calc_md5(content):
    hash_obj = hashlib.md5()
    hash_obj.update(content)
    return hash_obj.hexdigest()

def fix_one_byte_mistake(content, target_md5):
    for i in range(len(content)):
        for byte in range(256):
            fixed_content = content[:i] + bytes([byte]) + content[i + 1:]
            if calc_md5(fixed_content) == target_md5:
                return fixed_content

def main():
    from_addr = 'goalboy@gmail.com'
    password = getpass.getpass('Password for {email}: '.format(email=from_addr))
    to_addr = P19.retrive_leopold_addr()
    subject = 'sorry'
    send_email(from_addr, password, to_addr, subject)
    
    time.sleep(10)
    reply_body = receive_email(from_addr, password, to_addr)
    print(reply_body)
     
    target_md5 = re.search(r'md5: (\S+)', reply_body).group(1)    
    fixed_content = fix_one_byte_mistake(P24.solve_zipfile().read('mybroken.zip'), target_md5)
    
    out_file = tempfile.TemporaryFile()
    out_file.write(fixed_content)
    
    zf = zipfile.ZipFile(out_file)
    
    image = Image.open(zf.open('mybroken.gif'))
    image.show()

if __name__ == '__main__':
    main()
