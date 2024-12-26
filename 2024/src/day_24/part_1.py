import heapq
import re
from collections import defaultdict, deque
from time import time

test_inputs = {
    'x00': 1,
    'x01': 1,
    'x02': 1,
    'y00': 0,
    'y01': 1,
    'y02': 0,
}

test_wires = {
    'z00': ['x00', 'AND', 'y00'],
    'z01': ['x01', 'XOR', 'y01'],
    'z02': ['x02', 'OR', 'y02'],
}

inputs = {}
wires = {}

with open('data.txt') as file:
    a, b = file.read().split('\n\n')

    for _ in a.splitlines():
        i, v = re.findall(r'([a-z0-9]+): ([01])', _)[0]
        inputs.update({i: int(v)})
    for _ in b.splitlines():
        a, o, b, r = re.findall(r'([a-z0-9]+) ([A-Z]+) ([a-z0-9]+) -> ([a-z0-9]+)', _)[0]
        wires.update({r: [a, o, b]})


def run(inputs, wires):
    queue = deque()

    for n, k in enumerate(wires.keys()):
        queue.append(k)

    while queue:
        current = queue.popleft()
        wire_1, op, wire_2 = wires[current]
        if wire_1 in inputs and wire_2 in inputs:
            value_1 = inputs[wire_1]
            value_2 = inputs[wire_2]
            if op == 'AND':
                inputs.update({current: value_1 & value_2})
            if op == 'OR':
                inputs.update({current: value_1 or value_2})
            if op == 'XOR':
                inputs.update({current: value_1 ^ value_2})
        else:
            queue.append(current)

    return int(''.join(([str(v) for k, v in sorted(inputs.items(), reverse=True) if k[0] == 'z'])), base=2)


def main():
    test_1 = run(test_inputs, test_wires)
    print('test_1:', test_1)

    start = time()
    answer = run(inputs, wires)
    print('answer:', answer)
    print('time:', time() - start)


if __name__ == '__main__':
    main()
