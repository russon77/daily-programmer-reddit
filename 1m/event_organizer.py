

class Event(object):
    def __init__(self, time, desc, _id):
        self.time = time
        self.desc = desc
        self.id = _id


def main():
    events = [[] for _ in range(24)]
    events_dict = {}

    while True:
        print("1) Add\n2) Edit\n3) Delete\n4) View\n5) Quit")
        user_input = input(">> ")

        if user_input == "1":
            event_time = input("Hour: ")
            try:
                event_time = int(event_time)
            except ValueError:
                print("Unable to parse hour. Please try again.")
                continue

            event_desc = input("Description: ")

            new_event = Event(event_time, event_desc, abs(hash(event_desc)))

            events[event_time].append(new_event)
            events_dict[new_event.id] = new_event

            print("Successfully added event %d." % new_event.id)

        elif user_input == "2":
            event_id = input("Id: ")
            try:
                event_id = int(event_id)
            except ValueError:
                print("Unable to parse id. Please try again.")
                continue

            if event_id not in events_dict:
                print("Invalid event id. Please try again.")

            new_desc = input("Description: ")

            events_dict[event_id].desc = new_desc

            print("Successfully updated event.")

        elif user_input == "3":
            event_id = input("Id: ")
            try:
                event_id = int(event_id)
            except ValueError:
                print("Unable to parse id. Please try again.")
                continue

            if event_id not in events_dict:
                print("Invalid event id. Please try again.")

            del events_dict[event_id]

            for i in range(0, 24):
                for j in range(0, len(events[i])):
                    if event_id == events[i][j].id:
                        events[i].pop(j)

                        print("Successfully deleted event.")

        elif user_input == "4":
            for event_list in events:
                for event in event_list:
                    print("Id: %d\tHour: %s\tDescription: %s" % (event.id, event.time, event.desc))

        elif user_input == "5":
            print("Thanks for using the program. Have a nice day!")
            break

        else:
            print("Invalid input. Please try again.")


if __name__ == '__main__':
    main()