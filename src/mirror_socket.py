from src.classes.sockets import Socket

__author__ = 'Aldo Roman Nurena'


def __main__():
    (host, port) = Socket.get_host_data('localhost', 4321, "mirror")
    server_socket(host, port)


def server_socket(host, port):
    """
    Instances a mirror socket that receives data
    send by client from the main server
    :param host: host to bind the socket
    :param port: port to listen to
    :return:
    """
    s = Socket.get_instance()
    s.bind((host, port))
    s.listen(2)

    print "Listening on %(host)s:%(port)s" % {"host":host, "port":port}

    while True:
        conn, address = s.accept()
        print address, "Now connected"
        content = conn.recv(64)
        print content

        if content.strip() == "EOF":
            conn.send("Good bye!")
            break
        else:
            conn.send("I'm mirror socket. I just read the request.")
        conn.close()


__main__()