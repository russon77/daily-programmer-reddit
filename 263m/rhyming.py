from collections import deque, OrderedDict


class Trie(object):
    class TrieNode(object):
        def __init__(self, key, storage=None, children=None, is_root=False):
            self.key = key
            self.storage = []
            if storage is not None:
                self.storage.append(storage)

            self.is_root = is_root

            if children is None:
                children = []
            self.children = children

        def get_all_storages(self):
            storages = []

            q = deque()
            q.append(self)
            while len(q):
                node = q.pop()

                storages.extend(node.storage)

                q.extend(node.children)

            return storages

        def __str__(self):
            if self.storage:
                s = "["
                for item in self.storage:
                    s += item + " "
                s += "]"
            else:
                s = "No storage"

            return s + ", key: " + self.key

    def __init__(self):
        self.root = Trie.TrieNode(None, None, is_root=True)

    def insert(self, key, storage, node=None):
        if node is None:
            node = self.root

        if len(key) == 0:
            node.storage.append(storage)
            return True

        key_part = key.pop(-1)

        for child in node.children:
            if key_part == child.key:
                return self.insert(key, storage, child)

        # key was not found among children -- create a new child for this node
        if len(key) == 0:
            node.children.append(Trie.TrieNode(key_part, storage))
            return True

        new_child = Trie.TrieNode(key_part)
        node.children.append(new_child)
        return self.insert(key, storage, new_child)

    def find(self, key, node=None):
        if node is None:
            node = self.root

        if len(key) == 0:
            return node
        elif len(key) == 1 and key[0] == node.key:
            return node

        key_part = key.pop(-1)
        for child in node.children:
            if child.key == key_part:
                return self.find(key, child)

        return False


class Rhyming(object):

    def __init__(self, filename="cmudict-0.7b"):
        self.word_to_phonetics = {}
        self.phonetics_trie = Trie()
        self.phonetics_to_word = {}

        with open(filename, "r", encoding="iso-8859-1") as handle:
            for line in handle:
                if line.startswith(";;;"):
                    continue

                initial_split = line.replace("\n", "").split("  ")
                word, phonetics = initial_split[0], initial_split[1].split(" ")

                self.word_to_phonetics[word] = phonetics
                self.phonetics_to_word[tuple(phonetics)] = word

                self.phonetics_trie.insert(list(phonetics), word)

    def rhyme(self, word):
        word = word.upper()
        phonetics = list(self.word_to_phonetics[word])

        found = []
        while len(phonetics) > 1:
            tmp = self.phonetics_trie.find(list(phonetics))
            if tmp:
                found.append(tmp)
            phonetics.pop(0)

        # for each Node in found, add all words to a set
        x = OrderedDict()
        for node in found:
            for s in node.get_all_storages():
                x[s] = None

        return list(x.keys())


if __name__ == '__main__':
    r = Rhyming()
    print(r.rhyme("solution"))


