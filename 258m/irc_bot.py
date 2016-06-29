from json import loads
from random import randint
import datetime
import socket


def formatted_time():
    return "{:%H:%M:%S}".format(datetime.datetime.now())


def send_message(sock, msg):
    print(">" + formatted_time() + " > " + msg)
    sock.sendall(bytes(msg + "\r\n", encoding="utf-8"))


def incoming_messages(sock):
    buffer = ""

    while True:
        delta_buffer = sock.recv(1024).decode("utf-8")
        if delta_buffer == "":
            raise StopIteration

        buffer += delta_buffer

        if "\r\n" in buffer:
            messages, buffer = buffer.rsplit("\r\n", maxsplit=1)
            messages = messages.split("\r\n")
            for message in messages:
                print("<" + formatted_time() + " < " + message)
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
                if " JOIN " in message:
                    chan = message.split(" ")[-1]
                    send_message(s, "PRIVMSG " + chan + " :" + join_msg)
            else:
                # get the message `contents`
                if ":" in message[1:]:
                    contents = message[message.index(":", 1):]
                    if contents.startswith(":@" + nickname + ": random "):
                        splits = contents.split(" ")
                        chan = ""
                        for st in message.split(" "):
                            if st.startswith("#"):
                                chan = st
                                break

                        a, b = int(splits[-2]), int(splits[-1])
                        send_message(s, "PRIVMSG " + chan + " : Your very random number... " + str(randint(a, b)))
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



