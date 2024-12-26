import heapq
import re
from collections import defaultdict, deque
from copy import deepcopy
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


def is_cycle(wires):
    """
    Check if the connection map contains a cycle, let quickly exit a test run()
    """
    def recursive(wires, current, visited, rec_stack):
        if current not in visited:
            visited.add(current)
            rec_stack[current] = True

            if current[0] not in ['x', 'y']:
                a, op, b = wires[current]
                if not a in visited and recursive(wires, a, visited, rec_stack):
                    return True
                elif rec_stack[a]:
                    return True

                if not b in visited and recursive(wires, b, visited, rec_stack):
                    return True
                elif rec_stack[b]:
                    return True

        rec_stack[current] = False
        return False

    visited = set()
    rec_stack = dict()

    for k in wires.keys():
        if not k in visited and recursive(wires, k, visited, rec_stack):
            return True

    return False

def run(inputs, wires):
    if is_cycle(wires):
        return -1

    queue = deque()

    for n, k in enumerate(wires.keys()):
        queue.append(k)

    while queue:
        # print(f'\r{len(queue)}, {queue}',end='')
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

    # return int(''.join(([str(v) for k, v in sorted(inputs.items(), reverse=True) if k[0] == 'z'])), base=2)
    return ''.join(([str(v) for k, v in sorted(inputs.items(), reverse=True) if k[0] == 'z']))



def find_bad_gates(inputs, wires):
    input_count = len([x for x in inputs if x[0] == 'x'])
    empty_inputs = {k: 0 for k, v in inputs.items()}

    bad_gate_count = 0

    for i in range(input_count):
        # print(f'{i:02}')
        test_for_x = empty_inputs.copy()
        test_for_y = empty_inputs.copy()

        test_for_x[f'x{i:02}'] = 1
        # print(f'running x{i:02}')
        x_1 = run(test_for_x, wires)
        if x_1 == -1:
            return 1_000
        # print(f'running y{i:02}')
        test_for_y[f'y{i:02}'] = 1
        y_1 = run(test_for_y, wires)
        if y_1 == -1:
            return 1_000

        expected = ['0' for _ in range(input_count + 1)]
        expected[-i - 1] = '1'

        # print(x_1, y_1, ''.join(expected))

        if x_1 != ''.join(expected):
            # print(f"{x_1=}\nz_1='{''.join(expected)}'")
            # print(f'x{i:02} is wrong')
            bad_gate_count += 1
        if y_1 != ''.join(expected):
            # print(f"{y_1=}\nz_1='{''.join(expected)}'")
            # print(f'y{i:02} is wrong')
            bad_gate_count += 1

    return bad_gate_count


def calculate_error(inputs, wires):
    swapped = defaultdict(set)

    edges_of_paths = []

    for _input in inputs:
        if _input[0] == 'x':
            edges_of_paths.append((f'z{_input[1:]}', _input))

    print(edges_of_paths)

    for start, end in edges_of_paths:
        queue = []
        heapq.heappush(queue, (0, start))

        visited_nodes = defaultdict(str)
        cost_to_node = defaultdict(int)

        visited_nodes[start] = None
        cost_to_node[start] = 0

        while queue:
            current = heapq.heappop(queue)[1]

            if current == end:
                path = []
                retrace_current = current

                # while visited_nodes[current]:
                #     retrace_current = visited_nodes[retrace_current]
                break
            if current[0] not in ['x', 'y']:
                a, _, b = wires[current]
                print(current, a, b)

                new_nodes = [a,b]
                new_cost = cost_to_node[current] + 1

                for node in new_nodes:
                    if node not in cost_to_node or new_cost < cost_to_node[node]:
                        cost_to_node[node] = new_cost
                        priority = new_cost
                        heapq.heappush(queue, (priority, node))
                        visited_nodes[node] = current

        print(visited_nodes)

    for k, v in wires.items():
        iters = 0
        if k[0] == 'z':
            seen_states = set()
            # print(f'{k=}')
            queue = deque()
            queue.append(k)

            while queue:
                # loop safety
                iters += 1
                if iters > 2000:
                    return 1000000000
                # print(f'{len(swapped)=}')
                # print(f'{len(queue)=}')

                current = queue.popleft()
                a, _, b = wires[current]

                if a[0] in ['x', 'y'] and b[0] in ['x', 'y']:
                    swapped.update({k: {*swapped[k], (a, b)}})
                else:
                    queue.append(a)
                    queue.append(b)

    # print(swapped)
    error = sum([len(x) for x in swapped.items()])
    return error


def swap(a, b, wires):
    swapped_wires = deepcopy(wires)
    swapped_wires[a] = wires[b]
    swapped_wires[b] = wires[a]
    return swapped_wires


def find_swapped_wires(inputs, wires):
    base_bad_gates_count = find_bad_gates(inputs, wires)

    queue = deque()

    for k in wires.keys():
        queue.append(k)

    swapped_pairs = []

    while queue:
        # print(f'{queue=}')
        a = queue.popleft()
        print(f'\rrunning swaps for {a} ({len(queue)} left)...')

        for i, b in enumerate(queue):
            print(f'\r {len(queue)-i-1} left...', end='')

            # print(f'{a=}, {b=}')
            swapped = swap(a, b, wires)

            bad_gates = find_bad_gates(inputs, swapped)
            if bad_gates < base_bad_gates_count:
                swapped_pairs.append((a, b))

    return swapped_pairs


def main():
    start = time()
    answer = find_swapped_wires(inputs, wires)
    print('answer:', answer)
    print('time:', time() - start)


if __name__ == '__main__':
    main()


# TODO: second approach to swapping wires method, slow as hell and calculate_error() still creates false positives...

# answer: [('kgn', 'ctv'), ('jds', 'z39'), ('gms', 'bkr'), ('vst', 'z28'), ('ctv', 'vvr'), ('rnq', 'bkr'),
# ('z39', 'mqh'), ('z08', 'vvr'), ('pvv', 'bkr'), ('tfb', 'z28'), ('z16', 'kbg'), ('z16', 'bkr'), ('kwv', 'vvr'),
# ('bkr', 'ngf'), ('ptk', 'z28')]
# 729.9781947135925 s
