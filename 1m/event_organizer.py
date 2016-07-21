

class Event(object):
    def __init__(self, time, desc):
        self.time = time
        self.desc = desc


def main():
    events = {}

    while True:
        print("1) Add\n2) Edit\n3) Delete\n4) View\n5) Quit")
        user_input = input(">> ")

        if user_input == "1":
            event_time = input("Time: ")
            event_desc = input("Description: ")

            new_event = Event(event_time, event_desc)
            events[str(hash(abs(new_event)))] = new_event

            print("Successfully added event.")

        elif user_input == "2":
            event_id = input("Id: ")
            if event_id not in events:
                print("Invalid event id. Please try again.")

            new_time = input("Time: ")
            new_desc = input("Description: ")

            new_event = Event(new_time, new_desc)
            events[event_id] = new_event

            print("Successfully updated event.")

        elif user_input == "3":
            event_id = input("Id: ")
            if event_id not in events:
                print("Invalid event id. Please try again.")

            del events[event_id]
            print("Successfully deleted event.")

        elif user_input == "4":
            for event_id in events:
                print("Event Id: %s\tEvent time: %s\tDescription: %s" %
                      (event_id, events[event_id].time, events[event_id].desc))

        elif user_input == "5":
            print("Thanks for using the program. Have a nice day!")
            break

        else:
            print("Invalid input. Please try again.")


if __name__ == '__main__':
    main()