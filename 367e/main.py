"""
https://www.reddit.com/r/dailyprogrammer/comments/9cvo0f/20180904_challenge_367_easy_subfactorials_another/
"""

import unittest
from itertools import permutations


def valid(l):
    """
    a given list is invalid if any element is equal to its 1-index
    """

    if len(l) == 0:
        return False

    for i, n in enumerate(l, 1):
        if n == i:
            return False

    return True

def subfactorial(n):
    """
    The subfactorial, defined as the derangement of a set of n objects, or a permutation of the elements of a set, such that no element appears in its original position. We denote it as !n.
    """
    p = permutations(range(1, n + 1))
    r = 0

    for l in p:
        if valid(l):
            r += 1

    return r


class Tests(unittest.TestCase):
    def test_main(self):
        self.assertEqual(subfactorial(1), 0)
        self.assertEqual(subfactorial(2), 1)
        self.assertEqual(subfactorial(3), 2)
        self.assertEqual(subfactorial(5), 44)
        self.assertEqual(subfactorial(6), 265)
        self.assertEqual(subfactorial(9), 133496)
#        self.assertEqual(subfactorial(14), 32071101049)

    def test_valid(self):
        self.assertFalse(valid([1]))

        self.assertTrue(valid([2, 3, 1]))
        self.assertTrue(valid([3, 1, 2]))

        self.assertFalse(valid([1, 2, 3]))
        self.assertFalse(valid([3, 2, 1]))
        self.assertFalse(valid([1, 3, 2]))
        self.assertFalse(valid([2, 1, 3]))

if __name__ == '__main__':
    unittest.main()

