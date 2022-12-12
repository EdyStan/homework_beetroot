# first of all import the socket library
import socket
from contextlib import contextmanager


@contextmanager
def socket_context(*args, **kw):
    s = socket.socket(*args, **kw)
    try:
        yield s
    finally:
        s.close()


with socket_context(socket.AF_INET, socket.SOCK_DGRAM) as s:
    print("Socket successfully created")

    # reserve a port on your computer in our
    # case it is 12345 but it can be anything
    port = 12345

    # Next bind to the port
    # we have not typed any ip in the ip field
    # instead we have inputted an empty string
    # this makes the server listen to requests
    # coming from other computers on the network
    s.bind(('', port))
    print("socket binded to %s" % port)

    # a forever loop until we interrupt it or
    # an error occurs
    while True:
        # Establish connection with client.
        c, addr = s.accept()
        print('Got connection from', addr)

        # send a thank you message to the client. encoding to send byte type.
        c.send('Thank you for connecting'.encode())

        # Breaking once connection closed
        break
