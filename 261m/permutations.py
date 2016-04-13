

def permutations(lst):
    # initialize the tree
    tree = initialize_tree([], lst)

    # yield the permutation of this tree
    yield get_permutation_from_tree(tree)

    # then, while the tree is not 'complete', yield each tree_advance result
    while advance_tree(tree):
        yield get_permutation_from_tree(tree)

    # that's all folks!


def initialize_tree(datum, lst):
    if len(lst) == 0:
        return {
            'datum': datum,
            'child': None,
            'uncomputed': [],
            'original': []
        }

    selected = lst[0]
    uncomputed = [x for x in lst if selected != x]
    child = initialize_tree(datum + [selected], uncomputed)

    return {
        'datum': datum,
        'child': child,
        'uncomputed': uncomputed,
        'original': lst
    }


def find_node_to_advance(tree):
    # reverse the tree
    nodes = [tree]
    while nodes[-1]['child'] is not None:
        nodes.append(nodes[-1]['child'])

    nodes = reversed(nodes)

    # iteratively check each node in order and return the one with uncomputed data
    for edon in nodes:
        if len(edon['uncomputed']) > 0:
            return edon

    return None


def advance_tree(tree):
    # find the bottom-most node who still has data to be computed
    node = find_node_to_advance(tree)

    # while node['child'] is not None and len(node['child']['uncomputed']) > 0:

    # end condition: we have nothing left!
    if node is None:
        return False

    # remove is current child
    del node['child']

    # then set its child to initialize_tree
    # ... and remove from its uncomputed list the value we just... computed!
    datum = node['uncomputed'].pop()
    zx = initialize_tree(node['datum'] + [datum], [z for z in node['original'] if z != datum])
    node['child'] = zx

    return True


def get_permutation_from_tree(tree):
    if tree['child'] is None:
        return tree['datum']

    return get_permutation_from_tree(tree['child'])


if __name__ == '__main__':
    for x in range(0, 13):
        i = 0
        for perm in permutations([z for z in range(0, x)]):
            i += 1
        print(str(x) + ": " + str(i))