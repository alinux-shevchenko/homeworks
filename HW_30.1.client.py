# task_1
# create a server and client, which will use user datagram protocol (UDP) for communication.

import socket

HOST = "127.0.0.1"
PORT = 3000
message = b'Hello, world'

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    print('Sending {!r}'.format(message))
    s.sendto(message, (HOST, PORT))

    print('Waiting to receive')
    data, addr = s.recvfrom(1024)

print('Received', repr(data))


