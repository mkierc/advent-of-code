import re

test_input_1 = [
    'pbga (66)',
    'xhth (57)',
    'ebii (61)',
    'havc (66)',
    'ktlj (57)',
    'fwft (72) -> ktlj, cntj, xhth',
    'qoyq (66)',
    'padx (45) -> pbga, havc, qoyq',
    'tknk (41) -> ugml, padx, fwft',
    'jptl (61)',
    'ugml (68) -> gyxo, ebii, jptl',
    'gyxo (61)',
    'cntj (57)'
]

with open("data.txt") as file:
    input_data = file.read().split('\n')


class Node(object):
    def __init__(self, children=[], parent=None):
        self.children = frozenset(children)
        self.parent = parent


def find_root(data):
    tree = dict()

    # build tree
    for line in data:
        if re.match('.*->.*', line):
            regex = re.search('([a-z]+) \(\d+\) -> ([a-z, ]+)', line)
            if regex:
                name = regex.group(1)
                children = regex.group(2).split(', ')
                node = Node(children)
                tree.update({name: node})
        else:
            regex = re.search('([a-z]+) \(\d+\)', line)
            if regex:
                name = regex.group(1)
                node = Node()
                tree.update({name: node})

    # update parents
    for node in tree.keys():
        for child in tree.get(node).children:
            c = tree.get(child)
            c.parent = node

    # find root
    for node in tree.keys():
        if tree.get(node).parent:
            pass
        else:
            return node


def main():
    test_1 = find_root(test_input_1)
    answer = find_root(input_data)

    print("test_1:", test_1)
    print("answer:", answer)


if __name__ == "__main__":
    main()
