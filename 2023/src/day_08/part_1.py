import itertools
import re

test_input_1 = '''RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
'''

test_input_2 = '''LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
'''

camel_map = ''

with open("data.txt") as file:
    for _line in file.readlines():
        camel_map += _line


def follow_steps(_map):
    directions = itertools.cycle(_map.split('\n')[0])
    nodes = dict()

    for line in _map.split('\n'):
        _node_regex = re.fullmatch(r'([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)', line)
        if _node_regex:
            nodes[_node_regex[1]] = (_node_regex[2], _node_regex[3])

    counter = 0
    current = 'AAA'

    while True:
        dir = next(directions)
        if dir == 'L':
            current = nodes[current][0]
        elif dir == 'R':
            current = nodes[current][1]

        counter += 1
        if current == 'ZZZ':
            return counter


def main():
    test_1 = follow_steps(test_input_1)
    print("test_1:", test_1)

    test_2 = follow_steps(test_input_2)
    print("test_2:", test_2)

    answer = follow_steps(camel_map)
    print("answer:", answer)


if __name__ == "__main__":
    main()
