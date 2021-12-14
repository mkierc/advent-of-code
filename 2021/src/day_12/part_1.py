import re
from collections import defaultdict

test_input_1 = [
    ('start', 'A'),
    ('start', 'b'),
    ('A', 'c'),
    ('A', 'b'),
    ('b', 'd'),
    ('A', 'end'),
    ('b', 'end'),
]
test_input_2 = [
    ('dc', 'end'),
    ('HN', 'start'),
    ('start', 'kj'),
    ('dc', 'start'),
    ('dc', 'HN'),
    ('LN', 'dc'),
    ('HN', 'end'),
    ('kj', 'sa'),
    ('kj', 'HN'),
    ('kj', 'dc'),
]
test_input_3 = [
    ('fs', 'end'),
    ('he', 'DX'),
    ('fs', 'he'),
    ('start', 'DX'),
    ('pj', 'DX'),
    ('end', 'zg'),
    ('zg', 'sl'),
    ('zg', 'pj'),
    ('pj', 'he'),
    ('RW', 'he'),
    ('fs', 'DX'),
    ('pj', 'RW'),
    ('zg', 'RW'),
    ('start', 'pj'),
    ('he', 'WI'),
    ('zg', 'he'),
    ('pj', 'fs'),
    ('start', 'RW'),
]

connection_regex = re.compile(r'(.*)-(.*)')
input_data = set()

with open("data.txt") as file:
    for line in file.read().splitlines():
        _from, _to = re.findall(connection_regex, line)[0]
        input_data.add((_to, _from))


def find_paths(_connections):
    # create dictionary for efficiency
    edges = defaultdict(set)
    for _from, _to in _connections:
        # connections are always two-way
        edges[_from].add(_to)
        edges[_to].add(_from)

    paths = set()

    queue = [('start',)]
    while queue:
        current = queue.pop()
        if current[-1] != 'end':
            open_end = current[-1]
            for edge in edges[open_end]:
                if edge.isupper() or edge not in current:
                    new_path = (*current, edge)
                    queue.append(new_path)
        else:
            paths.add(current)

    return len(paths)


def main():
    test_1 = find_paths(test_input_1)
    print("test_1:", test_1)
    test_2 = find_paths(test_input_2)
    print("test_2:", test_2)
    test_3 = find_paths(test_input_3)
    print("test_3:", test_3)

    answer = find_paths(input_data)
    print("answer:", answer)


if __name__ == "__main__":
    main()
