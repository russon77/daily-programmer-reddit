import socket
from itertools import cycle
from threading import Thread

from config import SERVER_PORT
from blackjack import Card


class Client(object):
    def __init__(self, client_socket, address):
        self.client_socket = client_socket
        self.address = address
        self.uuid = hash(hash(client_socket) + hash(address))

        self.cards = []


class Server(object):
    def __init__(self, port):
        self.port = port
        self.clients = []
        self.not_ready = {}

    def run(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((socket.gethostname(), SERVER_PORT))
        server_socket.listen()

        server_socket.settimeout(1.5)

        while len(self.clients) == 0 or len(self.not_ready) > 0:
            try:
                client = Client(*server_socket.accept())

                self.not_ready[client.uuid] = True
                self.clients.append(client)

                client_thread = Thread(target=self.client_thread_wait_for_ready, args=(client,), daemon=True)
                client_thread.start()
            except socket.timeout:
                continue

        # play the blackjack game:
        consecutive_passes = 0
        players_at_or_above_max = 0
        for player in cycle(self.clients):
            # ask client for move
            player.client_socket.send(b"TAKE or PASS")

            # receive move: if TAKE, give player a card and update players min score
            data = player.client_socket.recv(128)
            data = data.decode("utf-8")

            if data == "PASS":
                consecutive_passes += 1
            elif data == "TAKE":
                card = Card.random()
                player.cards.append(card)
                player.client_socket.send(b"Your card: " + card)

                # check if this player's min sum of card values is at or above 21
                if Card.min_value(player.cards) >= 21:
                    players_at_or_above_max += 1

                # reset consecutive passes
                consecutive_passes = 0
            else:
                # invalid request
                pass

            # check for game over conditions
            if consecutive_passes == len(self.clients) or players_at_or_above_max == len(self.clients):
                break

        # decide winner and send to all clients
        # todo
        # for player in self.clients:
        #     player.client_socket.send(b"Game over!")

    def client_thread_wait_for_ready(self, client):
        # todo respond to socket closing, errors
        while True:
            try:
                data = client.client_socket.recv(128)
                data = data.decode("utf-8")
                print(data)

                if data == "START":
                    del self.not_ready[client.uuid]

                    return
            except BlockingIOError:
                continue

if __name__ == '__main__':
    server = Server(SERVER_PORT)
    server.run()
