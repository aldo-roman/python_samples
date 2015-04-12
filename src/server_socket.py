from sys import stdin
from src.classes.sockets import Socket

__author__ = 'Aldo Roman Nurena'


def __main__():
    (host, port) = Socket.get_host_data('localhost', 1234)
    (host_m, port_m) = Socket.get_host_data('localhost', 4321, "mirror")
    server_socket((host, port), (host_m,port_m))


def server_socket((host, port), (host_m,port_m)):
    """
    Instances the main server.
    Receives data from client, forward the data to
    a mirror server and replies the client.
    :param host: host to bind socket
    :param port: port to listen to
    :return:
    """
    s = Socket.get_instance()
    s.bind((host, port))
    s.listen(2)

    print "Listening on %(host)s:%(port)s" % {"host":host, "port":port}

    while True:
        # accept connections from client
        conn, address = s.accept()
        print address, "Now connected"
        content = conn.recv(64)

        # connect to mirror socket
        m = Socket.get_instance()
        m.connect((host_m,port_m))

        # m.send(len(content))     # send content length
        # m.recv(1)               # receive OK or ERROR
        m.sendall(content)      # send actual data

        print m.recv(64)
        m.close()

        if content.strip() == "EOF":
            print "EOF"
            conn.send("Good bye!")
            conn.close()
            break

        # response to client
        print content
        conn.send("I'm server socket. Thank you for connecting.\n")
        conn.close()
        print ""


__main__()