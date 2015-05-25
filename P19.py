#!/usr/bin/env python3

# Q: http://www.pythonchallenge.com/pc/hex/bin.html
# A: http://www.pythonchallenge.com/pc/hex/idiot2.html

import audioop
import email
import re
import subprocess
import tempfile
import time
import urllib.request
import wave
import PC_Util

def download_email():
    PC_Util.configure_auth()
    source = urllib.request.urlopen('http://www.pythonchallenge.com/pc/hex/bin.html').read().decode()

    email_content = re.search(r'<!--\s+(.+)\s+-->', source, re.DOTALL).group(1)
    return email.message_from_string(email_content)

def retrive_leopold_addr():
    return download_email().get('From')

def main():
    email_message = download_email()
    for part in email_message.walk():
        if part.get_content_maintype() == 'audio':
            wave_file = tempfile.NamedTemporaryFile()
            wave_file.write(part.get_payload(decode=True))
    
    wave_read = wave.open(wave_file.name, 'rb')
    
    swapped_wave_file = tempfile.NamedTemporaryFile(suffix='.wav')
    wave_write = wave.open(swapped_wave_file.name, 'wb')
    wave_write.setparams(wave_read.getparams())
    wave_write.writeframes(audioop.byteswap(wave_read.readframes(wave_read.getnframes()), wave_read.getsampwidth()))
     
    subprocess.call(['open', '-a', '/Applications/MPlayerX.app', swapped_wave_file.name])
    time.sleep(1)

if __name__ == '__main__':
    main()
