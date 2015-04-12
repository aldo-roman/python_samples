from sys import stdin
from src.classes.sockets import Socket

__author__ = 'Aldo Roman Nurena'


def __main__():
    client_socket()


def client_socket():
    """
    Receive text from user and sends to main server.
    :return:
    """

    print "Write some text: (line by line)"

    while True:
        s = Socket.get_instance()
        s.connect(('localhost',1234))

        line = stdin.readline()
        # s.send(line.length)
        s.send(line)
        response = s.recv(64)
        print(response)
        s.close()

__main__()