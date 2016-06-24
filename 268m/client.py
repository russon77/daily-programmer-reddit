import socket
from threading import Thread

from config import SERVER_PORT


def listen_thread(sock):
    while True:
        data = sock.recv(128)
        print(data.decode("utf-8"))


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), SERVER_PORT))

    listen = Thread(target=listen_thread, args=(s,))
    listen.run()

    while True:
        i = input()
        if i in ("TAKE", "PASS", "START"):
            s.send(bytes(i))
