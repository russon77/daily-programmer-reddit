from itertools import cycle


class BusDriver(object):
    def __init__(self, route):
        self.route = route
        self.gossip = {self: True}

        self.location = cycle(route)

    def next_location(self):
        return next(self.location)


def exchange_gossip(drivers):
    gossip = {}
    for driver in drivers:
        gossip = {**gossip, **driver.gossip}

    for driver in drivers:
        driver.gossip = gossip


def all_gossip_exchanged(drivers):
    for driver in drivers:
        if len(driver.gossip) != len(drivers):
            return False

    return True


def gossiping_drivers(routes):
    bus_drivers = []
    for route in routes:
        bus_drivers.append(BusDriver(route))

    for time in range(0, 480):
        if all_gossip_exchanged(bus_drivers):
            break

        meetups = {}
        for driver in bus_drivers:
            loc = driver.next_location()
            if loc not in meetups:
                meetups[loc] = [driver]
            else:
                meetups[loc].append(driver)

        for key in meetups:
            if len(meetups[key]) >= 2:
                exchange_gossip(meetups[key])

    if time >= 479:
        return "never"
    else:
        return time


def string_to_routes(s):
    ret = []
    for line in s.split("\n"):
        ret.append([int(_) for _ in line.split(" ")])

    return ret

if __name__ == '__main__':
    r = [
        [2, 1, 2],
        [5, 2, 8]
    ]

    print(gossiping_drivers(r))

    r = [
        [2, 1],
        [1, 2, 2]
    ]

    print(gossiping_drivers(r))

    with open("test.txt", "r") as handle:
        print(gossiping_drivers(string_to_routes(handle.read())))

    with open("test2.txt", "r") as handle:
        print(gossiping_drivers(string_to_routes(handle.read())))

