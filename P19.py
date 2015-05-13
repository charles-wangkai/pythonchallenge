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

def configure_auth():
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, 'http://www.pythonchallenge.com', 'butter', 'fly')
    auth_handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    opener = urllib.request.build_opener(auth_handler)
    urllib.request.install_opener(opener)

def main():
    configure_auth()
    source = urllib.request.urlopen('http://www.pythonchallenge.com/pc/hex/bin.html').read().decode()

    email_content = re.search(r'<!--\s+(.+)\s+-->', source, re.DOTALL).group(1)
    email_message = email.message_from_string(email_content)
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
