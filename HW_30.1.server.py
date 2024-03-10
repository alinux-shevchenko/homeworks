# task_1
# create a server and client, which will use user datagram protocol (UDP) for communication.

import socket

HOST = "127.0.0.1"
PORT = 3000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))

    while True:
        print('Waiting to receive message')
        data, address = s.recvfrom(4096)

        print('Received {} bytes from {}'.format(len(data), address))
        print(data)

        if data:
            sent = s.sendto(data, address)
            print('Sent {} bytes back to {}'.format(sent, address))