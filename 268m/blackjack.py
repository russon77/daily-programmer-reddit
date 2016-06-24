from random import randint


class Card(object):
    SUITS = [
        "SPADES",
        "HEARTS",
        "CLUBS",
        "DIAMONDS"
    ]

    CARDS = [
        "TWO",
        "THREE",
        "FOUR",
        "FIVE",
        "SIX",
        "SEVEN",
        "EIGHT",
        "NINE",
        "TEN",
        "JACK",
        "QUEEN",
        "KING",
        "ACE"
    ]

    VALUES = {
        "TWO": 2,
        "THREE": 3,
        "FOUR": 4,
        "FIVE": 5,
        "SIX": 6,
        "SEVEN": 7,
        "EIGHT": 8,
        "NINE": 9,
        "TEN": 10,
        "JACK": 10,
        "QUEEN": 10,
        "KING": 10,
        "ACE": 1
    }

    def __init__(self, suit=None, value=None, from_string=None):
        if from_string is not None:
            pass
        else:
            self.suit = suit
            self.value = value

    def __str__(self):
        return self.value + "," + self.suit

    @staticmethod
    def min_value(*cards):
        # todo implement me
        pass

    @staticmethod
    def random():
        return Card(Card.SUITS[randint(0, 3)], Card.CARDS[randint(0, 12)])