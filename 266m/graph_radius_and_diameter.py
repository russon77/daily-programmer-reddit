from collections import deque


class Tree(object):

    class TreeNode(object):
        def __init__(self, key, children=None):
            self.key = key

            if children is None:
                self.children = []
            else:
                self.children = children

        def is_leaf(self):
            return len(self.children) == 0

        def add_child(self, node):
            self.children.append(node)

    def __init__(self):
        self.root = None
        self.values = {}

    def insert(self, key, where):
        if key in self.values:
            return False

        if where is None and self.root is None:
            self.root = Tree.TreeNode(key)
            self.values[key] = True
            return True

        q = deque()
        q.append(self.root)

        while len(q):
            node = q.popleft()

            if node.key == where:
                node.add_child(Tree.TreeNode(key))
                self.values[key] = True
                return True

            for child in node.children:
                q.append(child)

        return False

    def height(self, node=None):
        if node is None:
            node = self.root

        # calculate heights of all children
        heights = []
        for child in node.children:
            heights.append(self.height(child))

        if len(node.children) == 0:
            return 1

        return 1 + max(heights)


class Graph(object):
    def __init__(self, nodes, adjacency_lists):
        self.nodes = nodes
        self.adjacency_lists = adjacency_lists

    def radius_diameter(self):
        # find all eccentricities
        eccentricities = []
        for node in self.nodes:
            t = self.minimum_spanning_tree(node)
            h = t.height() - 1

            # if the vertex has no adjacent neighbors, its height is 0 but its distance is technically infinite
            if h > 0:
                eccentricities.append(h)

        # return min
        return min(eccentricities), max(eccentricities)

    @staticmethod
    def from_file(filename):
        nodes = []
        adjacency_lists = {}

        with open(filename, "r") as handle:
            for line in handle.read().split("\n"):
                source, dest = line.split(" ")

                if source not in nodes:
                    nodes.append(source)
                    adjacency_lists[source] = []
                if dest not in nodes:
                    nodes.append(dest)
                    adjacency_lists[dest] = []

                adjacency_lists[source].append(dest)

        return Graph(nodes, adjacency_lists)

    def minimum_spanning_tree(self, start):
        tree = Tree()
        tree.insert(start, None)

        # each entry in the queue will be a (parent, target) pair
        q = deque()
        visited = {}

        for adj in self.adjacency_lists[start]:
            q.append((start, adj))

        while len(q):
            parent, target = q.popleft()
            visited[target] = True

            tree.insert(target, parent)

            for adj in self.adjacency_lists[target]:
                if adj in visited:
                    continue

                q.append((target, adj))

        return tree


if __name__ == '__main__':
    g = Graph.from_file("test.txt")
    print(g.radius_diameter())

    print(Graph.from_file("test2.txt").radius_diameter())

    print()

