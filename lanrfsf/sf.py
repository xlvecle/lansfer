#coding: utf-8

import zlib
import base64
import socket
import fcntl
import struct
import sys
import os
import socket
import SocketServer
import SimpleHTTPServer
import thread
import time
from utils import get_lan_ip

global httpd
global filename
global is_shutdown

httpd = None
filename = ''
is_shutdown = False

class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        global httpd
        global is_shutdown
        """Serve a GET request."""
        f = self.send_head()
        import sf
        print "Waiting to receive " + self.path + "..."
        if self.path == "/"+filename:
            def kill_me_please(server):
                server.shutdown()
            thread.start_new_thread(kill_me_please, (httpd,))
            is_shutdown = True
            print "success"
        if f:
            try:
                self.copyfile(f, self.wfile)
            finally:
                f.close()

class MyTCPServer(SocketServer.TCPServer):
    def server_bind(self):
        import socket
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)

def args_handler():
    pass

def print_tips():
    print '''ERROR: args not specified
usage:  sf [FILE_NAME]  #send file                 
        rf [FILE_CODE/FILE_URL]  #receive file
if you are useing OSX, the file_url will be copy to your clipboard
                '''

def main():
    global httpd
    global filename
    global is_shutdown
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

    Handler = MyHandler
    httpd = MyTCPServer(("", PORT), Handler)
    print "serving at port", PORT
    thread.start_new_thread(httpd.serve_forever, ())

    try:
        for x in xrange(1,10):
            if is_shutdown:
                exit()
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        print "exit"
        exit()
    
if __name__ == "__main__":
	main()