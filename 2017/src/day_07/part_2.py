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
    def __init__(self, weight, children=[], parent=None):
        self.children = frozenset(children)
        self.weight = weight
        self.parent = parent
        self.total_weight = None

    def __repr__(self):
        if self.parent:
            return "par: " + self.parent + ", ch: " + str(set(self.children)) + ", wg: " + str(self.weight) + ", tot: " + str(self.total_weight)
        else:
            return "ch: " + str(set(self.children)) + ", wg: " + str(self.weight) + ", tot: " + str(self.total_weight)


def find_the_culprit(tree, node):
    # are all children balanced?
    children = tree.get(node).children
    children_weights = [tree.get(child).total_weight for child in children]
    are_children_balanced = len(set(children_weights)) <= 1

    if are_children_balanced:
        # get total weights of siblings or current node
        siblings = tree.get(tree.get(node).parent).children
        siblings_weights = [tree.get(sibling).total_weight for sibling in siblings]

        # get the difference of total weights between balanced and unbalanced
        correct_total_weight = max(set(siblings_weights), key=siblings_weights.count)
        current_total_weight = tree.get(node).total_weight
        difference = correct_total_weight - current_total_weight
        return node + ' weighs ' + str(tree.get(node).weight) + ', but is should weigh ' + str(tree.get(node).weight + difference)
    else:
        return find_the_culprit(tree, get_the_odd_one_out(tree, children))


def get_the_odd_one_out(tree, nodes):
    node_weights = dict()
    for node in nodes:
        current_weight = tree.get(node).total_weight
        if current_weight in node_weights:
            node_weights.update({current_weight: node_weights.get(current_weight) + 1})
        else:
            node_weights.update({current_weight: 1})

    for node in nodes:
        if tree.get(node).total_weight == min(node_weights, key=node_weights.get):
            return node


def update_weights(tree, node):
    current_node = tree.get(node)

    if current_node.total_weight:
        return current_node.total_weight

    total_weight = current_node.weight

    if current_node.children:
        for child in tree.get(node).children:
            child_weight = update_weights(tree, child)
            total_weight += child_weight
        current_node.total_weight = total_weight
        tree.update({node: current_node})
        return total_weight
    else:
        current_node.total_weight = total_weight
        return total_weight


def build_tree(data):
    tree = dict()

    # build tree
    for line in data:
        if re.match('.*->.*', line):
            plok = re.search('([a-z]+) \((\d+)\) -> ([a-z, ]+)', line)
            if plok:
                name = plok.group(1)
                weight = int(plok.group(2))
                children = plok.group(3).split(', ')
                node = Node(weight, children)
        else:
            plok = re.search('([a-z]+) \((\d+)\)', line)
            if plok:
                name = plok.group(1)
                weight = int(plok.group(2))
                node = Node(weight)

        tree.update({name: node})

    # update parents
    for node in tree.keys():
        for child in tree.get(node).children:
            c = tree.get(child)
            c.parent = node

    # find root
    root = None
    for node in tree.keys():
        if tree.get(node).parent:
            pass
        else:
            root = node

    # update total weights
    update_weights(tree, root)

    # find
    unbalanced = find_the_culprit(tree, root)
    return unbalanced


def main():
    test_1 = build_tree(test_input_1)
    answer = build_tree(input_data)

    print("test_1:", test_1)
    print("answer:", answer)


if __name__ == "__main__":
    main()