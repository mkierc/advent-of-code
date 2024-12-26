import heapq
import re
from collections import defaultdict, deque
from copy import deepcopy
from itertools import combinations
from time import time

inputs = {}
wires = {}

with open('data.txt') as file:
# with open('fixed_data.txt') as file:
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
    """
    Runs a logic circuit simulation
    """
    if is_cycle(wires):
        # print('cycle!')
        return inputs

    new_inputs = inputs.copy()
    queue = deque()

    for n, k in enumerate(wires.keys()):
        queue.append(k)

    while queue:
        # print(queue)
        current = queue.popleft()
        wire_1, op, wire_2 = wires[current]
        if wire_1 in new_inputs and wire_2 in new_inputs:
            value_1 = new_inputs[wire_1]
            value_2 = new_inputs[wire_2]
            if op == 'AND':
                new_inputs.update({current: value_1 & value_2})
            if op == 'OR':
                new_inputs.update({current: value_1 or value_2})
            if op == 'XOR':
                new_inputs.update({current: value_1 ^ value_2})
        else:
            queue.append(current)

    # return int(''.join(([str(v) for k, v in sorted(inputs.items(), reverse=True) if k[0] == 'z'])), base=2)
    return ''.join(([str(v) for k, v in sorted(new_inputs.items(), reverse=True) if k[0] == 'z']))


def find_bad_inputs(inputs, wires):
    """
    Test the adder circuit for mismatched I/O, by running series of additions for zero plus consecutive powers of 2

    TODO: find a better way to test for bad inputs, this one creates a lot of false positives in some swaps...
    """
    input_count = len([x for x in inputs if x[0] == 'x'])
    empty_inputs = {k: 0 for k, v in inputs.items()}

    bad_gates = []

    for i in range(input_count):
        # print(f'{i:02}')
        test_for_x = empty_inputs.copy()
        test_for_y = empty_inputs.copy()

        test_for_x[f'x{i:02}'] = 1
        x_1 = run(test_for_x, wires)
        test_for_y[f'y{i:02}'] = 1
        y_1 = run(test_for_y, wires)

        expected = ['0' for _ in range(input_count + 1)]
        expected[-i - 1] = '1'

        if x_1 != ''.join(expected):
            # print(f"{x_1=}\nz_1='{''.join(expected)}'")
            # print(f'x{i:02} is wrong')
            bad_gates.append(f'x{i:02}')
        if y_1 != ''.join(expected):
            # print(f"{y_1=}\nz_1='{''.join(expected)}'")
            # print(f'y{i:02} is wrong')
            bad_gates.append(f'y{i:02}')

    return bad_gates


def find_connected_gates(wires, output, debug=False):
    """
    Return a flat list of wires connecting to the output,
    with a possibility of printing the connections level by level with the debug flag
    """
    queue = []
    heapq.heappush(queue, (0, output))

    visited_nodes = defaultdict(str)
    cost_to_node = defaultdict(lambda: 1_000)

    visited_nodes[output] = None
    cost_to_node[output] = 0

    level_map = {output: 0}
    flat_connections = set()

    while queue:
        current = heapq.heappop(queue)[1]

        if current[0] in ['x', 'y']:
            break

        a, _, b = wires[current]
        new_cost = cost_to_node[current] + 1

        level = level_map[current]
        level_map.update({a: level + 1})
        level_map.update({b: level + 1})
        flat_connections.add(current)
        flat_connections.add(a)
        flat_connections.add(b)

        if a not in cost_to_node or new_cost < cost_to_node[a]:
            cost_to_node[a] = new_cost
            heapq.heappush(queue, (new_cost, a))
            visited_nodes[a] = current

        if b not in cost_to_node or new_cost < cost_to_node[b]:
            cost_to_node[b] = new_cost
            heapq.heappush(queue, (new_cost, b))
            visited_nodes[b] = current

    if debug:
        for i in range(max(level_map.values())+1):
            print(sorted([k for k, v in level_map.items() if v == i]))

    return sorted(flat_connections)


def find_all_connections(wires, debug=False):
    paths = {}
    for n in range(44):
        path = find_connected_gates(wires, f'z{n:02}', debug)
        paths.update({f'z{n:02}': path})
    return paths


def swap(a, b, wires):
    swapped_wires = deepcopy(wires)
    swapped_wires[a] = wires[b]
    swapped_wires[b] = wires[a]
    return swapped_wires


def solve(inputs, wires):
    real_swaps = []

    # find all inputs that don't generate correct outputs
    bad_inputs = find_bad_inputs(inputs, wires)
    # print(bad_inputs)
    found_a_swap = False
    while len(bad_inputs) > 0:
        if found_a_swap:
            print(real_swaps)
            bad_inputs = find_bad_inputs(inputs, wires)
            potential_gates_to_swap = find_all_connections(wires, debug=True)
            print(potential_gates_to_swap)
            break

        # find all inputs that don't generate correct outputs
        bad_inputs = find_bad_inputs(inputs, wires)
        # print(bad_inputs)

        # find gates that those inputs connect to
        potential_gates_to_swap = find_all_connections(wires)
        # print(potential_gates_to_swap)

        gates_to_switch = set()

        for output, connections in potential_gates_to_swap.items():
            for connection in connections:
                if connection in bad_inputs:
                    gates_to_switch.update(connections)

        # prune x_N / y_N - we don't switch inputs to gates
        gates_to_switch = [x for x in gates_to_switch if x[0] not in ['x', 'y']]

        for a, b in sorted(combinations(gates_to_switch, 2)):
            # print(a, b)
            swapped = swap(a, b, wires)
            new_bad_inputs = find_bad_inputs(inputs, swapped)

            if len(new_bad_inputs) < len(bad_inputs):
                bad_inputs = new_bad_inputs
                print(f'swap found! {a} <-> {b}')
                real_swaps.append((a, b))
                wires = swapped
                found_a_swap = True
                break

    return real_swaps


def main():
    bad_inputs = find_bad_inputs(inputs, wires)
    print(bad_inputs)
    find_all_connections(wires, debug=True)

    # start = time()
    # answer = solve(inputs, wires)
    # print('answer:', answer)
    # print('time:', time() - start)


if __name__ == '__main__':
    main()

#  1. find_bad_inputs() -> tells me which inputs are giving wrong outputs, and lets me test the circuit
#  2. find_all_connections() -> outputs levels of connections, can be used to find patterns (candidates for swapping)
#
#  correct setup (apart from first two input pairs x00, y00 and x01, y01 should look like this:
#    level 0 - z_N
#    level 1 - two gates
#    level 2 - two different gates than level 1 + x_N, y_N
#    level 3 - same two gates as level 1 + x_N-1, y_N-1
#
# TODO: automate the algo to find the bad gates:
#  3. solve() -> after 1. try swappping the candidates from 2.
#  at this point it does it randomly (not very efficient...), and the find_bad_inputs() is ofter causing false-positives
#
# TODO: another idea is to remove gates from "bad_inputs" that are present in "good inputs" to prune a little more

# ('bkr', 'rnq'), ('z39', 'mqh'), ('z08', 'vvr'), ('z28', 'tfb')
# anwer:   bkr,mqh,rnq,tfb,vvr,z08,z28,z39