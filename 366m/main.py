"""
https://www.reddit.com/r/dailyprogrammer/comments/99d24u/20180822_challenge_366_intermediate_word_funnel_2/

Builds a tree containing all word funnels, then finds the longest path.
"""

import unittest


class Node(object):
    def __init__(self, word):
        self.word = word
        self.children = []

    def add_child(self, node):
        self.children.append(node)


class WordFunneler(object):
    def __init__(self, dictionary):
        self.words = set()

        with open(dictionary, 'r') as f:
            for line in f:
                word = line.replace('\n', '')
                self.words.add(word)

    def build_tree(self, word):
        root = Node(word)

        for i in range(len(word)):
            # create the new word by removing a single letter
            new_word = word[0:i] + word[i+1:]

            # only continue if the new word is valid
            if new_word in self.words:
                # build the node for the new word
                node = self.build_tree(new_word)

                # add the new node as a child of the current root node
                root.add_child(node)

        return root

    def longest_path(self, node):
        if len(node.children) == 0:
            return 1

        longest = max( self.longest_path(c) for c in node.children )

        return 1 + longest

    def funnel(self, word):
        # build the tree containing all the paths
        tree = self.build_tree(word)

        # find the longest path
        result = self.longest_path(tree)

        return result

class Tests(unittest.TestCase):
    def setUp(self):
        self.funneler = WordFunneler("./enable1.txt")

    def test_funneler(self):
        self.assertEqual(self.funneler.funnel("gnash"), 4)
        self.assertEqual(self.funneler.funnel("princesses"), 9)
        self.assertEqual(self.funneler.funnel("turntables"), 5)
        self.assertEqual(self.funneler.funnel("implosive"), 1)
        self.assertEqual(self.funneler.funnel("programmer"), 2)

