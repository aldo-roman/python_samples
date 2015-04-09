import socket
import sys

__author__ = 'Aldo Roman Nurena'


class Socket:

    @staticmethod
    def get_instance():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            return s
        except socket.error:
            print 'Failed to create socket'
            sys.exit()
        print 'Socket Created'
