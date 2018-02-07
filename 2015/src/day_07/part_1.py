import re
from collections import defaultdict, deque

test_input_1 = [
    '123 -> x',
    '456 -> y',
    'x AND y -> d',
    'x OR y -> e',
    'x LSHIFT 2 -> f',
    'y RSHIFT 2 -> g',
    'NOT x -> h',
    'NOT y -> i'
]

LIMIT = 65535

with open('data.txt') as file:
    input_data = file.read().splitlines()


def solve(instructions):
    wires = defaultdict(str)
    instruction_queue = deque(instructions)

    # TODO: refactor the ifs to reduce code repetition
    while instruction_queue:
        instruction = instruction_queue.popleft()
        if 'AND' in instruction:
            a, b, c = re.search(r'([a-z0-9]+) AND ([a-z0-9]+) -> ([a-z0-9]+)', instruction).groups()

            if a.isalpha():
                a = wires[a]
            else:
                a = int(a)

            if b.isalpha():
                b = wires[b]
            else:
                b = int(b)

            if a == '' or b == '':
                wires[c] = ''
                instruction_queue.append(instruction)
                continue

            wires[c] = (a & LIMIT) & (b & LIMIT)

        elif 'OR' in instruction:
            a, b, c = re.search(r'([a-z0-9]+) OR ([a-z0-9]+) -> ([a-z0-9]+)', instruction).groups()

            if a.isalpha():
                a = wires[a]
            else:
                a = int(a)

            if b.isalpha():
                b = wires[b]
            else:
                b = int(b)

            if a == '' or b == '':
                wires[c] = ''
                instruction_queue.append(instruction)
                continue

            wires[c] = (a & LIMIT) | (b & LIMIT)

        elif 'LSHIFT' in instruction:
            a, b, c = re.search(r'([a-z0-9]+) LSHIFT ([a-z0-9]+) -> ([a-z0-9]+)', instruction).groups()

            if a.isalpha():
                a = wires[a]
            else:
                a = int(a)

            if b.isalpha():
                b = wires[b]
            else:
                b = int(b)

            if a == '' or b == '':
                wires[c] = ''
                instruction_queue.append(instruction)
                continue

            wires[c] = (a & LIMIT) << (b & LIMIT)

        elif 'RSHIFT' in instruction:
            a, b, c = re.search(r'([a-z0-9]+) RSHIFT ([a-z0-9]+) -> ([a-z0-9]+)', instruction).groups()

            if a.isalpha():
                a = wires[a]
            else:
                a = int(a)

            if b.isalpha():
                b = wires[b]
            else:
                b = int(b)

            if a == '' or b == '':
                wires[c] = ''
                instruction_queue.append(instruction)
                continue

            wires[c] = (a & LIMIT) >> (b & LIMIT)

        elif 'NOT' in instruction:
            a, b = re.search(r'([a-z0-9]+) -> ([a-z0-9]+)', instruction).groups()

            if a.isalpha():
                a = wires[a]
            else:
                a = int(a)

            if a == '':
                wires[b] = ''
                instruction_queue.append(instruction)
                continue

            wires[b] = ~a & LIMIT

        else:
            a, b = re.search(r'([a-z0-9]+) -> ([a-z0-9]+)', instruction).groups()

            if a.isalpha():
                a = wires[a]
            else:
                a = int(a)

            if a == '':
                wires[b] = ''
                instruction_queue.append(instruction)
                continue

            wires[b] = a

    return wires


def main():
    test_1 = solve(test_input_1)
    test_1_formatted = '\n'.join([str(x) + ': ' + str(y) for x, y, in sorted(test_1.items())])
    print('test_1:', test_1_formatted)

    answer = solve(input_data)['a']
    print('answer:', answer)


if __name__ == '__main__':
    main()
