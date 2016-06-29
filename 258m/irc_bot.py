from json import loads
import socket


def send_message(sock, msg):
    print(">" + msg)
    sock.send(bytes(msg + "\r\n", encoding="utf-8"))


def incoming_messages(sock):
    buffer = ""

    while True:
        buffer += sock.recv(1024).decode("utf-8")

        if "\r\n" in buffer:
            messages, buffer = buffer.split("\r\n", maxsplit=1)
            messages = messages.split("\r\n")
            for message in messages:
                print("<" + message)
                yield message


def irc_bot(server, port, nickname, username, realname, initial_servers, join_msg):
    """
    connect to an IRC server, set credentials, then listen / output all messages from server
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, port))

    # send credentials
    send_message(s, "NICK " + nickname)
    send_message(s, "USER " + username + " 0 * :" + realname)

    motd_over = False
    for message in incoming_messages(s):
        # handle message
        # check for ping/pong timeout
        if message.startswith("PING"):
            # parse and respond with appropriate PONG message
            ser = message.split(" ")[1]
            send_message(s, "PONG " + ser)
            continue

        if not motd_over:
            # check if this is the "end of MOTD message"
            if " 376 " in message:
                motd_over = True

                # join the configured servers
                send_message(s, "JOIN " + initial_servers)
        else:
            # otherwise, check for a direct message
            if message.startswith(":" + nickname):
                pass

    s.close()

if __name__ == '__main__':
    with open("config.json") as handle:
        config = loads(handle.read())

    servername, port_no = config["server"].split(":")
    irc_bot(servername,
            int(port_no),
            config["nickname"],
            config["username"],
            config["real_name"],
            config["channels_to_join"],
            config["join_message"])



