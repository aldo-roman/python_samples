from src.classes.sockets import Socket

__author__ = 'Aldo Roman Nurena'


def __main__():
    host = 'localhost'
    port = 4321

    server_socket(host, port)


def server_socket(host, port):
    s = Socket.get_instance()
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