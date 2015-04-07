import socket

__author__ = 'Aldo Roman Nurena'


def __main__():
    server_socket()


def server_socket():
    host = 'localhost'
    port = 1234

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(2)

    print "Listening to port ", port

    while True:
        # accept connections from client
        conn, address = s.accept()
        print address, "Now connected"
        content = conn.recv(64)

        # connect to mirror socket
        m = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        m.connect(('localhost',4321))
        m.send(content)
        print m.recv(64)
        m.close()

        # response to client
        print content
        conn.send("I'm server socket. Thank you for connecting.\n")
        conn.close()
        print ""


__main__()