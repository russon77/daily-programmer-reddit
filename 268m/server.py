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

    def broadcast(self, message, dont_send_to=None):
        for player in self.clients:
            if player is not dont_send_to:
                player.client_socket.send(bytes(message, "utf-8"))

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

                # logging -- when a connection happens
                print("New connection: " + str(len(self.clients)))
            except socket.timeout:
                continue

        # minor cleanup
        server_socket.close()

        # play the blackjack game:
        consecutive_passes = 0
        players_at_or_above_max = 0

        # send message to all players announcing start
        self.broadcast("The game is beginning.\n")

        # main game loop: infinite cycle through clients, until exit conditions are met
        for player in cycle(self.clients):
            # ask client for move
            player.client_socket.send(b"TAKE or PASS")

            # receive move: if TAKE, give player a card and update players min score
            data = player.client_socket.recv(128)
            data = data.decode("utf-8")

            # move will be broadcast to all players
            move = "Player " + str(player.uuid) + " has: "

            if data == "PASS":
                consecutive_passes += 1

                move += " opted to PASS.\n"
            elif data == "TAKE":
                card = Card.random()
                player.cards.append(card)
                player.client_socket.send(
                    bytes("Your card: " + str(card) + ".\n", "utf-8")
                )

                move += " TAKEN the card " + str(card) + "\n"

                # check if this player's min sum of card values is at or above 21
                if Card.min_value(player.cards) >= 21:
                    players_at_or_above_max += 1

                # reset consecutive passes
                consecutive_passes = 0
            else:
                # invalid request
                pass

            # send move broadcast
            self.broadcast(move, dont_send_to=player)

            # check for game over conditions
            if consecutive_passes == len(self.clients) or players_at_or_above_max == len(self.clients):
                break

        # decide winner and send to all clients
        # todo
        message = "It's over! "
        if consecutive_passes == len(self.clients):
            message = "Game is over because each player has passed consecutively.\n"

            # todo get winner

        elif players_at_or_above_max == len(self.clients):
            message = "Game is over because every player is either at or above 21 score.\n"

            # todo get winners

        # send final message
        for player in self.clients:
            player.client_socket.send(bytes(message, "utf-8"))

        # cleanup the server
        for player in self.clients:
            player.client_socket.close()

    def client_thread_wait_for_ready(self, client):
        client.client_socket.send(
            bytes("Welcome to Blackjack. Please send START when you are ready to play.\n", "utf-8"))
        while True:
            try:
                data = client.client_socket.recv(128)
                data = data.decode("utf-8")
                print(data)

                if data == "START":
                    del self.not_ready[client.uuid]

                    client.client_socket.send(
                        bytes("You have declared your readiness. We are still waiting on " +
                              str(len(self.not_ready)) + " other clients.\n", "utf-8")
                    )

                    return
            except BlockingIOError:
                continue

if __name__ == '__main__':
    server = Server(SERVER_PORT)
    server.run()
