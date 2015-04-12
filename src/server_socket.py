from sys import stdin
from src.classes.sockets import Socket

__author__ = 'Aldo Roman Nurena'


def __main__():
    (host, port) = Socket.get_host_data('localhost', 1234)
    server_socket(host, port)


def server_socket(host, port):
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
        m.connect(('localhost',4321))

        # m.send(len(content))     # send content length
        # m.recv(1)               # receive OK or ERROR
        m.sendall(content)      # send actual data

        print m.recv(64)
        m.close()

        # response to client
        print content
        conn.send("I'm server socket. Thank you for connecting.\n")
        conn.close()
        print ""


__main__()