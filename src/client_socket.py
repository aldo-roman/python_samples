from sys import stdin
from src.classes.sockets import Socket

__author__ = 'Aldo Roman Nurena'


def __main__():
    client_socket()


def client_socket():
    s = Socket.get_instance()
    s.connect(('localhost',1234))
    print "Connected to server."
    print "Write some text: (line by line)"

    while True:
        line = stdin.readline()
        # s.send(line.length)
        s.send(line)
        response = s.recv(64)
        print(response)
        s.close()

__main__()