import heapq
import re
from collections import defaultdict
from itertools import product
from pprint import pprint
from time import time

test_input = '''029A
980A
179A
456A
379A'''

test_codes = test_input.split()

with open('data.txt') as file:
    codes = file.read().split()


def find_all_paths(_from, _to, keypad_map):
    if _from == _to:
        return ['']

    # < v > ^
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    start = keypad_map[_from]
    end = keypad_map[_to]

    # print(_from, _to)
    queue = []
    heapq.heappush(queue, start)

    visited_nodes = defaultdict(set)
    cost_to_node = defaultdict(lambda: 0)

    visited_nodes[start] = set()
    cost_to_node[start] = 0

    while queue:
        (x, y) = heapq.heappop(queue)

        new_moves = []
        for d_x, d_y in directions:
            if (x + d_x, y + d_y) in keypad_map.values():
                new_moves.append((x + d_x, y + d_y, d_x, d_y))

        for n_x, n_y, d_x, d_y in new_moves:
            new_cost = cost_to_node[(x, y)] + 1

            if (n_x, n_y) not in cost_to_node or new_cost < cost_to_node[(n_x, n_y)]:
                cost_to_node[(n_x, n_y)] = new_cost
                heapq.heappush(queue, (n_x, n_y))
                visited_nodes[(n_x, n_y)] = {(x, y)}
            elif new_cost == cost_to_node[(n_x, n_y)]:
                visited_nodes[(n_x, n_y)] = {*visited_nodes[(n_x, n_y)], (x, y)}

    # retrace the steps of all the equally best paths
    backtrace_queue = []
    heapq.heappush(backtrace_queue, [end])

    list_of_paths = []

    while backtrace_queue:
        current = heapq.heappop(backtrace_queue)
        tail = current[-1]

        # we've found a complete path -> save directions as keystrokes
        if tail == start:
            # reverse order
            current = current[::-1]
            keystrokes = ''
            for i in range(len(current) - 1):
                x1, y1 = current[i]
                x2, y2 = current[i + 1]
                if x1 - x2 == -1:
                    keystrokes += '>'
                elif x1 - x2 == 1:
                    keystrokes += '<'
                elif y1 - y2 == -1:
                    keystrokes += '^'
                elif y1 - y2 == 1:
                    keystrokes += 'v'
            list_of_paths.append(keystrokes)

        new_tails = visited_nodes[tail]
        for new_tail in new_tails:
            heapq.heappush(backtrace_queue, [*current, new_tail])

    return list_of_paths


def build_robot_mappings():
    buttons = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A']
    arrows = ['<', '>', '^', 'v', 'A']

    button_combinations = [x for x in product(buttons, buttons)]
    arrow_combinations = [x for x in product(arrows, arrows)]

    keypad_positions = {
        '7': (0, 3), '8': (1, 3), '9': (2, 3),
        '4': (0, 2), '5': (1, 2), '6': (2, 2),
        '1': (0, 1), '2': (1, 1), '3': (2, 1),
        '0': (1, 0), 'A': (2, 0),
    }

    arrow_positions = {
        '^': (1, 1), 'A': (2, 1),
        '<': (0, 0), 'v': (1, 0), '>': (2, 0),
    }

    # arrows_to_arrows = {}
    #
    # for _from, _to in arrow_combinations:
    #     path_list = find_all_paths(_from, _to, arrow_positions)
    #     arrows_to_arrows.update({(_from, _to): path_list})

    arrows_to_arrows = {('<', '<'): [''],
                        ('<', '>'): ['>>'],
                        ('<', 'A'): ['>>^', '>^>'],  # '>>^' = 136_422, '>^>' = 138_798
                        ('<', '^'): ['>^'],
                        ('<', 'v'): ['>'],
                        ('>', '<'): ['<<'],
                        ('>', '>'): [''],
                        ('>', 'A'): ['^'],
                        ('>', '^'): ['<^', '^<'],  # eq 136_422
                        ('>', 'v'): ['<'],
                        ('A', '<'): ['v<<', '<v<'],  # 'v<<' = 132_376, '<v<' = 136_422
                        ('A', '>'): ['v'],
                        ('A', 'A'): [''],
                        ('A', '^'): ['<'],
                        ('A', 'v'): ['<v', 'v<'],  # eq 132_376
                        ('^', '<'): ['v<'],
                        ('^', '>'): ['v>', '>v'],  # eq 132_376
                        ('^', 'A'): ['>'],
                        ('^', '^'): [''],
                        ('^', 'v'): ['v'],
                        ('v', '<'): ['<'],
                        ('v', '>'): ['>'],
                        ('v', 'A'): ['>^', '^>'],  # eq 132_376
                        ('v', '^'): ['^'],
                        ('v', 'v'): ['']}
    pprint(arrows_to_arrows)

    keypad_to_arrows = defaultdict(list)

    for _from, _to in button_combinations:
        path_list = find_all_paths(_from, _to, keypad_positions)

        min_path = 1_000
        for path in path_list:
            double_decoded = decode(decode(path, arrows_to_arrows), arrows_to_arrows)
            # print(decode(path, arrows_to_arrows), len(decode(path, arrows_to_arrows)))
            if len(double_decoded) < min_path:
                min_path = len(double_decoded)

        for path in path_list:
            double_decoded = decode(decode(path, arrows_to_arrows), arrows_to_arrows)
            if len(double_decoded) == min_path:
                keypad_to_arrows.update({(_from, _to): [*keypad_to_arrows[(_from, _to)], path]})

    pprint(keypad_to_arrows)
    pprint(arrows_to_arrows)

    return keypad_to_arrows, arrows_to_arrows


