import socket
import sys

__author__ = 'Aldo Roman Nurena'


class Socket:


    @staticmethod
    def get_instance():
        """
        Static factory that returns a socket instance.
        Will throw an error if instantiation was not correct
        :return: Socket
        """
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            return s
        except socket.error:
            print 'Failed to create socket'
            sys.exit()
        print 'Socket Created'

    @staticmethod
    def get_host_data(host, port):
        """
        Reads host and port from std input.
        Set a default host and port if no data provided.
        :param host: default host ip
        :param port: default port
        :return: tuple of host and port
        """
        sys.stdout.write("Enter host ip [localhost]:")
        line = sys.stdin.readline()

        if line.strip(): # not empty string
            host = line

        sys.stdout.write("Enter host port [1234]:")
        line = sys.stdin.readline()

        if line.strip(): # not empty string
            port = line

        return host, port