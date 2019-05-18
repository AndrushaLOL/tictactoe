import socket
import threading


def start_server():
    server_address = ('0.0.0.0', 8888)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_address)
    server_socket.listen(10)
    print('server running on port 8888')

    while True:
        try:
            connection, address = server_socket.accept()

            data = connection.recv(1024)
            print(str(data))

            connection.send(bytes('Hello from server', encoding='UTF-8'))

            connection.close()
        except KeyboardInterrupt:
            print('server stopping...')
            break


class ServerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.start_server = start_server

    def run(self):
        self.start_server()