def decode(code, mapping):
    if code == '':
        return ''

    decoded = ''
    decoded += mapping[('A', code[0])][0]
    decoded += 'A'
    for i in range(len(code) - 1):
        decoded += mapping[(code[i], code[i + 1])][0]
        decoded += 'A'

    return decoded


def solve(code_list):
    # keypad_to_arrows = {('0', '0'): '',
    #                     ('0', '1'): '<^',
    #                     ('0', '2'): '^',
    #                     ('0', '3'): '>^',
    #                     ('0', '4'): '<^^',
    #                     ('0', '5'): '^^',
    #                     ('0', '6'): '>^^',
    #                     ('0', '7'): '<^^^',
    #                     ('0', '8'): '^^^',
    #                     ('0', '9'): '>^^^',
    #                     ('0', 'A'): '>',
    #                     ('1', '0'): '>v',
    #                     ('1', '1'): '',
    #                     ('1', '2'): '>',
    #                     ('1', '3'): '>>',
    #                     ('1', '4'): '^',
    #                     ('1', '5'): '>^',
    #                     ('1', '6'): '>>^',
    #                     ('1', '7'): '^^',
    #                     ('1', '8'): '>^^',
    #                     ('1', '9'): '>>^^',
    #                     ('1', 'A'): '>>v',
    #                     ('2', '0'): 'v',
    #                     ('2', '1'): '<',
    #                     ('2', '2'): '',
    #                     ('2', '3'): '>',
    #                     ('2', '4'): '<^',
    #                     ('2', '5'): '^',
    #                     ('2', '6'): '>^',
    #                     ('2', '7'): '<^^',
    #                     ('2', '8'): '^^',
    #                     ('2', '9'): '>^^',
    #                     ('2', 'A'): '>v',
    #                     ('3', '0'): '<v',
    #                     ('3', '1'): '<<',
    #                     ('3', '2'): '<',
    #                     ('3', '3'): '',
    #                     ('3', '4'): '<<^',
    #                     ('3', '5'): '<^',
    #                     ('3', '6'): '^',
    #                     ('3', '7'): '<<^^',
    #                     ('3', '8'): '<^^',
    #                     ('3', '9'): '^^',
    #                     ('3', 'A'): 'v',
    #                     ('4', '0'): '>vv',
    #                     ('4', '1'): 'v',
    #                     ('4', '2'): '>v',
    #                     ('4', '3'): '>>v',
    #                     ('4', '4'): '',
    #                     ('4', '5'): '>',
    #                     ('4', '6'): '>>',
    #                     ('4', '7'): '^',
    #                     ('4', '8'): '>^',
    #                     ('4', '9'): '>>^',
    #                     ('4', 'A'): '>>vv',
    #                     ('5', '0'): 'vv',
    #                     ('5', '1'): '<v',
    #                     ('5', '2'): 'v',
    #                     ('5', '3'): '>v',
    #                     ('5', '4'): '<',
    #                     ('5', '5'): '',
    #                     ('5', '6'): '>',
    #                     ('5', '7'): '<^',
    #                     ('5', '8'): '^',
    #                     ('5', '9'): '>^',
    #                     ('5', 'A'): '>vv',
    #                     ('6', '0'): '<vv',
    #                     ('6', '1'): '<<v',
    #                     ('6', '2'): '<v',
    #                     ('6', '3'): 'v',
    #                     ('6', '4'): '<<',
    #                     ('6', '5'): '<',
    #                     ('6', '6'): '',
    #                     ('6', '7'): '<<^',
    #                     ('6', '8'): '<^',
    #                     ('6', '9'): '^',
    #                     ('6', 'A'): 'vv',
    #                     ('7', '0'): '>vvv',
    #                     ('7', '1'): 'vv',
    #                     ('7', '2'): '>vv',
    #                     ('7', '3'): '>>vv',
    #                     ('7', '4'): 'v',
    #                     ('7', '5'): '>v',
    #                     ('7', '6'): '>>v',
    #                     ('7', '7'): '',
    #                     ('7', '8'): '>',
    #                     ('7', '9'): '>>',
    #                     ('7', 'A'): '>>vvv',
    #                     ('8', '0'): 'vvv',
    #                     ('8', '1'): '<vv',
    #                     ('8', '2'): 'vv',
    #                     ('8', '3'): '>vv',
    #                     ('8', '4'): '<v',
    #                     ('8', '5'): 'v',
    #                     ('8', '6'): '>v',
    #                     ('8', '7'): '<',
    #                     ('8', '8'): '',
    #                     ('8', '9'): '>',
    #                     ('8', 'A'): '>vvv',
    #                     ('9', '0'): '<vvv',
    #                     ('9', '1'): '<<vv',
    #                     ('9', '2'): '<vv',
    #                     ('9', '3'): 'vv',
    #                     ('9', '4'): '<<v',
    #                     ('9', '5'): '<v',
    #                     ('9', '6'): 'v',
    #                     ('9', '7'): '<<',
    #                     ('9', '8'): '<',
    #                     ('9', '9'): '',
    #                     ('9', 'A'): 'vvv',
    #                     ('A', '0'): '<',
    #                     ('A', '1'): '^<<',
    #                     ('A', '2'): '<^',
    #                     ('A', '3'): '^',
    #                     ('A', '4'): '^^<<',
    #                     ('A', '5'): '<^^',
    #                     ('A', '6'): '^^',
    #                     ('A', '7'): '^^^<<',
    #                     ('A', '8'): '<^^^',
    #                     ('A', '9'): '^^^',
    #                     ('A', 'A'): ''}
    # arrows_to_arrows = {('<', '<'): '',
    #                     ('<', '>'): '>>',
    #                     ('<', 'A'): '>>^',
    #                     ('<', '^'): '>^',
    #                     ('<', 'v'): '>',
    #                     ('>', '<'): '<<',
    #                     ('>', '>'): '',
    #                     ('>', 'A'): '^',
    #                     ('>', '^'): '<^',
    #                     ('>', 'v'): '<',
    #                     ('A', '<'): '<v<',
    #                     ('A', '>'): 'v',
    #                     ('A', 'A'): '',
    #                     ('A', '^'): '<',
    #                     ('A', 'v'): '<v',
    #                     ('^', '<'): '<v',
    #                     ('^', '>'): '>v',
    #                     ('^', 'A'): '>',
    #                     ('^', '^'): '',
    #                     ('^', 'v'): 'v',
    #                     ('v', '<'): '<',
    #                     ('v', '>'): '>',
    #                     ('v', 'A'): '>^',
    #                     ('v', '^'): '^',
    #                     ('v', 'v'): ''}

    keypad_to_arrows, arrows_to_arrows = build_robot_mappings()

    complexity_sum = 0

    for code in code_list:
        print(code)
        decoded = decode(code, keypad_to_arrows)
        print(decoded)
        decoded = decode(decoded, arrows_to_arrows)
        print(decoded)
        decoded = decode(decoded, arrows_to_arrows)
        print(decoded)
        complexity = len(decoded)
        numeric_code = int(re.findall(r'(\d+)', code)[0])
        print(complexity, numeric_code, complexity * numeric_code)
        complexity_sum += complexity * numeric_code

    return complexity_sum


def main():
    test_1 = solve(test_codes)
    print('test_1:', test_1)

    start = time()
    answer = solve(codes)
    print('time:', time() - start)
    print('answer:', answer)


if __name__ == '__main__':
    main()
