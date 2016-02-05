#coding: utf-8

import zlib
import base64
import sys
import os
from utils import get_lan_ip, print_tips, args_handler

def main():
    args = args_handler('rf')
    filename = ''
    if args.filename:
        filename = args.filename
    if filename.startswith('http'):
        os.system('curl -O '+filename)
    else:
        tmp = base64.b64decode(filename)
        url = "http://" + zlib.decompress(tmp)
        print url
        os.system('curl -O '+ url)
if __name__ == "__main__":
    main()