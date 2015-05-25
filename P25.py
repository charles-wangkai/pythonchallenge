#!/usr/bin/env python3

# Q: http://www.pythonchallenge.com/pc/hex/lake.html
# A: http://www.pythonchallenge.com/pc/hex/decent.html

import urllib.request
import wave
from PIL import Image
import PC_Util

def main():
    PC_Util.configure_auth()
    
    PART_SIZE = 60
    
    out_image = Image.new('RGB', (PART_SIZE * 5, PART_SIZE * 5))
    for row in range(5):
        for col in range(5):
            local_filename = urllib.request.urlretrieve('http://www.pythonchallenge.com/pc/hex/lake{id}.wav'.format(id=row * 5 + col + 1))[0]
            wave_read = wave.open(local_filename, 'rb')
            frames = wave_read.readframes(wave_read.getnframes())
            
            for i in range(PART_SIZE):
                for j in range(PART_SIZE):
                    index = (i * PART_SIZE + j) * 3
                    red, green, blue = frames[index:index + 3]
                    out_image.putpixel((col * PART_SIZE + j, row * PART_SIZE + i), (red, green, blue))
    
    out_image.show()
    out_image.close()

if __name__ == '__main__':
    main()
