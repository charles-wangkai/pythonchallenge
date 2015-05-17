#!/usr/bin/env python3

# Q: http://www.pythonchallenge.com/pc/hex/ambiguity.html
# A: http://www.pythonchallenge.com/pc/hex/lake.html

import tempfile
import urllib.request
import zipfile
from PIL import Image

TOP, BOTTOM = (639, 0), (1, 640)
WHITE_COLOR = (255, 255, 255, 255)
OFFSETS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def configure_auth():
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, 'http://www.pythonchallenge.com', 'butter', 'fly')
    auth_handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    opener = urllib.request.build_opener(auth_handler)
    urllib.request.install_opener(opener)

def bfs(image):
    width, height = image.size
    
    queue = [TOP]
    prevs = {TOP: None}
    index = 0
    while queue[index] != BOTTOM:
        for (offset_x, offset_y) in OFFSETS:
            next_coord = (next_x, next_y) = queue[index][0] + offset_x, queue[index][1] + offset_y
            if next_x >= 0 and next_x < width and next_y >= 0 and next_y < height and next_coord not in prevs and image.getpixel(next_coord) != WHITE_COLOR:
                queue.append(next_coord)
                prevs[next_coord] = index
        index += 1
    
    path = []
    while index != None:
        path.append(queue[index])
        index = prevs[queue[index]]
    return list(reversed(path))

def main():
    configure_auth()
    local_filename = urllib.request.urlretrieve('http://www.pythonchallenge.com/pc/hex/maze.png')[0]
    image = Image.open(local_filename)
    
    path = bfs(image)
    
    out_file = tempfile.TemporaryFile()
    skip = False
    for coord in path:
        skip = not skip
        if skip:
            continue
        out_file.write(bytes([image.getpixel(coord)[0]]))
    
    zf = zipfile.ZipFile(out_file)
    
    image = Image.open(zf.open('maze.jpg'))
    image.show()

if __name__ == '__main__':
    main()
