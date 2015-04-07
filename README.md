# python_samples

Simple project with samples written in Python.

# Current features

Server: receives connections on port 1234 and resend the content to a mirror server
Mirror server: receives connections on port 4321
Client: sends connections request to port 1234

# Running

Run both servers first to enable the listening on ports.
Client server simply makes a request and receives a response. Therefore, should be run after servers are listening.

In different processes (terminal tabs, for example), run:

```$ python server_socket.py```

```$ python mirror_socket.py```

```$ python client_socket.py```