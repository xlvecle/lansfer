#coding: utf-8

import zlib
import base64
import sys
import os
from utils import get_lan_ip, print_tips

def main():
    filename = ''
    if len(sys.argv)<2:
        print_tips()
        exit()
    filename = sys.argv[1]
    if filename.startswith('http'):
        os.system('curl -O '+filename)
    else:
        tmp = base64.b64decode(filename)
        url = zlib.decompress(tmp)
        print url
        os.system('curl -O '+url)
if __name__ == "__main__":
    main()