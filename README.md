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

# Future features

- [ ] error handling: code assumes every host is connected and responds correctly
- [ ] response length: code assumes a maximum of 64 bytes, but a dynamic header with message length should be provided.
- [ ] threaded servers: main server and mirror server run only one thread, but a high request period would take the system down.
- [ ] end of program: main server should end if received a "end of file" request or something similar.
- [X] configuration: most parameters (ip addresses, ports, messages) are fixed.