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
is_shutdown = False

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
    import threading
    assassin = threading.Thread(target=httpd.shutdown)
    assassin.daemon = True
    assassin.start()

def main():
    if len(sys.argv)<2:
        print_tips()
        exit()
    PORT = 8001
    filename = ''
    filename = sys.argv[1]
    ip = get_lan_ip()

    address = "http://" + ip + ":" + str(PORT) + "/" + filename
    print address
    z = zlib.compress(address)
    result = base64.b64encode(z)
    print result
    cmd = 'echo "%s" | pbcopy ' % result
    if sys.platform == 'darwin':
        os.system(cmd)

    Handler = SimpleHTTPServerModified.SimpleHTTPRequestHandler

    httpd = SocketServer.TCPServer(("", PORT), Handler)
    SimpleHTTPServerModified.running_httpd=httpd
    SimpleHTTPServerModified.file_name=filename
    print "serving at port", PORT

    import threading
    assassin = threading.Thread(target=httpd.serve_forever)
    assassin.daemon = True
    assassin.start()
    SimpleHTTPServerModified.http_thread = assassin
    import time
    try:
        for x in xrange(1,10):
            if is_shutdown:
                close_server(httpd)
                exit()
            time.sleep(1)
        close_server(httpd)
    except (KeyboardInterrupt, SystemExit):
        print "exit"
        exit()
    
if __name__ == "__main__":
	main()