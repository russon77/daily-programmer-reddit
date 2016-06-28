from json import loads
import socket


def irc_listener(server, port, nickname, username, realname):
    """
    connect to an IRC server, set credentials, then listen / output all messages from server
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, port))

    s.send(bytes("NICK " + nickname + "\r\n", encoding="utf-8"))
    s.send(bytes("USER " + username + " 0 * :" + realname + "\r\n", encoding="utf-8"))

    while True:
        messages = s.recv(2048).decode("utf-8").split("\r\n")

        for msg in messages:
            if msg.startswith("PING "):
                ser = msg.split(" ")[1]
                s.send(bytes("PONG " + ser, "utf-8"))

            print(msg)

if __name__ == '__main__':
    with open("config.json") as handle:
        config = loads(handle.read())

    servername, port_no = config["server"].split(":")
    irc_listener(servername, int(port_no), config["nickname"], config["username"], config["real_name"])



