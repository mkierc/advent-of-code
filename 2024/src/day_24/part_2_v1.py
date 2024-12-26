import heapq
import re
from collections import defaultdict, deque, Counter
from copy import deepcopy
from pprint import pprint
from time import time

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


def calculate_error(wires):
    from_back = defaultdict(set)

    transposed = {}

    for k, v in wires.items():
        if k[0] == 'z':
            # print(f'{k=}')
            queue = deque()
            queue.append(k)

            while queue:
                # print(f'{len(swapped)=}')
                # print(f'{len(queue)=}')

                current = queue.popleft()
                a, _, b = wires[current]

                if not a[0] in ['x', 'y']:
                    queue.append(a)
                    from_back.update({k: {*from_back[k], a}})
                if not b[0] in ['x', 'y']:
                    queue.append(b)
                    from_back.update({k: {*from_back[k], b}})

        transposed.update({v[0]: k})
        transposed.update({v[2]: k})

    # print(transposed)
    # exit()

    from_front = defaultdict(set)

    for k, v in transposed.items():
        if k[0] in ['x', 'y']:
            queue = deque()
            queue.append(k)

            while queue:
                # print(f'{queue=}')
                current = queue.popleft()
                v = transposed[current]

                if not v[0] == 'z':
                    queue.append(v)
                from_front.update({k: {*from_front[k], v}})

    # print(from_front)
    # print(from_back)

    good_set = set()
    for i, (k, v) in enumerate(from_back.items()):
        front_set = from_front[f'x{i:02}']
        back_set = v

        # good_set.update(front_set.difference(back_set))
        print(i, front_set.symmetric_difference(back_set))
    # print(good_set)

    # print(set(wires)-good_set)
    return 0


def swap(a, b, wires):
    swapped_wires = deepcopy(wires)
    swapped_wires[a] = wires[b]
    swapped_wires[b] = wires[a]
    return swapped_wires


def find_swapped_wires(wires):
    base_error = calculate_error(wires)
    print(base_error)
    exit()

    queue = deque()
    for k in wires.keys():
        if k[0] != 'z':
            queue.append(k)

    swapped_pairs = []

    while queue:
        # print(f'{queue=}')
        a = queue.popleft()
        for b in queue:
            # print(f'{a=}, {b=}')
            swapped = swap(a, b, wires)
            swapped_error = calculate_error(swapped)
            print(swapped_error, base_error)
            if swapped_error < base_error:
                base_error = swapped_error
                swapped_pairs.append(a)
                swapped_pairs.append(b)
                wires = swapped

    print(swapped_pairs)


def main():
    start = time()
    answer = find_swapped_wires(wires)
    print('answer:', answer)
    print('time:', time() - start)


if __name__ == '__main__':
    main()

# TODO: initial approach to swapping wires method, but the calculate_error() is a pretty crap metric of correctness...
