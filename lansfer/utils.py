# coding: utf-8
import socket
import argparse

desc = '''A simple tool for transfer file in LAN
If you are using OSX, the file_url will be copy on your clipboard'''


def print_tips():
    print '''ERROR: args not specified,
usage:  sf [FILE_NAME]  #send file
        rf [FILE_CODE/FILE_URL]  #receive file
if you are useing OSX, the file_url will be copy to your clipboard
                '''


def args_handler(script_type):
    parser = argparse.ArgumentParser(
        description=desc, formatter_class=argparse.RawTextHelpFormatter)
    if script_type == 'rf':
        parser.add_argument("filename", help="file_name or file_code",
                            type=str)
        return parser.parse_args()
    parser.add_argument("filename", help="filename",
                        type=str)
    parser.add_argument("-p", "--port", help="Http Port", type=int)
    parser.add_argument("-e", "--eth", help="Ethernet Networking Interface")
    parser.add_argument(
        "-a", "--alive", help="Disable auto stop",
        action="store_true", default=False)
    args = parser.parse_args()
    return args


def check_port_in_use(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex(('127.0.0.1', port))

    if result == 0:
        # print('socket is open')
        return True
    s.close()
    return False


def get_lan_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("gmail.com", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip
