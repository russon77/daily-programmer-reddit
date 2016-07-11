import unittest


class MyUnitTest(unittest.TestCase):
    def test_splurthian(self):
        tests = [
            ("Spenglerium", "Ee", True),
            ("Zeddemorium", "Zr", True),
            ("Venkmine", "Kn", True),
            ("Stantzon", "Zt", False),
            ("Melintzum", "Nn", False),
            ("Tullium", "Ty", False)
        ]

        for t in tests:
            self.assertEqual(valid_splurthian(t[0], t[1]), t[2])


def valid_splurthian(element, short):
    # rule 1: length of symbol must be two letters
    if len(short) != 2:
        return False

    element = element.lower()
    short = short.lower()

    # rule 2: both letters in short must appear in element name
    if not all([_ in element for _ in short]):
        return False

    # rule 3: if the short is two of the same letters, it must appear twice. otherwise, check rule 4
    if short[0] == short[1]:
        if element.count(short[0]) < 2:
            return False
    # rule 4: one instance of first letter in short must appear in element before second letter -- or reversed!
    else:
        if short[1] not in element[element.index(short[0]):]:
            return False

    return True

if __name__ == '__main__':
    unittest.main()
