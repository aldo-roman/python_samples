import socket
import sys

__author__ = 'Aldo Roman Nurena'


class Socket:
    """ A simple class for managing sockets"""

    def __init__(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            print 'Failed to create socket'
            sys.exit()
        print 'Socket Created'