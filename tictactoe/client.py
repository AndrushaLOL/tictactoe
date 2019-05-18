import socket


def connect(address=('0.0.0.0', 8888)):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(address)
    client.send(bytes('Hello from client!', encoding='UTF-8'))

