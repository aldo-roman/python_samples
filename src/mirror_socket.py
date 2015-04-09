from src.classes.socket import Socket

__author__ = 'Aldo Roman Nurena'


def __main__():
    server_socket()


def server_socket():
    host = 'localhost'
    port = 4321

    s = Socket()
    s.bind((host, port))
    s.listen(2)

    print "Listening to port ", port

    while True:
        conn, address = s.accept()
        print address, "Now connected"
        print conn.recv(64)
        conn.send("I'm mirror socket. I just read the request.")
        conn.close()


__main__()