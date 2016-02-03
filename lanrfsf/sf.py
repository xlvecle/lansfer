#coding: utf-8

import zlib
import base64
import socket
import fcntl
import struct
import sys
import os
import socket
import SimpleHTTPServerModified
import SocketServer

httpd = None

if os.name != "nt":
    import fcntl
    import struct

    def get_interface_ip(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s',
                                ifname[:15]))[20:24])

def get_lan_ip():
    ip = socket.gethostbyname(socket.gethostname())
    if ip.startswith("127.") and os.name != "nt":
        interfaces = [
            "eth0",
            "eth1",
            "eth2",
            "wlan0",
            "wlan1",
            "wifi0",
            "ath0",
            "ath1",
            "ppp0",
            ]
        for ifname in interfaces:
            try:
                ip = get_interface_ip(ifname)
                break
            except IOError:
                pass
    return ip


def print_tips():
    print '''ERROR: args not specified
usage:  sf [FILE_NAME]  #send file                 
        rf [FILE_CODE/FILE_URL]  #receive file
if you are useing OSX, the file_url will be copy to your clipboard
                '''

def close_server(httpd):
    for i in xrange(1,20):
        import time
        time.sleep(1)
    httpd.shutdown()

def main():
    if len(sys.argv)<2:
        print_tips()
        exit()
    port = '8001'
    filename = ''
    filename = sys.argv[1]
    ip = get_lan_ip()

    address = "http://" + ip + ":" + port + "/" + filename
    print address
    z = zlib.compress(address)
    result = base64.b64encode(z)
    print result
    cmd = 'echo "%s" | pbcopy ' % result
    if sys.platform == 'darwin':
        os.system(cmd)

    PORT = 8001

    Handler = SimpleHTTPServerModified.SimpleHTTPRequestHandler

    httpd = SocketServer.TCPServer(("", PORT), Handler)
    SimpleHTTPServerModified.running_httpd=httpd
    SimpleHTTPServerModified.file_name=filename
    print "serving at port", PORT

    import threading
    assassin = threading.Thread(target=httpd.serve_forever)
    assassin2 = threading.Thread(target=close_server, args=(httpd,))

    # assassin.daemon = True
    assassin.start()
    assassin2.start()
    SimpleHTTPServerModified.max_live_thread=assassin2
    
if __name__ == "__main__":
	main()