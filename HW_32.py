# task_1
#Make a class called Counter, and make it a subclass of the Thread class in the Threading module.
# Make the class have two global variables, one called counter set to 0, and another called rounds set to 100.000.
# Now implement the run() method, let it include a simple for-loop that iterates through rounds (e.i. 100.000 times)
# and for each time increments the value of the counter by 1. Create 2 instances of the thread and start them,
# then join them and check the result of the counter, it should be 200.000, right?
# Run it a couple of times and consider some different reasons why you get the answer that you get.

import threading

class Counter(threading.Thread):
    counter = 0
    rounds = 100000

    def run(self):
        for _ in range(self.rounds):
            Counter.counter += 1

counter1 = Counter()
counter2 = Counter()

counter1.start()
counter2.start()

counter1.join()
counter2.join()

print(f"The value is {Counter.counter}")

# task_2
#Create a socket echo server which handles each connection in a separate Thread

import socket
import threading

class ClientThread(threading.Thread):
    def __init__(self, client_address, client_socket):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        print("New connection added: ", client_address)

    def run(self):
        message = ''
        while True:
            data = self.client_socket.recv(1024)
            message = data.decode()
            if not data:
                break
            print("from client", message)
            self.client_socket.send(data)
        self.client_socket.close()

host = "127.0.0.1"
port = 3000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
print("Server started")

while True:
    server_socket.listen(1)
    client_sock, client_address = server_socket.accept()
    new_thread = ClientThread(client_address, client_sock)
    new_thread.start()
