#coding: utf-8
import os
import socket

desc = '''A simple tool for transfer file in LAN
If you are using OSX, the file_url will be copy on your clipboard'''


def print_tips():
    print '''ERROR: args not specified
usage:  sf [FILE_NAME]  #send file                 
        rf [FILE_CODE/FILE_URL]  #receive file
if you are useing OSX, the file_url will be copy to your clipboard
                '''

def check_port_in_use(port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = s.connect_ex(('127.0.0.1', port))

	if result == 0:
	    # print('socket is open')
	    return True
	s.close()
	return False

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