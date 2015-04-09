import socket

__author__ = 'Aldo Roman Nurena'


def __main__():
    client_socket()


def client_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost',1234))

    s.send("I'm client socket!")
    response = s.recv(64)
    print(response)
    s.close()

__main__()