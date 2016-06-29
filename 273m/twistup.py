from random import randrange
from re import match


def insert_or_append(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = [value]
    else:
        dictionary[key].append(value)


class Twister(object):
    def __init__(self, data_source="data.txt"):
        self.latin_to_gibberish = {}
        with open(data_source) as handle:
            for line in handle:
                if match("\|\[\[..\|..\s..\]\]\|\|\w\s.*", line):
                    upper, lower, latin = line[6], line[9], line[15]
                    if latin == upper:
                        continue
                    insert_or_append(self.latin_to_gibberish, latin, upper)
                    insert_or_append(self.latin_to_gibberish, latin.lower(), lower)

    def twist_up_letter(self, letter):
        if letter in self.latin_to_gibberish:
            index = randrange(0, len(self.latin_to_gibberish[letter]))
            return self.latin_to_gibberish[letter][index]

        return letter

    def twist_up(self, word):
        ret = ""
        for letter in word:
            ret += self.twist_up_letter(letter)

        return ret


if __name__ == '__main__':
    tw = Twister()
    print(tw.twist_up("Hello, world"))
    print(tw.twist_up("""
    For, after all, how do we know that two and two make four?
Or that the force of gravity works? Or that the past is unchangeable?
If both the past and the external world exist only in the mind,
and if the mind itself is controllable – what then?
"""))
