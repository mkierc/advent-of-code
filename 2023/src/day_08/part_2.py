import itertools
import math
import re

test_input = '''LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
'''

camel_map = ''

with open("data.txt") as file:
    for _line in file.readlines():
        camel_map += _line


def follow_steps(_map):
    directions = itertools.cycle(_map.split('\n')[0])
    nodes = dict()

    for line in _map.split('\n'):
        _node_regex = re.fullmatch(r'([A-Z0-9]{3}) = \(([A-Z0-9]{3}), ([A-Z0-9]{3})\)', line)
        if _node_regex:
            nodes[_node_regex[1]] = (_node_regex[2], _node_regex[3])

    counter = 0
    current = []

    for key in nodes.keys():
        if key[-1] == 'A':
            current.append(key)

    # because each of the paths is cycling after a certain amount of steps, we need to find their respective cycle count
    multi_counter = [0 for x in current]

    while True:
        dir = next(directions)
        if dir == 'L':
            for i, node in enumerate(current):
                current[i] = nodes[node][0]
        elif dir == 'R':
            for i, node in enumerate(current):
                current[i] = nodes[node][1]

        counter += 1
        # count each time one of the path cycles
        if 'Z' in [x[-1] for x in current]:
            for i, x in enumerate(current):
                if x[-1] == 'Z':
                    multi_counter[i] = counter - multi_counter[i]
            print(multi_counter)

        # if every cycle is found, return their least common multiple
        if 0 not in multi_counter:
            return math.lcm(*multi_counter)


def main():
    test = follow_steps(test_input)
    print("test:", test)

    answer = follow_steps(camel_map)
    print("answer:", answer)


if __name__ == "__main__":
    main()
