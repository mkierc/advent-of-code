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


class Path:  # "classpath", get it?
    def __init__(self, caves, visited_small_cave):
        self.caves = caves
        self.visited_small_cave = visited_small_cave

    def __eq__(self, other):
        if not isinstance(other, Path):
            return NotImplemented

        return (self.caves == other.caves and
                self.visited_small_cave == other.visited_small_cave)


def find_paths_2(_connections):
    # create dictionary for efficiency
    edges = defaultdict(set)
    for _from, _to in _connections:
        # connections are always two-way
        edges[_from].add(_to)
        edges[_to].add(_from)

    paths = set()

    queue = [Path(('start',), False)]
    while queue:
        current = queue.pop()
        if current.caves[-1] != 'end':
            open_end = current.caves[-1]
            # don't visit start twice
            for edge in edges[open_end] - {'start'}:
                # big cave
                if edge.isupper():
                    queue.append(Path((*current.caves, edge), current.visited_small_cave))
                # small cave visited first time
                elif edge not in current.caves:
                    queue.append(Path((*current.caves, edge), current.visited_small_cave))
                # small cave visited second time
                elif current.visited_small_cave is False and current.caves.count(edge) == 1:
                    queue.append(Path((*current.caves, edge), True))
        else:
            paths.add(current.caves)

    return len(paths)


def main():
    test_1 = find_paths_2(test_input_1)
    print("test_1:", test_1)
    test_2 = find_paths_2(test_input_2)
    print("test_2:", test_2)
    test_3 = find_paths_2(test_input_3)
    print("test_3:", test_3)

    answer = find_paths_2(input_data)
    print("answer:", answer)


if __name__ == "__main__":
    main()
