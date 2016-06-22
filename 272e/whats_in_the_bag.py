

def whats_in_my_bag(s):
    # construct the base table with every letter => "full"
    letters_to_frequency = {
        'a': 9,
        'b': 2,
        'c': 2,
        'd': 4,
        'e': 12,
        'f': 2,
        'g': 3,
        'h': 2,
        'i': 9,
        'j': 1,
        'k': 1,
        'l': 4,
        'm': 2,
        'n': 6,
        'o': 8,
        'p': 2,
        'q': 1,
        'r': 6,
        's': 4,
        't': 6,
        'u': 4,
        'v': 2,
        'x': 1,
        'y': 2,
        'z': 1,
        '_': 2
    }

    # set input to all lowercase
    s = s.lower()

    for c in s:
        letters_to_frequency[c] -= 1
        if letters_to_frequency[c] < 0:
            print("Invalid input. More " + c + " have been taken than possible.")
            return

    ret = [list() for _ in range(0, 13)]
    for c in letters_to_frequency:
        ret[letters_to_frequency[c]].append(c)

    for l in ret:
        l.sort()

    for i in range(0, 13):
        print(str(i) + ": ")
        print(ret[i])

    return ret

if __name__ == '__main__':
    whats_in_my_bag("AEERTYOXMCNB_S")
    whats_in_my_bag("AXHDRUIOR_XHJZUQEE")
