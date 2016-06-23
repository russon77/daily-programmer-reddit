import random


def triplify_string(s):
    """
    split the given input string, and as a generator return each triple such that for a string containing
    "w1 w2 w3 w4 w5...", yield (w1, w2, w3), (w2, w3, w4), (w3, w4, w5)...
    NB: we start with None, None to help identify the target first word
    :param s:
    :return:
    """
    split = [None, None] + s.split()
    for i in range(0, len(split) - 2):
        yield split[i], split[i + 1], split[i + 2]


def random_list_member(l):
    return l[random.randint(0, len(l) - 1)]


def markov_generator(s, max_output_length=32):
    """
    for a given training string s, output a markov process generated string
    :param s: string containing training set
    :return: markov generated string
    """
    training = {}
    for triple in triplify_string(s):
        if (triple[0], triple[1]) not in training:
            training[triple[0], triple[1]] = [triple[2]]
        else:
            training[triple[0], triple[1]].append(triple[2])

    first = random_list_member(training[None, None])
    output = [first, random_list_member(training[None, first])]
    while len(output) < max_output_length and (output[-2], output[-1]) in training:
        output.append(random_list_member(training[output[-2], output[-1]]))

    return output


if __name__ == '__main__':
    x = """
    Now is not the time for desert, now is the time for dinner
    """

    print(markov_generator(x))
