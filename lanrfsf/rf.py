#coding: utf-8

import zlib
import base64
import sys
import os

def print_tips():
    print '''ERROR: config not specified
usage:  sf [FILE_NAME]                   
        rf [FILE_CODE/FILE_URL]
if you are useing OSX, the file_url will be copy to your clipboard
            '''

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